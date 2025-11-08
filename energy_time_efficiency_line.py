import matplotlib.pyplot as plt
import numpy as np

# Data from the table
route_types = ['Urban (High)', 'Suburban', 'Highway']
base_energy = [21.5, 28.9, 35.3]
opt_energy = [14.8, 19.4, 23.2]
energy_save = [31.2, 32.9, 34.3]
time_save = [22.4, 19.6, 17.3]

# Create a single figure
fig, ax = plt.subplots(figsize=(14, 8))

# Create line plots with vibrant colors
x = np.arange(len(route_types))

ax.plot(route_types, base_energy, marker='o', linewidth=3, markersize=14, label='Base Energy (kWh)', 
        color='#e74c3c', markeredgecolor='black', markeredgewidth=1.5)
ax.plot(route_types, opt_energy, marker='s', linewidth=3, markersize=14, label='Optimized Energy (kWh)', 
        color='#2ecc71', markeredgecolor='black', markeredgewidth=1.5)
ax.plot(route_types, energy_save, marker='^', linewidth=3, markersize=14, label='Energy Save (%)', 
        color='#3498db', markeredgecolor='black', markeredgewidth=1.5)
ax.plot(route_types, time_save, marker='D', linewidth=3, markersize=14, label='Time Save (%)', 
        color='#f39c12', markeredgecolor='black', markeredgewidth=1.5)

# Customize the plot
ax.set_xlabel('Route Type', fontsize=14, fontweight='bold')
ax.set_ylabel('Metric Values', fontsize=14, fontweight='bold')
ax.set_title('Energy and Time Efficiency Comparison per Route Category', fontsize=16, fontweight='bold', pad=20)
ax.legend(fontsize=13, loc='best', framealpha=0.95, edgecolor='black', fancybox=True)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=1)

# Add value labels on all points with large fonts
for i, route in enumerate(route_types):
    # Base Energy
    ax.text(i, base_energy[i] + 1.2, f'{base_energy[i]} kWh', ha='center', va='bottom', 
            fontsize=13, fontweight='bold', color='#e74c3c', bbox=dict(boxstyle='round,pad=0.3', 
            facecolor='white', edgecolor='#e74c3c', linewidth=1.5))
    
    # Optimized Energy
    ax.text(i, opt_energy[i] - 1.5, f'{opt_energy[i]} kWh', ha='center', va='top', 
            fontsize=13, fontweight='bold', color='#2ecc71', bbox=dict(boxstyle='round,pad=0.3', 
            facecolor='white', edgecolor='#2ecc71', linewidth=1.5))
    
    # Energy Save
    ax.text(i, energy_save[i] + 0.8, f'{energy_save[i]}%', ha='center', va='bottom', 
            fontsize=13, fontweight='bold', color='#3498db', bbox=dict(boxstyle='round,pad=0.3', 
            facecolor='white', edgecolor='#3498db', linewidth=1.5))
    
    # Time Save
    ax.text(i, time_save[i] - 1.0, f'{time_save[i]}%', ha='center', va='top', 
            fontsize=13, fontweight='bold', color='#f39c12', bbox=dict(boxstyle='round,pad=0.3', 
            facecolor='white', edgecolor='#f39c12', linewidth=1.5))

# Set better y-axis limits
ax.set_ylim(10, 42)

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\9_energy_time_efficiency_line.png', dpi=300, bbox_inches='tight')
print("✓ Line Graph: Energy and Time Efficiency Comparison saved")
print("\nGraph Details:")
print("  • Base Energy (Red Line): Original energy consumption")
print("  • Optimized Energy (Green Line): Energy after optimization")
print("  • Energy Save % (Blue Line): Percentage of energy saved")
print("  • Time Save % (Orange Line): Percentage of time saved")
print("\nKey Insights:")
print("  • Urban (High): 31.2% energy savings with 22.4% time savings")
print("  • Suburban: 32.9% energy savings with 19.6% time savings")
print("  • Highway: 34.3% energy savings with 17.3% time savings")
print("  • Most efficient route type: Urban (High) - highest savings ratios")
plt.show()
