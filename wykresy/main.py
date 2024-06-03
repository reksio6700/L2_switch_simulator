import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Path to your CSV file
csv_file_path = 'data_s2_out.csv'

# Read the CSV file using pandas, specifying no header is present
df = pd.read_csv(csv_file_path, header=None)

# Assuming the data is in the first column, we refer to it by its index 0
# Convert the first column to numeric, just in case it's not already
df[0] = pd.to_numeric(df[0], errors='coerce')
print(df.size)

print(np.average(df[0]))
print(np.std(df[0]))

# Plotting the histogram
plt.figure(figsize=(10, 6))  # Optional: Adjusts the size of the figure
plt.hist(df[0], bins=50, color='blue', edgecolor='black')  # Adjust the number of bins as needed
plt.title('Odstęp czasowy między kolejnymi pakietami na podstawie zrzutu pcap (' + str(df.size) + ' pakietów)')
plt.xlabel('Odstęp czasowy (s)')
plt.ylabel('Liczba pakietów')
plt.xscale('linear')
plt.yscale('log')
plt.grid(True)  # Optional: Adds a grid for better readability
plt.show()