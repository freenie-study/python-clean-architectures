from datetime import datetime, date
import random
from pydantic import BaseModel, Field
from typing import Annotated


class BasicModel(BaseModel):
    created_date: date = datetime.now().date()


class Event(BasicModel):
    id: int = 0
    name: str
    start_date: date
    end_date: date
    
    
class Coupon(BasicModel):
    id: int = 0
    event: Event
    name: str
    codes: list


class CouponGenerator:
    all_coupons_code_list: list[str] = []

    @staticmethod
    def generate_code() -> str:
        return str(random.randrange(1000, 9999))+'-'+str(random.randrange(1000, 9999))+'-'+ str(random.randrange(1000, 9999))

    @classmethod
    def generate_coupons_code(cls, n: int) -> list[str]:
        while len(cls.all_coupons_code_list) <= n:
            coupon_code = cls.generate_code()
            if coupon_code not in cls.all_coupons_code_list:
                cls.all_coupons_code_list.append(coupon_code)
        
        return cls.all_coupons_code_list



def create_coupons(n: int, event: Event) -> Coupon:
    coupons_code_list = CouponGenerator.generate_coupons_code(n)
    return Coupon(event=event, name='test_coupon', codes=coupons_code_list)


    
event = Event(name='test_event', start_date='2022-11-01', end_date='2022-11-30')
coupons = create_coupons(5, event)
print(coupons)