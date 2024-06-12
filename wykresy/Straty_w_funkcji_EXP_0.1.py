import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([0.0006,0.0007,0.001,0.0012,0.0015,0.002,0.0025,0.003,0.0035,0.004,0.0045,0.005,0.0055])
y_values = np.array([0.050325,0.2269,3.03213,8.1263,18.77443,33.68371,44.7939,52.46946,58.25723,62.34023,65.67716667
,68.2785,70.54248

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
plt.yscale('log')
plt.legend()

# Dodanie etykiet i legendy
plt.xlabel('Wartość parametru λ')
plt.ylabel('Strata %')
#plt.title('Strata ramek w zależności od parametru Lambda')
#plt.xscale('log')

plt.legend()

# Wyświetlanie wykresu
plt.show()
