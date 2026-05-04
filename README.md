# Geographic Representation in the MoMA and MET Museums

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
- Representation is heavily concentrated in a few dominant regions, particularly the Americas and Europe, indicating a strong Western bias in the collection.
- There is evidence of increasing geographic diversity in more recent periods, with a gradual rise in artists from non-Western regions.
- Despite this shift, regions such as Africa and parts of Asia remain underrepresented, suggesting persistent historical imbalances in global art representation.

---

## Data Profile
*Max 2000 words*  

### Dataset 1: *MoMA: Artists.txt*
- **Location in repository:**  [reneeh3/is477/MoMA datasets/Artists.txt.zip](https://github.com/reneeh3/is477/blob/main/MoMA%20datasets/Artists.txt.zip)
- **Source:** Open-access dataset [MoMA github link](https://github.com/museumofmodernart/collection), [Dataset accessed April 1st, 2026](https://media.githubusercontent.com/media/MuseumofModernArt/collection/43399bad2fad626a0750ab6801ced6f1e83b0a41/Artists.csv)
- **Description:** Contains key information about individual artist profiles in the MoMA collections by artist ID number. The dataset is derived from MoMA's internal collections database and includes only accessioned and catalogued works. It reflects institutional decisions and curation, so it is not a complete representation of all artists. Some records are marked as not curatorially approved, so the metadata may be incomplete or unverified. 
- **Structure:**
  - Format: CSV (UTF-8 encoded)
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
- **Source:** Open-access dataset [MoMA github link](https://github.com/museumofmodernart/collection), [Dataset Accessed April 1st, 2026](https://media.githubusercontent.com/media/MuseumofModernArt/collection/a46be68e826552737fce8152b002dcd603c0a300/Artworks.csv)
- **Description**: This dataset includes information about the MoMA collection's artworks. The dataset is derived from MoMA's internal collections database and includes only accessioned and catalogued works. It reflects institutional decisions and curation, so it is not a complete representation of all artworks. Some records are marked as not curatorially approved, so the metadata may be incomplete or unverified. 
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
- **Content & characteristics:** This is an artwork-level dataset that is linked to the artists dataset through `ConstituentID`. It has very descriptive metadata and numerical measurement fields for physical art. The dataset has 8 unique departments and 42 unique classifications. While MoMA’s full collection contains nearly 200,000 works, this dataset includes only those that have been digitized/cataloged, so some artists, regions, or time periods may be underrepresented.
- **Ethical/legal considerations:** Similarly to  Artists.txt, it reflects the curators' and institutional decisions to catalog and preserve these pieces rather than a random sample of all artworks. The Metadata quality varies a lot, with some having the majority of fields filled out and some having no documentation. Ethically, missing or inconsistent artist information may affect conclusions about representation, which may negatively or positively influence perception of the museum. The dataset is provided “as is” for research purposes. Some records are incomplete, inconsistent, or not curatorially verified, which may affect accuracy. Therefore, results derived from this dataset should be interpreted cautiously and not treated as definitive measures of representation.
- **Relevance to research questions:** This dataset shows which artists are actually represented in MoMA through their artworks in the collection. Linking artists to the artworks, it helps measure how frequently each geographic origin appears. It also allows for analysis of representation across departments and classifications if interested.

The museum periodically updates both MoMA datasets. This project uses a snapshot of the data accessed on April 1, 2026, and results may differ if the dataset is updated in the future. They are also both released under a CC0 public domain license, allowing unrestricted use. However, MoMA requests proper attribution, and any modifications to the dataset should be clearly indicated.

### Dataset 3: *MET: MetObjects.csv*
- **Location in repository:** [MetObjects_csv.zip](https://github.com/reneeh3/is477/blob/88d9c8cc519c2e3528372bedea528e0b20797174/Met%20datasets/MetObjects_csv.zip)
- **Source:** Open-access dataset [Met Github link](https://github.com/metmuseum), [Dataset accessed April 2026](https://github.com/metmuseum/openaccess)
- **Description:** This dataset contains information about artworks and associated artist metadata from the Metropolitan Museum of Art collection. Unlike the MoMA datasets, which separate artists and artworks into different files, the MET dataset stores both artwork-level and artist-level information within a single table. The dataset is derived from the museum’s internal collections database and includes only digitized and cataloged works, reflecting institutional acquisition and curation decisions rather than a complete representation of all artworks or artists.  
- **Structure:**
  - Format: CSV (UTF-8 encoded)
  - Rows: ~70,000 records (reduced for this project)
  - Columns: 9 variables  
    - `Object ID`: Unique artwork identifier  
    - `Object Number`: Museum accession number  
    - `Title`: Title of artwork  
    - `Artist Display Name`: Artist name  
    - `Artist Nationality`: Artist nationality  
    - `Artist Begin Date`: Artist birth year (text format)  
    - `Artist End Date`: Artist death year (text format)  
    - `Object Date`: Artwork creation date  
    - `Constituent ID`: Artist identifier  
  - Primary identifier: `Object ID`  
- **Content & characteristics:** This is a combined artwork-artist dataset that includes both descriptive metadata and artist demographic information. The dataset required preprocessing to standardize column names, extract year values from text fields, and clean nationality data. Compared to the MoMA datasets, it is less structured and contains inconsistencies such as missing values and varied formatting. The dataset used in this project is a sampled and reduced version to meet file size constraints and improve computational efficiency.  
- **Ethical/legal considerations:** This dataset reflects curatorial and institutional decisions regarding which artworks are collected and cataloged, and therefore does not represent a complete or unbiased sample of global art. Some fields contain missing or inconsistent data, which may affect analysis. Additionally, nationality labels are assigned by the museum and may not fully reflect artists’ identities. The dataset is released under an open-access policy for research and educational use.  
- **Relevance to research questions:** This dataset provides both artwork-level and artist-level information needed to analyze geographic representation in the MET collection. By cleaning and standardizing key variables such as nationality and birth year, it enables direct comparison with the MoMA dataset to examine patterns of representation across institutions.

---

## Data Quality
*(500–1000 words)*  
To assess data quality, we examined completeness, consistency, and accuracy across key variables. A primary focus was on identifying missing values, as these directly impact our ability to analyze artist representation. For MoMA, there were many incomplete and inconsistent variables. Generally, the percentage for the important variables required for analysis was not very concerning, and the higher missingness variables are only apparent in less critical information such as size or web links to the works.

**MoMA Artists.txt:**
- **High missingness:**
  - There are **2 variables** with extremely high levels of missing data. However, these were not important to the question we're evaluating.

    - `ULAN`: 12,927 missing (~81.5%)  
    - `Wiki QID`: 12,611 missing (~79.5%)  

- **Moderate missingness:**
  - Several variables have noticeable but less severe missing data:

    - `Gender`: 3,282 missing (~20.7%)  
    - `Nationality`: 2,500 missing (~15.8%)  
    - `ArtistBio`: 2,188 missing (~13.8%)  

- **No missing values:**
  - The following key variables are fully filled out:
  
    - `ConstituentID`  
    - `DisplayName`  
    - `BeginDate`  
    - `EndDate`  

**MoMA Artworks.txt**
- **High missingness:**
  - There are **10 variables** with extremely high levels of missing data. However, these were both not important to the central question or exclusive to digital/physical artworks so they are blank on purpose.

    - `Seat Height (cm)`: 160,632 missing (100%)  
    - `Circumference (cm)`: 160,622 missing (~99.99%)  
    - `Weight (kg)`: 160,332 missing (~99.81%)  
    - `Length (cm)`: 159,898 missing (~99.54%)  
    - `OnView`: 159,345 missing (~99.20%)  
    - `Diameter (cm)`: 159,237 missing (~99.13%)  
    - `Duration (sec.)`: 158,651 missing (~98.77%)  
    - `Depth (cm)`: 141,944 missing (~88.36%)  

  - The rest of the variables have **moderate missingness**:
    - `ImageURL`: 67,397 missing (~41.96%)  
    - `URL`: 58,958 missing (~36.71%)  
    - `Medium`: 9,162 missing (~5.70%)  
    - `Dimensions`: 8,739 missing (~5.44%)  
    - `DateAcquired`: 5,467 missing (~3.40%) 

---

## Data Cleaning
*(Max 1000 words)*  

### MoMA Datasets

For the MoMA Artists and Artworks dataset, the data was initially cleaned and merged through Python. Then, using OpenRefine, the data was manually standardized for consistency. Key transformations include standardizing nationality and gender fields, splitting multi-artist records, and creating new variables such as `nationality_clean`. As a result, the final dataset differs from the original source and should be interpreted as a derived dataset. 

#### Python Cleaning

For Python, I started by normalizing column names in  `Artists.txt` and `Artworks.txt`. I stripped extra spaces, converted all column names to lowercase, and replaced spaces with underscores, which addresses consistency issues. The text fields were trimmed, and numerical columns like `constituentid`, `begindate`, and `enddate` were converted to numeric values. Fields with `0` values in date columns were replaced with missing values because `0` was being used as a placeholder rather than a real year. This addressed accuracy and missing-value issues.

I also created functions that standardize nationality, gender, and dates. The nationality function removed extra parentheses and formatting, and used a mapping dictionary to combine the same values that were written differently, such as `USA` or `US.` I did the same with gender, in case that was something extra we wanted to analyze. For the year function, it pulled the first valid four-digit year from the strings to standardize strings like `c. 1950` or `1945-46`.

For the artworks dataset, I cleaned text columns, converted `objectid` into a numeric field, and standardized nationality and gender the same way. A common issue in the MoMA data was that some artworks had multiple artists listed in one row. So, I parsed the `constituentid` field into a list of artist IDs and exploded the dataset so that each artwork-artist pair received its own row, enabling easier merging and preventing multiple nationalities from being trapped inside one cell.

After that, I created an artist lookup table from the cleaned artist dataset and merged it with the cleaned artworks dataset using `constituentid`. When both artwork-level and artist-level nationality or gender values existed, I prioritized the artist-level fields because they came directly from the artist profile dataset, and that dataset was also more high quality. I then created `nationality_clean` and `gender_clean` fields using those preferred values.

Finally, I removed invalid rows missing both `objectid` and `accessionnumber`, removed duplicate rows, and removed duplicate artwork-artist combinations, addressing uniqueness issues and preventing the same artwork-artist relationship from being counted more than once.

#### OpenRefine Cleaning

I imported the post-Python cleaned MoMA dataset into OpenRefine for additional cleaning. I mainly used it to inspect facets and mass-edit inconsistent nationality values that would be difficult to fix through Python. Most corrections were ones of repeated parentheses, multi-artist nationality strings, spelling errors such as `Russiam`, and inconsistent versions of the same nationality. I also removed irrelevant columns to our question, cleaned up the column names, and trimmed whitespace.

The unnecessary columns I removed included mostly physical measurement columns, image/link fields, and old/unclean nationality columns to reduce clutter and keep the final dataset focused on the variables for geographic representation. For multi-nationality values, I used OpenRefine’s multi-valued cell split function to separate values by commas, then trimmed whitespace. This made the nationality field more consistent.

---

## Findings
The comparative analysis of the cleaned datasets from the Metropolitan Museum of Art and the Museum of Modern Art reveals clear and consistent patterns in how geographic origin influences artist representation. Across both institutions, artists from Western countries—particularly the United States and major European nations such as France, the United Kingdom, and Germany—dominate the collections. This concentration reflects longstanding historical dynamics in the global art world, where Western regions have had greater institutional power, market influence, and access to preservation resources. As a result, museum collections are not only repositories of art but also reflections of broader cultural and geopolitical hierarchies.

Despite this shared pattern of Western dominance, there are notable differences between the two museums. The MET exhibits a stronger concentration of American artists and tends to have repeated entries of the same artists across multiple artworks. This reflects the museum’s object-centered approach to collecting, where individual works—rather than distinct artists—serve as the primary unit of acquisition. Consequently, certain artists are overrepresented due to the number of objects attributed to them, which can inflate their perceived presence in the dataset. In contrast, MoMA demonstrates a relatively more diverse distribution of nationalities, with a broader representation of artists from outside Western Europe and North America. This difference can be attributed to MoMA’s focus on modern and contemporary art, which inherently includes more global artistic movements and reflects a more recent shift toward inclusivity in artistic recognition.

Another key finding relates to the structure of representation itself. The analysis shows that representation is not simply about the number of artists from a given country but also about how frequently those artists appear within a collection. In the MET dataset, the same artist may be associated with multiple artworks, leading to a higher count of appearances compared to unique artist representation. This distinction is important because it highlights how institutional collecting practices can shape the interpretation of diversity. A museum may appear diverse when measured by total artwork counts, but less so when evaluated based on unique artists. MoMA’s dataset, which more clearly separates artists and artworks, provides a more balanced perspective in this regard.

Additionally, the use of artist birth years as a proxy for time reveals potential trends in representation over time. While the analysis primarily focuses on nationality, preliminary observations suggest that more recent artists—particularly those born in the twentieth century—exhibit greater geographic diversity compared to earlier periods. This aligns with broader shifts in the art world, including globalization, increased cross-cultural exchange, and evolving curatorial priorities that emphasize inclusivity. However, these changes appear gradual rather than transformative, indicating that historical biases still play a significant role in shaping museum collections.

Overall, the findings suggest that while both institutions have made some progress toward broader representation, their collections continue to reflect historical patterns of Western dominance. The differences between the MET and MoMA highlight how institutional focus, collection strategy, and historical context influence representation. These insights reinforce the idea that museums are not neutral spaces but active participants in constructing cultural narratives, with their collections shaping public understanding of art history and global artistic contributions.

---

## Future Work
While this analysis provides valuable insights into the relationship between geographic origin and artist representation, there are several opportunities for further research and refinement. One important direction for future work is the aggregation of nationalities into broader geographic regions. Instead of analyzing individual countries, grouping artists into regions such as North America, Western Europe, East Asia, Latin America, and Africa would allow for clearer comparisons and more meaningful interpretations of global representation patterns. This approach would also help mitigate inconsistencies in nationality labeling and provide a more holistic view of diversity across different parts of the world.

Another key area for expansion is time-based analysis. By leveraging the artist birth year data more systematically, future research could examine how representation has evolved across different historical periods. For example, dividing artists into cohorts based on birth decades or centuries would allow researchers to identify trends in diversity over time and assess whether museums have become more inclusive in recent years. This temporal perspective could also be combined with regional analysis to explore how representation of different geographic areas has changed, offering deeper insight into the impact of globalization and shifting curatorial priorities.

In addition to refining analytical methods, future work could improve how representation is measured. The current analysis primarily relies on counts of artwork-artist pairs, which may overrepresent artists with multiple works in a collection. A more nuanced approach would involve calculating metrics based on unique artists rather than total artwork entries. This would provide a clearer picture of diversity by focusing on how many distinct artists from each region are represented, rather than how frequently their works appear. Furthermore, weighting strategies could be developed to balance the influence of artists with large numbers of works, ensuring that representation metrics more accurately reflect diversity.

Expanding the scope of the dataset is another important avenue for future research. While this study focuses on two major institutions, incorporating additional museums—both within and outside the United States—would allow for a more comprehensive analysis of global representation. Including museums with different cultural, geographic, and institutional backgrounds could reveal whether the patterns observed in the MET and MoMA are consistent across the broader museum landscape or specific to these institutions. This expansion would strengthen the generalizability of the findings and provide a more robust understanding of representation in the art world.

Future work could also explore more nuanced dimensions of identity beyond nationality. Nationality alone may not fully capture an artist’s cultural background or influences, particularly in cases of migration, dual citizenship, or transnational artistic practice. Incorporating additional variables, such as place of birth, cultural affiliation, or artistic movement, could provide a richer and more accurate representation of diversity. While such data may not always be readily available, integrating these dimensions where possible would enhance the depth and interpretability of the analysis.

Finally, methodological improvements could further enhance reproducibility and scalability. Automating the entire data pipeline—from data acquisition and cleaning to analysis and visualization—using workflow tools would ensure that the process can be easily replicated and extended. This would be particularly valuable for incorporating new datasets or updating existing analyses as museum collections evolve. Additionally, integrating visualization tools to present findings in interactive formats could make the results more accessible to broader audiences, including researchers, curators, and the general public.

---

## Challenges
The process of cleaning, integrating, and analyzing the MET and MoMA datasets presented several significant challenges. One of the most prominent issues was the inconsistency in nationality data. The datasets contained a wide range of formatting irregularities, including duplicate values (e.g., “American|American”), trailing symbols (e.g., “American|”), variations in capitalization, and missing entries. These inconsistencies required extensive preprocessing, including string cleaning, standardization using mapping dictionaries, and clustering techniques in OpenRefine. Ensuring that all nationality values were consistent and comparable was essential for accurate analysis but required careful attention to detail and multiple iterations of cleaning.

Another major challenge involved handling records with multiple artists or multiple nationalities. In both datasets, some artworks were associated with more than one artist, and in certain cases, artists were linked to multiple nationalities. This created ambiguity in how to represent these relationships in a structured dataset. To address this, the data had to be transformed into a one-to-many format by splitting and exploding rows, ensuring that each artwork-artist-nationality combination was represented separately. While this approach improved analytical clarity, it also increased the size and complexity of the dataset, making subsequent processing more resource-intensive.

The size and structure of the MET dataset posed additional difficulties. Compared to the MoMA dataset, the MET data was significantly larger and less standardized, with artist and artwork information combined in a single file. This required additional steps to separate, clean, and restructure the data into a format comparable to MoMA’s two-table structure. Furthermore, the large file size created practical challenges for storage, processing, and uploading to platforms such as GitHub and OpenRefine. To manage this, it was necessary to reduce the dataset by selecting only relevant columns and filtering out incomplete or less useful records, balancing the need for efficiency with the preservation of meaningful information.

Finally, aligning the two datasets for comparative analysis required careful schema matching and consistency checks. Differences in column names, data types, and overall structure meant that direct comparison was not initially possible. Significant effort was needed to standardize variable names, ensure consistent data types, and apply the same cleaning logic across both datasets. This process highlighted the importance of methodological consistency when working with multiple data sources and underscored the challenges of integrating datasets that were not originally designed to be used together.

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

7. Run analysis **(`INSERT THE ANALYSIS FILE NAME`)** to generate results.
---

## References
- 
