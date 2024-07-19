# JobMarketProject

## Project Overview

This project provides insights into the job market by analyzing the demand for skills and experience across various job areas, companies, and industries. Utilizing Databricks, data is stored on S3, analyzed, and visualized with Power BI.

# Datasets

## requirementsFinal.csv
jobID: Unique identifier for the job. <br>
Degree: The degree required (e.g., undergraduate, graduate, postgraduate).<br>
Experience: Years of experience required.<br>
Skill1 to Skill29: Various skills required for the job.

## jobDataFinal.csv
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
Job Area: The area of the job (e.g., Data Science).

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

## Getting Started

### Prerequisites
- Databricks account (recommended)
- AWS S3 account
- Power BI account
- Python (with necessary libraries)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```


2. **Set up your environment**:

- Install required Python libraries:
```bash
Copy code
pip install -r requirements.txt
Configure Databricks and AWS S3:
```

Set up your Databricks workspace and AWS S3 buckets.
Update the configuration file with your Databricks and AWS credentials.
Run data processing scripts:

Execute the data processing scripts to load data into Databricks and perform initial transformations.
Visualize data with Power BI:

Open the Power BI file and connect it to the processed data for visualization.
Usage

Running the Analysis
Follow the Jupyter notebooks provided in the notebooks directory to run the analysis.
Each notebook contains detailed instructions and explanations of the analysis steps.
Viewing the Dashboards
Open the Power BI file to interact with the dashboards and explore the job market insights.
Customization
The scripts and notebooks can be adjusted to focus on specific locations, job titles, or other parameters of interest. Modify the filtering criteria in the data processing scripts to tailor the insights to your needs. For example:
To filter by location, adjust the location filter in the data extraction or transformation steps.
To focus on specific job titles, update the job title filtering criteria accordingly.

