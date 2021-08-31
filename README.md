# Polynomial-Regression-Python-
Implementation of Polynomial Regression in Python

The class Polynomial Regression consists of three methods: -

1) Coefficients method: - This methods shall calculate the coefficients of the regression equation with the given degree. 
                   
If the degree specified is 2, then the regression equation shall be <img src="https://render.githubusercontent.com/render/math?math=y=a%2Bbx%2Bcx^2">

Similarly, if the degree is 3, then the regression equation is <img src="https://render.githubusercontent.com/render/math?math=y=a%2Bbx%2Bcx^2%2Bdx^3">

So, the coefficients method is concerned with calculating the values of a,b,c and d if the degree specified is 3..

Logic behind the code: -

If the degree selected by the user is 2, after optimizing the cost function using the partial derivatives of the mean squared error function wrt _a_,_b_ and _c_, the following equations are obtained:-

a) <img src="https://render.githubusercontent.com/render/math?math=\sum^{n}_{i=1}y_i=\sum^{n}_{i=1}a%2B\sum^{n}_{i=1}bx_i%2B\sum^{n}_{i=1}cx^2_i">

b) <img src="https://render.githubusercontent.com/render/math?math=\sum^{n}_{i=1}x_iy_i=\sum^{n}_{i=1}ax_i%2B\sum^{n}_{i=1}bx^2_i%2B\sum^{n}_{i=1}cx^3_i">

c) <img src="https://render.githubusercontent.com/render/math?math=\sum^{n}_{i=1}x^2_iy_i=\sum^{n}_{i=1}ax^2_i%2B\sum^{n}_{i=1}bx^3_i%2B\sum^{n}_{i=1}cx^4">

Converting the above three equations in matrix form,

<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\sum^{n}_{i=1}y_i\\\sum^{n}_{i=1}x_iy_i\\\sum^{n}_{i=1}x^2_iy_i\end{bmatrix}="> <img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\sum^{n}_{i=1}(1)\quad\sum^{n}_{i=1}x_i\quad\sum^{n}_{i=1}x^2_i\\\sum^{n}_{i=1}x_i\quad\sum^{n}_{i=1}x^2_i\quad\sum^{n}_{i=1}x^3_i\\\sum^{n}_{i=1}x^2_i\quad\sum^{n}_{i=1}x^3_i\quad\sum^{n}_{i=1}x^4\end{bmatrix}">  <img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}a\\b\\c\end{bmatrix}">

The value of the coefficients matrix can be found by multipying the inverse of first matrix on the right hand side with the matrix on the left hand side of the equation.

2)Predict Method: - The predict method is calculates the predicted y value for the given x value.

3)R_Square Method: - The r_square method calculates the _r^2_ value of the regression equation which ranges from 0<=r^2<=1

_r^2_=(Total Variance-UnExplained Variance)/Total Variance
