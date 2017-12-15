
# This is a script to parse market and demographic data for residential solar customers.
#     The excel file used in this script can be found here:
#         https://www.newsolarhomes.org/WebPages/Public/Reports.aspx

import xlrd

book = xlrd.open_workbook('NSHP.xlsx')
sheet = book.sheet_by_name('NSHP')
count = 0
data = {}
for i in range(sheet.nrows):
	if count < 10:
		if i >= 14:
			row = sheet.row_values(i)
			zip = row[2]
	print sheet.row_values(i) 