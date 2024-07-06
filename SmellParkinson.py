import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2

# create a random number generator
rng = np.random.default_rng()

# how many "experiments" or trials do we want to conduct.
NUM_TRIALS = 20 

# how many guesses per trial.
NUM_GUESSES = 12

# create and initialize a list of results for our trials.
trials = [0] * NUM_TRIALS

# iterate the number of trials.
for i in range (0, NUM_TRIALS):
    # reset the number of correct answers for the current trial.
    correct = 0

    # iterate the number of guesses per trial. 
    for j in range (0, NUM_GUESSES):
        # "flip a coin" to determine randomly if our guess is correct or not.
        val = rng.integers(0, 100)
        if (val < 50):
            # for our simulation, any value from 0 to 49 means the guess was correct.
            # for values greater than 49, the guess was incorrect.
            correct = correct + 1
    
    # record how many correct answers we had for the current trial.
    trials[i] = correct

# use the unique() function to generate a list of unique (distinct) values in our data.
# also generate a corresponding list of counts for each distinct answer in our data
# (i.e., how many times each distinct answer appears in our data).
values, counts = np.unique(trials, return_counts=True)

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
    # ms tells pyplot to use a marker size of 10.
    # don't have any visible lines connecting the markers (set linestyle to blank).
    ax.plot(answers, y_values, 'bo', ms=10, linestyle='')

# hide the top, right, and left spines of our graph.
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.yaxis.set_visible(False)

# set the y axis view limits
ax.set_ylim(-1, max(counts))

# set the ticks along the x axis.
ax.set_xticks(range(0, NUM_GUESSES + 1))
ax.tick_params(axis='x', length=0, pad=8, labelsize=12)

# set the title and x axis label.
ax.set_title("Smelling Parkinson's Simulated Trials")
ax.set_xlabel(f"Number of Correct Guesses (out of {NUM_GUESSES})")

# adjust bottom so the xlabel does not get cut off.
plt.subplots_adjust(bottom=0.30)

# show the plot
plt.show()