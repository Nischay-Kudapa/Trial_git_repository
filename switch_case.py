def calculate_weather(t, h, w):  
    pred = (0.5 * t * t) - (0.2 * h) + (0.1 * w) - 15  
    if pred > 300:  
        return "Sunny"  
    elif pred > 200 and pred <= 300:  
        return "Cloudy"  
    elif pred > 100 and pred <= 200:  
        return "Rainy"  
    else:  
        return "Stormy"  

def hardcoded_input():  
    t, h, w = 30, 25, 205  
    print(f"The weather condition is: {calculate_weather(t, h, w)}")  

def user_input():  
    t = int(input("Enter temperature: "))  
    h = int(input("Enter humidity: "))  
    w = int(input("Enter wind speed: "))  
    print(f"The weather condition is: {calculate_weather(t, h, w)}")  

def file_input():  
    with open('inputvalues.txt', 'r') as file:  
        lines = file.readlines()  

    for i in range(0, len(lines), 3):  
        t = int(lines[i].strip())  
        h = int(lines[i + 1].strip())  
        w = int(lines[i + 2].strip())  

        print(f"The weather condition is: {calculate_weather(t, h, w)}")  

print("Select an input method:")  
print("1: Hardcoded values")  
print("2: User input")  
print("3: File-based input")  

choice = int(input("Enter your choice (1-3): "))  

match choice:  
    case 1:  
        hardcoded_input()  
    case 2:  
        user_input()  
    case 3:  
        file_input()  
    case _:  
        print("Invalid choice. Please select a valid option (1-3).")
