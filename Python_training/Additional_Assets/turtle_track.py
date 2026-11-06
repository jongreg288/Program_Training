import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# 1. Create a figure set exactly to 800x600 pixels
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)

# Set the background field to grass green
ax.set_facecolor('#7ec850')

# 2. Draw a racing track (grey asphalt) spanning the width
track_min_y, track_max_y = .5, 5
ax.fill_between([0, 10], track_min_y, track_max_y, color='#444444')

# 3. Draw lane dividers (dashed white lines for 7 distinct lanes)
ax.plot([0, 10], [.65, .65], color='white', linestyle='--', linewidth=2)
ax.plot([0, 10], [1.25, 1.25], color='white', linestyle='--', linewidth=2)
ax.plot([0, 10], [1.85, 1.85], color='white', linestyle='--', linewidth=2)
ax.plot([0, 10], [2.45, 2.45], color='white', linestyle='--', linewidth=2)
ax.plot([0, 10], [3.05, 3.05], color='white', linestyle='--', linewidth=2)
ax.plot([0, 10], [3.65, 3.65], color='white', linestyle='--', linewidth=2)
ax.plot([0, 10], [4.25, 4.25], color='white', linestyle='--', linewidth=2)
ax.plot([0, 10], [4.85, 4.85], color='white', linestyle='--', linewidth=2)

# Add color labels for each lane
ax.text(0, 4.5, 'Red', color='red')
ax.text(0, 3.9, 'Orange', color='orange')
ax.text(0, 3.3, 'Yellow', color='yellow')
ax.text(0, 2.7, 'Green', color='green')
ax.text(0, 2.1, 'Blue', color='blue')
ax.text(0, 1.5, 'Indigo', color='indigo')
ax.text(0, 0.9, 'Violet', color='violet')

# Draw outer solid track boundaries
ax.plot([0, 10], [track_min_y, track_min_y], color='white', linewidth=3)
ax.plot([0, 10], [track_max_y, track_max_y], color='white', linewidth=3)

# 4. Draw the checkered finish line near the right side (x = 8.5)
finish_x = 8.5
check_width = 0.15
check_height = 0.25

y_vals = np.arange(track_min_y, track_max_y, check_height)
for i, y in enumerate(y_vals):
    for col in range(2):
        x_pos = finish_x + col * check_width
        color = 'white' if (i + col) % 2 == 0 else 'black'
        ax.add_patch(Rectangle((x_pos, y), check_width, check_height, color=color, edgecolor='none'))

# 5. Add clear markers for the track limits
ax.text(finish_x + check_width, track_max_y + 0.2, 'FINISH', color='white', 
        weight='bold', fontsize=12, ha='center', 
        bbox=dict(facecolor='#d9534f', alpha=0.9, edgecolor='none', boxstyle='round,pad=0.3'))

ax.text(1.5, track_max_y + 0.2, 'START', color='white', 
        weight='bold', fontsize=12, ha='center', 
        bbox=dict(facecolor='#0275d8', alpha=0.9, edgecolor='none', boxstyle='round,pad=0.3'))

# Clean up axes so it looks like a clean graphical asset
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.5)
ax.axis('off')

# Save directly to your workspace as an 800x600 PNG
plt.savefig('turtle_track.png', bbox_inches='tight', pad_inches=0, dpi=100)
print("Saved 'turtle_track.png' successfully at exactly 800x600 pixels.")
