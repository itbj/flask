from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    user = {'nickname':'Michael'}
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''

if __name__ == "__main__":
#    app.run()
#     app.run(host='0.0.0.0',port=5000,debug=True)
     app.run(host='10.75.53.249', port= 5000, debug = True)

