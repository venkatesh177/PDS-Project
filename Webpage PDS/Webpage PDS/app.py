from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def skills_tilte():
   return render_template("index.html")

@app.route('/clustering')
def clustering():
   return render_template("clustering.html")

@app.route('/skills-group')
def skills_group():
   return render_template("skills_group.html")

@app.route('/word-cloud')
def word_cloud():
   return render_template("word_cloud.html")

@app.route('/skills-frequency')
def skills_frequency():
   return render_template("skills_frequency.html")

if __name__ == '__main__':
   app.run(debug=True)