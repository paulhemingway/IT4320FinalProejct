from .chart import *

def Add_reservation(firstName, row, column):

    if (check_availability(row, column) == False):
        return False

    code = generate_reservation_code(firstName)

    file = open('reservation.txt', 'a')  # this should open it as append
    record = ('\n'+firstName+','+str(row)+','+str(column)+','+code)
    file.write(record)
    file.close()

def check_availability(row, col):
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
    