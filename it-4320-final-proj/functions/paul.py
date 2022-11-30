import csv
def print_chart(chart):
  for row in chart:
    for col in row:
      print(str(col) + " ", end=''),
    print()

def read_reservations():
  chart = [[0, 0, 0, 0] for row in range(12)]

  f = open("reservations.txt", "r")
  reader = csv.reader(f, delimiter='\n')

  for row in reader:
    split = row[0].split(',')
    chart[int(split[1])][int(split[2])] = 1

  # print_chart(chart)
  f.close()
  return chart

def check_availability(row, col):
  chart = read_reservations()
  return chart[row][col] == 0


read_reservations()
