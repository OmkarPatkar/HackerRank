'''
Problem Statement:

Loops

Task

Read an integer N. For all non-negative integers i < N, print . See the sample for details.

Input Format
The first and only line contains the integer, N.

Constraints
1 < N < 20

Output Format
Print N lines, one corresponding to each i.

Sample Input 0
5

Sample Output 0
0
1
4
9
16

'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a // b)
    print(str(round(a/b, 11)))
