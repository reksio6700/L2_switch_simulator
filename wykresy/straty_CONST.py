import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane - punkty i przedziały ufności
x_values = np.array([0,10,100,300,500,750,1000,1250,1500])
y_values = np.array([94.11966,93.19958,84.93296,66.55869,48.20678,25.49616,8.23661,1.30581,0.10688

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
text_offset = 0.08
for x, y in zip(x_values, y_values):
    plt.text(x, y+text_offset , '{:.2f}%'.format(y), fontsize=6, ha='center')
plt.yscale('log')
#plt.xscale('log')
# Dodanie etykiet i legendy
plt.xlabel('Wartość CONSTANT')
plt.ylabel('Strata %')

#plt.title('Strata ramek w zależności od wartości CONSTANT')


plt.legend()

# Wyświetlanie wykresu
plt.show()
