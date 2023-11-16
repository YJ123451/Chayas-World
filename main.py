from flask import Flask, render_template, request
import hashlib

from werkzeug.utils import redirect

app = Flask(__name__, template_folder='template', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/queues')
def queue():
    return render_template('queues.html')

@app.route('/arrays')
def array():
    return render_template('arrays.html')

@app.route('/trees')
def trees():
    return render_template('trees.html')

@app.route('/bfs')
def BFS():
    return render_template('bfs.html')

@app.route('/hashing', methods=['GET', 'POST'])
def hashing():
    hashed_data = None

    if request.method == 'POST':
        input_data = request.form['input_data']
        hasher = hashlib.sha256()
        hasher.update(input_data.encode('utf-8'))
        hashed_data = hasher.hexdigest()

    return render_template('hashing.html', hashed_data=hashed_data)

@app.route('/easter_egg')
def easter_egg():
    return redirect("https://youtu.be/dQw4w9WgXcQ?si=OsPRAho8d8KCgvjJ")
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
