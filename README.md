# Quilt_Project

Author: Sam Martel
Email: samuelmartel.prof@gmail.com 
project: Quilt Assesment

Language: Python 3.7 or above
Required Packages: pillow, csv, math, sys
Installing missing packages: pip3 install <package>

Usage: python3 main.py <input>.csv <output>.jpg



Description of Approach:
Divide desired image into layers where each layer can only have one colour and is made up of squares located at the corners of the previous layer. Each layer is a defined as a class so that the values are contained within itself. When all layers are set the image can be constructed from the bottom up.

The edge of the outmost square needs to be the edge of the image therefore the image must scale to fit these in without any white space around the edge.

Used csv to as it is easy it is an easy format to use and interperet the inputs as it is generally immune from the line ending problems when switching between linux and windows. Output is limited to jpeg as that is the default file type of the pillow library. Other formats are available. Other formats weren't neccesary as jpeg is widely used and easily opened on Windows, Mac and Linux.



Flow Description:
1. Take inputs from the commandline arguements
2. Check that the arguements are valid to use
3. Parse the arguements into the contruct_image function
4. Extract scale and colour values from the input csv file
5. Check the colour values are valid (0 <= x <= 255)
6. Parse the scale values to the scale image function to ensure that the outmost square is on the edge of the image
7. Create a blank white image with size dictated by the scaling function
8. Create layers using the scale and colour values and put into a list
9. Iterate through list of layers and draw in order
10. Save image to output file