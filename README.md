# De voorspellende waarde van ESG-washing-strategieën:
## De impact van thematische en talige verhulling via LinkedIn op ESG-controverses en de validatie van LLM-gestuurde tekstanalyse.
### masterproef Kobe Verdoodt 2025-2026
Handelswetenschappen - traject Management & IT

Promotor: Prof. Els Clarysse

Deze repository bevat de data-input, Python-scripts en .csv outputs voor de masterproef van Kobe Verdoodt.

## Opmerkingen
* **Bestandsbeheer:** Gebruik als één geheel en behoud de huidige bestandindeling. Vul uw eigen rootfolder in in de Python-scripts waar nodig.
* **Beveiliging:** API-sleutels zijn om veiligheidsredenen verwijderd en vervangen door een lege .txt file.

## 📂 Projectstructuur

### 1. `/Data Collection`
Bevat de ruwe data-extracties afkomstig uit **LSEG Workspace**, en de dataset met **LinkedIn-scrapes** voor de betrokken bedrijven. Deze data vormen de input voor de alle gebruikte variabelen.
* **/LSEG:** tekst
* **/LinkedIn:** tekst

### 2. `/Ground Truth`
Tekst

### 3. `/LLM Analyses`
De kern van de tekstanalyse, onderverdeeld in twee subsecties:
* **/Classification** (Thematische Classificatie)
* **/Readability Analysis** (Leesbaarheidsanalyse)


**Elke submap bevat:**
* **Scripts:** Code voor OpenAI GPT modellen.
* **Ground Truth:** Bestand voor de handmatige annotaties.
* **Categorieën & Voorbeelden:** Documentatie van de gehanteerde labels en voorbeelden, dient als input voor de prompt.
* **Model Performance Comparison:** Een `.png` bestand met een visuele vergelijking van de prestaties tussen de verschillende modellen/prompttechnieken. Deze metrieken komen ook nog niet allemaal overeen met de geschreven methodologie.
* **/scores**: De ruwe output van de LLM-analyses.
* **/performance-measuring**: De berekende performantiemetrieken per analyse-output.

### 4. `/Inferential Analysis`
Bevat de scripts en bestanden voor de finale statistische verwerking:
* **aggregation:** Script om postniveau data om te zetten naar bedrijf-jaar-niveau scores.
* **final analysis:** Script om finale inferentiële analyse uit te werken (nog niet toepasbaar vanwege lage N bij de PoC).
* **final analysis input:** De uiteindelijke inputbestanden (.csv) en scripts voor de inferentiële statistiek (regressies en toetsen).
