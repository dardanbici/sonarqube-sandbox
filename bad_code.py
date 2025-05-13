# bad_code.py

# Security vulnerability
def insecure_eval():
    user_input = input("Enter code: ")
    eval(user_input)  # 🚨 This should be flagged by Sonar as dangerous


# Duplicate logic
def duplicate_logic_one():
    print("Duplicated logic here")

def duplicate_logic_two():
    print("Duplicated logic here")  # 🚨 Sonar will flag this as duplicate


# Maintainability issue: unused variable
def unused_variable_example():
    temp = 42  # 🚨 Never used
    return "This function has dead code"


# Bug risk: swallowed exception
def silent_fail():
    try:
        1 / 0
    except:
        pass  # 🚨 Exception swallowed with no logging
