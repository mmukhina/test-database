import psycopg2
from flask import Flask


#DATABASE_URL = os.environ['DATABASE_URL']
#con = psycopg2.connect(DATABASE_URL)
#cur = con.cursor()

#query = f"""SELECT name FROM users """

#con.close()

app = Flask(__name__)

@app.route('/')
def main():
    return "query[0]"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
