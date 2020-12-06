##### Euler_022
You are given around five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list in sample is sorted into alphabetical order, PAMELA, which is worth 16 + 1 + 13 + 5 + 12 + 1 = 48, is the 5th name in the list.
So, PAMELA would obtain a score of 5 * 48 = 240.

You are given Q queries, each query is a name, you have to print the score.

##### Input Format

The first line contains an integer N, i.e., number of names.
Next N lines will contain a Name.
Followed by an integer, Q, followed by Q lines each having a word.

##### Constraints

1 <= N <= 5200

length of each word will be less than 12

1 <= Q <= 100

##### Output Format

Print the values corresponding to each test case.

##### Sample Input

5

ALEX

LUIS

JAMES

BRIAN

PAMELA

1

PAMELA

##### Sample Output

240