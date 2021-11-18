import csv
import pymysql
import json
from datetime import date, datetime
import pymysql.cursors
from app import db


def insertsql_from_json():
    conn = pymysql.connect( 
            user = 'root',
            passwd = '1234',
            host = 'localhost',
            port = 3307,
            db = 'libs',
            charset = 'utf8mb4'
    ) 
    curs = conn.cursor()
    with open('app/static/test1.json', encoding='utf-8') as json_file: 
        json_data = json.load(json_file)

        for row in json_data:
            #published_at = datetime.strptime(
            #                row['publication_date'], '%Y-%m-%d').date()
            image_path = f"static/img/{row['id']}"
            try:
                open(f'./app/{image_path}.png')
                image_path += '.png'
            except:
                image_path += '.jpg'

            # id=int(row['id'])
            # book_name=row['book_name']
            # publisher=row['publisher']
            # author=row['author']
            # publication_date=published_at
            # pages=int(row['pages'])
            # isbn=row['isbn']
            # description=row['description']
            # link=row['link']
            # image=image_path
            # stock=1
            # rating=0

            sql = "INSERT INTO books(id, book_name, publisher, author, publication_date, pages, isbn, description, link, image, stock, rating ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
                row['id'], 
                row['book_name'], 
                row['publisher'],
                row['author'], 
                row['publication_date'], 
                int(row['pages']),
                row['isbn'], 
                row['description'], 
                row['link'],
                image_path,
                1,
                0,
            )

            curs.execute(sql, val) 
            conn.commit()


insertsql_from_json()