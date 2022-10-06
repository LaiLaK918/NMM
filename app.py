from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('success.html')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return render_template('success.html', name='document')
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
