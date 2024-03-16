import threading
import time
import philosofer_dinners
from philosofer_dinners import DiningPhilosophers
def test_dining_philosophers():
    # Define the mock functions
    def pickLeftFork():
        print(threading.current_thread().name, "picks up left fork")

    def pickRightFork():
        print(threading.current_thread().name, "picks up right fork")

    def eat():
        print(threading.current_thread().name, "eats")

    def putLeftFork():
        print(threading.current_thread().name, "puts down left fork")

    def putRightFork():
        print(threading.current_thread().name, "puts down right fork")

    # Create an instance of DiningPhilosophers
    dp = DiningPhilosophers()

    # Create 5 threads, each representing a philosopher
    philosophers = [threading.Thread(target=dp.wantsToEat, args=(i, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)) for i in range(5)]

    # Start all threads
    for p in philosophers:
        p.start()

    # Wait for all threads to complete
    for p in philosophers:
        p.join()

# Run the test
def some_function():
    print(threading.current_thread().name, "puts down left fork")
    
test_dining_philosophers()
some_function()