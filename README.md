# Gauss-Jordan Elimination for Calculating Matrix Systems

This project contains Python code for calculating matrix systems using the Gauss-Jordan elimination method. It supports solving matrix equations and finding matrix inverses.

## Overview

The code is segmented for clarity and provides detailed steps for calculating matrix systems. For additional insights, you can refer to the paper "Use of Gauss-Jordan Elimination Method to Balance Chemical Reaction" by M.V. Deshmukh.

### Note:
- If the determinant of matrix {A} is zero, the program will not work.

## Code Segments

### 1. Inputs
The code handles two types of problems:
- **Matrix Systems**: Input as {A|B}.
- **Matrix Inverse**: Input as {A}, which is then extended to {A|I}.

The code supports inputs directly or through Excel files using the `xlrd` module.

### 2. Pivoting
Pivoting is used when a zero or small value appears in the diagonal of {A}. The row is replaced with another row with a larger value in that column to prevent errors.

### 3. Gauss-Jordan Algorithm
The code follows the Gauss-Jordan elimination steps. The diagonal element is divided, and the algorithm eliminates other elements in the same column. The process continues until the matrix is in reduced row echelon form.

### 4. Output
The code prints the matrix after each elimination step and displays the final result. Optionally, the output can be exported to an Excel file using the `xlwt` module.

## Resources
This code was inspired by numerical calculation courses and further supported by M.V. Deshmukh's paper. Additional coding tips were sourced from Stack Overflow.

## Author
Kamyab Safaie  
Student of Chemical Engineering at Sharif University of Technology  
November 2021
