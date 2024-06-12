import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter, LogLocator
# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([25,100,250])
y_values_4 = np.array([42.59249,41.21823,44.40814])
y_values_8 = np.array([18.27002,17.31298,19.24494])
y_values_16 = np.array([16.83659,16.514488,16.63725])
y_values_32 = np.array([16.6115,16.98817,16.601956])

# Przykładowe przedziały ufności (dolne i górne wartości)
#lower_confidence_interval = np.array([84.78746978,20.21910573,5.022251408,1.53733438,0.808003093,0.540068567,0.356958066,0.185465779])

#upper_confidence_interval = np.array([89.36813022,21.19489427,5.379748592,1.63506562,0.857196907,0.574331433,0.391841934,0.218534221])

# Rysowanie wykresu punktów
plt.scatter(x_values, y_values_4,label='CAM SIZE= 4')
plt.scatter(x_values, y_values_8,label='CAM SIZE= 8')
plt.scatter(x_values, y_values_16,label='CAM SIZE= 16')
plt.scatter(x_values, y_values_32,label='CAM SIZE= 32')
#pozioma
#plt.axhline(y=40, color='red', linestyle='--')
# Rysowanie przedziałów ufności
#plt.errorbar(x_values, y_values, yerr=[y_values - lower_confidence_interval, upper_confidence_interval - y_values],
            # fmt='none', ecolor='gray', capsize=5, capthick=2)

# Dodanie etykiet i legendy
plt.xlabel('CAM TTL')
plt.ylabel('Strata ramek [%]')

#formatter = FuncFormatter(lambda y, _: '{:.0f}%'.format(y))
#plt.gca().yaxis.set_major_formatter(formatter)
#text_offset = 0.2
#for x, y in zip(x_values, y_values):
    #plt.text(x, y+text_offset , '{:.2f}%'.format(y), fontsize=6, ha='center')
plt.yscale('log')
plt.legend()

# Wyświetlanie wykresu
plt.show()
