# factors: 
# time for library to set up
# score of books in library
# number of books
# no of parallel books that can be scanned
# no of unique books

f = open('e_so_many_books.txt','r')

books,libs,days = [int(i) for i in f.readline().split()]

bscore = [int(i) for i in f.readline().split()]

ldesc = []
lb = []

for i in range(libs):
	ldesc.append([int(j) for j in f.readline().split()]+[i])
	lb.append([int(j) for j in f.readline().split()])

sorter = [-i[0]*0.8+i[1]*600-i[2]*600 for i in ldesc]
sorter2 = sorter[:]
p = list(zip(sorter,lb))
p.sort(key=lambda x: x[0])
#p = p[::-1]
lb = [j for i,j in p]

p = list(zip(sorter2,ldesc))
p.sort(key=lambda x: x[0])
#p = p[::-1]
ldesc = [j for i,j in p]

o = open('e_sol.txt','w')

o.write(str(libs)+'\n')

for i in range(libs):
	o.write(str(ldesc[i][-1])+' '+str(ldesc[i][0])+'\n')
	o.write(' '.join([str(j) for j in lb[i]])+'\n')


