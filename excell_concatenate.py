import pandas as pd

excel_files = ["xlsx1.xlsx", "xlsx2.xlsx"]

excels = [pd.ExcelFile(name) for name in excel_files]

dataframes = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

dataframes[1:] = [df[1:] for df in dataframes[1:]]

combined = pd.concat(dataframes)

combined.to_excel("concatenated.xlsx", header=False, index=False)
