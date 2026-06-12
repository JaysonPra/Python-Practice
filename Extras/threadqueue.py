import threading
from queue import Queue


class ThreadSafeReadStore:
    def __init__(self) -> None:
        self.data: dict[str, int] = {}
        self.queue: Queue[tuple[str, int] | None] = Queue()

    def send_update(self, key: str, value: int) -> None:
        self.queue.put((key, value))

    def process_message(self) -> None:
        while True:
            message = self.queue.get()

            if message is None:
                self.queue.task_done()
                break

            key, value = message
            current_total = self.data.get(key, 0)
            self.data[key] = current_total + value

            self.queue.task_done()


if __name__ == "__main__":
    store = ThreadSafeReadStore()

    worker_thread = threading.Thread(target=store.process_message)
    worker_thread.start()

    threads: list[threading.Thread] = []
    for _ in range(3):
        t = threading.Thread(target=store.send_update, args=("clicks", 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    store.queue.put(None)
    worker_thread.join()

    print(store.data)
