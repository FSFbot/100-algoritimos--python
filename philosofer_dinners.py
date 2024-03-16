import threading

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Semaphore(1) for _ in range(5)]
        self.lock = threading.Lock()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        left_fork = philosopher
        right_fork = (philosopher + 1) % 5

        # philosopher with odd number picks right fork first, philosopher with even number picks left fork first
        first_fork = right_fork if philosopher % 2 == 0 else left_fork
        second_fork = left_fork if philosopher % 2 == 0 else right_fork

        with self.forks[first_fork]:
            with self.forks[second_fork]:
                pickLeftFork() if philosopher % 2 == 0 else pickRightFork()
                pickRightFork() if philosopher % 2 == 0 else pickLeftFork()
                eat()
                putLeftFork() if philosopher % 2 == 0 else putRightFork()
                putRightFork() if philosopher % 2 == 0 else putLeftFork()