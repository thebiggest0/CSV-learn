import csv
import random

'''
writes data to CSV file
writer_one: writes inputs into file
writer_two: writes random data into files (for test cases)
'''

def writer_one():
    with open("groceryList.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        item = input("What is the item: ")
        price = input("How much is it: ")
        location = input("Where did you find this: ")

        writer.writerow([item, price, location])


def writer_two(items, locations):
    with open("groceryList.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        index_one = random.randrange(len(items))
        index_two = random.randrange(len(locations))
        item = items[index_one]
        price = random.randrange(100)
        location = locations[index_two]

        writer.writerow([item, price, location])

# list of inputs to be used for random generation
items = ["egg", "milk", "beef", "chicken", "chips", "banana", "apple"]
locations = ["costco", "price smart", "shoppers", "super store", "walmart", "t&t"]

# writes 100 randomly generated test files to groceryList.csv
for _ in range(100):
    writer_two(items, locations)