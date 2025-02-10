t = 30  
h = 25  
w = 205  

pred = (0.5 * t * t) - (0.2 * h) + (0.1 * w) - 15  

if pred > 300:  
    print("Sunny")  
elif pred > 200 and pred <= 300:  
    print("Cloudy")  
elif pred > 100 and pred <= 200:  
    print("Rainy")  
else:  
    print("Stormy")
