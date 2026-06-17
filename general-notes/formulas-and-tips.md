# Formulas and Tips

A quick-reference cheat sheet, grouped by topic:

1. [Number & Arithmetic](#1-number--arithmetic)
2. [Algebra](#2-algebra)
3. [Geometry & Measurement](#3-geometry--measurement)
4. [Counting & Probability](#4-counting--probability)
5. [Reasoning Aids (Verbal & Numerical)](#5-reasoning-aids-verbal--numerical)

---

# 1. Number & Arithmetic

## Number, Average, Percentage & Rate

Description | Formula
--- | --- |
HCF and LCM relationship | $\text{HCF}(a, b) \times \text{LCM}(a, b) = a \times b$
Mean (average) | $\frac{\text{sum of values}}{\text{number of values}}$
Average speed | $\frac{\text{total distance}}{\text{total time}}$ (**not** the average of the speeds)
Speed / Distance / Time | $\text{speed} = \frac{\text{distance}}{\text{time}}$
Percentage change | $\frac{\text{new} - \text{old}}{\text{old}} \times 100\%$
Simple interest | $I = \frac{P \cdot R \cdot T}{100}$
Profit / Loss percentage | $\frac{\text{profit or loss}}{\text{cost price}} \times 100\%$

### Divisibility Quick Checks
- **2:** last digit even. **5:** ends in 0 or 5. **10:** ends in 0.
- **4:** last two digits form a number divisible by 4. **8:** last three digits divisible by 8.
- **3:** digit sum divisible by 3. **9:** digit sum divisible by 9. **6:** divisible by both 2 and 3.
- **11:** the alternating digit sum is 0 or a multiple of 11. e.g. $2728$: $2 - 7 + 2 - 8 = -11$ ✓ (divisible); $2918$: $2 - 9 + 1 - 8 = -14$ ✗ (not divisible).

## Index (Power) Laws

Law | Rule
--- | --- |
Multiplying | $a^m \cdot a^n = a^{m+n}$
Dividing | $\frac{a^m}{a^n} = a^{m-n}$
Power of a power | $\left(a^m\right)^n = a^{m \cdot n}$
Power of a product | $(a \cdot b)^n = a^n \cdot b^n$
Zero index | $a^0 = 1$ (for $a \neq 0$)
Negative index | $a^{-n} = \frac{1}{a^n}$
Fractional index | $a^{\frac{1}{n}} = \sqrt[n]{a}$, and $a^{\frac{m}{n}} = \sqrt[n]{a^m}$

## Sequences & Series

Type | nth term | Sum of first $n$ terms
--- | --- | --- |
Arithmetic (common difference $d$) | $a + (n - 1)d$ | $\frac{n}{2}\left(2a + (n - 1)d\right)$, or $\frac{n}{2}(\text{first} + \text{last})$
Geometric (common ratio $r$) | $a \cdot r^{\,n-1}$ | $\frac{a\left(r^n - 1\right)}{r - 1}$ (for $r \neq 1$)

### Useful sums (first $n$ terms)

Description | Formula
--- | --- |
Sum of the first $n$ natural numbers | $\frac{n \cdot (n + 1)}{2}$
Sum of the first $n$ even numbers | $n \cdot (n + 1)$
Sum of the first $n$ odd numbers | $n^2$
Sum of the first $n$ squares | $\frac{n \cdot (n + 1) \cdot (2 \cdot n + 1)}{6}$
Sum of the first $n$ cubes | $\left(\frac{n \cdot (n + 1)}{2}\right)^2$

Number patterns to recognise on sight:
- **Square numbers:** $1, 4, 9, 16, 25, \ldots$ ($n^2$)
- **Triangular numbers:** $1, 3, 6, 10, 15, \ldots$ $\left(\frac{n(n+1)}{2}\right)$
- **Fibonacci:** $1, 1, 2, 3, 5, 8, 13, \ldots$ (each term is the sum of the previous two)
- **Powers of 2:** $1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024$

---

# 2. Algebra

## Parabola (Quadratic) Formulas

For a quadratic $y = ax^2 + bx + c$ (with $a \neq 0$), the graph is a parabola — opening **upwards** if $a > 0$ and **downwards** if $a < 0$.

### The three forms (each one tells you something at a glance)

Form | Equation | What you can read off immediately
--- | --- | --- |
Standard (general) | $y = ax^2 + bx + c$ | $y$-intercept $= c$ → point $(0, c)$
Vertex (turning point) | $y = a(x - h)^2 + k$ | vertex $(h, k)$ and axis of symmetry $x = h$
Factored (x-intercept) | $y = a(x - p)(x - q)$ | $x$-intercepts at $x = p$ and $x = q$

### Key formulas (standard form)

Description | Formula
--- | --- |
Axis of symmetry | $x = -\frac{b}{2a}$
Vertex from standard form | $\left(-\frac{b}{2a},\ c - \frac{b^2}{4a}\right)$
$y$-intercept | $(0,\ c)$

### Finding the x-intercepts (roots)

Set $y = 0$ and solve $ax^2 + bx + c = 0$. Two ways:
- **Factorise** if it factors neatly, e.g. $x^2 - 5x + 6 = (x - 2)(x - 3) = 0 \Rightarrow x = 2, 3$.
- **Read straight off the factored form** $y = a(x - p)(x - q)$ → roots are $x = p$ and $x = q$ (note the sign flips: $(x + 3)$ gives a root at $x = -3$).

The **axis of symmetry** is always halfway between the two $x$-intercepts: $x = \frac{p + q}{2}$.

### Effect of the dilation factor $a$

$a$ sets the **direction and width**: $a > 0$ opens **up** (vertex is a minimum), $a < 0$ opens **down** (vertex is a maximum). The **bigger** $|a|$ is, the **narrower** (steeper) the parabola; the **smaller** $|a|$ is (closer to 0), the **wider** (flatter) it is. At $a = \pm 1$ it has the same width as $y = \pm x^2$.

### Notes
- The **axis of symmetry** passes through the vertex; the parabola is a mirror image on either side of it.
- The $x$-coordinate of the vertex is always $-\frac{b}{2a}$; substitute it back to get the $y$-coordinate.
- In vertex form $y = a(x - h)^2 + k$, the vertex is $(h, k)$, so the sign **inside the bracket** is opposite to the shift: $(x - 3)^2$ shifts **right** 3, and $(x + 3)^2$ shifts **left** 3. The $k$ is straightforward: $+k$ up, $-k$ down.
- **Finding $a$ from a graph:** given the vertex $(h, k)$ and one other point $(x, y)$, $a = \frac{y - k}{(x - h)^2}$.

## Coordinate Geometry

For points $(x_1, y_1)$ and $(x_2, y_2)$:

Description | Formula
--- | --- |
Distance between two points | $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
Midpoint | $\left(\frac{x_1 + x_2}{2},\ \frac{y_1 + y_2}{2}\right)$
Gradient (slope) | $m = \frac{y_2 - y_1}{x_2 - x_1}$
Equation of a straight line | $y = mx + c$ ($m$ = gradient, $c$ = $y$-intercept)

- **Parallel** lines have **equal** gradients; for **non-vertical perpendicular** lines the gradients multiply to $-1$. (A horizontal line and a vertical line are also perpendicular.)

---

# 3. Geometry & Measurement

## Angle & Line Facts

Fact | Rule
--- | --- |
Angles on a straight line | add to $180°$
Angles around a point | add to $360°$
Angles in a triangle | add to $180°$
Angles in a quadrilateral | add to $360°$
Vertically opposite angles | are equal
Exterior angle of a triangle | equals the sum of the two opposite interior angles

**Parallel lines cut by a transversal:**
- **Corresponding** angles (F-shape) are **equal**.
- **Alternate** angles (Z-shape) are **equal**.
- **Co-interior / allied** angles (C or U-shape) add to **$180°$**.

**Polygon angles ($n$ sides):**
- Sum of the **interior** angles $= (n - 2) \cdot 180°$.
- Sum of the **exterior** angles $= 360°$ (for any polygon).
- For a **regular** polygon: each interior angle $= \frac{(n - 2) \cdot 180}{n}$ ; each exterior angle $= \frac{360}{n}$.

## Area & Perimeter Formulas

Shape | Attributes | Area | Perimeter
--- | --- | --- | --- |
Rectangle | length $l$ and width $w$ | $l \cdot w$ | $2 \cdot (l + w)$
Square | side $a$ | $a^2$ | $4 \cdot a$
Parallelogram | base $b$, height $h$ and slant side $s$ | $b \cdot h$ | $2 \cdot (b + s)$
Rhombus | side $a$, diagonals $d_1$ and $d_2$ | $\frac{d_1 \cdot d_2}{2}$ | $4 \cdot a$
Trapezium (Trapezoid) | bases $b_1$, $b_2$ and height $h$ | $\frac{(b_1 + b_2) \cdot h}{2}$ | sum of all sides
Triangle | base $b$ and height $h$ | $\frac{b \cdot h}{2}$ | sum of all sides
Equilateral Triangle | side $a$ | $\frac{\sqrt{3} \cdot a^2}{4}$ | $3 \cdot a$
Circle | radius $r$ | $\pi \cdot r^2$ | $2 \cdot \pi \cdot r$

### Circle: Arc & Sector (angle $\theta$ in degrees)

Description | Formula
--- | --- |
Diameter | $d = 2 \cdot r$
Arc length | $\frac{\theta}{360} \times 2 \pi r$
Sector area | $\frac{\theta}{360} \times \pi r^2$

## Volume & Surface Area Formulas

Shape | Attributes | Volume | Surface Area
--- | --- | --- | --- |
Cube | side $a$ | $a^3$ | $6 \cdot a^2$
Rectangular Prism | length $l$, width $w$ and height $h$ | $(l \cdot w \cdot h)$ | $(2 \cdot (l \cdot w + w \cdot h + h \cdot l))$
Cylinder | radius $r$ and height $h$ | $(\pi \cdot r^2 \cdot h)$ | $(2 \cdot \pi \cdot r^2 + 2 \cdot \pi \cdot r \cdot h)$
Cone | radius $r$ and height $h$ | $\frac{\pi \cdot r^2 \cdot h}{3}$ | $(\pi \cdot r^2 + \pi \cdot r \cdot \sqrt{r^2 + h^2})$
Sphere | radius $r$ | $\frac{4 \cdot \pi \cdot r^3}{3}$ | $4 \cdot \pi \cdot r^2$
Square-based Pyramid | base side $a$, height $h$, slant height $l$ | $\frac{a^2 \cdot h}{3}$ | $a^2 + 2 \cdot a \cdot l$

### Notes
- For **any** pyramid or cone, $\text{Volume} = \frac{1}{3} \times \text{base area} \times \text{height}$ (use the perpendicular height, not the slant height).
- The **slant height** of a square pyramid is $l = \sqrt{\left(\frac{a}{2}\right)^2 + h^2}$.
- Surface area $=$ base $+$ lateral area. For a square pyramid the 4 triangular faces give the lateral area $2 \cdot a \cdot l$.

## Faces, Edges and Vertices of common 3D shapes

Shape | Faces | Edges | Vertices
--- | --- | --- | --- |
Cube | 6 | 12 | 8
Rectangular Prism | 6 | 12 | 8
Triangular Prism | 5 | 9 | 6
Square-based Pyramid | 5 | 8 | 5
Triangular-based Pyramid (Tetrahedron) | 4 | 6 | 4
Cylinder | 3 | 2 | 0
Cone | 2 | 1 | 1
Sphere | 1 | 0 | 0

### Euler's Formula (polyhedra with flat faces only)

$$V - E + F = 2$$

- Check (cube): $8 - 12 + 6 = 2$ ✓ ; (square pyramid): $5 - 8 + 5 = 2$ ✓ ; (triangular prism): $6 - 9 + 5 = 2$ ✓.
- It works **only** for solids with flat faces (prisms, pyramids) — **not** cylinders, cones, or spheres.

### Note (school convention for curved solids)
- The counts above use the common school convention. Strictly (topologically), **curved surfaces have no edges or vertices**, so some exams count a cylinder and a cone as **0 edges / 0 vertices**. Read the question to see which version is expected.
- A **square-based pyramid** has 8 edges and 5 vertices; a **triangular-based pyramid (tetrahedron)** has 6 edges and 4 vertices — don't mix them up.

## Trigonometric Formulas

### Right Triangle

Description | Formula
--- | --- |
Pythagorean Theorem | $a^2 + b^2 = c^2$
Sine | $\sin(\theta) = \frac{opposite}{hypotenuse} = \frac{a}{c}$
Cosine | $\cos(\theta) = \frac{adjacent}{hypotenuse} = \frac{b}{c}$
Tangent | $\tan(\theta) = \frac{opposite}{adjacent} = \frac{a}{b}$
Cosecant | $\csc(\theta) = \frac{hypotenuse}{opposite} = \frac{c}{a}$
Secant | $\sec(\theta) = \frac{hypotenuse}{adjacent} = \frac{c}{b}$
Cotangent | $\cot(\theta) = \frac{adjacent}{opposite} = \frac{b}{a}$

where $a$ is the opposite side, $b$ is the adjacent side and $c$ is the hypotenuse

### Common Trigonometric Values

Memory trick: write $\sin$ as $\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2}$ for $0°, 30°, 45°, 60°, 90°$. Then $\cos$ is the **same list reversed**, and $\tan = \frac{\sin}{\cos}$.

Angle | $\sin$ | $\cos$ | $\tan$
--- | --- | --- | --- |
$0°$ | $0$ | $1$ | $0$
$30°$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{3}}$
$45°$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$
$60°$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$
$90°$ | $1$ | $0$ | undefined

- $\frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}} \approx 0.707$ and $\frac{\sqrt{3}}{2} \approx 0.866$.
- $\frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3} \approx 0.577$ and $\sqrt{3} \approx 1.732$.
- $\tan(90°)$ is **undefined** because $\cos(90°) = 0$ (you cannot divide by zero).

### Pythagorean Triples (worth memorising)

Whole-number side lengths that satisfy $a^2 + b^2 = c^2$ — spotting them saves calculation:
- $3, 4, 5$ and its multiples ($6, 8, 10$ ; $9, 12, 15$ ; $15, 20, 25$)
- $5, 12, 13$
- $8, 15, 17$
- $7, 24, 25$

### Special Right Triangles

Triangle | Angles | Side ratio (opposite each angle)
--- | --- | --- |
Isosceles right | $45° : 45° : 90°$ | $1 : 1 : \sqrt{2}$
Half-equilateral | $30° : 60° : 90°$ | $1 : \sqrt{3} : 2$

---

# 4. Counting & Probability

## Permutation and Combination Formulas

Description | Formula
--- | --- |
Factorial | $n! = n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot 2 \cdot 1$
Permutation of $k$ objects from $n$ distinct objects (order matters) | $nPk = \frac{n!}{(n - k)!}$
Combination of $k$ objects from $n$ distinct objects (order does not matter) | $nCk = \frac{n!}{k! \cdot (n - k)!}$
Permutation with repetition allowed (length $k$ from $n$ choices) | $n^k$
Circular arrangement of $n$ distinct objects (clockwise/anticlockwise considered different) | $(n - 1)!$
Circular arrangement where mirror images are considered same (necklace type, $n > 2$) | $\frac{(n - 1)!}{2}$

### Notes
- Use $nPk$ when position/order is important.
- Use $nCk$ when only selection matters, not order.
- For circular arrangements around a table, one fixed reference position removes rotational duplicates, so use $(n - 1)!$.
- **Handshakes** in a group of $n$ people $= \frac{n \cdot (n - 1)}{2}$ (this is just $nC2$ — each pair shakes once).
- **Diagonals** in a polygon with $n$ sides $= \frac{n \cdot (n - 3)}{2}$.

## Probability

Description | Formula
--- | --- |
Probability of an event | $\frac{\text{favourable outcomes}}{\text{total outcomes}}$

- Probability is always between $0$ (impossible) and $1$ (certain).
- $P(\text{not } A) = 1 - P(A)$.

---

# 5. Reasoning Aids (Verbal & Numerical)

## Letter–Number Values ($A=1 \ldots Z=26$)

Used constantly in **numerical and verbal reasoning** codes (e.g. shift each letter forward by 3).

A | B | C | D | E | F | G | H | I | J | K | L | M
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13

N | O | P | Q | R | S | T | U | V | W | X | Y | Z
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26

- **Anchor letters to recall fast:** $E = 5$, $J = 10$, $O = 15$, $T = 20$, $Y = 25$, and $Z = 26$.
- The vowels are $A = 1$, $E = 5$, $I = 9$, $O = 15$, $U = 21$.
- **Reverse value** (Z=1 … A=26): reverse value $= 27 - (\text{normal value})$. e.g. $C = 3$, reverse $= 24$.

## Roman Numerals

Symbol | I | V | X | L | C | D | M
--- | --- | --- | --- | --- | --- | --- | --- |
Value | 1 | 5 | 10 | 50 | 100 | 500 | 1000

**How to read:** add symbols left to right; but when a smaller symbol comes **before** a larger one, you **subtract** it.

- Subtractive pairs: $IV = 4$, $IX = 9$, $XL = 40$, $XC = 90$, $CD = 400$, $CM = 900$.
- A symbol repeats at most **three** times in a row ($III = 3$, but $4$ is $IV$, not $IIII$).
- Examples: $XXVII = 27$, $XLIX = 49$, $MMXXIV = 2024$.
- Memory phrase for the order: **I**vy **V**ines **X**tend **L**ush **C**limbing **D**own **M**aples.
