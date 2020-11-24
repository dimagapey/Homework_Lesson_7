def fahr_temp(temp):
    print('Fahrenheit temperature: ', temp)
    print('Kelvin temperature: ', round((temp + 459.67) // 1.8))
    print('Celsium temperature:', round((temp - 32) / 1.8))

def cels_temp(temp):
    print('Celsium temperature: ', temp)
    print('Fahrenheit temperature:', round(temp * 1.8 + 32))
    print('Kelvin temperature:', round(temp + 273.15))

def kelv_temp(temp):
    print('Kelvin temperature: ', temp)
    print('Fahrenheit temperature:', round(temp * 1.8 - 459.67))
    print('Celsium temperature:', round(temp - 273.15))


temp = int(input('Please, enter the temperature - '))
type_of_temp = input('Please, enter the type of temperature(F, C or K) - ')
if type_of_temp == 'F':
    fahr_temp(temp)
elif type_of_temp == 'C':
    cels_temp(temp)
elif type_of_temp == 'K':
    kelv_temp(temp)
else:
    print('Fatal error :(')