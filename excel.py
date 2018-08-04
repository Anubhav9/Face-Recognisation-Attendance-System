import xlwt
from xlwt import Workbook
import datetime

date=datetime.datetime.now().date()
time=datetime.datetime.now().time()
wb=Workbook()
sheet=wb.add_sheet("Attendance System")
sheet.write(0,0,str(time))
sheet.write(0,1,str(date))
sheet.write(1,0,"Name")
sheet.write(1,1,"Attendence")
wb.save("Attendace Reports.xlsx")

