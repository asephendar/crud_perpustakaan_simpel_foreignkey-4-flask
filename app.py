from flask import Flask, request
import psycopg2

app = Flask(__name__)

params = {
    "dbname": "task_library",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}

@app.route('/', methods=['GET'])
def view_books():
    conn = psycopg2.connect(**params)
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books ORDER BY year DESC")
    data = cursor.fetchall()
    
    conn.close()
    
    json_data = []

    for el in data:
        json_data.append({
            'title': el[0],
            'author': el[1],
            'year': el[2],
            'total_pages': el[3],
            'category': el[4]
        })
    
    return {'data': json_data}

if __name__ == '__main__':
    app.run(debug=True)