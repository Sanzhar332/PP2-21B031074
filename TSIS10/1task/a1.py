import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'phone_book',
    port = '5432',
    user = 'postgres',
    password = 'postgres'
)

current = config.cursor()

postgres_insert_query = ''' insert into phonebook (username, number) values (%s,%s) '''
a = input('enter your name: ')
b = input('enter your number: ')
current.execute(postgres_insert_query, (a,b))
config.commit()

current.close()
config.close()