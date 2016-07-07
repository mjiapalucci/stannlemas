import xlrd

file = xlrd.open_workbook('C:\Users\MJI\Dropbox\Yahoo! Mail\database_julyaug.xlsx')
worksheet = file.sheet_by_name('LREU Schedule')

date = raw_input('Enter the weekend as a text string e.g Sep 1/2: ')
#date = 'Jul 2/3'
month1_list = []
month2_list = []
column = []
email_servers = []

for i in range(1,6):
    month1_list.append(str((worksheet.row(1).pop(i)).value))
    month2_list.append(str((worksheet.row(19).pop(i)).value))
    column.append(i)

month1_column = dict(zip(month1_list, column))    
month2_column = dict(zip(month2_list, column))
monthall_column = month1_list + month2_list

get_column = month1_column.get(date)
if get_column != None:
    
    LR5 = str((worksheet.row(3).pop(get_column)).value)
    EU15 = str((worksheet.row(4).pop(get_column)).value)
    EU25 = str((worksheet.row(5).pop(get_column)).value)

else:
    get_column = month2_column.get(date)
    LR5 = str((worksheet.row(21).pop(get_column)).value)
    EU15 = str((worksheet.row(22).pop(get_column)).value)
    EU25 = str((worksheet.row(23).pop(get_column)).value)    


    
'''
LR = str((worksheet.row(3).pop(1)).value)
EU1 = str((worksheet.row(4).pop(1)).value)
EU2 = str((worksheet.row(5).pop(1)).value)
'''
LREU = LR5, EU15, EU25

#print LR, EU1, EU2

print month1_column.keys(), month2_column
print column
print LREU
print monthall_column
