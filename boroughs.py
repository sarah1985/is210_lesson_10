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
            if grade is None:
                pass
            elif grade == 'P':
                pass
            else:
                boro_dict[camis] = [boro, grade]

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

    for value in boro_dict.itervalues():
        if 'MANHATTAN' in value:
            manhattan_count += 1
            manhattan_score = GRADES[value[1]]
            manhattan_avg += manhattan_score
        if 'BROOKLYN' in value:
            brooklyn_count += 1
            brooklyn_score = GRADES[value[1]]
            brooklyn_avg += brooklyn_score
        if 'BRONX' in value:
            bronx_count += 1
            bronx_score = GRADES[value[1]]
            bronx_avg += bronx_score
        if 'STATEN ISLAND' in value:
            staten_island_count += 1
            staten_island_score = GRADES[value[1]]
            staten_island_avg += staten_island_score
        if 'QUEENS' in value:
            queens_count += 1
            queens_score = GRADES[value[1]]
            queens_avg += queens_score

    boro_score = {
        'MANHATTAN': (manhattan_count, manhattan_avg/manhattan_count),
        'BROOKLYN': (brooklyn_count, brooklyn_avg/brooklyn_count),
        'BRONX': (bronx_count, bronx_avg/bronx_count),
        'STATEN ISLAND': (
            staten_island_count, staten_island_avg/staten_island_count),
        'QUEENS': (queens_count, queens_avg/queens_count)
    }
    return boro_score


def get_market_density(filename):
    """market density"""

    input_file = open(filename, 'r')
    j_son = json.load(input_file)

    manhattan_count = 0
    brooklyn_count = 0
    bronx_count = 0
    queens_count = 0
    staten_island_count = 0

    for line in j_son['data']:
        if line[8] == 'Manhattan':
            manhattan_count += 1
        elif line[8] == 'Brooklyn':
            brooklyn_count += 1
        elif line[8] == 'Bronx':
            bronx_count += 1
        elif line[8] == 'Queens':
            queens_count += 1
        elif line[8] == 'Staten Island':
            staten_island_count += 1

    green_market_dict = {
        'MANHATTAN': manhattan_count,
        'BROOKLYN': brooklyn_count,
        'BRONX': bronx_count,
        'QUEENS': queens_count,
        'STATEN ISLAND': staten_island_count
    }
    return green_market_dict


def correlate_data(rest_file, filename, file_output):
    """correlate data"""

    rest_scores = get_score_summary(rest_file)
    green_density = get_market_density(filename)
    man_compare = float(green_density['MANHATTAN'])/rest_scores['Manhattan']
    brook_compare = float(green_density['BROOKLYN'])/rest_scores['Brooklyn']
    bronx_compare = float(green_density['BRONX'])/rest_scores['Bronx']
    queens_compare = float(green_density['QUEENS'])/rest_scores['Queens']
    si_compare = float(green_density['STATEN ISLAND'])/rest_scores['Staten Island']

    boro_dict = {
        'MANHATTAN': (rest_scores['Manhattan'][1], man_compare),
        'BROOKLYN': (rest_scores['Brooklyn'][1]), brook_compare),
        'BRONX': (rest_scores['Bronx'][1]), bronx_compare),
        'QUEENS': (rest_scores['Queens'][1]), queens_compare),
        'STATEN ISLAND': (rest_scores['Staten Island'[1]], si_compare)
    }

    out_file = open(file_output, 'w')
    json.dump(boro_dict, out_file)
    out_file.close()

    return boro_dict

# if __name__ == "__main__":
#     TEST = get_score_summary("inspection_results.csv")
#     print TEST