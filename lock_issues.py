import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    print("Task1: acquiring lock A")
    lock_a.acquire()
    time.sleep(0.1)

    print("Task1: acquiring lock B")
    lock_b.acquire()

    print("Task1: doing work")
    time.sleep(0.2)

    # BUG: lock_a never released
    lock_b.release()
    print("Task1: released lock B")


def task2():
    print("Task2: acquiring lock B")
    lock_b.acquire()
    time.sleep(0.1)

    print("Task2: acquiring lock A")
    lock_a.acquire()  # DEADLOCK potential (reverse order vs task1)

    print("Task2: doing work")
    time.sleep(0.2)

    lock_a.release()
    lock_b.release()
    print("Task2: released both locks")


def task3():
    print("Task3: acquiring lock A")
    lock_a.acquire()
    print("Task3: acquired lock A")

    # BUG: double acquire on non-reentrant lock → deadlock
    print("Task3: acquiring lock A again")
    lock_a.acquire()

    lock_a.release()
    lock_a.release()


def task4():
    print("Task4: acquiring lock B")
    lock_b.acquire()

    # BUG: exception causes lock to never be released
    raise RuntimeError("Unexpected error in task4")

    lock_b.release()


threads = [
    threading.Thread(target=task1),
    threading.Thread(target=task2),
    threading.Thread(target=task3),
    threading.Thread(target=task4),
]

for t in threads:
    t.start()

for t in threads:
    t.join()
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    print("Task1: acquiring lock A")
    lock_a.acquire()
    time.sleep(0.1)

    print("Task1: acquiring lock B")
    lock_b.acquire()

    print("Task1: doing work")
    time.sleep(0.2)

    # BUG: lock_a never released
    lock_b.release()
    print("Task1: released lock B")


def task2():
    print("Task2: acquiring lock B")
    lock_b.acquire()
    time.sleep(0.1)

    print("Task2: acquiring lock A")
    lock_a.acquire()  # DEADLOCK potential (reverse order vs task1)

    print("Task2: doing work")
    time.sleep(0.2)

    lock_a.release()
    lock_b.release()
    print("Task2: released both locks")


def task3():
    print("Task3: acquiring lock A")
    lock_a.acquire()
    print("Task3: acquired lock A")

    # BUG: double acquire on non-reentrant lock → deadlock
    print("Task3: acquiring lock A again")
    lock_a.acquire()

    lock_a.release()
    lock_a.release()


def task4():
    print("Task4: acquiring lock B")
    lock_b.acquire()

    # BUG: exception causes lock to never be released
    raise RuntimeError("Unexpected error in task4")

    lock_b.release()


threads = [
    threading.Thread(target=task1),
    threading.Thread(target=task2),
    threading.Thread(target=task3),
    threading.Thread(target=task4),
]

for t in threads:
    t.start()

for t in threads:
    t.join()
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    print("Task1: acquiring lock A")
    lock_a.acquire()
    time.sleep(0.1)

    print("Task1: acquiring lock B")
    lock_b.acquire()

    print("Task1: doing work")
    time.sleep(0.2)

    # BUG: lock_a never released
    lock_b.release()
    print("Task1: released lock B")


def task2():
    print("Task2: acquiring lock B")
    lock_b.acquire()
    time.sleep(0.1)

    print("Task2: acquiring lock A")
    lock_a.acquire()  # DEADLOCK potential (reverse order vs task1)

    print("Task2: doing work")
    time.sleep(0.2)

    lock_a.release()
    lock_b.release()
    print("Task2: released both locks")


def task3():
    print("Task3: acquiring lock A")
    lock_a.acquire()
    print("Task3: acquired lock A")

    # BUG: double acquire on non-reentrant lock → deadlock
    print("Task3: acquiring lock A again")
    lock_a.acquire()

    lock_a.release()
    lock_a.release()


def task4():
    print("Task4: acquiring lock B")
    lock_b.acquire()

    # BUG: exception causes lock to never be released
    raise RuntimeError("Unexpected error in task4")

    lock_b.release()


threads = [
    threading.Thread(target=task1),
    threading.Thread(target=task2),
    threading.Thread(target=task3),
    threading.Thread(target=task4),
]

for t in threads:
    t.start()

for t in threads:
    t.join()
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    print("Task1: acquiring lock A")
    lock_a.acquire()
    time.sleep(0.1)

    print("Task1: acquiring lock B")
    lock_b.acquire()

    print("Task1: doing work")
    time.sleep(0.2)

    # BUG: lock_a never released
    lock_b.release()
    print("Task1: released lock B")


def task2():
    print("Task2: acquiring lock B")
    lock_b.acquire()
    time.sleep(0.1)

    print("Task2: acquiring lock A")
    lock_a.acquire()  # DEADLOCK potential (reverse order vs task1)

    print("Task2: doing work")
    time.sleep(0.2)

    lock_a.release()
    lock_b.release()
    print("Task2: released both locks")


def task3():
    print("Task3: acquiring lock A")
    lock_a.acquire()
    print("Task3: acquired lock A")

    # BUG: double acquire on non-reentrant lock → deadlock
    print("Task3: acquiring lock A again")
    lock_a.acquire()

    lock_a.release()
    lock_a.release()


def task4():
    print("Task4: acquiring lock B")
    lock_b.acquire()

    # BUG: exception causes lock to never be released
    raise RuntimeError("Unexpected error in task4")

    lock_b.release()


threads = [
    threading.Thread(target=task1),
    threading.Thread(target=task2),
    threading.Thread(target=task3),
    threading.Thread(target=task4),
]

for t in threads:
    t.start()

for t in threads:
    t.join()

