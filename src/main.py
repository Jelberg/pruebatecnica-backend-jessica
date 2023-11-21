
from flask import Flask, request, make_response, render_template, jsonify
from dotenv import load_dotenv

from postgres.Postgres import Postgres
from blueprint_task import task_routes_blueprint

load_dotenv("../.env")
app =  Flask(__name__)
app.register_blueprint(task_routes_blueprint, url_prefix="/task")

