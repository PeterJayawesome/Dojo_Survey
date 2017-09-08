from flask import Flask,render_template,request,redirect,flash,session
app = Flask(__name__)
app.secret_key="djosurvey"
@app.route('/')
def survey():
	return render_template('survey.html')

@app.route('/result',methods=['POST'])
def result():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	if len(name)<1:
		flash("Name could not be empty!")
	elif len(comment)<1:
		flash("Comment could not be empty!")
	elif len(comment)>120:
		flash("Comment could not be longer than 120 characters!")
	else:
		return render_template('result.html',name = name,location = location, language = language, comment = comment)
	return redirect('/')

app.run(debug=True)	