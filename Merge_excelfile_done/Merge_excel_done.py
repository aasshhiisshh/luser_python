
# Import the function
import xlsxwriter

# make one excel file.
workbook = xlsxwriter.Workbook('studentsdetails.xlsx')
worksheet = workbook.add_worksheet();

worksheet.write('A1','Name')
worksheet.write('B1','Phone')
worksheet.write('C1','dept')
worksheet.write('D1','grade')

# make database here
data = ([''' you can put it according you.'''])

row=1
col=0

for Name,Phone,dept,grade in data:
    worksheet.write(row,col,Name)
    worksheet.write(row,col+1,Phone)
    worksheet.write(row,col+2,dept)
    worksheet.write(row,col+3,grade)
    row+=1

# make sure everytime you have to close this file.
workbook.close()
