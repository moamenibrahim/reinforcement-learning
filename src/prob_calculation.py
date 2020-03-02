import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from prob_function import probability

bin_x = 0
bin_y = 0

starting_position_x = -5
starting_position_y = -5

plt.scatter(bin_x, bin_y, label="Bin")
plt.scatter(starting_position_x, starting_position_y, label="A")
plt.ylim([-10, 10])
plt.xlim([-10, 10])
plt.grid()
plt.legend()
plt.show()

bin_x = 0
bin_y = 0

starting_position_x = -5
starting_position_y = -5

test_1 = probability(bin_x, bin_y, starting_position_x,
                     starting_position_y, 50)
test_2 = probability(bin_x, bin_y, starting_position_x,
                     starting_position_y, 60)

print("Probability of first throw at 50 degrees = ", np.round(test_1, 4))
print("Probability of second throw at 60 degress = ", np.round(test_2, 4))


bin_x = 0
bin_y = 0
throw_direction = 180

prob_table = pd.DataFrame()
for i in range(0, 20):
    state_x = -10 + i
    for j in range(0, 20):
        state_y = -10 + j
        prob = pd.DataFrame({'x': state_x, 'y': state_y, 'prob': probability(
            bin_x, bin_y, state_x, state_y, throw_direction)}, index=[0])
        prob_table = prob_table.append(prob)
prob_table = prob_table.reset_index()

plt.scatter(prob_table['x'], prob_table['y'],
            s=prob_table['prob']*400, alpha=0.5)
plt.ylim([-10, 10])
plt.xlim([-10, 10])
plt.grid()
plt.title("Probability of Landing Shot for a given Thrown Direction: \n " +
          str(throw_direction)+" degrees")
plt.show()
