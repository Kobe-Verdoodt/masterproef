'''
GROUND TRUTH ANNOTATION SCRIPT
------------------------------
Script to efficiently annotate the LinkedIn posts for the ground truth dataset.
To run this script use these cmd prompts (change it to fit your directory):

cd C:**FILE DIRECTORY**
streamlit run "Ground truth annotation.py"
'''

import streamlit as st
import pandas as pd
import os
import re

# --- CONFIGURATION ---
APP_MODE = ["CLSF", "RDBL"][1]  # Choose the mode for analyzing the posts

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directories
INPUT_DIR = os.path.abspath(os.path.join(BASE_DIR, "./Samples"))
OUTPUT_DIR = os.path.abspath(os.path.join(BASE_DIR, "./Annotations"))
CONFIG_DIR_CLSF = os.path.abspath(os.path.join(BASE_DIR, "../LLM Analyses/Classification")) # Path for categories.txt file
CONFIG_DIR_RDBL = os.path.abspath(os.path.join(BASE_DIR, "../LLM Analyses/Readability Analysis")) # Path for criteria.txt file

# Files based on mode
if APP_MODE == "CLSF":  # CLSF mode
    INPUT_FILE = os.path.join(INPUT_DIR, "LinkedIn Ground Truth Sample - clsf.csv")
    OUTPUT_FILE = os.path.join(OUTPUT_DIR, "Ground truth - clsf.csv")
    CAT_FILE = os.path.join(CONFIG_DIR_CLSF, "Classification categories.txt")
else:  # RDBL mode
    INPUT_FILE = os.path.join(INPUT_DIR, "LinkedIn Ground Truth Sample - rdbl.csv")
    OUTPUT_FILE = os.path.join(OUTPUT_DIR, "Ground truth - rdbl.csv")
    CAT_FILE = os.path.join(CONFIG_DIR_RDBL, "Readability criteria.txt")

# Ensure folders exist
for folder in [INPUT_DIR, OUTPUT_DIR, CONFIG_DIR_CLSF, CONFIG_DIR_RDBL]:
    os.makedirs(folder, exist_ok=True)

# --- DATA PARSING ---
def parse_classification_file(filepath):
    """Parses LSEG ESG categories and definitions."""
    if not os.path.exists(filepath): return {}
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    pillars = {}
    sections = re.split(r'(Pillar \d+: \w+)', content)
    for i in range(1, len(sections), 2):
        current_pillar = sections[i].strip()
        pillars[current_pillar] = []
        # Extract name and definition
        items = re.findall(r'\d+\.\s+(.*?)\n+Definition:\s+(.*?)(?=\n\d+\.|\n\nPillar|$)', sections[i+1], re.DOTALL)
        for name, definition in items:
            pillars[current_pillar].append({"name": name.strip(), "definition": definition.strip()})
    return pillars

def parse_rdbl_file(filepath):
    """Parses Shimamura readability criteria and 1-3-5 score descriptions ."""
    if not os.path.exists(filepath): return {}
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    criteria = {}
    blocks = re.split(r'\n(?=[A-Z]-\d{2})', content)
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) < 2: continue
        header = lines[0].split(' ', 1)
        code = header[0].strip()
        name = header[1].strip() if len(header) > 1 else ""
        definition = lines[1].strip()
        scores = {}
        # Extract descriptions for scores 1, 3, 5
        score_matches = re.findall(r'([135]):\s+(.*?)(?=\n[135]:|$)', block, re.DOTALL)
        for num, text in score_matches:
            scores[int(num)] = text.strip()
        criteria[code] = {"name": name, "definition": definition, "scores": scores}
    return criteria

# --- DATA LOADING ---
def get_data():
    # Load input
    if os.path.exists(INPUT_FILE):
        df_base = pd.read_csv(INPUT_FILE)
    else:
        st.error(f"Input file not found: {INPUT_FILE}")
        df_base = pd.DataFrame()
    # Load output/progress
    if os.path.exists(OUTPUT_FILE):
        df_out = pd.read_csv(OUTPUT_FILE, encoding="utf-8-sig")
    else:
        df_out = pd.DataFrame()
        
    return df_base, df_out

# --- UI SETUP ---
st.set_page_config(layout="wide", page_title=f"LinkedIn {APP_MODE} Engine")
st.title(f"LinkedIn Manual Annotation - {'Classification' if APP_MODE == 'CLSF' else 'Readability'}")

df_base, df_out = get_data()
cat_data = parse_classification_file(CAT_FILE) if APP_MODE == "CLSF" else parse_rdbl_file(CAT_FILE)

# Track progress
done_urls = set(df_out['URL'].tolist()) if not df_out.empty and 'URL' in df_out.columns else set()

if 'current_idx' not in st.session_state:
    # Find first unfinished post
    start_idx = 0
    for idx, row in df_base.iterrows():
        if row['URL'] not in done_urls:
            start_idx = idx
            break
    st.session_state.current_idx = start_idx

# Progress Bar
total = len(df_base)
st.write(f"**Progress:** {len(done_urls)}/{total}")
st.progress(len(done_urls)/total if total > 0 else 0)

# --- MAIN ENGINE ---
if st.session_state.current_idx < total:
    row = df_base.iloc[st.session_state.current_idx]
    
    st.markdown(f"### Company: [{row['Company Name']}]({row['URL']}) | Date: {row['Date'].split("T")[0]} | Annotated: {'✅' if row['URL'] in done_urls else '❌'}")
    st.markdown("<style>textarea { spellcheck: false !important; }</style>", unsafe_allow_html=True)
    st.text_area("LinkedIn Post Content", row['Text'], height=250, key=f"post_{st.session_state.current_idx}")

    st.divider()

    if APP_MODE == "CLSF":  # CLSF MODE
        st.subheader("ESG Classification")
        selected_subcats = []
        for pillar, subs in cat_data.items():
            st.write(f"**{pillar}**")
            cols = st.columns(len(subs))
            for i, s in enumerate(subs):
                with cols[i]:
                    if st.checkbox(s['name'], key=f"c_{s['name']}_{st.session_state.current_idx}", help=s['definition']):
                        selected_subcats.append(s['name'])
        st.divider()
        is_none = st.checkbox("None", key=f"c_none_{st.session_state.current_idx}", help="Select if no evidence of any ESG subcategory is present.")

        if st.button("Save Classification"):
            res = row.to_dict()
            # Pillar mapping logic
            res["Cat_E"] = "Yes" if any(x['name'] in selected_subcats for x in cat_data.get("Pillar 1: Environmental", [])) else "No"
            res["Cat_S"] = "Yes" if any(x['name'] in selected_subcats for x in cat_data.get("Pillar 2: Social", [])) else "No"
            res["Cat_G"] = "Yes" if any(x['name'] in selected_subcats for x in cat_data.get("Pillar 3: Governance", [])) else "No"
            res["Cat_N"] = "Yes" if is_none else "No"
            
            for p_list in cat_data.values():
                for s in p_list:
                    res[f"{s['name'].replace(' ', '_')}_active"] = "Yes" if (s['name'] in selected_subcats and not is_none) else "No"
            
            df_out = pd.concat([df_out, pd.DataFrame([res])]).drop_duplicates(subset=['URL'], keep='last')
            df_out.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
            st.success("Saved!")
            st.session_state.current_idx = min(total - 1, st.session_state.current_idx + 1)
            st.rerun()

    else:  # RDBL MODE
        st.subheader("Readability Analysis")
        crit_codes = list(cat_data.keys())
        tabs = st.tabs([f"{c} {'✅' if st.session_state.get(f're_{c}_{st.session_state.current_idx}') else ''}" for c in crit_codes])
        
        res = row.to_dict()
        for i, code in enumerate(crit_codes):
            with tabs[i]:
                info = cat_data[code]
                st.markdown(f"**{info['name']}**")
                st.info(f"**Definition:** {info['definition']}")
                
                is_na = st.checkbox("Not applicable (N/A)", key=f"na_{code}_{row['URL']}")
                
                if not is_na:
                    st.markdown(f"**Score Guide:**\n* **1:** {info['scores'].get(1, '')}\n* **3:** {info['scores'].get(3, '')}\n* **5:** {info['scores'].get(5, '')}")
                    score = st.select_slider("Score", options=[1,2,3,4,5], value=3, key=f"s_{code}_{st.session_state.current_idx}")
                    res[f"{code.replace('-', '_')}_score"] = score # Formats A-01 to A_01_score 
                else:
                    st.warning("Marked as N/A. Provide reasoning down below.", width=400)
                    res[f"{code.replace('-', '_')}_score"] = "N/A"

                reason = st.text_area("Reasoning", key=f"re_{code}_{st.session_state.current_idx}", height=100)
                res[f"{code.replace('-', '_')}_reasoning"] = reason

        if st.button("Save Readability Analysis"):
            df_out = pd.concat([df_out, pd.DataFrame([res])]).drop_duplicates(subset=['URL'], keep='last')
            df_out.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
            st.success("Saved!")
            st.session_state.current_idx = min(total - 1, st.session_state.current_idx + 1)
            st.rerun()

    st.divider()
    c1, c2, _ = st.columns([1,1,5])
    if c1.button("Previous"): st.session_state.current_idx = max(0, st.session_state.current_idx - 1); st.rerun()
    if c2.button("Next"): st.session_state.current_idx = min(total - 1, st.session_state.current_idx + 1); st.rerun()
else:
    st.success("All posts processed!")