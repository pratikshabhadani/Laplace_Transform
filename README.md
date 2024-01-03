# Laplace_Transform
Scratch implemantation of Laplace Transform;

**In the file lp_tr.py following implementations have been done:**
1. The formula of Laplace transform is integration from 0 to infinity of e^(-sx)*f(x). f(x) being the function we are finding laplace of. Lets call e^(-sx)*f(x) as L.
2. The code takes input as the function and value of s to give output.
3. Now first we check if the laplace transform of given function can be calculated by my code by checking if the limit tends to infinity of the function should be finite, if its not the code simply stops displaying the error message.
4. If the tranform is possible our main challange is now to find a number big enough so that the integration value at infinity and at that number are almost the same, this is done in function upper bound.
5. Once we have done that we the integration value from trapezoidal rule.

   
**Note 1:** The code fails to give right output if:

    1. The limit tends to infinity of the function L is not finite.
    2. The value of the function L is infinite at some point between 0 to infinity.
    3. The function L is discontionus between 0 to infinity.
   
**Note 2:** The need to input value of s:

    1. The final answer from comes out to be in addition of terms of trapezoidal rule(in form of y0+y1+y2......yn) which is very long.
    2. I tried my best to find a way to evalute such terms but was unable to.

  **In the file lp_tr2.py following implementations have been done:**
  1. We input only the function we want to find Laplace of.
  2. Rest working is the same as lp_tr.py.
  3. To calculate the transform we plot a graph between differnent values of s and L.
  4. Then we use pythons library curve_fit to find the function corresponding to graph
  5. We have to use custom fits to get desired results(I have implemented one in my code for testing input functions like sin(x), x etc. rest other custom fits needs to done for all kind of desired output).
