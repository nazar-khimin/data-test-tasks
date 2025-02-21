import numpy as np
from collections import deque

class DBSCAN:
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps  # Maximum distance to consider a neighbor
        self.min_samples = min_samples  # Minimum points to form a cluster
        self.labels = []  # Cluster labels for each point
        self.noise_label = -1  # Label for noise points

    def fit(self, data):
        """
        Perform DBSCAN clustering on the input data.
        """

        data = np.array(data)
        self.labels = -1 * np.ones(len(data))  # Initialize all points as noise
        cluster_id = 0

        for point_idx, point in enumerate(data):
            if self.labels[point_idx] != -1:  # Skip already processed points
                continue

            neighbors = self.region_query(data, point_idx)
            if len(neighbors) < self.min_samples:
                self.labels[point_idx] = self.noise_label  # Label as noise
            else:
                self.expand_cluster(data, point_idx, neighbors, cluster_id)
                cluster_id += 1

    def expand_cluster(self, data, point_idx, neighbors, cluster_id):
        """
        Expand the cluster from the core point.
        """
        self.labels[point_idx] = cluster_id
        queue = deque(neighbors)

        while queue:
            neighbor_idx = queue.popleft()
            if self.labels[neighbor_idx] == self.noise_label:
                self.labels[neighbor_idx] = cluster_id  # Change noise to border point
            if self.labels[neighbor_idx] != -1:
                continue

            self.labels[neighbor_idx] = cluster_id
            new_neighbors = self.region_query(data, neighbor_idx)
            if len(new_neighbors) >= self.min_samples:
                queue.extend(new_neighbors)


    def region_query(self, data, point_idx):
        """
        Find all points within `eps` distance of the given point.
        """
        neighbors = [i for i in range(len(data)) if self.euclidean_distance(data[point_idx], data[i]) <= self.eps]
        return neighbors


    @staticmethod
    def euclidean_distance(point1, point2):
        """
        Calculate the Euclidean distance between two points.
        """
        return np.sqrt(np.sum((np.array(point1) - np.array(point2)) ** 2))

# Visualization function for clusters
def plot_clusters(data, labels):
    """
    Visualize DBSCAN results.
    """
    import matplotlib.pyplot as plt
    data = np.array(data)
    unique_labels = set(labels)

    for label in unique_labels:
        if label == -1:
            # Noise points
            color = "red"
            label_name = "Noise"
        else:
            color = np.random.rand(3,)
            label_name = f"Cluster {label}"

        cluster_points = data[np.array(labels) == label]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=color, label=label_name)

    plt.title("DBSCAN Clustering")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()


# Main Execution
if __name__ == "__main__":
    data = [
        [1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]
    ]
    eps = 2
    min_samples = 2

    # Perform DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan.fit(data)

    print("Labels:", dbscan.labels)  # Output cluster and noise labels
    plot_clusters(data, dbscan.labels)  # Visualize results
