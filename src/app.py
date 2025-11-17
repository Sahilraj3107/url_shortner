import random, string
from flask import Flask, render_template, request, redirect as flask_redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('url_shortner.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS url_mapping (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE,
            url TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        
        if url:
            # Clean and validate URL
            url = url.strip()
            
            # Ensure URL has protocol
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            short_code = generate_short_code()
            save_url_mapping(short_code, url)
            
            short_url = f'http://127.0.0.1:5000/{short_code}'
            output = f'Original URL: {url} <br>Short URL: <a href="/{short_code}" target="_blank">{short_url}</a>'
            return render_template('home.html', output=output)
    
    return render_template('home.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = sqlite3.connect('url_shortner.db')
    cursor = conn.cursor()
    cursor.execute('SELECT url FROM url_mapping WHERE short_code = ?', (short_code,))
    result = cursor.fetchone()
    conn.close()

    if result:
        url = result[0]
        print(f"Redirecting to: {url}")  
        
        # Ensure URL has protocol
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        return flask_redirect(url)
    else:
        return 'URL not found', 404

def generate_short_code():  # Removed url parameter since you don't use it
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def save_url_mapping(short_code, url):
    conn = sqlite3.connect('url_shortner.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO url_mapping (short_code, url) VALUES(?, ?)', 
                   (short_code, url))
    conn.commit()
    conn.close()
    print(f"Saved: {short_code} -> {url}")  # Debug line


if __name__ == '__main__':
    init_db()
    app.run(debug=True) 