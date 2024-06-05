import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Sample data for each day of the week
dates = ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05',
         '2023-07-06', '2023-07-07']
hits = [10, 20, 15, 8, 12, 5, 18]

# Convert date strings to numpy datetime64
numpy_dates = np.array(dates, dtype='datetime64')

# Determine the weekday index for each date
weekday_indices = np.array([datetime.strptime(date, '%Y-%m-%d').weekday() for date in dates])

# Create an array to hold the hit counts for each weekday
calendar_data = np.zeros(7)
for i, idx in enumerate(weekday_indices):
    calendar_data[idx] += hits[i]

# Create a calendar plot
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow([calendar_data], cmap='Blues')

# Customize the plot
ax.set_title('Hits by Day of Week')
ax.set_xlabel('Weekday')
ax.set_ylabel('Week')
ax.set_xticks(np.arange(7))
ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

# Display the colorbar
cbar = ax.figure.colorbar(im, ax=ax, fraction=0.03, pad=0.04)
cbar.ax.set_ylabel('Hits')

# Show the plot
plt.tight_layout()
plt.show()
