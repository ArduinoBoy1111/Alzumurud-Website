class item:
    def __init__(
        self,
        name: str,
        item_type: str,
        color: str,
        dimensions: str,
        origin: str,
        image: str,
        new: bool = False,
        onsale: bool = False,
        price: int = 0,
    ):
        self.name = name
        self.item_type = item_type
        self.color = color
        self.dimensions = dimensions
        self.origin = origin
        self.image = image
        self.new = new
        self.onsale = onsale
        self.price = price

    def __str__(self):
        return (
            f"Item(name={self.name}, type={self.item_type}, color={self.color}, "
            f"dimensions={self.dimensions}, origin={self.origin}, image={self.image}, "
            f"new={self.new}, onsale={self.onsale}, price={self.price})"
        )


items = [
    item(
        "سيراميك مصقول",
        "بورسلين",
        "بيج",
        "120*60",
        "مصري",
        r"static\items_imgs\photo_1_2025-06-20_15-37-19.jpg",
        new=False,
        onsale=False,
        price=12500,
    ),
    item(
        "جرانيت كلاسيكي",
        "جرانيت",
        "كريمي",
        "120*60",
        "برازيلي",
        r"static\items_imgs\photo_2_2025-06-20_15-37-19.jpg",
        new=False,
        onsale=True,
        price=12800,
    ),
    item(
        "بلاط عتيق",
        "بورسلين",
        "أبيض",
        "120*60",
        "إيطالي",
        r"static\items_imgs\photo_3_2025-06-20_15-37-19.jpg",
        new=False,
        onsale=False,
        price=12200,
    ),
    item(
        "سيراميك لامع",
        "سيراميك",
        "رمادي",
        "120*60",
        "إيراني",
        r"static\items_imgs\photo_4_2025-06-20_15-37-19.jpg",
        new=False,
        onsale=True,
        price=12750,
    ),
    item(
        "رخام طبيعي",
        "رخام",
        "بني",
        "60*60",
        "أردني",
        r"static\items_imgs\s-l1200.jpg",
        new=False,
        onsale=True,
        price=13000,
    ),
    item(
        "رخام طبيعي",
        "رخام",
        "بني",
        "60*60",
        "أردني",
        r"static\items_imgs\s-l1200.jpg",
        new=False,
        onsale=True,
        price=13000,
    ),
    item(
        "رخام طبيعي",
        "رخام",
        "بني",
        "120*60",
        "أردني",
        r"static\items_imgs\photo_5_2025-06-20_15-37-19.jpg",
        new=False,
        onsale=True,
        price=13000,
    ),
]

for i in range(113):
    items.append(
        item(
            (
                "رخام طبيعي"
                if i % 5 == 0
                else (
                    "سيراميك لامع"
                    if i % 5 == 1
                    else (
                        "بلاط عتيق"
                        if i % 5 == 2
                        else "جرانيت كلاسيكي" if i % 5 == 3 else "سيراميك مصقول"
                    )
                )
            ),
            (
                "رخام"
                if i % 4 == 0
                else "سيراميك" if i % 4 == 1 else "بورسلين" if i % 4 == 2 else "جرانيت"
            ),
            "رمادي" if i % 3 == 0 else "أبيض" if i % 3 == 1 else "بيج",
            "120*60" if i % 2 == 0 else "60*60",
            (
                "أردني"
                if i % 6 == 0
                else (
                    "إيراني"
                    if i % 6 == 1
                    else (
                        "إيطالي"
                        if i % 6 == 2
                        else (
                            "مصري"
                            if i % 6 == 3
                            else "برازيلي" if i % 6 == 4 else "أردني"
                        )
                    )
                )
            ),
            r"static\items_imgs\test.jpg",
            new=bool((i + 1) % 37 == 0),
            onsale=((i + 1) % 37 == 0),
            price=12000 + (i % 10) * 100,
        )
    )


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
