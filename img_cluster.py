import cv2
import numpy as np
from sklearn.cluster import KMeans
import os

# Path to the folder containing shape images
# trouble shoot so i will cluster shapes on image
folder_path = '/Users/jamarw/Documents/GitHub/imagemixer/n3'

# Function to load images from folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

# Load images from the folder
images = load_images_from_folder(folder_path)

# Convert images to grayscale and flatten them
gray_images = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in images]
flattened_images = [img.flatten() for img in gray_images]

# Convert flattened images to numpy array
data = np.array(flattened_images)

# Perform KMeans clustering
num_clusters = 3  # You can adjust this based on your needs
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(data)

# Assign labels to each image
labels = kmeans.labels_

# Create a dictionary to store clustered images
clustered_images = {}
for i, label in enumerate(labels):
    if label not in clustered_images:
        clustered_images[label] = []
    clustered_images[label].append(images[i])

# Display the clustered images
for cluster, images in clustered_images.items():
    print(f"Cluster {cluster}: {len(images)} images")
    for img in images:
        cv2.imshow(f"Cluster {cluster}", img)
        cv2.waitKey(0)