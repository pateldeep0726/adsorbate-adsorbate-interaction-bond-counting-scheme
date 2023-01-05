Code to calculate delta total adsorbate-adsorbate interactions need two input files. Each input files should have 'x' coordinates in one column, and 'y' coordinates in the second column. The file names should be "config1.csv" for initial configuration, and "config2.csv" for final configuration (see the example files with respective name provided hereby). Delta Total interaction countring code reads file "config1.csv" and "config2.csv", and spits out the coefficients a,b,c,d,... of nearest-neighbor interaction parmeters y1,y2,y3,y4 (for (100))and y1,y2,y3,y4,y5,y6 (for (111)) and likewise second-nearest-neighbor interaction parameters (y11,...,y44 for (100), and y11, ...,y66 for (111)) in the equation of calculating difference in the total adsorbate-adsorbate interaction energies between config.2 and config1, i.e., total ads-ads in config2 minus total ads-ads in config1, as discuseed in DOI. 

Similarly, total interaction counting code reads the file "config1.csv", and spits out the coefficients of respective interaction parameters involved in calculation total adsorbate-adsorbate interactions. 

For example, for configurations of adsorbate on a (111) surface, if the output of either of the codes is: [1,1,0,0,3,1]
                                                                                                          [1,1,2,1,0,0]
It means that the equation to calculate ads-ads interactions (total or delta total, depending on which code you use) is: 1*y1 + 1*y2 + 0*y3 + 0*y4 + 3*y5 + 1*y6 + 1*y11 + 1*y22 + 2*y33 + 1*y44 + 0*y55 + 0*y66

The values of all the interaction parameters may be derived or can be directly extracted from literature, as shown in DOI.
