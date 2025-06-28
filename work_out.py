one_rep_max = {}
bench = {}
squad = {}
deadlift = {}
date = ""
b = False
s = False
d = False
with open("筋トレ記録.txt", encoding='utf-8-sig') as f:
    for i in range(5):
        line = f.readline().split(" ")
        if line[0].strip()!="最高重量":
            ex_type = line[0].strip()
            weight = line[1].strip()
            one_rep_max[ex_type] = weight[:-2]
    lines = f.readlines()
    lines = map(str.strip, lines)
    lines = list(lines)

    for line in lines:
        if "月" in line and "日" in line:
            line = line.split("月")
            month = line[0]
            day = line[1][:-1]
            date = day + "/" + month
        elif line=="ベンチプレス":
            b = True
        elif b:
            print(line)
            weight, rep = line.split(" ")
            bench[date] = tuple([weight[:-2], rep[:-1]])
            b = False
        elif line=="デッドリフト" or line == "デットリフト":
            d = True
        elif d:
            #print(line)
            weight, rep = line.split(" ")
            deadlift[date] = tuple([weight[:-2], rep[:-1]])
            d = False
        elif line=="スクワット":
            s = True
        elif s:
            weight, rep = line.split(" ")
            squad[date] = tuple([weight[:-2], rep[:-1]])
            s = False
            
print(one_rep_max)
print(squad)
print(deadlift)
print(bench)