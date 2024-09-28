import numpy as np
import random
import matplotlib.pyplot as plt

# how many samples do we want in our distribution
NUM_SAMPLES = 1000000

# create and initialize a list of results for our trials.
distribution = [0] * NUM_SAMPLES

# iterate the number of trials.
for i in range (0, NUM_SAMPLES):
    # reset the number of correct answers for the current trial.
    correct = 0

    # get random value from 0 up to but not including 4.
    val = random.uniform(0,4)

    # round to 3 digits
    val = round(val, 3)
    #print(f"{val}")

    # record value to list.
    distribution[i] = val

# use the unique() function to generate a list of unique (distinct) values in our data.
# also generate a corresponding list of counts for each distinct answer in our data
# (i.e., how many times each distinct answer appears in our data).
values, counts = np.unique(distribution, return_counts=True)

# we will plot a circular dot for each instance that a distinct answer occurs in our data.
# first set size of our plot to be 6" wide by 2.25" tall
fig, ax = plt.subplots(figsize=(6, 2.25))

# iterate through the distinct answers in our data.
# value is the current distinct answer from our data.
# count is how many times this distinct answer appears in our data.
for value, count in zip(values, counts):
    # create a list of our current distinct answer.
    answers = [value]*count

    # create a sequence of values to match each instance of our current unique answer.
    # for example, if the answer of "4" appears 3 times in our data, then create a list of [0, 1, 2].
    # this list will be used to plot the dots for the current unique answer, one on top of another.
    y_values = list(range(count))

    # use answers as the x values for our dot plot.
    # use y_values as the corresponding y values each distinct answer in our data set.
    # 'bo' tells pyplot to use blue circular markers.
    # ms tells pyplot to use a marker size of 5.
    # don't have any visible lines connecting the markers (set linestyle to blank).
    ax.plot(answers, y_values, 'b+', ms=5, linestyle='')

# hide the top, right, and left spines of our graph.
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.yaxis.set_visible(False)

# set the y axis view limits
ax.set_ylim(-1, max(counts))

# set the ticks along the x axis.
ax.set_xticks(range(0, 5))
ax.tick_params(axis='x', length=0, pad=8, labelsize=12)

# set the title and x axis label.
ax.set_title(f"Random Number Generator (n = {NUM_SAMPLES})")
ax.set_xlabel(f"Value")

# adjust bottom so the xlabel does not get cut off.
plt.subplots_adjust(bottom=0.30)

# show the plot
plt.show()