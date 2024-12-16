import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# Load data and model
df = pd.read_pickle("job_embeddings.pkl")
model = load_model("job_recommender_model.h5")

# User preferences
user_skills = ["Python", "SQL", "Machine Learning"]
user_experience = 2

# Encode user input
user_input = encode_user_input(user_skills, user_experience)
skill_input = user_input[:-1].reshape(1, -1)
experience_input = np.array([user_input[-1]]).reshape(1, -1)

# Predict job scores
predictions = model.predict([skill_input, experience_input]).flatten()

# Get top 5 jobs
top_5_indices = predictions.argsort()[-5:][::-1]
recommended_jobs = df.iloc[top_5_indices]

# Display recommendations
print("Top 5 Recommended Jobs:")
print(recommended_jobs[["jobTitle", "Location", "cluster"]])
