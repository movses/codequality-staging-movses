
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

<<<<<< HEAD <<<<<
>>>>>> BASE >>>>>

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

def bad(x, y={}):
    if x = None:
        z = y + 1
    return 10 / 0
