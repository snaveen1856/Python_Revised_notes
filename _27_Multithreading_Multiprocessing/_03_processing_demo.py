import multiprocessing
import time
from multiprocessing import freeze_support
import concurrent.futures

st = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds")
    time.sleep(seconds)
    print(f"sleeping done {seconds} seconds")


if __name__ == '__main__':
    freeze_support()
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     results = [executor.submit(do_something, 1.5) for _ in range(10)]
    #     for i in concurrent.futures.as_completed(results):
    #         print(i.result())
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something, sec) for sec in secs]
        for i in concurrent.futures.as_completed(results):
            print(i.result())
        fn = time.perf_counter()
        print(f"Finished in {round(fn - st, 2)} seconds")

"""
import multiprocessing
import time
from multiprocessing import freeze_support

st = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} seconds")
    time.sleep(seconds)
    print(f"sleeping done {seconds} seconds")


if __name__ == '__main__':
    freeze_support()
    p1 = multiprocessing.Process(target=do_something, args=[1])
    p2 = multiprocessing.Process(target=do_something, args=[1])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    fn = time.perf_counter()
    print(f"Finished in {round(fn - st, 2)} seconds")
"""
"""
import time

st = time.perf_counter()


def do_somthing(seconds):
    print(f"Sleeping {seconds} seconds")
    time.sleep(seconds)
    print(f"sleeping done {seconds} seconds")


do_somthing(2)
do_somthing(1)
fn = time.perf_counter()
print(f"Finished in {round(fn - st, 2)} seconds")
"""
"""
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')
"""
