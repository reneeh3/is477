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
- For the MoMA dataset, representation seems to be concentrated in a small number of dominant regions, namely the Americas, followed by Europe.
**- INSERT MORE**
**- INSERT ONE MORE?**

---

## Data Profile
*Max 2000 words*  

### Dataset 1: *MoMA: Artists.txt*
- **Location in repository:**  [reneeh3/is477/MoMA datasets/Artists.txt.zip](https://github.com/reneeh3/is477/blob/main/MoMA%20datasets/Artists.txt.zip)
- **Source:** Open-access dataset [MoMA github link](https://github.com/museumofmodernart/collection), [Dataset accessed April 1st](https://media.githubusercontent.com/media/MuseumofModernArt/collection/43399bad2fad626a0750ab6801ced6f1e83b0a41/Artists.csv)
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
- **Source:** Open-access dataset [MoMA github link](https://github.com/museumofmodernart/collection), [Dataset Accessed April 1st](https://media.githubusercontent.com/media/MuseumofModernArt/collection/a46be68e826552737fce8152b002dcd603c0a300/Artworks.csv) 
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
To assess data quality, we examined completeness, consistency, and accuracy across key variables. A primary focus was on identifying missing values, as these directly impact our ability to analyze artist representation. For MoMA, there were many incomplete and inconsistent variables. Generally, the percentage for the important variables required for analysis was not very concerning, and the higher missingness variables are only apparent in less critical information such as size or web links to the works.

**MoMA Artists.txt:**
- **High missingness:**
  - There are **2 variables** with extremely high levels of missing data. However, these were not important to the question we're evaluating.

    - `ULAN` → 12,927 missing (~81.5%)  
    - `Wiki QID` → 12,611 missing (~79.5%)  

- **Moderate missingness:**
  - Several variables have noticeable but less severe missing data:

    - `Gender` → 3,282 missing (~20.7%)  
    - `Nationality` → 2,500 missing (~15.8%)  
    - `ArtistBio` → 2,188 missing (~13.8%)  

- **No missing values:**
  - The following key variables are fully filled out:
  
    - `ConstituentID`  
    - `DisplayName`  
    - `BeginDate`  
    - `EndDate`  

**MoMA Artworks.txt**
- **Sparse variables (high missingness):**
  - There are **10 variables** with extremely high levels of missing data. However, these were both not important to the central question or exclusive to digital/physical artworks so they are blank on purpose.

    - `Seat Height (cm)` → 160,632 missing (100%)  
    - `Circumference (cm)` → 160,622 missing (~99.99%)  
    - `Weight (kg)` → 160,332 missing (~99.81%)  
    - `Length (cm)` → 159,898 missing (~99.54%)  
    - `OnView` → 159,345 missing (~99.20%)  
    - `Diameter (cm)` → 159,237 missing (~99.13%)  
    - `Duration (sec.)` → 158,651 missing (~98.77%)  
    - `Depth (cm)` → 141,944 missing (~88.36%)  

  - The rest of the variables have **moderate missingness**:
    - `ImageURL` → 67,397 missing (~41.96%)  
    - `URL` → 58,958 missing (~36.71%)  
    - `Medium` → 9,162 missing (~5.70%)  
    - `Dimensions` → 8,739 missing (~5.44%)  
    - `DateAcquired` → 5,467 missing (~3.40%~) 

---

## Data Cleaning
*(Max 1000 words)*  

### MoMA Datasets

For the MoMA Artists and Artworks dataset, the data was first initially cleaned and merged through Python. Then, using OpenRefine, the data was manually standardized for consistency. 

#### Python Cleaning

For Python, I started by normalizing column names in  `Artists.txt` and `Artworks.txt`. I stripped extra spaces, converted all column names to lowercase, and replaced spaces with underscores, which addresses consistency issues. The text fields were trimmed and numerical columns like `constituentid`, `begindate`, and `enddate` were converted to numeric values. Fields with `0` values in date columns were replaced with missing values because `0` was being used as a placeholder rather than a real year. This addressed accuracy and missing-value issues.

I also created functions that standardize nationality, gender, and dates. The nationality function removed extra parentheses and formatting, and used a mapping dictionary to combine the same values that were written differently, such as `USA` or `US.` I did the same with gender, in case that was something extra we wanted to analyze. For the year function, it pulled the first valid four-digit year from the strings to standardize strings like `c. 1950` or `1945-46`.

For the artworks dataset, I cleaned text columns, converted `objectid` into a numeric field, and standardized nationality and gender the same way. A common issue in the MoMA data was that some artworks had multiple artists listed in one row. So, I parsed the `constituentid` field into a list of artist IDs and exploded the dataset so that each artwork-artist pair received its own row, enabling easier merging and preventing multiple nationalities from being trapped inside one cell.

After that, I created an artist lookup table from the cleaned artist dataset and merged it with the cleaned artworks dataset using `constituentid`. When both artwork-level and artist-level nationality or gender values existed, I prioritized the artist-level fields because they came directly from the artist profile dataset, and that dataset was also more high quality. I then created `nationality_clean` and `gender_clean` fields using those preferred values.

Finally, I removed invalid rows missing both `objectid` and `accessionnumber`, removed duplicate rows, and removed duplicate artwork-artist combinations, addressing uniqueness issues and preventing the same artwork-artist relationship from being counted more than once.

#### OpenRefine Cleaning

I imported the post-Python cleaned MoMA dataset into OpenRefine for additional cleaning. I mainly used it to inspect facets and mass-edit inconsistent nationality values that would be difficult to fix through Python. Most corrections were ones of repeated parentheses, multi-artist nationality strings, spelling errors such as `Russiam`, and inconsistent versions of the same nationality. I also removed irrelevant columns to our question, cleaned up the column names, and trimmed whitespace.

The unnecessary columns I removed included mostly physical measurement columns, image/link fields, and old/unclean nationality columns to reduce clutter and keep the final dataset focused on the variables for geographic representation. For multi-nationality values, I used OpenRefine’s multi-valued cell split function to separate values by commas, then trimmed whitespace. This made the nationality field more consistent.

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

1. Clone the project repository and navigate into it:
   ```bash
   git clone <your-repo-link>
   cd is477
   ```
2.  Install required dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
3.  Run the MoMA workflow using Snakemake:
   ```bash
snakemake --cores 1
   ```
This will automatically download the MoMA datasets from the official MoMA GitHub repository, run the cleaning script ( `clean_moma.py`), and generate a cleaned dataset  (`moma_snakefile_cleaned.csv`).

4.  Open the cleaned dataset in OpenRefine.
   - Load `moma_snakefile_cleaned.csv`
   - Apply the saved history file:
     - `apply_openrefine.json`
5. Export the final cleaned MoMA dataset from OpenRefine as `final_moma.csv`.
**6. COMPLETE THE MET CLEANING STEPS**
-
-
-

7. Run analysis **(`INSERT THE ANALYSIS FILE NAME`)** to generate results.
---

## References
- 
