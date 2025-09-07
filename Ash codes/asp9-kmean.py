
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=4, random_state=0)
kmeans = KMeans(n_clusters=4, n_init=10).fit(X)

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', s=50)
x, y = kmeans.cluster_centers_.T
plt.plot(x, y, "rX")
plt.title("K-means Clustering")
plt.show()

