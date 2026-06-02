# De verklarende waarde van ESG-washing-strategieën.
## De relatie tussen thematische en talige verhulling via LinkedIn op ESG-controverses, en de validatie van LLM-gestuurde tekstanalyse.
<code style="color : none">masterproef Kobe Verdoodt 2025-2026</code>

Handelswetenschappen - traject Management & IT

Promotor: Prof. Els Clarysse

Deze repository bevat de data-input, Python-scripts en .csv outputs voor de masterproef van Kobe Verdoodt.

## Opmerkingen
* **Bestandsbeheer:** Gebruik als één geheel en behoud de huidige bestandindeling. Vul uw eigen rootfolder in de Python-scripts in waar nodig.
* **Beveiliging:** API-sleutels zijn om veiligheidsredenen verwijderd en vervangen door een lege .txt file.

## 📂 Projectstructuur

### 1. `/Data Collection`
Bevat de ruwe data-extracties afkomstig uit **LSEG Workspace**, en de dataset met **LinkedIn-scrapes** voor de betrokken bedrijven. Deze data vormen de input voor alle gehanteerde variabelen.
* **/LSEG:** bevat zowel de ruwe dataset uit LSEG Workspace als de bewerkte versie. In de gefilterde dataset zijn variabelen hernoemd en zijn observaties weggelaten op basis van de aanwezige (on)afhankelijke en controlevariabelen.
* **/LinkedIn:** bevat de LSEG dataset gefilterd op aanwezigheid van LinkedIn-profielen. Daarnaast is ook de LinkedIn dataset (verzameling van alle LinkedIn-posts) hierin te vinden, inclusief een versie gefilterd voor classificatie, en een versie gefilterd voor de leesbaarheidsanalyse. De filtering gebeurde via `LinkedIn data cleaning.ipynb` en de filterresultaten zijn beschreven in een `.txt` bestand.

### 2. `/Ground Truth`
Bevat twee scripts, één voor het selecteren van een steekproef van LinkedIn-posts, één voor een overzichtelijke interface om handmatig de posts te annoteren. De gebruikte steekproeven zijn terug te vinden in de submap `/Samples`, en de annotaties in submap `/Annotations`.

### 3. `/LLM Analyses`
De kern van de tekstanalyse, onderverdeeld in twee subsecties:
* **/Classification** (thematische classificatie)
* **/Readability Analysis** (leesbaarheidsanalyse)


**Elke submap bevat:**
* **Script:** code voor uitvoering van de tekstanalyse met OpenAI GPT modellen.
* **Finale output:** `.csv` bestand met de output van de tekstanalyse op de finale LinkedIn-dataset.
* **Categorieën & Voorbeelden:** `.txt` bestanden van de gehanteerde labels en few-shot voorbeelden, dient als input voor de prompt.
* **/Ground Truth sample:** een `submap` met daarin het script om de prestaties van de analyses te vergelijken met de ground truth, een `.csv` bestand met de uitkomsten van die prestatiemeting overheen alle uitgevoerde LLM-analyses, een `.svg` bestand met de grafische voorstelling hiervan, en daarnaast nog volgende submappen:
    * **/Classifications of /Readability analyses**: de ruwe output van de LLM-analyses uitgevoerd op de beperkte ground truth steekproef.
    * **/Performance- measuring**: de berekende performantiemetrieken per analyse-output.

### 4. `/Inferential Analysis`
Bevat de scripts en bestanden voor de finale statistische verwerking:
* **LLM analyses join.ipynb:** script om beide LLM-analyses op de finale dataset in één bestand samen te voegen. Resulteert in `LinkedIn LLM Analysis output.csv`
* **Final aggregation.ipynb:** script om postniveau data om te zetten naar geaggregeerde scores of filtering op bedrijfsniveau. Combineert dit met de LSEG dataset en berekent de onafhankelijke variabele 'GAP'. Resulteert in `Final Dataset.csv`
* **Final analysis.ipynb:** script om finale logistische regressies uit te voeren met de gekozen variabelen. Deze regressieresultaten worden telkens toegevoegd aan `Regressions results.xlsx`
