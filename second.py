# import module
import mysql.connector

# function to cinvert data
def convert_data(data, file_name):
	# Convert binary format to images
	# or files data(with given file_name)
	with open(file_name, 'wb') as file:
		file.write(data)


for i in range(10):
    try:
        # establish connection
        connection = mysql.connector.connect(host='localhost',
                                            database='example',
                                            user='root',
                                            password='')
        cursor = connection.cursor()
        # getting data by id value
        query = """ SELECT * from imgs where id = %s"""

        id = 1
        cursor.execute(query, (i,))
        records = cursor.fetchall()
        for row in records:
            image = row[1]
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
