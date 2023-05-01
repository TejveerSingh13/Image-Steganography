import sys
import cv2
import numpy as np

# Get the file paths from command line arguments
original_path = sys.argv[1]
encoded_path = sys.argv[2]

# Load the original and edited images
original_img = cv2.imread(original_path)
edited_img = cv2.imread(encoded_path)

# Convert the images to float32 data type
original_img = original_img.astype(np.float32)
edited_img = edited_img.astype(np.float32)

# Calculate the mean squared error (MSE) between the original and edited images
mse_R = np.mean((original_img[:,:,0] - edited_img[:,:,0]) ** 2)
mse_G = np.mean((original_img[:,:,1] - edited_img[:,:,1]) ** 2)
mse_B = np.mean((original_img[:,:,2] - edited_img[:,:,2]) ** 2)
mse = (mse_R + mse_G + mse_B) / 3

# Calculate the maximum pixel value
max_pixel_value = 255

# Calculate the PSNR using the formula PSNR = 20 * log10(max_pixel_value / sqrt(MSE))
psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))

# Print the PSNR value
print('PSNR value: {:.2f}dB'.format(psnr))
