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
#cryst = input("Enter the crystal type (100 or 111): ")
cryst = "111"

if cryst == "111": ##Patterns suggested by Schneider et al. (2014): https://pubs.rsc.org/en/content/articlelanding/2014/cy/c4cy00763h##
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
								if coord[l] == coord[i] and (searchop(coord_count,coord[i]) or searchop(coord_count,coord[j]) or searchop(coord_count,coord[k])):
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

	##Coefficients of correspinding 1-1-3 parameters##
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
								if coord[l] == coord[i] and (searchop(coord_count,coord[i]) or searchop(coord_count,coord[j]) or searchop(coord_count,coord[k])):
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


if cryst == "100": ## Patterns suggested by Reuter et al. (2007): 10.1103/PhysRevB.75.235406##
	coord = pd.read_csv("/mnt/c/users/dmpatel/OneDrive - Iowa State University/desktop/research_data/General Script/Fermi_Development/config1.csv", sep = '  ', usecols = [0,1], names = ["x", "y"])
	print(coord)
	x = coord.x.to_list()
	y = coord.y.to_list()
	coord = []
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
	print(True and (True or False or False))

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
								if coord[l] == coord[i] and (searchop(coord_count,coord[i]) or searchop(coord_count,coord[j]) or searchop(coord_count,coord[k])):
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

	##Coefficients of correspinding 1-1-3 parameters##
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
								if coord[l] == coord[i] and (searchop(coord_count,coord[i]) or searchop(coord_count,coord[j]) or searchop(coord_count,coord[k])):
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

	##Coefficients of correspinding 1-2-4 parameters##
	sigma_124nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		coord_surr = []
		for j in range(0,9*n-8,9):										
			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
				for k in range(0,9*n-8,9):
					if lattconst+0.008 < round(((coord[j][0]-coord[k][0])**2 + (coord[j][1]-coord[k][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+1][0])**2 + (coord[j][1]-coord[k+1][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+2][0])**2 + (coord[j][1]-coord[k+2][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+3][0])**2 + (coord[j][1]-coord[k+3][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+4][0])**2 + (coord[j][1]-coord[k+4][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+5][0])**2 + (coord[j][1]-coord[k+5][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+6][0])**2 + (coord[j][1]-coord[k+6][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+7][0])**2 + (coord[j][1]-coord[k+7][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+8][0])**2 + (coord[j][1]-coord[k+8][1])**2)**0.5,3) <= 1.73*lattconst+0.008:		##The cut-off will change for each new metal##
						for l in range(0,9*n-8,9):
							if 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l][0])**2 + (coord[k][1]-coord[l][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l+1][0])**2 + (coord[k][1]-coord[l+1][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l+2][0])**2 + (coord[k][1]-coord[l+2][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l+3][0])**2 + (coord[k][1]-coord[l+3][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l+4][0])**2 + (coord[k][1]-coord[l+4][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l+5][0])**2 + (coord[k][1]-coord[l+5][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l+6][0])**2 + (coord[k][1]-coord[l+6][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l+7][0])**2 + (coord[k][1]-coord[l+7][1])**2)**0.5,3) <= 2.65*lattconst+0.008 or 2.00*lattconst+0.008 < round(((coord[k][0]-coord[l+8][0])**2 + (coord[k][1]-coord[l+8][1])**2)**0.5,3) <= 2.65*lattconst+0.008:		##The cut-off will change for each new metal##
								if coord[l] == coord[i] and (searchop(coord_count,coord[i]) or searchop(coord_count,coord[j]) or searchop(coord_count,coord[k])):
									sigma_124nn = sigma_124nn + 1	
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

	print("sigma_124nn =",sigma_124nn)

	##Coefficients of correspinding 2-2-5 parameters##
	sigma_225nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		coord_surr = []
		for j in range(0,9*n-8,9):										
			if lattconst+0.008 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= 1.73*lattconst+0.008:		##The cut-off will change for each new metal##
				for k in range(0,9*n-8,9):
					if lattconst+0.008 < round(((coord[j][0]-coord[k][0])**2 + (coord[j][1]-coord[k][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+1][0])**2 + (coord[j][1]-coord[k+1][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+2][0])**2 + (coord[j][1]-coord[k+2][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+3][0])**2 + (coord[j][1]-coord[k+3][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+4][0])**2 + (coord[j][1]-coord[k+4][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+5][0])**2 + (coord[j][1]-coord[k+5][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+6][0])**2 + (coord[j][1]-coord[k+6][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+7][0])**2 + (coord[j][1]-coord[k+7][1])**2)**0.5,3) <= 1.73*lattconst+0.008 or lattconst+0.008 < round(((coord[j][0]-coord[k+8][0])**2 + (coord[j][1]-coord[k+8][1])**2)**0.5,3) <= 1.73*lattconst+0.008:		##The cut-off will change for each new metal##
						for l in range(0,9*n-8,9):
							if 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l][0])**2 + (coord[k][1]-coord[l][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l+1][0])**2 + (coord[k][1]-coord[l+1][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l+2][0])**2 + (coord[k][1]-coord[l+2][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l+3][0])**2 + (coord[k][1]-coord[l+3][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l+4][0])**2 + (coord[k][1]-coord[l+4][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l+5][0])**2 + (coord[k][1]-coord[l+5][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l+6][0])**2 + (coord[k][1]-coord[l+6][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l+7][0])**2 + (coord[k][1]-coord[l+7][1])**2)**0.5,3) <= 3.00*lattconst+0.008 or 2.65*lattconst+0.008 < round(((coord[k][0]-coord[l+8][0])**2 + (coord[k][1]-coord[l+8][1])**2)**0.5,3) <= 3.00*lattconst+0.008:		##The cut-off will change for each new metal##
								if coord[l] == coord[i] and (searchop(coord_count,coord[i]) or searchop(coord_count,coord[j]) or searchop(coord_count,coord[k])):
									sigma_225nn = sigma_225nn + 1	
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

	print("sigma_225nn =", sigma_225nn)


	##Coefficients of correspinding 1-1-1-2-2 parameters##
	sigma_11122nn = 0
	coord_count = []
	for i in range(0,9*n-8,9):
		count = 0
		coord_surr = []
		for j in range(0,9*n-8,9):										
			if 0 < round(((coord[i][0]-coord[j][0])**2 + (coord[i][1]-coord[j][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+1][0])**2 + (coord[i][1]-coord[j+1][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+2][0])**2 + (coord[i][1]-coord[j+2][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+3][0])**2 + (coord[i][1]-coord[j+3][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+4][0])**2 + (coord[i][1]-coord[j+4][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+5][0])**2 + (coord[i][1]-coord[j+5][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+6][0])**2 + (coord[i][1]-coord[j+6][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+7][0])**2 + (coord[i][1]-coord[j+7][1])**2)**0.5,3) <= lattconst+0.008 or 0 < round(((coord[i][0]-coord[j+8][0])**2 + (coord[i][1]-coord[j+8][1])**2)**0.5,3) <= lattconst+0.008:		##The cut-off will change for each new metal##
				
				coord_surr.append(coord[j])
				coord_surr.append(coord[j+1])
				coord_surr.append(coord[j+2])
				coord_surr.append(coord[j+3])
				coord_surr.append(coord[j+4])
				coord_surr.append(coord[j+5])
				coord_surr.append(coord[j+6])
				coord_surr.append(coord[j+7])
				coord_surr.append(coord[j+8])
				count = count + 1
		
		if count == 3:
			if (searchop(coord_count,coord[i]) or searchop(coord_count,coord_surr[0]) or searchop(coord_count,coord_surr[9]) or searchop(coord_count,coord_surr[18])) == True:
				sigma_11122nn = sigma_11122nn + 1
				coord_count.append(coord[i])
				coord_count.append(coord[i+1])
				coord_count.append(coord[i+2])
				coord_count.append(coord[i+3])
				coord_count.append(coord[i+4])
				coord_count.append(coord[i+5])
				coord_count.append(coord[i+6])
				coord_count.append(coord[i+7])
				coord_count.append(coord[i+8])
				for k in range(0,len(coord_surr)):
					if searchop(coord_count, coord_surr[k]) == True:
						coord_count.append(coord_surr[k])
		elif count == 4:
			if (searchop(coord_count,coord[i]) or searchop(coord_count,coord_surr[0]) or searchop(coord_count,coord_surr[9]) or searchop(coord_count,coord_surr[18]) or searchop(coord_count,coord_surr[27])) == True:
				sigma_11122nn = sigma_11122nn + 4
				coord_count.append(coord[i])
				coord_count.append(coord[i+1])
				coord_count.append(coord[i+2])
				coord_count.append(coord[i+3])
				coord_count.append(coord[i+4])
				coord_count.append(coord[i+5])
				coord_count.append(coord[i+6])
				coord_count.append(coord[i+7])
				coord_count.append(coord[i+8])
				for k in range(0,len(coord_surr)):
					if searchop(coord_count, coord_surr[k]) == True:
						coord_count.append(coord_surr[k])


	print("sigma_11122nn =", sigma_11122nn)