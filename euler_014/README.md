##### Euler_014
The following iterative sequence is defined for the set of positive integers:

n -> n/2 if n is even

n -> 3*n + 1 if n is odd

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, <= N produces the longest chain? If many possible such numbers are there print the maximum one.

Note: Once the chain starts the terms are allowed to go above N.

##### Input Format

The first line contains an integer T, i.e., number of test cases.
Next T lines will contain an integers N.

##### Constraints

1 <= T <= 10e4

1 <= N <= 5 * 10e6

##### Output Format

Print the values corresponding to each test case.

##### Sample Input

3

10 

15

20

##### Sample Output

9

9

19