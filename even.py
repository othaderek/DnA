def evenDigitsNumber(a):
    even = 0
    
    for i in a:
        s = str(i)
        if len(s) % 2 == 0:
            even += 1
    return even
    

print(evenDigitsNumber([12, 134, 111, 1111, 10]))
