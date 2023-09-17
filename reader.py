import csv
'''
open file: googleSurvey.csv, read mode, name file once open "file" 
loads file into variable reader
for loop: calls upon each row in reader (it will be a list), call on individual items by index
*fragile design: changes can break it...
'''

def design_one():
    with open("googleSurvey.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[1])


# Using csv.DictReader, it will now return key:value pair because each row is now a dictionary
# allows for: flexibility
# added a way to count male/ females with 2 variables and for loop

def design_two():
    with open("googleSurvey.csv", "r") as file:
        reader = csv.DictReader(file)
        male, female = 0, 0
        for row in reader:
            variable = row["2. What gender do you identify as?"]
            if variable.lower() == "male":
                male += 1
            elif variable.lower() == "female":
                female += 1

        return(print("male:", male, "female", female))


# to be even more flexible, we change the male/ female variables to a dictionary
# now, new answers can be recorded and printed too
def design_three():
    with open("googleSurvey.csv", "r") as file:
        reader = csv.DictReader(file)
        keys = {}
        for row in reader:
            variable = row["2. What gender do you identify as?"]
            if variable.lower() not in keys:
                keys[variable.lower()] = 1
            else:
                keys[variable.lower()] += 1

        for key in sorted(keys, key=lambda x: keys[x], reverse=True):
            # sorted() allows us to make an un-ordered dictionary ordered
            # don't worry about lambda, pretty much sorts dictionary from largest value first
            print(key, keys[key])


# creating a function that can return cheapest item price and it's location + average price
def design_four():
    with open("groceryList.csv", "r") as file:
        reader = csv.reader(file)
        next(file)
        count = {}
        cheapest = {}

        for row in reader:
            #x, y, z = row[0], row[1], row[2]

            if row[0] not in count:
                count[row[0]] = 1
            else:
                count[row[0]] += 1

            if row[0] not in cheapest:
                cheapest[row[0]] = (row[1], row[2])
            else:
                if cheapest[row[0]][0] > row[1]:
                    cheapest[row[0]] = (row[1], row[2])

        for item in count:
            print(item + ":", count[item])
            print("cheapest: $" + cheapest[item][0], "from", cheapest[item][1])


# improved to dictionary, instead of using a list
def design_five():
    with open("groceryList.csv", "r") as file:
        reader = csv.DictReader(file)
        count = {}
        cheapest = {}

        for row in reader:
            item, price, location = row["item"], row["price"], row["location"]

            if item not in count:
                count[item] = 1
            else:
                count[item] += 1

            if item not in cheapest:
                cheapest[item] = (price, location)
            else:
                if cheapest[item][0] > price:
                    cheapest[item] = (price, location)

        for name in count:
            print(name + ":", count[name])
            print("cheapest: $" + cheapest[name][0], "from", cheapest[name][1])

    return count, cheapest


# call on function and return the 2 dictionaries
count, cheapest = design_five()

# allow user to input an item for search, if present return cheapest price and location
search_item = input("what item do you want to check? ")
if search_item in cheapest:
    print("cheapest " + search_item + " is available at " + cheapest[search_item][1] + " for $" + cheapest[search_item][0])
else:
    print("item not in data")