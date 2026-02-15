from flask import Flask
app = Flask(name)

@app.get("/")
def home():
    return "Hello ِAyoya"

