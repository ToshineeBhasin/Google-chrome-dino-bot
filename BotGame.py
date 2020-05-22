from PIL import ImageGrab, ImageOps
import pyautogui
from time import sleep
from numpy import *

class Cordinates():
    replayBtn = (1150,400)
    dinasaur = (910,560)  #  x=1230 and y= 560 when dino was down so 560-410=150
    #580=x coordinates to check for tree (dino should jump when obstacle appears)
    #y coordinates = 710 it is for the lowest obstacle
    
    
def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    #pyautogui.keyDown('down')
     
restartGame()

def pressSpace():
    #pyautogui.keyUp('down')
  pyautogui.press('space') 
    #     pyautogui.keyDown('down')
    
'''
restartGame()
sleep(1) 
pressSpac e()

'''
def imageGrab():
    box=(558,305,696,328)   #box is the area where any obstacle is detected
    image= ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    '''    
    analysing images to  grayscale is much more efficient than in color so we 
    convert the grabbed image to grayscale
    '''    
    a=array(grayImage.getcolors())
    #now we print out the grayedscaled sum of all the colour values of each of pixel in the box
    print(a.sum())
    return a.sum()

  
def main():
    restartGame()
    while True:
        if(imageGrab()!=3421):
            pressSpace()
            sleep(0.1)
        
main()

    
    
        
    
    

