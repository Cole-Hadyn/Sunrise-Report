import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Loading data into python
data = np.genfromtxt('2024_sunrise_times_in_conway_ar.csv', dtype= 'str', delimiter=',', skip_header=1)

print(data[0][1])
print(data, "Sunrise times during 2024 in Conway,AR")


# Load your CSV file
#df = pd.read_csv('2024_sunrise_times_in_conway_ar.csv')



# List of month names (you can adjust based on your CSV)
#months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
 #         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Function to convert HH:MM to decimal
#def to_decimal(time_str):
    #try:
      #  h, m = map(int, time_str.split(":"))
     #   return h + m / 60
    #except:
   #     return None  # or 0, depending on how you want to handle bad data

# Apply conversion to each month column
#for month in months:
 #   if month in df.columns:
  #      df[month] = df[month].apply(to_decimal)

# Optional: save the updated dataframe
#df.to_csv('converted_times.csv', index=False)








# Load your CSV file
df = pd.read_csv('converted_times.csv')
data_convert = np.genfromtxt('converted_times.csv', dtype= 'str', delimiter=',', skip_header=1)

print(data_convert, "Cleaning up the data for python use")
# List the columns for which you want to calculate the mean
columns_to_average = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  # Replace with actual column names

# Calculate the mean of each specified column
monthly_means = df[columns_to_average].mean()

# Print the results
print("Mean of each month:")
print(monthly_means)





# Load CSV data
df = pd.read_csv("month_means.csv")

# Create figure
fig, ax = plt.subplots(figsize=(4, len(df) * 0.4 + 1))  # Adjust height based on number of rows
ax.axis('off')

# Create table
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Save as image
plt.savefig("data_table_from_csv.png", bbox_inches='tight', dpi=300)
plt.show()


# Create chart of data
plt.figure(figsize=(10, 6))
monthly_means.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Sunrise for 2024 in Conway, AR (in Decimal Hours)')
plt.ylabel('Time the AM')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
