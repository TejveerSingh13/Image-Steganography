# Image-Steganography
This project extends the histogram shift code present at : https://github.com/vctrop/image_histogram_data_hiding
The original version of the project had some limitations, including the fact that it only took in a string and converted it into its ASCII 8-bit code for encoding in a cover image. Additionally, it converted all images into grayscale before encoding, which meant that only one channel per image could be encoded, resulting in a final encoded image that was also in grayscale.

In this version of the project, several enhancements have been made to improve its functionality and performance. Some of the notable changes include:

* A separate Huffman Encoding and Compression program has been added, which can take in any .txt file and sanitize the input to achieve a higher compression ratio after encoding. 
* This program saves the frequency table for the given secret data .txt file, which can be used as a key to decode the binary encoded data.
* The Histogram Shift algorithm has been modified to encode not just in grayscale, but also in any format color image. This is achieved by splitting the given cover image into its 3 channels (R, G, and B) and encoding in each channel, thereby increasing the data capacity. 
* The program then merges the three channels to form an encoded color image that is very similar to the original image.
* The Histogram Shift program provides an option to encode, decode or check the capacity of a given cover image, so that the user can select the best cover image based on the amount of data that needs to be hidden.
* Additionally, the program saves a separate enc_data.pkl file, which acts as a key to decode the encrypted image for the encoded binary data.

These changes enhance the overall functionality and efficiency of the project, making it more versatile and user-friendly.nary

## Project Structure
The ./Code directory contains the actual working code for the Huffman Encoding and Compression algorithm. This is the core of the project, and is responsible for encoding and compressing data.

The ./Analysis directory contains code and files that are used to analyze both the original and encoded images. This allows for a deeper understanding of the project and its impact on the data.

To understand the workings, rules, and dependencies of the project, please refer to the README.md file. This file provides an overview of the project and offers guidance on how to get started.

Finally, the project includes a requirements.txt file that lists all the dependencies and libraries used in the project. This file is essential for ensuring that the project runs smoothly and without error.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

Python3.x
Windows, Linux or any other OS supporting python3.x

### Installing

Run the following command to update PIP
```
pip install --upgrade pip
```
Then, Run command to install all the dependecy library in the parent directory
```
pip install -r requirements.txt
```
And you are all set with the required setup!

## Working

This section covers step by step instructions to run the given python files
### A. huffman.py
The huffman.py file included in this project is responsible for creating a frequency table for the input text file, and then using a priority queue to generate a Huffman tree. This tree is then used to encode the given secret text into binary format.
In addition to encoding, the huffman.py file is also capable of decoding an encoded binary back into plain text. This is accomplished using the frequency provided to the code during encoding.
Overall, the huffman.py file is a crucial component of this project, responsible for the core encoding and decoding functionality of the Huffman Encoding and Compression algorithm.

huffman.py on execution gives us two options:
#### 1. Encoding:
parameters : the text file containig the secret message that needs to be encoded.
return : saves the encoded binary in a .txt file and also saves the frequency table which is needed for decoding.
#### 2. Decoding:
parameters : the encoded binary in a .txt file and the frequency table which is needed for decoding.
return : saves the encoded binary in a .txt file and also saves the frequency table which is needed for decoding.

![image](https://user-images.githubusercontent.com/44855917/235492143-15c4c687-53b9-42fc-b099-20376f66dd69.png)

output of a successful encoded and compressed data

### B. histo-shift.py
The histo-shift.py file included in this project is responsible for encoding a given binary string .txt file into a cover image. The image can be in any format, but .png is recommended for optimal encoding capacity and desired output.
Once the binary string and cover image are provided, the histo-shift.py program generates an encoded image in .png format. Additionally, it saves the enc_data.pkl file, which is necessary for decoding the given encoded image.
The histo-shift.py file is also capable of decoding a given encoded image, along with the provided enc_data.pkl file. Upon decoding, it returns a .txt file containing the binary encoded text that was retrieved from the image.
Overall, the histo-shift.py file is a key component of this project, responsible for encoding and decoding binary data into and from cover images, using the Histogram Shifting Steganography technique.

histo-shift.py on execution gives us three options:
#### 1. Encoding:
parameters : the text file containig the binary string that needs to be encoded and the cover image.
return : encoded image and enc_fre.pkl file which contains the data necesssary to decode
#### 2. Decoding:
parameters : encoded image and enc_fre.pkl file which contains the data necesssary to decode
return : saves the decoded binary in a .txt file.
#### 3. Capacity:
parameters : Image you wish to use as a cover image in any format
return : encoding capacity of the image in bit.

![image](https://user-images.githubusercontent.com/44855917/235496464-6e4c2349-6311-4206-a360-00f650d7961d.png)

output of a successful encoding of binary text file into a cover image

![image](https://user-images.githubusercontent.com/44855917/235496635-7483c0db-aaed-48a1-8733-5dd93705975d.png)

output of testing capacity of different cover images

### C. main.py
The main.py file included in Analysis folder is used to find and analysis parameter for the encoded image. The main.py takes the origninal and encoded image an a command line argument. It runs three codes 1. pnsr.py, 2. pvd.py and 3.ssid.py which gives Peak Signal to Noise ratio, Mean Square Error and Stuctural Similarity respectively for the given original and encoded image. We can run the 3 tests individually too.

![image](https://user-images.githubusercontent.com/44855917/235498396-9745d866-d1a3-44b0-a1da-ab243c9886c6.png)

output main.py for given original and cover image

## Future Work (ToDo)

* Adding a user interface (UI) to the code to make it more accessible and easier to use.
* Incorporating the Huffman frequency table into the binary encoded data to increase security and make it more difficult to crack.
* Including a snippet in histo-shift.py to retrieve the original image back when the user decodes the hidden binary data from the encoded image.
* Adding an additional layer of image steganography encoding to make the encoded image more robust and difficult to crack. This could involve encoding the original image with another technique and then using histogram shifting on the result.
* Adding more analysis tools to help users better understand and analyze the data and images that they are working with.
