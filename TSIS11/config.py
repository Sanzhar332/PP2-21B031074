import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'phonebook2',
    port = '5432',
    user = 'sanzhar',
    password = '1234'
)

cursor = conn.cursor()