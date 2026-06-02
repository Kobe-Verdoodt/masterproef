<code style="color : name_color">text</code>
# De verklarende waarde van ESG-washing-strategieën:
## De relatie tussen thematische en talige verhulling via LinkedIn op ESG-controverses, en de validatie van LLM-gestuurde tekstanalyse.
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
* **/LSEG:** Bevat zowel de ruwe dataset uit LSEG Workspace als de bewerkte versie. In de gefilterde dataset zijn variabelen hernoemd en zijn observaties weggelaten op basis van de aanwezige (on)afhankelijke en controlevariabelen.
* **/LinkedIn:** Bevat de LSEG dataset gefilterd op aanwezigheid van LinkedIn-profielen. Bevat daarnaast de LinkedIn dataset (verzameling van alle LinkedIn-posts), inclusief een versie gefilterd voor classificatie, en een versie gefilterd voor de leesbaarheidsanalyse. De filtering gebeurde via `LinkedIn data cleaning.ipynb` en de filterresultaten zijn beschreven in een `.txt` bestand.

### 2. `/Ground Truth`
Bevat twee scripts, één voor het selecteren van een steekproef van LinkedIn-posts, één voor een overzichtelijke interface om handmatig de posts te annoteren. De gebruikte steekproeven zijn terug te vinden in de submap `Samples`, en de annotaties in submap `Annotations`.

### 3. `/LLM Analyses`
De kern van de tekstanalyse, onderverdeeld in twee subsecties:
* **/Classification** (Thematische Classificatie)
* **/Readability Analysis** (Leesbaarheidsanalyse)


**Elke submap bevat:**
* **Script:** Code voor uitvoering van de tekstanalyse met OpenAI GPT modellen.
* **Finale output:** `.csv` bestand met de output van de tekstanalyse op de finale LinkedIn-dataset.
* **Categorieën & Voorbeelden:** `.txt` bestanden van de gehanteerde labels en few-shot voorbeelden, dient als input voor de prompt.
* **/Ground Truth sample:** Een `submap` met daarin het script om de prestaties van de analyses te vergelijken met de ground truth, een `.csv` bestand met de uitkomsten van die prestatiemeting overheen alle uitgevoerde LLM-analyses, een `.svg` bestand met de grafische voorstelling hiervan, en daarnaast nog volgende submappen:
    * **/Classifications of /Readability analyses**: De ruwe output van de LLM-analyses uitgevoerd op de beperkte ground truth steekproef.
    * **/Performance- measuring**: De berekende performantiemetrieken per analyse-output.

### 4. `/Inferential Analysis`
Bevat de scripts en bestanden voor de finale statistische verwerking:
* **LLM analyses join:** Script om beide LLM-analyses op de finale dataset in één bestand samen te voegen. Resulteert in `LinkedIn LLM Analysis output.csv`
* **Final aggregation:** Script om postniveau data om te zetten naar geaggregeerde scores of filtering op bedrijfsniveau. Combineert dit met de LSEG dataset en berekent de onafhankelijke variabele 'GAP'. Resulteert in `Final Dataset.csv`
* **Final analysis:** Script om finale logistische regressies uit te voeren met de gekozen variabelen. Deze regressieresultaten worden telkens toegevoegd aan `Regressions results.xlsx`
