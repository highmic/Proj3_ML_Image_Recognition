from flask import Flask, render_template, redirect, request
from predict import predict_new

# Create an instance of Flask
app = Flask(__name__)

filepath = "images/Dog.jpeg"

print("---------------> FLASK < --------------")
@app.route("/", methods=["GET", "POST"])
def home():
        labels = predict_new(filepath)
        label = labels[0]
        return render_template('index.html', message = label)
if __name__ == "__main__":
    app.run(debug=True)

