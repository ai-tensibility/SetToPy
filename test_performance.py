import time
import numpy as np
import matplotlib.pyplot as plt
from settopy_bindings import SetToPy


class Set:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = list(set(elements))  # Ensure unique elements

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def __contains__(self, element):
        return element in self.elements

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        return iter(self.elements)

    def __repr__(self):
        return "{" + ", ".join(map(str, self.elements)) + "}"

# Function to generate random pixels for a given screen size using simple Set
def generate_random_pixels_set(screen_size):
    pixels = Set()
    for i in range(0, screen_size, 2):  # Reducing the number of iterations
        for j in range(0, screen_size, 2):  # Reducing the number of iterations
            R = (i * j) % 256
            pixels.add((i, j, R))
    return pixels

# Function to generate random pixels for SetToPy
def generate_random_pixels_settopy(screen_size):
    pixels = SetToPy()
    for i in range(0, screen_size, 2):  # Reducing the number of iterations
        for j in range(0, screen_size, 2):  # Reducing the number of iterations
            R = (i * j) % 256
            pixels.add(i, j, R)
    return pixels

# Function to generate random pixels for matrix-based approach using NumPy
def generate_random_pixels_matrix(screen_size):
    pixels = np.zeros((screen_size, screen_size, 3), dtype=int)
    for i in range(0, screen_size, 2):  # Reducing the number of iterations
        for j in range(0, screen_size, 2):  # Reducing the number of iterations
            R = (i * j) % 256
            pixels[i, j] = [i, j, R]
    return pixels

# Function to calculate brightness of a pixel
def calculate_brightness_set(pixel):
    x, y, value = pixel
    return x, y, 0.299 * value + 0.587 * value + 0.114 * value

# Function to calculate brightness of a pixel for SetToPy
def calculate_brightness_settopy(element):
    x, y, value = element
    return x, y, 0.299 * value + 0.587 * value + 0.114 * value

# Function to calculate brightness of a pixel for matrix-based approach
def calculate_brightness_matrix(pixels):
    brightness = 0.299 * pixels[:, :, 2] + 0.587 * pixels[:, :, 2] + 0.114 * pixels[:, :, 2]
    return brightness

# Set-Based Approach for simple Set class
def set_based_approach_simple(screen_size):
    pixels = generate_random_pixels_set(screen_size)
    brightness_set = Set()
    for pixel in pixels:
        brightness = calculate_brightness_set(pixel)
        brightness_set.add((brightness[0], brightness[1], int(brightness[2])))
    return brightness_set

# Set-Based Approach for SetToPy class
def set_based_approach_settopy(screen_size):
    pixels = generate_random_pixels_settopy(screen_size)
    brightness_set = SetToPy()
    elements = pixels.get_elements()
    for element in elements:
        brightness = calculate_brightness_settopy(element)
        brightness_set.add(brightness[0], brightness[1], int(brightness[2]))
    return brightness_set

# Matrix-Based Approach using NumPy
def matrix_based_approach(screen_size):
    pixels = generate_random_pixels_matrix(screen_size)
    brightness = calculate_brightness_matrix(pixels)
    return brightness

# Measure execution time for different screen sizes
screen_sizes = [10, 20, 30, 40, 50, 70, 90, 100, 150, 200, 250, 300]
set_simple_times = []
set_topy_times = []
matrix_times = []

for size in screen_sizes:
    # Test with simple Set class
    start_time = time.time()
    set_based_approach_simple(size)
    end_time = time.time()
    avg_time = (end_time - start_time)
    set_simple_times.append(avg_time)
    print(f"Simple Set-Based Approach - Screen Size {size}: {avg_time} seconds")

    # Test with SetToPy class
    start_time = time.time()
    set_based_approach_settopy(size)
    end_time = time.time()
    avg_time = (end_time - start_time)
    set_topy_times.append(avg_time)
    print(f"SetToPy Set-Based Approach - Screen Size {size}: {avg_time} seconds")

    # Test with matrix-based approach
    start_time = time.time()
    matrix_based_approach(size)
    end_time = time.time()
    avg_time = (end_time - start_time)
    matrix_times.append(avg_time)
    print(f"Matrix-Based Approach - Screen Size {size}: {avg_time} seconds")

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(screen_sizes, set_simple_times, label='Simple Set-Based Approach', marker='d')
plt.plot(screen_sizes, set_topy_times, label='SetToPy Set-Based Approach', marker='d')
plt.plot(screen_sizes, matrix_times, label='Matrix-Based Approach', marker='x')
plt.xlabel('Screen Size (NxN)')
plt.ylabel('Average Execution Time (seconds)')
plt.yscale('log')  # Set the y-axis to logarithmic scale
plt.title('Execution Time Comparison: Simple Set vs SetToPy vs Matrix-Based Approach')
plt.legend()
plt.grid(True)
plt.show()
