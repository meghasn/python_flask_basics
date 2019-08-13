from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('helloo.html',mark=score)
if __name__=='__main__':
    app.run(host='localhost',port=5004)
    