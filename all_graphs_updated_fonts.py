import matplotlib.pyplot as plt
import numpy as np

# ============= GRAPH 1: Traffic Forecasting - Orange Palette =============
fig1, ax1 = plt.subplots(figsize=(14, 7))

models = ['ARIMA', 'SVR (RBF)', 'CNN', 'LSTM (Proposed)']
mae = [6.9, 5.6, 4.9, 3.8]
rmse = [8.3, 6.8, 6.0, 4.6]
mape = [11.5, 9.7, 8.2, 4.6]
r2 = [0.78, 0.84, 0.88, 0.93]
time = [15, 42, 58, 66]

x = np.arange(len(models))
width = 0.15

colors_orange = ['#d62728', '#ff7f0e', '#ff9e1b', '#ffb347', '#ffd580']

bars1 = ax1.bar(x - 2*width, mae, width, label='MAE', color=colors_orange[0], edgecolor='black', linewidth=1.2)
bars2 = ax1.bar(x - width, rmse, width, label='RMSE', color=colors_orange[1], edgecolor='black', linewidth=1.2)
bars3 = ax1.bar(x, mape, width, label='MAPE', color=colors_orange[2], edgecolor='black', linewidth=1.2)
bars4 = ax1.bar(x + width, r2, width, label='R²', color=colors_orange[3], edgecolor='black', linewidth=1.2)
bars5 = ax1.bar(x + 2*width, [t/10 for t in time], width, label='Time (÷10s)', color=colors_orange[4], edgecolor='black', linewidth=1.2)

ax1.set_xlabel('Models', fontsize=12, fontweight='bold')
ax1.set_ylabel('Performance Metrics', fontsize=12, fontweight='bold')
ax1.set_title('Traffic Speed Forecasting Performance Comparison', fontsize=14, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(models, fontsize=11)
ax1.legend(fontsize=11, loc='upper left')
ax1.grid(axis='y', alpha=0.3, linestyle='--')

def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontsize=13, fontweight='bold')

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)
add_value_labels(bars4)
add_value_labels(bars5)

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\1_traffic_forecasting_orange.png', dpi=300, bbox_inches='tight')
print("✓ Graph 1: Traffic Forecasting (Orange) updated")
plt.close()

# ============= GRAPH 2: Route Optimization - Purple Palette =============
fig2, ax2 = plt.subplots(figsize=(12, 7))

algorithms = ['Dijkstra', 'A*', 'Ant Colony', 'GA (Proposed)']
energy = [28.6, 25.9, 22.8, 19.3]
time_min = [52.7, 49.3, 45.6, 42.3]
conv_time = [2.1, 3.4, 37.0, 29.2]
feasible = [87, 91, 93, 97]

colors_purple = ['#440154', '#31688e', '#35b779', '#fde724']

ax2.plot(algorithms, energy, marker='o', linewidth=2.5, markersize=12, label='Energy (kWh)', color=colors_purple[0])
ax2.plot(algorithms, time_min, marker='s', linewidth=2.5, markersize=12, label='Time (min)', color=colors_purple[1])
ax2.plot(algorithms, conv_time, marker='^', linewidth=2.5, markersize=12, label='Conv. Time (s)', color=colors_purple[2])
ax2.plot(algorithms, feasible, marker='D', linewidth=2.5, markersize=12, label='Feasible (%)', color=colors_purple[3])

ax2.set_xlabel('Algorithms', fontsize=12, fontweight='bold')
ax2.set_ylabel('Metric Values', fontsize=12, fontweight='bold')
ax2.set_title('Route Optimization Algorithm Comparison', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11, loc='best')
ax2.grid(True, alpha=0.3, linestyle='--')

for i, algo in enumerate(algorithms):
    ax2.text(i, energy[i] + 1.5, f'{energy[i]}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax2.text(i, time_min[i] + 1.5, f'{time_min[i]}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax2.text(i, conv_time[i] + 2, f'{conv_time[i]}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax2.text(i, feasible[i] + 1.5, f'{feasible[i]}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\2_route_optimization_line_purple.png', dpi=300, bbox_inches='tight')
print("✓ Graph 2: Route Optimization Line (Purple) updated")
plt.close()

# ============= GRAPH 3: Route Optimization - Pink Palette =============
fig3, ax3 = plt.subplots(figsize=(12, 8))

normalized_scores = []
for i in range(len(algorithms)):
    score = (energy[i] + time_min[i] + conv_time[i]) / feasible[i]
    normalized_scores.append(score)

colors_pink = ['#ff1493', '#ff69b4', '#ffb6c1', '#ffc0cb']

wedges, texts, autotexts = ax3.pie(normalized_scores, labels=algorithms, autopct='%1.1f%%', 
                                    colors=colors_pink, startangle=90, 
                                    textprops={'fontsize': 13, 'fontweight': 'bold'},
                                    explode=(0.05, 0.05, 0.05, 0.1))

ax3.set_title('Route Optimization Algorithm Comparison\n(Overall Performance Score)', 
             fontsize=14, fontweight='bold', pad=20)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(13)
    autotext.set_fontweight('bold')

for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

legend_labels = []
for i, algo in enumerate(algorithms):
    legend_labels.append(f'{algo}:\n  Energy: {energy[i]} kWh, Time: {time_min[i]} min\n  Conv. Time: {conv_time[i]}s, Feasible: {feasible[i]}%')
ax3.legend(legend_labels, loc='center left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\3_route_optimization_pie_pink.png', dpi=300, bbox_inches='tight')
print("✓ Graph 3: Route Optimization Pie (Pink) updated")
plt.close()

# ============= GRAPH 4: EV Battery and SoC - Cyan Palette =============
fig4, ax4 = plt.subplots(figsize=(12, 7))

algorithms_ev = ['Dijkstra', 'A*', 'Ant Colony', 'GA (Prop.)']
final_soc = [18.2, 20.6, 23.9, 26.7]
avg_soc_drop = [0.82, 0.73, 0.66, 0.57]
charging_stops = [3, 2, 2, 1]
avg_duration = [68, 54, 47, 41]

x_ev = np.arange(len(algorithms_ev))
width_ev = 0.2

colors_cyan = ['#00bfff', '#1e90ff', '#00ced1', '#40e0d0']

bars1_ev = ax4.bar(x_ev - 1.5*width_ev, final_soc, width_ev, label='Final SoC (%)', color=colors_cyan[0], edgecolor='black', linewidth=1.2)
bars2_ev = ax4.bar(x_ev - 0.5*width_ev, avg_soc_drop, width_ev, label='Avg. SoC Drop/km (%)', color=colors_cyan[1], edgecolor='black', linewidth=1.2)
bars3_ev = ax4.bar(x_ev + 0.5*width_ev, charging_stops, width_ev, label='Charging Stops', color=colors_cyan[2], edgecolor='black', linewidth=1.2)
bars4_ev = ax4.bar(x_ev + 1.5*width_ev, avg_duration, width_ev, label='Avg. Duration (min)', color=colors_cyan[3], edgecolor='black', linewidth=1.2)

ax4.set_xlabel('Algorithms', fontsize=12, fontweight='bold')
ax4.set_ylabel('Metric Values', fontsize=12, fontweight='bold')
ax4.set_title('EV Battery and SoC Analysis', fontsize=14, fontweight='bold')
ax4.set_xticks(x_ev)
ax4.set_xticklabels(algorithms_ev, fontsize=11)
ax4.legend(fontsize=11, loc='upper left')
ax4.grid(axis='y', alpha=0.3, linestyle='--')

def add_value_labels_ev(bars):
    for bar in bars:
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontsize=13, fontweight='bold')

add_value_labels_ev(bars1_ev)
add_value_labels_ev(bars2_ev)
add_value_labels_ev(bars3_ev)
add_value_labels_ev(bars4_ev)

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\4_ev_battery_soc_histogram_cyan.png', dpi=300, bbox_inches='tight')
print("✓ Graph 4: EV Battery and SoC (Cyan) updated")
plt.close()

# ============= GRAPH 5: GA Convergence - Red Palette =============
fig5, ax5 = plt.subplots(figsize=(12, 7))

generation = [10, 30, 50, 70, 80]
best_fitness = [0.845, 0.682, 0.581, 0.519, 0.492]
avg_fitness = [0.903, 0.713, 0.602, 0.531, 0.501]
energy_ga = [26.4, 23.7, 21.1, 19.8, 19.3]
time_ga = [50.2, 47.0, 44.2, 43.1, 42.3]

colors_red = ['#8b0000', '#dc143c', '#ff4500', '#ff6347']

ax5.plot(generation, best_fitness, marker='o', linewidth=2.5, markersize=12, label='Best Fitness', color=colors_red[0])
ax5.plot(generation, avg_fitness, marker='s', linewidth=2.5, markersize=12, label='Avg. Fitness', color=colors_red[1])
ax5.plot(generation, energy_ga, marker='^', linewidth=2.5, markersize=12, label='Energy (kWh)', color=colors_red[2])
ax5.plot(generation, time_ga, marker='D', linewidth=2.5, markersize=12, label='Time (min)', color=colors_red[3])

ax5.set_xlabel('Generation', fontsize=12, fontweight='bold')
ax5.set_ylabel('Metric Values', fontsize=12, fontweight='bold')
ax5.set_title('Genetic Algorithm Convergence Statistics', fontsize=14, fontweight='bold')
ax5.legend(fontsize=11, loc='best')
ax5.grid(True, alpha=0.3, linestyle='--')
ax5.set_xticks(generation)

for i, gen in enumerate(generation):
    ax5.text(gen, best_fitness[i] - 0.04, f'{best_fitness[i]}', ha='center', va='top', fontsize=12, fontweight='bold')
    ax5.text(gen, avg_fitness[i] + 0.03, f'{avg_fitness[i]}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax5.text(gen, energy_ga[i] + 0.5, f'{energy_ga[i]}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax5.text(gen, time_ga[i] - 0.8, f'{time_ga[i]}', ha='center', va='top', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\5_ga_convergence_line_red.png', dpi=300, bbox_inches='tight')
print("✓ Graph 5: GA Convergence Line (Red) updated")
plt.close()

# ============= GRAPH 6: GA Convergence - Teal Palette =============
fig6, ax6 = plt.subplots(figsize=(14, 7))

gen_labels = [f'Gen {g}' for g in generation]
x_ga = np.arange(len(generation))
width_ga = 0.2

colors_teal = ['#004d4d', '#008080', '#20b2aa', '#66cdaa']

bars1_ga = ax6.bar(x_ga - 1.5*width_ga, best_fitness, width_ga, label='Best Fitness', color=colors_teal[0], edgecolor='black', linewidth=1.2)
bars2_ga = ax6.bar(x_ga - 0.5*width_ga, avg_fitness, width_ga, label='Avg. Fitness', color=colors_teal[1], edgecolor='black', linewidth=1.2)
bars3_ga = ax6.bar(x_ga + 0.5*width_ga, energy_ga, width_ga, label='Energy (kWh)', color=colors_teal[2], edgecolor='black', linewidth=1.2)
bars4_ga = ax6.bar(x_ga + 1.5*width_ga, time_ga, width_ga, label='Time (min)', color=colors_teal[3], edgecolor='black', linewidth=1.2)

ax6.set_xlabel('Generation', fontsize=12, fontweight='bold')
ax6.set_ylabel('Metric Values', fontsize=12, fontweight='bold')
ax6.set_title('Genetic Algorithm Convergence Statistics', fontsize=14, fontweight='bold')
ax6.set_xticks(x_ga)
ax6.set_xticklabels(gen_labels, fontsize=11)
ax6.legend(fontsize=11, loc='upper right')
ax6.grid(axis='y', alpha=0.3, linestyle='--')

def add_value_labels_ga(bars):
    for bar in bars:
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}', ha='center', va='bottom', fontsize=13, fontweight='bold')

add_value_labels_ga(bars1_ga)
add_value_labels_ga(bars2_ga)
add_value_labels_ga(bars3_ga)
add_value_labels_ga(bars4_ga)

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\6_ga_convergence_bar_teal.png', dpi=300, bbox_inches='tight')
print("✓ Graph 6: GA Convergence Bar (Teal) updated")
plt.close()

# ============= GRAPH 7: Comprehensive Performance - Indigo/Multi-Color Palette =============
fig7, ax7 = plt.subplots(figsize=(14, 8))

algo_comp = ['Dijkstra', 'A*', 'Ant Colony', 'GA-LSTM']
avg_energy_comp = [28.6, 26.9, 22.8, 19.3]
avg_time_comp = [52.7, 49.3, 45.6, 42.3]
rmse_traffic = [6.2, 5.7, 5.2, 3.8]
final_soc_comp = [18.2, 20.6, 23.9, 26.7]
charging_stops_comp = [3, 2, 2, 1]
feasibility_comp = [87, 91, 93, 97]
improvement = [0, -6.5, 20.2, 32.4]

x_comp = np.arange(len(algo_comp))

colors_indigo = ['#4b0082', '#6a0dad', '#8a2be2', '#9370db', '#ba55d3', '#da70d6', '#ee82ee']

ax7.plot(x_comp, avg_energy_comp, marker='o', linewidth=3, markersize=14, label='Avg. Energy (kWh)', 
        color=colors_indigo[0], markeredgecolor='black', markeredgewidth=1.5)
ax7.plot(x_comp, avg_time_comp, marker='s', linewidth=3, markersize=14, label='Avg. Time (min)', 
        color=colors_indigo[1], markeredgecolor='black', markeredgewidth=1.5)
ax7.plot(x_comp, rmse_traffic, marker='^', linewidth=3, markersize=14, label='RMSE (Traffic) (km/h)', 
        color=colors_indigo[2], markeredgecolor='black', markeredgewidth=1.5)
ax7.plot(x_comp, final_soc_comp, marker='D', linewidth=3, markersize=14, label='Final SoC (%)', 
        color=colors_indigo[3], markeredgecolor='black', markeredgewidth=1.5)
ax7.plot(x_comp, charging_stops_comp, marker='*', linewidth=3, markersize=18, label='Charging Stops', 
        color=colors_indigo[4], markeredgecolor='black', markeredgewidth=1.5)
ax7.plot(x_comp, feasibility_comp, marker='P', linewidth=3, markersize=14, label='Feasibility (%)', 
        color=colors_indigo[5], markeredgecolor='black', markeredgewidth=1.5)
ax7.plot(x_comp, improvement, marker='h', linewidth=3, markersize=14, label='Improvement (%)', 
        color=colors_indigo[6], markeredgecolor='black', markeredgewidth=1.5)

ax7.set_xlabel('Algorithms', fontsize=13, fontweight='bold')
ax7.set_ylabel('Metric Values', fontsize=13, fontweight='bold')
ax7.set_title('Comprehensive Performance Summary - Detailed Comparison\nAcross All Algorithms', 
             fontsize=15, fontweight='bold', pad=20)
ax7.set_xticks(x_comp)
ax7.set_xticklabels(algo_comp, fontsize=12, fontweight='bold')
ax7.legend(fontsize=11, loc='upper left', framealpha=0.95, edgecolor='black', fancybox=True)
ax7.grid(True, alpha=0.4, linestyle='--', linewidth=0.8)

for i, algo in enumerate(algo_comp):
    ax7.text(i, avg_energy_comp[i] + 1.2, f'{avg_energy_comp[i]}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax7.text(i, avg_time_comp[i] + 1.8, f'{avg_time_comp[i]}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax7.text(i, rmse_traffic[i] - 0.7, f'{rmse_traffic[i]}', ha='center', va='top', fontsize=12, fontweight='bold')
    ax7.text(i, final_soc_comp[i] + 1.2, f'{final_soc_comp[i]}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax7.text(i, charging_stops_comp[i] + 0.2, f'{charging_stops_comp[i]}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax7.text(i, feasibility_comp[i] + 1.2, f'{feasibility_comp[i]}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
    if improvement[i] >= 0:
        ax7.text(i, improvement[i] + 2.2, f'{improvement[i]}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
    else:
        ax7.text(i, improvement[i] - 2.2, f'{improvement[i]}%', ha='center', va='top', fontsize=12, fontweight='bold')

ax7.set_ylim(-15, 115)

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\7_comprehensive_performance_line_indigo.png', dpi=300, bbox_inches='tight')
print("✓ Graph 7: Comprehensive Performance Line (Indigo) updated")
plt.close()

# ============= GRAPH 8: Comprehensive Performance - Gold/Yellow Palette =============
fig8, ax8 = plt.subplots(figsize=(16, 8))

x_hist = np.arange(len(algo_comp))
width_hist = 0.11

colors_gold = ['#b8860b', '#daa520', '#ffd700', '#ffed4e', '#ffff99', '#fffacd', '#ffffe0']

bars1_hist = ax8.bar(x_hist - 3.3*width_hist, avg_energy_comp, width_hist, label='Avg. Energy (kWh)', color=colors_gold[0], edgecolor='black', linewidth=1.2)
bars2_hist = ax8.bar(x_hist - 2.2*width_hist, avg_time_comp, width_hist, label='Avg. Time (min)', color=colors_gold[1], edgecolor='black', linewidth=1.2)
bars3_hist = ax8.bar(x_hist - 1.1*width_hist, rmse_traffic, width_hist, label='RMSE (Traffic) (km/h)', color=colors_gold[2], edgecolor='black', linewidth=1.2)
bars4_hist = ax8.bar(x_hist, final_soc_comp, width_hist, label='Final SoC (%)', color=colors_gold[3], edgecolor='black', linewidth=1.2)
bars5_hist = ax8.bar(x_hist + 1.1*width_hist, charging_stops_comp, width_hist, label='Charging Stops', color=colors_gold[4], edgecolor='black', linewidth=1.2)
bars6_hist = ax8.bar(x_hist + 2.2*width_hist, feasibility_comp, width_hist, label='Feasibility (%)', color=colors_gold[5], edgecolor='black', linewidth=1.2)
bars7_hist = ax8.bar(x_hist + 3.3*width_hist, improvement, width_hist, label='Improvement (%)', color=colors_gold[6], edgecolor='black', linewidth=1.2)

ax8.set_xlabel('Algorithms', fontsize=13, fontweight='bold')
ax8.set_ylabel('Metric Values', fontsize=13, fontweight='bold')
ax8.set_title('Comprehensive Performance Summary - Histogram Comparison', fontsize=15, fontweight='bold')
ax8.set_xticks(x_hist)
ax8.set_xticklabels(algo_comp, fontsize=12, fontweight='bold')
ax8.legend(fontsize=10, loc='upper left', framealpha=0.95, edgecolor='black', fancybox=True, ncol=2)
ax8.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.8)

def add_value_labels_hist(bars):
    for bar in bars:
        height = bar.get_height()
        if height != 0:
            ax8.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

add_value_labels_hist(bars1_hist)
add_value_labels_hist(bars2_hist)
add_value_labels_hist(bars3_hist)
add_value_labels_hist(bars4_hist)
add_value_labels_hist(bars5_hist)
add_value_labels_hist(bars6_hist)
add_value_labels_hist(bars7_hist)

ax8.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)

plt.tight_layout()
plt.savefig(r'c:\Users\HP\OneDrive\Desktop\EVcharging\8_comprehensive_performance_histogram_gold.png', dpi=300, bbox_inches='tight')
print("✓ Graph 8: Comprehensive Performance Histogram (Gold) updated")
plt.close()

print("\n" + "="*70)
print("✓ ALL GRAPHS UPDATED WITH LARGER FONT SIZES FOR DATA LABELS!")
print("="*70)
print("\nFont size improvements made:")
print("  • Data labels: Increased to 11-13 pt (from 8-9 pt)")
print("  • Pie chart labels: Increased to 12-13 pt (from 9-11 pt)")
print("  • Line chart values: Increased to 12 pt (from 9 pt)")
print("  • Bar chart values: Increased to 13 pt (from 7-8 pt)")
print("\nAll graphs are now much more readable! 🎨")
print("="*70)
