import gwsurrogate as gws
from gwsurrogate import gwtools
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# ell_m specific modes to pull from data: we are pulling (2,2) modes
spec =  gws.EvaluateSurrogate('SpEC_q1_10_NoSpin_nu5thDegPoly_exclude_2_0.h5', ell_m=[(2,2)])

timeLength = 28501
massRatioFirstTerm = [1, 2, 3, 4, 5, 6, 7]
massRatioSecondTerm = [.2, .4, .6, .8]
combined_mass_ratios = []

# generate mass ratios (1.2 - 9.8)
for i in range (len(massRatioFirstTerm)):
	for j in range(len(massRatioSecondTerm)):
		massRatio = massRatioFirstTerm[i] + massRatioSecondTerm[j]
		combined_mass_ratios.append(massRatio)

# parse time, cross/plus polarization data, saves to text file in same directory
for i in range (len(combined_mass_ratios)):

	formatted_data = []
	modes, times, hp, hc = spec(q = combined_mass_ratios[i], ell = [2], m = [2], mode_sum = False, fake_neg_modes = False)

	for j in range(timeLength):
		formatted_data.append((times[j], hp[j], hc[j]))

	dataframe = pd.DataFrame.from_records(formatted_data, columns = ['Times', 'Plus Polarization', 'Cross Polarization'])
	file_name = 'm_' + modes[0] + '_m_' + modes[1] + '_q' + str(combined_mass_ratios[i]) +'_f15.txt'
	np.savetxt(file_name, dataframe.values, fmt='%.18e\t%.18e\t%.18e')

