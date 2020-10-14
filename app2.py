from flask import Flask, render_template, redirect, request
from predict import predict_new 

# Create an instance of Flask
app = Flask(__name__)

new_image = 'images/ship.jpeg'

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route("/predict", methods=["GET", "POST"])
def home():
      if request.method == "POST":
          #call predict function to label new image
          label = predict_new(new_image)
          return render_template('index.html', message = label)

if __name__ == "__main__":
    app.run()