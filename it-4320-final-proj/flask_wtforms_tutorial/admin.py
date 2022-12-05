from pathlib import Path

def authenticate(username, password):
    with open('passcodes.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            creds = line.split(", ")
            
            if(username == creds[0] and password == creds[1].replace('\n', '')):
                return True

        return False
