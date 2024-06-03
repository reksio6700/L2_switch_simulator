import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([1,5,10,20,50,200,500,1000,2500,5000,7500,10000])
y_values = np.array([96.81276667,80.99176667,67.92433333,65.5781,65.68716667,65.39113333,64.8107,63.708,59.80363333,52.39003,39.87286667,14.3261])

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
plt.xlabel('Wielkość bufora')
plt.ylabel('Strata %')
plt.title('Strata ramek w zależności od wielkości bufora dla Lambda = 0.0035')
plt.xscale('log')

plt.legend()

# Wyświetlanie wykresu
plt.show()
