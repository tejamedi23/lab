import math
import statistics
import numpy as np
import pandas as pd

def demonstrate_maths():
    print("--- Math Functions ---")
    print("Pi:", math.pi)
    print(math.sqrt(16))
    print(math.pow(2, 3))
    print(math.exp(2))
    print(math.log10(100))
    print(math.log2(8))
    print(math.ceil(3.1))
    print(math.floor(3.9))
    print(math.fabs(-7.5))
    print(math.factorial(5))
    print(f"Result in radians sin 30: {math.sin(30)}")
    print(f"Result for sin 90 degrees: {math.sin(math.radians(90))}")
    print(math.sinh(1))
    print(math.cosh(1))
    print(math.tanh(1))
    print(math.gcd(36, 48))
    print(math.lcm(12, 18))
    print(math.isfinite(5))
    print(math.isinf(math.inf))
    print(math.isnan(math.nan))
    print(math.perm(5, 2))
    print(math.comb(5, 2))
    print(math.dist([3, 4], [0, 0]))

def demonstrate_numpy():
    print("--- NumPy Functions ---")
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(matrix)
    myArray3=np.array([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,6]]])
    print("Dimension of myArray3 is", np.ndim(myArray3))
    print("Three dimesional Array values are:", myArray3)
    print(arr.ndim)
    print(matrix.shape)
    print(arr.size)
    print(arr.dtype)
    print(arr[0])
    print(matrix[1, 2])
    print(arr[1:4])
    print(matrix[:, 1])
    
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a + 5)
    print(a * 2)
    
    print(np.sqrt(arr))
    print(np.exp(arr))
    print(np.sin(arr))
    print(np.log(arr))
    print(np.sum(arr))
    print(np.mean(arr))
    print(np.median(arr))
    print(np.std(arr))
    print(np.min(arr))
    print(np.max(arr))
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(np.dot(A, B))
    print(A.T)

def demonstrate_statistics():
    print("--- Statistics Functions ---")
    data = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
    print(f"Mean: {statistics.mean(data)}")
    print(f"Median (even case): {statistics.median(data)}")
    
    mode_data = [10, 20, 30, 30, 30, 40]
    print(f"Mode : {statistics.mode(mode_data)}")
    print(f"Standard Deviation: {statistics.stdev(data)}")
    print(f"Variance: {statistics.variance(data)}")
    print(f"Harmonic Mean: {statistics.harmonic_mean(data)}")
    print(f"Median Low: {statistics.median_low(data)}")
    print(f"Median High: {statistics.median_high(data)}")
    
    quantiles_data = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16]
    print(f"Quantiles (Quartiles) Q1, Q2 and Q3: {statistics.quantiles(quantiles_data)}")

def demonstrate_pandas():
    print("--- Pandas Functions ---")
    data = [10, 20, 30, 40]
    s = pd.Series(data)
    print("Data types of s is: ", type(s))
    print(s)
    
    dict1={"day1":420, "day2":380, "day3":390}
    Sr3=pd.Series(dict1)
    print(type(Sr3))
    print(Sr3)
    
    mydataset = {
     'Name': ['Shiva', 'Ram', 'Krishna'],
     'Age': [25, 30, 35],
     'City': ['Hyderabad', 'Delhi', 'Mumbai']
    }
    df=pd.DataFrame(mydataset)
    print(type(df))
    print(df)
    print(df.columns)
    print(df.shape)
    print(df.ndim)

if __name__ == "__main__":
    demonstrate_maths()
    demonstrate_numpy()
    demonstrate_statistics()
    demonstrate_pandas()
