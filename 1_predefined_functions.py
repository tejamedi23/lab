import math

print("Pi:", math.pi) # Print PI value

# Basic Mathematical Functions
print(math.sqrt(16)) # Square root: 4.0
print(math.pow(2, 3)) # Power: 8.0
print(math.exp(2)) # Exponential e^x: 7.38905609893065
print(math.log10(100)) # Log base 10: 2.0
print(math.log2(8)) # Log base 2: 3.0

# Rounding and Absolute Values
print(math.ceil(3.1)) # Round up: 4
print(math.floor(3.9)) # Round down: 3
print(math.fabs(-7.5)) # float Absolute value: 7.5

# Factorial of a given number
print(math.factorial(5)) # 5! = 120

# Trigonometric Functions
result_in_radians = math.sin(30)
result_in_degrees = math.sin(math.radians(90))
print(f"Result in radians sin 30: {result_in_radians}")
print(f"Result for sin 90 degrees: {result_in_degrees}") # Correct result for sine of 30 degrees

# Hyperbolic Functions
print(math.sinh(1)) # Hyperbolic sine
print(math.cosh(1)) # Hyperbolic cosine
print(math.tanh(1)) # Hyperbolic tangent

# GCD, LCM, and Other Functions
print(math.gcd(36, 48)) # Greatest Common Divisor: 12
print(math.lcm(12, 18)) # Least Common Multiple: 36

# Special Functions
# math.inf #print inf
# math.nan #print Nat a Number
print(math.isfinite(5)) # True (is finite)
print(math.isinf(math.inf)) # True (infinity)
print(math.isnan(math.nan)) # True (Not a Number)

# Permutations (perm) and Combinations (comb)
print(math.perm(5, 2)) # 5P2 = 5! / (5-2)! = 20
print(math.comb(5, 2)) # 5C2 = 5! / (2!(5-2)!) = 10

# Distance Between Two Points
print(math.dist([3, 4], [0, 0])) # 5.0 (Euclidean distance)

# Using math library in Real-World Problems
# Example 1: Finding the Area of a Circle
radius = 5
area = math.pi * math.pow(radius, 2)
print(area) # 78.53981633974483

# Example 2: Convert Degrees to Radians and Find Cosine
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(math.cos(angle_rad)) # 0.7071067811865476

# Example 3: Calculate Monthly EMI for a Loan
def calculate_emi(principal, annual_rate, tenure_months):
 r = annual_rate / (12 * 100)
 emi = (principal * r * math.pow(1 + r, tenure_months)) / (math.pow(1 + r, tenure_months) - 1)
 return round(emi, 2)

emi = calculate_emi(500000, 7.5, 60)
print("Monthly EMI:", emi) # Output: Monthly EMI: 10037.24


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr) # Output: [1 2 3 4 5]

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)

myArray3=np.array([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,6]]])
print("Dimension of myArray3 is", np.ndim(myArray3))
print("Three dimesional Array values are:", myArray3)

print(arr.ndim) # Number of dimensions: 1
print(matrix.ndim) # Number of dimensions: 2
print(matrix.shape) # Shape of array: (2, 3)
print(arr.size) # Total number of elements: 5
print(matrix.size) # Total number of elements: 6
print(arr.dtype) # Data type of elements: int32 (or int64 depending on sy
print(matrix.dtype) # Data type of elements: int32 (or int64 depending on

print(arr[0]) # First element: 1
print(matrix[1, 2]) # Element at 2nd row, 3rd column: 6
print(arr[1:4]) # Elements from index 1 to 3: [2 3 4]
print(matrix[:, 1]) # All rows, second column: [2 5]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b) # [5 7 9]
print(a - b) # [-3 -3 -3]
print(a * b) # [4 10 18]
print(a / b) # [0.25 0.4 0.5 ]

print(a + 5) # [6 7 8]
print(a * 2) # [2 4 6]

arr = np.array([1, 2, 3, 4, 5])
print(np.sqrt(arr)) # [1. 1.414 1.732 2. 2.236]
print(np.exp(arr)) # Exponentials
print(np.sin(arr)) # Sine values
print(np.log(arr)) # Natural logarithm

print(np.sum(arr)) # Sum: 15
print(np.mean(arr)) # Mean: 3.0
print(np.median(arr)) # Median: 3.0
print(np.std(arr)) # Standard deviation
print(np.min(arr)) # Minimum: 1
print(np.max(arr)) # Maximum: 5

arr = np.arange(1, 10)
reshaped = arr.reshape(3, 3)
print(reshaped)

arr = np.array([10, 20, 30, 40, 50])
print(arr > 30) # [False False False True True]

arr = np.array([1, 2, 3])
copy_arr = arr.copy()
print(copy_arr) # [1 2 3]

copy_arr[0] = 100
print(arr) # [1 2 3]
print(copy_arr) # [100 2 3]

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))
print(A.T)

random_numbers = np.random.rand(10)
print(random_numbers)
random_integers = np.random.randint(1, 101, size=10)
print(random_integers)
random_floats = np.random.uniform(5, 15, size=10)
print(random_floats)


import statistics
data = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
mean_value = statistics.mean(data)
print(f"Mean: {mean_value}")

data = [15, 20, 25, 35, 45, 55, 65, 75, 85, 95, 105] # odd case
median_value = statistics.median(data)
print(f"Median (odd case): {median_value}")

data = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105] # even case
median_value = statistics.median(data)
print(f"Median (even case): {median_value}")

mode_data = [10, 20, 30, 30, 30, 40]
mode_value = statistics.mode(mode_data)
print(f"Mode : {mode_value}")

mode_data = [10, 20, 20, 20, 30, 30, 30, 40]
mode_value = statistics.mode(mode_data)
print(f"Mode (multimodel) : {mode_value}")

mode_data = [10, 20, 30, 40, 50]
mode_value = statistics.mode(mode_data)
print(f"Mode (No_mode case) : {mode_value}")

stdev_value = statistics.stdev(data)
print(f"Standard Deviation: {stdev_value}")
variance_value = statistics.variance(data)
print(f"Variance: {variance_value}")

harmonic_mean_value = statistics.harmonic_mean(data)
print(f"Harmonic Mean: {harmonic_mean_value}")

data = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
median_low_value = statistics.median_low(data)
median_high_value = statistics.median_high(data)
print(f"Median Low: {median_low_value}")
print(f"Median High: {median_high_value}")

data = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16]
quantiles_value = statistics.quantiles(data)
print(f"Quantiles (Quartiles) Q1, Q2 and Q3: {quantiles_value}")


import pandas as pd
print(pd.__version__)

data = [10, 20, 30, 40]
s = pd.Series(data)
print("Data types of s is: ", type(s))
print(s)

dict1={"day1":420, "day2":380, "day3":390}
Sr3=pd.Series(dict1)
print(type(Sr3))
print(Sr3)

data = {100, 200, 300}
series = pd.Series(list(data)) # Convert set to list first
print(series)

data = [10, 20, 30, 40]
s = pd.Series(data)
print(s[0])

data = [10, 20, 30]
s = pd.Series(data, index=["X", "Y", "Z"])
print(s)
print(s['Y'])

mydataset = {
 'Name': ['Shiva', 'Ram', 'Krishna'],
 'Age': [25, 30, 35],
 'City': ['Hyderabad', 'Delhi', 'Mumbai']
}
print(type(mydataset))
df=pd.DataFrame(mydataset)
print(type(df))
print(df)
print(df.columns)
print(df.shape)
print(df.ndim)
print(df.size)
