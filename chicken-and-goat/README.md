# Chicken and Goat Problems

## Question 1

A farmer has some chickens and some goats. Together there are 116 heads and 282 legs. How many chickens and goats does the farmer have?

### Answer

- [ ] 25 goats and 91 chickens

### Explanation

Suppose there are only chickens. With 116 heads, there would be 116*2=232 legs. The 282-232=50 additional legs would have come from 50/2=25 goats. It implies that there are 116-25=91 chickens.

## Question 2

There are 25 questions in a language exam. 4 marks are awarded for each correct answer and 2 marks are deducted for each wrong answer. If Sam scored 76 marks in the exam, how many questions did he get correct?
### Answer

- [ ] 21 correct answers

### Explanation

For each wrong sum, total number of marks lost = 6 (4 - (-2)).

If Sam answers all the questions correctly, he would earn a total of 100 (25 * 4) marks.

The difference of marks = 100 - 76 = 24. These 24 marks must be due to the wrong answers.

Therefore, number of wrong sums = Total marks lost / marks lost for each wrong answer = 24 / 6 = 4.

Therefore, the number of correct sums = 25 - 4 = 21.

We can cross-verify the answer. For 21 correct answers:

Total Score = 21 * 4 - (4 * 2) = 84 - 8 = 76.

## QUestion 3

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
(7 * 4) + (0 * 4) = Not possible (28 > 26)
(7 * 3) + (_ * 4) = Not possible
(7 * 2) + (3 * 4) = 26
(7 * 1) + (_ * 4) = Not possible
(7 * 0) + (_ * 4) = Not possible
```

So, Pete must have got 3 questions wrong from the first 30 questions (4 marks each) and 2 questions wrong from last 10 questions (7 marks each).

Therefore, Pete answered 27 questions correct from first 30 questions (4 marks each) and 8 questions correct from last 10 questions (7 marks each).

This can be cross-verified. Total marks earned = (27 * 4) + ( 8 * 7) = 108 + 56 = 164.
