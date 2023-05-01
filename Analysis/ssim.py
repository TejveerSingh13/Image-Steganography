import sys
from skimage import io
from skimage.metrics import structural_similarity as ssim

# Get the file paths from command line arguments
original_path = sys.argv[1]
encoded_path = sys.argv[2]

# Load the original and encoded images
original_img = io.imread(original_path)
encoded_img = io.imread(encoded_path)

# Compute the SSIM for each color channel
ssim_r = ssim(original_img[:,:,0], encoded_img[:,:,0], multichannel=False)
ssim_g = ssim(original_img[:,:,1], encoded_img[:,:,1], multichannel=False)
ssim_b = ssim(original_img[:,:,2], encoded_img[:,:,2], multichannel=False)
# ssim_A = ssim(original_img, encoded_img, multichannel=True)

# Print the SSIM values for each channel
print('SSIM for Red channel:', ssim_r)
print('SSIM for Green channel:', ssim_g)
print('SSIM for Blue channel:', ssim_b)
print('Avg SSIM :', (ssim_r + ssim_b + ssim_g)/3)