from typing import Optional

from models.customer_details import Customer
from fastapi import APIRouter

router = APIRouter()

@router.get("/customer")
def get_customer_details(name:Optional[str],phone_number:Optional[int]=None):
    pass