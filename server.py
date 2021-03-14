from flask import Flask, render_template, redirect, request
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def next(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as databse:
        user_name = data['Name']
        email = data['email']
        content = data['content']
        file = databse.write(f'\n{user_name}// {email}// {content}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as databse2:
        user_name = data['Name']
        email = data['email']
        content = data['content']
        csv_writer = csv.writer(databse2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([user_name, email, content])


@app.route('/submitted', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thank.html')
    else:
        return 'there was a problem'
