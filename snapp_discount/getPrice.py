# from snapp_discount.main import get_foods
import os

try: 
    from snapp_discount.main import get_foods
except:
    from main import get_foods

import json


class get_price():
    def __init__(self,res_name,res_link=None,city='اصفهان') -> None:
        self.city = city
        self.res_name = res_name
        self.res_link = res_link





    def get_name_price(self):
        try:
            self.get_foods = get_foods()

            self.get_foods.open_snap_food(self.res_link)
            self.get_foods.close_set_city()
            foods = self.get_foods.get_name_price(self.res_name)

            # foods = {'pizza_sara': {'False': 'False', 'هپی برگر': '۱۳۲,۰۰۰ تومان'}}


            self.get_foods.json_obj.write_restaurant_prices(self.city,self.res_name,foods)

            return True
    
        except:
            return False
    
    def ret_price(self):

        path = os.path.join('snapp_discount/cache/cities/{}/{}.json'.format(self.city,self.res_name))

        with open(path, 'r') as f:
            data = json.load(f)

        return data



if __name__=='__main__':

    import json

    with open('snapp_discount/cache/links/esfahan_links.json', 'r') as f:
        data = json.load(f)


    name = 'pizza_sara'

    link = data[name]


    gp = get_price(res_link=link,res_name=name)

    print(gp.ret_price())

    # gp.get_name_price()
