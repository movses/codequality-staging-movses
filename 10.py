def f(a=[]):
    for i in range(len(a)+1):
        if a == None:
            print(x)
        y = 1 / 0
        return a + 1



# accidental_duplication.py
def greet_user(name):
    print(f"Hello, {name}!")


def main():
    greet_user("Alice")



def greet_user(name):
    print(f"Hello, {name}!")

# --- accidentally repeated code starts here ---

<< HEAD <<<
def main():
    greet_user("Alice")

>>>>> BASE >>>>>
def main():
    greet_user("Alice")


if __name__ == "__main__":
    main()


