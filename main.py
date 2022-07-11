"""
Author:        Sam Martel - samuelmartel.prof@gmail.com
Description:   Main program for the 'Quilting Bee' Prpject
Date Created:  01/07/22
"""

from PIL import Image, ImageDraw
import csv
import math
import Layer
import sys



"""
#Function:      Help message to explain usage of the program
#Parameters:    N/A
#Return Val:    N/A
"""
def help_message():
    print("")
    print("Usage of main function for Quilt_Project:")
    print("Calling the function from the command line (format as below)")
    print("python3 main.py <your_filename.csv> <output.jpg>")
    print("____________________________________________________________________")
    print("Input file must by of type .csv")
    print("Ouput file must be of type .jpg")
    print("____________________________________________________________________")
    print("csv file format:")
    print("Each line must have 4 elements in the following order: Scale, Red, Green, Blue")
    print("You can have as many lines in the csv as you need, however the first line will be discarded and should be used to label columns")    
    print("Each RGB value must be within the range 0-255 to not exceed 8-bits")
    return

"""
!! this function is adapted from python csv library examples !!
#Function:      Open CSV file
#Parameters:    csv file name
#Return Val:    values for scale and colour
"""
def open_csv(file_name):
    output = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                temp = (row[0], row[1], row[2], row[3])
                output.append(temp)
                line_count += 1
    return output

"""
#Function:      Get Scale values from list
#Parameters:    Input list
#Return Val:    values for scale
"""
def get_scale_values(parameters):
    output = []
    for x in range(len(parameters)):
        output.append(float(parameters[x][0]))
    return output

"""
#Function:      Get Colour values from list
#Parameters:    Input list
#Return Val:    values for colour
"""
def get_colour_values(parameters):
    output = []
    for x in range(len(parameters)):
        if(int(parameters[x][1]) < 0 or int(parameters[x][1]) > 255):
            raise ValueError
        
        if(int(parameters[x][2]) < 0 or int(parameters[x][2]) > 255):
            raise ValueError

        if(int(parameters[x][3]) < 0 or int(parameters[x][3]) > 255):
            raise ValueError
        
        output.append((int(parameters[x][1]), int(parameters[x][2]), int(parameters[x][3])))
    return output

"""
#Function:      Convert scale values to pixel values
#Parameters:    Scale Values
#Return Val:    initial pixel number
"""
def scale_image(values, unit_value):
    scale_factor = 10
    unit_value = int(unit_value/scale_factor)
    unit_scales = values * unit_value
    scale_sum = sum(unit_scales)
    total_image_size = math.ceil(scale_factor * scale_sum)
    return int(total_image_size)

"""
#Function:      Build image
#Parameters:    input file name, output file name
#Return Val:    N/A
"""
def construct_image(input, output):
    seed_values = open_csv(input)
    scale_values = get_scale_values(seed_values)
    colour_values = get_colour_values(seed_values)
    """    if colour_values == -1:
        return -1"""
    square_size = 1000
    image_size = scale_image(scale_values, square_size)
    
    image = Image.new("RGB", (image_size, image_size), "white")    

    layers = []
    for x in range(len(scale_values)):
        if x == 0:
            layers.append(Layer.Layer(colour_values[x], scale_values[x]*square_size, [(int(image_size/2),int(image_size/2))]))
        else:    
            layers.append(Layer.Layer(colour_values[x], scale_values[x]*square_size, layers[x-1].corners))

    for i in layers:
        i.draw_layer(image)

    image.save(output)

"""
#Function:      Main function
#Parameters:    Terminal inputs
#Return Val:    N/A
"""
def main():
    args = sys.argv[1:]
    try:
        if(len(args) != 2):
            raise TypeError
        if(args[0] == "-h" or args[0] == "--h" or args[0] == "-help" or args[0] == "--help"):
            help_message()
            return
        if "." not in args[0] or "." not in args[1]:
            raise TypeError
        if args[0].split(".")[1] != "csv":
            raise TypeError
        if args[1].split(".")[1] != "jpg":
            raise TypeError

        input = args[0]
        output = args[1]
        if construct_image(input, output) == -1:
            raise ValueError

    except ValueError:
        print("Colour Value Error: Colour values outside of 8-bits allowed")
        help_message()
        return

    except TypeError:
        print("Arguement Error: Incorrect arguements given")
        help_message()
        return






if __name__ == "__main__":
    main()
