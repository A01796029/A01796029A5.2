from typing import Dict, Any


class Sale:
    """Class to represent a sale from the Sales data"""

    def __init__(self,
                 sale_id: int,
                 sale_date: str,
                 product: str,
                 quantity: int
                 ):
        self.sale_id = sale_id
        self.sale_date = sale_date
        self.product = product
        self.quantity = quantity

    def __repr__(self):
        return f"Sale(id={self.sale_id}, date={self.sale_date}, " \
               f"product={self.product}, qty={self.quantity})"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Sale':
        """Create a Sale instance from a dictionary"""
        return cls(
            sale_id=data['SALE_ID'],
            sale_date=data['SALE_Date'],
            product=data['Product'],
            quantity=data['Quantity']
        )
