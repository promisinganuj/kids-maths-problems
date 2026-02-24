# Proportional Output Problems

## Difficulty Guide

- `(*)` Foundational level (quick single-step reasoning)
- `(**)` Intermediate level (2-step or mixed-concept reasoning)
- `(***)` Challenge level (multi-step selective-school style problems)

## Question 1 (*)

Suppose it takes 4 workers working 6 hours per day to produce 360 units of a product. How many workers would be needed to produce 600 units of the same product if each worker worked for 8 hours per day?

### Answer

- [x] 5
- [ ] 3
- [ ] 8
- [ ] 4

### Explanation

For such sums, it is easier to start by writing the details in tabular format. The variable which needs to be calculated should be written at the last:

```text
Units | Hours | Workers
-----------------------
360   | 6     | 4
600   | 8     | ?
```

#### Method 1

The easiest way to solve such problems is by using logical reasoning about the impact of changing each input variable on the output variable, while keeping rest of the input variables unchanged. Here is how it works:

Keeping the hours unchanged, if 360 units are made by 4 workers, it would take more workers to make 600 units, so we multiply by a fraction that is greater than 1, i.e., (600/360).

Now, keeping the units unchanged, if each worker is working 6 hours, it takes 4 workers to finish the job. So, if each worker works for 8 hours, it would take fewer workers to finish the same amount of work. Thus, in this case, we multiply by a fraction that is less than 1, i.e., (6/8).

Combining everything, No. of required Workers = 4 * (600/360) * (6/8) = 5.

#### Method 2

To solve this problem, we can set up a proportion:

(Number of workers) x (Number of hours worked per day) x (Output per worker per hour) = Total output

Using the values given in the problem, we get:

(4) x (6) x (Output per worker per hour) = 360

Simplifying, we get:

Output per worker per hour = 15

Now we can use this value to solve for the number of workers needed to produce 600 units with 8 hours per day:

(Number of workers) x (8) x (15) = 600

Simplifying, we get:

(Number of workers) = 5

Therefore, 5 workers would be needed to produce 600 units of the product in 8 hours per day.

## Question 2 (**)

Suppose a factory produces a certain product, and it takes 4 workers working 8 hours per day to produce 160 units of the product. If the factory wants to produce 1200 units of the same product, how many workers will be needed if they work 12 hours per day? Assume that the output per worker per hour is constant.

### Answer

- [ ] 10
- [ ] 12
- [ ] 15
- [x] 20

### Explanation

```text
Units | Hours | Workers
-----------------------
160   | 8     | 4
1200  | 12    | ?
```

No. of required Workers = 4 * (1200/160) * (8/12) = 20.

## Question 3 (**)

8 workers working 5 hours per day can pack 960 boxes in 6 days. How many workers are needed to pack 1,680 boxes in 7 days if each works 6 hours per day?

### Answer

- [ ] 8
- [ ] 9
- [x] 10
- [ ] 12

### Explanation

Workers needed = $8 \times \frac{1680}{960} \times \frac{5}{6} \times \frac{6}{7}$

$= 8 \times \frac{7}{4} \times \frac{5}{6} \times \frac{6}{7} = 8 \times \frac{5}{4} = 10$.

## Question 4 (***)

12 machines running 9 hours a day produce 2,700 parts in 5 days. If 3 machines are under maintenance, how many hours per day must the remaining machines run to produce 2,400 parts in 4 days?

### Answer

- [ ] 8 hours
- [ ] 10 hours
- [ ] 12 hours
- [x] 13 1/3 hours

### Explanation

Let required hours be $h$.

$12 \times 9 \times 5$ machine-hours produce 2700 parts.

$9 \times h \times 4$ machine-hours must produce 2400 parts.

So,

$\frac{9 \cdot h \cdot 4}{12 \cdot 9 \cdot 5} = \frac{2400}{2700} = \frac{8}{9}$

$\Rightarrow \frac{h}{15} = \frac{8}{9} \Rightarrow h = \frac{120}{9} = 13\frac{1}{3}$.

Therefore, they must run for $13\frac{1}{3}$ hours per day.

## Question 5 (**)

6 painters can paint 4 identical rooms in 3 days, working 8 hours per day. At the same rate, how many days will 9 painters take to paint 9 rooms if they work 6 hours per day?

### Answer

- [ ] 4 days
- [x] 6 days
- [ ] 7 days
- [ ] 8 days

### Explanation

Work is proportional to painters $\times$ days $\times$ hours.

Required days

$= 3 \times \frac{9}{4} \times \frac{6}{9} \times \frac{8}{6}$

$= 3 \times \frac{9}{4} \times \frac{8}{9} = 6$ days.

## Question 6 (*)

15 students can arrange 1,200 books in 4 hours. If only 10 students are available and they work for 5 hours, how many books can they arrange (assuming equal rate)?

### Answer

- [ ] 900
- [ ] 950
- [x] 1000
- [ ] 1100

### Explanation

Books are proportional to students $\times$ hours.

Books possible

$= 1200 \times \frac{10}{15} \times \frac{5}{4}$

$= 1200 \times \frac{2}{3} \times \frac{5}{4} = 1000$.

## Question 7 (***)

A factory uses 18 workers for 10 days, 8 hours per day, to complete an order. After 4 days, 6 workers leave. To finish the same total order on time (in the original 10 days), how many hours per day must the remaining workers work for the last 6 days?

### Answer

- [ ] 9 hours
- [ ] 10 hours
- [ ] 11 hours
- [x] 12 hours

### Explanation

Total work in worker-hours = $18 \times 10 \times 8 = 1440$.

Work done in first 4 days = $18 \times 4 \times 8 = 576$.

Remaining work = $1440 - 576 = 864$ worker-hours.

Remaining workers = $12$, remaining days = $6$, let hours/day be $h$.

$12 \times 6 \times h = 864 \Rightarrow 72h = 864 \Rightarrow h = 12$.

So they must work 12 hours per day.
