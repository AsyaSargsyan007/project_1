from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html",)

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        file_context = request.form.get('file_context')
        file_date = request.form.get('file_date')
        fw = open(file_name, 'w')
        fw.write(file_context)
        fw.write(file_date)
        fw.close()

        return render_template('create.html')
    return redirect ('/')
