# Setup a simple flask app. This app will download a colab notebook from google drive and run it.
from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/file/d/<colab_notebook_id>', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
