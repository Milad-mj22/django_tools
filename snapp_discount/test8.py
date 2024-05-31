import convert_numbers

a= {'پیتزا تی ان تی آمریکایی':'۱۵\n۲۵۴,۰۰۰\n۲۱۵,۹۰۰ تومان'\
    ,'برگر سوخاری':'۱۵\n۱۹۶,۰۰۰\n۱۶۶,۶۰۰ تومان','مرغ سوخاری نه تکه':'۵۷۸,۰۰۰ تومان'}


# for name,price in zip(a.keys(),a.values()):
#     print(name,price)
#     a=price[2]
#     a= price.split('\n')
#     print(len(a))
#     b=convert_numbers.persian_to_english(a[1])
#     print(price[0])

import json

def write_json(file_name,dict):

    # Serializing json
    json_object = json.dumps(dict,ensure_ascii=False)
    
    if file_name[-5:]!='.json':
        file_name=file_name+'.json'

    # Writing to sample.json
    with open(file_name, "w",encoding='utf-8') as outfile:
        outfile.write(json_object)


write_json('a',dict=a)