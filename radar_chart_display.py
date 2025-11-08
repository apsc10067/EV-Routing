#!/usr/bin/env python3
"""
EV Optimization Algorithms - Radar Chart Visualization
Shows multi-dimensional performance comparison
"""

def display_radar_charts():
    """Display radar chart visualizations for each algorithm"""
    
    print("📡 EV OPTIMIZATION ALGORITHMS - RADAR CHART PERFORMANCE")
    print("=" * 70)
    print()
    
    algorithms = {
        "🏆 Ant Colony": {
            "cost": 100, "efficiency": 93, "speed": 85, "reliability": 90, "scalability": 88,
            "color": "🟢", "winner": True
        },
        "⚡ Dijkstra": {
            "cost": 65, "efficiency": 100, "speed": 100, "reliability": 95, "scalability": 85,
            "color": "🔴", "winner": False
        },
        "🧬 Genetic": {
            "cost": 78, "efficiency": 70, "speed": 70, "reliability": 80, "scalability": 90,
            "color": "🟡", "winner": False
        },
        "🌡️ Simulated": {
            "cost": 75, "efficiency": 72, "speed": 75, "reliability": 82, "scalability": 75,
            "color": "🟠", "winner": False
        },
        "🧠 Deep RL": {
            "cost": 60, "efficiency": 95, "speed": 50, "reliability": 85, "scalability": 95,
            "color": "🟣", "winner": False
        }
    }
    
    print("   Cost    Efficiency    Speed    Reliability  Scalability")
    print("     ↑          ↑          ↑           ↑           ↑")
    print("   100%       100%       100%        100%        100%")
    print()
    
    for name, data in algorithms.items():
        crown = " 👑" if data["winner"] else ""
        print(f"{data['color']} {name}{crown}")
        
        # Create radar visualization using text
        cost_bar = "█" * (data['cost'] // 10) + "▌" if data['cost'] % 10 >= 5 else "█" * (data['cost'] // 10)
        eff_bar = "█" * (data['efficiency'] // 10) + "▌" if data['efficiency'] % 10 >= 5 else "█" * (data['efficiency'] // 10)
        speed_bar = "█" * (data['speed'] // 10) + "▌" if data['speed'] % 10 >= 5 else "█" * (data['speed'] // 10)
        rel_bar = "█" * (data['reliability'] // 10) + "▌" if data['reliability'] % 10 >= 5 else "█" * (data['reliability'] // 10)
        scale_bar = "█" * (data['scalability'] // 10) + "▌" if data['scalability'] % 10 >= 5 else "█" * (data['scalability'] // 10)
        
        print(f"   {cost_bar:<12} {eff_bar:<12} {speed_bar:<12} {rel_bar:<12} {scale_bar:<12}")
        print(f"   {data['cost']:<12} {data['efficiency']:<12} {data['speed']:<12} {data['reliability']:<12} {data['scalability']}")
        print()
    
    print("=" * 70)
    print()
    
    # Performance pentagon for each algorithm
    print("🔷 ALGORITHM PERFORMANCE PENTAGONS")
    print("=" * 50)
    print()
    
    for name, data in algorithms.items():
        crown = " 👑" if data["winner"] else ""
        print(f"{data['color']} {name}{crown}")
        print("       Efficiency")
        print("           ↑")
        print(f"          {data['efficiency']}%")
        print("           |")
        print(f"Speed {data['speed']}% ──┼── {data['reliability']}% Reliability")
        print("           |")
        print(f"        {data['cost']}%")
        print("      Cost Efficiency")
        print(f"           |")
        print(f"       {data['scalability']}%")
        print("      Scalability")
        print()
    
    print("=" * 70)
    print("📊 MULTI-DIMENSIONAL PERFORMANCE SUMMARY")
    print("=" * 50)
    print()
    
    categories = ["Cost", "Efficiency", "Speed", "Reliability", "Scalability"]
    
    for category in categories:
        print(f"🏆 BEST {category.upper()}:")
        
        if category == "Cost":
            sorted_algos = sorted(algorithms.items(), key=lambda x: x[1]['cost'], reverse=True)
        elif category == "Efficiency":
            sorted_algos = sorted(algorithms.items(), key=lambda x: x[1]['efficiency'], reverse=True)
        elif category == "Speed":
            sorted_algos = sorted(algorithms.items(), key=lambda x: x[1]['speed'], reverse=True)
        elif category == "Reliability":
            sorted_algos = sorted(algorithms.items(), key=lambda x: x[1]['reliability'], reverse=True)
        else:  # Scalability
            sorted_algos = sorted(algorithms.items(), key=lambda x: x[1]['scalability'], reverse=True)
        
        for i, (name, data) in enumerate(sorted_algos, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            score = data[category.lower()]
            print(f"   {medal} {name:<15} {score:>3}%")
        print()
    
    print("🎯 OPTIMAL ALGORITHM SELECTION MATRIX")
    print("=" * 45)
    print()
    print("USE CASE                   → RECOMMENDED ALGORITHM")
    print("─" * 50)
    print("💰 Minimize costs          → 🏆 Ant Colony (100%)")
    print("⚡ Maximize efficiency     → ⚡ Dijkstra (100%)")
    print("🚀 Real-time performance   → ⚡ Dijkstra (100%)")
    print("🎯 High reliability        → ⚡ Dijkstra (95%)")
    print("📈 Future scalability      → 🧠 Deep RL (95%)")
    print("🔄 Multi-objective goals   → 🧬 Genetic (90%)")
    print("🎲 Explore solution space  → 🌡️ Simulated (82%)")
    print("🧠 Adaptive learning       → 🧠 Deep RL (95%)")
    print()
    print("=" * 70)
    print("✅ RADAR CHART ANALYSIS COMPLETE!")
    print("🎯 Each algorithm excels in different performance dimensions")
    print("🏆 Ant Colony provides the best balanced performance overall")
    print("=" * 70)

if __name__ == "__main__":
    display_radar_charts()