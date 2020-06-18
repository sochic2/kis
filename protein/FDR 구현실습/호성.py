# FDR 구현 2

f22 = open('charge2.txt')


data22 = f22.readlines()
# print(data22[:5])


# dataset = [data22, data33, data44]

f222 = open('201909r.1.real.charge2.1%.txt', 'w')


# check =
# print(str(data22[2:3]))
# print(strdata22[2:3].split())

# for i in range(len(dataset)):
#     for j in range(i, 3):
#         print(dataset[i])
#         if j <= 1:
#             f222.write(dataset[j])
#             f333.write(dataset[j])
#             f444.write(dataset[j])

#         else:

# print(data22)


sortResult = []
for line in data22:
    #     print(line)
    if line[0] == 'C' or line[0] == 's':
        f222.write(line)
    else:
        sortResult.append(line.split("\t"))

sortResult = sorted(sortResult, key=lambda sortResult: int(sortResult[0]))

del_sortResult = [sortResult[0]]
for i in range(1, len(sortResult)):
    if del_sortResult[len(del_sortResult) - 1][0] == sortResult[i][0]:
        if float(del_sortResult[len(del_sortResult) - 1][5]) > float(sortResult[i][5]):
            del_sortResult[len(del_sortResult) - 1] = sortResult[i]
    else:
        del_sortResult.append(sortResult[i])

# print(len(del_sortResult))

del_sortResult = sorted(del_sortResult, key = lambda x:float(x[5]))
# target & decoy count
fdr = 0
max_fdr = 0
tcount = 0
dcount = 0
e_value_threshold = 0
total_target = 0

# protein index = 15

for i in range(len(del_sortResult)):
    # for i in range(5):
    protein = del_sortResult[i][15].split(',')
    flag = 0

    for j in range(len(protein)):
        if protein[j].startswith('XXX_'):
            continue
        else:
            flag = 1

    if flag:
        tcount += 1
    else:
        dcount += 1

    #     print(protein, tcount, dcount)

    if tcount == 0 or dcount == 0: continue
    if dcount / tcount <= 0.01:
        e_value_threshold = float(del_sortResult[i][5])
        total_target = tcount




print('total tcount = {}'.format(tcount))
print('total dcount = {}'.format(dcount))
print('e-value threshold = {}'.format(e_value_threshold))
print('total target : {}'.format(total_target))

f22.close()

f222.close()
