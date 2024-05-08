Code to calculate delta total adsorbate-adsorbate interactions needs two input files. Each input file should have 'x' coordinates (direct coordinates) in one column and 'y' coordinates (direct coordinates) in the second column. The file names should be "config1.csv" for the initial configuration and "config2.csv" for the final configuration (see the example files with respective names provided hereby). Delta Total interaction counting code reads the file "config1.csv" and "config2.csv", and spits out the coefficients a,b,c,d,... of nearest-neighbor interaction parameters β1, β2, β3, β4 (for (100)) or β1, β2, β3, β4, β5, β6 (for (111)) and likewise second-nearest-neighbor interaction parameters (β11, ..., β44 for (100) or β11, ..., β44 for (111)) in the equation of calculating the difference in the total adsorbate-adsorbate interaction energies between config.2 and config1, i.e., total ads-ads in config2 minus total ads-ads in config1, as discussed in DOI. 

Similarly, the total interaction counting code reads the file "config1.csv" in direct coordinates and spits out the coefficients of respective interaction parameters involved in calculating total adsorbate-adsorbate interactions. 

For example, for configurations of adsorbate on a (111) surface, if the output of either of the codes is [1,1,0,0,3,1]
                                                                                                          [1,1,2,1,0,0]
It means that the equation to calculate ads-ads interactions (total or delta total, depending on which code you use) is: 1 * β1 + 1 * β2 + 0 * β3 + 0 * β4 + 3 * β5 + 1 * β6 + 1 * β11 + 1 * β22 + 2 * β33 + 1 * β44 + 0 * β55 + 0 * β66

The values of all the interaction parameters may be derived or can be directly extracted from the literature, as shown by Patel et al. (https://doi.org/10.1021/acs.jpcc.3c04646)

The "cluster_expansion_ads_ads_interactions.py" file reads "config1.csv" file, described in the first paragraph, and gives the number of following clusters: 1NN, 2NN, ..., 5NN, 1-1-1, 1-1-2, and 1-1-3 in "conf1.csv" input file, which can then be used for predicting effective interaction parameters for each cluster through least-squared-regression against DFT-predicted energy, as suggested by Schneider et al. (https://doi.org/10.1039/C4CY00763H) for (111) surfaces, and Reuter et al. (https://doi.org/10.1103/PhysRevB.75.235406) for (100) surfaces.
