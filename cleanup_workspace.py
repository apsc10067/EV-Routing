import os
import shutil
from pathlib import Path

# Define paths
workspace = Path(r'c:\Users\HP\OneDrive\Desktop\EVcharging')

# Files to keep
keep_files = {
    # Graph generation scripts (main)
    'all_graphs_updated_fonts.py',
    'energy_time_efficiency_line.py',
    
    # Core system files
    'eco_routing_system.py',
    'EV_Eco_Routing_Demo.ipynb',
    
    # Data and documentation
    'EVcharging.csv',
    'ev_algorithm_analysis.json',
    'ev_dashboard.html',
    'README.md',
    'requirements.txt',
    
    # Generated graphs (the final ones)
    '1_traffic_forecasting_orange.png',
    '2_route_optimization_line_purple.png',
    '3_route_optimization_pie_pink.png',
    '4_ev_battery_soc_histogram_cyan.png',
    '5_ga_convergence_line_red.png',
    '6_ga_convergence_bar_teal.png',
    '7_comprehensive_performance_line_indigo.png',
    '8_comprehensive_performance_histogram_gold.png',
    '9_energy_time_efficiency_line.png',
}

# Files to delete (temporary, old versions, demos)
delete_patterns = [
    'ascii_graphs.py',
    'corrected_demo.py',
    'demo_eco_routing.py',
    'enhanced_demo.py',
    'ev_battery_soc_histogram.py',
    'ev_battery_soc_line_chart.py',
    'ga_convergence_bar_graph.py',
    'ga_convergence_line_graph.py',
    'ga_convergence_pie_chart.py',
    'launcher.py',
    'light_colors_demo.py',
    'lstm_loss_curves.py',
    'matplotlib_simple.py',
    'python_graphs.py',
    'route_optimization_line_graph.py',
    'route_optimization_pie_chart.py',
    'route_optimization_single_pie.py',
    'simple_python_graphs.py',
    'traffic_forecasting_comparison.py',
    'traffic_forecasting_single_graph.py',
    'weekly_traffic_patterns.py',
    'all_graphs_different_colors.py',
    'all_graphs_green_tone.py',
    'comprehensive_performance_histogram.py',
    'comprehensive_performance_line_chart.py',
    'traffic_forecasting_green.png',
    'route_optimization_line_green.png',
    'route_optimization_pie_green.png',
    'ev_battery_soc_histogram_green.png',
    'ga_convergence_line_green.png',
    'ga_convergence_bar_green.png',
    'comprehensive_performance_line_green.png',
    'comprehensive_performance_histogram_green.png',
    # Old temporary graphs
    'comprehensive.png',
    'corrected_distance_matrix.png',
    'corrected_traffic_patterns.png',
    'distance_matrix.png',
    'eco_routing_demo_results.png',
    'friday_traffic_pattern.png',
    'ga_convergence_statistics_line_graph.png',
    'genetic algo.png',
    'light_distance_matrix.png',
    'lstm_training_curves_light.png',
    'Rout Optimisation.png',
    'sunday_traffic_pattern.png',
    'table.png',
    'TRAFFICSPEEDFORECASTINGPERFORMANCECOMPARISON.png',
    'traffic_patterns.png',
    'tuesday_traffic_pattern.png',
    'weekly_traffic_comparison.png',
    'EV battery.png',
]

# Delete unnecessary files
deleted_count = 0
for file in delete_patterns:
    filepath = workspace / file
    if filepath.exists():
        try:
            filepath.unlink()
            print(f"✓ Deleted: {file}")
            deleted_count += 1
        except Exception as e:
            print(f"✗ Failed to delete {file}: {e}")

print(f"\n{'='*60}")
print(f"Total files deleted: {deleted_count}")
print(f"{'='*60}\n")

# List remaining files
print("Remaining files in workspace:")
print("-" * 60)

py_files = list(workspace.glob('*.py'))
notebook_files = list(workspace.glob('*.ipynb'))
data_files = list(workspace.glob('*.csv')) + list(workspace.glob('*.json'))
doc_files = list(workspace.glob('*.md')) + list(workspace.glob('*.txt'))
graph_files = list(workspace.glob('*.png'))
html_files = list(workspace.glob('*.html'))

if py_files:
    print("\n📄 Python Scripts:")
    for f in sorted(py_files):
        print(f"  • {f.name}")

if notebook_files:
    print("\n📓 Jupyter Notebooks:")
    for f in sorted(notebook_files):
        print(f"  • {f.name}")

if data_files:
    print("\n📊 Data Files:")
    for f in sorted(data_files):
        print(f"  • {f.name}")

if doc_files:
    print("\n📝 Documentation:")
    for f in sorted(doc_files):
        print(f"  • {f.name}")

if html_files:
    print("\n🌐 Web Files:")
    for f in sorted(html_files):
        print(f"  • {f.name}")

if graph_files:
    print("\n📈 Generated Graphs:")
    for f in sorted(graph_files):
        print(f"  • {f.name}")

print("\n" + "="*60)
print("✓ CLEANUP COMPLETE - READY FOR GITHUB!")
print("="*60)
