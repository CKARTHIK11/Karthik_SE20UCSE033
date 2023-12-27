from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="Users",
            passwd="Hike1234@",
            database="karthik"
        )
        #replace host user passwd and database 
        return connection
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

@app.route('/question', methods=['GET'])
def get_question():
    connection = create_connection()
    if connection is None:
        return jsonify(error="Database connection failed"), 500

    cursor = connection.cursor()
    cursor.execute("SELECT id, question FROM questions ORDER BY RAND() LIMIT 1")
    question = cursor.fetchone()
    connection.close()

    if question:
        return jsonify(id=question[0], question=question[1])
    else:
        return jsonify(error="No questions found"), 404

if __name__ == '__main__':
    app.run(debug=True)
