import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Load data
requirements_df = pd.read_csv("jobRequirements.csv")
job_data_df = pd.read_csv("jobData.csv")

# Merge datasets
merged_df = pd.merge(job_data_df, requirements_df, on="jobID", how="inner")

# Select text fields for embedding
text_fields = ["jobTitle", "job function", "industries"]

# Load pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
for field in text_fields:
    print(f"Generating embeddings for {field}...")
    merged_df[f"{field}_embedding"] = merged_df[field].apply(
        lambda x: model.encode(str(x)).tolist()
    )

# Save embeddings
merged_df.to_pickle("job_embeddings.pkl")
