import csv
import mysql.connector

# Replace with your database credentials
db_config = {
    'host': 'localhost',
    'user': 'etd_user',
    'password': 'etd_user',
    'database': 'db_etd'
}

# Replace with the path to your CSV file
csv_file = 'etd.csv'

# Connect to the MySQL database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Open and read the CSV file
with open(csv_file, 'r', encoding='iso-8859-1') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        title = row['title']
        creator = row['creator']
        description = row['description']
        publisher = row['publisher']

        # Insert data into the MySQL table
        insert_query = "INSERT INTO etd_metadata (title, creator, description, publisher) VALUES (%s, %s, %s, %s)"
        values = (title, creator, description, publisher)
        cursor.execute(insert_query, values)
        connection.commit()

# Close the database connection
cursor.close()
connection.close()
