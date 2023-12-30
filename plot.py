import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load your JSON data
with open('keypoints_val_results_0.json', 'r') as json_file:
    data = json.load(json_file)

# Extract keypoints and skeleton connections
keypoints = np.array(data[0]['keypoints'])
keypoints = keypoints.reshape(-1, 3)  # Reshape to (num_keypoints, 3)

skeleton = [[15, 13], [13, 11], [16, 14], [14, 12], [11, 12], [5, 11], [6, 12],
            [5, 6], [5, 7], [6, 8], [7, 9], [8, 10], [1, 2], [0, 1], [0, 2],
            [1, 3], [2, 4], [3, 5], [4, 6]]

# Separate x, y, and visibility values
x = keypoints[:, 0]
y = keypoints[:, 1]
v = keypoints[:, 2]

# Plot skeleton connections
for sk in skeleton:
    if np.all(v[sk] > 0):
        plt.plot(x[sk], y[sk], linewidth=1, color='red')

# Plot keypoints
plt.plot(x[v > 0], y[v > 0], 'o', markersize=5, markerfacecolor='red', markeredgecolor='k', markeredgewidth=2)

# Load and show the image
img_path = 'val/0.jpg'
img = mpimg.imread(img_path)
plt.imshow(img)

# Show the plot
plt.title('Keypoint Visualization on Your Image')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
# plt.gca().invert_yaxis()  # Invert Y-axis to match image coordinates
plt.show()
