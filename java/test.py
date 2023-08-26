import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
entries = [7, 12, 5, 10, 15, 18, 6, 9, 3, 14, 8, 17]

fig, ax = plt.subplots()

ax.plot(months, entries, marker='o', linestyle='-', color='b', label='Entries')

ax.set_ylim(0, 20)
ax.set_yticks(np.arange(0, 21, 5))

ax.set_xlabel('Months')
ax.set_ylabel('Number of Entries')
ax.set_title('Monthly Entries for calibration of tools')
ax.legend()
plt.show()