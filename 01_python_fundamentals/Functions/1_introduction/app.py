def add(marks):
    '''This function adds all the marks in the list and returns the total
    Input: list of marks
    Output: total of marks
    Eg: add([10, 20, 30]) returns 60
    
    '''
    total = 0
    for mark in marks:
        total += mark
    return total

def greet(name):
    '''This function greets the person with the given name
    Input: name (string)
    Output: greeting message (string)
    Eg: greet("Alice") returns "Hello, Alice!"
    
    '''
    return f"Hello, {name}!"

def isPrime(number,starting_point):
    '''This function will help in finding prime number developed by xyz'''
    isDivisible = False;
    i=starting_point;
    if starting_point<number:
        while i < number:
            if number % i == 0:
                isDivisible = True;
                break; # this line is the only addition.
            i += 1;

        if isDivisible:
            return "{} is NOT a Prime number".format(number)
        else:
            return "{} is a Prime number".format(number)
        
    return 'starting point can be more then input number'

database = {}
def create_user(username,email):
    if username in database:
        return "User already exists"
    database[username] = email
    return "User created successfully"

def read_user(username):
    return database.get(username, "User not found")
def update_user(username, email):
    if username not in database:
        return "User not found"
    database[username] = email
    return "User updated successfully"

