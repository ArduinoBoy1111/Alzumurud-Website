class item:
    def __init__(
        self,
        name: str,
        item_type: str,
        color: str,
        dimensions: str,
        origin: str,
        image: str,
        new: bool,
        onsale: bool,
    ):
        self.name = name
        self.item_type = item_type
        self.color = color
        self.dimensions = dimensions
        self.origin = origin
        self.image = image
        self.new = new
        self.onsale = onsale

    def __str__(self):
        return f"Item(name={self.name}, type={self.item_type}, color={self.color}, dimensions={self.dimensions}, origin={self.origin}, image={self.image}), new={self.new}, onsale={self.onsale})"


items = [
    item(
        "polished ceramic",
        "porcelin",
        "beige",
        "120*60",
        "egyptian",
        "static\items_imgs\photo_1_2025-06-20_15-37-19.jpg",
    ),
    item(
        "granite classic",
        "granite",
        "cream",
        "120*60",
        "brazilian",
        "static\items_imgs\photo_2_2025-06-20_15-37-19.jpg",
    ),
    item(
        "vintage tile",
        "porcelin",
        "white",
        "120*60",
        "italian",
        "static\items_imgs\photo_3_2025-06-20_15-37-19.jpg",
    ),
    item(
        "glossy ceramic",
        "ceramic",
        "grey",
        "120*60",
        "iranian",
        "static\items_imgs\photo_4_2025-06-20_15-37-19.jpg",
    ),
    item(
        "natural marble",
        "marble",
        "brown",
        "120*60",
        "jordanian",
        "static\items_imgs\photo_5_2025-06-20_15-37-19.jpg",
    ),
]


def filter_items(
    items: list,
    item_type: str = "any",
    color: str = "any",
    dimensions: str = "any",
    origin: str = "any",
    new: str = "any",
    onsale: str = "any",
):
    filtered = []

    for item in items:
        if (
            (item_type == "any" or item.item_type == item_type)
            and (color == "any" or item.color == color)
            and (dimensions == "any" or item.dimensions == dimensions)
            and (origin == "any" or item.origin == origin)
            and (new == "any" or item.new == new)
            and (onsale == "any" or item.onsale == onsale)
        ):
            filtered.append(item)

    return filtered
