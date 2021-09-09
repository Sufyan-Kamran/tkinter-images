# import module
import mysql.connector
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk,ImageFile
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

root = Tk()
ImageFile.LOAD_TRUNCATED_IMAGES = True

image1 = Image.open("img1.png")
basewidth = 300
wpercent = (basewidth / float(image1.size[0]))
hsize = int((float(image1.size[1]) * float(wpercent)))
image1 = image1.resize((basewidth, hsize), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
i1 = tk.Label(image=test, width=150,height=150)
i1.place(x=10,y=50)


image2 = Image.open("img2.png")
basewidth = 300
wpercent = (basewidth / float(image2.size[0]))
hsizes = int((float(image2.size[1]) * float(wpercent)))
image2 = image2.resize((basewidth, hsizes), Image.ANTIALIAS)
tests = ImageTk.PhotoImage(image2)
i2 = tk.Label(image=tests, width=150,height=150)
i2.place(x=150,y=50)


image3 = Image.open("img3.png")
basewidth = 300
wpercent = (basewidth / float(image3.size[0]))
hsize3 = int((float(image3.size[1]) * float(wpercent)))
image3 = image3.resize((basewidth, hsize3), Image.ANTIALIAS)
test3 = ImageTk.PhotoImage(image3)
i2 = tk.Label(image=test3, width=150,height=150)
i2.place(x=10,y=200)


image4 = Image.open("img4.png")
basewidth = 300
wpercent = (basewidth / float(image4.size[0]))
hsize4 = int((float(image4.size[1]) * float(wpercent)))
image4 = image4.resize((basewidth, hsize4), Image.ANTIALIAS)
test4 = ImageTk.PhotoImage(image4)
i2 = tk.Label(image=test4, width=150,height=150)
i2.place(x=200,y=200)


image5 = Image.open("img5.png")
basewidth = 300
wpercent = (basewidth / float(image5.size[0]))
hsize5 = int((float(image5.size[1]) * float(wpercent)))
image5 = image5.resize((basewidth, hsize5), Image.ANTIALIAS)
tests = ImageTk.PhotoImage(image5)
i2 = tk.Label(image=tests, width=150,height=150)
i2.place(x=150,y=50)


image6 = Image.open("img6.png")
basewidth = 300
wpercent = (basewidth / float(image6.size[0]))
hsizes = int((float(image6.size[1]) * float(wpercent)))
image6 = image6.resize((basewidth, hsizes), Image.ANTIALIAS)
tests = ImageTk.PhotoImage(image6)
i2 = tk.Label(image=tests, width=150,height=150)
i2.place(x=150,y=50)


image7 = Image.open("img7.png")
basewidth = 300
wpercent = (basewidth / float(image7.size[0]))
hsizes = int((float(image7.size[1]) * float(wpercent)))
image7 = image7.resize((basewidth, hsizes), Image.ANTIALIAS)
tests = ImageTk.PhotoImage(image7)
i2 = tk.Label(image=tests, width=150,height=150)
i2.place(x=150,y=50)


image8 = Image.open("img8.png")
basewidth = 300
wpercent = (basewidth / float(image8.size[0]))
hsizes = int((float(image8.size[1]) * float(wpercent)))
image8 = image8.resize((basewidth, hsizes), Image.ANTIALIAS)
tests = ImageTk.PhotoImage(image8)
i2 = tk.Label(image=tests, width=150,height=150)
i2.place(x=150,y=50)


root.mainloop()