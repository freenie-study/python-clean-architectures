from datetime import datetime
import random


class Event:
    def __init__(self, name: str, start_date: str, expirarion_date: str) -> None:
        self._name = name
        self._start_date = start_date
        self._expirarion_date = expirarion_date 
        self._created_at = datetime.now()


    @property
    def name(self) -> str:
        return self._name


    @name.setter
    def name(self, new_name: str) -> str:
        self._name = new_name


    @property
    def created_at(self) -> str:
        return self._created_at.strftime('%Y-%m-%d')


    @created_at.setter
    def created_at(self, new_date: str) -> str:
        self._created_at = new_date


    @property
    def start_date(self) -> str:
        return self._start_date


    @start_date.setter
    def start_date(self, new_start_date: str) -> str:
        self._start_date = new_start_date


    @property
    def expiration_date(self) -> str:
        return self._expirarion_date


    @expiration_date.setter
    def expiration_date(self, new_expiration_date: str) -> str:
        self._expiration_date = new_expiration_date


class Coupon:
    all_coupons_code_list = []
    
    def __init__(self, event: object, name: str) -> None:
        self._event = event
        self._name = name
        self._created_at = datetime.now()
        self._code = self.generate_code()


    @classmethod
    def create_coupons(cls, n: int, event: object, coupon_name: str) -> list:
        coupon_info_list = []
        while len(coupon_info_list) != n:
            coupon = cls(event, coupon_name)

            if coupon.code not in cls.all_coupons_code_list:
                cls.all_coupons_code_list.append(coupon.code)
                coupon_info_list.append([
                    f'이벤트 이름: {coupon.event.name}', 
                    f'쿠폰이름: {coupon.name}', 
                    f'쿠폰 유효 기간: {coupon.event.start_date} ~ {coupon.event.expiration_date}', 
                    f'코드번호: {coupon.code}'
                    ])      
            
        return coupon_info_list


    @property
    def code(self) -> str:
        return self._code


    @code.setter
    def code(self, new_coupon_code: str) -> str:
        self._code = new_coupon_code
    

    @property
    def name(self) -> str:
        return self._name


    @name.setter
    def name(self, new_name: str) -> str:
        self._name = new_name


    @property
    def event(self) -> object:
        return self._event


    @staticmethod
    def generate_code():
        return str(random.randrange(1000, 9999))+'-'+str(random.randrange(1000, 9999))+'-'+ str(random.randrange(1000, 9999))
    

if __name__ == '__main__':
    summer_event = Event('summser evnet', '2022-08-03', '2022-09-02')

    coupon1 = Coupon(summer_event, '1만원 쿠폰')
    coupons1 = coupon1.create_coupons(5, summer_event, coupon1.name)
    print(f'summer event, 1만원 쿠폰: {coupons1}', end='\n\n')

    coupon2 = Coupon(summer_event, '3만원 쿠폰')
    coupons2 = coupon2.create_coupons(3, summer_event, coupon2.name)
    print(f'summer event, 3만원 쿠폰: {coupons2}', end='\n\n')

    coupon3 = Coupon(summer_event, '5만원 쿠폰')
    coupons3 = coupon2.create_coupons(1, summer_event, coupon3.name)
    print(f'summer event, 5만원 쿠폰: {coupons3}')