from typing import Dict, Any


class Product:
    """Class to represent a product from the ProductList"""

    def __init__(self,
                 title: str,
                 type: str,
                 description: str,
                 filename: str,
                 height: int,
                 width: int,
                 price: float,
                 rating: int
                 ):
        self.title = title
        self.type = type
        self.description = description
        self.filename = filename
        self.height = height
        self.width = width
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"Product(title={self.title}," \
               f"type={self.type}, price={self.price})"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Product':
        """Create a Product instance from a dictionary"""
        return cls(
            title=data['title'],
            type=data['type'],
            description=data['description'],
            filename=data['filename'],
            height=data['height'],
            width=data['width'],
            price=data['price'],
            rating=data['rating']
        )
