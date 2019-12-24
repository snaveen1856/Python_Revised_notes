import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s)')

"""
import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} seconds")
    time.sleep(seconds)
    print(f"Done sleeping {seconds} seconds")


t1 = threading.Thread(target=do_something, args=[1.5])
t2 = threading.Thread(target=do_something, args=[1.5])
t1.start()
t2.start()
t1.join()
t2.join()
finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
"""