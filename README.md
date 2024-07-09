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

## Key Analyses
1. **Skill Demand Analysis**: Identified the most in-demand skills across job postings.
2. **Experience and Degree Requirements**: Analyzed the relationship between required degrees, years of experience, and skill types.
3. **Company and Industry Analysis**: Assessed job posting trends by company and industry.
4. **Job Area Analysis**: Examined experience, degree requirements, and common skills by job area.


## Tools and Technologies
- **Databricks**: For data processing and warehousing.
- **AWS S3**: For data storage.
- **Power BI**: For data visualization.
- **SQL and Python**: For data querying and preprocessing.

## Visualizations
Interactive Power BI dashboards visualize the key insights and trends in the job market.
