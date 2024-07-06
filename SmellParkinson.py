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

# iterate  the number of trials.
for i in range (0, NUM_TRIALS):
    # reset the number of correct answers for the current trial.
    correct = 0

    # iterate the number of guesses per trial. 
    for j in range (0, NUM_GUESSES):
        # "flip a coin" several times to determine randomly if our guess is correct or not.
        val = rng.integers(0, 100)
        if (val < 50):
            # for our simulation, any value from 0 to 49 means the guess was correct.
            # for values greater than 49, the guess was incorrect.
            correct = correct + 1
    
    # record how many correct answers we had for the current trial.
    trials[i] = correct

# use the unique() function to generate a list of unique answers in our data.
# also generate a corresponding list of counts for each unique answer in our data
# (i.e., how many times each unique answer appears in our data).
values, counts = np.unique(trials, return_counts=True)

# Draw dot plot with appropriate figure size, marker size and y-axis limits
fig, ax = plt.subplots(figsize=(6, 2.25))
for value, count in zip(values, counts):
    ax.plot([value]*count, list(range(count)), 'co', ms=10, linestyle='')
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.yaxis.set_visible(False)
ax.set_ylim(-1, max(counts))
ax.set_xticks(range(0, NUM_GUESSES + 1))
ax.tick_params(axis='x', length=0, pad=8, labelsize=12)

plt.show()