#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 01: Reading a CSV
    Task 02: """

import csv
import json

GRADES = {
    'A': float(1.0),
    'B': float(0.9),
    'C': float(0.8),
    'D': float(0.7),
    'F': float(0.6)
    }


def get_score_summary(boro_file):
    """score summary dictionary"""

    boro_dict = {}

    input_file = csv.reader(open(boro_file, "r"),
                            delimiter=',')

    for line in input_file:
        camis = line[0]
        boro = line[1]
        grade = line[10]
        if camis not in boro_dict:
            if grade != '' or 'P':
                boro_dict[camis] = (boro, grade)

    input_file.close()

    boro_score = {}
    manhattan_sum = 0
    manhattan_avg = 0
    brooklyn_sum = 0
    brooklyn_avg = 0
    bronx_sum = 0
    bronx_avg = 0
    queens_sum = 0
    queens_avg = 0
    staten_island_sum = 0
    staten_island_avg = 0

    for key, value in boro_dict.iteritems():
        if value = 'MANHATTAN':
            manhattan_sum += 1
            manhattan_avg += grade
        if value = 'BROOKLYN':
            brooklyn_sum += 1
            brooklyn_avg += grade
        if value = 'BRONX':
            bronx_sum += 1
            bronx_avg += grade
        if value = 'STATEN ISLAND':
            staten_island_sum += 1
            staten_island_avg += grade
        if value = 'QUEENS':
            queens_sum += 1
            queens_avg += grade


def get_market_density(filename):
    """market density"""



# if __name__ == "__main__":
#     TEST = get_score_summary("inspection_results.csv")
#     print TEST