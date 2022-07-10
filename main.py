"""
Author:        Sam Martel - samuelmartel.prof@gmail.com
Description:   Main program for the 'Quilting Bee' Prpject
Date Created:  01/07/22
"""

from PIL import Image, ImageDraw
import csv
import math
import Layer

#Function:      
#Parameters:    
#Return Val: 


"""
!!this function is taken from examples on the internet!!
#Function:      Round up   
#Parameters:    number, decimals    
#Return Val:    rounded number
"""
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

"""
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
        temp = (int(parameters[x][1]), int(parameters[x][2]), int(parameters[x][3]))
        output.append(temp)
    return output

"""
#Function:      Convert scale values to pixel values
#Parameters:    Scale Values
#Return Val:    initial pixel number
"""
def scale_image(values):
    unit_value = 100
    scale_factor = 10
    unit_scales = values * unit_value
    scale_sum = sum(unit_scales)
    total_image_size = round_up(scale_factor * scale_sum)
    return int(total_image_size)

### !!!Not a good scaling method!!! ###


def main():

    seed_values = open_csv("Input.csv")
    scale_values = get_scale_values(seed_values)
    #print(scale_values)
    colour_values = get_colour_values(seed_values)
    #print(colour_values)
    image_size = 5000   
#    image_size = scale_image(scale_values)
    square_scale = int(image_size/2)
    print(image_size, square_scale)
    image = Image.new("RGB", (image_size, image_size), "white")    

    layers = []
    for x in range(len(scale_values)):
        if x == 0:
            layers.append(Layer.Layer(colour_values[x], scale_values[x]*square_scale, [(square_scale,square_scale)]))
        else:    
            temp = layers[x-1]
            layers.append(Layer.Layer(colour_values[x], scale_values[x]*square_scale, temp.corners))

    for i in layers:
        i.draw_layer(image)

    image.save("Testing.jpg")



if __name__ == "__main__":
    main()



# Need Better naming  convensions
# Need better function descriptions
# Should make functions more specialized and not round with in build functions of Python 