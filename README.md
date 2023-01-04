Each input files should have 'x' coordinates in one column, and 'y' coordinates in the second column. The file names should be "config1.csv" for initial
configuration, and "config2.csv" for final configuration.

Total interaction counting code reads the file "config1.csv", and spits out the coefficients a,b,c,d,... of nearest-neighbor interaction parmeters y1,y2,y3,y4 (for (100))and y1,y2,y3,y4,y5,y6 (for (111)) and likewise second-nearest-neighbor interaction parameters (y11,...,y44 for (100), and y11, ...,y66 for (111))in the equation of calculating total adsorbate-adsorbate interactions as discussed in <ENTER DOI OF THE PAPER>.

Similarly, delta Total interaction countring code reads file "config1.csv" and "config2.csv", and spits out the coefficients of respective interaction parameters involved in calculation difference in the total adsorbate-adsorbate interaction energies between config.2 minus config1.

For example, for configurations of adsorbate on a (111) surface, if the output of either of the codes is: [1,1,0,0,3,1]
                                                                                                          [1,1,2,1,0,0]
It means that the equation to calculate ads-ads interactions (total or delta total, depending on which code you use) is: 1*y1 + 1*y2 + 0*y3 + 0*y4 + 3*y5 + 1*y6 + 1*y11 + 1*y22 + 2*y33 + 1*y44 + 0*y55 + 0*y66
