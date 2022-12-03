import csv

accounts = {}

def authenticate(username, password):

    with open('passcodes.csv', 'r') as file:
        passstr = csv.reader(file)

        for line in passstr:
            if(username == line[0] and password == line[1].replace(' ', '')):
                return True

        return False

testUser = "admin2"
testPass = "24680"

authenticate(testUser,testPass)

print(authenticate(testUser, testPass))
