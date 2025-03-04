### **Challenge: Optimal Feature Selection for Model Training**
"""
#### **Problem Statement**
You are given a dataset represented as a 2D matrix `X` of size `(n_samples, n_features)` and a target vector `y` of size `(n_samples,)`. Your task is to select the optimal subset of features that maximizes the model's performance while minimizing the number of features used.

To achieve this, you need to implement a function `select_features(X, y, k)` that:
1. Selects the top `k` features based on their importance scores.
2. Returns the indices of the selected features.

#### **Constraints**
- Use **Mutual Information** to calculate feature importance.
- The function should run efficiently for large datasets (e.g., `n_samples <= 10^6`, `n_features <= 10^4`).
- You are not allowed to use any built-in feature selection libraries (e.g., `sklearn.feature_selection`).

#### **Input**
- `X`: A 2D NumPy array of shape `(n_samples, n_features)`.
- `y`: A 1D NumPy array of shape `(n_samples,)`.
- `k`: An integer representing the number of features to select.

#### **Output**
- A list of indices of the selected features (sorted in descending order of importance).
```
#---
"""
#### **Example**
import numpy as np

X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
y = np.array([0, 1, 0])
k = 2

# Expected output: [2, 1] or [1, 2] (since feature 2 and 1 have the highest mutual information with y)
print(select_features(X, y, k))


---

#### **Solution Template**
import numpy as np

def mutual_information(X, y):
    """
    Calculate the mutual information between each feature and the target.
    
    Args:
        X (np.ndarray): Input features of shape (n_samples, n_features).
        y (np.ndarray): Target values of shape (n_samples,).
    
    Returns:
        np.ndarray: Mutual information scores for each feature.
    """
    # Implement mutual information calculation here
    pass

def select_features(X, y, k):
    """
    Select the top k features based on mutual information.
    
    Args:
        X (np.ndarray): Input features of shape (n_samples, n_features).
        y (np.ndarray): Target values of shape (n_samples,).
        k (int): Number of features to select.
    
    Returns:
        list: Indices of the selected features.
    """
    # Calculate mutual information scores
    mi_scores = mutual_information(X, y)
    
    # Select the top k features
    top_k_indices = np.argsort(mi_scores)[-k:][::-1]
    
    return list(top_k_indices)

# Example usage
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
y = np.array([0, 1, 0])
k = 2
print(select_features(X, y, k))  # Output: [2, 1] or [1, 2]

"""
#### **Hints**
1. **Mutual Information** measures the dependence between two variables. For discrete data, it can be calculated as:
   \[
   I(X; Y) = \sum_{x \in X} \sum_{y \in Y} p(x, y) \log \frac{p(x, y)}{p(x)p(y)}
   \]
   You can use histograms or probability distributions to estimate \( p(x) \), \( p(y) \), and \( p(x, y) \).

2. Use vectorized operations in NumPy for efficient computation.

3. For large datasets, consider using approximations or sampling to speed up the calculation.

#---

#### **Evaluation Criteria**
1. **Correctness**: Does the function correctly select the top `k` features based on mutual information?
2. **Efficiency**: Is the solution optimized for large datasets?
3. **Code Quality**: Is the code clean, modular, and well-documented?
4. **Edge Cases**: Does the solution handle edge cases (e.g., `k > n_features`, `k = 0`, or constant features)?



#### **Bonus**
1. Extend the function to handle both discrete and continuous features.
2. Implement a parallelized version of the mutual information calculation for faster computation.



This challenge tests your ability to:
- Implement a core data science concept (feature selection).
- Write efficient and scalable code.
- Handle edge cases and optimize for performance.
"""
