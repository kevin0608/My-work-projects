import matplotlib.pyplot as plt
import numpy as np

# Data
data1 = {
    "Classroom": {30: 1.5, 50: 2.5, 100: 3, 150: 4, 200: 4.5, 250: 5},
    "Cabaret": {30: 1.5, 50: 2, 100: 2.5, 150: 3, 200: 3.5, 250: 4, 300: 5},
    "Theatre": {30: 1, 50: 1.5, 100: 2.25, 150: 2.5, 200: 2.75, 250: 3, 300: 3.25, 350: 3.5},
    "Boardroom & U-Shape" : {30: 1.5, 50: 2, 100: 3, 150: 4}
}

data2 = {
    "Breakfast": {30: 1, 50: 2.5, 100: 3, 150: 3.5, 200: 4, 250: 5.5, 300: 6, 350: 6.5, 400: 7},
    "Dinner": {30: 1, 50: 2, 100: 4, 150: 4.5, 200: 6, 250: 6.5, 300: 7, 350: 7.5, 400: 8},
    "Bar": {30: 2.5, 50: 3, 100: 3, 150: 4, 200: 4, 250: 5, 300: 5, 350: 6, 400: 6},
    "Beverage": {30: 0.5, 50: 0.5, 100: 1, 150: 1, 200: 1.5, 250: 1.5, 300: 1.5, 350: 2, 400: 2},
    "Mezzanine": {30: 1.5, 50: 1.5, 100: 1.5, 150: 2, 200: 2, 250: 2.5, 300: 3, 350: 3.5, 400: 3.5},
    "Stage & Closing Partition": {30: 0.5, 50: 0.5, 100: 0.5, 150: 0.5, 200: 0.5, 250: 0.5, 300: 0.5, 350: 0.5, 400: 0.5},
    "Dance Floor": {30: 1, 50: 1, 100: 1, 150: 1, 200: 1, 250: 1, 300: 1, 350: 1, 400: 1}
}

# Extract all unique pax values
pax_values = sorted({pax for data in data1.values() for pax in data})

# Set up the figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 8))

# Create bar width
bar_width = 0.20
bar_width2 = 0.13
gap_width = 0
gap_width = 0.5
print(len(data1) + len(data2))

# Generate a list of unique colors
colors = plt.cm.tab20(np.linspace(0, 1, len(data1) + len(data2)))

# Plot data1
for i, (category, data) in enumerate(data1.items()):
    hours = {data.get(pax, 0)}