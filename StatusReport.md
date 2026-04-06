# Task Updates:
For this milestone, we focused on data preparation. We cleaned the MoMA and MET datasets. Both datasets required us to handle missing data, inconsistent formatting, and to restructure some fields to make them more usable. We overall made a lot of progress towards creating usable datasets to use in our next steps of merging the two datasets to use for our exploratory analysis.

# Timeline:

| Task | Status | Description | Expected Completion |
|------|--------|------------|--------------------|
| Project Planning | Completed | Defined research question and outlined project scope | Completed |
| Dataset Acquisition | Completed | Collected datasets from the Metropolitan Museum of Art and MoMA | Completed |
| Initial Data Exploration | Completed | Reviewed dataset structures and identified relevant variables | Completed |
| Data Cleaning | In Progress | Filtering relevant columns, removing missing values, and handling inconsistencies | April 7 |
| Data Standardization | In Progress | Standardizing fields such as artist nationality for consistency across datasets | April 9 |
| Data Integration | Not Started | Plan to combine MET and MoMA datasets for comparative analysis | April 12 |
| Data Analysis | Not Started | Analyze how artist origin influences representation in museums | April 14 |
| Visualization | Not Started | Create charts and visualizations to present findings | April 16 |
| Final Report Writing | Not Started | Compile results, interpretations, and conclusions into final report | April 18 |
| Final Review & Submission | Not Started | Review project, finalize deliverables, and submit | April 20 |

# Changes to Project Plan:
There have been no significant changes to our original project plan. We are on track with the tasks that we outlined in the Project Plan submission, and we were able to do the data cleaning and preparation plans as expected. However, we will stay flexible if we do encounter issues that require us to pivot with our Project Plan.

# Challenges and Problems:

### MoMA dataset
One challenge that Renee encountered was missing values in the MoMA dataset. One issue was that the artworks' data included duplicated rows containing mostly `NAN` values with "New York City Transit Authority" as the title. For context, MoMA has all data in two datasets (one being about the artist and one being about the artwork) so we had to merge them to be consistent with the MET data. We believe that the rows were artifacts from merging and not actual observations so we filtered out rows missing `objectid   and `accessionnumber .` 

Another challenge from the MoMA dataset was the inconsistent nationality data. There were multiple variations of the same country, like "East German" and "West German" referring to the two Germanies before the war, and things like "American, born in Germany." We standardized them to a single label.

Additionally, there were messy date fields. For example, some of the values were like "c. 1950" or ranges like "1945-46." I extracted the first valid four-digit year into a new column and did the same for the date acquired to be consistent.

Overall, these challenges were resolved through targeted cleaning.

### Metropolitan Museum of Art dataset
One of the main challenges encountered was the size and complexity of the Metropolitan Museum of Art dataset. The dataset contains a large number of columns, many of which are not relevant to the research question. To address this, I carefully reviewed the dataset and selected only the columns necessary for analyzing artist origin, such as artist name, nationality, and department.

Another challenge was the presence of missing and incomplete data. A significant number of records had missing values for key attributes such as artist name and nationality. Since these fields are essential for the analysis, I removed rows with missing or invalid entries to ensure the reliability of the results.

In addition, the dataset contained inconsistencies in how artist nationalities were recorded. For example, some entries included duplicated values or multiple nationalities within a single field. I resolved this by standardizing the nationality column and extracting a single, consistent value for each artist.

There were also entries that did not correspond to individual artists, such as museum departments or collections.
These entries could distort the analysis, so they were filtered out to ensure that the dataset focuses only on individual artists.

Finally, duplicate records were identified within the dataset. These duplicates were removed to prevent overcounting and to improve the overall accuracy of the analysis.

Moving forward, I will continue refining the dataset and validating the cleaned data before proceeding to analysis and visualization.

# Contributions:
### Renee:
For the milestone, I was in charge of preparing and cleaning the MoMA dataset by merging the Artist.txt and Artworks.txt files. I loaded both datasets and standardized the column names by removing extra spaces and underscores so they'd be consistent. One issue I had was that some artworks had multiple artists. So, I separated the IDs so each row only had one artist linked to one artwork before merging. 

Another issue I fixed was the messy date column. I extracted the first year listed and created a new column with it. I did the same with the `dateacquired` column.

Additionally, I standardized the nationalities by grouping them with a nationality map and creating a function to replace things like "UK," "Welsh," etc into just "British or "U.S.," "United States," etc., into just "American." There were more like "Soviet" and "Russia", or East/West Germany, when referring to pre-war countries. For these cases, I simplified it into just the current, modern-day name/country in that location. I understand that causes the dataset to lose some of the nuances of historical countries; however, we want to just look at the broader geographic patterns, so making it more simplified and consistent aligns with our goals, even with the downside of data loss. There were also input errors. For example, one of the artists was listed as "  Japanese) (Japanese," so cleaning this up to be just "Japanese" was important. 

After merging the datasets, I also removed invalid rows that were missing key artwork identifiers and duplicate rows. Most of the duplicate rows were the `NAN` values with "New York City Transit Authority" as the title mentioned before, so there was no worry of important information being lost. The final result was a cleaned dataset, which is now ready for the next step of analysis.

### Sarah:
For this milestone, I was responsible for working with the Metropolitan Museum of Art dataset. My contributions included acquiring the dataset, exploring its structure, and identifying the relevant columns needed for the project. I implemented data cleaning procedures using Python, including removing missing values, filtering irrelevant entries, and eliminating duplicate records.

I also addressed inconsistencies in the dataset, particularly within the artist nationality field, by standardizing the data to ensure accurate analysis. Overall, my work focused on preparing a clean and reliable dataset that can be used to analyze how the geographic origin of artists influences their representation in museums.
