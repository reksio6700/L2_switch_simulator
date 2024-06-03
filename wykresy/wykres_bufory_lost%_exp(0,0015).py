import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([1,5,15,25,50,100,500,1000,2000,5000])
y_values = np.array([93.39015,60.32705,28.467,28.33445,28.36965,27.8562,26.70265,24.6672,20.56545,3.6585
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
plt.xlabel('Wielkość bufora')
plt.ylabel('Strata %')
plt.title('Strata rammek w zależności od wielkości bufora dla Lambda = 0.0015')
plt.xscale('log')

plt.legend()

# Wyświetlanie wykresu
plt.show()
