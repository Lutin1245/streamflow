import matplotlib.pyplot as plt
import numpy as np


def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    with open(filename, 'r') as file:
        next(file)
        data = []
        for line in file:
            line_data = line.strip().split(',')
            line_data[0] = line_data[0].strip('"')
            line_data[1:] = [float(value) for value in line_data[1:]]
            data.append(line_data)

    dates = np.array([line[0] for line in data], dtype='datetime64[s]')
    flows = np.array([line[1:] for line in data], dtype=float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge with the Matplotlib homework formatting."""
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
    plt.savefig('provo_streamflow.png', dpi=150, bbox_inches='tight')
    plt.show()


# Excel check for gauge 10163000: maximum = 131.0 cfs; average = 56.9523611111 cfs.
def summarize(dates, flows, sites):
    """Print and save maximum, date of maximum, minimum, and average flow for each gauge."""
    print(f"{'Gauge':<12}{'Max (cfs)':>10}   {'Date of max':<19}{'Min (cfs)':>10}   {'Avg (cfs)':>10}")

    with open('streamflow_summary.csv', 'w') as file:
        file.write('Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n')
        for column, site in enumerate(sites):
            gauge_flows = flows[:, column]
            maximum = np.max(gauge_flows)
            minimum = np.min(gauge_flows)
            average = np.mean(gauge_flows)
            maximum_row = np.argmax(gauge_flows)
            date_of_maximum = str(dates[maximum_row])
            print(f"{site:<12}{maximum:10.1f}   {date_of_maximum:<19}{minimum:10.1f}   {average:10.1f}")
            file.write(f"{site},{maximum:.1f},{date_of_maximum},{minimum:.1f},{average:.1f}\n")


# Main program
sites = ['10163000', '10155200', '10155500', '10154200', '10155000']
dates, flows = load_streamflow('June-2021-Provo-River-Streamflow-Rates.csv')
plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)
