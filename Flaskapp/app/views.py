from flask import render_template, jsonify, json, url_for
from app import aws_controller

from app import app

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/vocabulary',)
def vocabulary():
    return render_template("vocabulary.html")

@app.route('/comming_soon')
def comming_soon():
    return render_template("comming_soon.html")

@app.route('/get-items',methods=['POST', 'GET'])
def get_items():
    return jsonify(aws_controller.get_items())
