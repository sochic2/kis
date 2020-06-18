f = open('201909r.1.real.txt')
charge2 = open('charge2.txt', 'w')
charge3 = open('charge3.txt', 'w')
charge4 = open('charge4.txt', 'w')


datas = f.readlines()
for data in datas:
    if not data[0].isdecimal():
        charge2.write(data)
        charge3.write(data)
        charge4.write(data)
    else:
        split_data = data.split()
        if split_data[1] == '1':
            if split_data[2] == '2':
                charge2.write(data)
            elif split_data[2] == '3':
                charge3.write(data)
            elif split_data[2] >= '4':
                charge4.write(data)

charge2.close()
charge3.close()
charge4.close()

