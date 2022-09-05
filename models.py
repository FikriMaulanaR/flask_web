import psycopg2
import psycopg2.extras
from flask import session

DB_HOST = "localhost"
DB_NAME = "dbsorong"
DB_USER = "postgres"
DB_PASS = "rahasia"
DB_PORT = 6543

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def index_posts():
    s = "SELECT * FROM tbl_post a, tbl_category b WHERE a.post_category=b.category_id AND a.post_category=1;"
    cur.execute(s)
    index_posts = cur.fetchall()
    return index_posts