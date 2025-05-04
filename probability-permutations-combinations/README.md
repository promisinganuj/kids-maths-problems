# Probability, Permutations and Combinations

## Question 1

A bag contains 12 blue marbles and 8 red marbles. If one marble is chosen at random, what is the probability that it will be a blue marble?

### Answer

- [ ] 0.5
- [ ] 0.8
- [x] 0.6
- [ ] 0.2

### Explanation

The total number of marbles in the bag is 12 + 8 = 20. The probability of choosing a blue marble is the number of blue marbles divided by the total number of marbles, which is:

12/20 = 3/5

So the probability of choosing a blue marble is 3/5 or 0.6.

Therefore, the probability that a marble chosen at random from the bag will be a blue marble is 0.6 or 60%.

## Question 2

In a certain country, car number plates consist of three letters followed by three digits (e.g., ABC123). If a car number plate is chosen at random, what is the probability that the plate contains at least one letter 'A'?

Hint: You can use the principle of inclusion-exclusion to solve this problem.

### Answer

- [x] 34.25
- [ ] 50.24
- [ ] 16.58
- [ ] 90.23

### Explanation

Let's first find the probability that the plate does not contain the letter 'A'. Since there are 26 letters in the English alphabet, there are 25 letters other than 'A'. Therefore, the probability that a randomly chosen letter is not 'A' is 25/26. Since there are three letters in the plate, the probability that none of them are 'A' is:

(25/26) x (25/26) x (25/26) = 0.6575 (approx.)

So the probability that the plate contains at least one 'A' is the complement of this, i.e., 1 minus the probability that none of the letters are 'A'. Therefore:

P(at least one 'A') = 1 - 0.6575 = 0.3425 (approx.)

So the probability that a car number plate chosen at random contains at least one letter 'A' is approximately 0.3425 or 34.25%.

## Question 3

A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. If a marble is randomly selected from the bag, what is the probability of drawing a blue marble? Assume that each marble has an equal chance of being drawn and that once a marble is drawn, it is not replaced back into the bag.

### Answer

- [x] 3 / 10
- [ ] 5 / 10
- [ ] 1 / 2
- [ ] 8 / 10

### Explanation

Total number of marbles = 5 (red) + 3 (blue) + 2 (green) = 10 marbles

Number of blue marbles = 3

Probability of drawing a blue marble = Number of blue marbles / Total number of marbles
Probability of drawing a blue marble = 3 / 10

Therefore, the probability of drawing a blue marble from the bag is 3/10 or 0.3 (or 30%).

## Question 4

A fair six-sided die is rolled. What is the probability of rolling an even number?

### Answer

- [x] 1 / 2
- [x] 2 / 3
- [x] 4 / 6
- [x] 1 / 3

### Explanation

To solve this problem, we need to determine the number of favorable outcomes (rolling an even number) and the total number of possible outcomes (rolling any number on the die).

Favorable outcomes (even numbers): 2, 4, 6 (three numbers)
Total possible outcomes: 1, 2, 3, 4, 5, 6 (six numbers)

Probability of rolling an even number = Number of favorable outcomes / Total number of possible outcomes
Probability of rolling an even number = 3 / 6

Therefore, the probability of rolling an even number on a fair six-sided die is 3/6 or 1/2, which can also be written as 0.5 or 50%.

## Question 5 (*)

A bag contains 4 red balls, 5 blue balls, and 3 green balls. If two balls are randomly drawn from the bag without replacement, what is the probability of drawing two blue balls in succession?

### Answer

- [ ] 103 / 132
- [x] 20 / 132
- [ ] 10 / 33
- [ ] 10 / 132

### Explanation

To solve this problem, we need to determine the total number of balls, the number of blue balls, and the number of balls remaining after the first draw.

Total number of balls = 4 (red) + 5 (blue) + 3 (green) = 12 balls
Number of blue balls = 5

After the first draw, one ball is removed from the bag, leaving a total of 11 balls.
Number of blue balls remaining = 5 - 1 = 4

Probability of drawing two blue balls in succession = (Number of blue balls / Total number of balls) * (Number of blue balls remaining / Total number of balls after the first draw)
Probability of drawing two blue balls in succession = (5/12) * (4/11)

Therefore, the probability of drawing two blue balls in succession is (5/12) * (4/11) = 20/132 = 5/33, which is approximately 0.152 or 15.2%.

## Question 6 (*)

A fair six-sided die is rolled. What is the probability of getting either an even number or a number which is divisible by 3?

### Answer

- [ ] 1 / 2
- [x] 4 / 6
- [ ] 3 / 6
- [ ] 1 / 3

### Explanation

To solve the problem, we need to determine the number of favorable outcomes (getting either an even number or a number divisible by 3) and the total number of possible outcomes (rolling any number on the fair six-sided die).

Favorable outcomes (even numbers): 2, 4, 6 (three numbers)
Favorable outcomes (numbers divisible by 3): 3, 6 (two numbers)

To avoid double-counting, we should remove the overlapping outcome, which is 6 since it satisfies both conditions. So, the total number of favorable outcomes is 3 + 2 - 1 = 4.

Total possible outcomes: 1, 2, 3, 4, 5, 6 (six numbers)

Probability of getting either an even number or a number divisible by 3 = Number of favorable outcomes / Total number of possible outcomes
Probability of getting either an even number or a number divisible by 3 = 4 / 6

Therefore, the probability of getting either an even number or a number divisible by 3 when rolling a fair six-sided die is 4/6, which can be simplified to 2/3 or approximately 0.667 or 66.7%.

The elimination method can also be helpful here. Note that option 1 (1/2) and option 3 (3/6) are essentially the same. But two answers can't be correct. So, the correct answer is either option 2 or option 4. With this reasoning, the chances of getting to the correct answer has increased from 25% (1/4) to 50% (1/2), without even solving the problem.

## Question 6 (*)

What's the probability of getting at-least two heads in 3 coin flips? What's the probability of getting exactly two heads. Assume that it's a fair coin.

### Answer

- [ ] 5 / 8
- [x] 4 / 8
- [ ] 3 / 8
- [ ] 2 / 8

### Explanation

To solve the problem, we need to determine the number of favorable outcomes (getting at least two heads) and the total number of possible outcomes (all possible results of flipping a fair coin three times).

Total possible outcomes: Each coin flip has 2 possible outcomes (heads or tails). For 3 flips, the total number of outcomes is 2^3 = 8. The possible outcomes are:

```text
1st | 2nd | 3rd
---------------
H     H     H   <---
H     H     T   <---
H     T     H   <---
H     T     T
T     H     H   <---
T     H     T
T     T     H
T     T     T
````

Favorable outcomes (at least two heads): HHH, HHT, HTH, THH (four outcomes).

Probability of getting at least two heads = Number of favorable outcomes / Total number of possible outcomes  
Probability of getting at least two heads = 4 / 8

Therefore, the probability of getting at least two heads in 3 coin flips is 4/8, which can be simplified to 1/2 or 50%.

Now, for exactly two heads, there are only 3 favorable outcomes: HHT, HTH, THH.

Probability of getting exactly two heads = Number of favorable outcomes / Total number of possible outcomes  
Probability of getting exactly two heads = 3 / 8

Therefore, the probability of getting at least two heads in 3 coin flips is 3/8, which can be simplified to 0.375 or 37.5%.
