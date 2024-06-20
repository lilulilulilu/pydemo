

# Review 1

def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list

'''
comments: the type of my_list is mutable and its default value of my_list is [], when call add_to_list(1) twice, the second time it will return [1, 1], please check if this is expected. 
If you want to initiate my_list as empty list every time, you can change the default value to None and initiate it in the function body as blow:
def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list
'''


# Review 2

def format_greeting(name, age):

    return "Hello, my name is {name} and I am {age} years old."

'''
comments: missed 'f', the return statement shoud be: f"Hello, my name is {name} and I am {age} years old."
'''


# Review 3

class Counter:

    count = 0

    def __init__(self):
        self.count += 1
 
    def get_count(self):
        return self.count
    
'''
comments: the count is a class variable and all instances share the same value, the self.count += 1 line in the __init__ method is not incrementing the class variable count. please check if it's expected.
if it's not, the class variable "count" should be accessed and modified through the class name as below:
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
 
    def get_count(self):
        return Counter.count

'''

 

# Review 4

import threading

class SafeCounter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

 
def worker(counter):
    for _ in range(1000):
        counter.increment()

counter = SafeCounter()
threads = []

for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
'''
comments: self.count += 1 is not thread-safe, the increment method should be protected by a lock to prevent concurrent access to the count variable as below.
class SafeCounter:

    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1

'''


# Review 5

def count_occurrences(lst):

    counts = {}

    for item in lst:

        if item in counts:

            counts[item] =+ 1

        else:

            counts[item] = 1

    return counts

'''
comments: the counts[item] =+ 1 may should be counts[item] += 1, since counts[item] =+ 1 means counts[item] = 1.
'''

 