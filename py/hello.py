from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print ("Time is")
    return "Hello World!"

if __name__ == "__main__":
#    app.run()
#     app.run(host='0.0.0.0',port=5000,debug=True)
     app.run(host='10.75.53.249', port= 5000, debug = True)

