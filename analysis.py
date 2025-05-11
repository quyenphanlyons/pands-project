# Create tableau Iris
#====================================================================================

# Data frames.
import pandas as pd

# Create names for the columns
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Load the CSV into a DataFrame:
tableau = pd.read_csv("iris/iris.data", names=column_names)

# Visualise tableau
print(tableau)



# 1/ Program that outputs a summary of each variable to a single text file,
#====================================================================================

import numpy as np

# summary of quantitative variables using describe() 
quanti = tableau.describe().round(2)

# As for class, get the frequency of each value
distri = tableau['class'].value_counts()

# Create a file text where the outputs can be stored
with open("Iris_stats_summary.txt","w") as f:
    f.write(("Iris data set - Statistical summary\n"))
    f.write('='*50 + "\n\n")
    f.write("Statistical Description of Quantitative Variables:\n")
    f.write("-" *50 + "\n")
    f.write(quanti.to_string())
    f.write("\n\n")
    f.write("Class Distribution:\n")
    f.write("-" *50 + "\n")
    f.write(distri.to_string())
    f.write("\n")


# 2/ Program that saves a histogram of each variable to png files
#====================================================================================

from matplotlib import pyplot as plt

for column in tableau.columns:
    # Create histograms
    plt.figure()
    plt.hist(tableau[column],bins = 10, alpha = 0.5, color = 'green', edgecolor = 'black')
    # Add labels and title
    plt.xlabel(column)
    plt.ylabel('number of observations')
    plt.title(f'Histogram: {column}', fontweight='bold')
    # Save histograms to png files
    plt.savefig(f'Histogram of {column}.png')
    plt.show()


# 3/ Program that outputs a scatter plot of each pair of variables
#====================================================================================

# Seaborn visualization library
import seaborn as sns

# Create pairplot
sns.pairplot(tableau, height=2, corner=True)
# Add title
plt.suptitle('Pair Plot - Iris Dataset', y=1.02)


# 4/ Performs any other analysis you think is appropriate
#====================================================================================

# Create the pairplot, with observations grouped by class by using parameter hue='class'
sns.pairplot(tableau, hue="class", height=2, corner=True)
# Add title
plt.suptitle('Pair Plot group by class - Iris Dataset', y=1.02)


# Calculate correlation coefficients using corr()
# Correlation is calculated between 2 numeric variables
# --> only select the first 4 columns of tableau
# Using round() to round the output to 2 decimals

correlation = round(tableau.iloc[:,:4].corr(), 2)
print(correlation)


# Heatmap
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title(f"Correlation Matrix")
plt.show()


# Boxplot
for column in tableau.iloc[:,:4]:
    plt.figure()
    # 'class' on x axe and feature on y axe
    sns.boxplot(data=tableau, x = 'class', y = tableau[column], hue='class', orient='v', palette='pastel',fill=True, dodge='auto', width=0.75, gap=0.1, whis=1.5, linecolor='k')
    
    # Add labels and title
    plt.xlabel('class')
    plt.ylabel(column)
    plt.title(f'Boxplot {column} by class', fontweight='bold')

