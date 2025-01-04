# Google pyq questions

def happy_num(n):
    emp = set()  
    while n != 1 and n not in emp:  
        emp.add(n)  
        n = sum(int(i)**2 for i in str(n)) 
    return n == 1 

n = 20 
print(happy_num(n)) 