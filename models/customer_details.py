from pydantic import BaseModel
from typing import Optional, Any


class Customer(BaseModel):
    """A model to get the customer details"""

    name: Optional[str]=None
    phone_number: Optional[int]=None
    no_of_times_visited: Optional[int]=1
    no_of_discount_availed: Optional[int]=1
