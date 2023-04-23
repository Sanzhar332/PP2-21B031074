import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'phone_book',
    port = '5432',
    user = 'postgres',
    password = 'postgres'
)

current = config.cursor()
#a = input('Enter username : ')
b = input('Enter number : ')
#sql = f'select * from phonebook where username = \'{a}\'' 
sql = f'select * from phonebook where number = \'{b}\''
current.execute(sql)

phonebook = current.fetchall()

print(phonebook)

current.close()
config.close()