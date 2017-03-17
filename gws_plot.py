import gwsurrogate as gws
from gwsurrogate import gwtools
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# ell_m specific modes to pull from data: we are pulling (n,n) modes
spec =  gws.EvaluateSurrogate('SpEC_q1_10_NoSpin_nu5thDegPoly_exclude_2_0.h5', ell_m=[(2,2)])

massRatioFirstTerm = [1, 2, 3, 4, 5, 6, 7, 8, 9]
massRatioSecondTerm = [.2, .4, .6, .8]
combined_mass_ratios = []

# generate mass ratios (1.2 - 9.8)
for i in range (len(massRatioFirstTerm)):
	for j in range(len(massRatioSecondTerm)):
		massRatio = massRatioFirstTerm[i] + massRatioSecondTerm[j]
		combined_mass_ratios.append(massRatio)

# generate waveform surrogate for (n,n) mode, plot (n,n) mode
for i in range (len(combined_mass_ratios)):

	modes, times, hp, hc = spec(q = combined_mass_ratios[i] , ell = [2], m = [2], mode_sum = False, fake_neg_modes = False)

	gwtools.plot_pretty(times, [hp, hc],fignum=1)
	plt.plot(times,gwtools.amp(hp+1j*hc),'r')
	plt.title('(%i,%i) mode'%(modes[0][0],modes[0][1]) + " for Mass Ratio: q= " + str(combined_mass_ratios[i]))
	plt.xlabel('t/M')
	plt.savefig('m_' + modes[0] + '_m_' + modes[1] + '_q' + str(combined_mass_ratios[i]) + 'PLOT.png')
	plt.close()
