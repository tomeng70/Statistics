import numpy as np

# Set the parameters
mean = 40.5  # Mean of the distribution
std_dev = 1.5  # Standard deviation of the distribution
size = 30  # Number of data points to generate

# Generate the data
data = np.random.normal(mean, std_dev, size)

# write to file
filename = "data.txt"
file = open(filename, "w")
for val in data:
    file.write(str(round(val, 1)))
    file.write("\n")

file.close()
print("data saved to \"" + filename + "\"")