# Task Updates:
For this milestone, we focused on data preparation. We cleaned the MoMA and MET datasets. Both datasets required us to handle missing data, inconsistent formatting, and to restructure some fields to make them more usable. We overall made a lot of progress towards creating usable datasets to use in our next steps of merging the two datasets to use for our exploratory analysis.

# Timeline:

# Changes to Project Plan:
There have been no significant changes to our original project plan. We are on track with the tasks that we outlined in the Project Plan submission, and we were able to do the data cleaning and preparation plans as expected. However, we will stay flexible if we do encounter issues that require us to pivot with our Project Plan.

# Challenges and Problems:
One challenge that Renee encountered was missing values in the MoMA dataset. One issue was that the artworks' data included duplicated rows containing mostly `NAN` values with "New York City Transit Authority" as the title. For context, MoMA has all data in two datasets (one being about the artist and one being about the artwork) so we had to merge them to be consistent with the MET data. We believe that the rows were artifacts from merging and not actual observations so we filtered out rows missing `objectid   and `accessionnumber .` 

Another challenge from the MoMA dataset was the inconsistent nationality data. There were multiple variations of the same country, like "East German" and "West German" referring to the two Germanies before the war, and things like "American, born in Germany." We standardized them to a single label.

Additionally, there were messy date fields. For example, some of the values were like "c. 1950" or ranges like "1945-46." I extracted the first valid four-digit year into a new column and did the same for the date acquired to be consistent.

Overall, these challenges were able to be resolved through targeted cleaning.

# Contributions:
### Renee:
For the milestone, I was in charge of preparing and cleaning the MoMA dataset by merging the Artist.txt and Artworks.txt files. I loaded both datasets and standardized the column names by removing extra spaces and underscores so they'd be consistent. One issue I had was that some artworks had multiple artists. So, I separated the IDs so each row only had one artist linked to one artwork before merging. 

Another issue I fixed was the messy date column. I extracted the first year listed and created a new column with it. I did the same with the `dateacquired` column.

Additionally, I standardized the nationalities by grouping them with a nationality map and creating a function to replace things like "UK," "Welsh," etc into just "British or "U.S.," "United States," etc., into just "American." There were more like "Soviet" and "Russia", or East/West Germany, when referring to pre-war countries. For these cases, I simplified it into just the current, modern-day name/country in that location. I understand that causes the dataset to lose some of the nuances of historical countries; however, we want to just look at the broader geographic patterns, so making it more simplified and consistent aligns with our goals, even with the downside of data loss.

After merging the datasets, I also removed invalid rows that were missing key artwork identifiers and duplicate rows. Most of the duplicate rows were the `NAN` values with "New York City Transit Authority" as the title mentioned before, so there was no worry of important information being lost. The final result was a cleaned dataset, which is now ready for the next step of analysis.
