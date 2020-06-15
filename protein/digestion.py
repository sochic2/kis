f = open('protein','r')
proteins = f.readlines()
for protein in proteins:
    cnt = 0
    store = ''
    for i in protein:
        store += i
        if i == 'R' or i == 'K':
            print(store)
            store = ''
            cnt += 1


    print(cnt,'개입니다.')
    print()