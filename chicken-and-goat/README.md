# Chicken and Goat Problems

## Question 1

A farmer has some chickens and some goats. Together there are 116 heads and 282 legs. How many chickens and goats does the farmer have?

### Answer

- [ ] 18 goats and 125 chickens
- [ ] 25 goats and 100 chickens
- [ ] 20 goats and 110 chickens
- [x] 25 goats and 91 chickens

### Explanation

Suppose there are only chickens. With 116 heads, there would be 116*2=232 legs. The 282-232=50 additional legs would have come from 50/2=25 goats. It implies that there are 116-25=91 chickens.

## Question 2

There are 25 questions in a language exam. 4 marks are awarded for each correct answer and 2 marks are deducted for each wrong answer. If Sam scored 76 marks in the exam, how many questions did he get correct?
### Answer

- [ ] 16
- [x] 21
- [ ] 18
- [ ] 22

### Explanation

For each wrong sum, total number of marks lost = 6 (4 - (-2)).

If Sam answers all the questions correctly, he would earn a total of 100 (25 * 4) marks.

The difference of marks = 100 - 76 = 24. These 24 marks must be due to the wrong answers.

Therefore, number of wrong sums = Total marks lost / marks lost for each wrong answer = 24 / 6 = 4.

Therefore, the number of correct sums = 25 - 4 = 21.

We can cross-verify the answer. For 21 correct answers:

Total Score = 21 * 4 - (4 * 2) = 84 - 8 = 76.

## Question 3

There are 40 questions in a science quiz. The first 30 questions are worth 4 marks and the next 10 questions are worth 7 marks each. There is no negative marking i.e., no marks are deducted for each wrong answer. Pete scored a total of 164 marks in the quiz. How many of the first 30 questions and how many of the last 10 questions does he answer correct?

### Answer

- [ ] 26 and 6
- [x] 27 and 8
- [ ] 28 and 6
- [ ] 26 and 3

### Explanation

The maximum possible score that can be earned = (30 * 4) + (10 * 7) = 120 + 70 = 190.

So, the marks lost due to the wrong answers = 190 - 164 = 26.

These 26 lost marks are due to some 3 marks questions and some 5 marks questions which are wrongly answered. Here, we have to do try the different multiples of 4 and 7 which can sum up to 26.

```
(7 * 4) + (4 * 0) = Not possible (28 > 26)
(7 * 3) + (4 * _) = Not possible
(7 * 2) + (4 * 3) = 26
(7 * 1) + (4 * _) = Not possible
(7 * 0) + (4 * _) = Not possible
```

So, Pete must have got 3 questions wrong from the first 30 questions (4 marks each) and 2 questions wrong from last 10 questions (7 marks each).

Therefore, Pete answered 27 questions correct from first 30 questions (4 marks each) and 8 questions correct from last 10 questions (7 marks each).

This can be cross-verified. Total marks earned = (27 * 4) + ( 8 * 7) = 108 + 56 = 164.

## Question 4

There are 20 goats more than chickens in a country farm. Given that there are 182 legs altogether, how many goats are there in the farm?

### Answer

- [ ] 35
- [x] 37
- [ ] 42
- [ ] 50

### Explanation

The number of legs because of additional 20 goats = 20 * 4
The number of legs because of additional 20 goats = 80

Subtracting it from the total number of legs = 182 - 80 = 102

Now, equal number of goats and chickens are contributing to these 102 legs.

One pair of goat and chicken contributes to 4 + 2 = 6 legs
Therefore, the number of pairs of goat and chicken = 106 / 6 = 17

Number of Chickens = 17
Number of Goats = 17 + 20 = 37

We can cross-verify the answer by calculating the total number of legs = (17 * 2) + (37 * 4) = 34 + 148 = 182.

Please note that using reasoning, we can easily eliminate option 4 (50) as it would result in 200 (50 * 4) legs. That increases the probability of the right answer from 25% (1/4) to 33.3% (1/3).
