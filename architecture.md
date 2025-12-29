# Architecture

## Current Pipeline

```
LinkedIn --> Python Scripts --> S3 --> Databricks --> Power BI
(Scraping)   (Notebooks)      (Raw)   (Transform)    (Viz)
```

```
┌─────────────────────────────────────────────────────────────────┐
│                         EXTRACT                                 │
│  ┌──────────┐      ┌──────────────────┐      ┌──────────┐      │
│  │ LinkedIn │ ---> │ dataCollection.  │ ---> │   S3     │      │
│  │   API    │      │     ipynb        │      │  (JSON)  │      │
│  └──────────┘      └──────────────────┘      └────┬─────┘      │
└────────────────────────────────────────────────────┼────────────┘
                                                     │
                                                     v
┌─────────────────────────────────────────────────────────────────┐
│                        TRANSFORM                                │
│  ┌──────────────────┐      ┌──────────────────────────┐        │
│  │ dataExploration. │ ---> │ dataCleaningand          │        │
│  │     ipynb        │      │ Transformation.ipynb     │        │
│  └──────────────────┘      └───────────┬──────────────┘        │
│                                        │                        │
│            Databricks (Spark SQL)      │                        │
└────────────────────────────────────────┼────────────────────────┘
                                         │
                                         v
┌─────────────────────────────────────────────────────────────────┐
│                          LOAD                                   │
│  ┌──────────────────┐      ┌──────────────────┐                │
│  │   CSV Files      │ ---> │    Power BI      │                │
│  │ (combinedUnpiv.) │      │   Dashboard      │                │
│  └──────────────────┘      └──────────────────┘                │
└─────────────────────────────────────────────────────────────────┘
```

## What's Missing (Growth Opportunities)

**Data Modeling**
- No star/snowflake schema (flat CSVs)
- Skills as 29 columns instead of normalized junction table
- No dimension tables (companies, skills, industries)

**ETL Pipeline Architecture**
- No orchestration (Airflow, Dagster, Prefect)
- Jupyter notebooks instead of modular Python code
- No idempotency - can't safely re-run
- No incremental loads (full refresh only)

**Scalability**
- Single-threaded scraping
- All data in memory (Pandas)
- Hardcoded paths, no config management
- No partitioning strategy

**Monitoring & Observability**
- No data quality checks (Great Expectations, dbt tests)
- No alerting on failures
- No data lineage tracking
- No freshness/SLA metrics

**Tooling & Ecosystem**
- No dbt for transformations
- No data catalog
- No CI/CD for pipelines
- No version control for data (Delta Lake versioning)

**Code Quality**
- Bare `except:` clauses swallowing errors
- No type hints or tests
- Business logic hardcoded (should be config files)
