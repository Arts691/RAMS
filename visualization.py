import matplotlib.pyplot as plt
from operations import get_all_roads

def visualize_conditions():
    roads = get_all_roads()
    names = [road[1] for road in roads]
    conditions = [road[3] for road in roads]
    
    # Count condition frequencies
    condition_counts = {cond: conditions.count(cond) for cond in set(conditions)}
    
    plt.bar(condition_counts.keys(), condition_counts.values())
    plt.xlabel('Condition')
    plt.ylabel('Number of Roads')
    plt.title('Distribution of Road Conditions')
    plt.show()
