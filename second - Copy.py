# import module
import mysql.connector
import mysql
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk,ImageFile
root = Tk()

root.geometry("1400x800+0+0")
#root.config(bg="")


  
# Show image using label
ImageFile.LOAD_TRUNCATED_IMAGES = True

# function to cinvert data
def convert_data(data, file_name):
	# Convert binary format to images
	# or files data(with given file_name)
	with open(file_name, 'wb') as file:
		file.write(data)
def iss():
    i=1
    for i in range(10):
        try:
            # establish connection
            connection = mysql.connector.connect(host='localhost',
                                                database='example',
                                                user='root',
                                                password='')
            cursor = connection.cursor()
            # getting data by id value
            query = """ SELECT * from products where Pid = %s"""

            id = 1
            cursor.execute(query, (i,))
            records = cursor.fetchall()
            for row in records:
                image = row[6]
                # Pass path with filename where we want to save our file
                convert_data(image, f"img{i}.png")
            print("Successfully Retrieved Values from database")

        except mysql.connector.Error as error:
            print(format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        
iss()


image1 = Image.open("img1.png")
basewidth = 200
wpercent = (basewidth / float(image1.size[0]))
hsize = int((float(image1.size[1]) * float(wpercent)))
image1 = image1.resize((basewidth, hsize), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
i1 = tk.Label(image=test, width=200,height=200,bg="white")
i1.place(x=10,y=50)


image2 = Image.open("img5.png")
basewidth = 200
wpercent2 = (basewidth / float(image2.size[0]))
hsize2 = int((float(image2.size[1]) * float(wpercent2)))
image2 = image2.resize((basewidth, hsize2), Image.ANTIALIAS)
test2 = ImageTk.PhotoImage(image2)
i2 = tk.Label(image=test2, width=200,height=200,bg="white")
i2.place(x= 420,y=50)


image3 = Image.open("img2.png")
basewidth = 200
wpercent3 = (basewidth / float(image3.size[0]))
hsize3 = int((float(image3.size[1]) * float(wpercent3)))
image3 = image3.resize((basewidth, hsize3), Image.ANTIALIAS)
test3 = ImageTk.PhotoImage(image3)
i2 = tk.Label(image=test3, width=200,height=200,bg="white")
i2.place(x=10,y=250)


image4 = Image.open("img6.png")
basewidth = 200
wpercent4 = (basewidth / float(image4.size[0]))
hsize4 = int((float(image4.size[1]) * float(wpercent4)))
image4 = image4.resize((basewidth, hsize4), Image.ANTIALIAS)
test4 = ImageTk.PhotoImage(image4)
i2 = tk.Label(image=test4,width=200,height=200,bg="white")
i2.place(x= 420,y=250)


image5 = Image.open("img2.png")
basewidth = 100
wpercent5 = (basewidth / float(image5.size[0]))
hsize5 = int((float(image5.size[1]) * float(wpercent5)))
image5 = image5.resize((basewidth, hsize5), Image.ANTIALIAS)
test5 = ImageTk.PhotoImage(image5)
i2 = tk.Label(image=test5, width=200,height=200,bg="white")
i2.place(x=10,y=450)


image6 = Image.open("img6.png")
basewidth = 200
wpercent6 = (basewidth / float(image6.size[0]))
hsize6 = int((float(image6.size[1]) * float(wpercent6)))
image6 = image6.resize((basewidth, hsize6), Image.ANTIALIAS)
test6 = ImageTk.PhotoImage(image6)
i2 = tk.Label(image=test6, width=200,height=200,bg="white")
i2.place(x= 420,y=450)


image7 = Image.open("img5.png")
basewidth = 200
wpercent7 = (basewidth / float(image7.size[0]))
hsize7 = int((float(image7.size[1]) * float(wpercent7)))
image7 = image7.resize((basewidth, hsize7), Image.ANTIALIAS)
test7 = ImageTk.PhotoImage(image7)
i2 = tk.Label(image=test7, width=200,height=200,bg="white")
i2.place(x=10,y=650)


image8 = Image.open("img8.png")
basewidth = 200
wpercent8 = (basewidth / float(image8.size[0]))
hsize8 = int((float(image8.size[1]) * float(wpercent8)))
image8 = image8.resize((basewidth, hsize8), Image.ANTIALIAS)
test8 = ImageTk.PhotoImage(image8)
i2 = tk.Label(image=test8, width=200,height=200,bg="white")
i2.place(x= 420,y=650)


pn1 = Label(root, text="")
pn1.place(x= 220,y=50)
pr1 = Label(root, text="")
pr1.place(x= 220,y=70)
ct1= Label(root, text="")
ct1.place(x= 220,y=90)
pn2 = Label(root, text="")
pn2.place(x= 220,y=250)
pr2 = Label(root, text="")
pr2.place(x= 220,y=270)
ct2= Label(root, text="")
ct2.place(x= 220,y=290)
pn3 = Label(root, text="")
pn3.place(x= 220,y=450)
pr3 = Label(root, text="")
pr3.place(x= 220,y=470)
ct3= Label(root, text="")
ct3.place(x= 220,y=490)
pn4 = Label(root, text="")
pn4.place(x= 220,y=650)
pr4 = Label(root, text="")
pr4.place(x= 220,y=670)
ct4= Label(root, text="")
ct4.place(x= 220,y=690)
pn5 = Label(root, text="")
pn5.place(x= 670,y=50)
pr5 = Label(root, text="")
pr5.place(x= 670,y=70)
ct5= Label(root, text="")
ct5.place(x= 670,y=90)
pn6 = Label(root, text="")
pn6.place(x= 670,y=250)
pr6 = Label(root, text="")
pr6.place(x= 670,y=270)
ct6= Label(root, text="")
ct6.place(x= 670,y=290)
pn7 = Label(root, text="")
pn7.place(x= 670,y=450)
pr7 = Label(root, text="")
pr7.place(x= 670,y=470)
ct7= Label(root, text="")
ct7.place(x= 670,y=490)
pn8 = Label(root, text="")
pn8.place(x= 670,y=650)
pr8 = Label(root, text="")
pr8.place(x= 670,y=670)
ct8= Label(root, text="")
ct8.place(x= 670,y=690)






                
connection = mysql.connector.connect(host='localhost',
                                            database='example',
                                            user='root',
                                            password='')
cursor = connection.cursor()
iss = 6
query = """ SELECT * from products """
cursor.execute(query)
records = cursor.fetchall()
i= 8
Pname = [] 
Price=[]
Category =[]
for rec in records:
    Pname.append(rec[1])
    Price.append(rec[2])
    Category.append(rec[3])
    
    i = i+1
         
pn1['text']=f"Name : {Pname[0]}"
pr1['text']=f"Price  : {Price[0]}"
ct1['text']=f"Category  : {Category[0]}"
pn2['text']=f"Name : {Pname[1]}"
pr2['text']=f"Price  : {Price[1]}"
ct2['text']=f"Category  : {Category[1]}"
pn3['text']=f"Name : {Pname[2]}"
pr3['text']=f"Price  : {Price[2]}"
ct3['text']=f"Category  : {Category[2]}"
pn4['text']=f"Name : {Pname[3]}"
pr4['text']=f"Price  : {Price[3]}"
ct4['text']=f"Category  : {Category[3]}"
pn5['text']=f"Name : {Pname[4]}"
pr5['text']=f"Price  : {Price[4]}"
ct5['text']=f"Category  : {Category[4]}"
pn6['text']=f"Name : {Pname[5]}"
pr6['text']=f"Price  : {Price[5]}"
ct6['text']=f"Category  : {Category[5]}"
pn7['text']=f"Name : {Pname[6]}"
pr7['text']=f"Price  : {Price[6]}"
ct7['text']=f"Category  : {Category[6]}"
pn8['text']=f"Name : {Pname[7]}"
pr8['text']=f"Price  : {Price[7]}"
ct8['text']=f"Category  : {Category[7]}"
root.mainloop()