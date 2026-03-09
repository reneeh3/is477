# Overview:

The goal of this project is to see how the locational origin of artists influences their representation in museums. Throughout history, museums (outside of private collectors) play one of the most important roles in preserving culture by deciding which artists and types of artworks are exhibited. However, representation might change depending on the background of the artist. We aim to analyze whether artists from certain regions are more frequently represented than others and how this representation has changed over time.

In order to research this question, we took datasets from major museums, the Metropolitan Museum of Art and the Museum of Modern Art. These datasets have metadata about the artworks, artists, names, nationalities, artwork titles, and dates. By combining these two major datasets, we can make a unified representation of patterns across institutions. 

The analysis overall will look into whether certain regions are represented more frequently, and whether that’s changed over time. We will be collecting and cleaning the data, combining records from the two museums, doing exploratory data analysis, and creating visualizations for easy analysis of the trends over time. The final results will provide insight into how museums reflect artistic diversity over time.

# Team:
Our team has two people: Sarah Kim (yewonwk2) and Renee Huang (reneh3). Each member will head different stages of the project while collaborating on all parts of the project.

Sarah will locate and prepare the datasets for analysis, such as downloading the data, loading the datasets, and conducting basic examination. Sarah will also lead the integration process by identifying shared attributes between datasets and finding the best methods to merge the two datasets.

Renee will focus on preparing the datasets for analysis and conducting the first rounds of data analysis. Since this is the bulk of the project, both members will collaborate, but Renee is primarily responsible for these steps. Renee will need to clean missing or inconsistent data (especially with standardizing locational fields) and prepare time-related variables. 
As a group, both members will conduct in depth data analysis and create visualizations that illustrate patterns in geographic representation and changes over time. Both team members will collaborate on interpreting results, writing reports, and explaining methodology/findings.

# Research Question:
The overarching research question for this project is:
**How does the geographic origin of artists influence their representation in major museums?**

To answer this question, we will explore these related questions:
Which geographic regions/countries are most represented in the Metropolitan Museum of Art and the Museum of Modern Art?
Are there differences in representation between the two museums?
Do certain regions show increasing or decreasing representation in museum collections across different time periods?

These questions help frame the overall representation patterns and how they evolve. By looking at geographic origin alongside time-based variables, we can explore whether museum collections have become more globally diverse over time or less diverse over time. We can also potentially see the effects of global events on the representation of regions (such as whether decreases of certain regions may be correlated with events like wars or political tensions).

# Datasets:
We plan on using two verified and public museum datasets called the Metropolitan Museum of Art Open Access dataset and the Museum of Modern Art collection dataset. 


### Metropolitan Museum of Art Open Access Dataset:
Source: https://github.com/metmuseum 

The Metropolitan Museum of Art has an open-access dataset with metadata about artworks in the museum’s collection. The dataset includes information about artworks, the artists, and geographic information associated.

Some of the relevant variables are:

Object ID and Object Number: unique identifiers for each artwork
Title: the title of the art
Artist Display Name: the name of the artist associated with the work
Artist Nationality:  the nationality of the artist
Artist Begin Date and Artist End Date: the birth and death years of the artist
Artist Gender: gender of the artist
Object Date, Object Begin Date, and Object End Date: dates of creation of the artwork
Department: Department that houses the object
Country, Region, Subregion, City, and other geographic attributes: as the name suggests, specific geographic information as available
Medium, Dimensions, and Classification:  information about the physical characteristics the artwork


### Museum of Modern Art (MoMA) Collection Dataset:
Source: https://github.com/MuseumofModernArt/collection 

The Museum of Modern Art has two primary datasets: Artists.csv and Artworks.csv. 
The Artists dataset contains metadata describing individual artists with these variables:

ConstituentID: a unique identifier for each artist
<br>
DisplayName: the artist’s name
<br>
Nationality: the artist’s nationality
<br>
ArtistBio: a short biographical description
<br>
Gender: gender of the artist
<br>
BeginDate and EndDate: the birth and death years of the artist
<br>
Wiki QID and ULAN: identifiers linking the artist to external knowledge databases
<br>
<br>
The Artworks dataset includes:
<br>
Title: the title of the artwork
<br>
Artist: the name of the artist
<br>
ConstituentID: identifier linking artworks to artists in the Artists dataset
<br>
Date: the year when the artwork was created
<br>
DateAcquired: the date when the museum acquired the artwork
<br>
Medium: the materials used to create the artwork
<br>
Dimensions: physical size of the artwork
<br>
Department: museum department containing the work
<br>
Classification: what type of art the artwork is
<br>
ObjectID: unique identifier for each artwork
<br>
URL and ImageURL: pictures of the art, or external relevant links
<br>
<br>
The primary variables we will use for integration include: 
<br>
‘Artist Display Name’ from the Met dataset and ‘DisplayName’ from the MoMA datasets
<br>
‘Artist Nationality’ (Met) and ‘Nationality’ (MoMA) to determine geographic origin
<br>
‘Artist Begin Date / End Date’ (Met) and ‘BeginDate / EndDate’ (MoMA) to help validate artist identity
<br>
<br>
We also might look into the acquisition dates of the artwork, since there might be a gap in time between the creation of the artworks and the acquisition of the artworks by the museums. Physical descriptions of the artworks may not be as relevant to our focus questions, so those may be dropped during analysis to reduce clutter.

The MoMA dataset links artists and artworks using ConstituentID, which is what we’ll use to combine those datasets before combining them with the Met dataset. By combining these datasets, we will be able to compare how artists from different geographic origins are represented across two major museum collections and see the patterns of representation over time.

# Timeline:

### Week 1 - Initial Review and Data Collection (Sarah)
- Download datasets from the Metropolitan Museum of Art and MoMa
- Review data structure
- Identify relevant variables needed for analysis
- Conduct initial analysis for missing values
- Load dataset into workbook

### Week 2 - Data Cleaning (Renee)
- Clean datasets by handling missing values and eliminating irrelevant data
- Standardize key variables including nationality, artists, and dates
- Prepare variables for merging

### Week 3 - Data Integration (Sarah)
- Identify overlapping attributes between Met and MoMa datasets
- Combine datasets into a unified structure
- Validate merged records to ensure consistency

### Week 4 - Data Analysis (Collaborative)
- Analyze the distribution of artists by region
- Compare representations between different museums
- Explore representation during different time periods
- Generate summary statistics and identify trends

### Week 5 - Visualization (Collaborative)
- Create visualizations for the trends identified
- Interpret patterns in artist representations during different time periods
- Identify major trends

### Week 6 - Final Report (Collaborative)
- Document methodology, analysis, and results
- Prepare final report
- Review findings, explanations and limitations


# Constraints:

There could be some possible limitations and challenges with our datasets that may affect our overall project. One challenge could be incomplete data. Some artists have missing nationality and creation dates. This could especially apply to artworks that were created a long time ago, as some historical records may be incomplete. As a result, some entries may need to be excluded from our analysis or require additional data cleaning. Second, there could be differences in dataset structures between the Met and MoMa datasets. The datasets could have different formatting and variable names which could make it difficult for the integration of the two datasets. Another potential limitation could be that there could be inconsistencies in the geographic information. The nationality fields may have different formats, which requires extra attention to detail. For example, “United States”, “US”,”USA”,and ”American” all mean the same geographic location, but need extra standardization. Additionally, the museum collections could only be a representation of the institutional collections rather than representing the global population of artists. Finally, although the datasets are open to the public, there could still be limitations in accuracy, because it solely depends on the museum records that are prone to change over time.


# Gaps:

There are several areas where additional clarification may be required. First, we need to determine the best method for organizing the geographic information. Nationalities need to be categorized into broader regions to make it easier for comparisons. Second, when comparing the process for artists across two museums, there could be a need for validation as artist names alone may not always identify the same person. Third, we may need to handle artists that could possibly have multiple nationalities which could affect geographic analysis. Finally, as we conduct exploratory data analysis, we may need to use additional variables that could improve the quality of our analysis of trends. These gaps will be addressed as we conduct further analysis and refine our approach.


