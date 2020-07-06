from flask import Flask

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "Hello! welcome to mi casa!"

@app.route("/contact")
def potato():
  return "Contact me!"  

app.run(host="0.0.0.0")