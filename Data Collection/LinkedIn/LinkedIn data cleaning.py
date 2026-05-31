'''
LinkedIn Data Cleaner
--------------------
This script cleans and filters the LinkedIn scrapes. First, companies with fewer posts than 10 total get removed, then:
- For classification: posts with a word count fewer than 3 get removed
- For readability analysis: trailing and leading hashtags, and posts with a sentence count fewer than 2 get removed
'''

import csv
import os
import re
import statistics
from collections import Counter, defaultdict

# ==========================================
# CONFIGURATION SECTION
# ==========================================

INPUT_DIR = "c:/Users/kover/OneDrive/Documenten/School/25-26_sem2/Masterproef/proces 3/Data Collection/LinkedIn"
INPUT_FILE = "LinkedIn 2025-26 Dataset.csv"
OUTPUT_DIR = "."
CLASSIFICATION_FILE = "LinkedIn 2025-26 Dataset - clsf.csv"
READABILITY_FILE = "LinkedIn 2025-26 Dataset - rdbl.csv"

# Thresholds for filtering
MIN_WORD_COUNT = 5
MIN_SENTENCE_COUNT = 3
MIN_POSTS_PER_COMPANY = 10

# ==========================================
# MAIN SCRIPT
# ==========================================

def clean_text_for_readability(text):
    """Removes hashtags only at the start and end of the string."""
    text = re.sub(r'^(\s*#\w+)+', '', text).strip()
    text = re.sub(r'(\s*#\w+)+\s*$', '', text).strip()
    return text

def count_sentences(text):
    """Estimates sentence count based on punctuation (. ! ?)."""
    if not text.strip(): return 0
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    return max(len(sentences), 1)

def get_clean_row(row):
    """Normalizes dictionary keys by stripping whitespace to prevent KeyErrors."""
    return {k.strip(): v for k, v in row.items() if k is not None}

def process_linkedin_data():
    input_path = os.path.join(INPUT_DIR, INPUT_FILE)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Storage for filtering
    clsf_by_company = defaultdict(list)
    read_by_company = defaultdict(list)
    
    # Lists for raw statistics
    raw_word_counts = []
    raw_sentence_counts = []
    company_post_tally = Counter()

    try:
        # 'utf-8-sig' handles Excel BOM markers
        with open(input_path, mode='r', encoding='utf-8-sig') as infile:
            sample = infile.read(2048)
            infile.seek(0)
            dialect = csv.Sniffer().sniff(sample)
            reader = csv.DictReader(infile, dialect=dialect)
            
            for row in reader:
                r = get_clean_row(row)
                comp = r.get('Company Name', 'Unknown')
                text = r.get('Text', '')
                
                # Update Raw Statistics data
                company_post_tally[comp] += 1
                w_count = len(text.split())
                s_count = count_sentences(text)
                
                raw_word_counts.append(w_count)
                raw_sentence_counts.append(s_count)

                # Classification Filter Logic
                if w_count >= MIN_WORD_COUNT:
                    new_row = r.copy()
                    new_row['word_count'] = w_count
                    clsf_by_company[comp].append(new_row)

                # Readability Filter Logic
                cleaned_text = clean_text_for_readability(text)
                final_s_count = count_sentences(cleaned_text)
                if final_s_count >= MIN_SENTENCE_COUNT:
                    new_row = r.copy()
                    new_row['Text'] = cleaned_text
                    new_row['sentence_count'] = final_s_count
                    read_by_company[comp].append(new_row)

    except Exception as e:
        print(f"Error processing file: {e}")
        return

    # Synchronization Logic: Company must have 10+ posts in BOTH filtered sets
    valid_clsf_comps = {c for c, posts in clsf_by_company.items() if len(posts) >= MIN_POSTS_PER_COMPANY}
    valid_read_comps = {c for c, posts in read_by_company.items() if len(posts) >= MIN_POSTS_PER_COMPANY}
    
    final_shared_companies = valid_clsf_comps.intersection(valid_read_comps)

    # Flatten dictionaries into final output lists
    final_clsf_data = [p for c in final_shared_companies for p in clsf_by_company[c]]
    final_read_data = [p for c in final_shared_companies for p in read_by_company[c]]

    # Save Output Files
    save_csv(os.path.join(OUTPUT_DIR, CLASSIFICATION_FILE), final_clsf_data)
    save_csv(os.path.join(OUTPUT_DIR, READABILITY_FILE), final_read_data)

    # Print Detailed Statistics
    print_descriptives(
        company_post_tally, raw_word_counts, raw_sentence_counts,
        valid_clsf_comps, valid_read_comps, final_shared_companies,
        final_clsf_data, final_read_data
    )

def save_csv(path, data):
    if not data: return
    with open(path, mode='w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def print_descriptives(comp_tally, words, sents, c_clsf, c_read, c_final, data_clsf, data_read):
    post_counts = list(comp_tally.values())
    total_posts = len(words)
    total_comps = len(comp_tally)

    print("\n" + "="*60)
    print("📊 DESCRIPTIVES (RAW DATA)")
    print("="*60)
    
    print(f"Total Posts: {total_posts} | Total Companies: {total_comps}")
    
    print("\n--- Company Post Distribution ---")
    print(f"Mean:   {statistics.mean(post_counts):.2f}")
    print(f"Median: {statistics.median(post_counts):.2f}")
    print(f"Min:    {min(post_counts)}")
    print(f"Max:    {max(post_counts)}")
    print(f"StDev:  {statistics.stdev(post_counts):.2f}")

    print("\n--- Word Count Distribution ---")
    print(f"Mean:   {statistics.mean(words):.2f}")
    print(f"Median: {statistics.median(words):.2f}")
    print(f"Min:    {min(words)}")
    print(f"Max:    {max(words)}")
    print(f"StDev:  {statistics.stdev(words):.2f}")

    print("\n--- Sentence Count Distribution ---")
    print(f"Mean:   {statistics.mean(sents):.2f}")
    print(f"Median: {statistics.median(sents):.2f}")
    print(f"Min:    {min(sents)}")
    print(f"Max:    {max(sents)}")
    print(f"StDev:  {statistics.stdev(sents):.2f}")

    print("\n" + "-"*60)
    print("🔍 FILTER & SYNCHRONIZATION RESULTS")
    print("-"*60)
    print(f"Companies with {MIN_POSTS_PER_COMPANY}+ posts (Clsf Set):  {len(c_clsf)}")
    print(f"Companies with {MIN_POSTS_PER_COMPANY}+ posts (Read Set):  {len(c_read)}")
    print(f"Final Synchronized Unique Companies:         {len(c_final)}")
    print(f"Total Companies Removed:                     {total_comps - len(c_final)}")
    print(f"\nFinal Rows in {CLASSIFICATION_FILE}: {len(data_clsf)}")
    print(f"Final Rows in {READABILITY_FILE}:    {len(data_read)}")
    print("="*60)

if __name__ == "__main__":
    process_linkedin_data()