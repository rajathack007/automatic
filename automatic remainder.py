from tkinter import *
import pywhatkit
from datetime import datetime

import tkinter.font as font
root = Tk()
root.geometry("1900x1200")
root.title('Automatic Remainder')
root['bg']='red'
frame = Frame(root)
frame['bg']='#F6F6F8'
frame.pack(expand=True,fill=BOTH)
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
dt = datetime.now()
print('Datetime is:', dt)
day= dt.strftime('%A')

myFont = font.Font(size=15,weight='bold') 
label2 = Label( frame, text = "Welcome",bg="Red",height=2,width=112,fg="white")
label2['font'] = myFont
label2.place(x=100,y=20)
def sendMon():  
    print("Today day is: ",day)
    
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',23,00)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',23,1)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',23,2)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,29)
def sendTue():  
    print("Today day is: ",day)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,26)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,27)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,28)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,29)
def sendWed():  
    print("Today day is: ",day)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,26)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,27)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,28)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,29)
def sendThu():  
    print("Today day is: ",day)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,26)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,27)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,28)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,29)
def sendFri():  
    print("Today day is: ",day)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,26)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,27)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,28)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,29)
def sendSat():  
    print("Today day is: ",day)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,26)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,27)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,28)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,29)
def sendSun():  
    print("Today day is: ",day)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,26)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,27)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,28)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,29)
def sendEmail():  
    print("Today day is: ",day)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,26)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,27)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of EOP https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,28)
    pywhatkit.sendwhatmsg('+918607821560','kindly fill the feedback form of FSD https://docs.google.com/spreadsheets/d/1c0sQEBkWzOzx1EcNCaPNt92UlFSaNM4gSeAXyVW8L9Q/edit#gid=0',17,29)



mondaybutton = Button(frame, text = 'Monday Remainder', fg ='white',bg='blue',command=sendMon,activebackground='#00ff00')

mondaybutton['font'] = myFont
mondaybutton.grid(row=2, column=0, pady=120,padx=100)
tuesdaybutton = Button(frame, text = 'Tuesday Remainder', fg='white',bg='blue',font='bold',command=sendTue,activebackground='#00ff00')
tuesdaybutton['font'] = myFont
tuesdaybutton.grid(row=2, column=1, padx=100)
wednesdaybutton = Button(frame, text = 'Wednesday Remainder', fg='white',bg='blue',font='bold',command=sendWed,activebackground='#00ff00')
wednesdaybutton['font'] = myFont
wednesdaybutton.grid(row=2, column=2, padx=100)
thursdaybutton = Button(frame, text = 'Thursday Remainder', fg='white',bg='blue',font='bold',command=sendThu,activebackground='#00ff00')
thursdaybutton['font'] = myFont
thursdaybutton.grid(row=2, column=3, padx=100)
fridaybutton = Button(frame, text = 'Friday Remainder', fg='white',bg='blue',font='bold',command=sendFri,activebackground='#00ff00')
fridaybutton['font'] = myFont
fridaybutton.grid(row=3, column=0, pady=30,padx=100)
saturdaybutton = Button(frame, text = 'Saturday Remainder', fg='white',bg='blue',font='bold',command=sendSat,activebackground='#00ff00')
saturdaybutton['font'] = myFont
saturdaybutton.grid(row=3, column=1, pady=30,padx=100)
sundaybutton = Button(frame, text = 'Sunday Remainder', fg='white',bg='blue',font='bold',command=sendSun,activebackground='#00ff00')
sundaybutton['font'] = myFont
sundaybutton.grid(row=3, column=2, pady=30,padx=100)
emailbutton = Button(frame, text = 'Email Remainder', fg='white',bg='blue',font='bold',command=sendEmail,activebackground='#00ff00')
emailbutton['font'] = myFont
emailbutton.grid(row=3, column=3, pady=30,padx=100)

closebutton = Button(frame, text = 'Close', fg='white',bg='Red',font='bold',command=root.destroy,activebackground='#00ff00')
closebutton['font'] = myFont
closebutton.place(x=910, y=500)

root.mainloop()
