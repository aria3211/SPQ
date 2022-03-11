


"""Question from: https://quera.ir/problemset/3107/ """

size_sarshoneh_ghad = input("Enter a size of T-shirt:").split()
shonehsize = range(int(size_sarshoneh_ghad[0])+1)
hight = range(int(size_sarshoneh_ghad[1])+1)



sizewinner = input("Enter a size of T-shirt:").split()
shonehsize1 = int(sizewinner[0])
hight1 = int(sizewinner[1])


result = []
for i in shonehsize:
    if shonehsize1 in shonehsize:
        result.append('yes')
        break
    else:
        result.append('no')
        break
for i in hight:
    if hight1 in hight:
        result.append('yes')
        break
    else:
        result.append('no')
        break



if __name__ == '__main__':
    counter = 0
    for i in result:
        if i == 'yes':
            counter += 1
        else:
            counter = 0
    if counter == 2:
        print('yes')
    else:
        print('no')
