import time
from queue import Queue
from faker import Faker
from random import randint

q = Queue()


class Order:
    def __init__(self, full_name: str):
        self.full_name = full_name


def generate_request():
    print('Generating orders...')
    fake = Faker()
    for _ in range(randint(0, 3)):
        order = Order(fake.name())
        q.put(order)
        print(f'Order from customer {order.full_name} was queued')


def process_request():
    print('Processing orders...')
    if q.empty():
        print('The queue is empty')
        return

    while not q.empty():
        order = q.get()
        print(f'Order from customer {order.full_name} was processed')


while True:
    generate_request()
    process_request()
    time.sleep(2)