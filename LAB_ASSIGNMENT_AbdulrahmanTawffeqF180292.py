# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 21:44:18 2020

@author: Ahmad
"""
import cv2
import numpy as np
from tkinter import *
from tkinter.ttk import *
from PIL import *

window=Tk()

window.title("Image Processing")
icons=PhotoImage(file='C:/Users/Ahmad/Desktop/image.png')
window.iconphoto(False, icons)
lable_for_input=Label(window,text="Image path: ")
lable_for_input.grid(row=0,column=0)

def grayScale():
    newImageList=[]
    pixels=cv2.imread(inputField.get())
    row,col,channel=pixels.shape
    
    for r in range(row):
        for c in range(col):
            for ch in range(channel):
                if pixels[r][c][0]>=100 and pixels[r][c][1]<=80 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=120
                    pixels[r][c][1]=120
                    pixels[r][c][2]=120
                elif pixels[r][c][0]<=80 and pixels[r][c][1]>=100 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=80
                    pixels[r][c][1]=80
                    pixels[r][c][2]=80
                elif pixels[r][c][0]<=80 and pixels[r][c][1]<=80 and pixels[r][c][2]>=100:
                    pixels[r][c][0]=100
                    pixels[r][c][1]=100
                    pixels[r][c][2]=100
                elif pixels[r][c][0]>=100 and pixels[r][c][1]<=80 and pixels[r][c][2]>=100:
                    pixels[r][c][0]=110
                    pixels[r][c][1]=110
                    pixels[r][c][2]=110
                elif pixels[r][c][0]>=100 and pixels[r][c][1]>=100 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=179
                    pixels[r][c][2]=179
                    pixels[r][c][1]=179
                elif pixels[r][c][0]<=80 and pixels[r][c][1]>=100 and pixels[r][c][2]>=100:
                    pixels[r][c][1]=165
                    pixels[r][c][0]=165
                    pixels[r][c][2]=165
                elif pixels[r][c][0]>=220 and pixels[r][c][1]>=220 and pixels[r][c][2]>=220:
                    pixels[r][c][0]=100
                    pixels[r][c][1]=100
                    pixels[r][c][2]=100
                elif pixels[r][c][0]<=20 and pixels[r][c][1]<=20 and pixels[r][c][2]<=20:
                    pixels[r][c][0]=130
                    pixels[r][c][1]=130
                    pixels[r][c][2]=130
                elif pixels[r][c][0]!=pixels[r][c][1]!=pixels[r][c][2]:
                    pixels[r][c][0]=150
                    pixels[r][c][1]=150
                    pixels[r][c][2]=150
                
                newImageList.append(pixels[r][c][ch])
                
    array=np.array(newImageList)
    cv2.imwrite('C:/Users/Ahmad/Desktop/new.png',array.reshape(row,col,channel))
   
    myNew=PhotoImage(file='C:/Users/Ahmad/Desktop/new.png')
    my_canvas=Canvas(window,width=myNew.width(),height=myNew.height())
    my_canvas.grid(row=1,column=1)
    my_canvas.create_image(0,0,anchor=NW, image=myNew).pack

def black():
    newImageList=[]
    pixels=cv2.imread(inputField.get())
    row,col,channel=pixels.shape
    
    for r in range(row):
        for c in range(col):
            for ch in range(channel):
                if pixels[r][c][0]>=100 and pixels[r][c][1]<=80 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=0
                    pixels[r][c][1]=0
                    pixels[r][c][2]=0
                elif pixels[r][c][0]<=80 and pixels[r][c][1]>=100 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=5
                    pixels[r][c][1]=5
                    pixels[r][c][2]=5
                elif pixels[r][c][0]<=80 and pixels[r][c][1]<=80 and pixels[r][c][2]>=100:
                    pixels[r][c][0]=11
                    pixels[r][c][1]=11
                    pixels[r][c][2]=11
                elif pixels[r][c][0]>=100 and pixels[r][c][1]<=80 and pixels[r][c][2]>=100:
                    pixels[r][c][0]=6
                    pixels[r][c][1]=6
                    pixels[r][c][2]=6
                elif pixels[r][c][0]>=100 and pixels[r][c][1]>=100 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=3
                    pixels[r][c][2]=3
                    pixels[r][c][1]=3
                elif pixels[r][c][0]<=80 and pixels[r][c][1]>=100 and pixels[r][c][2]>=100:
                    pixels[r][c][1]=13
                    pixels[r][c][0]=13
                    pixels[r][c][2]=13
                elif pixels[r][c][0]>=170 and pixels[r][c][1]>=170 and pixels[r][c][2]>=170:
                    pixels[r][c][0]=9
                    pixels[r][c][1]=9
                    pixels[r][c][2]=9
                elif pixels[r][c][0]==pixels[r][c][1] and pixels[r][c][1]==pixels[r][c][2] and pixels[r][c][0]>13:
                    pixels[r][c][0]=9
                    pixels[r][c][1]=9
                    pixels[r][c][2]=9
                elif pixels[r][c][0]!=pixels[r][c][1] and pixels[r][c][1]!=pixels[r][c][2]:
                    pixels[r][c][0]=16
                    pixels[r][c][1]=16
                    pixels[r][c][2]=16
    
                
                newImageList.append(pixels[r][c][ch])
                
    array=np.array(newImageList)
    cv2.imwrite('C:/Users/Ahmad/Desktop/new.png',array.reshape(row,col,channel))
   
    myNew=PhotoImage(file='C:/Users/Ahmad/Desktop/new.png')
    my_canvas=Canvas(window,width=myNew.width(),height=myNew.height())
    my_canvas.grid(row=1,column=1)
    my_canvas.create_image(0,0,anchor=NW, image=myNew).pack
    
def white():
    newImageList=[]
    pixels=cv2.imread(inputField.get())
    row,col,channel=pixels.shape
    
    for r in range(row):
        for c in range(col):
            for ch in range(channel):
                if pixels[r][c][0]>=100 and pixels[r][c][1]<=80 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=255
                    pixels[r][c][1]=255
                    pixels[r][c][2]=255
                elif pixels[r][c][0]<=80 and pixels[r][c][1]>=100 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=245
                    pixels[r][c][1]=245
                    pixels[r][c][2]=245
                elif pixels[r][c][0]<=80 and pixels[r][c][1]<=80 and pixels[r][c][2]>=100:
                    pixels[r][c][0]=235
                    pixels[r][c][1]=235
                    pixels[r][c][2]=235
                elif pixels[r][c][0]>=100 and pixels[r][c][1]<=80 and pixels[r][c][2]>=100:
                    pixels[r][c][0]=225
                    pixels[r][c][1]=225
                    pixels[r][c][2]=225
                elif pixels[r][c][0]>=100 and pixels[r][c][1]>=100 and pixels[r][c][2]<=80:
                    pixels[r][c][0]=215
                    pixels[r][c][2]=215
                    pixels[r][c][1]=215
                elif pixels[r][c][0]<=80 and pixels[r][c][1]>=100 and pixels[r][c][2]>=100:
                    pixels[r][c][1]=220
                    pixels[r][c][0]=220
                    pixels[r][c][2]=220
                elif pixels[r][c][0]>=170 and pixels[r][c][1]>=170 and pixels[r][c][2]>=170:
                    pixels[r][c][0]=205
                    pixels[r][c][1]=205
                    pixels[r][c][2]=205
                elif pixels[r][c][0]==pixels[r][c][1] and pixels[r][c][1]==pixels[r][c][2] and pixels[r][c][0]>13:
                    pixels[r][c][0]=200
                    pixels[r][c][1]=200
                    pixels[r][c][2]=200
                elif pixels[r][c][0]!=pixels[r][c][1] and pixels[r][c][1]!=pixels[r][c][2]:
                    pixels[r][c][0]=210
                    pixels[r][c][1]=210
                    pixels[r][c][2]=210
    
                
                newImageList.append(pixels[r][c][ch])
                
    array=np.array(newImageList)
    cv2.imwrite('C:/Users/Ahmad/Desktop/new.png',array.reshape(row,col,channel))
   
    myNew=PhotoImage(file='C:/Users/Ahmad/Desktop/new.png')
    my_canvas=Canvas(window,width=myNew.width(),height=myNew.height())
    my_canvas.grid(row=1,column=1)
    my_canvas.create_image(0,0,anchor=NW, image=myNew).pack
    
def submit():
    my_image=PhotoImage(file=inputField.get())
    my_canvas=Canvas(window,width=my_image.width(),height=my_image.height())
    my_canvas.grid(row=1,column=1)
    my_canvas.create_image(0,0,anchor=NW, image=my_image).pack

inputField=Entry(window,width=30)
inputField.grid(row=0,column=1)
button_submit=Button(window,text="Submit",width=10,command=submit)
button_submit.grid(row=0,column=2)




button_gray=Button(window,text="Gray",width=10,command=grayScale)
button_gray.grid(row=2,column=0)

button_black=Button(window,text="Black",width=10,command=black)
button_black.grid(row=2,column=1)

button_white=Button(window,text="White",width=10,command=white)
button_white.grid(row=2,column=2)



mainloop()