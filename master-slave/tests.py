import unittest
import queue
from multiprocessing import Process, Queue

from main import sum_worker, run

class TestHandler(unittest.TestCase):
    def test_sum_worker(self):
        input_queue = Queue()
        output_queue = Queue()

        input_queue.put(1)
        input_queue.put(2)
        input_queue.put(3)
        input_queue.put(4)
        input_queue.put(None) # Error break

        process = Process(target=sum_worker, args=(input_queue, output_queue))
        process.start()

        results = []

        while True:
            try:
                incremented = output_queue.get(timeout=1)
                if incremented is None:
                    break
                results.append(incremented)
            except queue.Empty:
                break

        process.join()

        self.assertEqual(results, [2, 3, 4, 5])

    def test_run_master_slave(self):
        numbers = [1, 2, 3, 4, 5, 6, 7]
        results = run(numbers)

        self.assertEqual(sorted(results), sorted([2, 3, 4, 5, 6, 7, 8]))


if __name__ == '__main__':
    unittest.main()