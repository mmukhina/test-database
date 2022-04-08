import psycopg2
from flask import Flask, url_for, request, render_template


DATABASE_URL = os.environ['DATABASE_URL']
con = psycopg2.connect(DATABASE_URL)
cur = con.cursor()

query = f"""SELECT * FROM users """

con.close()

app = Flask(__name__)

@app.route('/')
def main():
    return query

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
