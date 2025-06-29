from flask import Flask, Blueprint, render_template, request
from .data_manager import items, filter_items, ascending_list, descending_list

views = Blueprint("views", __name__)

new_items = filter_items(items, new=True)
onsale_items = filter_items(items, onsale=True)


@views.route("/")
def home():
    return render_template("index.html", new_items=new_items, onsale_items=onsale_items)


@views.route("/products", methods=["GET"])
def products():
    name = request.args.get("name").lower().replace(" ", "")
    type = request.args.get("type")
    dimensions = request.args.get("dimensions")
    origin = request.args.get("origin")
    color = request.args.get("color")

    if request.args.get("onsale"):
        onsale = True
    else:
        onsale = "any"

    if request.args.get("price") == "none":
        items_to_filter = items
    elif request.args.get("price") == "asc":
        items_to_filter = ascending_list
    elif request.args.get("price") == "desc":
        items_to_filter = descending_list
    else:
        items_to_filter = items

    if type != None:
        filtered_items = filter_items(
            items_to_filter, type, color, dimensions, origin, "any", onsale, name
        )
    else:
        filtered_items = items_to_filter

    count = len(filtered_items)

    return render_template(
        "products.html",
        filtered_items=filtered_items,
        count=count,
        name=name,
        type=type,
        dimensions=dimensions,
        origin=origin,
        color=color,
        onsale=onsale,
        price=request.args.get("price"),
    )
