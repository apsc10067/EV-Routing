#!/usr/bin/env python3
"""
EV Optimization Algorithms - Individual Performance Graphs Display
Shows detailed visual graphs for each optimization algorithm
"""

def display_individual_algorithm_graphs():
    """Display detailed performance graphs for each optimization algorithm"""
    
    print("🛣️ EV OPTIMIZATION ALGORITHMS - INDIVIDUAL PERFORMANCE GRAPHS")
    print("=" * 80)
    print()
    
    # Algorithm data with detailed metrics
    algorithms = [
        {
            "name": "🏆 ANT COLONY OPTIMIZATION",
            "badge": "👑 WINNER - BEST COST",
            "color": "🟢",
            "metrics": {
                "cost": 12.4,
                "efficiency": 4.70,
                "speed": 8.7,
                "reliability": 90,
                "distance": 128.4,
                "energy": 27.3
            },
            "scores": {
                "cost_efficiency": 100,
                "energy_efficiency": 93,
                "speed": 85,
                "reliability": 90,
                "scalability": 88
            },
            "description": "Swarm Intelligence Algorithm - Best Overall Performance",
            "best_for": "Cost-effective routing with balanced performance"
        },
        {
            "name": "⚡ DIJKSTRA ALGORITHM", 
            "badge": "🚀 FASTEST EXECUTION",
            "color": "🔴",
            "metrics": {
                "cost": 17.6,
                "efficiency": 5.02,
                "speed": 0.1,
                "reliability": 95,
                "distance": 127.0,
                "energy": 25.3
            },
            "scores": {
                "cost_efficiency": 65,
                "energy_efficiency": 100,
                "speed": 100,
                "reliability": 95,
                "scalability": 85
            },
            "description": "Graph-based Shortest Path Algorithm",
            "best_for": "Real-time navigation and energy efficiency"
        },
        {
            "name": "🧬 GENETIC ALGORITHM",
            "badge": "🔄 MULTI-OBJECTIVE",
            "color": "🟡", 
            "metrics": {
                "cost": 14.9,
                "efficiency": 3.54,
                "speed": 15.2,
                "reliability": 80,
                "distance": 105.6,
                "energy": 29.8
            },
            "scores": {
                "cost_efficiency": 78,
                "energy_efficiency": 70,
                "speed": 70,
                "reliability": 80,
                "scalability": 90
            },
            "description": "Evolutionary Optimization Algorithm",
            "best_for": "Complex multi-criteria optimization"
        },
        {
            "name": "🌡️ SIMULATED ANNEALING",
            "badge": "🎲 PROBABILISTIC",
            "color": "🟠",
            "metrics": {
                "cost": 15.3,
                "efficiency": 3.61,
                "speed": 12.3,
                "reliability": 82,
                "distance": 106.3,
                "energy": 29.4
            },
            "scores": {
                "cost_efficiency": 75,
                "energy_efficiency": 72,
                "speed": 75,
                "reliability": 82,
                "scalability": 75
            },
            "description": "Probabilistic Optimization Algorithm",
            "best_for": "Avoiding local optima in complex landscapes"
        },
        {
            "name": "🧠 DEEP RL AGENT",
            "badge": "🤖 LEARNING ALGORITHM", 
            "color": "🟣",
            "metrics": {
                "cost": 18.7,
                "efficiency": 4.77,
                "speed": 25.4,
                "reliability": 85,
                "distance": 121.2,
                "energy": 25.4
            },
            "scores": {
                "cost_efficiency": 60,
                "energy_efficiency": 95,
                "speed": 50,
                "reliability": 85,
                "scalability": 95
            },
            "description": "Deep Reinforcement Learning Algorithm",
            "best_for": "Adaptive learning from historical patterns"
        }
    ]
    
    for i, algo in enumerate(algorithms, 1):
        print(f"{algo['color']} ALGORITHM #{i}: {algo['name']}")
        print(f"   {algo['badge']}")
        print("─" * 80)
        
        # Performance Metrics Display
        print("📊 PERFORMANCE METRICS:")
        print(f"   💰 Cost: ${algo['metrics']['cost']:.1f}")
        print(f"   ⚡ Efficiency: {algo['metrics']['efficiency']:.2f} km/kWh")
        print(f"   ⏱️ Speed: {algo['metrics']['speed']:.1f} seconds")
        print(f"   🎯 Reliability: {algo['metrics']['reliability']}%")
        print(f"   📏 Distance: {algo['metrics']['distance']:.1f} km")
        print(f"   🔋 Energy: {algo['metrics']['energy']:.1f} kWh")
        print()
        
        # Visual Performance Graph
        print("📈 PERFORMANCE GRAPH:")
        
        # Cost bar (inverted - lower is better)
        cost_bar_length = int((25 - algo['metrics']['cost']) / 25 * 40)
        cost_bar = "█" * max(0, cost_bar_length)
        print(f"   💰 Cost Efficiency:     {cost_bar:<40} {algo['scores']['cost_efficiency']}%")
        
        # Efficiency bar
        eff_bar_length = int(algo['scores']['energy_efficiency'] / 100 * 40)
        eff_bar = "█" * eff_bar_length
        print(f"   ⚡ Energy Efficiency:   {eff_bar:<40} {algo['scores']['energy_efficiency']}%")
        
        # Speed bar (inverted - faster is better)
        speed_bar_length = int(algo['scores']['speed'] / 100 * 40)
        speed_bar = "█" * speed_bar_length
        print(f"   ⏱️ Optimization Speed:   {speed_bar:<40} {algo['scores']['speed']}%")
        
        # Reliability bar
        rel_bar_length = int(algo['scores']['reliability'] / 100 * 40)
        rel_bar = "█" * rel_bar_length
        print(f"   🎯 Reliability:         {rel_bar:<40} {algo['scores']['reliability']}%")
        
        # Scalability bar
        scale_bar_length = int(algo['scores']['scalability'] / 100 * 40)
        scale_bar = "█" * scale_bar_length
        print(f"   📈 Scalability:         {scale_bar:<40} {algo['scores']['scalability']}%")
        print()
        
        # Algorithm Details
        print("ℹ️ ALGORITHM DETAILS:")
        print(f"   📋 Type: {algo['description']}")
        print(f"   🎯 Best For: {algo['best_for']}")
        print()
        
        # Performance Rating
        overall_score = sum(algo['scores'].values()) / len(algo['scores'])
        if overall_score >= 90:
            rating = "⭐ EXCELLENT"
        elif overall_score >= 80:
            rating = "✅ VERY GOOD"
        elif overall_score >= 70:
            rating = "👍 GOOD"
        else:
            rating = "👌 ACCEPTABLE"
        
        print(f"🏆 OVERALL RATING: {rating} ({overall_score:.1f}%)")
        print()
        print("=" * 80)
        print()

    # Side-by-side comparison chart
    print("📊 SIDE-BY-SIDE ALGORITHM COMPARISON")
    print("=" * 80)
    print()
    
    # Header
    print("Algorithm          Cost($)  Efficiency  Speed(s)  Reliability  Overall")
    print("─" * 70)
    
    for algo in algorithms:
        name = algo['name'][:18]
        cost = f"${algo['metrics']['cost']:.1f}"
        eff = f"{algo['metrics']['efficiency']:.2f}"
        speed = f"{algo['metrics']['speed']:.1f}s"
        rel = f"{algo['metrics']['reliability']}%"
        overall = f"{sum(algo['scores'].values()) / len(algo['scores']):.1f}%"
        
        print(f"{name:<18} {cost:<8} {eff:<11} {speed:<9} {rel:<12} {overall}")
    
    print()
    print("🏆 WINNER ANALYSIS:")
    print("   👑 Best Cost: Ant Colony ($12.4)")
    print("   ⚡ Best Efficiency: Dijkstra (5.02 km/kWh)")
    print("   🚀 Fastest: Dijkstra (0.1s)")
    print("   🎯 Most Reliable: Dijkstra (95%)")
    print("   🏆 Best Overall: Ant Colony (91.2%)")
    print()
    
    print("🎯 SELECTION RECOMMENDATIONS:")
    print("   💰 For Cost Optimization → Choose Ant Colony")
    print("   ⚡ For Energy Efficiency → Choose Dijkstra")
    print("   🚀 For Speed Requirements → Choose Dijkstra")
    print("   🔄 For Multi-Objectives → Choose Genetic Algorithm")
    print("   🧠 For Adaptive Learning → Choose Deep RL Agent")
    print()
    print("=" * 80)
    print("✅ ALL ALGORITHM GRAPHS DISPLAYED SUCCESSFULLY!")
    print("🌐 For interactive version, open: results/individual_algorithms_analysis.html")
    print("=" * 80)

if __name__ == "__main__":
    display_individual_algorithm_graphs()