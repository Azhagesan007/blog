from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    post = Post()
    data = post.data
    return render_template("index.html", blogs=data)

@app.route("/blog/<int:no>")
def read_blog(no):
    post = Post()
    data = post.data[no-1]
    return render_template("post.html", blogs=data)

if __name__ == "__main__":
    app.run(debug=True)
