from django.db import models

# Create your models here.

class ViewProductItem:
    def __init__(self, image_name, description, quantity, sizes=None, colours=None):
        self.image_name = image_name
        self.description = description
        self.quantity = range(quantity + 1)
        self.sizes = sizes
        self.colours = colours

productDB = [
        {"image_name": "hat.jpg",
         "description": "One-size summer hat",
         "quantity": 4,
         "sizes": ["oneSize"],
         "colours":["Black", "White"]},
        {"image_name": "jeans.jpg",
         "description": "Skinny-fit denim jeans",
         "quantity": 4,
         "sizes": ["6","8","10","12","14","16"],
         "colours":["Black", "Blue"]},
        {"image_name": "tshirt.jpg",
         "description": "Casual Basic Tee",
         "quantity": 4,
         "sizes": ["6","8","10","12","14","16"],
         "colours":["Black", "White", "Pink"]}
    ]

def retrieveProducts():
    product_items = []
    for db_item in productDB:
        product_items.append(ViewProductItem(db_item["image_name"], db_item["description"], db_item["quantity"], db_item["sizes"], db_item["colours"]))
    return product_items





