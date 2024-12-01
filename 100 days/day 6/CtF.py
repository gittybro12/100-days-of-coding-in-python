# A PROGRAM THAT CONVERTS CELSIUS TO FAHRENHEIT AND VICE VERSA
import time

def to_fahrenheit():
    global user_input
    sorbet = (user_input * 9/5)
    ben = sorbet + 32
    print('CONVERTING.....')
    time.sleep(5)
    print(f'{ben}*F')

def to_celsius():
    global user_input
    jake = (user_input - 32)
    fin = jake * 5/9
    print('CONVERTING.....')
    time.sleep(5)
    print(f'{fin}*C')
bacon = False
while not bacon:
    dynamic = ''
    welcome = input('CONVERT TO CELSIUS OR FAHRENHEIT?').lower()
    if welcome == 'fahrenheit':
        dynamic += 'celsius'
        user_input = int(input(f"please enter temperature {dynamic}:"))
        to_fahrenheit()
    elif welcome == 'celsius':
        dynamic += 'fahrenheit'
        user_input = int(input(f"please enter temperature {dynamic}:"))
        to_celsius()
    else:
        print('enter valid input')

    inp = input('continue program y/n: ').lower()
    if inp == 'n':
        bacon = True
        print('GOODBYE')
    

