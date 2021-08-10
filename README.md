# karatsubaMultiplication
The Karatsuba algorithm is a fast multiplication algorithm.
Karatsuba multiplication algorithm is named after the Russian mathematician Anatoly Karatsuba. It uses a divide and conquer approach that gives it a running time improvement over the standard “grade-school” method. Read on for Python implementations of both algorithms and a comparison of their running time.


Example
![image](https://user-images.githubusercontent.com/66325605/128862680-950d6074-09cc-48a3-b2bd-e6c1fde83f22.png)


![image](https://user-images.githubusercontent.com/66325605/128863043-8a665659-aa70-440b-a964-37f5890b5db1.png)

Where a,b,c,d are n/2 digit numbers.

![image](https://user-images.githubusercontent.com/66325605/128862579-ea010bf6-97f9-4458-bdf1-48e96451c52c.png)


Here’s Karatsuba’s algorithm:
1. Break the two integers x and y into a, b, c and d as described above
2. Recursively compute ac
3. Recursively compute bd
4. Recursively compute (a + b)(c + d)
5. Calculate (ab + bc) as (a + b)(c + d) – ac – bd
6. Let A be ac with n zeros added to the end
7. let B be (ab + bc) with half n zeros added to the end
8. The final answer is A + B + bd





for more information https://en.wikipedia.org/wiki/Karatsuba_algorithm
