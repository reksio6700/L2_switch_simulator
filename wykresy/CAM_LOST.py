import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([1,2,3,4,5,6,7,8,9,10,12,15,18,20])
y_values = np.array([93.7278,93.02346667,92.1088,90.83073333,89.10933333,86.52733333,82.54633333,75.671,75.6564,75.6473,75.69363333,75.6536,75.6241,75.6321










])

# Przykładowe przedziały ufności (dolne i górne wartości)
#lower_confidence_interval = np.array([84.78746978,20.21910573,5.022251408,1.53733438,0.808003093,0.540068567,0.356958066,0.185465779])

#upper_confidence_interval = np.array([89.36813022,21.19489427,5.379748592,1.63506562,0.857196907,0.574331433,0.391841934,0.218534221])

# Rysowanie wykresu punktów
plt.scatter(x_values, y_values)

#pozioma
#plt.axhline(y=40, color='red', linestyle='--')
# Rysowanie przedziałów ufności
#plt.errorbar(x_values, y_values, yerr=[y_values - lower_confidence_interval, upper_confidence_interval - y_values],
            # fmt='none', ecolor='gray', capsize=5, capthick=2)

# Dodanie etykiet i legendy
plt.xlabel('Wielkość tablicy CAM')
plt.ylabel('Strata %')
plt.title('Strata ramek w zależności wielkości tablicy CAM')
plt.xscale('linear')

plt.legend()

# Wyświetlanie wykresu
plt.show()
