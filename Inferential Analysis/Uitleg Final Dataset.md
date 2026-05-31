**Overzicht Dataset Variabelen**
================================

Dit document bevat een compacte en gestructureerde beschrijving van de variabelen in de dataset (vanaf de variabele Year). Om het overzichtelijk te houden, worden herhalende kolommen uitgelegd aan de hand van universele suffixes.

**1\. Basis- en Financiële Variabelen**
---------------------------------------

*   **Year**: Het kalenderjaar van de geobserveerde data.
    
*   **CAP**: De marktkapitalisatie (_Market Capitalization_) van het bedrijf.
    
*   **CAPln**: Het natuurlijk logaritme van de marktkapitalisatie, genoteerd als ln(CAP), om scheefheid in de verdeling te corrigeren.
        
*   **BOARD**: Aantal onafhankelijke leden van de Raad van Bestuur (_Independent Board Members_).
    
*   **LEV**: Hefboomfactor of schuldgraad (_Leverage_).
    
*   **WORDS**: Het totale aantal woorden in de geanalyseerde posts van het bedrijf.
    
*   **WORDSln**: Het natuurlijk logaritme van het totale aantal woorden in de geanalyseerde posts, genoteerd als ln(WORDS).
    
*   **CONTR**: Indicator voor controverses op het gebied van ESG (waardes 1 of 0).
    
*   **GAP**: Het verschil tussen de Weighted ESG Score en ESG Score (_Selective Disclosure_).
    
*   **RDBL**: Gemiddelde algemene leesbaarheidsscore (_Readability_) van de posts.
    

**2\. ESG Scores (LSEG)**
---------------------------------------------

*   **ESG Controversies Score**: Score van LSEG gebaseerd op negatieve ESG-incidenten in de media.
    
*   **ESG Score**: De ESG Score van het bedrijf, geëxtraheerd van LSEG Workspace.
    
*   **Pijlerscores (Pillar Scores)**: De scores voor hoofdcomponenten van de ESG-meting:
    
*   _Environmental Pillar Score_ (Milieupijler)
    
*   _Social Pillar Score_ (Sociale pijler)
    
*   _Governance Pillar Score_ (Bestuurspijler)
    
*   **Sub-categorie / Sub-pijler Scores**: Specifieke onderliggende scores binnen de hoofdpijlers:
    
*   _Milieu (E)_: Emissions Score, Innovation Score, Resource Use Score.
    
*   _Sociaal (S)_: Human Rights Score, Product Responsibility Score, Workforce Score, Community Score.
    
*   _Bestuur (G)_: Management Score, Shareholders Score, CSR Strategy Score.


**3\. Social Media & LinkedIn Statistieken**
--------------------------------------------

*   **LinkedIn URL**: De directe weblink naar de officiële LinkedIn-bedrijfspagina.
    
*   **POSTS**: Het totale aantal LinkedIn-berichten van het bedrijf in het afgelopen jaar (30-04-2025 tot en met 30-04-2026).
    
*   **POSTSln**: Het natuurlijk logaritme van het aantal berichten, genoteerd als ln(POSTS).
    
*   **WORDS\_per\_post**: Het gemiddelde aantal woorden per geplaatst bericht.
    
*   **SENTENCES\_per\_post**: Het gemiddelde aantal zinnen per geplaatst bericht.
    

**4\. Suffixes voor Tekst- en Sentimentkenmerken**
--------------------------------------------------

Een groot deel van de dataset bestaat uit herhalende metingen (zoals de _Gunning Fog_ leesbaarheidsindex, specifieke criteria-scores Crit\_A t/m Crit\_L, of specifieke sub-scores A\_01\_score t/m L\_01\_score). In plaats van elke kolom afzonderlijk te benoemen, worden deze gedefinieerd door de volgende achtervoegsels (suffixes):

### **Inhoudelijke Suffixes**

*   **\_posts**: Het aandeel of aantal _posts_ dat specifiek over deze ESG-categorie gaat, gefilterd door de LLM-classificatie (bijv. Cat\_E\_posts of Emissions\_posts).
    
*   **\_words**: Het aandeel of aantal _woorden_ dat specifiek aan deze ESG-categorie is gewijd, gefilterd door de LLM-classificatie (bijv. Cat\_E\_words of Emissions\_words).
    

### **Categorie Suffixes (Metingen binnen specifieke tekstgedeelten)**

*   _(Geen suffix)_: Gemeten over de gehele tekst (alle posts gecombineerd).
    
*   **\_ESG**: Uitsluitend gemeten binnen posts die over algemene ESG-onderwerpen gaan.
    
*   **\_E**: Uitsluitend gemeten binnen posts die over Milieu (_Environmental_) gaan.
    
*   **\_S**: Uitsluitend gemeten binnen posts die over Sociale (_Social_) onderwerpen gaan.
    
*   **\_G**: Uitsluitend gemeten binnen posts die over Bestuur (_Governance_) gaan.
    
*   **\_N**: Uitsluitend gemeten binnen posts die niet tot één van vorige categorieën zijn geclassificeerd.
    

### **Statistische Suffixes**

*   **\_z**: De gestandaardiseerde waarde van de variabele berekend als een z-score:
    $$z = \frac{x - \mu}{\sigma}$$
    

### **Voorbeelden van Suffix-combinaties:**

*   **Gunning\_Fog\_E**: De Gunning Fog leesbaarheidsindex berekend _uitsluitend_ op de tekst van de Milieu-gerelateerde posts.
    
*   **Crit\_A\_S**: De score voor Criterium A berekend _uitsluitend_ op de Social-gerelateerde posts.
    

**5\. ESG Scores (Afgeleid)**
---------------------------------------------

*   **ESG Weighted Score**: Berekende score gevormd door de som van het relatief aantal posts (_\_posts_) of woorden (_\_words_) voor iedere ESG-pilaar, telkens vermenigvuldigd met de deelscore voor die pilaar:
$$\text{ESG Weighted Score\_words} = \text{Cat\_E\_words} \times \text{Environmental Pillar Score} + \text{Cat\_S\_words} \times \text{Social Pillar Score} + \text{Cat\_G\_words} \times \text{Governance Pillar Score}$$