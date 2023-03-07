import xlrd

data = xlrd.open_workbook("horse_name.xls")

source_table = data.sheet_by_index(0)
clean_data = set()
for val in source_table.col_values(0):
    temp = "nmd"
    if "、" in val:
        temp = str(val).split("、")[1]
    if ". " in val:
        temp = str(val).split(". ")[1]

    print(temp)
    clean_data.add(temp)
print(clean_data)
print(len(clean_data))



