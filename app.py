from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from sqlalchemy.orm import query
import sqlite3
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/touch/OneDrive/Documents/UMBC stuff/Spring24/CompEngineering/Hw2/users.db'

db = SQLAlchemy(app)





def fetch_data_from_database():
    conn = sqlite3.connect('users.db') 
    c = conn.cursor()
    c.execute("SELECT name, id, points FROM users")  
    data = c.fetchall()
    conn.close()
    return data


def get_all_data_Two():
    conn = sqlite3.connect('users.db')  
    c = conn.cursor()
    c.execute("SELECT name, id, points FROM users")
    data = c.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
   data = fetch_data_from_database()
   return render_template('home.html', data=data)
  




@app.route('/create', methods=['GET', 'POST'])  
def create_user():
    
    data = fetch_data_from_database()
    return render_template('create.html', data=data)

@app.route('/submit_user', methods=['POST'])
def submit_user():
    name = request.form['name']
    id = request.form['id']
    points = request.form['points']
    
    
    conn = sqlite3.connect('users.db')  
    c = conn.cursor()
    c.execute("INSERT INTO users (name, id, points) VALUES (?, ?, ?)", (name, id, points))
    conn.commit()
    conn.close()
    
    return redirect('/')



@app.route('/search', methods=['GET', 'POST'])   
def search():
    data = fetch_data_from_database()
    return render_template('search.html', data=data)

@app.route('/search_user', methods=['GET', 'POST'])  
def search_user():
    id = int(request.form['id'])
    data = get_all_data_Two()
    #print("All data:", data)
    
    #print("looping now:")
    filtered_data = []
    for row in data:
        if row[1] == id:
            filtered_data.append(row)


    print("Filtered data:", filtered_data)  



    return render_template('search_results.html', data=filtered_data, id=id, searchType=1)

@app.route('/delete', methods=['GET', 'POST'])  
def delete():
    
   data = fetch_data_from_database()
   return render_template('delete.html', data=data)

@app.route('/delete_user', methods=['GET', 'POST'])  
def delete_user():
    id = int(request.form['id'])
    data = get_all_data_Two()
    #print("All data:", data)
    
    #print("looping now:")
    filtered_data = []
    for row in data:
        if row[1] == id:
            filtered_data.append(row)

    conn = sqlite3.connect('users.db') 
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()  



    return redirect('/')

@app.route('/update', methods=['GET', 'POST'])  
def update():
    
    data = fetch_data_from_database()
    return render_template('update.html', data=data)

@app.route('/search_user_update', methods=['POST'])
def search_user_update():
    id = int(request.form['id'])
    data = get_all_data_Two()
    #print("All data:", data)
    
    #print("looping now:")
    filtered_data = []
    for row in data:
        if row[1] == id:
            filtered_data.append(row)


    print("Filtered data:", filtered_data)  



    return render_template('search_update_results.html', data=filtered_data, id=id, searchType=1)


@app.route('/submit_user_update', methods=['POST'])
def submit_user_update():
    name = request.form['name']
    id = request.form['id']
    points = request.form['points']
    
    
    conn = sqlite3.connect('users.db') 
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (id,)) #delete the old record
    c.execute("INSERT INTO users (name, id, points) VALUES (?, ?, ?)", (name, id, points))
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)  #running debug mode for localhosting