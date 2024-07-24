import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)


def create_histogram():
    data = np.random.normal(20, 25, 5)
    plt.hist(data, color='blue')  # Plot the histogram
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('filename', format='jpg')  # Save the figure as a JPG file
    plt.close()  # Close the figure to free memory
    return 0



