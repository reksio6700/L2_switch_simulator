import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([1,5,10,15,20])
y_values = np.array([94.8488,67.5038,33.4451,7.7065,0.373333333
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
text_offset = 0.01
for x, y in zip(x_values, y_values):
    plt.text(x, y+text_offset , '{:.2f}%'.format(y), fontsize=7, ha='center')

plt.legend()
# Dodanie etykiet i legendy
plt.xlabel('Wielkość bufora')
plt.ylabel('Strata %')
#plt.title('Strata ramek w zależności od wielkości bufora dla Lambda = 0.002 ')
#plt.xscale('log')

plt.legend()

# Wyświetlanie wykresu
plt.show()
