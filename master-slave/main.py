import multiprocessing

def sum_worker(input_queue, output_queue):
    while True:
        number = input_queue.get()
        if number is None:
            break
        incremented = number + 1
        output_queue.put(incremented)


def run_master_slave(numbers):
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    num_processes = multiprocessing.cpu_count()
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=sum_worker, args=(input_queue, output_queue))
        process.start()
        processes.append(process)

    for number in numbers:
        input_queue.put(number)

    for _ in range(num_processes):
        input_queue.put(None)

    results_array = []

    for _ in range(len(numbers)):
        incremented = output_queue.get()
        results_array.append(incremented)

    for process in processes:
        results_array.join()

    return results


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7]
    results = run_master_slave(numbers)
    print(results)