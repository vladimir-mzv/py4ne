from matplotlib import pyplot
from openpyxl import load_workbook
wb = load_workbook('data_analysis_lab.xlsx')
def getvalue(x): return x.value
sheet = wb['Data']
years = list(map(getvalue, sheet['A'][1:]))
temp = list(map(getvalue, sheet['C'][1:]))
act = list(map(getvalue, sheet['D'][1:]))
pyplot.plot(years, temp, label="temperature")
pyplot.plot(years, act, label="activity")
# pyplot.plot(act, temp)
pyplot.show()