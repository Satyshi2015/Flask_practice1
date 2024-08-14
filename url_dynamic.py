from flask import Flask, redirect,url_for,render_template,request

''' 
{%...%} condition,loop, statements
{{ }} expressions to print output
{#...#}this is for comments
'''

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    if score>=50:
        res="pass"
    else:
        res="fail"
    exp={'score':score,'res':res}
    return render_template('result.html',result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has fail the test with " + str(score) + " marks"

@app.route('/result/<int:marks>')
def result(marks):
    if marks<50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result,score=marks))


##result checker html page with submit button
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+math+c+data_science)/4
    return redirect(url_for('success',score=total_score))


if __name__=='__main__':
    app.run()