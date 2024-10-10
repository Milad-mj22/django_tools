

LANGUAGE = 'fa'

def translate(input):
    
    if LANGUAGE == 'en':

        return input
    

    if LANGUAGE == 'fa':
        if input =='number':
            return 'عدد'
        if input =='kg':
            return 'کیلوگرم'
        if input =='pack':
            return 'بسته'