from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "<h1 style='text-align:center;margin-top:100px'>Hello Ayoya 👋</h1>"

