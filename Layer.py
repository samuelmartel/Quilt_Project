"""
Author:        Sam Martel - samuelmartel.prof@gmail.com
Description:   Layer class description for 'Quilting Bee' Project
Date Created:  01/07/22
"""

from PIL import ImageDraw, Image
import math

#Class:         Layer
#Description:   Holds information and method for drawing one layer of the image
class Layer:
    
    #Function:      Initialises Layer class
    #Parameters:    colour, size, centers[]
    #Return Val:    N/A    
    def __init__(self, colour, size, centers):
        self.colour = colour
        self.size = math.ceil(size)
        self.centers = centers
        self.corners = self.find_corners()        


    #Function:      Draws a layer
    #Parameters:    Image
    #Return Val:    N/A    
    def draw_layer(self, image):
        for x in range(len(self.centers)):
            self.draw_square(image, self.centers[x])
        return

    #Function:      Finds corners from each center
    #Parameters:    N/A
    #Return Val:    array of all corners
    def find_corners(self):
        output = []
        for i in range(len(self.centers)):
            xy = self.centers[i]
            
            x = xy[0]
            y = xy[1]
            x0 = x + (self.size/2)
            x1 = x - (self.size/2)
            y0 = y + (self.size/2)
            y1 = y - (self.size/2)
            
            temp = [(x0,y0), (x0,y1), (x1, y0), (x1, y1)]

            output = output + temp
        return output

    #Function:      Draws a square
    #Parameters:    image, colour(rgb), center(pixels), side length
    #Return Val:    N/A
    def draw_square(self, image, xy):

        draw = ImageDraw.Draw(image)

        x = xy[0]
        y = xy[1]
        x0 = x + (self.size/2)
        x1 = x - (self.size/2)
        y0 = y + (self.size/2)
        y1 = y - (self.size/2)
        
        co_ordinates = (x0, y0, x1, y1)

        draw.rectangle(co_ordinates, fill=self.colour)

    

    

