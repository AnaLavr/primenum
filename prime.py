def is_prime(num):
    b=0
    for i in range(2,num):  
        if num%i == 0:
            b += 1
    if b!=0:
        return('False')    
    else:
        return('True')
    
print(is_prime(8))






 
    








































