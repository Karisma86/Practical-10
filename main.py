import math

# Function to calculate the mean
def calc_mean(data):
    return sum(data) / len(data)

# Function to calculate the variance
def calc_variance(data):
    mean = calc_mean(data)
    temp = 0
    for value in data:
        temp += (value - mean) ** 2
    return temp / len(data)

# Function to calculate the standard deviation
def calc_std_dev(data):
    return math.sqrt(calc_variance(data))

# Function to calculate the frequency of each value in the dataset
def calc_frequency(data):
    frequency = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    return frequency

# Collect dataset from user input
data = []
print("Program To Calculate Frequency, Standard Deviation, Variance")
while True:
    value = input("Supply a value (type or 'x' to stop): ")
    if value.lower() == 'x':
        break
    data.append(float(value))

# Calculate and display results
mean = calc_mean(data)
variance = calc_variance(data)
std_dev = calc_std_dev(data)
frequency = calc_frequency(data)

print("")
print("Frequency:")
for value, count in frequency.items():
    print(f"{value}: {count}")
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

