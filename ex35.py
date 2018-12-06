#nested_if statement
statement1 = 'true'
nested_statement = ''
if statement1: #outer if statement
    print("true")
    if nested_statement: #nested if statement
        print("yes")
    else: #nested else statement
        print("no")
else: #outer else statement
    print("false")
