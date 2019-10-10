# Notes 

### Two problems I face while solving algorithms
1. mathematical analysis
2. Pattern recognition

I have noticed I approach problems in a brute force manner. However, from solutions I have encoutered, I have learnt that I should try and find a pattern and see how that can be used to optimize my code.


Patterns I have noticed so far
===============================
1. Rise, fall, valleys and peak patterns of numbers
2. When there are sequential numbers that are scattered and you ned to find minimum actions to take a sorting algorithm will most likely be the clue.

Mathematical Tricks
===================
1. The Modulo (%) operator
x + (y - (x % y)) will return the next highest multiple of y from x
It can also be used to wrap around an array preventing the need of an IF statement
idx % N will wrap around an array
2. For any number K, the sum of 2 values (A & B) is evenly divisible by K if the sum of the remainders of A/K + B/K is K
That is if (A%K) + (B%K) == K


PITFALLS
===========
1. Try not to confuse SUBSET with SUB-ARRAY
2. For sequential lists 1 <= a[i] <= n -- should not be confused with from 1 <= a[i] <= 10^x