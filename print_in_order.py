from threading import Event, Thread
from typing import Callable

class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond: Callable[[], None]) -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird: Callable[[], None]) -> None:
        self.second_done.wait()
        printThird()


def printFirst():
    print("first")

def printSecond():
    print("second")

def printThird():
    print("third")


if __name__ == "__main__":
    foo = Foo()

    # Threads started in random order
    t1 = Thread(target=foo.second, args=(printSecond,))
    t2 = Thread(target=foo.first, args=(printFirst,))
    t3 = Thread(target=foo.third, args=(printThird,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

# output:
# first
# second
# third