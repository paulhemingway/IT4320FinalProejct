from pathlib import Path

def authenticate(username, password):
    with open('passcodes.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            creds = line.split(", ")
            
            if(username == creds[0] and password == creds[1].replace('\n', '')):
                return True

        return False

def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def calculate_sales():
    sales = 0
    matrix = get_cost_matrix()
    reservation = 0
    with open('reservations.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.split(", ")
            
            if int(data[2]) == 0:
                sales += int(matrix[reservation][0])
            
            elif int(data[2]) == 1:
                sales += int(matrix[reservation][1])
                
            elif int(data[2]) == 2:
                sales += int(matrix[reservation][2])
                
            elif int(data[2]) == 3:
                sales += int(matrix[reservation][3])
            

    return(sales)