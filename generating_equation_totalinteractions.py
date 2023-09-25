import pandas as pd

def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count

def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

#lattconst = float(input("Enter the value of Scaling constant (lattice_constant/1.414):"))
lattconst = 2.95217081000000
#cryst = input("Enter the crystal type (100 or 111): ")
cryst = "100"

if cryst == "111":
	coord = pd.read_csv("/mnt/c/users/dmpatel/OneDrive - Iowa State University/desktop/research_data/General Script/Fermi_Development/config1.csv", sep = '  ', usecols = [0,1], names = ["x", "y"])
	print(coord)
	x = coord.x.to_list()
	y = coord.y.to_list()
	coord = []
	for i in range(len(x)):	##Creating and saving periodic images of a slab repeated by 3x3##										
		x[i] = x[i]*lattconst*4+y[i]*2*lattconst
		y[i] = y[i]*lattconst*3.46410161
		coord.append([x[i]+6*lattconst,y[i]+3.46410161*lattconst])
		coord.append([x[i]+10*lattconst,y[i]+3.46410161*lattconst])
		coord.append([x[i]+lattconst*2,y[i]+3.46410161*lattconst])
		coord.append([x[i]+4*lattconst,y[i]])
		coord.append([x[i]+8*lattconst,y[i]+2*3.46410161*lattconst])
		coord.append([x[i],y[i]])
		coord.append([x[i]+8*lattconst,y[i]])
		coord.append([x[i]+12*lattconst,y[i]+2*3.46410161*lattconst])
		coord.append([x[i]+4*lattconst,y[i]+2*3.46410161*lattconst])
		
	#print(coord)
	##Coefficients of correspinding NN parameters##
	a_final = []
	n = int(input("Enter the number of adsorbates:"))
	coord_count = []
	coord_surr = []
	for i in range(0,9*n-8,9):
		coord_surr_current = []
		f = 0
		nn = 0
		a = [0]*6
		for j in range(0,9*n-8,9):										
			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
				if search(coord_count,coord[j]):					##If you found the already counted NN, then empty the first element##
					#print(nn,f)
					if nn != 0 and nn != f:
						a[f] = 0
						a[nn] = a[nn] + 1
						f = f + 1
						nn = nn + 1
					else:
						a[f] = 0
						f = f + 1
						nn = nn + 1
				else:	
					coord_surr_current.append(coord[j])
					coord_surr_current.append(coord[j+1])
					coord_surr_current.append(coord[j+2])
					coord_surr_current.append(coord[j+3])
					coord_surr_current.append(coord[j+4])
					coord_surr_current.append(coord[j+5])
					coord_surr_current.append(coord[j+6])
					coord_surr_current.append(coord[j+7])
					coord_surr_current.append(coord[j+8])
					coord_surr.append(coord[j])
					coord_surr.append(coord[j+1])
					coord_surr.append(coord[j+2])
					coord_surr.append(coord[j+3])
					coord_surr.append(coord[j+4])
					coord_surr.append(coord[j+5])
					coord_surr.append(coord[j+6])
					coord_surr.append(coord[j+7])
					coord_surr.append(coord[j+8])
					#print(nn)
					a[nn] = a[nn] + 1
					nn = nn + 1

		for k in range(0,len(coord_surr_current),9):					##Taking into account the bond formation of NN##
			if search(coord_surr,coord_surr_current[k]):			##If this condition is True##
				b = countX(coord_surr,coord_surr_current[k]) 		##Counting the number of previous repetition##
				if b > 0:
					a[b-1] = a[b-1] + 1
				else:
					continue

		coord_count.append(coord[i])
		coord_count.append(coord[i+1])
		coord_count.append(coord[i+2])
		coord_count.append(coord[i+3])
		coord_count.append(coord[i+4])
		coord_count.append(coord[i+5])
		coord_count.append(coord[i+6])
		coord_count.append(coord[i+7])
		coord_count.append(coord[i+8])
		a_final.append(a)

	print(a_final)
	a1 = 0
	a2 = 0
	a2 = 0
	a3 = 0
	a4 = 0
	a5 = 0
	a6 = 0

	for i in range(len(a_final)):
		a1 = a1 + a_final[i][0]
		a2 = a2 + a_final[i][1]
		a3 = a3 + a_final[i][2]
		a4 = a4 + a_final[i][3]
		a5 = a5 + a_final[i][4]
		a6 = a6 + a_final[i][5]

	print("a1 =",a1)
	print("a2 =",a2)
	print("a3 =",a3)
	print("a4 =",a4)
	print("a5 =",a5)
	print("a6 =",a6)


	##Coefficients of correspinding secNN parameters##
	a_final = []
	coord_count = []
	coord_surr = []
	i = 0
	k = 0
	b = 0
	for i in range(0,9*n-8,9):
		coord_surr_current = []
		f = 0
		nn = 0
		a = [0]*6
		for j in range(0,9*n-8,9):										
			if lattconst+0.008 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= 1.78*lattconst or lattconst+0.008 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= 1.78*lattconst or lattconst+0.008 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= 1.78*lattconst or lattconst+0.008 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= 1.78*lattconst or lattconst+0.008 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= 1.78*lattconst or lattconst+0.008 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= 1.78*lattconst or lattconst+0.008 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= 1.78*lattconst or lattconst+0.008 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= 1.78*lattconst or lattconst+0.008 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= 1.78*lattconst:		##The cut-off will change for each new metal##
				if search(coord_count,coord[j]):					##If you found the already counted NN, then empty the first element##
					#print(nn,f)
					if nn != 0 and nn != f:
						a[f] = 0
						a[nn] = a[nn] + 1
						f = f + 1
						nn = nn + 1
					else:
						a[f] = 0
						f = f + 1
						nn = nn + 1
				else:	
					coord_surr_current.append(coord[j])
					coord_surr_current.append(coord[j+1])
					coord_surr_current.append(coord[j+2])
					coord_surr_current.append(coord[j+3])
					coord_surr_current.append(coord[j+4])
					coord_surr_current.append(coord[j+5])
					coord_surr_current.append(coord[j+6])
					coord_surr_current.append(coord[j+7])
					coord_surr_current.append(coord[j+8])
					coord_surr.append(coord[j])
					coord_surr.append(coord[j+1])
					coord_surr.append(coord[j+2])
					coord_surr.append(coord[j+3])
					coord_surr.append(coord[j+4])
					coord_surr.append(coord[j+5])
					coord_surr.append(coord[j+6])
					coord_surr.append(coord[j+7])
					coord_surr.append(coord[j+8])
					#print(nn)
					a[nn] = a[nn] + 1
					nn = nn + 1

		for k in range(0,len(coord_surr_current),9):					##Taking into account the bond formation of NN##
			if search(coord_surr,coord_surr_current[k]):			##If this condition is True##
				b = countX(coord_surr,coord_surr_current[k]) 		##Counting the number of previous repetition##
				if b > 0:
					a[b-1] = a[b-1] + 1
				else:
					continue

		coord_count.append(coord[i])
		coord_count.append(coord[i+1])
		coord_count.append(coord[i+2])
		coord_count.append(coord[i+3])
		coord_count.append(coord[i+4])
		coord_count.append(coord[i+5])
		coord_count.append(coord[i+6])
		coord_count.append(coord[i+7])
		coord_count.append(coord[i+8])
		a_final.append(a)

	print(a_final)
	a1 = 0
	a2 = 0
	a2 = 0
	a3 = 0
	a4 = 0
	a5 = 0
	a6 = 0

	for i in range(len(a_final)):
		a1 = a1 + a_final[i][0]
		a2 = a2 + a_final[i][1]
		a3 = a3 + a_final[i][2]
		a4 = a4 + a_final[i][3]
		a5 = a5 + a_final[i][4]
		a6 = a6 + a_final[i][5]

	print("a11 =",a1)
	print("a22 =",a2)
	print("a33 =",a3)
	print("a44 =",a4)
	print("a55 =",a5)
	print("a66 =",a6)


elif cryst == "100":
	coord = pd.read_csv("/mnt/c/users/dmpatel/OneDrive - Iowa State University/desktop/research_data/General Script/Fermi_Development/config1.csv", sep = '  ', usecols = [0,1], names = ["x", "y"])
	print(coord)
	x = coord.x.to_list()
	y = coord.y.to_list()
	coord = []
	#print(x,y)
	for i in range(len(x)):	##Creating and saving periodic images of a slab repeated by 3x3##										
		x[i] = x[i]*4*lattconst
		y[i] = y[i]*4*lattconst
		coord.append([x[i]+4*lattconst,y[i]+4*lattconst])
		coord.append([x[i]+8*lattconst,y[i]+4*lattconst])
		coord.append([x[i],y[i]+4*lattconst])
		coord.append([x[i]+4*lattconst,y[i]])
		coord.append([x[i]+4*lattconst,y[i]+2*4*lattconst])
		coord.append([x[i],y[i]])
		coord.append([x[i]+8*lattconst,y[i]])
		coord.append([x[i]+8*lattconst,y[i]+2*4*lattconst])
		coord.append([x[i],y[i]+2*4*lattconst])
		
	#print(coord)
	##Coefficients of correspinding NN parameters##
	a_final = []
	n = int(input("Enter the number of adsorbates:"))
	coord_count = []
	coord_surr = []
	for i in range(0,9*n-8,9):
		coord_surr_current = []
		f = 0
		nn = 0
		a = [0]*4
		print(i)
		for j in range(0,9*n-8,9):										
			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
				if search(coord_count,coord[j]):					##If you found the already counted NN, then empty the first element##
					#print(nn,f)
					if nn != 0 and nn != f:
						a[f] = 0
						a[nn] = a[nn] + 1
						f = f + 1
						nn = nn + 1
					else:
						a[f] = 0
						f = f + 1
						nn = nn + 1
				else:	
					coord_surr_current.append(coord[j])
					coord_surr_current.append(coord[j+1])
					coord_surr_current.append(coord[j+2])
					coord_surr_current.append(coord[j+3])
					coord_surr_current.append(coord[j+4])
					coord_surr_current.append(coord[j+5])
					coord_surr_current.append(coord[j+6])
					coord_surr_current.append(coord[j+7])
					coord_surr_current.append(coord[j+8])
					coord_surr.append(coord[j])
					coord_surr.append(coord[j+1])
					coord_surr.append(coord[j+2])
					coord_surr.append(coord[j+3])
					coord_surr.append(coord[j+4])
					coord_surr.append(coord[j+5])
					coord_surr.append(coord[j+6])
					coord_surr.append(coord[j+7])
					coord_surr.append(coord[j+8])
					#print(nn)
					a[nn] = a[nn] + 1
					nn = nn + 1

		for k in range(0,len(coord_surr_current),9):					##Taking into account the bond formation of NN##
			if search(coord_surr,coord_surr_current[k]):			##If this condition is True##
				b = countX(coord_surr,coord_surr_current[k]) 		##Counting the number of previous repetition##
				if b > 0:
					a[b-1] = a[b-1] + 1
				else:
					continue
			else:
				continue

		coord_count.append(coord[i])
		coord_count.append(coord[i+1])
		coord_count.append(coord[i+2])
		coord_count.append(coord[i+3])
		coord_count.append(coord[i+4])
		coord_count.append(coord[i+5])
		coord_count.append(coord[i+6])
		coord_count.append(coord[i+7])
		coord_count.append(coord[i+8])
		a_final.append(a)

	print(a_final)
	a1 = 0
	a2 = 0
	a2 = 0
	a3 = 0
	a4 = 0

	for i in range(len(a_final)):
		a1 = a1 + a_final[i][0]
		a2 = a2 + a_final[i][1]
		a3 = a3 + a_final[i][2]
		a4 = a4 + a_final[i][3]


	print("a1 =",a1)
	print("a2 =",a2)
	print("a3 =",a3)
	print("a4 =",a4)


	##Coefficients of correspinding secNN parameters##
	a_final = []
	coord_count = []
	coord_surr = []
	i = 0
	k = 0
	b = 0
	for i in range(0,9*n-8,9):
		coord_surr_current = []
		f = 0
		nn = 0
		a = [0]*4
		for j in range(0,9*n-8,9):										
			if lattconst+0.008 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= 1.45*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= 1.45*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= 1.45*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= 1.45*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= 1.45*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= 1.45*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= 1.45*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= 1.45*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= 1.45*lattconst+0.008:		##The cut-off will change for each new metal##
				if search(coord_count,coord[j]):					##If you found the already counted NN, then empty the first element##
					#print(nn,f)
					if nn != 0 and nn != f:
						a[f] = 0
						a[nn] = a[nn] + 1
						f = f + 1
						nn = nn + 1
					else:
						a[f] = 0
						f = f + 1
						nn = nn + 1
				else:	
					coord_surr_current.append(coord[j])
					coord_surr_current.append(coord[j+1])
					coord_surr_current.append(coord[j+2])
					coord_surr_current.append(coord[j+3])
					coord_surr_current.append(coord[j+4])
					coord_surr_current.append(coord[j+5])
					coord_surr_current.append(coord[j+6])
					coord_surr_current.append(coord[j+7])
					coord_surr_current.append(coord[j+8])
					coord_surr.append(coord[j])
					coord_surr.append(coord[j+1])
					coord_surr.append(coord[j+2])
					coord_surr.append(coord[j+3])
					coord_surr.append(coord[j+4])
					coord_surr.append(coord[j+5])
					coord_surr.append(coord[j+6])
					coord_surr.append(coord[j+7])
					coord_surr.append(coord[j+8])
					#print(nn)
					a[nn] = a[nn] + 1
					nn = nn + 1

		for k in range(0,len(coord_surr_current),9):					##Taking into account the bond formation of NN##
			if search(coord_surr,coord_surr_current[k]):			##If this condition is True##
				b = countX(coord_surr,coord_surr_current[k]) 		##Counting the number of previous repetition##
				if b > 0:
					a[b-1] = a[b-1] + 1
				else:
					continue

		coord_count.append(coord[i])
		coord_count.append(coord[i+1])
		coord_count.append(coord[i+2])
		coord_count.append(coord[i+3])
		coord_count.append(coord[i+4])
		coord_count.append(coord[i+5])
		coord_count.append(coord[i+6])
		coord_count.append(coord[i+7])
		coord_count.append(coord[i+8])
		a_final.append(a)

	print(a_final)
	a1 = 0
	a2 = 0
	a2 = 0
	a3 = 0
	a4 = 0

	for i in range(len(a_final)):
		a1 = a1 + a_final[i][0]
		a2 = a2 + a_final[i][1]
		a3 = a3 + a_final[i][2]
		a4 = a4 + a_final[i][3]


	print("a11 =",a1)
	print("a22 =",a2)
	print("a33 =",a3)
	print("a44 =",a4)
