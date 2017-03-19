#from flash import render_template
from flask import Flask, render_template
#from flask import Flask
import string
import random,datetime

app = Flask(__name__)
#print (Flask.__doc__)
#
@app.route("/")
@app.route('/index')
def index():
    char_set = string.ascii_uppercase + string.digits
    str = ''.join(random.sample(char_set*6, 6))    
    user = {'nickname':str}
    now = datetime.datetime.now()
    t = {'value':now}
    print ("------",user,"----------")
    return render_template('index.html',title='Home', user=user,time=t)


if __name__ == "__main__":
#    app.run()
#     app.run(host='0.0.0.0',port=5000,debug=True)
     app.run(host='10.75.53.249', port= 5000, debug = True)

