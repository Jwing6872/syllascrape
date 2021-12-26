import pdfplumber
import pandas as pd

path = 'ec10a_syllabus.pdf'
with pdfplumber.open(path) as pdf:
    print(pdf.pages[6].extract_text())
    table1 = pdf.pages[13].extract_table()
    table2 = pdf.pages[14].extract_table()
    table3 = pdf.pages[15].extract_table()

    df1 = pd.DataFrame(table1[1:], columns=table1[0])
    df2 = pd.DataFrame(table2[1:], columns=table2[0])
    df3 = pd.DataFrame(table3[1:], columns=table3[0])
##    for column in ["Effective", "Received"]:
##        df[column] = df[column].str.replace(" ", "")
    print(df1)
    print("")
    print(df2)
    print("")
    print(df3)
