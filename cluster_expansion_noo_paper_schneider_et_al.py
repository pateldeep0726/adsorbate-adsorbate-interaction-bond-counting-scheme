import pandas as pd

def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count

def searchop(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return False
    return True

def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

#lattconst = float(input("Enter the value of Scaling constant (lattice_constant/1.414):"))
lattconst = 2.95217081000000
cryst = "111"
#cryst = input("Enter the crystal type (100 or 111): ")

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
	
	n = int(input("Enter the number of adsorbates:"))
	#print(coord)
	##Coefficients of correspinding NN parameters##
	sigma_1nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		for j in range(0,9*n-8,9):										
			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
				if searchop(coord_count,coord[j]):					##If you found the already counted NN, then continue##
					sigma_1nn = sigma_1nn + 1
		if searchop(coord_count,coord[i]):
			coord_count.append(coord[i])
			coord_count.append(coord[i+1])
			coord_count.append(coord[i+2])
			coord_count.append(coord[i+3])
			coord_count.append(coord[i+4])
			coord_count.append(coord[i+5])
			coord_count.append(coord[i+6])
			coord_count.append(coord[i+7])
			coord_count.append(coord[i+8])

	print("sigma_1nn =",sigma_1nn)


	##Coefficients of correspinding secNN parameters##
	sigma_2nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		for j in range(0,9*n-8,9):										
			if lattconst+0.008 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= 1.73*lattconst+0.008:		##The cut-off will change for each new metal##
				if searchop(coord_count,coord[j]):					##If you found the already counted NN, then continue##
					sigma_2nn = sigma_2nn + 1
		if searchop(coord_count,coord[i]):
			coord_count.append(coord[i])
			coord_count.append(coord[i+1])
			coord_count.append(coord[i+2])
			coord_count.append(coord[i+3])
			coord_count.append(coord[i+4])
			coord_count.append(coord[i+5])
			coord_count.append(coord[i+6])
			coord_count.append(coord[i+7])
			coord_count.append(coord[i+8])

	print("sigma_2nn =",sigma_2nn)

	##Coefficients of correspinding thirdNN parameters##
	sigma_3nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		for j in range(0,9*n-8,9):										
			if 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= 2.00*lattconst+0.008:		##The cut-off will change for each new metal##
				if searchop(coord_count,coord[j]):					##If you found the already counted NN, then continue##
					sigma_3nn = sigma_3nn + 1
		if searchop(coord_count,coord[i]):
			coord_count.append(coord[i])
			coord_count.append(coord[i+1])
			coord_count.append(coord[i+2])
			coord_count.append(coord[i+3])
			coord_count.append(coord[i+4])
			coord_count.append(coord[i+5])
			coord_count.append(coord[i+6])
			coord_count.append(coord[i+7])
			coord_count.append(coord[i+8])

	print("sigma_3nn =",sigma_3nn)

	##Coefficients of correspinding fourthNN parameters##
	sigma_4nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		for j in range(0,9*n-8,9):										
			if 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= 2.65*lattconst+0.008:		##The cut-off will change for each new metal##
				if searchop(coord_count,coord[j]):					##If you found the already counted NN, then continue##
					sigma_4nn = sigma_4nn + 1
		if searchop(coord_count,coord[i]):
			coord_count.append(coord[i])
			coord_count.append(coord[i+1])
			coord_count.append(coord[i+2])
			coord_count.append(coord[i+3])
			coord_count.append(coord[i+4])
			coord_count.append(coord[i+5])
			coord_count.append(coord[i+6])
			coord_count.append(coord[i+7])
			coord_count.append(coord[i+8])

	print("sigma_4nn =",sigma_4nn)

	##Coefficients of correspinding fifthNN parameters##
	sigma_5nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		for j in range(0,9*n-8,9):										
			if 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= 3.00*lattconst+0.008:		##The cut-off will change for each new metal##
				if searchop(coord_count,coord[j]):					##If you found the already counted NN, then continue##
					sigma_5nn = sigma_5nn + 1
		if searchop(coord_count,coord[i]):
			coord_count.append(coord[i])
			coord_count.append(coord[i+1])
			coord_count.append(coord[i+2])
			coord_count.append(coord[i+3])
			coord_count.append(coord[i+4])
			coord_count.append(coord[i+5])
			coord_count.append(coord[i+6])
			coord_count.append(coord[i+7])
			coord_count.append(coord[i+8])

	print("sigma_5nn =",sigma_5nn)

	##Coefficients of correspinding 1-1-1 parameters##
	sigma_111nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		coord_surr = []
		for j in range(0,9*n-8,9):										
			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
				if searchop(coord_count,coord[j]):					##If you found the already counted NN, then continue##
					coord_surr.append(coord[j])
					coord_surr.append(coord[j+1])
					coord_surr.append(coord[j+2])
					coord_surr.append(coord[j+3])
					coord_surr.append(coord[j+4])
					coord_surr.append(coord[j+5])
					coord_surr.append(coord[j+6])
					coord_surr.append(coord[j+7])
					coord_surr.append(coord[j+8])

		coord_surr_count = []
		for k in range(0,len(coord_surr),9):
			for l in range(0,len(coord_surr),9):									
				if 0 < round(((coord_surr[k][0]-coord_surr[l][0])**2 + (coord_surr[k][1]-coord_surr[l][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord_surr[k][0]-coord_surr[l+1][0])**2 + (coord_surr[k][1]-coord_surr[l+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord_surr[k][0]-coord_surr[l+2][0])**2 + (coord_surr[k][1]-coord_surr[l+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord_surr[k][0]-coord_surr[l+3][0])**2 + (coord_surr[k][1]-coord_surr[l+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord_surr[k][0]-coord_surr[l+4][0])**2 + (coord_surr[k][1]-coord_surr[l+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord_surr[k][0]-coord_surr[l+5][0])**2 + (coord_surr[k][1]-coord_surr[l+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord_surr[k][0]-coord_surr[l+6][0])**2 + (coord_surr[k][1]-coord_surr[l+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord_surr[k][0]-coord_surr[l+7][0])**2 + (coord_surr[k][1]-coord_surr[l+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord_surr[k][0]-coord_surr[l+8][0])**2 + (coord_surr[k][1]-coord_surr[l+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
					if searchop(coord_surr_count,coord_surr[l]):
						sigma_111nn = sigma_111nn + 1


			if searchop(coord_surr_count,coord_surr[k]):					##If you found the already counted NN, then continue##
				coord_surr_count.append(coord_surr[k])
				coord_surr_count.append(coord_surr[k+1])
				coord_surr_count.append(coord_surr[k+2])
				coord_surr_count.append(coord_surr[k+3])
				coord_surr_count.append(coord_surr[k+4])
				coord_surr_count.append(coord_surr[k+5])
				coord_surr_count.append(coord_surr[k+6])
				coord_surr_count.append(coord_surr[k+7])
				coord_surr_count.append(coord_surr[k+8])
		

		if searchop(coord_count,coord[i]):
			coord_count.append(coord[i])
			coord_count.append(coord[i+1])
			coord_count.append(coord[i+2])
			coord_count.append(coord[i+3])
			coord_count.append(coord[i+4])
			coord_count.append(coord[i+5])
			coord_count.append(coord[i+6])
			coord_count.append(coord[i+7])
			coord_count.append(coord[i+8])

	print("sigma_111nn =",sigma_111nn)

	##Coefficients of correspinding 1-1-2 parameters##
	sigma_112nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		coord_surr = []
		for j in range(0,9*n-8,9):										
			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
				for k in range(0,9*n-8,9):
					if 0 < round(((coord[j][0]-coord[k][0])**2 + (coord[j][1]-coord[k][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+1][0])**2 + (coord[j][1]-coord[k+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+2][0])**2 + (coord[j][1]-coord[k+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+3][0])**2 + (coord[j][1]-coord[k+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+4][0])**2 + (coord[j][1]-coord[k+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+5][0])**2 + (coord[j][1]-coord[k+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+6][0])**2 + (coord[j][1]-coord[k+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+7][0])**2 + (coord[j][1]-coord[k+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+8][0])**2 + (coord[j][1]-coord[k+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
						for l in range(0,9*n-8,9):
							if lattconst+0.008 < round(((coord[k][0]-coord[l][0])**2 + (coord[k][1]-coord[l][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[k][0]-coord[l+1][0])**2 + (coord[k][1]-coord[l+1][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[k][0]-coord[l+2][0])**2 + (coord[k][1]-coord[l+2][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[k][0]-coord[l+3][0])**2 + (coord[k][1]-coord[l+3][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[k][0]-coord[l+4][0])**2 + (coord[k][1]-coord[l+4][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[k][0]-coord[l+5][0])**2 + (coord[k][1]-coord[l+5][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[k][0]-coord[l+6][0])**2 + (coord[k][1]-coord[l+6][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[k][0]-coord[l+7][0])**2 + (coord[k][1]-coord[l+7][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[k][0]-coord[l+8][0])**2 + (coord[k][1]-coord[l+8][1])**2)**0.5,3) <= 1.73*lattconst+0.008:		##The cut-off will change for each new metal##
								if coord[l] == coord[i] and (searchop(coord_count,coord[i]) and searchop(coord_count,coord[j]) and searchop(coord_count,coord[k])):
									sigma_112nn = sigma_112nn + 1	
									coord_count.append(coord[i])
									coord_count.append(coord[i+1])
									coord_count.append(coord[i+2])
									coord_count.append(coord[i+3])
									coord_count.append(coord[i+4])
									coord_count.append(coord[i+5])
									coord_count.append(coord[i+6])
									coord_count.append(coord[i+7])
									coord_count.append(coord[i+8])
									coord_count.append(coord[j])
									coord_count.append(coord[j+1])
									coord_count.append(coord[j+2])
									coord_count.append(coord[j+3])
									coord_count.append(coord[j+4])
									coord_count.append(coord[j+5])
									coord_count.append(coord[j+6])
									coord_count.append(coord[j+7])
									coord_count.append(coord[j+8])
									coord_count.append(coord[k])
									coord_count.append(coord[k+1])
									coord_count.append(coord[k+2])
									coord_count.append(coord[k+3])
									coord_count.append(coord[k+4])
									coord_count.append(coord[k+5])
									coord_count.append(coord[k+6])
									coord_count.append(coord[k+7])
									coord_count.append(coord[k+8])

	print("sigma_112nn =",sigma_112nn)

	##Coefficients of correspinding 1-1-2 parameters##
	sigma_113nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		coord_surr = []
		for j in range(0,9*n-8,9):										
			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
				for k in range(0,9*n-8,9):
					if 0 < round(((coord[j][0]-coord[k][0])**2 + (coord[j][1]-coord[k][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+1][0])**2 + (coord[j][1]-coord[k+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+2][0])**2 + (coord[j][1]-coord[k+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+3][0])**2 + (coord[j][1]-coord[k+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+4][0])**2 + (coord[j][1]-coord[k+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+5][0])**2 + (coord[j][1]-coord[k+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+6][0])**2 + (coord[j][1]-coord[k+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+7][0])**2 + (coord[j][1]-coord[k+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[j][0]-coord[k+8][0])**2 + (coord[j][1]-coord[k+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
						for l in range(0,9*n-8,9):
							if 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l][0])**2 + (coord[k][1]-coord[l][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l+1][0])**2 + (coord[k][1]-coord[l+1][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l+2][0])**2 + (coord[k][1]-coord[l+2][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l+3][0])**2 + (coord[k][1]-coord[l+3][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l+4][0])**2 + (coord[k][1]-coord[l+4][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l+5][0])**2 + (coord[k][1]-coord[l+5][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l+6][0])**2 + (coord[k][1]-coord[l+6][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l+7][0])**2 + (coord[k][1]-coord[l+7][1])**2)**0.5,3) <= 2.00*lattconst+0.008 or 1.73*lattconst+0.008 < round(((coord[k][0]-coord[l+8][0])**2 + (coord[k][1]-coord[l+8][1])**2)**0.5,3) <= 2.00*lattconst+0.008:		##The cut-off will change for each new metal##
								if coord[l] == coord[i] and (searchop(coord_count,coord[i]) and searchop(coord_count,coord[j]) and searchop(coord_count,coord[k])):
									sigma_113nn = sigma_113nn + 1	
									coord_count.append(coord[i])
									coord_count.append(coord[i+1])
									coord_count.append(coord[i+2])
									coord_count.append(coord[i+3])
									coord_count.append(coord[i+4])
									coord_count.append(coord[i+5])
									coord_count.append(coord[i+6])
									coord_count.append(coord[i+7])
									coord_count.append(coord[i+8])
									coord_count.append(coord[j])
									coord_count.append(coord[j+1])
									coord_count.append(coord[j+2])
									coord_count.append(coord[j+3])
									coord_count.append(coord[j+4])
									coord_count.append(coord[j+5])
									coord_count.append(coord[j+6])
									coord_count.append(coord[j+7])
									coord_count.append(coord[j+8])
									coord_count.append(coord[k])
									coord_count.append(coord[k+1])
									coord_count.append(coord[k+2])
									coord_count.append(coord[k+3])
									coord_count.append(coord[k+4])
									coord_count.append(coord[k+5])
									coord_count.append(coord[k+6])
									coord_count.append(coord[k+7])
									coord_count.append(coord[k+8])

	print("sigma_113nn =",sigma_113nn)


# elif cryst == "100":
# 	coord = pd.read_csv("/mnt/c/users/dmpatel/OneDrive - Iowa State University/desktop/research_data/General Script/Fermi_Development/config1.csv", sep = '  ', usecols = [0,1], names = ["x", "y"])
# 	print(coord)
# 	x = coord.x.to_list()
# 	y = coord.y.to_list()
# 	coord = []
# 	#print(x,y)
# 	for i in range(len(x)):	##Creating and saving periodic images of a slab repeated by 3x3##										
# 		x[i] = x[i]*4*lattconst
# 		y[i] = y[i]*4*lattconst
# 		coord.append([x[i]+4*lattconst,y[i]+4*lattconst])
# 		coord.append([x[i]+8*lattconst,y[i]+4*lattconst])
# 		coord.append([x[i],y[i]+4*lattconst])
# 		coord.append([x[i]+4*lattconst,y[i]])
# 		coord.append([x[i]+4*lattconst,y[i]+2*4*lattconst])
# 		coord.append([x[i],y[i]])
# 		coord.append([x[i]+8*lattconst,y[i]])
# 		coord.append([x[i]+8*lattconst,y[i]+2*4*lattconst])
# 		coord.append([x[i],y[i]+2*4*lattconst])
		
# 	#print(coord)
# 	##Coefficients of correspinding NN parameters##
# 	a_final = []
# 	n = int(input("Enter the number of adsorbates:"))
# 	coord_count = []
# 	coord_surr = []
# 	for i in range(0,9*n-8,9):
# 		coord_surr_current = []
# 		f = 0
# 		nn = 0
# 		a = [0]*4
# 		print(i)
# 		for j in range(0,9*n-8,9):										
# 			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
# 				if search(coord_count,coord[j]):					##If you found the already counted NN, then empty the first element##
# 					#print(nn,f)
# 					if nn != 0 and nn != f:
# 						a[f] = 0
# 						a[nn] = a[nn] + 1
# 						f = f + 1
# 						nn = nn + 1
# 					else:
# 						a[f] = 0
# 						f = f + 1
# 						nn = nn + 1
# 				else:	
# 					coord_surr_current.append(coord[j])
# 					coord_surr_current.append(coord[j+1])
# 					coord_surr_current.append(coord[j+2])
# 					coord_surr_current.append(coord[j+3])
# 					coord_surr_current.append(coord[j+4])
# 					coord_surr_current.append(coord[j+5])
# 					coord_surr_current.append(coord[j+6])
# 					coord_surr_current.append(coord[j+7])
# 					coord_surr_current.append(coord[j+8])
# 					coord_surr.append(coord[j])
# 					coord_surr.append(coord[j+1])
# 					coord_surr.append(coord[j+2])
# 					coord_surr.append(coord[j+3])
# 					coord_surr.append(coord[j+4])
# 					coord_surr.append(coord[j+5])
# 					coord_surr.append(coord[j+6])
# 					coord_surr.append(coord[j+7])
# 					coord_surr.append(coord[j+8])
# 					#print(nn)
# 					a[nn] = a[nn] + 1
# 					nn = nn + 1

# 		for k in range(0,len(coord_surr_current),9):					##Taking into account the bond formation of NN##
# 			if search(coord_surr,coord_surr_current[k]):			##If this condition is True##
# 				b = countX(coord_surr,coord_surr_current[k]) 		##Counting the number of previous repetition##
# 				if b > 0:
# 					a[b-1] = a[b-1] + 1
# 				else:
# 					continue
# 			else:
# 				continue

# 		coord_count.append(coord[i])
# 		coord_count.append(coord[i+1])
# 		coord_count.append(coord[i+2])
# 		coord_count.append(coord[i+3])
# 		coord_count.append(coord[i+4])
# 		coord_count.append(coord[i+5])
# 		coord_count.append(coord[i+6])
# 		coord_count.append(coord[i+7])
# 		coord_count.append(coord[i+8])
# 		a_final.append(a)

# 	print(a_final)
# 	a1 = 0
# 	a2 = 0
# 	a2 = 0
# 	a3 = 0
# 	a4 = 0

# 	for i in range(len(a_final)):
# 		a1 = a1 + a_final[i][0]
# 		a2 = a2 + a_final[i][1]
# 		a3 = a3 + a_final[i][2]
# 		a4 = a4 + a_final[i][3]


# 	print("a1 =",a1)
# 	print("a2 =",a2)
# 	print("a3 =",a3)
# 	print("a4 =",a4)


# 	##Coefficients of correspinding secNN parameters##
# 	a_final = []
# 	coord_count = []
# 	coord_surr = []
# 	i = 0
# 	k = 0
# 	b = 0
# 	for i in range(0,9*n-8,9):
# 		coord_surr_current = []
# 		f = 0
# 		nn = 0
# 		a = [0]*4
# 		for j in range(0,9*n-8,9):										
# 			if lattconst+0.008 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= 1.73*lattconst+0.008:		##The cut-off will change for each new metal##
# 				if search(coord_count,coord[j]):					##If you found the already counted NN, then empty the first element##
# 					#print(nn,f)
# 					if nn != 0 and nn != f:
# 						a[f] = 0
# 						a[nn] = a[nn] + 1
# 						f = f + 1
# 						nn = nn + 1
# 					else:
# 						a[f] = 0
# 						f = f + 1
# 						nn = nn + 1
# 				else:	
# 					coord_surr_current.append(coord[j])
# 					coord_surr_current.append(coord[j+1])
# 					coord_surr_current.append(coord[j+2])
# 					coord_surr_current.append(coord[j+3])
# 					coord_surr_current.append(coord[j+4])
# 					coord_surr_current.append(coord[j+5])
# 					coord_surr_current.append(coord[j+6])
# 					coord_surr_current.append(coord[j+7])
# 					coord_surr_current.append(coord[j+8])
# 					coord_surr.append(coord[j])
# 					coord_surr.append(coord[j+1])
# 					coord_surr.append(coord[j+2])
# 					coord_surr.append(coord[j+3])
# 					coord_surr.append(coord[j+4])
# 					coord_surr.append(coord[j+5])
# 					coord_surr.append(coord[j+6])
# 					coord_surr.append(coord[j+7])
# 					coord_surr.append(coord[j+8])
# 					#print(nn)
# 					a[nn] = a[nn] + 1
# 					nn = nn + 1

# 		for k in range(0,len(coord_surr_current),9):					##Taking into account the bond formation of NN##
# 			if search(coord_surr,coord_surr_current[k]):			##If this condition is True##
# 				b = countX(coord_surr,coord_surr_current[k]) 		##Counting the number of previous repetition##
# 				if b > 0:
# 					a[b-1] = a[b-1] + 1
# 				else:
# 					continue

# 		coord_count.append(coord[i])
# 		coord_count.append(coord[i+1])
# 		coord_count.append(coord[i+2])
# 		coord_count.append(coord[i+3])
# 		coord_count.append(coord[i+4])
# 		coord_count.append(coord[i+5])
# 		coord_count.append(coord[i+6])
# 		coord_count.append(coord[i+7])
# 		coord_count.append(coord[i+8])
# 		a_final.append(a)

# 	print(a_final)
# 	a1 = 0
# 	a2 = 0
# 	a2 = 0
# 	a3 = 0
# 	a4 = 0

# 	for i in range(len(a_final)):
# 		a1 = a1 + a_final[i][0]
# 		a2 = a2 + a_final[i][1]
# 		a3 = a3 + a_final[i][2]
# 		a4 = a4 + a_final[i][3]


# 	print("a11 =",a1)
# 	print("a22 =",a2)
# 	print("a33 =",a3)
# 	print("a44 =",a4)
