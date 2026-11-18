import matplotlib.pyplot as plt
import numpy as np


with open('June-2021-Provo-River-Streamflow-Rates.csv', 'r') as file:
    next(file)
    data = []
    for line in file:
        line_data = line.strip().split(',')
        line_data[0] = line_data[0].strip('"')
        line_data[1:] = [float(value) for value in line_data[1:]]
        data.append(line_data)

dates = np.array([line[0] for line in data], dtype='datetime64[s]')
flows = np.array([line[1:] for line in data], dtype=float)
sites = ['10163000', '10155200', '10155500', '10154200', '10155000']

plt.figure(figsize=(10, 5))
for column in range(flows.shape[1]):
    plt.plot(dates, flows[:, column], label=f'Site {sites[column]}')
plt.title('Provo River Streamflow Rates, June 2021')
plt.xlabel('Date')
plt.ylabel('Streamflow (ft³/s)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
