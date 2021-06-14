from os import write
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

image_path='pan3.jpeg'
reader= easyocr.Reader(['en'],gpu=True)
result=reader.readtext(image_path)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread(image_path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,2)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+y,y+h),(255,0,0),2)
f=open("output.txt","w")


if faces==():
    print("not a valid document")
    f.write("not a valid document")
else:
    
    flag=0
    if(len(result))>55 or (len(result))<10:
        print("not identifiable")
        f.write("not identifiable")
    else:
        for i in range(len(result)):
            s=result[i]
            for j in range(len(s)):
                if (s[j]=="DRIVING" and result[i+1][j]=="LICENCE") or (s[j]=="Driving" and result[i+1][j]=="Licence"):
                    print("driving licence")
                    text_var1="The given document is a driving license"
                    f.write(text_var1)
                    flag=1
                    for i in result:
                        for j in range(len(i)):
                            if i[j]=="Name":
                                d=result.index(i)
                                print("Name : "+result[d+1][1])
                                f.write("\nName : "+result[d+1][1])
                                top_left=result[d+1][0][0]
                                bottom_right=result[d+1][0][2]
                                img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
                            
                            elif i[j]=="SIWID of":
                                d=result.index(i)
                                print("Guardian name : "+result[d+1][1])  
                                f.write("\nGuardian name : "+result[d+1][1])  
                                top_left=result[d+1][0][0]
                                bottom_right=result[d+1][0][2]
                                img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
                elif s[j]=="INCOME TAX DEPARTMENT": 
                    print("PAN CARD")
                    text_var2="The given document is a PAN CARD"
                    f.write(text_var2)
                    flag=1
                    for i in result:
                        for j in range(len(i)):
                            if i[j]=="GOVT. OF INDIA":
                                d=result.index(i)
                                print("Name : "+result[d+1][1])
                                f.write("\nName : "+result[d+1][1])
                                top_left=result[d+1][0][0]
                                bottom_right=result[d+1][0][2]
                                img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
                            elif i[j]=="Permanent Account Number" :
                                d=result.index(i)
                                print("PAN Number : "+result[d+1][1])
                                f.write("\nPAN Number : "+result[d+1][1])
                                top_left=result[d+1][0][0]
                                bottom_right=result[d+1][0][2]
                                img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
                            
                elif s[j]=="REPUBLIC":
                    print(" THE GIVEN DOCUMENT IS A PASSPORT")
                    text_var3="The given document is a passport"
                    f.write(text_var3)
                    flag=1
                    for i in result:
                        for j in range(len(i)):
                            if i[j]=="Given Name(s)":
                                d=result.index(i)
                                print("Name : "+result[d+1][1])
                                f.write("\nName : "+result[d+1][1])
                                top_left=result[d+1][0][0]
                                bottom_right=result[d+1][0][2]
                                img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
                            elif i[j]=="M" or i[j]=="F"or i[j]=="T":
                                d=result.index(i)
                                print("DATE OF BIRTH : "+result[d+1][1]) 
                                f.write("\nDATE OF BIRTH : "+result[d+1][1]) 
                                top_left=result[d+1][0][0]
                                bottom_right=result[d+1][0][2]
                                img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
        if flag==0:
            print("NOT A VALID DOCUMENT. PLEASE TRY UPLOADING A CLEARER IMAGE")  
            f.write("NOT A VALID DOCUMENT. PLEASE TRY UPLOADING A CLEARER IMAGE") 
        elif flag==1:
            plt.imshow(img)
            plt.show()