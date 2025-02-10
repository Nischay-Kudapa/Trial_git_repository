with open('inputvalues.txt', 'r') as file:  
    lines = file.readlines()  

for i in range(0, len(lines), 3):  
    t = int(lines[i].strip())  
    h = int(lines[i + 1].strip())  
    w = int(lines[i + 2].strip())  

    pred = (0.5 * t * t) - (0.2 * h) + (0.1 * w) - 15  

    if pred > 300:  
        print("Sunny")  
    elif pred > 200 and pred <= 300:  
        print("Cloudy")  
    elif pred > 100 and pred <= 200:  
        print("Rainy")  
    else:  
        print("Stormy")
