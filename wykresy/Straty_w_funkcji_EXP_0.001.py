import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([0.0005,0.0007,0.001,0.0012,0.0015,0.002,0.0025,0.003,0.0035,0.004,0.0045,0.005])
y_values = np.array([0.21929,2.12308,12.41878,21.6918,34.0798,48.3298,57.4485,63.5878,67.9751,71.2136,73.7663,75.7655

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
plt.xlabel('Wartość parametru Lambda')
plt.ylabel('Strata %')
plt.title('Strata ramek w zależności od parametru Lambda')
#plt.xscale('log')

plt.legend()

# Wyświetlanie wykresu
plt.show()
