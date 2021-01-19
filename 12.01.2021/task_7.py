import json
profit = []
dif = 0
average = 0
firms_profit = {}
with open('ex_7.txt', 'r', encoding='utf-8') as ex_7:
    for line in ex_7:
        dif = int(line.split()[2]) - int(line.split()[3])
        if dif > 0:
            profit.append(dif)
            average += dif
            firms_profit.update({line.split()[0]: dif})
    average_profit = {'average profit': round((average / len(profit)), 2)}
data = [firms_profit, average_profit]
with open('firms_profit_data.json', 'w', encoding='utf-8') as firms_profit_data:
    json.dump(data, firms_profit_data)
