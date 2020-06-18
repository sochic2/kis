import time
startTime = time.time()

# L = 45
# S = 35
# K = 55
# E = 50
# G = 25
# A = 30
# V = 40
dict = {'L':45, 'S':35, 'K':55, 'E':50, 'G':25, 'A':30, 'V':40}

f = open('spectrum.mgf')
BEGIN_IONS = f.readline()
TITLE = f.readline().split('=')[1]
PEPMASS = int(f.readline().split('=')[1])
CHARGE = f.readline().split('=')[1]


fragmentTolerance = 1
bin_size = int(PEPMASS/fragmentTolerance)+1
experimental = [0] * bin_size

while True:
    inputt = f.readline()
    if inputt == 'END IONS':break
    element = inputt.split()
    m_z, intensity = int(element[0]), int(element[1])
    index = int(m_z/fragmentTolerance)
    experimental[index] = intensity

print(experimental)

f.close()

f = open('database.fasta')
database = f.readlines()
peptides = []
for line in range(len(database)):
    # line = line.rstrip("\n")
    if database[line][0] == '>':continue
    peptide = database[line].rstrip("\n")
    # if '\n' in peptide:
    #     peptide = peptide.split('\n')[0]
    peptides.append(peptide)

print(peptides)
print()
f.close()

best_XCorr = 0
bestPeptide = ''
for peptide in peptides:
    theoretical = [0] * bin_size
    yion = 0
    bion = 0
    for word in peptide:
        yion += dict[word]

    for i in range(len(peptide)-1):
        bion += dict[peptide[i]]
        yion -= dict[peptide[i]]
        theoretical[int(bion/fragmentTolerance)] = 1
        theoretical[int(yion/fragmentTolerance)] = 1
        # print(bion, yion)
    # 계산하고 값의 평균을 빼줌?
    # XCorr 가장 높은 값, 가장 높은 점수를 가진 애 출력하기
    # tn시간의
    xcorr = 0
    average = 0
    tau = 74
    for o in range(len(experimental)):
        if theoretical[o]:
            xcorr += experimental[o] * theoretical[o]

    for o in range(len(experimental)):
        for c in range(o-tau, o+tau+1):
            if o-c == 0:continue
            if c >= len(experimental) or c < 1:continue
            average += experimental[o] * theoretical[c]


    # for t in range(-tau, tau+1):
    #     for b in range(bin_size):
    #         if((b+t)>=0) and ((b+t) < bin_size):
    #             average += experimental[b+t]*theoretical[b]

    average /= 2*tau

    xcorr -= average

    if xcorr > best_XCorr:
        best_XCorr = xcorr
        bestPeptide = peptide
    print(xcorr)
    #
    # print(theoretical)
print()
print(best_XCorr)
print(bestPeptide)