print('You can use Fahrenheit, Celsius, Kelvin, Metric units, Inches, Yards, Feet, Pounds, Ounces, Grams, Digital Storage units and Miles_per_Hour or Kilometers_per_Hour as well as Knots.')

def Convert():
    input('What units are you working with? ')

units = input('What units are you working with? ')

value = int(input (f"How many {units}? "))
    
if units in ['Fahrenheit', 'Celsius', 'Kelvin']:
    
    if units == "Fahrenheit":
        
        Fahrenheit = value
        
        Celsius = (value - 32) * (5/9)
        
        Kelvin = (value - 32) * (5/9) + 273.15            
    
    if units == "Celsius":
        
        Celsius = value 
        
        Fahrenheit = Celsius * 9/5 + 32
        
        Kelvin = Celsius + 273.15            
    
    elif units == "Kelvin":
        
        Kelvin = value
        
        Celsius = Kelvin - 273.15
        
        Fahrenheit = (Kelvin - 273.15) * 9/5 + 32           
    
    print('Fahrenheit =', Fahrenheit)
    print('Celsius =', Celsius)
    print('Kelvin =', Kelvin)

if units in ['Inches', 'Feet', 'Yards', 'Miles']:

    if units == "Inches":
        Inches = value
    
        Feet = Inches / 12
    
        Yards = Inches / 36
    
        Miles = Inches / 63360

    if units == "Feet":
        Feet = value
    
        Inches = Feet * 12
    
        Yards = Feet / 36
    
        Miles = Feet / 5280
    
    if units == "Yards":
        Yards = value
        
        Feet = Yards * 3
        
        Inches = Yards * 36
        
        Miles = Yards / 1760

    if units == "Miles":
        Miles = value
        
        Inches = Miles * 63360
        
        Feet = Miles * 5280
        
        Yards = Miles * 1760
        
    print('Inches =', Inches)
    print('Feet =', Feet)
    print('Yards =', Yards)
    print('Miles =', Miles)

if units in ['Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Petabytes', 'Exabytes']:
    
    
    if units == "Bytes":
        
        Bytes = value
        
        Kilobytes = Bytes * (10**-3)
        
        Megabytes = Bytes * (10**-6)
        
        Gigabytes = Bytes * (10**-9)
        
        Terabytes = Bytes * (10**-12)
        
        Petabytes = Bytes * (10**-15)
        
        Exabytes = Bytes * (10**-18)
        
    if units == "Kilobytes":
        
        Kilobytes = value
        
        Bytes = Kilobytes * (10**3)
        
        Megabytes = Kilobytes * (10**-3)
        
        Gigabytes = Kilobytes * (10**-6)
        
        Terabytes = Kilobytes * (10**-9)
        
        Petabytes = Kilobytes * (10**-12)
        
        Exabytes = Kilobytes * (10**-15)
        
    if units == "Megabytes":
        
        Megabytes = value
        
        Bytes = Megabytes * (10**6)
        
        Kilobytes = Megabytes * (10**3)
        
        Gigabytes = Megabytes * (10**-3)
        
        Terabytes = Megabytes * (10**-6)
        
        Petabytes = Megabytes * (10**-9)
        
        Exabytes = Megabytes * (10**-12)
    
    if units == "Gigabytes":
        
        Gigabytes = value
        
        Kilobytes = Gigabytes * (10**9)
        
        Bytes = Gigabytes * (10**6)
        
        Megabytes = Gigabytes * (10**3)
        
        Terabytes = Gigabytes * (10**-3)
        
        Petabytes = Gigabytes * (10**-6)
        
        Exabytes = Gigabytes * (10**-9)       
    
    if units == "Terabytes":
        
        Terabytes = value
        
        Bytes = Terabytes * (10**12)
        
        Kilobytes = Terabytes * (10**9)
        
        Gigabytes = Terabytes * (10**6)
        
        Megabytes = Terabytes * (10**3)
        
        Petabytes = Terabytes * (10**-3) 
        
        Exabytes = Terabytes * (10**-6)                    
    
    if units == "Petabytes":
        
        Petabytes = value
        
        Bytes = Petabytes * (10**15)
        
        Kilobytes = Petabytes * (10**12)
        
        Gigabytes = Petabytes * (10**9)
        
        Megabytes = Petabytes * (10**6)
        
        Terabytes = Petabytes * (10**3)
        
        Exabytes = Petabytes * (10**-3)
        
    if units == "Exabytes":
        
        Exabytes = value
        
        Kilobytes = Exabytes * (10**18)
        
        Bytes = Exabytes * (10**15)
        
        Megabytes = Exabytes * (10**12)
        
        Gigabytes = Exabytes * (10**9)
        
        Terabytes = Exabytes * (10**6)
        
        Petabytes = Exabytes * (10**3)
    
    print('Bytes =', Bytes)
    print('Kilobytes =', Kilobytes)
    print('Megabytes =', Megabytes)
    print('Gigabytes =', Gigabytes)
    print('Terabytes =', Terabytes)
    print('Petabytes =', Petabytes)
    print('Exabytes =', Exabytes)

if units in ['Millimeters', 'Centimeters', 'Meters']:
    
    if units == "Millimeters":
        
        Millimeters = value
        
        Centimeters = Millimeters * 0.1
        
        Meters = Millimeters * 0.01
        
    if units == "Centimeters":
        
        Centimeters = value
        
        Millimeters = Centimeters * 10
        
        Meters = Centimeters * 0.01
        
    if units == "Meters":
        
        Meters = value
        
        Millimeters = Meters * 1000
        
        Centimeters = Meters * 100
        
    print('Millimeters =', Millimeters)
    print('Centimeters =', Centimeters)
    print('Meters =', Meters)
    
    
if units in ['Grams', 'Ounces', 'Pounds', 'Tons']:
    
    if units == "Grams":
        
        Grams = value
        
        Ounces = Grams / 28.35
        
        Pounds = Grams / 453.592
        
        Tons = Grams / 907184.74
        
    if units == "Ounces":
        
        Ounces = value
        
        Grams = Ounces * 28.35
        
        Pounds = Ounces / 16
        
        Tons = Ounces / 32000
        
    if units == "Pounds":
        
        Pounds = value
        
        Ounces = Pounds * 16
        
        Grams = Pounds * 453.592
        
        Tons = Pounds / 2000
        
    if units == "Tons":
        
        Tons = value
        
        Ounces = Tons * 32000
        
        Grams = Tons * 907184.74
        
        Pounds = Tons * 2000
        
    print('Ounces =', Ounces)
    print('Grams =', Grams)
    print('Pounds =', Pounds)
    print('Tons =', Tons)
    
if units in ['Miles_Per_Hour', 'Kilometers_Per_Hour']:
    
    if units == "Miles_Per_Hour":
        
        Miles_Per_Hour = value
        
        Kilometers_Per_Hour = Miles_Per_Hour * 1.609
        
    if units == "Kilometers_Per_Hour":
        
        Kilometers_Per_Hour = Miles_Per_Hour / 1.609
        
    print('Miles_Per_Hour =', Miles_Per_Hour)
    print('Kilometers_Per_Hour =', Kilometers_Per_Hour)
