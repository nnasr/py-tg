"""
This file uses an imported .xlsx or .csv file to generate any
number of occurrences for any type of drug (EN accepted language)
"""
import re
import xlsxwriter
import pandas as pd
#from pd import read_excel

def algorithm():
    """
    This reads the imported file, runs it through the algorithm,
    and outputs the generated results in a .xlsx file
    """
    occurrence_column = int(input(
        'Enter the column you are interested in generating occurrences from: '
        )) # used only when processing a .xlsx file

    number_of_words = int(input('Enter the number of words you are interested ' +
                                'in finding occurrences for: '))

    number_of_occurrences = int(input('Enter the number of occurrences you are interested ' +
                                      'in finding (ex: co-occurrence, tri-occurrence, etc..): '))

    bag_of_words = []  # create empty list

    for i in range(0, number_of_words):  # TBD on range -> alternative is number_of_words
        bow_contents = str(input('Please enter a word of interest: '))
        # prompt user for words in bag of words
        bag_of_words.append(bow_contents)  # append to our_list

    # specific to JC county example- user specs alter id
    # print(bag_of_words)
    #target_col = [occurrence_column]
    data_set = pd.read_excel('Simple1.xlsx', na_values="null",
                             sheet_names='JeffCoDataSimple.xlsx', usecols=occurrence_column)
    data_frame = pd.DataFrame(data_set)
    total_rows = len(data_frame)  # altering file to user input

    med_dict = pd.read_excel('DrugNames.xlsx', na_values="null", sheet_names='DrugNames.xlsx')
    # print(med_dict)
    #med_dict_dataframe = pd.DataFrame(med_dict)
    med_dict_array = med_dict.values
    # print(mdf[7616])
    # print(mddf['DrugNames'][3])
    # c = len(mddf)
    # loop to iterate *through* the row
    for row in data_frame.items():
        for i in range(0, total_rows):
            tri_guys = []
            med_dict_count = 0
            bow_check = False
            data_lowercase = str(data_frame['CauseDeath'][i]).lower()
            data_stripped = [c.strip() for c in re.split(r'(\W+)',
                                                         data_lowercase) if c.strip() != '']
            for current_word in data_stripped:
                if current_word in bag_of_words:
                    bow_check = True
                if current_word in med_dict_array:
                    med_dict_count += 1
                    # print(bow_check, med_dict_count, y, d)
                    # use above for testing each component for bugs
            if med_dict_count > number_of_occurrences and bow_check is True:
                tri_guys = tri_guys + [data_lowercase]
                # print(triGuys)
                med_dict_count = 0

    workbook = xlsxwriter.Workbook('Occurrences.xlsx')
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'List of Occurrences', bold)

    list_occurrences = tri_guys
    row = 1
    col = 0

    for cause_death in list_occurrences:
        worksheet.write(row, col, cause_death)
        row += 1

    workbook.close()

algorithm()
