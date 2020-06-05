from flask import Flask, render_template

app = Flask(__name__)
friends = ['abhishek', 'yadav', 'jatin', 'katyal']
num = 15


@app.route('/')
def hello():
	return render_template("index.html", my_friends = friends, number = num)

if (__name__=="__main__"):
	app.run(debug=True)
