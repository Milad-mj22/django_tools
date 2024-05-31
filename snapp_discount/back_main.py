
# web import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#------------------------------------------------------------------

import time
import os
import json

CACHE_PATH = 'cache/'


class web_driver():
    def __init__(self,timeout=10) -> None:
        self.timeout = timeout
        self.create_driver()
        

    def create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome('./chromedriver',options=options)
     

    def wait(self,auto=True,time=0):
        if auto:
            self.driver.implicitly_wait(self.timeout)
        else:
            self.driver.implicitly_wait(time)   

    def open_site(self,url):
        self.driver.get(url)

    def find_element(self,element,by=By.XPATH,get_text=False,click=False,manual_timeout='False',print_error = True):
        ret = {'val':False,'text':False,'click_status':False}
        if manual_timeout =='False':
            self.wait()
        else:
            self.wait(auto=False,time=int(manual_timeout))
        try:
            val = self.driver.find_element(by=by,value=element)
            ret.update({'val':val})
            if get_text:
                text = val.text
                ret.update({'text':text})
            if click:
                click_status = val.click()
                ret.update({'click_status':click_status})
        except:
            if print_error:
                print('Error in find element')
            
        return ret
    

    def sendkeys(self,element,value,by=By.XPATH):
        self.wait()
        self.driver.find_element(by=by,value=element).send_keys(value)
        

    def scrool(self,repeat=5):
        for iter in range(int(repeat)):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.2)


class get_foods():
    def __init__(self) -> None:
        self.web = web_driver()
        self.json_obj = json_cache()

        self.foods={}
        self.res_names  = []
        self.city = False
        


    def open_snap_food(self,url ='https://snappfood.ir/'):
        self.web.open_site(url)
    def set_city_page(self,city = 'اصفهان'):
        
        self.web.find_element(element='/html/body/div[1]/div/div/main/div[1]/div[3]/nav/a[1]/div',click=True)   # click restaurant
        self.web.find_element(element='/html/body/div[2]/div/div/section/div/section/form/div[1]',click=True)   # click cities
        time.sleep(0.1)
        self.web.sendkeys(element='/html/body/div[2]/div[2]/div/section/div/div/input',value=city)             # select city
        time.sleep(0.1)
        self.web.find_element(element='/html/body/div[2]/div[2]/div/section/section/div',click=True)            # set city
        time.sleep(1)
        self.web.find_element(element='/html/body/div[2]/div/div/form/div/button',click=True)                   # confirm city
        print('a')
        self.city = city
        # /html/body/div[2]/div/div/form/div/button


    def set_city(self,city = 'اصفهان',set_page=False):
        self.city=city
        if set_page:
            self.set_city_page(city=city)




    def set_area_page(self,area):


        self.web.find_element(element='/html/body/div[1]/div/div[1]/header/div/div[1]/div',click=True)   # click areas
        time.sleep(0.1)

        self.web.find_element(element='/html/body/div[2]/div/div/section/div/section/form/div[2]/div',click=True)   # click area text field
        time.sleep(0.1)


        self.web.sendkeys(element='/html/body/div[2]/div/div/section/div/section/form/div[2]/div/input',value=area)             # select city
        time.sleep(0.1)

        self.web.sendkeys(element='/html/body/div[2]/div/div/section/div/section/form/div[2]/div/input',value=Keys.ENTER)       # confirm restaurant
        time.sleep(0.1)

    def set_area(self,area='خاقانی',set_page = True):
    

        self.area=area
        if set_page:
            self.set_area_page(area=area)



    def search_restaurant(self,name):
        
        self.web.find_element(element='/html/body/div[1]/div/div[1]/header/div/div[2]/p',click=True)       # select restaurant
        time.sleep(0.5)
        self.web.find_element(element='/html/body/div[2]/div/div/div/div[1]/svg',click=True)       # select restaurant
        
        self.web.sendkeys(element='/html/body/div[2]/div/div/div/div[1]/input',value='')             # input empty
        self.web.sendkeys(element='/html/body/div[2]/div/div/div/div[1]/input',value=name)             # input restaurant
        time.sleep(0.5)
        self.web.sendkeys(element='/html/body/div[2]/div/div/div/div[1]/input',value=Keys.ENTER)       # confirm restaurant
        time.sleep(0.5)
        self.web.find_element(element='/html/body/div[1]/div/main/section/div/div[1]',click=True)       # select restaurant

        
    def get_name_price(self,restaurant_name=str):
        section =1
        res_name={}
        
        time.sleep(2)
        while True:
            for i in range(1,15):
                # try:/html/body/div[1]/div/main/div/section/section/section[4]/div/div[1]/section/div[1]/div[1]/h2
                # /html/body/div[1]/div/main/div/section/section/section[3]/div/div[2]/section/div[1]/div[1]/h2
                # /html/body/div[1]/div/main/div/section/section/section[1]/div/div[1]/section/div[1]/div[1]/h2
                # try:
                food = self.web.find_element('/html/body/div[1]/div/main/div/section/section/section[{}]/div/div[{}]/section/div[1]/div[1]/h2'.format(str(section),str(i)),get_text=True,manual_timeout=0,print_error=False)                         # get name of food   
                # res_name.update({'name':str(food)})
                p=self.web.find_element('/html/body/div[1]/div/main/div/section/section/section[{}]/div/div[{}]/section/div[2]/footer/div/div[1]/div/div'.format(str(section),str(i)),get_text=True,manual_timeout=0,print_error=False)              # get price of food               
                res_name.update({str(food['text']):str(p['text'])})
                # except:
                #     pass
            section+=1
            if section>10:
                break

        self.foods.update({str(restaurant_name):res_name})
        print(self.foods)

    def get_all_restaurants_name_city(self,cache=False):
        if not cache:
            none=0
            self.web.scrool(repeat=50)
            self.res_names=[]
            for iter in range(1,200):
                name = self.web.find_element('/html/body/div[1]/div/main/div[2]/div/div[1]/div[{}]/a/div/div[2]/div/h2'.format(iter),get_text=True,manual_timeout=0,print_error=False)
                if name['text'] not in self.res_names:
                    self.res_names.append(name['text'])
                print(name['text'])
                if not name['text'] and iter>100:
                    none+=1
                    if none>7:
                        break
                else:
                    none=0    
            self.json_obj.write_city_restaurants(city_name=self.city,value = self.res_names)

        else:
            self.res_names = self.json_obj.ret_city_cache(city_name=self.city)

            




    def search_in_res_names(self):
        for res in self.res_names:
            self.search_restaurant(name= res)
            time.sleep(0.5)
            self.get_name_price(restaurant_name= res)



class json_cache():

    def read_json(self,file_path):
        file = open(file_path)
        data = json.load(file)
        try:
            file.close()
        except:
            print('cant close file')
            pass
        return data

    def write_json(self,file_name,dict):

        # Serializing json
        json_object = json.dumps(dict,ensure_ascii=False)
        
        if file_name[-5:]!='.json':
            file_name=file_name+'.json'

        # Writing to sample.json
        with open(file_name, "w",encoding='utf-8') as outfile:
            outfile.write(json_object)

    def ret_city_cache(self,city_name):
        try:
            if os.path.exists('{}{}.json'.format(CACHE_PATH,city_name)):
                data = self.read_json(file_path=city_name)
                return data
            else:
                return []
        except:
            return []
    def write_city_restaurants(self,city_name,value):
        new_names =[]
        last_restaurants = self.ret_city_cache(city_name=city_name)
        for res_name in value:
            if res_name not in last_restaurants and res_name !=False:
                new_names.append(res_name)
        
        self.write_json(CACHE_PATH+city_name+'.json',dict=new_names)




if __name__=='__main__':
    web = get_foods()
    web.open_snap_food()
    web.set_city_page()
    # web.open_snap_food()

    web.set_area_page(' خاقانی')
    web.get_all_restaurants_name_city()
    web.search_in_res_names()
    web.search_restaurant(name='فست فود رستوران سارا (جی)')
    web.get_name_price('sara')