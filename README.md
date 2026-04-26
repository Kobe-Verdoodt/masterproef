# masterproef

# ESG-Washing & LinkedIn-communicatie

Deze repository bevat de data-input, Python-scripts en .csv outputs voor de masterproef van Kobe Verdoodt.

## ⚠️ Belangrijke Opmerking over de Status
Dit is een **werkversie** (Proof-of-Concept fase). De scripts en bestanden zijn nog niet in hun definitieve vorm.
* **Bestandsbeheer:** De scripts bevatten momenteel relatieve paden. Voor een correcte uitvoering dienen inputbestanden mogelijk in dezelfde directory als de scripts geplaatst te worden.
* **Prompttechnieken:** De LLM-scripts bevatten experimentele prompt-technieken die niet allemaal zijn opgenomen in de huidige versie van de geschreven methodologie.
* **Beveiliging:** API-sleutels zijn om veiligheidsredenen verwijderd uit alle scripts.

## 📂 Projectstructuur

### 1. `/data`
Bevat de ruwe data-extracties afkomstig uit **LSEG Workspace**, en de omgevormde versie naar bedrijf-jaar-instanties. Deze data vormen de basis voor zowel de ESG-washing scores als de financiële controlevariabelen.

### 2. `/PSM`
Bevat de volledige uitwerking van de **Propensity Score Matching** procedure. Hierin bevinden zich de scripts voor de steekproefselectie en de bijbehorende balansdiagnostiek (SMD-tabellen en plots).

### 3. `/LLM-analysis`
De kern van de inhoudsanalyse, onderverdeeld in drie subsecties:
* **/classification** (Thematische Classificatie)
* **/sentiment-analysis** (Sentimentanalyse)
* **/readability-analysis** (Leesbaarheidsanalyse)

**Elke submap bevat:**
* **Scripts:** Code voor zowel Google Gemini als OpenAI GPT modellen.
* **Ground Truth:** Bestanden voor de handmatige validatie.
* **Categorieën & Voorbeelden:** Documentatie van de gehanteerde labels en voorbeelden.
* **Model Performance Comparison:** Een `.png` bestand met een visuele vergelijking van de prestaties tussen de verschillende modellen/prompttechnieken.
* **/scores**: De ruwe output van de LLM-analyses.
* **/performance-measuring**: De berekende performantiemetrieken.

### 4. `/inferential-analysis`
Bevat de scripts en bestanden voor de finale statistische verwerking:
* **aggregation:** Script om postniveau data om te zetten naar bedrijf-jaar-niveau scores.
* **final analysis:** Script om finale inferentiële analyse uit te werken (nog niet toepasbaar vanwege lage N bij de PoC).
* **translation table:** Een koppeltabel om LSEG-identifiers (RIC's) om te zetten naar leesbare bedrijfsnamen.
* **final analysis input:** De uiteindelijke inputbestanden (.csv) en scripts voor de inferentiële statistiek (regressies en toetsen).
