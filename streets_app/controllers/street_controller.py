from flask import Blueprint, jsonify, request, render_template, redirect, url_for, abort, current_app
from main import db
from models.streets import Street
from schemas.street_schema import single_street_schema, multi_street_schema

streets = Blueprint('streets', __name__)

@streets.route('/')
def index():
    data = {
        "page_title": "Street Index",
        "streets": multi_street_schema.dump(Street.query.all()) 
    }
    print(data)
    return render_template("index.html", page_data=data)
