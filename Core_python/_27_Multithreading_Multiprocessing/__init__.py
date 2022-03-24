"""
Differences between a Process and a Thread:
===========================================
A process represents a group of statements which are executed by the PVM using a main thread.
We can take a running program as an example for a process. Each process will have its own memory,
a program counter that keeps track of the instruction being executed and a stack that holds the data.
The data of one process is generally isolated from another process. It means the data or result of a process
is generally not available to another process unless both the processes communicate explicitly.

A thread also represents a group of statements within a program. When we want to use threads, we have to create them
separately which are in turn run by the main thread. Threads will not have their own memory and program counter.
The data of one thread is  shared easily by another thread. So, it is possible that a thread can easily modify the
data of another thread. Any program utilizes resources like memory and processor time. Hence it is called heavy
weight process. But a thread is a small part of the program that takes very less memory  and processor time.
 Hence threads are called light weight processes.

Dr. R. Nageswara Rao. Core Python Programming, 2ed (p. 541). Wiley India. Kindle Edition.

There can only be one thread running at any given time in a python process:
===========================================================================
1.Multiprocessing is parallelism. Multi-threading is concurrency.
2.Multiprocessing is for increasing speed. Multi-threading is for hiding latency(illusion).
3.Multiprocessing is best for computations(download file, different tasks).
     Multi-threading is best for IO(file handling, query DB, web pages loading).
4.If you have CPU heavy tasks, use multiprocessing with n_process = n_cores and never more. Never!
5.If you have IO heavy tasks, use multi-threading with n_threads = m * n_cores with m a number bigger
     than 1 that you can tweak on your own.
 Try many values and choose the one with the best speedup because there isn’t a general rule.
  For instance the default value of m in ThreadPoolExecutor is set to 5 [Source]
 which honestly feels quite random in my opinion.

"""