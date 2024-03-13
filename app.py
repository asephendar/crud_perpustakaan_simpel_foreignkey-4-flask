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

@app.route('/add', methods=['POST'])
def add_books():
    conn = psycopg2.connect(**params)
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title , author, year, total_pages, category) VALUES (%s, %s, %s, %s, %s)", (
        request.form['title'], 
        request.form['author'], 
        request.form['year'], 
        request.form['total_pages'], 
        request.form['category']))
    
    conn.commit()
    conn.close()
    
    return {'message': 'Data is added successfully'}

@app.route('/update', methods=['PUT'])
def update_books():
    conn = psycopg2.connect(**params)
    
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=%s, author=%s, year=%s, total_pages=%s, category=%s WHERE title=%s", (
        request.form['title'], 
        request.form['author'], 
        request.form['year'], 
        request.form['total_pages'], 
        request.form['category'],
        
        request.form['title']))
    
    conn.commit()
    conn.close()
    
    return {'message': 'Data is updated successfully'}

@app.route('/delete', methods=['DELETE'])
def delete_books():
    conn = psycopg2.connect(**params)
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE title=%s", (request.form['title'],))
    
    conn.commit()
    conn.close()
    
    return {'message': 'Data is deleted successfully'}

if __name__ == '__main__':
    app.run(debug=True)