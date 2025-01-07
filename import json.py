import json
from openpyxl import Workbook
def load_customer_data(json_file):
  try:
    with open(json_file,'r',encoding='utf-8') as file:
      return json.load(file)
  except Exception as e:
    print("khata dar khandane JSON:",e)
    return None
def export_to_excel(customers,output_file):
  try:
    workbook=Workbook()
    sheet=workbook.active
    sheet.title="shomare moshtarian"
    sheet.append(["num","shomare telfon"])
    for customer in customers:
        sheet.append([customer.get("name","namoshakhas"),customer.get("phone","namoshakhas")])
    workbook.save(output_file)
    print(f"file Excel ba movafagiiat zakhire shod{output_file}")
  except Exception as e:
    print("khata dar zakhire Excel",e)
if name=="main":
  json_file="customers.json" 
  output_file="customer_phone_list.xlsx"
  customer_data=load_customer_data(json_file)
  if customer_data:
    export_to_excel(customer_data,output_file)