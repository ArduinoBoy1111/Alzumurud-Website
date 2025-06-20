from flask import Flask, Blueprint, render_template, url_for
from data_manager import items, filter_items

views = Blueprint("views", __name__)

filtered_items = filter_items(items)


@views.route("/")
def home():
    return render_template("index.html", filtered_items=filtered_items)
