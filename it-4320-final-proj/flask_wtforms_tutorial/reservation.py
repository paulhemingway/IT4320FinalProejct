from .chart import *

def add_reservation(firstName, row, column, code):

    if (is_available(row-1, column-1) == False):
        return False


    file = open('reservations.txt', 'a')  # this should open it as append
    record = ('\n'+firstName+', '+str(row-1)+', '+str(column-1)+', '+code)
    file.write(record)
    file.close()

    return True

def is_available(row, col):
    chart = display_chart()

    return chart[row][col] == 0

def generate_reservation_code(firstName):
    str = "INFOTC4320"
    output = ""
    n = 0 

    n = max(len(str), len(firstName))

    for i in range(n):
        if(i < len(firstName)):
            output += firstName[i]
        if(i < len(str)):
            output += str[i]

    return output
    