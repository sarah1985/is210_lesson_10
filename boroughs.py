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
    manhattan_count = 0
    manhattan_avg = 0
    brooklyn_count = 0
    brooklyn_avg = 0
    bronx_count = 0
    bronx_avg = 0
    queens_count = 0
    queens_avg = 0
    staten_island_count = 0
    staten_island_avg = 0

    for key, value in boro_dict.iteritems():
        if 'MANHATTAN' in value:
            manhattan_count += 1
            manhattan_score = GRADES[value[1]]
            manhattan_avg += manhattan_score
            boro_score['MANHATTAN'] = \
                (manhattan_count, manhattan_avg/manhattan_count)
        if 'BROOKLYN' in value:
            brooklyn_count += 1
            brooklyn_score = GRADES[value[1]]
            brooklyn_avg += brooklyn_score
            boro_score['BROOKLYN'] = \
                (brooklyn_count, brooklyn_avg/brooklyn_count)
        if 'BRONX' in value:
            bronx_count += 1
            bronx_score = GRADES[value[1]]
            bronx_avg += bronx_score
            boro_score['BRONX'] = (bronx_count, bronx_avg/bronx_count)
        if 'STATEN ISLAND' in value:
            staten_island_count += 1
            staten_island_score = GRADES[value[1]]
            staten_island_avg += staten_island_score
            boro_score['STATEN ISLAND'] = \
                (staten_island_count, staten_island_avg/staten_island_count)
        if 'QUEENS' in value:
            queens_count += 1
            queens_score = GRADES[value[1]]
            queens_avg += queens_score
            boro_score['QUEENS'] = (queens_count, queens_avg/queens_count)

    return boro_score
    

def get_market_density(filename):
    """market density"""



# if __name__ == "__main__":
#     TEST = get_score_summary("inspection_results.csv")
#     print TEST