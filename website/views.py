from flask import Flask, Blueprint, render_template, url_for
from .data_manager import items, filter_items

views = Blueprint("views", __name__)

new_items = filter_items(items, new=True)
onsale_items = filter_items(items, onsale=True)


@views.route("/")
def home():
    return render_template("index.html", new_items=new_items, onsale_items=onsale_items)


@views.route("/products")
def products():
    return render_template("products.html")
