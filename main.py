from flask import Flask, render_template, request

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return "Hello! welcome to mi casa!"

@app.route("/<username>")
def potato(username):
  return f"Hello {username} how are you doing"

@app.route("/html")
def html():
  # html template load
  return render_template("flasktest.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  return render_template("report.html", word=word)


app.run(host="0.0.0.0")