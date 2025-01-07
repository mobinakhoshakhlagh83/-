import pandas as pd
data=pd.read_csv('form_data.csv')
code_melli=input("lotfan kode melli ra vared konid:")
etelaat=data[data["kode melli"]==code_melli]
if not etelaat.empty:
    print(etelaat.to_string(index=False))
else:
    print("karbar yaft nashod")