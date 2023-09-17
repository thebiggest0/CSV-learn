import csv
'''
open file: googleSurvey.csv, read mode, name file once open "file" 
loads file into variable reader
for loop: calls upon each row in reader (it will be a list), call on individual items by index
*fragile design: changes can break it...
'''

with open("googleSurvey.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])


# Using csv.DictReader, it will now return key:value pair because each row is now a dictionary
# allows for: flexibility
# added a way to count male/ females with 2 variables and for loop

with open("googleSurvey.csv", "r") as file:
    reader = csv.DictReader(file)
    male, female = 0, 0
    for row in reader:
        variable = row["2. What gender do you identify as?"]
        if variable.lower() == "male":
            male += 1
        elif variable.lower() == "female":
            female += 1

    print("male:", male, "female", female)


# to be even more flexible, we change the male/ female variables to a dictionary
# now, new answers can be recorded and printed too

with open("googleSurvey.csv", "r") as file:
    reader = csv.DictReader(file)
    keys = {}
    for row in reader:
        variable = row["4. To what extent does price impact your choices when you're shopping for groceries?"]
        if variable.lower() not in keys:
            keys[variable.lower()] = 1
        else:
            keys[variable.lower()] += 1

    for key in sorted(keys, key=lambda x: keys[x], reverse=True):
        # sorted() allows us to make an un-ordered dictionary ordered
        # don't worry about lambda, pretty much sorts dictionary from largest value first
        print(key, keys[key])