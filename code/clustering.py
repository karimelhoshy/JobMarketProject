import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load embedded data
df = pd.read_pickle("job_embeddings.pkl")

# Combine embeddings into a single matrix
embedding_cols = [col for col in df.columns if "embedding" in col]
X = np.hstack(df[embedding_cols].values)

# Dimensionality reduction (optional for visualization)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Perform clustering
kmeans = KMeans(n_clusters=10, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# Visualize clusters
plt.figure(figsize=(10, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['cluster'], cmap='viridis')
plt.title("Job Clusters")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.colorbar(label="Cluster")
plt.show()

# Save clustered data
df.to_csv("clustered_jobs.csv", index=False)
