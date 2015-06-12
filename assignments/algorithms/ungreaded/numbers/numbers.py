
dat = []
file = open('data.txt')

    
lst = file.readlines()
##try:
##       for line in lst:
##              for s in line.split():
##                     dat.append(s)
##                     dat.sort(key=int)
##              print('min:',dat[0])
##              print('max:',dat[-1])
##              theSum = 0
##              for i in dat:
##                     theSum = theSum + int(i)
##              print('Average:',theSum/len(dat))
##except ValueError as error:
##        print('There are string in file this program accept only intergers')
##
##
##              


for line in lst:
       for s in line.split():
              dat.append(s)
ls = dat
for i in range(0, len(ls) - 1):
        pos = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[pos]:
                pos = j
        ls[pos], ls[i] = ls[i], ls[pos]
print(ls)
       
