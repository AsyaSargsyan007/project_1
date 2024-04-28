from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        file_context = request.form.get('file_context')
        file_date = request.form.get('file_date')
        fw = open(f'./files/{file_name}', 'w')
        fw.write(file_context)
        fw.write(file_date)
        fw.close()

        return render_template('create.html')
    return redirect ('/')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    files_paths = os.listdir('./files')
    return render_template('news.html', list_files = files_paths)

@app.route('/statement', methods=['GET','POST'])
def statement():
    if request.method == 'POST':
        your_name = request.form.get('your_name')
        your_number = request.form.get('your_number')
        your_mail = request.form.get('your_mail')
        fw = open(your_name, 'w')
        fw.write(your_number)
        fw.write(your_mail)
        fw.close()

        return render_template('statement.html')
    
@app.route('/file/<name>')
def file_fn(name):
    path = f'./files/{name}'
    file_context = open(path, 'r').read()
    file_date = open(path, 'r').read()
    return render_template('file.html', file_name=path, file_context=file_context, file_date=file_date)