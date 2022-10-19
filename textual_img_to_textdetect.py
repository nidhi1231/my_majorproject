import cv2
from pytesseract import pytesseract
from pytesseract import Output
import PIL.Image
from PIL import Image
from googletrans import Translator
import pyttsx3
from playsound import playsound
import os
from gtts import gTTS
from tkinter import *
import tkinter as tk
from tkinter import font


pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def show_image():
    img = cv2.imread("images/krishna.jpg")# add image
    cv2.imshow("original image",img)
    cv2.waitKey(0)

def convert():
    # to give path tesseract
    #pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # read image
    img = cv2.imread("images/krishna.jpg")# add image
    '''
    height,width,c = img.shape
    words_in_image = pytesseract.image_to_string(img)# using string diplay console
    print(words_in_image)

    # return each character detect and thier boundaries
    letter_boxes = pytesseract.image_to_boxes(img) #using letter boxes
    print(letter_boxes)

    for box in letter_boxes.splitlines():
        box = box.split()
        x,y,w,h = int(box[1]),int(box[2]),int(box[3]),int(box[4])
    #    create rectangular bounding box  over each character
        cv2.rectangle(img,(x,height-y),(w,height-h),(0,0,255),3)
    #     label in each character in image
        cv2.putText(img,box[0],(x,height-h+32),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        '''
    # raw information of detected text
    img_data = pytesseract.image_to_data(img, output_type=Output.DICT)
    # print(img_data)
    for i, word in enumerate(img_data['text']):  # using dictionary
        if word != "":
            x, y, w, h = img_data['left'][i], img_data['top'][i], img_data['width'][i], img_data['height'][i]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, word, (x, y - 16), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
            # print(i)
    # text = pytesseract.image_to_string(PIL.Image.open(img))
    # print(text)
    # f = open("abc.txt", "w")
    # f.write(text)
    # text = pytesseract.image_to_string(img)
    # # text add in .txt file
    # f = open('abc.txt', mode='w')
    # f.write(text)
    # print("Given image of text is:", text)
    cv2.imshow("Output image",img)
    cv2.waitKey(0)
def img_text():
    img = PIL.Image.open('images/krishna.jpg') # add image
    img = img.convert('L')
    img.save('image.jpg')
    # path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(PIL.Image.open('image.jpg'))
    print(text)
    f = open("abc.txt", "w")
    f.write(text)
img_text()
def speech():
    f = open("abc.txt", "r")
    tts = f.read()
    tt = gTTS(tts, lang='en')
    tt.save("good.mp3")
    os.system(" good.mp3")


# create GUI
root = tk.Tk()
root.geometry("500x650+500+50")
root.configure(bg="white")
pic1 = PhotoImage(file="photo (2).png")
pic2 = PhotoImage(file="photo (3).png")
pic3 = PhotoImage(file="microphone.png")
my_font = font.Font(family="Arial",size=12,weight="bold",slant="italic")
mfont= ('Times',12,'italic')
lbl = Label(root,text = " Textual Image To Speech convertor",fg="Blue",bg="white"
            ,font=my_font,pady=10)
lbl.pack(side=TOP)
# label1 =Label(root,text=" Display Image",pady =10,bg="white",font=("Arial",10),style="italic")
label1 = Label(root,text="Display Real Image",width =15,font=mfont,fg="black",bg="white")
label1.pack()
# label1.pack(side=LEFT)
# lbl2 =Label(root)
# lbl2.pack()

# show_imgbtn = Button(root,text=" Display original image ",bg="blue",fg="white",command=show_image)
# uploadbtn.pack(side=LEFT,padx=15)
show_imgbtn = Button(root,image=pic1,command=show_image)
show_imgbtn.pack()
label2 = Label(root,text="Display Output Image",width =15,font=mfont,fg="black",bg="white")
label2.pack()
changebtn = Button(root,image=pic2,fg="white",command=convert)
# uploadbtn.pack(side=LEFT,padx=15)
changebtn.pack()
label3 = Label(root,text="Audio file",pady =10,width =15,font=mfont,fg="black",bg="white")
label3.pack()
playbtn = Button(root,image=pic3,fg="white",command=speech)
# playbtn.pack(side=LEFT,padx=15)
playbtn.pack()
label4 = Label(root,text="Exit app",pady =10,width =15,font=mfont,fg="black",bg="white")
label4.pack()
exitbtn =Button(root,text="Exit",bg="blue",fg="white",font="Arial 10 bold",borderwidth=20,command=lambda :exit())
# exitbtn.pack(side=LEFT,padx=15)
exitbtn.pack()
root.mainloop()