from openpyxl import load_workbook
wb = load_workbook('Untitled.xlsx')
def getvalue(x): return x.value
sheet = wb['Sheet1']
name = list(map(getvalue, sheet['A'][1:]))
age = list(map(getvalue, sheet['C'][1:]))
#act = list(map(getvalue, sheet['D'][1:]))
#pyplot.plot(years, temp, label="temperature")
#pyplot.plot(years, act, label="activity")
# pyplot.plot(act, temp)
#pyplot.show()
#print(years)
#pyplot.show()
print(name[1])
print(age[2])