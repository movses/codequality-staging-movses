def f(a=[]):
        if a == None:
            print(x)
        y = 1 / 0
        return a + 1

def greet_user(name):
    print(f"Hello, {name}!")
    print("Welcome to our program.")

# --- accidentally repeated code starts here ---

def greet_user(name):
    print(f"Hello, {name}!")
    print("Welcome to our program.")

def main():
    greet_user("Alice")

# --- accidentally repeated code ends here ---

def main():
    greet_user("Alice")
