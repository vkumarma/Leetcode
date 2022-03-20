def intToRoman(num):
    q = 0
    n = 0
    some_str = ""
    hash = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
    }
    
    while num > 0:
        if num >= 1000:
            q = int(num / 1000)
            num = num % 1000
            n = 1000
        elif num >= 500:
            if num >= 900:
                num = num - 900
                some_str += "CM"
                q = 0
            else:
                q = int(num / 500)
                num = num % 500
                n = 500
        elif num >= 100:
            if num >= 400:
                num = num - 400
                some_str += "CD"
                q = 0
            else:
                q = int(num / 100)
                num = num % 100
                n = 100
        elif num >= 50:
            if num >= 90:
                num = num - 90
                some_str += "XC"
                q = 0
            else:
                q = int(num / 50)
                num = num % 50
                n = 50
        elif num >= 10:
            if num >= 40:
                num = num - 40
                some_str += "XL"
                q = 0
            else:
                q = int(num / 10)
                num = num % 10
                n = 10
        elif num >= 5:
            if num == 9:
                some_str += "IX" 
                num = num - 9
                q = 0
            else:
                q = int(num / 5)
                num = num % 5
                n = 5
        elif num >= 1:
            if num == 4:
                num = num - 4
                some_str += "IV" 
                q = 0
            else:
                q = int(num / 1)
                num = num % 1
                n = 1
            
        for i in range(0,q):
            some_str += hash[n]
        
    return some_str
                
print(intToRoman(456))    
                
                
                
                
                
                
                
                
                
        
