
# This is a script to parse market and demographic data for residential solar customers.
#     The excel file used in this script can be found here:
#         https://www.newsolarhomes.org/WebPages/Public/Reports.aspx

import xlrd
import agate
book = xlrd.open_workbook('NSHP.xlsx')
sheet = book.sheet_by_name('NSHP')
data = [
[sheet.cell_value(r,c)]
for c in range(sheet.ncols)
for r in range(sheet.nrows)
]



# psuedocode:
# if zip code columne == 8888:
	# run mean function on col_values(colx,)
	# print and eventually write to notebook
