from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///books.db')
metadata = MetaData()

books_table = Table('books', metadata, autoload_with=engine)

with engine.connect() as connection:
    result = connection.execute(books_table.select().order_by(books_table.c.title))
    for row in result:
        print(row['title'])
