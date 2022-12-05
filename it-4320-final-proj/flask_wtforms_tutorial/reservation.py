def Add_reservation(firstName, row, column):

    if (check_availability(row, column) == False):
        return False
    while (True):
        # figured i should make sure they are inputing integers
        if (not row.isdigit() or not column.isdigit()):
            print('Enter valid seat row and column.\n')
        elif (int(row) < 1 or int(row) > 10 or int(column) < 1 or int(column) > 5 or seating_chart[int(row)-1][int(column)-1] != 'O'):
            print('Row:{} Seat:{} is not available. Please choose again.\n'.format(
                row, column))
        else:
            break

    code = generate_reservation_code(firstName)

    file = open('reservation.txt', 'a')  # this should open it as append
    record = ('\n'+firstName+','+str(row)+','+str(column)+','+code)
    file.write(record)
    file.close()

    test = [[1,0,0,0]]

def check_availability(row, col):
  return True