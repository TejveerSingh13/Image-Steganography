import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Get the file paths from command line arguments
original_path = sys.argv[1]
encoded_path = sys.argv[2]

# Load the original and encoded image
original_img = cv2.imread(original_path)
encoded_img = cv2.imread(encoded_path)


# Split the channels of the original and encoded images
original_b, original_g, original_r = cv2.split(original_img)
encoded_b, encoded_g, encoded_r = cv2.split(encoded_img)

# Calculate the mean absolute difference between the pixel values in the original and encoded images
mae = np.mean(np.abs(original_img.astype(np.float32) - encoded_img.astype(np.float32)))
print('Mean Absolute Difference:', mae)

# Plot the histograms of the pixel values in each channel
fig, axs = plt.subplots(2, 3, figsize=(12,6))
colors = ['R', 'G', 'B']
for i, channel in enumerate([original_b, original_g, original_r]):
    axs[0,i].hist(channel.flatten(), bins=256, range=(0, 256), color='blue', alpha=0.5)
    axs[0,i].set_xlim([0, 256])
    axs[0,i].set_ylim([0, 10000])
    axs[0,i].set_title('Original Image - Channel ' + colors[i])
for i, channel in enumerate([encoded_b, encoded_g, encoded_r]):
    axs[1,i].hist(channel.flatten(), bins=256, range=(0, 256), color='green', alpha=0.5)
    axs[1,i].set_xlim([0, 256])
    axs[1,i].set_ylim([0, 10000])
    axs[1,i].set_title('Encoded Image - Channel ' + colors[i])
plt.show()

