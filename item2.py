import numpy as np

# Waiting times data
data = np.array([2, 5, 10, 12, 4, 4, 5, 17, 11, 8, 9, 8, 12, 21, 6, 8, 7, 13, 18, 3])

# Define the classes
bins = np.arange(0, max(data) + 5, 5)

# Frequency distribution
freq_dist = np.histogram(data, bins)[0]

# Relative frequency distribution
rel_freq_dist = freq_dist / len(data)

# Cumulative frequency distribution
cum_freq_dist = np.cumsum(freq_dist)

# Cumulative relative frequency distribution
cum_rel_freq_dist = cum_freq_dist / len(data)

# Proportion of customers who wait 9 minutes or less
prop_9_or_less = cum_rel_freq_dist[bins[:-1] <= 9][-1]

print("Frequency Distribution: ", freq_dist)
print("Relative Frequency Distribution: ", rel_freq_dist)
print("Cumulative Frequency Distribution: ", cum_freq_dist)
print("Cumulative Relative Frequency Distribution: ", cum_rel_freq_dist)
print("Proportion of Customers Who Wait 9 Minutes or Less: ", prop_9_or_less)

# In this code, we first define the classes using the np.arange function. We then use the np.histogram function to
# calculate the frequency distribution. The relative frequency distribution is calculated by dividing the frequency
# distribution by the total number of data points. The cumulative frequency and cumulative relative frequency
# distributions are calculated using the np.cumsum function, which returns the cumulative sum of the elements along a
# given axis. Finally, we calculate the proportion of customers who wait 9 minutes or less by finding the last value
# in the cumulative relative frequency distribution where the bin value is less than or equal to 9.
