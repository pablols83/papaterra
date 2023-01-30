import os
import pandas as pd

def find_line(search_string):
    # setting 'found' flag and line index position to 0
    flag = 0
    index = 0

    # creates an empty list for string row positions
    string_pos_list = []

    # loop through the file line by line
    for line in file1:
        index = index + 1

        # check if string is present in line or not, and then append to position list and set flag to 1
        if search_string in line:
            string_pos_list.append(index)
            line_content = line
            flag = 1

    # return the string, the flag and line position list
    return search_string, flag, string_pos_list, line_content

folder = "D:\Python\Papa-Terra\Wells"
filelist = []
well_table_df = pd.DataFrame()


for count, filename in enumerate(os.listdir(folder)):
    filelist.append(filename)
    # combine folder path with file name and open text file
    filepath = folder + r'\\' + filename
    file1 = open(filepath, "r")

    string_well_start = 'WELL NAME:'
    file1.seek(0)
    line_name_start = find_line(string_well_start)
    name = line_name_start[3][line_name_start[3].find(':')+1:]
    name = name.strip()

    string_line_x_start = 'WELL HEAD X-COORDINATE:'
    file1.seek(0)
    line_x_start = find_line(string_line_x_start)
    x = line_x_start[3][line_x_start[3].find(':')+1:]
    x = x.strip()

    string_line_y_start = 'WELL HEAD Y-COORDINATE:'
    file1.seek(0)
    line_y_start = find_line(string_line_y_start)
    y = line_y_start[3][line_y_start[3].find(':')+1:]
    y = y.strip()

    string_line_kb_start = 'WELL DATUM (KB, Kelly bushing, from MSL):'
    file1.seek(0)
    line_kb_start = find_line(string_line_kb_start)
    kb = line_kb_start[3][line_kb_start[3].find(':')+1:]
    kb = kb.strip()

    list = [name, x, y, kb]
    df_temp = pd.DataFrame(list)
    series = pd.Series(list)
    well_table_df = pd.concat([well_table_df, df_temp], axis=1)


well_table_df = pd.DataFrame.transpose(well_table_df)
pd.DataFrame.to_clipboard(well_table_df)

print(well_table_df)