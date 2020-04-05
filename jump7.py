data = range(1,101)
for tmpData in data:
    if(tmpData % 7 ==0) or (tmpData % 10 == 7) or (tmpData // 10  == 7):
        continue
    else:
        print(tmpData)
