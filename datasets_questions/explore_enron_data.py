#!/usr/bin/python
from __future__ import division
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

total_entry = len(enron_data)
print(total_entry)
print(len(enron_data["SKILLING JEFFREY K"]))

poi_count = 0
persons = []
for person in enron_data:
    persons.append(person)
    if enron_data[person]['poi'] == 1:
        poi_count += 1
print(poi_count)

# print(persons)
print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# who took most of the money
print(enron_data["LAY KENNETH L"]["total_payments"])
print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])

# how many folks in this dataset have a quantified salary? Known email addresses?
salaried_person_count = 0
have_email_address = 0
biggest_outlier = 0
person_name = ''
for person in enron_data:
    if enron_data[person]['salary'] != 'NaN':
        salaried_person_count += 1
    if enron_data[person]['email_address'] != 'NaN':
        have_email_address += 1
    if enron_data[person]['salary'] != 'NaN' and enron_data[person]['bonus'] != 'NaN':
        salary_bonus_ratio = (enron_data[person]['bonus']/enron_data[person]['salary'])
        if salary_bonus_ratio > biggest_outlier:
            biggest_outlier = salary_bonus_ratio
            person_name = person
print(salaried_person_count)
print(have_email_address)
print "Biggest outlier:", person_name, biggest_outlier

# How many people in the E+F dataset (as it currently exists) have "NaN" for their total payments? What percentage of
# people in the dataset as a whole is this?
no_total_payments = 0
for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN':
        no_total_payments += 1
print("Total payments NaN: " + str(no_total_payments))
print("Percentage of total payments NaN: " + str(no_total_payments*100/total_entry))

# How many POIs in the E+F dataset have "NaN" for their total payments? What percentage of POI's as a whole is this?
no_total_payments = 0
for person in enron_data:
    if enron_data[person]['poi'] == 1 and enron_data[person]['total_payments'] == 'NaN':
        no_total_payments += 1
print("Total payments NaN (POI): " + str(no_total_payments))
print("Percentage of total payments NaN (POI): " + str(no_total_payments*100/poi_count))

# What is the new number of people of the dataset? What is the new number of folks with NaN for total payments?