import random
import numpy as np
import matplotlib.pyplot as plt


# K-Means Clustering Implementation
class KMeans:
    def __init__(self, k=3, max_iters=100, random_state=42):
        self.k = k  # Number of clusters
        self.max_iters = max_iters  # Max iterations to converge
        self.centroids = []  # Cluster centroids
        self.labels = []  # Labels for data points
        self.random_state = random_state  # Seed for random number generator

    def fit(self, data, initial_centroids=None):
        """
        Fits K-Means to the provided data.
        """
        data = np.array(data)
        np.random.seed(self.random_state)

        # Initialize centroids
        if initial_centroids is not None:
            self.centroids = np.array(initial_centroids)
        else:
            self.centroids = data[np.random.choice(data.shape[0], self.k, replace=False)]

        for _ in range(self.max_iters):
            # Assign labels to each data point based on centroids
            self.labels = [self.get_cluster_label(point) for point in data]

            # Update centroids
            new_centroids = [self.compute_centroid(data[np.array(self.labels) == i]) for i in range(self.k)]

            # Check for convergence
            if np.allclose(self.centroids, new_centroids, atol=1e-4):
                break

            self.centroids = new_centroids

    def predict(self, point):
        """
        Predicts the cluster label for a given point.
        """

        return self.get_cluster_label(point)

    def get_cluster_label(self, point):
        """
        Helper function to determine a cluster label.
        """

        distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
        return distances.index(min(distances))

    @staticmethod
    def euclidean_distance(point1, point2):
        """
        Computes Euclidean distance between two points.
        """
        return np.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

    @staticmethod
    def compute_centroid(cluster):
        """
        Computes the centroid of a cluster.
        """

        return np.mean(cluster, axis=0).tolist()


# Visualization function
def plot_clusters(data, labels, centroids):
    """
    Visualizes clustered data points.
    """
    data = np.array(data)
    labels = np.array(labels)
    centroids = np.array(centroids)

    plt.figure(figsize=(8, 6))
    for i in range(len(centroids)):
        plt.scatter(data[labels == i, 0], data[labels == i, 1], label=f'Cluster {i + 1}')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
    plt.title('K-Means Clustering')
    plt.xlabel('Annual Income ($1000)')
    plt.ylabel('Spending Score')
    plt.legend()
    plt.show()


# Main Execution
if __name__ == "__main__":
    # Input Data
    data = [
        [15, 39], [15, 81], [16, 6], [16, 77], [17, 40],
        [18, 6], [18, 94], [19, 3], [19, 72], [20, 44]
    ]

    # Step 1: Train K-Means
    kmeans = KMeans(k=3)
    kmeans.fit(data)

    # Step 2: Visualize Results
    print("Centroids:", kmeans.centroids)
    print("Labels:", kmeans.labels)
    plot_clusters(data, np.array(kmeans.labels), kmeans.centroids)
