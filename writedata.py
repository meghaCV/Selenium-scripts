import openpyxl

path = "/Users/chandrashekarbasavaraj/Downloads/Writedata.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active


for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value = "welcome"

workbook.save(path)