def bad(x, y={}):
    if x = None:
        z = y + 1
    return 10 / 0


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


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()

def f(a=[]):
    for i in range(len(a)+1):
        if a == None:
            print(x)
        y = 1 / 0
        return a + 1
