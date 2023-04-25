from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home')
def homePage():
    return render_template('homepage.html', title='Matrix')

