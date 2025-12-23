# accidental_duplication.py
def main():
    greet_user("Alice")



def greet_user(name):
    print(f"Hello, {name}!")

# --- accidentally repeated code starts here ---

<<<< HEAD <<<
def main():
    greet_user("Alice")

>>>>> BASE >>>>>
def main():
    greet_user("Alice")


if __name__ == "__main__":
    main()


