charge2s = open('charge2.txt')
charge3s = open('charge3.txt')
charge4s = open('charge4.txt')

charge2_sort = open('201909r.1.real.charge2.1%.txt', 'w')
charge3_sort = open('201909r.1.real.charge3.1%.txt', 'w')
charge4_sort = open('201909r.1.real.charge4.1%.txt', 'w')

sorted_charge2 = []


for line in charge2s:
    if line[0] == "C" or line[0] == "s":
        charge2_sort.write(line)

    else:
        sorted_charge2.append(line.split("\t"))

sorted_charge2 = sorted(sorted_charge2, key = lambda sortResult:int(sortResult[0]))
# charge2_sort.writelines(r_2)
# print(sorted_charge2[0])
# print(sorted_charge2[1])
# print(sorted_charge2[2])

result_charge2 = [sorted_charge2[0]]
for i in sorted_charge2:
    if i[0] == result_charge2[-1][0]:
        if float(i[5]) < float(result_charge2[-1][5]):
            result_charge2.pop()
            result_charge2.append(i)
    else:
        result_charge2.append(i)

# print(result_charge2[0])
# print(result_charge2[1])
# print(result_charge2[2])

result_charge2 = sorted(result_charge2, key = lambda result_charge2:float(result_charge2[5])) # lambda result_charge2 부분은 변수명, x : float(x[5])로 바꿀수 있음
# print(result_charge2[0])
# print(result_charge2[1])
# print(len(result_charge2))

total_tcount = 0
total_dcount = 0
e_value_threshold = 0
total_target = 0
print(result_charge2[3])
t_count_list = []
for line in result_charge2:
    flag = 0
    proteins = line[15].split(',')
    for protein in proteins:
        if protein[0:4] != 'XXX_':
            flag = 1
    if flag == 1:
        total_tcount += 1
        t_count_list.append("\t".join(line).rstrip("\t"))
    else:
        total_dcount += 1

    if total_tcount == 0 or total_dcount == 0:continue
    if total_dcount / total_tcount <= 0.01:
        e_value_threshold = float(line[5])
        total_target = total_tcount



print(total_tcount, total_dcount, e_value_threshold, total_target)
fdrResult = open('fdrResult.txt', 'w')

for i in t_count_list:
    fdrResult.write(i)
