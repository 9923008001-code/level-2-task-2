import pandas as pd
import plotly.express as px

# 1️⃣ Ask for CSV file path
file = input("Enter CSV file path (example: data.csv): ")

try:
    data = pd.read_csv(file)
    print("CSV Loaded Successfully!")
    print("\nPreview of your data:")
    print(data.head())
except Exception as e:
    print("Error loading CSV:", e)
    exit()

# 2️⃣ Choose Plot Type
plot_type = input("\nChoose plot type (scatter/bar/line/histogram): ").lower()

# 3️⃣ Select Columns
if plot_type in ['scatter', 'bar', 'line']:
    print(f"\nAvailable columns: {list(data.columns)}")
    x_col = input("Select X-axis column: ")
    y_col = input("Select Y-axis column: ")
elif plot_type == 'histogram':
    print(f"\nAvailable columns: {list(data.columns)}")
    x_col = input("Select column to plot histogram: ")
    y_col = None
else:
    print("Invalid plot type!")
    exit()

# 4️⃣ Create Plot
if plot_type == 'scatter':
    fig = px.scatter(data, x=x_col, y=y_col, title=f"Scatter Plot of {y_col} vs {x_col}")
elif plot_type == 'bar':
    fig = px.bar(data, x=x_col, y=y_col, title=f"Bar Chart of {y_col} vs {x_col}")
elif plot_type == 'line':
    fig = px.line(data, x=x_col, y=y_col, title=f"Line Chart of {y_col} vs {x_col}")
elif plot_type == 'histogram':
    fig = px.histogram(data, x=x_col, nbins=30, title=f"Histogram of {x_col}")

# 5️⃣ Show Plot
fig.show()

# 6️⃣ Save Plot
html_file = f"{plot_type}_plot.html"
png_file = f"{plot_type}_plot.png"

try:
    fig.write_html(html_file)
    fig.write_image(png_file)
    print(f"\n✅ Plot saved as {html_file} (interactive) and {png_file} (image).")
except Exception as e:
    print("\n⚠ Could not save PNG (requires kaleido):", e)
    print("Plot is still visible in browser.")