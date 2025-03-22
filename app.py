from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
app = Flask(__name__, static_folder="static")
app = Flask(__name__)

@app.route("/")
def home():
    username = os.getenv("App_username", "Guest")  # Default to "Guest" if not found
    return render_template("index.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)