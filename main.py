from collections import Counter

# Where do you live now?
live_now = ['S', 'T', 'R', 'C', 'R', 'R', 'T', 'C', 'S', 'T', 'C', 'S', 'C', 'S', 'T',
            'S', 'S', 'C', 'S', 'S', 'T', 'T', 'C', 'C', 'S', 'T', 'C', 'S', 'T', 'C',
            'T', 'R', 'S', 'S', 'T', 'C', 'S', 'C', 'T', 'C', 'T', 'C', 'T', 'C', 'R',
            'C', 'C', 'R', 'T', 'C', 'S', 'S', 'T', 'S', 'C', 'C', 'C', 'R', 'S', 'C',
            'S', 'S', 'C', 'C', 'S', 'C', 'R', 'T', 'T', 'T', 'C', 'R', 'T', 'C', 'R',
            'C', 'T', 'R', 'R', 'C', 'T', 'C', 'C', 'R', 'T', 'T', 'R', 'S', 'R', 'T',
            'T', 'S', 'S', 'S', 'S', 'C', 'C', 'R', 'T']

# What do you consider to be the ideal community?
ideal_community = ['S', 'C', 'R', 'R', 'R', 'S', 'T', 'S', 'S', 'T', 'T', 'S', 'C', 'S', 'T',
                   'C', 'C', 'R', 'T', 'R', 'S', 'T', 'T', 'S', 'S', 'C', 'C', 'T', 'T', 'S',
                   'S', 'R', 'C', 'S', 'C', 'C', 'S', 'C', 'R', 'C', 'T', 'S', 'R', 'R', 'R',
                   'C', 'T', 'S', 'T', 'T', 'T', 'R', 'R', 'S', 'C', 'C', 'R', 'R', 'S', 'S',
                   'S', 'T', 'C', 'T', 'T', 'C', 'R', 'T', 'T', 'T', 'C', 'T', 'T', 'R', 'R',
                   'C', 'S', 'R', 'T', 'C', 'T', 'C', 'C', 'T', 'T', 'T', 'R', 'C', 'R', 'T',
                   'T', 'C', 'S', 'S', 'C', 'S', 'T', 'S', 'S', 'R']
# Count frequencies
live_now_freq = Counter(live_now)
ideal_community_freq = Counter(ideal_community)

# Calculate percent frequencies
live_now_percent = {k: v / len(live_now) * 100 for k, v in live_now_freq.items()}
ideal_community_percent = {k: v / len(ideal_community) * 100 for k, v in ideal_community_freq.items()}

print("Live Now Frequencies: ", live_now_freq)
print("Ideal Community Frequencies: ", ideal_community_freq)
print("Live Now Percent Frequencies: ", live_now_percent)
print("Ideal Community Percent Frequencies: ", ideal_community_percent)


import matplotlib.pyplot as plt

# Where do you live now?
live_now_labels, live_now_values = zip(*live_now_freq.items())

# What do you consider to be the ideal community?
ideal_community_labels, ideal_community_values = zip(*ideal_community_freq.items())

fig, axs = plt.subplots(2)

# Plot for 'Where do you live now?'
axs[0].bar(live_now_labels, live_now_values, color=['b', 'g', 'r', 'c'])
axs[0].set_title('Where do you live now?')
axs[0].set_xlabel('Community Type')
axs[0].set_ylabel('Frequency')

# Plot for 'What do you consider to be the ideal community?'
axs[1].bar(ideal_community_labels, ideal_community_values, color=['b', 'g', 'r', 'c'])
axs[1].set_title('What do you consider to be the ideal community?')
axs[1].set_xlabel('Community Type')
axs[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()