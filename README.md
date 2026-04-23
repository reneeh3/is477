# Comparative Analysis of Geographic Representation in the MoMA and MET Museums

---

## Contributors
- Renee Huang (reneeh3)  
- Sarah Kim (yewonwk2)
  
---

## Summary

This project looks into the influence of the geographic origin of artists in major museums, specifically the Metropolitan Museum of Art (MET) and the Museum of Modern Art (MoMA). Museums are key in shaping and preserving cultural and social narratives by selecting which artworks to keep and preserve. This means representation is an important area to study/
Our main research question is:
* How does the geographic origin of artists influence their representation in major museums?

Support questions include:
* Which nationalities or regions are the most represented?
* Are there differences between MoMA and MET collections?
* How has representation changed over time (with the measure being the artists' birthdays)?

We used publicly available datasets from both museums, cleaned and standardized key variables, and prepared them to be merged. Some of our preliminary findings from both are:
* For the MoMA dataset, representation seems to be concentrated in a small number of dominant regions, namely the Americas followed by Europe.
* INSERT MORE
* INSERT ONE MORE?

---

## Data Profile
*Max 2000 words*  

### Dataset 1: *MoMA: Artists.txt*
- **Location in repository:**  [reneeh3/is477/MoMA datasets/Artists.txt.zip](https://github.com/reneeh3/is477/blob/main/MoMA%20datasets/Artists.txt.zip)
- **Source:** Open-access dataset [MoMA github link](https://github.com/museumofmodernart/collection)
- **Description:** Contains key information about individual artist profiles in the MoMA collections by artist ID number
- **Structure:**
  - Rows: 15,859 individual artists
  - Columns: 9 variables
    -   `ConstituentID`: Artist unique identifier
    -   `DisplayName`: Artist name
    -   `ArtistBio`: Short artist biography
    -   `Nationality`: Country of citizenship
    -   `Gender`
    -   `BeginDate`: Birth year
    -   `EndDate`: Death year
    -   `Wiki QID`: URL for artist "About me's"
    -   `ULAN`:  Catalog for artists [artist](https://www.getty.edu/research/tools/vocabularies/ulan/index.html)
  - Primary identifier: `ConstituentID`
- **Content & characteristics:** This is an artist-level dataset with demographic and biographical attributes like nationality, gender, birth years, and death years. Most variables are categorical and text fields, with `BeginDate` and `EndDate` as numeric year fields. There are 137 unique nationalities and 7 gender values (see later in data cleaning that most of these are syntactic errors). There are many missing values in `ArtistBio` (2,188 missing), `Nationality` (2,500 missing), `Gender` (3,282 missing), `Wiki QID` (12,611 missing), and `ULAN` (12,927 missing)
- **Ethical/legal considerations:** While this is a large, public museum dataset, it still reflects institutional choices about which artists are documented. Missing demographic information can limit how we can interpret how fully artists are represented. Additionally, the fields may be reflective of what the museum labels the artists and not how the artists actually identify.
- **Relevance to research questions:** The dataset provides the artists' nationalities and birthdate information needed to analyze geographic origin. It is generally more accurate and/or filled out than the Artwork dataset. It will let us study the background represented in MoMA and to compare it with the MET dataset.

  
### Dataset 2: *MoMA: Artworks.txt*
- **Location in repository:**  [reneeh3/is477/MoMA datasets/Artwork.txt.zip]([https://github.com/reneeh3/is477/blob/main/MoMA%20datasets/Artist.txt.zip](https://github.com/reneeh3/is477/blob/main/MoMA%20datasets/Artworks.txt.zip))
- **Source:** Open-access dataset [MoMA github link](https://github.com/museumofmodernart/collection)
- **Structure:**
  - Rows: 160,632 individual artworks
  - Columns: 
  - **Basic artwork info:**
    - `Title`: Title of artwork  
    - `Artist`: Name of artist  
    - `ConstituentID`: Artist identifier (links to Artists dataset)  

  - **Artist-related metadata (duplicated from artist dataset):**
    - `ArtistBio`: Short description of the artist  
    - `Nationality`: Artist nationality  
    - `BeginDate`: Artist birth year  
    - `EndDate`: Artist death year  
    - `Gender`: Artist gender  

  - **Artwork-specific metadata:**
    - `Date`: Year or year range the artwork was created  
    - `Medium`: Materials used to create 
    - `Dimensions`: Physical size description  
    - `Classification`: Type of artwork (e.g., architecture, sculpture)  
    - `Department`: Museum department  

  - **Museum/catalog information:**
    - `CreditLine`: Acquisition credit  
    - `AccessionNumber`: Unique accession number  
    - `DateAcquired`: Date the museum acquired the artwork  
    - `Cataloged`: Whether the item is cataloged  
    - `ObjectID`: Unique artwork identifier  

  - **Links and display info:**
    - `URL`: Link to artwork page  
    - `ImageURL`: Link to artwork image  
    - `OnView`: Whether the artwork is currently on display  

  - **Physical measurement fields (numeric):**
    - `Circumference (cm)`  
    - `Depth (cm)`  
    - `Diameter (cm)`  
    - `Height (cm)`  
    - `Length (cm)`  
    - `Weight (kg)`  
    - `Width (cm)`  
    - `Seat Height (cm)`  
    - `Duration (sec.)`  

  - Primary identifier: `ObjectID`
- **Content & characteristics:** This is an artwork-level dataset that is linked to the artists dataset through `ConstituentID`. It has very descriptive metadata and numerical measurement fields for physical art. The dataset has 8 unique departments and 42 unique classifications.
- **Ethical/legal considerations:** Similarly to  Artists.txt, it reflects the curators' and institutional decisions to catalog and preserve these pieces rather than a random sample of all artworks. The Metadata quality varies a lot, with some having the majority of fields filled out and some having no documentation. Ethically, missing or inconsistent artist information may affect conclusions about representation, which may negatively or positively influence perception of the museum.
- **Relevance to research questions:** This dataset shows which artists are actually represented in MoMA through their artworks in the collection. Linking artists to the artworks, it helps measure how frequently each geographic origin appears. It also allows for analysis of representation across departments and classifications if interested.

---

## Data Quality
*(500–1000 words)*  
Summarize your data quality assessment.

---

## Data Cleaning
*(Max 1000 words)*  
Describe the data cleaning steps and how they addressed specific data quality issues.

---

## Findings
*(500 words)*  
Present key findings, including numeric results and/or visualizations.

---

## Future Work
*(500–1000 words)*  
Discuss lessons learned and potential future directions.

---

## Challenges
*(500 words)*  
Describe the main challenges encountered during the project.

---

## Reproducing
Provide a step-by-step guide to reproduce your results:

1.  
2.  
3.  
4.  

---

## References
- Author, A. A. (Year). *Title*. Source.  
- Dataset Name. (Year). Source/URL.  
- Software/Library Name.  
