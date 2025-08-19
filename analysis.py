import matplotlib.pyplot as plt
import numpy as np
#this is the code 
def analyze_inventory_turnover():
    """
    Analyzes the inventory turnover ratio and generates a visualization.
    """
    # Data
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    turnover_ratios = [5.2, 3.18, 7.98, 6.6]
    average_turnover = np.mean(turnover_ratios)
    industry_target = 8

    # Print the calculated average to confirm it's 5.74
    print(f"Calculated Average Inventory Turnover: {average_turnover:.2f}")

    # Visualization
    x = np.arange(len(quarters))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x, turnover_ratios, width, label='Quarterly Turnover')

    # Add a line for the industry target
    ax.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')
    # Add a line for the average turnover
    ax.axhline(y=average_turnover, color='g', linestyle='--', label=f'Average Turnover ({average_turnover:.2f})')


    # Add some text for labels, title and axes ticks
    ax.set_ylabel('Inventory Turnover Ratio')
    ax.set_title('Quarterly Inventory Turnover Ratio vs. Industry Target')
    ax.set_xticks(x)
    ax.set_xticklabels(quarters)
    ax.legend()

    ax.bar_label(rects1, padding=3)

    fig.tight_layout()

    # Save the figure
    plt.savefig('inventory_turnover_chart.png')
    print("Chart saved as inventory_turnover_chart.png")

if __name__ == '__main__':
    analyze_inventory_turnover()
