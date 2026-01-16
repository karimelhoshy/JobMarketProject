# Import required libraries
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input, Embedding, Flatten, Concatenate
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Step 1: Load and Merge Datasets
def load_data():
    print("Loading data...")
    requirements_df = pd.read_csv("jobRequirements.csv")
    job_data_df = pd.read_csv("jobData.csv")
    merged_df = pd.merge(job_data_df, requirements_df, on="jobID", how="inner")
    return merged_df

# Step 2: Generate Embeddings for Text Fields
def generate_embeddings(df):
    print("Generating embeddings...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    text_fields = ["jobTitle", "job function", "industries"]
    for field in text_fields:
        print(f"Generating embeddings for {field}...")
        df[f"{field}_embedding"] = df[field].apply(
            lambda x: model.encode(str(x)).tolist()
        )
    return df

# Step 3: Perform Clustering
def perform_clustering(df):
    print("Performing clustering...")
    embedding_cols = [col for col in df.columns if "embedding" in col]
    X = np.hstack(df[embedding_cols].values)
    
    kmeans = KMeans(n_clusters=10, random_state=42)
    df['cluster'] = kmeans.fit_predict(X)
    
    # Dimensionality reduction for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['cluster'], cmap='viridis')
    plt.title("Job Clusters")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.colorbar(label="Cluster")
    plt.show()
    
    return df

# Step 4: Build and Train Recommender System
def build_recommender_system(df):
    print("Building recommender system...")
    skill_cols = [col for col in df.columns if col.startswith("Skill")]
    skills_data = df[skill_cols].values
    experience_data = df["Experience"].values.reshape(-1, 1)
    labels = to_categorical(df["cluster"].values)
    
    # Neural network architecture
    skill_input = Input(shape=(len(skill_cols),), name="Skills")
    experience_input = Input(shape=(1,), name="Experience")
    
    x = Dense(128, activation='relu')(skill_input)
    x = Dense(64, activation='relu')(x)
    experience_embedding = Dense(8, activation='relu')(experience_input)
    x = Concatenate()([x, experience_embedding])
    x = Dense(32, activation='relu')(x)
    output = Dense(labels.shape[1], activation='softmax')(x)
    
    model = Model(inputs=[skill_input, experience_input], outputs=output)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    # Train model
    model.fit([skills_data, experience_data], labels, epochs=10, batch_size=32)
    model.save("job_recommender_model.h5")
    print("Recommender system model saved.")
    return model

# Step 5: Job Recommendation
def recommend_jobs(df, model, user_skills, user_experience):
    print("Recommending jobs...")
    skill_cols = [col for col in df.columns if col.startswith("Skill")]
    
    # Encode user input
    skill_vec = np.array([1 if skill in user_skills else 0 for skill in skill_cols])
    experience_vec = np.array([user_experience])
    
    # Predict job scores
    skill_input = skill_vec.reshape(1, -1)
    experience_input = experience_vec.reshape(1, -1)
    predictions = model.predict([skill_input, experience_input]).flatten()
    
    # Get top 5 job recommendations
    top_5_indices = predictions.argsort()[-5:][::-1]
    recommended_jobs = df.iloc[top_5_indices]
    
    print("Top 5 Recommended Jobs:")
    print(recommended_jobs[["jobTitle", "Location", "cluster"]])

# Main Function
def main():
    # Load and preprocess data
    df = load_data()
    df = generate_embeddings(df)
    df = perform_clustering(df)
    
    # Build and train recommender system
    model = build_recommender_system(df)
    
    # User preferences
    user_skills = ["Python", "SQL", "Machine Learning"]
    user_experience = 3
    
    # Recommend jobs
    recommend_jobs(df, model, user_skills, user_experience)

if __name__ == "__main__":
    main()
