from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name2']
    email = request.form['email2']
    return render_template('result.html', name1=name, email1=email)

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)                                  # app.run(debug=True,port=8080)