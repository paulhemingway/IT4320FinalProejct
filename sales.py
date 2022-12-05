'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def Calculate_sales():
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

#Total_Sales = Calculate_sales()
#print(Total_Sales)