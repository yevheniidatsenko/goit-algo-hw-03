# Recursive Functions, Algorithms, and Applications

In this assignment, you will explore the power of recursion through various tasks. By the end of this homework, you should have learned the following:

- How to implement recursive algorithms to solve complex problems.
- How to manage file systems using recursion for tasks such as sorting and copying files.
- How to create and visualize fractals, specifically the "Koch Snowflake", using recursive techniques.
- (Optional) How to solve the classic Tower of Hanoi problem, deepening your understanding of recursion and stack operations.

## Assignment Description

### Task 1: Recursive File Sorting

Write a Python program that recursively copies files from a source directory, moves them to a new directory, and sorts them into subdirectories based on file extensions.

Consider the following conditions:

1. **Argument Parsing**:

   - The script should accept two command line arguments: the path to the source directory and the path to the destination directory (default to a directory named `dist` if not provided).

2. **Recursive Directory Reading**:

   - Write a function that accepts a directory path as an argument.
   - The function should iterate through all elements in the directory.
   - If an element is a directory, the function should call itself recursively for that directory.
   - If an element is a file, it should be copied to the appropriate location.

3. **File Copying**:

   - Create a new path in the destination directory for each file type, using the file extension for naming subdirectories.
   - Copy each file to the corresponding subdirectory.

4. **Exception Handling**:
   - The code should properly handle exceptions, such as access errors to files or directories.

### Task 2: Koch Snowflake Fractal

Write a Python program that uses recursion to create a "Koch Snowflake" fractal, allowing the user to specify the recursion level.

### Task 3: Tower of Hanoi (Optional)

Write a program that moves disks from rod A to rod C, using rod B as an auxiliary, following these rules:

1. Only one disk can be moved at a time.
2. A disk can only be placed on a larger disk or an empty rod.

Input: `n` - the number of disks on the initial rod.
Output: Log the sequence of steps to move the disks from rod A to rod C.

Example execution for `n = 3`:

```
Initial state: {'A': [3, 2, 1], 'B': [], 'C': []}
Move disk from A to C: 1
Intermediate state: {'A': [3, 2], 'B': [], 'C': [1]}
Move disk from A to B: 2
Intermediate state: {'A': [3], 'B': [2], 'C': [1]}
Move disk from C to B: 1
Intermediate state: {'A': [3], 'B': [2, 1], 'C': []}
Move disk from A to C: 3
Intermediate state: {'A': [], 'B': [2, 1], 'C': [3]}
Move disk from B to A: 1
Intermediate state: {'A': [1], 'B': [2], 'C': [3]}
Move disk from B to C: 2
Intermediate state: {'A': [1], 'B': [], 'C': [3, 2]}
Move disk from A to C: 1
Intermediate state: {'A': [], 'B': [], 'C': [3, 2, 1]}
Final state: {'A': [], 'B': [], 'C': [3, 2, 1]}
```
