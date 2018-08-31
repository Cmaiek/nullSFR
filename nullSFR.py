import xlrd
import xml.etree.ElementTree as ET

workbook = xlrd.open_workbook('OTLA1.xlsx')

sheet = workbook.sheet_by_index(0)
lp = sheet.col_values(0)

for wiersz in lp:
    r = int(wiersz)
    NIPx = str(sheet.cell(r, 2).value).split(".")[0]
    nazwax = sheet.cell(r, 1).value

    tree = ET.parse('OTLA_1_null.xml')
    root = tree.getroot()

    elemNIP = tree.findall('.//{http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}NIP')

    for elem in elemNIP:
        elem.text = str(NIPx)

    elemName = tree.findall('.//{http://jpk.mf.gov.pl/wzor/2017/11/13/1113/}PelnaNazwa')

    for elemn in elemName:
        elemn.text = str(nazwax)
    if r < 9:
        filenum = str(0)+str(r+1)
    else:
        filenum = str(r+1)
    tree.write(filenum+'_VAT_201806_'+NIPx+'.xml')

    if wiersz > max(lp):
        break