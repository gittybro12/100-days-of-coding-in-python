# fibonacci sequence can be defined as a series of 
# numbers in which each superseding number is a sum 
# of the 2 preceding numbers

def fibonacci(number):
    if number < 0:
        print ('please enter a positive number')
    elif number == 1:
        print (0)
    elif number  == 2:
        print (1)
    else:
        sequence = [0,1]
        while len(sequence) < number :
            sequence.append(sequence[-1] + sequence[-2])
            print(sequence)
        
fibonacci(1)