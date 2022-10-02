#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv


print("Starting parsing of CSV file with words...")

with open('words.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=';')
	line_count = 0

	file = open("output.txt","w")

	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			print(row[0], row[1], row[2], row[3])
			# Write in file
			file.write("[" + str(line_count) + "] = {" + "\n")
			file.write("[\"word_english\"] = \""+ str(row[0]) +"\"," + "\n")
			# file.write("[\"word_bulgarian\"] = \""+ str(row[1]) + "\"," + "\n")
			file.write("[\"word_description\"] = \"" + str(row[2]) + "\"," + "\n")
			file.write("[\"word_sentence\"] = \""+ str(row[3]) + "\"," + "\n")
			file.write("}," + "\n")

			line_count += 1

	file.close()
	print('Done.')
