def display_chart():
    chart = [[0,0,0,0] for row in range(12)]


    with open("reservations.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            cell = line.split(", ")
            chart[int(cell[1])][int(cell[2])] = 1

        file.close()

    return chart
