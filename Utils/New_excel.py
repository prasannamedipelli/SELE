from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
sheet["A1"] = "name"
sheet["B1"] = "role"  
wb.save("sample.xlsx")