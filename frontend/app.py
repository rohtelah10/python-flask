from flask import Flask, render_template, request, redirect, url_for  
import requests
BACKEND_URL = 'http://127.0.0.1:8000'

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    
    response = requests.post(BACKEND_URL + '/submit', data=form_data)
    
    print("response", response)
    
    if response.status_code == 200:
        return redirect(url_for('success')) 
    
    
    
    return "Data submitted successfully from frontend"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)