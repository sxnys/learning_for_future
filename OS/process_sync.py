from multiprocessing import Process
from datetime import datetime

mutex = 1
empty = 10
full = 0
items = []

class Item:
    index = 0
    def __init__(self):
        index += 1
        self.index = index
        self.time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    def __repr__(self):
        return '{}({}, {})'.format(type(self).__name__, self.index, self.time)

def produce_item():
    return Item()

def consume_item(item):
    print('Consume {}'.format(item))

def insert_item(item):
    items.append(item)

def remove_item():
    return items.pop()

def down(signal, type):
    global mutex, item, full
    l = [mutex, item, full]
    if signal > 0:
        l[type] -= 1
    else:
        producer_process.terminate()
        consumer_process.run()

def producer():
    global mutex, item, full
    while True:
        item = produce_item()
        down(empty, 1)
        down(mutex, 0)
        insert_item(item)
        up(mutex, 0)
        up(full, 2)

def consumer():
    global mutex, item, full
    while True:
        down(full, 2)
        down(mutex, 0)
        item = remove_item()
        consume_item(item)
        up(mutex, 0)
        up(empty, 1)

if __name__ == '__main__':
    producer_process = Process(target=producer)
    consumer_process = Process(target=consumer)