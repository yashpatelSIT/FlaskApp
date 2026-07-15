from flask import Flask

app = Flask(__name__)

print("User Authentication Feature")

@app.route('/')
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)
