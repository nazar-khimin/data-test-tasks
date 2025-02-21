# Sprint 11. Data Visualization and Exploration
---

## Note for Contributors

To ensure the correct functionality of GitHub workflows when working with plotting tasks, **always include a call to `plt.close()` immediately after displaying a plot** using `plt.show()` in your code. This prevents figures from lingering in memory, which can cause errors during automated testing in CI/CD environments like GitHub Actions.

For example:
```python
import matplotlib.pyplot as plt

def example_plot():
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Example Plot")
    plt.show()
    plt.close()  # Ensure the figure is closed after showing it
```

Adding `plt.close()` is crucial for:
1. Freeing up memory by closing the plot once it is displayed.
2. Preventing conflicts in automated workflows that test plotting functions.
3. Maintaining consistency between local and remote test environments.

Please adhere to this practice for all plotting-related tasks to avoid issues during testing and workflow execution.

---

### **Task 1: Importance of Data Visualization in Data Science and Analytics**

Demonstrate the importance of data visualization by creating a simple bar chart to represent the frequency of categorical data.
- **Details:** 
  - You will generate a dataset of categorical values ('A', 'B', 'C') using random sampling.
  - Use Matplotlib to plot a bar chart showing the frequency of each category.
- **Requirements:**
  - The plot should have clear labels for the x-axis (Category) and y-axis (Frequency).
  - The chart must include a title that reflects the content being visualized.
  - Ensure the chart is easy to interpret, with distinct colors for the bars.

### **Task 2: Key Principles of Effective Data Visualization**
Apply key principles of effective data visualization—clarity, simplicity, and accuracy—by creating a scatter plot using Seaborn.
- **Details:**
  - Use Seaborn to create a scatter plot of two variables ('x' and 'y') from a given dataset.
  - Focus on ensuring the visualization is clear and easy to understand.
  - Include gridlines, appropriate axis labels, and a descriptive title to enhance the clarity of the plot.
- **Requirements:**
  - The scatter plot should clearly display the relationship between the two variables.
  - Use Seaborn’s built-in styling to maintain simplicity and enhance readability.
  - The visualization should avoid unnecessary elements that could clutter the plot.

### **Task 3: Plotting Different Types of Data with Matplotlib**
Explore how to visualize 1D, 2D, and 3D data using Matplotlib, demonstrating the flexibility of the library in handling various data dimensions.
- **Details:**
  - Create a 1D line plot for a sequence of values.
  - Create a 2D scatter plot to show the relationship between two variables.
  - Create a 3D scatter plot using Matplotlib's `Axes3D` to represent three-dimensional data points.
- **Requirements:**
  - Each plot must include appropriate axis labels and a title that reflects the nature of the data being visualized.
  - For 3D plots, ensure that the axes are labeled to clearly indicate what each dimension represents.
  - Demonstrate proper use of Matplotlib's plotting capabilities for different types of data.

### **Task 4: Exploratory Data Analysis (EDA) Techniques**
Conduct a comprehensive EDA on a dataset, covering descriptive statistics, outlier detection, and correlation analysis, to summarize key characteristics of the data.
- **Details:**
  - Perform descriptive statistics to calculate measures such as mean, median, mode, variance, etc.
  - Use box plots to identify outliers in the dataset and visually assess data distribution.
  - Generate a correlation matrix and visualize it with a heatmap to analyze relationships between variables.
- **Requirements:**
  - Descriptive statistics should be presented clearly in a table format.
  - The box plot must visually represent potential outliers.
  - The heatmap of the correlation matrix should include annotations to show correlation coefficients.
  - Provide an explanation of the findings from each EDA step.

### **Task 5: Creating Interactive Plots with Plotly and Bokeh**
Create interactive visualizations using Plotly to enhance the data exploration process and illustrate the benefits of interactive plots.
- **Details:**
  - Use Plotly to create an interactive scatter plot that allows for dynamic exploration of the data points (e.g., zooming, panning, hovering for details).
- **Requirements:**
  - The Plotly scatter plot should include a legend, axis labels, and a title.
  - The plot should be embedded directly into the web environment to showcase interactivity.

These detailed problem definitions set clear objectives and guidelines for each task, ensuring that students understand the purpose and expected outcomes of their visualizations while practicing essential data visualization and exploration skills.
