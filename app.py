from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_wrold():
  return "HELLO CLIENT THIS IS IRM CONSULTING"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug= False)
