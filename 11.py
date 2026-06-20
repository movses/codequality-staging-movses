# accidental_duplication.py

def greet_user(name):
    print(f"Hello, {name}!")

# --- accidentally repeated code starts here ---


def main():
    greet_user("Alice")

def main():
    greet_user("Alice")


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

