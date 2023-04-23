import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'phone_book',
    port = '5432',
    user = 'postgres',
    password = 'postgres'
)

current = config.cursor()
current.execute(
    '''
    create table phonebook(
        username varchar(20),
        number varchar(12)
    );
    '''
)
config.commit()

current.close()
config.close()