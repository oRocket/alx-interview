# Rotate 2D Matrix

## Concepts Needed:
1. Matrix Representation in Python:

    - Understanding how 2D matrices are represented using lists of lists in Python.
    - Accessing and modifying elements in a 2D matrix.

2. In-place Operations:

    - Performing operations on data without creating a copy of the data structure.
    - The importance of minimizing space complexity by modifying the matrix in place.

3. Matrix Transposition:

    - Understanding the concept of transposing a matrix (swapping rows and columns).
    - Implementing matrix transposition as a step in the rotation process.

4. Reversing Rows in a Matrix:

    - Manipulating rows of a matrix by reversing their order as part of the rotation process.

5. Nested Loops:

    - Using nested loops to iterate through 2D data structures like matrices.
    - Modifying elements within nested loops to achieve the desired rotation.


## Tasks
```
0. Rotate 2D Matrix
```
Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise.

- Prototype: `def rotate_2d_matrix(matrix)`:
- Do not return anything. The matrix must be edited **in-place**.
- You can assume the matrix will have 2 dimensions and will not be empty.
```
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
```
**Repo**:

- GitHub repository: `alx-interview`
- Directory: `0x07-rotate_2d_matrix`
- File: `0-rotate_2d_matrix.py`
