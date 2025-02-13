def convert_cel_to_far(c):
    f = c * (9/5) + 32
    return round(f,2)
c = float(input("Enter the temperature in Celcius: "))
print(f"{c} degrees C = {convert_cel_to_far(c)} degrees in F")

def convert_far_to_cel(f):
    c = (f-32) * (5/9)
    return round(c,2)
f = float(input("Enter the temperature in Fahrenheit: "))
print(f"{f} degrees F = {convert_far_to_cel(f)} degrees in C")
