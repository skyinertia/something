import statistics as stats
import matplotlib.pyplot as plt
import os

# DATA GOES HERE
uniform_size = [38, 40, 38, 39, 40, 41, 38]
shoe_size = [24, 25, 24.5, 26, 25.5, 24, 24.5]
height = [160.2, 162.5, 158.4, 163.0, 161.7]
weight = [55.5, 58.0, 52.4, 60.2, 56.9]

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Calculate Stats
def calc_stats(data, label):
    print(f"\n{label.upper()} STATISTICS:")
    data_sorted = sorted(data)
    mean = round(stats.mean(data), 2)
    median = round(stats.median(data), 2)
    try:
        mode = stats.mode(data)
    except stats.StatisticsError:
        mode = "No mode found"
    data_range = round(max(data) - min(data), 2)
    q1 = round(stats.quantiles(data, n=4)[0], 2)
    q2 = round(stats.median(data), 2)
    q3 = round(stats.quantiles(data, n=4)[2], 2)
    iqr = round(q3 - q1, 2)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Range: {data_range}")
    print(f"Min: {min(data)}")
    print(f"Max: {max(data)}")
    print(f"Q1: {q1}")
    print(f"Q2 (Median): {q2}")
    print(f"Q3: {q3}")
    print(f"IQR: {iqr}")

# Graph Creation
def draw_graphs(data, label):
    plt.figure(figsize=(12, 4))
    
    # Line diagram
    plt.subplot(1, 3, 1)
    plt.plot(data, marker='o')
    plt.title(f'{label} Line Diagram')
    plt.xlabel('Index')
    plt.ylabel(label)

    # Bar diagram
    plt.subplot(1, 3, 2)
    plt.bar(range(len(data)), data)
    plt.title(f'{label} Bar Diagram')
    plt.xlabel('Index')
    plt.ylabel(label)

    # Pie chart
    plt.subplot(1, 3, 3)
    countz = {}
    for item in data:
        countz[item] = countz.get(item, 0) + 1
    plt.pie(countz.values(), labels=[str(k) for k in countz.keys()], autopct='%1.1f%%')
    plt.title(f'{label} Pie Chart')

    plt.tight_layout()

    # Save all to user Desktop
    filename = f"{label.replace(' ', '_')}_graphs.png"
    save_path = os.path.join(desktop_path, filename)
    plt.savefig(save_path)
    plt.close()
    print(f"saved graph to: {save_path}")

datasets = {
    "Uniform Size": uniform_size,
    "Shoe Size": shoe_size,
    "Height": height,
    "Weight": weight
}

for label, data in datasets.items():
    calc_stats(data, label)

answer = input("Would you like to draw and save graphs to Desktop? (y/n): ") or "n"

if answer.lower() == "y":
    for label, data in datasets.items():
        draw_graphs(data, label)
else:
    input("Press enter to exit...")
