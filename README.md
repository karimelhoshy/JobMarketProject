# JobMarketProject

## Project Overview

This project provides insights into the job market by analyzing the demand for skills and experience across various job areas, companies, and industries. Utilizing Databricks, data is stored on S3, analyzed, and visualized with Power BI.

# Datasets

## jobRequirements.csv
jobID: Unique identifier for the job. <br>
Degree: The degree required (e.g., undergraduate, graduate, postgraduate).<br>
Experience: Years of experience required.<br>
Skill1 to Skill29: Various skills required for the job.

## jobData.csv
companyName: The name of the company. <br>
DatePosted: The date the job was posted. <br>
jobTitle: The title of the job. <br>
job function: The function of the job. <br>
employment type: The type of employment (e.g., full-time). <br>
seniority level: The seniority level required (e.g., entry level). <br>
industries: The industry of the company. <br>
Location: The location of the job. <br>
jobID: Unique identifier for the job, matching with requirementsFinal.csv. <br>
Standardized Job Title: Standardized job title. <br>
Job Area: The area of the job (e.g., Data Science, Cybersecurity, Web and Mobile Development).

## combinedUnpivoted.csv
Joined jobData.csv and jobRequirements.csv on jobID to simplify visualizations in Power BI <br>

## Tools and Technologies
- **Databricks**: For data processing and warehousing.
- **AWS S3**: For data storage.
- **Power BI**: For data visualization.
- **SQL and Python**: For data querying and preprocessing.

## Visualizations
Interactive Power BI dashboards visualize the key insights and trends in the job market. Here is an overview of some of the insights:
![My Image](https://github.com/karimelhoshy/JobMarketProject/blob/main/dashboard.png)
![My Image](https://github.com/karimelhoshy/JobMarketProject/blob/main/jobTitlesPerIndustry.png)

## Full Report
For a detailed report on the project, including methodologies, analysis, and findings, please refer to the [full report](https://github.com/karimelhoshy/JobMarketProject/blob/main/jobMarketProjectReport.pdf).


# Getting Started

## Prerequisites
- Databricks account (recommended)
- AWS S3 account
- Power BI account
- Python (with necessary libraries)


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```


2. **Set up your environment**:
- Install required Python libraries:
```bash
pip install -r requiredLibraries.txt
```

3. **Configure Databricks and AWS S3**:
- Set up your Databricks workspace and AWS S3 buckets.
- Update the configuration file with your Databricks and AWS credentials.

4. **Run the scripts**:
- Execute the scripts to collect, clean and load data into Databricks and perform initial transformations.

5. **Visualize data with Power BI**:
- Open the Power BI file and connect it to the processed data for visualization.


## Usage

1. **Run the Data Collection Notebook:**
   - Start by running `dataCollection.ipynb` to gather and collect the necessary data.

2. **Run the Data Exploration Notebook:**
   - Next, run `dataExploration.ipynb` to perform initial exploration and analysis of the collected data.

3. **Run the Data Cleaning and Transformation Notebook:**
   - Finally, run `dataCleaningandTransformation.ipynb` to clean and transform the data. This will generate an unpivoted CSV file ready for visualization.

4. **Visualize Data with Power BI:**
   - After generating the unpivoted CSV file, import it into Power BI.
   - Use Power BI to create interactive dashboards and visualizations based on the cleaned and transformed data.


## Customization

You can adjust the scripts and notebooks to target specific locations, job titles, skills, job areas, or other parameters. Modify the filtering criteria in the data processing scripts to tailor the insights to your needs. For example:
- To focus on a particular location or emphasize specific job titles, modify the location and/or job title filter during the data collection step.
- To target specific skills, adjust the skill filtering criteria in the data cleaning and transformation step.
- To focus on particular job areas, modify the job area filter during the data cleaning and transformation process.


## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


## Contact

For questions or further information, please contact me at:
   - **Email**: [karim.elhoshy@mail.mcgill.ca](mailto:karim.elhoshy@mail.mcgill.ca)
   - **LinkedIn**: [thekarimelhoshy](https://linkedin.com/in/thekarimelhoshy)
   - **GitHub**: [karimelhoshy](https://github.com/karimelhoshy)
