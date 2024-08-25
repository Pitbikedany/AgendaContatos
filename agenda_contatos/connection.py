import mysql.connector

mydatabase = mysql.connector.connect(host="localhost", user="root", password="", database="agenda_contatos")

myqueries = mydatabase.cursor()