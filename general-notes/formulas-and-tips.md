# Formulas and Tips

## General Formulas

Description | Formula
--- | --- |
sum of the first $n$ natural numbers | $\frac{n \cdot (n + 1)}{2}$
sum of the first $n$ even numbers | $n \cdot (n + 1)$
sum of the first $n$ odd numbers | $n^2$
sum of the first $n$ squares | $\frac{n \cdot (n + 1) \cdot (2 \cdot n + 1)}{6}$
sum of the first $n$ cubes | $\left(\frac{n \cdot (n + 1)}{2}\right)^2$
The number of handshake in a group of $n$ people | $\frac{n \cdot (n - 1)}{2}$
The number of diagonals in a polygon with $n$ sides | $\frac{n \cdot (n - 3)}{2}$
The sum of the interior angles of a polygon with $n$ sides | $(n - 2) \cdot 180$
The sum of the exterior angles of a polygon with $n$ sides | $360$

## Permutation and Combination Formulas

Description | Formula
--- | --- |
Factorial | $n! = n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot 2 \cdot 1$
Permutation of $k$ objects from $n$ distinct objects (order matters) | $nPk = \frac{n!}{(n - k)!}$
Combination of $k$ objects from $n$ distinct objects (order does not matter) | $nCk = \frac{n!}{k! \cdot (n - k)!}$
Permutation with repetition allowed (length $k$ from $n$ choices) | $n^k$
Circular arrangement of $n$ distinct objects (clockwise/anticlockwise considered different) | $(n - 1)!$
Circular arrangement where mirror images are considered same (necklace type) | $\frac{(n - 1)!}{2}$

### Notes
- Use $nPk$ when position/order is important.
- Use $nCk$ when only selection matters, not order.
- For circular arrangements around a table, one fixed reference position removes rotational duplicates, so use $(n - 1)!$.

## Area & Perimeter Formulas

Shape | Attributes | Area | Perimeter
--- | --- | --- | --- |
Rectangle | length $l$ and width $w$ | $l \cdot w$ | $2 \cdot (l + w)$
Square | side $a$ | $a^2$ | $4 \cdot a$
Parallelogram | base $b$ and height $h$ | $b \cdot h$ | $2 \cdot (b + h)$
Rhombus | side $a$, diagonals $d_1$ and $d_2$ | $\frac{d_1 \cdot d_2}{2}$ | $4 \cdot a$
Trapezoid | bases $b_1$, $b_2$ and height $h$ | $\frac{(b_1 + b_2) \cdot h}{2}$ | sum of all sides
Triangle | base $b$ and height $h$ | $\frac{b \cdot h}{2}$ | sum of all sides
Equilateral Triangle | side $a$ | $\frac{\sqrt{3} \cdot a^2}{4}$ | $3 \cdot a$
Circle | radius $r$ | $\pi \cdot r^2$ | $2 \cdot \pi \cdot r$

## Volume & Surface Area Formulas

Shape | Attributes | Volume | Surface Area
--- | --- | --- | --- |
Cube | side $a$ | $a^3$ | $6 \cdot a^2$
Rectangular Prism | length $l$, width $w$ and height $h$ | $(l \cdot w \cdot h)$ | $(2 \cdot (l \cdot w + w \cdot h + h \cdot l))$
Cylinder | radius $r$ and height $h$ | $(\pi \cdot r^2 \cdot h)$ | $(2 \cdot \pi \cdot r^2 + 2 \cdot \pi \cdot r \cdot h)$
Cone | radius $r$ and height $h$ | $\frac{\pi \cdot r^2 \cdot h}{3}$ | $(\pi \cdot r^2 + \pi \cdot r \cdot \sqrt{r^2 + h^2})$
Sphere | radius $r$ | $\frac{4 \cdot \pi \cdot r^3}{3}$ | $4 \cdot \pi \cdot r^2$
Pyramid | base area $B$ and height $h$ | $\frac{B \cdot h}{3}$ | $B + \sqrt{B^2 + 4 \cdot h^2}$

## Edges and Vertices of common 3D shapes

Shape | Edges | Vertices
--- | --- | --- |
Cube | 12 | 8
Rectangular Prism | 12 | 8
Cylinder | 3 (2 bases and 1 side) | 2 (top and bottom)
Cone | 1 (base) | 1 (apex)
Sphere | N/A | N/A
Pyramid | 8 | 5

### Note:
- For the Sphere, since it is a curved surface with no edges or vertices, the values are marked as N/A (not applicable).
- For the Cylinder, it has 3 edges (2 bases and 1 side) and 2 vertices (top and bottom).
- For the Cone, it has 1 edge (the base) and 1 vertex (the apex).
- For the Pyramid, the number of edges and vertices can vary depending on the type and base shape of the pyramid. It may have a different number of edges and vertices based on its base (triangular, square, pentagonal, etc.).

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