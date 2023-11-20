\title{

REAL AND
![](https://cdn.mathpix.com/cropped/2023_11_05_7e12dc896954aac605c1g-001.jpg?height=260&width=770&top_left_y=360&top_left_x=225)

Walter Rudin

Third Edition

# REAL AND <br> COMPLEX <br> ANALYSIS 

Third Edition

Walter Rudin

Professor of Mathematics

University of Wisconsin, Madison

## McGraw-Hill Book Company

New York St. Louis San Francisco Auckland Bogotá Hamburg London Madrid Mexico Milan Montreal New Delhi

Panama Paris São Paulo Singapore Sydney Tokyo Toronto

## REAL AND COMPLEX ANALYSIS

INTERNATIONAL EDITION 1987

Exclusive rights by McGraw-Hill Book Co., Singapore for manufacture and export. This book cannot be re-exported from the country to which it is consigned by McGraw-Hill.

## $012345678920 \mathrm{BJE} 9876$

Copyright $\odot 1987,1974,1966$ by McGraw-Hill, Inc.

All rights reserved. No part of this publication may be reproduced or distributed in any form or by any means, or stored in a data base or a retrieval system, without the prior written permission of the publisher.

This book was set in Times Roman.

The editor was Peter R. Devine.

The production supervisor was Diane Renda.

## Library of Congress Cataloging-in-Publication Data

Rudin, Walter, 1921 -

Real and complex analysis.

Bibliography: $p$.

Includes index.

1. Mathematical analysis. I. Title.

QA300.R82 1987515 86-7

ISBN 0-07-054234-1

When ordering this title use ISBN 0-07-100276-6

## ABOUT THE AUTHOR

Walter Rudin is the author of three textbooks, Principles of Mathematical Analysis, Real and Complex Analysis, and Functional Analysis, whose widespread use is illustrated by the fact that they have been translated into a total of 13 languages. He wrote the first of these while he was a C.L.E. Moore Instructor at M.I.T., just two years after receiving his Ph.D. at Duke University in 1949. Later he taught at the University of Rochester, and is now a Vilas Research Professor at the University of Wisconsin-Madison, where he has been since 1959.

He has spent leaves at Yale University, at the University of California in La Jolla, and at the University of Hawaii.

His research has dealt mainly with harmonic analysis and with complex variables. He has written three research monographs on these topics, Fourier Analysis on Groups, Function Theory in Polydiscs, and Function Theory in the Unit Ball of $\mathrm{C}^{\mathbf{n}}$.

Preface $\quad$ xiii

Prologue: The Exponential Function 1
Chapter 1 Abstract Integration 5

$\begin{array}{ll}\text { Set-theoretic notations and terminology } & 6\end{array}$

$\begin{array}{ll}\text { The concept of measurability } & \mathbf{8}\end{array}$

$\begin{array}{ll}\text { Simple functions } & 15\end{array}$

$\begin{array}{ll}\text { Elementary properties of measures } & 16\end{array}$

![](https://cdn.mathpix.com/cropped/2023_11_05_7e12dc896954aac605c1g-008.jpg?height=40&width=968&top_left_y=1141&top_left_x=330)

$\begin{array}{ll}\text { Integration of positive functions } & 19\end{array}$

Integration of complex functions $\quad 24$

$\begin{array}{ll}\text { The role played by sets of measure zero } & 27\end{array}$

Exercises 31

Chapter 2 Positive Borel Measures 33

Vector spaces 33

Topological preliminaries $\quad 35$

The Riesz representation theorem $\quad 40$

Regularity properties of Borel measures 47

$\begin{array}{ll}\text { Lebesgue measure } & 49\end{array}$

Continuity properties of measurable functions $\quad 55$

$\begin{array}{ll}\text { Exercises } & 57\end{array}$

$\begin{array}{lll}\text { Chapter } 3 & L^{p} \text {-Spaces } & 61\end{array}$

Convex functions and inequalities $\quad 61$

The $L^{p}$-spaces $\quad 65$

Approximation by continuous functions $\quad 69$

$\begin{array}{ll}\text { Exercises } & 71\end{array}$
Chapter 4 Elementary Hilbert Space Theory ..... 76
Inner products and linear functionals ..... 76
Orthonormal sets ..... 82
Trigonometric series ..... 88
Exercises ..... 92
Chapter 5 Examples of Banach Space Techniques ..... 95
Banach spaces ..... 95
Consequences of Baire's theorem ..... 97
Fourier series of continuous functions ..... 100
Fourier coefficients of $L^{1}$-functions ..... 103
The Hahn-Banach theorem ..... 104
An abstract approach to the Poisson integral ..... 108
Exercises ..... 112
Chapter 6 Complex Measures ..... 116
Total variation ..... 116
Absolute continuity ..... 120
Consequences of the Radon-Nikodym theorem ..... 124
Bounded linear functionals on $L^{p}$ ..... 126
The Riesz representation theorem ..... 129
Exercises ..... 132
Chapter 7 Differentiation ..... 135
Derivatives of measures ..... 135
The fundamental theorem of Calculus ..... 144
Differentiable transformations ..... 150
Exercises ..... 156
Chapter 8 Integration on Product Spaces ..... 160
Measurability on cartesian products ..... 160
Product measures ..... 163
The Fubini theorem ..... 164
Completion of product measures ..... 167
Convolutions ..... 170
Distribution functions ..... 172
Exercises ..... 174
Chapter 9 Fourier Transforms ..... 178
Formal properties ..... 178
The inversion theorem ..... 180
The Plancherel theorem ..... 185
The Banach algebra $L^{1}$ ..... 190
Exercises ..... 193
Chapter 10 Elementary Properties of Holomorphic Functions ..... 196
Complex differentiation ..... 196
Integration over paths ..... 200
The local Cauchy theorem ..... 204
The power series representation ..... 208
The open mapping theorem ..... 214
The global Cauchy theorem ..... 217
The calculus of residues ..... 224
Exercises ..... 227
Chapter 11 Harmonic Functions ..... 231
The Cauchy-Riemann equations ..... 231
The Poisson integral ..... 233
The mean value property ..... 237
Boundary behavior of Poisson integrals ..... 239
Representation theorems ..... 245
Exercises ..... 249
Chapter 12 The Maximum Modulus Principle ..... 253
Introduction ..... 253
The Schwarz lemma ..... 254
The Phragmen-Lindelöf method ..... 256
An interpolation theorem ..... 260
A converse of the maximum modulus theorem ..... 262
Exercises ..... 264
Chapter 13 Approximation by Rational Functions ..... 266
Preparation ..... 266
Runge's theorem ..... 270
The Mittag-Leffler theorem ..... 273
Simply connected regions ..... 274
Exercises ..... 276
Chapter 14 Conformal Mapping ..... 278
Preservation of angles ..... 278
Linear fractional transformations ..... 279
Normal families ..... 281
The Riemann mapping theorem ..... 282
The class $\mathscr{S}$ ..... 285
Continuity at the boundary ..... 289
Conformal mapping of an annulus ..... 291
Exercises ..... 293
Chapter 15 Zeros of Holomorphic Functions ..... 298
Infinite products ..... 298
The Weierstrass factorization theorem ..... 301
An interpolation problem ..... 304
Jensen's formula ..... 307
Blaschke products ..... 310
The Müntz-Szasz theorem ..... 312
Exercises ..... 315
Chapter 16 Analytic Continuation ..... 319
Regular points and singular points ..... 319
Continuation along curves ..... 323
The monodromy theorem ..... 326
Construction of a modular function ..... 328
The Picard theorem ..... 331
Exercises ..... 332
Chapter $17 H^{p}$-Spaces ..... 335
Subharmonic functions ..... 335
The spaces $H^{p}$ and $N$ ..... 337
The theorem of F. and M. Riesz ..... 341
Factorization theorems ..... 342
The shift operator ..... 346
Conjugate functions ..... 350
Exercises ..... 352
Chapter 18 Elementary Theory of Banach Algebras ..... 356
Introduction ..... 356
The invertible elements ..... 357
Ideals and homomorphisms ..... 362
Applications ..... 365
Exercises ..... 369
Chapter 19 Holomorphic Fourier Transforms ..... 371
Introduction ..... 371
Two theorems of Paley and Wiener ..... 372
Quasi-analytic classes ..... 377
The Denjoy-Carleman theorem ..... 380
Exercises ..... 383
Chapter 20 Uniform Approximation by Polynomials ..... 386
Introduction ..... 386
Some lemmas ..... 387
Mergelyan's theorem ..... 390
Exercises ..... 394
Appendix : Hausdorff's Maximality Theorem ..... 395
Notes and Comments ..... 397
Bibliography ..... 405
List of Special Symbols ..... 407
Index ..... 409

This book contains a first-year graduate course in which the basic techniques and theorems of analysis are presented in such a way that the intimate connections between its various branches are strongly emphasized. The traditionally separate subjects of "real analysis" and "complex analysis" are thus united; some of the basic ideas from functional analysis are also included.

Here are some examples of the way in which these connections are demonstrated and exploited. The Riesz representation theorem and the Hahn-Banach theorem allow one to "guess" the Poisson integral formula. They team up in the proof of Runge's theorem. They combine with Blaschke's theorem on the zeros of bounded holomorphic functions to give a proof of the Müntz-Szasz theorem, which concerns approximation on an interval. The fact that $L^{2}$ is a Hilbert space is used in the proof of the Radon-Nikodym theorem, which leads to the theorem about differentiation of indefinite integrals, which in turn yields the existence of radial limits of bounded harmonic functions. The theorems of Plancherel and Cauchy combined give a theorem of Paley and Wiener which, in turn, is used in the Denjoy-Carleman theorem about infinitely differentiable functions on the real line. The maximum modulus theorem gives information about linear transformations on $L^{p}$-spaces.

Since most of the results presented here are quite classical (the novelty lies in the arrangement, and some of the proofs are new), I have not attempted to document the source of every item. References are gathered at the end, in Notes and Comments. They are not always to the original sources, but more often to more recent works where further references can be found. In no case does the absence of a reference imply any claim to originality on my part.

The prerequisite for this book is a good course in advanced calculus (settheoretic manipulations, metric spaces, uniform continuity, and uniform convergence). The first seven chapters of my earlier book "Principles of Mathematical Analysis" furnish sufficient preparation.

Experience with the first edition shows that first-year graduate students can study the first 15 chapters in two semesters, plus some topics from 1 or 2 of the remaining 5. These latter are quite independent of each other. The first 15 should be taken up in the order in which they are presented, except for Chapter 9, which can be postponed.

The most important difference between this third edition and the previous ones is the entirely new chapter on differentiation. The basic facts about differentiation are now derived from the existence of Lebesgue points, which in turn is an easy consequence of the so-called "weak type" inequality that is satisfied by the maximal functions of measures on euclidean spaces. This approach yields strong theorems with minimal effort. Even more important is that it familiarizes students with maximal functions, since these have become increasingly useful in several areas of analysis.

One of these is the study of the boundary behavior of Poisson integrals. A related one concerns $\mathbf{H}^{\mathrm{p}}$-spaces. Accordingly, large parts of Chapters 11 and 17 were rewritten and, I hope, simplified in the process.

I have also made several smaller changes in order to improve certain details: For example, parts of Chapter 4 have been simplified; the notions of equicontinuity and weak convergence are presented in more detail; the boundary behavior of conformal maps is studied by means of Lindelöf's theorem about asymptotic valued of bounded holomorphic functions in a disc.

Over the last 20 years, numerous students and colleagues have offered comments and criticisms concerning the content of this book. I sincerely appreciated all of these, and have tried to follow some of them. As regards the present edition, my thanks go to Richard Rochberg for some useful last-minute suggestions, and I especially thank Robert Burckel for the meticulous care with which he examined the entire manuscript.

## PROLOGUE <br> THE EXPONENTIAL FUNCTION

This is the most important function in mathematics. It is defined, for every complex number $z$, by the formula

$$
\exp (z)=\sum_{n=0}^{\infty} \frac{z^{n}}{n !}
$$

The series (1) converges absolutely. for every $z$ and converges uniformly on every bounded subset of the complex plane. Thus exp is a continuous function. The absolute convergence of (1) shows that the computation

$$
\sum_{k=0}^{\infty} \frac{a^{k}}{k !} \sum_{m=0}^{\infty} \frac{b^{m}}{m !}=\sum_{n=0}^{\infty} \frac{1}{n !} \sum_{k=0}^{n} \frac{n !}{k !(n-k) !} a^{k} b^{n-k}=\sum_{n=0}^{\infty} \frac{(a+b)^{n}}{n !}
$$

is correct. It gives the important addition formula

$$
\exp (a) \exp (b)=\exp (a+b)
$$

valid for all complex numbers $a$ and $b$.

We define the number $e$ to be $\exp (1)$, and shall usually replace $\exp (z)$ by the customary shorter expression $e^{z}$. Note that $e^{0}=\exp (0)=1$, by (1).

## Theorem

(a) For every complex $z$ we have $e^{z} \neq 0$.

(b) exp is its own derivative: $\exp ^{\prime}(z)=\exp (z)$.
(c) The restriction of $\exp$ to the real axis is a monotonically increasing positive function, and

$$
e^{x} \rightarrow \infty \text { as } x \rightarrow \infty, \quad e^{x} \rightarrow 0 \text { as } x \rightarrow-\infty
$$

(d) There exists a positive number $\pi$ such that $e^{\pi i / 2}=i$ and such that $e^{z}=1$ if and only if $z /(2 \pi i)$ is an integer.

(e) $\exp$ is a periodic function, with period $2 \pi i$.

(f) The mapping $t \rightarrow e^{i t}$ maps the real axis onto the unit circle.

(g) If $w$ is a complex number and $w \neq 0$, then $w=e^{z}$ for some $z$.

Proof By (2), $e^{z} \cdot e^{-z}=e^{z-z}=e^{0}=1$. This implies $(a)$. Next,

$$
\exp ^{\prime}(z)=\lim _{h \rightarrow 0} \frac{\exp (z+h)-\exp (z)}{h}=\exp (z) \lim _{h \rightarrow 0} \frac{\exp (h)-1}{h}=\exp (z) .
$$

The first of the above equalities is a matter of definition, the second follows from (2), and the third from (1), and $(b)$ is proved.

That exp is monotonically increasing on the positive real axis, and that $e^{x} \rightarrow \infty$ as $x \rightarrow \infty$, is clear from (1). The other assertions of $(c)$ are consequences of $e^{x} \cdot e^{-x}=1$.

For any real number $t$, (1) shows that $e^{-i t}$ is the complex conjugate of $e^{i t}$. Thus

$$
\left|e^{i t}\right|^{2}=e^{i t} \cdot \overline{e^{i t}}=e^{i t} \cdot e^{-i t}=e^{i t-i t}=e^{0}=1
$$

or

$$
\left|e^{i t}\right|=1 \quad(t \text { real })
$$

In other words, if $t$ is real, $e^{i t}$ lies on the unit circle. We define $\cos t, \sin t$ to be the real and imaginary parts of $e^{i t}$ :

$$
\cos t=\operatorname{Re}\left[e^{i t}\right], \quad \sin t=\operatorname{Im}\left[e^{i t}\right] \quad(t \text { real })
$$

If we differentiate both sides of Euler's identity

$$
e^{i t}=\cos t+i \sin t
$$

which is equivalent to (4), and if we apply $(b)$, we obtain

$$
\cos ^{\prime} t+i \sin ^{\prime} t=i e^{i t}=-\sin t+i \cos t,
$$

so that

$$
\cos ^{\prime}=-\sin , \quad \sin ^{\prime}=\cos
$$

The power series (1) yields the representation

$$
\cos t=1-\frac{t^{2}}{2 !}+\frac{t^{4}}{4 !}-\frac{t^{6}}{6 !}+\cdots
$$

Take $t=2$. The terms of the series (7) then decrease in absolute value (except for the first one) and their signs alternate. Hence $\cos 2$ is less than the sum of the first three terms of (7), with $t=2$; thus $\cos 2<-\frac{1}{3}$. Since $\cos 0=1$ and $\cos$ is a continuous real function on the real axis, we conclude that there is a smallest positive number $t_{0}$ for which $\cos t_{0}=0$. We define

$$
\pi=2 t_{0}
$$

It follows from (3) and (5) that $\sin t_{0}= \pm 1$. Since

$$
\sin ^{\prime}(t)=\cos t>0
$$

on the segment $\left(0, t_{0}\right)$ and since $\sin 0=0$, we have $\sin t_{0}>0$, hence $\sin t_{0}=$ 1 , and therefore

$$
e^{\pi i / 2}=i
$$

It follows that $e^{\pi i}=i^{2}=-1, e^{2 \pi i}=(-1)^{2}=1$, and then $e^{2 \pi i n}=1$ for every integer $n$. Also, $(e)$ follows immediately:

$$
e^{z+2 \pi i}=e^{z} e^{2 \pi i}=e^{z}
$$

If $z=x+i y, x$ and $y$ real, then $e^{z}=e^{x} e^{i y}$; hence $\left|e^{z}\right|=e^{x}$. If $e^{z}=1$, we therefore must have $e^{x}=1$, so that $x=0$; to prove that $y / 2 \pi$ must be an integer, it is enough to show that $e^{i y} \neq 1$ if $0<y<2 \pi$, by (10).

Suppose $0<y<2 \pi$, and

$$
e^{i y / 4}=u+i v \quad(u \text { and } v \text { real })
$$

Since $0<y / 4<\pi / 2$, we have $u>0$ and $v>0$. Also

$$
e^{i y}=(u+i v)^{4}=u^{4}-6 u^{2} v^{2}+v^{4}+4 i u v\left(u^{2}-v^{2}\right)
$$

The right side of (12) is real only if $u^{2}=v^{2}$; since $u^{2}+v^{2}=1$, this happens only when $u^{2}=v^{2}=\frac{1}{2}$, and then (12) shows that

$$
e^{i y}=-1 \neq 1
$$

This completes the proof of $(d)$.

We already know that $t \rightarrow e^{i t}$ maps the real axis into the unit circle. To prove $(f)$, fix $w$ so that $|w|=1$; we shall show that $w=e^{i t}$ for some real $t$. Write $w=u+i v, u$ and $v$ real, and suppose first that $u \geq 0$ and $v \geq 0$. Since $u \leq 1$, the definition of $\pi$ shows that there exists a $t, 0 \leq t \leq \pi / 2$, such that $\cos t=u$; then $\sin ^{2} t=1-u^{2}=v^{2}$, and since $\sin t \geq 0$ if $0 \leq t \leq \pi / 2$, we have $\sin t=v$. Thus $w=e^{i t}$.

If $u<0$ and $v \geq 0$, the preceding conditions are satisfied by $-i w$. Hence $-i w=e^{i t}$ for some real $t$, and $w=e^{i(t+\pi / 2)}$. Finally, if $v<0$, the preceding two cases show that $-w=e^{i t}$ for some real $t$, hence $w=e^{i(t+\pi)}$. This completes the proof of $(f)$.

If $w \neq 0$, put $\alpha=w /|w|$. Then $w=|w| \alpha$. By (c), there is a real $x$ such that $|w|=e^{x}$. Since $|\alpha|=1,(f)$ shows that $\alpha=e^{i y}$ for some real $y$. Hence $w=e^{x+i y}$. This proves $(g)$ and completes the theorem.

## 4 REAL AND COMPLEX ANALYSIS

We shall encounter the integral of $\left(1+x^{2}\right)^{-1}$ over the real line. To evaluate it, put $\varphi(t)=\sin t / \cos t$ in $(-\pi / 2, \pi / 2)$. By $(6), \varphi^{\prime}=1+\varphi^{2}$. Hence $\varphi$ is a monotonically increasing mapping of $(-\pi / 2, \pi / 2)$ onto $(-\infty, \infty)$, and we obtain

$$
\int_{-\infty}^{\infty} \frac{d x}{1+x^{2}}=\int_{-\pi / 2}^{\pi / 2} \frac{\varphi^{\prime}(t) d t}{1+\varphi^{2}(t)}=\int_{-\pi / 2}^{\pi / 2} d t=\pi
$$

## ABSTRACT INTEGRATION

Toward the end of the nineteenth century it became clear to many mathematicians that the Riemann integral (about which one learns in calculus courses) should be replaced by some other type of integral, more general and more flexible, better suited for dealing with limit processes. Among the attempts made in this direction, the most notable ones were due to Jordan, Borel, W. H. Young, and Lebesgue. It was Lebesgue's construction which turned out to be the most successful.

In brief outline, here is the main idea: The Riemann integral of a function $f$ over an interval $[a, b]$ can be approximated by sums of the form

$$
\sum_{i=1}^{n} f\left(t_{i}\right) m\left(E_{i}\right)
$$

where $E_{1}, \ldots, E_{n}$ are disjoint intervals whose union is $[a, b], m\left(E_{i}\right)$ denotes the length of $E_{i}$, and $t_{i} \in E_{i}$ for $i=1, \ldots, n$. Lebesgue discovered that a completely satisfactory theory of integration results if the sets $E_{i}$ in the above sum are allowed to belong to a larger class of subsets of the line, the so-called "measurable sets," and if the class of functions under consideration is enlarged to what he called "measurable functions." The crucial set-theoretic properties involved are the following: The union and the intersection of any countable family of measurable sets are measurable; so is the complement of every measurable set; and, most important, the notion of "length" (now called "measure") can be extended to them in such a way that

$$
m\left(E_{1} \cup E_{2} \cup E_{3} \cup \cdots\right)=m\left(E_{1}\right)+m\left(E_{2}\right)+m\left(E_{3}\right)+\cdots
$$

for every countable collection $\left\{E_{i}\right\}$ of pairwise disjoint measurable sets. This property of $m$ is called countable additivity.

The passage from Riemann's theory of integration to that of Lebesque is a process of completion (in a sense which will appear more precisely later). It is of the same fundamental importance in analysis as is the construction of the real number system from the rationals.

The above-mentioned measure $m$ is of course intimately related to the geometry of the real line. In this chapter we shall present an abstract (axiomatic) version of the Lebesgue integral, relative to any countably additive measure on any set. (The precise definitions follow.) This abstract theory is not in any way more difficult than the special case of the real line; it shows that a large part of integration theory is independent of any geometry (or topology) of the underlying space; and, of course, it gives us a tool of much wider applicability. The existence of a large class of measures, among them that of Lebesgue, will be established in Chap. 2.

## Set-Theoretic Notations and Terminology

1.1 Some sets can be described by listing their members. Thus $\left\{x_{1}, \ldots, x_{n}\right\}$ is the set whose members are $x_{1}, \ldots, x_{n}$; and $\{x\}$ is the set whose only member is $x$. More often, sets are described by properties. We write

$$
\{x: P\}
$$

for the set of all elements $x$ which have the property $P$. The symbol $\varnothing$ denotes the empty set. The words collection, family, and class will be used synonymously with set.

We write $x \in A$ if $x$ is a member of the set $A$; otherwise $x \notin A$. If $B$ is a subset of $A$, i.e., if $x \in B$ implies $x \in A$, we write $B \subset A$. If $B \subset A$ and $A \subset B$, then $A=B$. If $B \subset A$ and $A \neq B, B$ is a proper subset of $A$. Note that $\varnothing \subset A$ for every set $A$.

$A \cup B$ and $A \cap B$ are the union and intersection of $A$ and $B$, respectively. If $\left\{A_{\alpha}\right\}$ is a collection of sets, where $\alpha$ runs through some index set $I$, we write

$$
\bigcup_{\alpha \in I} A_{\alpha} \text { and } \bigcap_{\alpha \in I} A_{\alpha}
$$

for the union and intersection of $\left\{A_{\alpha}\right\}$ :

$$
\begin{aligned}
& \bigcup_{\alpha \in I} A_{\alpha}=\left\{x: x \in A_{\alpha} \text { for at least one } \alpha \in I\right\} \\
& \bigcap_{\alpha \in I} A_{\alpha}=\left\{x: x \in A_{\alpha} \text { for every } \alpha \in I\right\}
\end{aligned}
$$

If $I$ is the set of all positive integers, the customary notations are

$$
\bigcup_{n=1}^{\infty} A_{n} \text { and } \bigcap_{n=1}^{\infty} A_{n}
$$

If no two members of $\left\{A_{\alpha}\right\}$ have an element in common, then $\left\{A_{\alpha}\right\}$ is a disjoint collection of sets:

We write $A-B=\{x: x \in A, x \notin B\}$, and denote the complement of $A$ by $A^{c}$ whenever it is clear from the context with respect to which larger set the complement is taken.

The cartesian product $A_{1} \times \cdots \times A_{n}$ of the sets $A_{1}, \ldots, A_{n}$ is the set of all ordered $n$-tuples $\left(a_{1}, \ldots, a_{n}\right)$ where $a_{i} \in A_{i}$ for $i=1, \ldots, n$.

The real line (or real number system) is $R^{1}$, and

$$
R^{k}=R^{1} \times \cdots \times R^{1} \quad(k \text { factors })
$$

The extended real number system is $R^{1}$ with two symbols, $\infty$ and $-\infty$, adjoined, and with the obvious ordering. If $-\infty \leq a \leq b \leq \infty$, the interval $[a, b]$ and the segment $(a, b)$ are defined to be

$$
[a, b]=\{x: a \leq x \leq b\}, \quad(a, b)=\{x: a<x<b\}
$$

We also write

$$
[a, b)=\{x: a \leq x<b\}, \quad(a, b]=\{x: a<x \leq b\}
$$

If $E \subset[-\infty, \infty]$ and $E \neq \varnothing$, the least upper bound (supremum) and greatest lower bound (infimum) of $E$ exist in $[-\infty, \infty]$ and are denoted by sup $E$ and inf $E$.

Sometimes (but only when $\sup E \in E$ ) we write $\max E$ for $\sup E$.

The symbol

$$
f: X \rightarrow Y
$$

means that $f$ is a function (or mapping or transformation) of the set $X$ into the set $Y$; i.e., $f$ assigns to each $x \in X$ an element $f(x) \in Y$. If $A \subset X$ and $B \subset Y$, the image of $A$ and the inverse image (or pre-image) of $B$ are

$$
\begin{aligned}
f(A) & =\{y: y=f(x) \text { for some } x \in A\} \\
f^{-1}(B) & =\{x: f(x) \in B\} .
\end{aligned}
$$

Note that $f^{-1}(B)$ may be empty even when $B \neq \varnothing$.

The domain of $f$ is $X$. The range of $f$ is $f(X)$.

If $f(X)=Y, f$ is said to map $X$ onto $Y$.

We write $f^{-1}(y)$, instead of $f^{-1}(\{y\})$, for every $y \in Y$. If $f^{-1}(y)$ consists of at most one point, for each $y \in Y, f$ is said to be one-to-one. If $f$ is one-to-one, then $f^{-1}$ is a function with domain $f(X)$ and range $X$.

If $f: X \rightarrow[-\infty, \infty]$ and $E \subset X$, it is customary to write $\sup _{x \in E} f(x)$ rather than $\sup f(E)$.

If $f: X \rightarrow Y$ and $g: Y \rightarrow Z$, the composite function $g \circ f: X \rightarrow Z$ is defined by the formula

$$
(g \circ f)(x)=g(f(x)) \quad(x \in X) .
$$

If the range of $f$ lies in the real line (or in the complex plane), then $f$ is said to be a real function (or a complex function). For a complex function $f$, the statement " $f \geq 0$ " means that all values $f(x)$ of $f$ are nonnegative real numbers.

## The Concept of Measurability

The class of measurable functions plays a fundamental role in integration theory. It has some basic properties in common with another most important class of functions, namely, the continuous ones. It is helpful to keep these similarities in mind. Our presentation is therefore organized in such a way that the analogies between the concepts topological space, open set, and continuous function, on the one hand, and measurable space, measurable set, and measurable function, on the other, are strongly emphasized. It seems that the relations between these concepts emerge most clearly when the setting is quite abstract, and this (rather than a desire for mere generality) motivates our approach to the subject.

### 1.2 Definition

(a) A collection $\tau$ of subsets of a set $X$ is said to be a topology in $X$ if $\tau$ has the following three properties:

(i) $\varnothing \in \tau$ and $X \in \tau$.

(ii) If $V_{i} \in \tau$ for $i=1, \ldots, n$, then $V_{1} \cap V_{2} \cap \cdots \cap V_{n} \in \tau$.

(iii) If $\left\{V_{\alpha}\right\}$ is an arbitrary collection of members of $\tau$ (finite, countable, or uncountable), then $\bigcup_{\alpha} V_{\alpha} \in \tau$.

(b) If $\tau$ is a topology in $X$, then $X$ is called a topological space, and the members of $\tau$ are called the open sets in $X$.

(c) If $X$ and $Y$ are topological spaces and if $f$ is a mapping of $X$ into $Y$, then $f$ is said to be continuous provided that $f^{-1}(V)$ is an open set in $X$ for every open set $V$ in $Y$.

### 1.3 Definition

(a) A collection $\mathfrak{M}$ of subsets of a set $X$ is said to be a $\sigma$-algebra in $X$ if $\mathfrak{M}$ has the following properties:

(i) $X \in \mathfrak{M}$.

(ii) If $A \in \mathfrak{M}$, then $A^{\mathfrak{c}} \in \mathfrak{M}$, where $A^{c}$ is the complement of $A$ relative to $X$.

(iii) If $A=\bigcup_{n=1}^{\infty} A_{n}$ and if $A_{n} \in \mathfrak{M}$ for $n=1,2,3, \ldots$, then $A \in \mathfrak{M}$.

(b) If $\mathfrak{M}$ is a $\sigma$-algebra in $X$, then $X$ is called a measurable space, and the members of $\mathfrak{M}$ are called the measurable sets in $X$.

(c) If $X$ is a measurable space, $Y$ is a topological space, and $f$ is a mapping of $X$ into $Y$, then $f$ is said to be measurable provided that $f^{-1}(V)$ is a measurable set in $X$ for every open set $V$ in $Y$.

It would perhaps be more satisfactory to apply the term "measurable space" to the ordered pair $(X, \mathfrak{M})$, rather than to $X$. After all, $X$ is a set, and $X$ has not been changed in any way by the fact that we now also have a $\sigma$-algebra of its subsets in mind. Similarly, a topological space is an ordered pair $(X, \tau)$. But if this sort of thing were systematically done in all mathematics, the terminology would become awfully cumbersome. We shall discuss this again at somewhat greater length in Sec. 1.21.

1.4 Comments on Definition 1.2 The most familiar topological spaces are the metric spaces. We shall assume some familiarity with metric spaces but shall give the basic definitions, for the sake of completeness.

A metric space is a set $X$ in which a distance function (or metric) $\rho$ is defined, with the following properties:

(a) $0 \leq \rho(x, y)<\infty$ for all $x$ and $y \in X$.

(b) $\rho(x, y)=0$ if and only if $x=y$.

(c) $\rho(x, y)=\rho(y, x)$ for all $x$ and $y \in X$.

(d) $\rho(x, y) \leq \rho(x, z)+\rho(z, y)$ for all $x, y$, and $z \in X$.

Property $(d)$ is called the triangle inequality.

If $x \in X$ and $r \geq 0$, the open ball with center at $x$ and radius $r$ is the set $\{y \in X: \rho(x, y)<r\}$.

If $X$ is a metric space and if $\tau$ is the collection of all sets $E \subset X$ which are arbitrary unions of open balls, then $\tau$ is a topology in $X$. This is not hard to verify; the intersection property depends on the fact that if $x \in B_{1} \cap B_{2}$, where $B_{1}$ and $B_{2}$ are open balls, then $x$ is the center of an open ball $B \subset B_{1} \cap B_{2}$. We leave this as an exercise.

For instance, in the real line $R^{1}$ a set is open if and only if is a union of open segments $(a, b)$. In the plane $R^{2}$, the open sets are those which are unions of open circular discs.

Another topological space, which we shall encounter frequently, is the extended real line $[-\infty, \infty]$; its topology is defined by declaring the following sets to be open: $(a, b),[-\infty, a),(a, \infty]$, and any union of segments of this type.

The definition of continuity given in Sec. 1.2(c) is a global one. Frequently it is desirable to define continuity locally: A mapping $f$ of $X$ into $Y$ is said to be continuous at the point $x_{0} \in X$ if to every neighborhood $V$ of $f\left(x_{0}\right)$ there corresponds a neighborhood $W$ of $x_{0}$ such that $f(W) \subset V$.

(A neighborhood of a point $x$ is, by definition, an open set which contains $x$.)

When $X$ and $Y$ are metric spaces, this local definition is of course the same as the usual epsilon-delta definition, and is equivalent to the requirement that $\lim f\left(x_{n}\right)=f\left(x_{0}\right)$ in $Y$ whenever $\lim x_{n}=x_{0}$ in $X$.

The following easy proposition relates the local and global definitions of continuity in the expected manner:

1.5 Proposition Let $X$ and $Y$ be topological spaces. A mapping $f$ of $X$ into $Y$ is continuous if and only if $f$ is continuous at every point of $X$.

Proof If $f$ is continuous and $x_{0} \in X$, then $f^{-1}(V)$ is a neighborhood of $x_{0}$, for every neighborhood $V$ of $f\left(x_{0}\right)$. Since $f\left(f^{-1}(V)\right) \subset V$, it follows that $f$ is continuous at $x_{0}$.

If $f$ is continuous at every point of $X$ and if $V$ is open in $Y$, every point $x \in f^{-1}(V)$ has a neighborhood $W_{x}$ such that $f\left(W_{x}\right) \subset V$. Therefore $W_{x} \subset$ $f^{-1}(V)$. It follows that $f^{-1}(V)$ is the union of the open sets $W_{x}$, so $f^{-1}(V)$ is itself open. Thus $f$ is continuous.

1.6 Comments on Definition 1.3 Let $\mathfrak{M}$ be a $\sigma$-algebra in a set $X$. Referring to Properties (i) to (iii) of Definition 1.3(a), we immediately derive the following facts.

(a) Since $\varnothing=X^{c}$, (i) and (ii) imply that $\varnothing \in \mathfrak{M}$.

(b) Taking $A_{n+1}=A_{n+2}=\cdots=\varnothing$ in (iii), we see that $A_{1} \cup A_{2} \cup \cdots \cup A_{n}$ $\in \mathfrak{M}$ if $A_{i} \in \mathfrak{M}$ for $i=1, \ldots, n$.

(c) Since

$$
\bigcap_{n=1}^{\infty} A_{n}=\left(\bigcup_{n=1}^{\infty} A_{n}^{c}\right)^{c}
$$

$\mathfrak{M}$ is closed under the formation of countable (and also finite) intersections.

(d) Since $A-B=B^{c} \cap A$, we have $A-B \in \mathfrak{M}$ if $A \in \mathfrak{M}$ and $B \in \mathfrak{M}$.

The prefix $\sigma$ refers to the fact that (iii) is required to hold for all countable unions of members of $\mathfrak{M}$. If (iii) is required for finite unions only, then $\mathfrak{M}$ is called an algebra of sets.

1.7 Theorem Let $Y$ and $Z$ be topological spaces, and let $g: Y \rightarrow Z$ be continuous.

(a) If $X$ is a topological space, if $f: X \rightarrow Y$ is continuous, and if $h=g \circ f$, then $h: X \rightarrow Z$ is continuous.

(b) If $X$ is a measurable space, if $f: X \rightarrow Y$ is measurable, and if $h=g \circ f$, then $h: X \rightarrow Z$ is measurable.

Stated informally, continuous functions of continuous functions are continuous; continuous functions of measurable functions are measurable.

Proof If $V$ is open in $Z$, then $g^{-1}(V)$ is open in $Y$, and

$$
h^{-1}(V)=f^{-1}\left(g^{-1}(V)\right)
$$

If $f$ is continuous, it follows that $h^{-1}(V)$ is open, proving $(a)$.

If $f$ is measurable, it follows that $h^{-1}(V)$ is measurable, proving $(b)$.

1.8 Theorem Let $u$ and $v$ be real measurable functions on a measurable space $X$, let $\Phi$ be a continuous mapping of the plane into a topological space $Y$, and define

$$
h(x)=\Phi(u(x), v(x))
$$

for $x \in X$. Then $h: X \rightarrow Y$ is measurable.

Proof Put $f(x)=(u(x), v(x))$. Then $f$ maps $X$ into the plane. Since $h=\Phi \circ f$, Theorem 1.7 shows that it is enough to prove the measurability of $f$.

If $R$ is any open rectangle in the plane, with sides parallel to the axes, then $R$ is the cartesian product of two segments $I_{1}$ and $I_{2}$, and

$$
f^{-1}(R)=u^{-1}\left(I_{1}\right) \cap v^{-1}\left(I_{2}\right)
$$

which is measurable, by our assumption on $u$ and $v$. Every open set $V$ in the plane is a countable union of such rectangles $R_{i}$, and since

$$
f^{-1}(V)=f^{-1}\left(\bigcup_{i=1}^{\infty} R_{i}\right)=\bigcup_{i=1}^{\infty} f^{-1}\left(R_{i}\right)
$$

$f^{-1}(V)$ is measurable.

1.9 Let $X$ be a measurable space. The following propositions are corollaries of Theorems 1.7 and 1.8:

(a) If $f=u+i v$, where $u$ and $v$ are real measurable functions on $X$, then $f$ is a complex measurable function on $X$.

This follows from Theorem 1.8, with $\Phi(z)=z$.

(b) If $f=u+i v$ is a complex measurable function on $X$, then $u, v$, and $|f|$ are real measurable functions on $X$.

This follows from Theorem 1.7, with $g(z)=\operatorname{Re}(z), \operatorname{Im}(z)$, and $|z|$.

(c) If $f$ and $g$ are complex measurable functions on $X$, then so are $f+g$ and $f g$.

For real $f$ and $g$ this follaws from Theorem 1.8, with

$$
\Phi(s, t)=s+t
$$

and $\Phi(s, t)=s t$. The complex case then follows from $(a)$ and $(b)$.

(d) If $E$ is a measurable set in $X$ and if

$$
\chi_{E}(x)= \begin{cases}1 & \text { if } x \in E \\ 0 & \text { if } x \notin E\end{cases}
$$

then $\chi_{E}$ is a measurable function.

This is obvious. We call $\chi_{E}$ the characteristic function of the set $E$. The letter $\chi$ will be reserved for characteristic functions throughout this book.

(e) If $f$ is a complex measurable function on $X$, there is a complex measurable function $\alpha$ on $X$ such that $|\alpha|=1$ and $f=\alpha|f|$.

Proof Let $E=\{x: f(x)=0\}$, let $Y$ be the complex plane with the origin removed, define $\varphi(z)=z /|z|$ for $z \in Y$, and put

$$
\alpha(x)=\varphi\left(f(x)+\chi_{E}(x)\right) \quad(x \in X)
$$

If $x \in E, \alpha(x)=1$; if $x \notin E, \alpha(x)=f(x) /|f(x)|$. Since $\varphi$ is continuous on $Y$ and since $E$ is measurable (why?), the measurability of $\alpha$ follows from $(c),(d)$, and Theorem 1.7.

We now show that $\sigma$-algebras exist in great profusion.

1.10 Theorem If $\mathscr{F}$ is any collection of subsets of $X$, there exists a smallest $\sigma$-algebra $\mathfrak{M}^{*}$ in $X$ such that $\mathscr{F} \subset \mathfrak{M}^{*}$.

This $\mathfrak{M}^{*}$ is sometimes called the $\sigma$-algebra generated by $\mathscr{F}$.

ProOF Let $\Omega$ be the family of all $\sigma$-algebras $\mathfrak{M}$ in $X$ which contain $\mathscr{F}$. Since the collection of all subsets of $X$ is such a $\sigma$-algebra, $\Omega$ is not empty. Let $\mathfrak{M}^{*}$ be the intersection of all $\mathfrak{M} \in \Omega$. It is clear that $\mathscr{F} \subset \mathfrak{M}^{*}$ and that $\mathfrak{M}^{*}$ lies in every $\sigma$-algebra in $X$ which contains $\mathscr{F}$. To complete the proof, we have to show that $\mathfrak{M}^{*}$ is itself a $\sigma$-algebra.

If $A_{n} \in \mathfrak{M}^{*}$ for $n=1,2,3, \ldots$, and if $\mathfrak{M} \in \Omega$, then $A_{n} \in \mathfrak{M}$, so $\bigcup A_{n} \in \mathfrak{M}$, since $\mathfrak{M}$ is a $\sigma$-algebra. Since $\bigcup A_{n} \in \mathfrak{M}$ for every $\mathfrak{M} \in \Omega$, we conclude that $\bigcup A_{n} \in \mathfrak{M}^{*}$. The other two defining properties of a $\sigma$-algebra are verified in the same manner.

1.11 Borel Sets Let $X$ be a topological space. By Theorem 1.10, there exists a smallest $\sigma$-algebra $\mathscr{B}$ in $X$ such that every open set in $X$ belongs to $\mathscr{B}$. The members of $\mathscr{B}$ are called the Borel sets of $X$.

In particular, closed sets are Borel sets (being, by definition, the complements of open sets), and so are all countable unions of closed sets and all countable intersections of open sets. These last two are called $F_{\sigma}$ 's and $G_{\delta}$ 's, respectively, and play a considerable role. The notation is due to Hausdorff. The letters $F$ and $G$ were used for closed and open sets, respectively, and $\sigma$ refers to union (Summe), $\delta$ to intersection (Durchschnitt). For example, every half-open interval $[a, b)$ is a $G_{\delta}$ and an $F_{\sigma}$ in $R^{1}$.

Since $\mathscr{B}$ is a $\sigma$-algebra, we may now regard $X$ as a measurable space, with the Borel sets playing the role of the measurable sets; more concisely, we consider the measurable space $(X, \mathscr{B})$. If $f: X \rightarrow Y$ is a continuous mapping of $X$, where $Y$ is any topological space, then it is evident from the definitions that $f^{-1}(V) \in \mathscr{B}$ for every open set $V$ in $Y$. In other words, every continuous mapping of $X$ is Borel measurable.

Borel measurable mappings are often called Borel mappings, or Borel functions.

1.12 Theorem Suppose $\mathfrak{M}$ is a $\sigma$-algebra in $X$, and $Y$ is a topological space. Let $f$ map $X$ into $Y$.

(a) If $\Omega$ is the collection of all sets $E \subset Y$ such that $f^{-1}(E) \in \mathfrak{M}$, then $\Omega$ is a $\sigma$-algebra in $Y$.

(b) If $f$ is measurable and $E$ is a Borel set in $Y$, then $f^{-1}(E) \in \mathfrak{M}$.

(c) If $Y=[-\infty, \infty]$ and $f^{-1}((\alpha, \infty]) \in \mathfrak{M}$ for every real $\alpha$, then $f$ is measurable.

(d) If $f$ is measurable, if $Z$ is a topological space, if $g: Y \rightarrow Z$ is a Borel mapping, and if $h=g \circ f$, then $h: X \rightarrow Z$ is measurable.

Part $(c)$ is a frequently used criterion for the measurability of real-valued functions. (See also Exercise 3.) Note that $(d)$ generalizes Theorem 1.7(b).

Proof (a) follows from the relations

$$
\begin{aligned}
f^{-1}(Y) & =X \\
f^{-1}(Y-A) & =X-f^{-1}(A)
\end{aligned}
$$

and

$$
f^{-1}\left(A_{1} \cup A_{2} \cup \cdots\right)=f^{-1}\left(A_{1}\right) \cup f^{-1}\left(A_{2}\right) \cup \cdots
$$

To prove $(b)$, let $\Omega$ be as in $(a)$; the measurability of $f$ implies that $\Omega$ contains all open sets in $Y$, and since $\Omega$ is a $\sigma$-algebra, $\Omega$ contains all Borel sets in $Y$.

To prove (c), let $\Omega$ be the collection of all $E \subset[-\infty, \infty]$ such that $f^{-1}(E) \in \mathfrak{M}$. Choose a real number $\alpha$, and choose $\alpha_{n}<\alpha$ so that $\alpha_{n} \rightarrow \alpha$ as $n \rightarrow \infty$. Since $\left(\alpha_{n}, \infty\right] \in \Omega$ for each $n$, since

$$
[-\infty, \alpha)=\bigcup_{n=1}^{\infty}\left[-\infty, \alpha_{n}\right]=\bigcup_{n=1}^{\infty}\left(\alpha_{n}, \infty\right]^{c}
$$

and since (a) shows that $\Omega$ is a $\sigma$-algebra, we see that $[-\infty, \alpha) \in \Omega$. The same is then true of

$$
(\alpha, \beta)=[-\infty, \beta) \cap(\alpha, \infty]
$$

Since every open set in $[-\infty, \infty]$ is a countable union of segments of the above types, $\Omega$ contains every open set. Thus $f$ is measurable. since

To prove $(d)$, let $V \subset Z$ be open. Then $g^{-1}(V)$ is a Borel set of $Y$, and

$$
h^{-1}(V)=f^{-1}\left(g^{-1}(V)\right)
$$

(b) shows that $h^{-1}(V) \in \mathfrak{M}$.

1.13 Definition Let $\left\{a_{n}\right\}$ be a sequence in $[-\infty, \infty]$, and put

$$
b_{k}=\sup \left\{a_{k}, a_{k+1}, a_{k+2}, \ldots\right\} \quad(k=1,2,3, \ldots)
$$

and

$$
\beta=\inf \left\{b_{1}, b_{2}, b_{3}, \ldots\right\}
$$

We call $\beta$ the upper limit of $\left\{a_{n}\right\}$, and write

$$
\beta=\limsup _{n \rightarrow \infty} a_{n}
$$

The following properties are easily verified: First, $b_{1} \geq b_{2} \geq b_{3} \geq \cdots$, so that $b_{k} \rightarrow \beta$ as $k \rightarrow \infty$; secondly, there is a subsequence $\left\{a_{n_{i}}\right\}$ of $\left\{a_{n}\right\}$ such that $a_{n_{i}} \rightarrow \beta$ as $i \rightarrow \infty$, and $\beta$ is the largest number with this property.

The lower limit is defined analogously: simply interchange sup and inf in (1) and (2). Note that

$$
\liminf _{n \rightarrow \infty} a_{n}=-\limsup _{n \rightarrow \infty}\left(-a_{n}\right) .
$$

If $\left\{a_{n}\right\}$ converges, then evidently

$$
\limsup _{n \rightarrow \infty} a_{n}=\liminf _{n \rightarrow \infty} a_{n}=\lim _{n \rightarrow \infty} a_{n} .
$$

Suppose $\left\{f_{n}\right\}$ is a sequence of extended-real functions on a set $X$. Then $\sup f_{n}$ and $\lim \sup f_{n}$ are the functions defined on $X$ by

$$
\begin{aligned}
\left(\sup _{n} f_{n}\right)(x) & =\sup _{n}\left(f_{n}(x)\right), \\
\left(\limsup _{n \rightarrow \infty} f_{n}\right)(x) & =\limsup _{n \rightarrow \infty}\left(f_{n}(x)\right)
\end{aligned}
$$

If

$$
f(x)=\lim _{n \rightarrow \infty} f_{n}(x),
$$

the limit being assumed to exist at every $x \in X$, then we call $f$ the pointwise limit of the sequence $\left\{f_{n}\right\}$.

1.14 Theorem If $f_{n}: X \rightarrow[-\infty, \infty]$ is measurable, for $n=1,2,3, \ldots$, and

$$
g=\sup _{n \geq 1} f_{n}, \quad h=\limsup _{n \rightarrow \infty} f_{n},
$$

then $g$ and $h$ are measurable.

ProOF $g^{-1}((\alpha, \infty])=\bigcup_{n=1}^{\infty} f_{n}^{-1}((\alpha, \infty])$. Hence Theorem 1.12(c) implies that $g$ is measurable. The same result holds of course with inf in place of sup, and since

$$
h=\inf _{k \geq 1}\left\{\sup _{i \geq k} f_{i}\right\}
$$

it follows that $h$ is measurable.

## Corollaries

(a) The limit of every pointwise convergent sequence of complex measurable functions is measurable.

(b) If $f$ and $g$ are measurable (with range in $[-\infty, \infty])$, then so are $\max \{f, g\}$ and $\min \{f, g\}$. In particular, this is true of the functions

$$
f^{+}=\max \{f, 0\} \quad \text { and } \quad f^{-}=-\min \{f, 0\} \text {. }
$$

1.15 The above functions $f^{+}$and $f^{-}$are called the positive and negative parts of $f$. We have $|f|=f^{+}+f^{-}$and $f=f^{+}-f^{-}$, a standard representation of $f$ as a difference of two nonnegative functions, with a certain minimality property:

Proposition Iff $=g-h, g \geq 0$, and $h \geq 0$, then $f^{+} \leq g$ and $f^{-} \leq h$.

Proof $f \leq g$ and $0 \leq g$ clearly implies $\max \{f, 0\} \leq g$.

## Simple Functions

1.16 Definition A complex function $s$ on a measurable space $X$ whose range consists of only finitely many points will be called a simple function. Among these are the nonnegative simple functions, whose range is a finite subset of $[0, \infty)$. Note that we explicitly exclude $\infty$ from the values of a simple function.

If $\alpha_{1}, \ldots, \alpha_{n}$ are the distinct values of a simple function $s$, and if we set $A_{i}=\left\{x: s(x)=\alpha_{i}\right\}$, then clearly

$$
s=\sum_{i=1}^{n} \alpha_{i} \chi_{A_{i}}
$$

where $\chi_{A_{i}}$ is the characteristic function of $A_{i}$, as defined in Sec. 1.9(d).

It is also clear that $s$ is measurable if and only if each of the sets $A_{i}$ is measurable.

1.17 Theorem Let $f: X \rightarrow[0, \infty]$ be measurable. There exist simple measurable functions $s_{n}$ on $X$ such that

(a) $0 \leq s_{1} \leq s_{2} \leq \cdots \leq f$

(b) $s_{n}(x) \rightarrow f(x)$ as $n \rightarrow \infty$, for every $x \in X$.

ProOF Put $\delta_{n}=2^{-n}$. To each positive integer $n$ and each real number $t$ corresponds a unique integer $k=k_{n}(t)$ that satisfies $k \delta_{n} \leq t<(k+1) \delta_{n}$. Define

$$
\varphi_{n}(t)= \begin{cases}k_{n}(t) \delta_{n} & \text { if } 0 \leq t<n \\ n & \text { if } n \leq t \leq \infty\end{cases}
$$

Each $\varphi_{n}$ is then a Borel function on $[0, \infty]$,

$$
t-\delta_{n}<\varphi_{n}(t) \leq t \quad \text { if } 0 \leq t \leq n
$$

$0 \leq \varphi_{1} \leq \varphi_{2} \leq \cdots \leq t$, and $\varphi_{n}(t) \rightarrow t$ as $n \rightarrow \infty$, for every $t \in[0, \infty]$. It follows that the functions

$$
s_{n}=\varphi_{n} \circ f
$$

satisfy $(a)$ and $(b)$; they are measurable, by Theorem $1.12(d)$.

## Elementary Properties of Measures

### 1.18 Definition

(a) A positive measure is a function $\mu$, defined on a $\sigma$-algebra $\mathfrak{M}$, whose range is in $[0, \infty]$ and which is countably additive. This means that if $\left\{A_{i}\right\}$ is a disjoint countable collection of members of $\mathfrak{M}$, then

$$
\mu\left(\bigcup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} \mu\left(A_{i}\right)
$$

To avoid trivialities, we shall also assume that $\mu(A)<\infty$ for at least one $A \in \mathfrak{M}$.

(b) A measure space is a measurable space which has a positive measure defined on the $\sigma$-algebra of its measurable sets.

(c) A complex measure is a complex-valued countably additive function defined on a $\sigma$-algebra.

Note: What we have called a positive measure is frequently just called a measure; we add the word "positive" for emphasis. If $\mu(E)=0$ for every $E \in \mathfrak{M}$, then $\mu$ is a positive measure, by our definition. The value $\infty$ is admissible for a positive measure; but when we talk of a complex measure $\mu$, it is understood that $\mu(E)$ is a complex number, for every $E \in \mathfrak{M}$. The real measures form a subclass of the complex ones, of course.

1.19 Theorem Let $\mu$ be a positive measure on a $\sigma$-algebra $\mathfrak{M}$. Then

(a) $\mu(\varnothing)=0$.

(b) $\mu\left(A_{1} \cup \cdots \cup A_{n}\right)=\mu\left(A_{1}\right)+\cdots+\mu\left(A_{n}\right)$ if $A_{1}, \ldots, A_{n}$ are pairwise disjoint members of $\mathfrak{M}$.

(c) $A \subset B$ implies $\mu(A) \leq \mu(B)$ if $A \in \mathfrak{M}, B \in \mathfrak{M}$.

(d) $\mu\left(A_{n}\right) \rightarrow \mu(A)$ as $n \rightarrow \infty$ if $A=\bigcup_{n=1}^{\infty} A_{n}, A_{n} \in \mathfrak{M}$, and

$$
A_{1} \subset A_{2} \subset A_{3} \subset \cdots
$$

(e) $\mu\left(A_{n}\right) \rightarrow \mu(A)$ as $n \rightarrow \infty$ if $A=\bigcap_{n=1}^{\infty} A_{n}, A_{n} \in \mathfrak{M}$,

$$
A_{1} \supset A_{2} \supset A_{3} \supset \cdots
$$

and $\mu\left(A_{1}\right)$ is finite.

As the proof will show, these properties, with the exception of $(c)$, also hold for complex measures; $(b)$ is called finite additivity; $(c)$ is called monotonicity.

## ProOF

(a) Take $A \in \mathfrak{M}$ so that $\mu(A)<\infty$, and take $A_{1}=A$ and $A_{2}=A_{3}=\cdots=$ $\varnothing$ in $1.18(1)$.

(b) Take $A_{n+1}=A_{n+2}=\cdots=\varnothing$ in 1.18(1).

(c) Since $B=A \cup(B-A)$ and $A \cap(B-A)=\varnothing$, we see that (b) implies $\mu(B)=\mu(A)+\mu(B-A) \geq \mu(A)$.

(d) Put $B_{1}=A_{1}$, and put $B_{n}=A_{n}-A_{n-1}$ for $n=2,3,4, \ldots$ Then $B_{n} \in \mathfrak{M}$, $B_{i} \cap B_{j}=\varnothing$ if $i \neq j, A_{n}=B_{1} \cup \cdots \cup B_{n}$, and $A=\bigcup_{i=1}^{\infty} B_{i}$. Hence

$$
\mu\left(A_{n}\right)=\sum_{i=1}^{n} \mu\left(B_{i}\right) \quad \text { and } \quad \mu(A)=\sum_{i=1}^{\infty} \mu\left(B_{i}\right)
$$

Now $(d)$ follows, by the definition of the sum of an infinite series.

(e) Put $C_{n}=A_{1}-A_{n}$. Then $C_{1} \subset C_{2} \subset C_{3} \subset \cdots$,

$$
\mu\left(C_{n}\right)=\mu\left(A_{1}\right)-\mu\left(A_{n}\right)
$$

$A_{1}-A=\bigcup C_{n}$, and so $(d)$ shows that

$$
\mu\left(A_{1}\right)-\mu(A)=\mu\left(A_{1}-A\right)=\lim _{n \rightarrow \infty} \mu\left(C_{n}\right)=\mu\left(A_{1}\right)-\lim _{n \rightarrow \infty} \mu\left(A_{n}\right)
$$

This implies $(e)$.

1.20 Examples The construction of interesting measure spaces requires some labor, as we shall see. However, a few simple-minded examples can be given immediately:

(a) For any $E \subset X$, where $X$ is any set, define $\mu(E)=\infty$ if $E$ is an infinite set, and let $\mu(E)$ be the number of points in $E$ if $E$ is finite. This $\mu$ is called the counting measure on $X$.

(b) Fix $x_{0} \in X$, define $\mu(E)=1$ if $x_{0} \in E$ and $\mu(E)=0$ if $x_{0} \notin E$, for any $E \subset X$. This $\mu$ may be called the unit mass concentrated at $x_{0}$.

(c) Let $\mu$ be the counting measure on the set $\{1,2,3, \ldots\}$, let $A_{n}=\{n, n+1$, $n+2, \ldots\}$. Then $\cap A_{n}=\varnothing$ but $\mu\left(A_{n}\right)=\infty$ for $n=1,2,3, \ldots$ This shows that the hypothesis

$$
\mu\left(A_{1}\right)<\infty
$$

is not superfluous in Theorem 1.19(e).

1.21 A Comment on Terminology One frequently sees measure spaces referred to as "ordered triples" $(X, \mathfrak{M}, \mu)$ where $X$ is a set, $\mathfrak{M}$ is a $\sigma$-algebra in $X$, and $\mu$ is a

![](https://cdn.mathpix.com/cropped/2023_11_05_7e12dc896954aac605c1g-032.jpg?height=46&width=1197&top_left_y=1989&top_left_x=117)

This is logically all right, and often convenient, though somewhat redundant. For instance, in $(X, \mathfrak{M})$ the set $X$ is merely the largest member of $\mathfrak{M}$, so if we know $\mathfrak{M}$ we also know $X$. Similarly, every measure has a $\sigma$-algebra for its domain, by definition, so if we know a measure $\mu$ we also know the $\sigma$-algebra $\mathfrak{M}$ on which $\mu$ is defined and we know the set $X$ in which $\mathfrak{M}$ is a $\sigma$-algebra.

It is therefore perfectly legitimate to use expressions like "Let $\mu$ be a measure" or, if we wish to emphasize the $\sigma$-algebra or the set in question, to say "Let $\mu$ be a measure on $\mathfrak{M}$ " or "Let $\mu$ be a measure on $X$."

What is logically rather meaningless but customary (and we shall often follow mathematical custom rather than logic) is to say "Let $X$ be a measure space"; the emphasis should not be on the set, but on the measure. Of course, when this wording is used, it is tacitly understood that there is a measure defined on some $\sigma$-algebra in $X$ and that it is this measure which is really under discussion.

Similarly, a topological space is an ordered pair $(X, \tau)$, where $\tau$ is a topology in the set $X$, and the significant data are contained in $\tau$, not in $X$, but "the topological space $X$ " is what one talks about.

This sort of tacit convention is used throughout mathematics. Most mathematical systems are sets with some class of distinguished subsets or some binary operations or some relations (which are required to have certain properties), and one can list these and then describe the system as an ordered pair, triple, etc., depending on what is needed. For instance, the real line may be described as a quadruple $\left(R^{1},+, \cdot,<\right)$, where,$+ \cdot$, and $<$ satisfy the axioms of a complete archimedean ordered field. But it is a safe bet that very few mathematicians think of the real field as an ordered quadruple.

## Arithmetic in $[0, \infty]$

1.22 Throughout integration theory, one inevitably encounters $\infty$. One reason is that one wants to be able to integrate over sets of infinite measure; after all, the real line has infinite length. Another reason is that even if one is primarily interested in real-valued functions, the lim sup of a sequence of positive real functions or the sum of a sequence of positive real functions may well be $\infty$ at some points, and much of the elegance of theorems like 1.26 and 1.27 would be lost if one had to make some special provisions whenever this occurs.

Let us define $a+\infty=\infty+a=\infty$ if $0 \leq a \leq \infty$, and

$$
a \cdot \infty=\infty \cdot a= \begin{cases}\infty & \text { if } 0<a \leq \infty \\ 0 & \text { if } a=0\end{cases}
$$

sums and products of real numbers are of course defined in the usual way.

It may seem strange to define $0 \cdot \infty=0$. However, one verifies without difficulty that with this definition the commutative, associative, and distributive laws hold in $[0, \infty]$ without any restriction.

The cancellation laws have to be treated with some care: $a+b=a+c$ implies $b=c$ only when $a<\infty$, and $a b=a c$ implies $b=c$ only when $0<a<\infty$.

Observe that the following useful proposition holds:

If $0 \leq a_{1} \leq a_{2} \leq \cdots, 0 \leq b_{1} \leq b_{2} \leq \cdots, a_{n} \rightarrow a$, and $b_{n} \rightarrow b$, then $a_{n} b_{n} \rightarrow a b$.

If we combine this with Theorems 1.17 and 1.14 , we see that sums and products of measurable functions into $[0, \infty]$ are measurable.

## Integration of Positive Functions

In this section, $\mathfrak{M}$ will be a $\sigma$-algebra in a set $X$ and $\mu$ will be a positive measure on $\mathfrak{M}$.

1.23 Definition If $s: X \rightarrow[0, \infty)$ is a measurable simple function, of the form

$$
s=\sum_{i=1}^{n} \alpha_{i} \chi_{A_{i}}
$$

where $\alpha_{1}, \ldots, \alpha_{n}$ are the distinct values of $s$ (compare Definition 1.16), and if $E \in \mathfrak{M}$, we define

$$
\int_{E} s d \mu=\sum_{i=1}^{n} \alpha_{i} \mu\left(A_{i} \cap E\right)
$$

The convention $0 \cdot \infty=0$ is used here; it may happen that $\alpha_{i}=0$ for some $i$ and that $\mu\left(A_{i} \cap E\right)=\infty$.

If $f: X \rightarrow[0, \infty]$ is measurable, and $E \in \mathfrak{M}$, we define

$$
\int_{E} f d \mu=\sup \int_{E} s d \mu
$$

the supremum being taken over all simple measurable functions $s$ such that $0 \leq s \leq f$.

The left member of (3) is called the Lebesgue integral of $f$ over $E$, with respect to the measure $\mu$. It is a number in $[0, \infty]$.

Observe that we apparently have two definitions for $\int_{E} f d \mu$ if $f$ is simple, namely, (2) and (3). However, these assign the same value to the integral, since $f$ is, in this case, the largest of the functions $s$ which occur on the right of (3).

1.24 The following propositions are immediate consequences of the definitions. The functions and sets occurring in them are assumed to be measurable:

(a) If $0 \leq f \leq g$, then $\int_{E} f d \mu \leq \int_{E} g d \mu$.

(b) If $A \subset B$ and $f \geq 0$, then $\int_{A} f d \mu \leq \int_{B} f d \mu$.
(c) If $f \geq 0$ and $c$ is a constant, $0 \leq c<\infty$, then

$$
\int_{E} c f d \mu=c \int_{E} f d \mu
$$

(d) If $f(x)=0$ for all $x \in E$, then $\int_{E} f d \mu=0$, even if $\mu(E)=\infty$.

(e) If $\mu(E)=0$, then $\int_{E} f d \mu=0$, even if $f(x)=\infty$ for every $x \in E$.

(f) If $f \geq 0$, then $\int_{E} f d \mu=\int_{X} \chi_{E} f d \mu$.

This last result shows that we could have restricted our definition of integration to integrals over all of $X$, without losing any generality. If we wanted to integrate over subsets, we could then use $(f)$ as the definition. It is purely a matter of taste which definition is preferred.

One may also remark here that every measurable subset $E$ of a measure space $X$ is again a measure space, in a perfectly natural way: The new measurable sets are simply those measurable subsets of $X$ which lie in $E$, and the measure is unchanged, except that its domain is restricted. This shows again that as soon as we have integration defined over every measure space, we automatically have it defined over every measurable subset of every measure space.

1.25 Proposition Let $s$ and $t$ be nonnegative measurable simple functions on $X$. For $E \in \mathfrak{M}$, define

$$
\varphi(E)=\int_{E} s d \mu
$$

Then $\varphi$ is a measure on $\mathfrak{M}$. Also

$$
\int_{X}(s+t) d \mu=\int_{X} s d \mu+\int_{X} t d \mu
$$

(This proposition contains provisional forms of Theorems 1.27 and 1.29.)

Proof If $s$ is as in Definition 1.23, and if $E_{1}, E_{2}, \ldots$ are disjoint members of $\mathfrak{M}$ whose union is $E$, the countable additivity of $\mu$ shows that

$$
\begin{aligned}
\varphi(E) & =\sum_{i=1}^{n} \alpha_{i} \mu\left(A_{i} \cap E\right)=\sum_{i=1}^{n} \alpha_{i} \sum_{r=1}^{\infty} \mu\left(A_{i} \cap E_{r}\right) \\
& =\sum_{r=1}^{\infty} \sum_{i=1}^{n} \alpha_{i} \mu\left(A_{i} \cap E_{r}\right)=\sum_{r=1}^{\infty} \varphi\left(E_{r}\right) .
\end{aligned}
$$

Also, $\varphi(\varnothing)=0$, so that $\varphi$ is not identically $\infty$.

Next, let $s$ be as before, let $\beta_{1}, \ldots, \beta_{m}$ be the distinct values of $t$, and let $B_{j}=\left\{x: t(x)=\beta_{j}\right\}$. If $E_{i j}=A_{i} \cap B_{j}$, then

and

$$
\begin{gathered}
\int_{E_{i j}}(s+t) d \mu=\left(\alpha_{i}+\beta_{j}\right) \mu\left(E_{i j}\right) \\
\int_{E_{i j}} s d \mu+\int_{E_{i j}} t d \mu=\alpha_{i} \mu\left(E_{i j}\right)+\beta_{j} \mu\left(E_{i j}\right)
\end{gathered}
$$

Thus (2) holds with $E_{i j}$ in place of $X$. Since $X$ is the disjoint union of the sets $E_{i j}(1 \leq i \leq n, 1 \leq j \leq m)$, the first half of our proposition implies that (2) holds.

We now come to the interesting part of the theory. One of its most remarkable features is the ease with which it handles limit operations.

1.26 Lebesgue's Monotone Convergence Theorem Let $\left\{f_{n}\right\}$ be a sequence of measurable functions on $X$, and suppose that

(a) $0 \leq f_{1}(x) \leq f_{2}(x) \leq \cdots \leq \infty$ for every $x \in X$,

(b) $f_{n}(x) \rightarrow f(x)$ as $n \rightarrow \infty$, for every $x \in X$.

Then $f$ is measurable, and

$$
\int_{X} f_{n} d \mu \rightarrow \int_{X} f d \mu \quad \text { as } n \rightarrow \infty
$$

Proof Since $\int f_{n} \leq \int f_{n+1}$, there exists an $\alpha \in[0, \infty]$ such that

$$
\int_{X} f_{n} d \mu \rightarrow \alpha \quad \text { as } n \rightarrow \infty
$$

By Theorem 1.14, $f$ is measurable. Since $f_{n} \leq f$, we have $\int f_{n} \leq \int f$ for every $n$, so (1) implies

$$
\alpha \leq \int_{x} f d \mu
$$

Let $s$ be any simple measurable function such that $0 \leq s \leq f$, let $c$ be a constant, $0<c<1$, and define

$$
E_{n}=\left\{x: f_{n}(x) \geq c s(x)\right\} \quad(n=1,2,3, \ldots)
$$

Each $E_{n}$ is measurable, $E_{1} \subset E_{2} \subset E_{3} \subset \cdots$, and $X=\bigcup E_{n}$. To see this equality, consider some $x \in X$. If $f(x)=0$, then $x \in E_{1}$; if $f(x)>0$, then $c s(x)<f(x)$, since $c<1$; hence $x \in E_{n}$ for some $n$. Also

$$
\int_{X} f_{n} d \mu \geq \int_{E_{n}} f_{n} d \mu \geq c \int_{E_{n}} s d \mu \quad(n=1,2,3, \ldots)
$$

Let $n \rightarrow \infty$, applying Proposition 1.25 and Theorem $1.19(d)$ to the last integral in (4). The result is

$$
\alpha \geq c \int_{X} s d \mu
$$

Since (5) holds for every $c<1$, we have

$$
\alpha \geq \int_{X} s d \mu
$$

for every simple measurable $s$ satisfying $0 \leq s \leq f$, so that

$$
\alpha \geq \int_{X} f d \mu
$$

The theorem follows from (1), (2), and (7).

1.27 Theorem If $f_{n}: X \rightarrow[0, \infty]$ is measurable, for $n=1,2,3, \ldots$, and

$$
f(x)=\sum_{n=1}^{\infty} f_{n}(x) \quad(x \in X)
$$

then

$$
\int_{X} f d \mu=\sum_{n=1}^{\infty} \int_{X} f_{n} d \mu
$$

ProOF First, there are sequences $\left\{s_{i}^{\prime}\right\},\left\{s_{i}^{\prime \prime}\right\}$ of simple measurable functions such that $s_{i}^{\prime} \rightarrow f_{1}$ and $s_{i}^{\prime \prime} \rightarrow f_{2}$, as in Theorem 1.17. If $s_{i}=s_{i}^{\prime}+s_{i}^{\prime \prime}$, then $s_{i} \rightarrow f_{1}+f_{2}$, and the monotone convergence theorem, combined with Proposition 1.25 , shows that

$$
\int_{X}\left(f_{1}+f_{2}\right) d \mu=\int_{X} f_{1} d \mu+\int_{X} f_{2} d \mu
$$

Next, put $g_{N}=f_{1}+\cdots+f_{N}$. The sequence $\left\{g_{N}\right\}$ converges monotonically to $f$, and if we apply induction to (3) we see that

$$
\int_{X} g_{N} d \mu=\sum_{n=1}^{N} \int_{X} f_{n} d \mu
$$

Applying the monotone convergence theorem once more, we obtain (2), and the proof is complete.

If we let $\mu$ be the counting measure on a countable set, Theorem 1.27 is a statement about double series of nonnegative real numbers (which can of course be proved by more elementary means):

Corollary If $a_{i j} \geq 0$ for $i$ and $j=1,2,3, \ldots$, then

$$
\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} a_{i j}=\sum_{j=1}^{\infty} \sum_{i=1}^{\infty} a_{i j}
$$

1.28 Fatou's Lemma If $f_{n}: X \rightarrow[0, \infty]$ is measurable, for each positive integer $n$, then

$$
\int_{X}\left(\liminf _{n \rightarrow \infty} f_{n}\right) d \mu \leq \liminf _{n \rightarrow \infty} \int_{X} f_{n} d \mu
$$

Strict inequality can occur in (1); see Exercise 8.

Proof Put

$$
g_{k}(x)=\inf _{i \geq k} f_{i}(x) \quad(k=1,2,3, \ldots ; x \in X)
$$

Then $g_{k} \leq f_{k}$, so that

$$
\int_{X} g_{k} d \mu \leq \int_{X} f_{k} d \mu \quad(k=1,2,3, \ldots)
$$

Also, $0 \leq g_{1} \leq g_{2} \leq \cdots$, each $g_{k}$ is measurable, by Theorem 1.14, and $g_{k}(x) \rightarrow \lim \inf f_{n}(x)$ as $k \rightarrow \infty$, by Definition 1.13. The monotone convergence theorem shows therefore that the left side of (3) tends to the left side of (1), as $k \rightarrow \infty$. Hence (1) follows from (3).

1.29 Theorem Suppose $f: X \rightarrow[0, \infty]$ is measurable, and

$$
\varphi(E)=\int_{E} f d \mu \quad(E \in \mathfrak{M})
$$

Then $\varphi$ is a measure on $\mathfrak{M}$, and

$$
\int_{X} g d \varphi=\int_{x} g f d \mu
$$

for every measurable $g$ on $X$ with range in $[0, \infty]$.

Proof Let $E_{1}, E_{2}, E_{3}, \ldots$ be disjoint members of $\mathfrak{M}$ whose union is $E$. Observe that

$$
\chi_{E} f=\sum_{j=1}^{\infty} \chi_{E_{j}} f
$$

and that

$$
\varphi(E)=\int_{X} \chi_{E} f d \mu, \quad \varphi\left(E_{j}\right)=\int_{X} \chi_{E_{j}} f d \mu
$$

It now follows from Theorem 1.27 that

$$
\varphi(E)=\sum_{j=1}^{\infty} \varphi\left(E_{j}\right)
$$

Since $\varphi(\varnothing)=0,(5)$ proves that $\varphi$ is a measure.

Next, (1) shows that (2) holds whenever $g=\chi_{E}$ for some $E \in \mathfrak{M}$. Hence

(2) holds for every simple measurable function $g$, and the general case follows from the monotone convergence theorem.

Remark The second assertion of Theorem 1.29 is sometimes written in the form

$$
d \varphi=f d \mu
$$

We assign no independent meaning to the symbols $d \varphi$ and $d \mu$; (6) merely means that (2) holds for every measurable $g \geq 0$.

Theorem 1.29 has a very important converse, the Radon-Nikodym theorem, which will be proved in Chap. 6 .

## Integration of Complex Functions

As before, $\mu$ will in this section be a positive measure on an arbitrary measurable space $X$.

1.30 Definition We define $L^{1}(\mu)$ to be the collection of all complex measurable functions $f$ on $X$ for which

$$
\int_{X}|f| d \mu<\infty
$$

Note that the measurability of $f$ implies that of $|f|$, as we saw in Proposition $1.9(b)$; hence the above integral is defined.

The members of $L^{1}(\mu)$ are called Lebesgue integrable functions (with respect to $\mu$ ) or summable functions. The significance of the exponent 1 will become clear in Chap. 3.

1.31 Definition If $f=u+i v$, where $u$ and $v$ are real measurable functions on $X$, and if $f \in L^{1}(\mu)$, we define

$$
\int_{E} f d \mu=\int_{E} u^{+} d \mu-\int_{E} u^{-} d \mu+i \int_{E} v^{+} d \mu-i \int_{E} v^{-} d \mu
$$

for every measurable set $E$.

Here $u^{+}$and $u^{-}$are the positive and negative parts of $u$, as defined in Sec. $1.15 ; v^{+}$and $v^{-}$are similarly obtained from $v$. These four functions are measurable, real, and nonnegative; hence the four integrals on the right of (1) exist, by Definition 1.23. Furthermore, we have $u^{+} \leq|u|<|f|$, etc., so that
each of these four integrals is finite. Thus (1) defines the integral on the left as a complex number.

Occasionally it is desirable to define the integral of a measurable function $f$ with range in $[-\infty, \infty]$ to be

$$
\int_{E} f d \mu=\int_{E} f^{+} d \mu-\int_{E} f^{-} d \mu
$$

provided that at least one of the integrals on the right of (2) is finite. The left side of $(2)$ is then a number in $[-\infty, \infty]$.

1.32 Theorem Suppose $f$ and $g \in L^{1}(\mu)$ and $\alpha$ and $\beta$ are complex numbers. Then $\alpha f+\beta g \in L^{1}(\mu)$, and

$$
\int_{X}(\alpha f+\beta g) d \mu=\alpha \int_{X} f d \mu+\beta \int_{X} g d \mu
$$

ProOF The measurability of $\alpha f+\beta g$ follows from Proposition 1.9(c). By Sec. 1.24 and Theorem 1.27,

$$
\begin{aligned}
\int_{X}|\alpha f+\beta g| d \mu & \leq \int_{X}(|\alpha||f|+|\beta||g|) d \mu \\
& =|\alpha| \int_{X}|f| d \mu+|\beta| \int_{X}|g| d \mu<\infty .
\end{aligned}
$$

Thus $\alpha f+\beta g \in L^{1}(\mu)$.

To prove (1), it is clearly sufficient to prove

$$
\int_{X}(f+g) d \mu=\int_{X} f d \mu+\int_{X} g d \mu
$$

and

$$
\int_{X}(\alpha f) d \mu=\alpha \int_{X} f d \mu
$$

and the general case of (2) will follow if we prove (2) for real $f$ and $g$ in $L^{1}(\mu)$.

Assuming this, and setting $h=f+g$, we have

$$
h^{+}-h^{-}=f^{+}-f^{-}+g^{+}-g^{-}
$$

or

$$
h^{+}+f^{-}+g^{-}=f^{+}+g^{+}+h^{-} \text {. }
$$

By Theorem 1.27,

$$
\int h^{+}+\int f^{-}+\int g^{-}=\int f^{+}+\int g^{+}+\int h^{-}
$$

and since each of these integrals is finite, we may transpose and obtain (2).

That (3) holds if $\alpha \geq 0$ follows from Proposition 1.24(c). It is easy to verify that (3) holds if $\alpha=-1$, using relations like $(-u)^{+}=u^{-}$. The case $\alpha=i$ is also easy: If $f=u+i v$, then

$$
\begin{aligned}
\int(i f) & =\int(i u-v)=\int(-v)+i \int u=-\int v+i \int u=i\left(\int u+i \int v\right) \\
& =i \int f
\end{aligned}
$$

Combining these cases with (2), we obtain (3) for any complex $\alpha$.

1.33 Theorem If $f \in L^{1}(\mu)$, then

$$
\left|\int_{X} f d \mu\right| \leq \int_{X}|f| d \mu
$$

Proof Put $z=\int_{X} f d \mu$. Since $z$ is a complex number, there is a complex number $\alpha$, with $|\alpha|=1$, such that $\alpha z=|z|$. Let $u$ be the real part of $\alpha f$. Then $u \leq|\alpha f|=|f|$. Hence

$$
\left|\int_{X} f d \mu\right|=\alpha \int_{X} f d \mu=\int_{X} \alpha f d \mu=\int_{X} u d \mu \leq \int_{X}|f| d \mu .
$$

The third of the above equalities holds since the preceding ones show that $\int \alpha f d \mu$ is real.

We conclude this section with another important convergence theorem.

1.34 Lebesgue's Dominated Convergence Theorem Suppose $\left\{f_{n}\right\}$ is a sequence of complex measurable functions on $X$ such that

$$
f(x)=\lim _{n \rightarrow \infty} f_{n}(x)
$$

exists for every $x \in X$. If there is a function $g \in L^{1}(\mu)$ such that

$$
\left|f_{n}(x)\right| \leq g(x) \quad(n=1,2,3, \ldots ; x \in X)
$$

then $f \in L^{1}(\mu)$,

$$
\lim _{n \rightarrow \infty} \int_{X}\left|f_{n}-f\right| d \mu=0
$$

and

$$
\lim _{n \rightarrow \infty} \int_{X} f_{n} d \mu=\int_{x} f d \mu
$$

Proof Since $|f| \leq g$ and $f$ is measurable, $f \in L^{1}(\mu)$. Since $\left|f_{n}-f\right| \leq 2 g$, Fatou's lemma applies to the functions $2 g-\left|f_{n}-f\right|$ and yields

$$
\begin{aligned}
\int_{X} 2 g d \mu & \leq \liminf _{n \rightarrow \infty} \int_{X}\left(2 g-\left|f_{n}-f\right|\right) d \mu \\
& =\int_{X} 2 g d \mu+\liminf _{n \rightarrow \infty}\left(-\int_{X}\left|f_{n}-f\right| d \mu\right) \\
& =\int_{X} 2 g d \mu-\limsup _{n \rightarrow \infty} \int_{X}\left|f_{n}-f\right| d \mu .
\end{aligned}
$$

Since $\int 2 g d \mu$ is finite, we may subtract it and obtain

$$
\limsup _{n \rightarrow \infty} \int_{X}\left|f_{n}-f\right| d \mu \leq 0
$$

If a sequence of nonnegative real numbers fails to converge to 0 , then its upper limit is positive. Thus (5) implies (3). By Theorem 1.33, applied to $f_{n}-f,(3)$ implies (4).

## The Role Played by Sets of Measure Zero

1.35 Definition Let $P$ be a property which a point $x$ may or may not have. For instance, $P$ might be the property " $f(x)>0$ " if $f$ is a given function, or it might be " $\left\{f_{n}(x)\right\}$ converges" if $\left\{f_{n}\right\}$ is a given sequence of functions.

If $\mu$ is a measure on a $\sigma$-algebra $\mathfrak{M}$ and if $E \in \mathfrak{M}$, the statement " $P$ holds almost everywhere on $E$ " (abbreviated to " $P$ holds a.e. on $E$ ") means that there exists an $N \in \mathfrak{M}$ such that $\mu(N)=0, N \subset E$, and $P$ holds at every point of $E-N$. This concept of a.e. depends of course very strongly on the given measure, and we shall write "a.e. $[\mu]$ " whenever clarity requires that the measure be indicated.

For example, if $f$ and $g$ are measurable functions and if

$$
\mu(\{x: f(x) \neq g(x)\})=0
$$

we say that $f=g$ a.e. $[\mu]$ on $X$, and we may write $f \sim g$. This is easily seen to be an equivalence relation. The transitivity $(f \sim g$ and $g \sim h$ implies $f \sim h)$ is a consequence of the fact that the union of two sets of measure 0 has measure 0 .

Note that if $f \sim g$, then, for every $E \in \mathfrak{M}$,

$$
\int_{E} f d \mu=\int_{E} g d \mu
$$

To see this, let $N$ be the set which appears in (1); then $E$ is the union of the disjoint sets $E-N$ and $E \cap N$; on $E-N, f=g$, and $\mu(E \cap N)=0$.

Thus, generally speaking, sets of measure 0 are negligible in integration. It ought to be true that every subset of a negligible set is negligible. But it may happen that some set $N \in \mathfrak{M}$ with $\mu(N)=0$ has a subset $E$ which is not a member of $\mathfrak{M}$. Of course we can define $\mu(E)=0$ in this case. But will this extension of $\mu$ still be a measure, i.e., will it still be defined on a $\sigma$-algebra? It is a pleasant fact that the answer is affirmative:

1.36 Theorem Let $(X, \mathfrak{M}, \mu)$ be a measure space, let $\mathfrak{M}^{*}$ be the collection of all $E \subset X$ for which there exist sets $A$ and $B \in \mathfrak{M}$ such that $A \subset E \subset B$ and $\mu(B-A)=0$, and define $\mu(E)=\mu(A)$ in this situation. Then $\mathfrak{M}^{*}$ is a $\sigma$-algebra, and $\mu$ is a measure on $\mathfrak{M}^{*}$.

This extended measure $\mu$ is called complete, since all subsets of sets of measure 0 are now measurable; the $\sigma$-algebra $\mathfrak{M}^{*}$ is called the $\mu$-completion of $\mathfrak{M}$. The theorem says that every measure can be completed, so, whenever it is convenient, we may assume that any given measure is complete; this just gives us more measurable sets, hence more measurable functions. Most measures that one meets in the ordinary course of events are already complete, but there are exceptions; one of these will occur in the proof of Fubini's theorem in Chap. 8.

Proof We begin by checking that $\mu$ is well defined for every $E \in \mathfrak{M}^{*}$. Suppose $A \subset E \subset B, A_{1} \subset E \subset B_{1}$, and $\mu(B-A)=\mu\left(B_{1}-A_{1}\right)=0$. (The letters $A$ and $B$ will denote members of $\mathfrak{M}$ throughout this proof.) Since

$$
A-A_{1} \subset E-A_{1} \subset B_{1}-A_{1}
$$

we have $\mu\left(A-A_{1}\right)=0$, hence $\mu(A)=\mu\left(A \cap A_{1}\right)$. For the same reason, $\mu\left(A_{1}\right)=\mu\left(A_{1} \cap A\right)$. We conclude that indeed $\mu\left(A_{1}\right)=\mu(A)$.

Next, let us verify that $\mathfrak{M}^{*}$ has the three defining properties of a $\sigma$ algebra.

(i) $X \in \mathfrak{M}^{*}$, because $X \in \mathfrak{M}$ and $\mathfrak{M} \subset \mathfrak{M}^{*}$.

(ii) If $A \subset E \subset B$ then $B^{c} \subset E^{c} \subset A^{c}$. Thus $E \in \mathfrak{M}^{*}$ implies $E^{c} \in \mathfrak{M}^{*}$, because $A^{c}-B^{c}=A^{c} \cap B=B-A$.

(iii) If $A_{i} \subset E_{i} \subset B_{i}, E=\bigcup E_{i}, A=\bigcup A_{i}, B=\bigcup B_{i}$, then $A \subset E \subset B$ and

$$
B-A=\bigcup_{1}^{\infty}\left(B_{i}-A\right) \subset \bigcup_{1}^{\infty}\left(B_{i}-A_{i}\right)
$$

Since countable unions of sets of measure zero have measure zero, it follows that $E \in \mathfrak{M}^{*}$ if $E_{i} \in \mathfrak{M}^{*}$ for $i=1,2,3, \ldots$

Finally, if the sets $E_{i}$ are disjoint in step (iii), the same is true of the sets $A_{i}$, and we conclude that

$$
\mu(E)=\mu(A)=\sum_{1}^{\infty} \mu\left(A_{i}\right)=\sum_{1}^{\infty} \mu\left(E_{i}\right)
$$

This proves that $\mu$ is countably additive on $\mathfrak{M}^{*}$.

1.37 The fact that functions which are equal a.e. are indistinguishable as far as integration is concerned suggests that our definition of measurable function might profitably be enlarged. Let us call a function $f$ defined on a set $E \in \mathfrak{M}$ measurable on $X$ if $\mu\left(E^{c}\right)=0$ and if $f^{-1}(V) \cap E$ is measurable for every open set $V$. If we define $f(x)=0$ for $x \in E^{c}$, we obtain a measurable function on $X$, in the old sense. If our measure happens to be complete, we can define $f$ on $E^{c}$ in a perfectly arbitrary manner, and we still get a measurable function. The integral of $f$ over any set $A \in \mathfrak{M}$ is independent of the definition of $f$ on $E^{c}$; therefore this definition need not even be specified at all.

There are many situations where this occurs naturally. For instance, a function $f$ on the real line may be differentiable only almost everywhere (with respect to Lebesgue measure), but under certain conditions it is still true that $f$ is the integral of its derivative; this will be discussed in Chap. 7. Or a sequence $\left\{f_{n}\right\}$ of measurable functions on $X$ may converge only almost everywhere; with our new definition of measurability, the limit is still a measurable function on $X$, and we do not have to cut down to the set on which convergence actually occurs.

To illustrate, let us state a corollary of Lebesgue's dominated convergence theorem in a form in which exceptional sets of measure zero are admitted:

1.38 Theorem Suppose $\left\{f_{n}\right\}$ is a sequence of complex measurable functions defined a.e. on $X$ such that

$$
\sum_{n=1}^{\infty} \int_{X}\left|f_{n}\right| d \mu<\infty
$$

Then the series

$$
f(x)=\sum_{n=1}^{\infty} f_{n}(x)
$$

converges for almost all $x, f \in L^{1}(\mu)$, and

$$
\int_{X} f d \mu=\sum_{n=1}^{\infty} \int_{X} f_{n} d \mu
$$

Proof Let $S_{n}$ be the set on which $f_{n}$ is defined, so that $\mu\left(S_{n}^{c}\right)=0$. Put $\varphi(x)=$ $\sum\left|f_{n}(x)\right|$, for $x \in S=\bigcap S_{n}$. Then $\mu\left(S^{c}\right)=0$. By (1) and Theorem 1.27,

$$
\int_{s} \varphi d \mu<\infty
$$

If $E=\{x \in S: \varphi(x)<\infty\}$, it follows from (4) that $\mu\left(E^{c}\right)=0$. The series (2) converges absolutely for every $x \in E$, and if $f(x)$ is defined by (2) for $x \in E$, then $|f(x)| \leq \varphi(x)$ on $E$, so that $f \in L^{1}(\mu)$ on $E$, by (4). If $g_{n}=f_{1}+\cdots+f_{n}$, then $\left|g_{n}\right| \leq \varphi, g_{n}(x) \rightarrow f(x)$ for all $x \in E$, and Theorem 1.34 gives (3) with $E$ in place of $X$. This is equivalent to (3), since $\mu\left(E^{c}\right)=0$.

Note that even if the $f_{n}$ were defined at every point of $X$, (1) would only imply that (2) converges almost everywhere. Here are some other situations in which we can draw conclusions only almost everywhere:

### 1.39 Theorem

(a) Suppose $f: X \rightarrow[0, \infty]$ is measurable, $E \in \mathfrak{M}$, and $\int_{E} f d \mu=0$. Then $f=0$ a.e. on $E$.

(b) Suppose $f \in L^{1}(\mu)$ and $\int_{E} f d \mu=0$ for every $E \in \mathfrak{M}$. Then $f=0$ a.e. on $X$.

(c) Suppose $f \in L^{1}(\mu)$ and

$$
\left|\int_{X} f d \mu\right|=\int_{X}|f| d \mu
$$

Then there is a constant $\alpha$ such that $\alpha f=|f|$ a.e. on $X$.

Note that $(c)$ describes the condition under which equality holds in Theorem 1.33.

## ProOF

(a) If $A_{n}=\{x \in E: f(x)>1 / n\}, n=1,2,3, \ldots$, then

$$
\frac{1}{n} \mu\left(A_{n}\right) \leq \int_{A_{n}} f d \mu \leq \int_{E} f d \mu=0
$$

so that $\mu\left(A_{n}\right)=0$. Since $\{x \in E: f(x)>0\}=\bigcup A_{n},(a)$ follows.

(b) Put $f=u+i v$, let $E=\{x: u(x) \geq 0\}$. The real part of $\int_{E} f d \mu$ is then $\int_{E} u^{+} d \mu$. Hence $\int_{E} u^{+} d \mu=0$, and $(a)$ implies that $u^{+}=0$ a.e. We conclude similarly that

$$
u^{-}=v^{+}=v^{-}=0 \quad \text { a.e. }
$$

(c) Examine the proof of Theorem 1.33. Our present assumption implies that the last inequality in the proof of Theorem 1.33 must actually be an equality. Hence $\int(|f|-u) d \mu=0$. Since $|f|-u \geq 0$, (a) shows that $|f|=u$ a.e. This says that the real part of $\alpha f$ is equal to $|\alpha f|$ a.e., hence $\alpha f=|\alpha f|=|f|$ a.e., which is the desired conclusion.

1.40 Theorem Suppose $\mu(X)<\infty, f \in L^{1}(\mu), S$ is a closed set in the complex plane, and the averages

$$
A_{E}(f)=\frac{1}{\mu(E)} \int_{E} f d \mu
$$

lie in $S$ for every $E \in \mathfrak{M}$ with $\mu(E)>0$. Then $f(x) \in S$ for almost all $x \in X$.

Proof Let $\Delta$ be a closed circular disc (with center at $\alpha$ and radius $r>0$, say) in the complement of $S$. Since $S^{c}$ is the union of countably many such discs, it is enough to prove that $\mu(E)=0$, where $E=f^{-1}(\Delta)$.

If we had $\mu(E)>0$, then

$$
\left|A_{E}(f)-\alpha\right|=\frac{1}{\mu(E)}\left|\int_{E}(f-\alpha) d \mu\right| \leq \frac{1}{\mu(E)} \int_{E}|f-\alpha| d \mu \leq r
$$

which is impossible, since $A_{E}(f) \in S$. Hence $\mu(E)=0$.

1.41 Theorem Let $\left\{E_{k}\right\}$ be a sequence of measurable sets in $X$, such that

$$
\sum_{k=1}^{\infty} \mu\left(E_{k}\right)<\infty
$$

Then almost all $x \in X$ lie in at most finitely many of the sets $E_{k}$.

Proof If $A$ is the set of all $x$ which lie in infinitely many $E_{k}$, we have to prove that $\mu(A)=0$. Put

$$
g(x)=\sum_{k=1}^{\infty} \chi_{E_{k}}(x) \quad(x \in X)
$$

For each $x$, each term in this series is either 0 or 1 . Hence $x \in A$ if and only if $g(x)=\infty$. By Theorem 1.27, the integral of $g$ over $\boldsymbol{X}$ is equal to the sum in (1). Thus $g \in L^{1}(\mu)$, and so $g(x)<\infty$ a.e.

## Exercises

1 Does there exist an infinite $\sigma$-algebra which has only countably many members?

2 Prove an analogue of Theorem 1.8 for $n$ functions.

3 Prove that if $f$ is a real function on a measurable space $X$ such that $\{x: f(x) \geq r\}$ is measurable for every rational $r$, then $f$ is measurable.

4 Let $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$, be sequences in $[-\infty, \infty]$, and prove the following assertions:

(a)

$$
\limsup _{n \rightarrow \infty}\left(-a_{n}\right)=-\liminf _{n \rightarrow \infty} a_{n} .
$$

(b)

$$
\lim _{n \rightarrow \infty} \sup \left(a_{n}+b_{n}\right) \leq \lim _{n \rightarrow \infty} \sup a_{n}+\lim \sup _{n \rightarrow \infty} b_{n}
$$

provided none of the sums is of the form $\infty-\infty$.

(c) If $a_{n} \leq b_{n}$ for all $n$, then

$$
\lim _{n \rightarrow \infty} \inf a_{n} \leq \lim _{n \rightarrow \infty} \inf b_{n} .
$$

Show by an example that strict inequality can hold in $(b)$.
(a) Suppose $f: X \rightarrow[-\infty, \infty]$ and $g: X \rightarrow[-\infty, \infty]$ are measurable. Prove that the sets

$$
\{x: f(x)<g(x)\},\{x: f(x)=g(x)\}
$$

are measurable.

(b) Prove that the set of points at which a sequence of measurable real-valued functions converges (to a finite limit) is measurable.

6 Let $X$ be an uncountable set, let $\mathfrak{M}$ be the collection of all sets $E \subset X$ such that either $E$ or $E^{c}$ is at most countable, and define $\mu(E)=0$ in the first case, $\mu(E)=1$ in the second. Prove that $\mathfrak{M}$ is a $\sigma$-algebra in $X$ and that $\mu$ is a measure on $\mathfrak{M}$. Describe the corresponding measurable functions and their integrals.

7 Suppose $f_{n}: X \rightarrow[0, \infty]$ is measurable for $n=1,2,3, \ldots, f_{1} \geq f_{2} \geq f_{3} \geq \cdots \geq 0, f_{n}(x) \rightarrow f(x)$ as $n \rightarrow \infty$, for every $x \in X$, and $f_{1} \in L^{1}(\mu)$. Prove that then

$$
\lim _{n \rightarrow \infty} \int_{X} f_{n} d \mu=\int_{X} f d \mu
$$

and show that this conclusion does not follow if the condition " $f_{1} \in L^{1}(\mu)$ " is omitted.

8 Put $f_{n}=\chi_{E}$ if $n$ is odd, $f_{n}=1-\chi_{E}$ if $n$ is even. What is the relevance of this example to Fatou's lemma?

9 Suppose $\mu$ is a positive measure on $X, f: X \rightarrow[0, \infty]$ is measurable, $\int_{X} f d \mu=c$, where $0<c<\infty$, and $\alpha$ is a constant. Prove that

$$
\lim _{n \rightarrow \infty} \int_{X} n \log \left[1+(f / n)^{\alpha}\right] d \mu= \begin{cases}\infty & \text { if } 0<\alpha<1 \\ c & \text { if } \alpha=1, \\ 0 & \text { if } 1<\alpha<\infty\end{cases}
$$

Hint: If $\alpha \geq 1$, the integrands are dominated by $\alpha f$. If $\alpha<1$, Fatou's lemma can be applied. 10 Suppose $\mu(X)<\infty,\left\{f_{n}\right\}$ is a sequence of bounded complex measurable functions on $X$, and $f_{n} \rightarrow f$ uniformly on $X$. Prove that

$$
\lim _{n=\infty} \int_{X} f_{n} d \mu=\int_{X} f d \mu
$$

and show that the hypothesis " $\mu(X)<\infty$ " cannot be omitted.

11 Show that

$$
A=\bigcap_{n=1}^{\infty} \bigcup_{k=n}^{\infty} E_{k}
$$

in Theorem 1.41, and hence prove the theorem without any reference to integration.

12 Suppose $f \in L^{1}(\mu)$. Prove that to each $\epsilon>0$ there exists a $\delta>0$ such that $\int_{E}|f| d \mu<\epsilon$ whenever $\mu(E)<\delta$.

13 Show that proposition $1.24(c)$ is also true when $c=\infty$.

## POSITIVE BOREL MEASURES

## Vector Spaces

2.1 Definition A complex vector space (or a vector space over the complex field) is a set $V$, whose elements are called vectors and in which two operations, called addition and scalar multiplication, are defined, with the following familiar algebraic properties:

To every pair of vectors $x$ and $y$ there corresponds a vector $x+y$, in such a way that $x+y=y+x$ and $x+(y+z)=(x+y)+z ; V$ contains a unique vector 0 (the zero vector or origin of $V$ ) such that $x+0=x$ for every $x \in V$; and to each $x \in V$ there corresponds a unique vector $-x$ such that $x+(-x)=0$.

To each pair $(\alpha, x)$, where $x \in V$ and $\alpha$ is a scalar (in this context, the word scalar means complex number), there is associated a vector $\alpha x \in V$, in such a way that $1 x=x, \alpha(\beta x)=(\alpha \beta) x$, and such that the two distributive laws

$$
\alpha(x+y)=\alpha x+\alpha y,(\alpha+\beta) x=\alpha x+\beta x
$$

hold.

A linear transformation of a vector space $V$ into a vector space $V_{1}$ is a mapping $\Lambda$ of $V$ into $V_{1}$ such that

$$
\Lambda(\alpha x+\beta y)=\alpha \Lambda x+\beta \Lambda y
$$

for all $x$ and $y \in V$ and for all scalars $\alpha$ and $\beta$. In the special case in which $V_{1}$ is the field of scalars (this is the simplest example of a vector space, except for the trivial one consisting of 0 alone), $\Lambda$ is called a linear functional. A linear functional is thus a complex function on $V$ which satisfies (2).

Note that one often writes $\Lambda x$, rather than $\Lambda(x)$, if $\Lambda$ is linear.

The preceding definitions can of course be made equally well with any field whatsoever in place of the complex field. Unless the contrary is explicitly stated, however, all vector spaces occurring in this book will be complex, with one notable exception: the euclidean spaces $R^{k}$ are vector spaces over the real field.

2.2 Integration as a Linear Functional Analysis is full of vector spaces and linear transformations, and there is an especially close relationship between integration on the one hand and linear functionals on the other.

For instance, Theorem 1.32 shows that $L^{1}(\mu)$ is a vector space, for any positive measure $\mu$, and that the mapping

$$
f \rightarrow \int_{x} f d \mu
$$

is a linear functional on $L^{1}(\mu)$. Similarly, if $g$ is any bounded measurable function, the mapping

$$
f \rightarrow \int_{X} f g d \mu
$$

is a linear functional on $L^{1}(\mu)$; we shall see in Chap. 6 that the functionals (2) are, in a sense, the only interesting ones on $L^{1}(\mu)$.

For another example, let $C$ be the set of all continuous complex functions on the unit interval $I=[0,1]$. The sum of the two continuous functions is continuous, and so is any scalar multiple of a continuous function. Hence $C$ is a vector space, and if

$$
\Lambda f=\int_{0}^{1} f(x) d x \quad(f \in C)
$$

the integral being the ordinary Riemann integral, then $\Lambda$ is clearly a linear functional on $C ; \Lambda$ has an additional interesting property: it is a positive linear functional. This means that $\Lambda f \geq 0$ whenever $f \geq 0$.

One of the tasks which is still ahead of us is the construction of the Lebesgue measure. The construction can be based on the linear functional (3), by the following observation: Consider a segment $(a, b) \subset I$ and consider the class of all $f \in C$ such that $0 \leq f \leq 1$ on $I$ and $f(x)=0$ for all $x$ not in $(a, b)$. We have $\Lambda f<b-a$ for all such $f$, but we can choose $f$ so that $\Lambda f$ is as close to $b-a$ as desired. Thus the length (or measure) of $(a, b)$ is intimately related to the values of the functional $\Lambda$.

The preceding observation, when looked at from a more general point of view, leads to a remarkable and extremely important theorem of $F$. Riesz:

To every positive linear functional $\Lambda$ on $C$ corresponds a finite positive Borel measure $\mu$ on I such that

$$
\Lambda f=\int_{I} f d \mu \quad(f \in C)
$$

[The converse is obvious: if $\mu$ is a finite positive Borel measure on $I$ and if $\Lambda$ is defined by (4), then $\Lambda$ is a positive linear functional on $C$.]

It is clearly of interest to replace the bounded interval $I$ by $R^{1}$. We can do this by restricting attention to those continuous functions on $R^{1}$ which vanish outside some bounded interval. (These functions are Riemann integrable, for instance.) Next, functions of several variables occur frequently in analysis. Thus we ought to move from $R^{1}$ to $R^{n}$. It turns out that the proof of the Riesz theorem still goes through, with hardly any changes. Moreover, it turns out that the euclidean properties of $R^{n}$ (coordinates, orthogonality, etc.) play no role in the proof; in fact, if one thinks of them too much they just get in the way. Essential to the proof are certain topological properties of $R^{n}$. (Naturally. We are now dealing with continuous functions.) The crucial property is that of local compactness: Each point of $R^{n}$ has a neighborhood whose closure is compact.

We shall therefore establish the Riesz theorem in a very general setting (Theorem 2.14). The existence of Lebesgue measure follows then as a special case. Those who wish to concentrate on a more concrete situation may skip lightly over the following section on topological preliminaries (Urysohn's lemma is the item of greatest interest there; see Exercise 3) and may replace locally compact Hausdorff spaces by locally compact metric spaces, or even by euclidean spaces, without missing any of the principal ideas.

It should also be mentioned that there are situations, especially in probability theory, where measures occur naturally on spaces without topology, or on topological spaces that are not locally compact. An example is the so-called Wiener measure which assigns numbers to certain sets of continuous functions and which is a basic tool in the study of Brownian motion. These topics will not be discussed in this book.

## Topological Preliminaries

2.3 Definitions Let $X$ be a topological space, as defined in Sec. 1.2.

(a) A set $E \subset X$ is closed if its complement $E^{c}$ is open. (Hence $\varnothing$ and $X$ are closed, finite unions of closed sets are closed, and arbitrary intersections of closed sets are closed.)

(b) The closure $\bar{E}$ of a set $E \subset X$ is the smallest closed set in $X$ which contains $E$. (The following argument proves the existence of $\bar{E}$ : The collection $\Omega$ of all closed subsets of $X$ which contain $E$ is not empty, since $X \in \Omega$; let $\bar{E}$ be the intersection of all members of $\Omega$.)

(c) A set $K \subset X$ is compact if every open cover of $K$ contains a finite subcover. More explicitly, the requirement is that if $\left\{V_{\alpha}\right\}$ is a collection of open sets whose union contains $K$, then the union of some finite subcollection of $\left\{V_{\alpha}\right\}$ also contains $K$.

In particular, if $X$ is itself compact, then $X$ is called a compact space.

(d) A neighborhood of a point $p \in X$ is any open subset of $X$ which contains $p$. (The use of this term is not quite standardized; some use
"neighborhood of $p$ " for any set which contains an open set containing p.)

(e) $X$ is a Hausdorff space if the following is true: If $p \in X, q \in X$, and $p \neq q$, then $p$ has a neighborhood $U$ and $q$ has a neighborhood $V$ such that $U \cap V=\varnothing$.

( $f$ ) $X$ is locally compact if every point of $X$ has a neighborhood whose closure is compact.

Obviously, every compact space is locally compact.

We recall the Heine-Borel theorem: The compact subsets of a euclidean space $R^{n}$ are precisely those that are closed and bounded ([26], $\dagger$ Theorem 2.41). From this it follows easily that $R^{n}$ is a locally compact Hausdorff space. Also, every metric space is a Hausdorff space.

2.4 Theorem Suppose $K$ is compact and $F$ is closed, in a topological space $X$. If $F \subset K$, then $F$ is compact.

Proof If $\left\{V_{\alpha}\right\}$ is an open cover of $F$ and $W=F^{c}$, then $W \cup \bigcup_{\alpha} V_{\alpha}$ covers $X$; hence there is a finite collection $\left\{V_{\alpha_{i}}\right\}$ such that

$$
K \subset W \cup V_{\alpha_{1}} \cup \cdots \cup V_{\alpha_{n}}
$$

Then $F \subset V_{\alpha_{1}} \cup \cdots \cup V_{\alpha_{n}}$.

Corollary If $A \subset B$ and if $B$ has compact closure, so does $A$.

2.5 Theorem Suppose $X$ is a Hausdorff space, $K \subset X, K$ is compact, and $p \in K^{c}$. Then there are open sets $U$ and $W$ such that $p \in U, K \subset W$, and $U \cap W=\varnothing$.

Proof If $q \in K$, the Hausdorff separation axiom implies the existence of disjoint open sets $U_{q}$ and $V_{q}$, such that $p \in U_{q}$ and $q \in V_{q}$. Since $K$ is compact, there are points $q_{1}, \ldots, q_{n} \in K$ such that

$$
K \subset V_{q_{1}} \cup \cdots \cup V_{q_{n}}
$$

Our requirements are then satisfied by the sets

$$
U=U_{q_{1}} \cap \cdots \cap U_{q_{n}} \text { and } \quad W=V_{q_{1}} \cup \cdots \cup V_{q_{n}} \text {. }
$$

## Corollaries

(a) Compact subsets of Hausdorff spaces are closed.

(b) If $F$ is closed and $K$ is compact in a Hausdorff space, then $F \cap K$ is compact.

Corollary $(b)$ follows from $(a)$ and Theorem 2.4.

2.6 Theorem If $\left\{K_{\alpha}\right\}$ is a collection of compact subsets of a Hausdorff space and if $\bigcap_{\alpha} K_{\alpha}=\varnothing$, then some finite subcollection of $\left\{K_{\alpha}\right\}$ also has empty intersection.

ProOF Put $V_{\alpha}=K_{\alpha}^{c}$. Fix a member $K_{1}$ of $\left\{K_{\alpha}\right\}$. Since no point of $K_{1}$ belongs to every $K_{\alpha},\left\{V_{\alpha}\right\}$ is an open cover of $K_{1}$. Hence $K_{1} \subset V_{\alpha_{1}} \cup \cdots \cup V_{\alpha_{n}}$ for some finite collection $\left\{V_{\alpha_{i}}\right\}$. This implies that

$$
K_{1} \cap K_{\alpha_{1}} \cap \cdots \cap K_{\alpha_{n}}=\varnothing
$$

2.7 Theorem Suppose $U$ is open in a locally compact Hausdorff space $X$, $K \subset U$, and $K$ is compact. Then there is an open set $V$ with compact closure such that

$$
K \subset V \subset \bar{V} \subset U .
$$

Proof Since every point of $K$ has a neighborhood with compact closure, and since $K$ is covered by the union of finitely many of these neighborhoods, $K$ lies in an open set $G$ with compact closure. If $U=X$, take $V=G$.

Otherwise, let $C$ be the complement of $U$. Theorem 2.5 shows that to each $p \in C$ there corresponds an open set $W_{p}$ such that $K \subset W_{p}$ and $p \notin \bar{W}_{p}$. Hence $\left\{C \cap \bar{G} \cap W_{p}\right\}$, where $p$ ranges over $C$, is a collection of compact sets with empty intersection. By Theorem 2.6 there are points $p_{1}, \ldots, p_{n} \in C$ such that

$$
C \cap \bar{G} \cap \bar{W}_{p_{1}} \cap \cdots \cap \bar{W}_{p_{n}}=\varnothing
$$

The set

$$
V=G \cap W_{p_{1}} \cap \cdots \cap W_{p_{n}}
$$

then has the required properties, since

$$
\bar{V} \subset \bar{G} \cap \bar{W}_{p_{1}} \cap \cdots \cap \bar{W}_{p_{n}} .
$$

2.8 Definition Let $f$ be a real (or extended-real) function on a topological space. If

$$
\{x: f(x)>\alpha\}
$$

is open for every real $\alpha, f$ is said to be lower semicontinuous. If

$$
\{x: f(x)<\alpha\}
$$

is open for every real $\alpha, f$ is said to be upper semicontinuous.

A real function is obviously continuous if and only if it is both upper and lower semicontinuous.

The simplest examples of semicontinuity are furnished by characteristic functions:
(a) Characteristic functions of open sets are lower semicontinuous.

(b) Characteristic functions of closed sets are upper semicontinuous.

The following property is an almost immediate consequence of the definitions:

(c) The supremum of any collection of lower semicontinuous functions is lower semicontinuous. The infimum of any collection of upper semicontinuous functions is upper semicontinuous.

2.9 Definition The support of a complex function $f$ on a topological space $X$ is the closure of the set

$$
\{x: f(x) \neq 0\} .
$$

The collection of all continuous complex functions on $X$ whose support is compact is denoted by $C_{c}(X)$.

Observe that $C_{c}(X)$ is a vector space. This is due to two facts:

(a) The support of $f+g$ lies in the union of the support of $f$ and the support of $g$, and any finite union of compact sets is compact.

(b) The sum of two continuous complex functions is continuous, as are scalar multiples of continuous functions.

(Statement and proof of Theorem 1.8 hold verbatim if "measurable function" is replaced by "continuous function," "measurable space" by "topological space"; take $\Phi(s, t)=s+t$, or $\Phi(s, t)=s t$, to prove that sums and products of continuous functions are continuous.)

2.10 Theorem Let $X$ and $Y$ be topological spaces, and let $f: X \rightarrow Y$ be continuous. If $K$ is a compact subset of $X$, then $f(K)$ is compact.

Proof If $\left\{V_{\alpha}\right\}$ is an open cover of $f(K)$, then $\left\{f^{-1}\left(V_{\alpha}\right)\right\}$ is an open cover of $K$, hence $K \subset f^{-1}\left(V_{\alpha_{1}}\right) \cup \cdots \cup f^{-1}\left(V_{\alpha_{n}}\right)$ for some $\alpha_{1}, \ldots, \alpha_{n}$, and therefore $f(K) \subset V_{\alpha_{1}} \cup \cdots \cup V_{\alpha_{n}}$.

Corollary The range of any $f \in C_{c}(X)$ is a compact subset of the complex plane.

In fact, if $K$ is the support of $f \in C_{c}(X)$, then $f(X) \subset f(K) \cup\{0\}$. If $X$ is not compact, then $0 \in f(X)$, but 0 need not lie in $f(K)$, as is seen by easy examples.

2.11 Notation In this chapter the following conventions will be used. The notation

$$
K \prec f
$$

will mean that $K$ is a compact subset of $X$, that $f \in C_{c}(X)$, that $0 \leq f(x) \leq 1$ for all $x \in X$, and that $f(x)=1$ for all $x \in K$. The notation

$$
f \prec V
$$

will mean that $V$ is open, that $f \in C_{c}(X), 0 \leq f \leq 1$, and that the support of $f$ lies in $V$. The notation

$$
K \prec f \prec V
$$

will be used to indicate that both (1) and (2) hold.

2.12 Urysohn's Lemma Suppose $X$ is a locally compact Hausdorff space, $V$ is open in $X, K \subset V$, and $K$ is compact. Then there exists an $f \in C_{c}(X)$, such that

$$
K \prec f \prec V \text {. }
$$

In terms of characteristic functions, the conclusion asserts the existence of a continuous function $f$ which satisfies the inequalities $\chi_{K} \leq f \leq \chi_{V}$. Note that it is easy to find semicontinuous functions which do this; examples are $\chi_{K}$ and $\chi_{V}$.

Proof Put $r_{1}=0, r_{2}=1$, and let $r_{3}, r_{4}, r_{5}, \ldots$ be an enumeration of the rationals in $(0,1)$. By Theorem 2.7, we can find open sets $V_{0}$ and then $V_{1}$ such that $\bar{V}_{0}$ is compact and

$$
K \subset V_{1} \subset \bar{V}_{1} \subset V_{0} \subset \bar{V}_{0} \subset V
$$

Suppose $n \geq 2$ and $V_{r_{1}}, \ldots, V_{r_{n}}$ have been chosen in such a manner that $r_{i}<r_{j}$ implies $\bar{V}_{r_{j}} \subset V_{r_{i}}$. Then one of the numbers $r_{1}, \ldots, r_{n}$, say $r_{i}$, will be the largest one which is smaller than $r_{n+1}$, and another, say $r_{j}$, will be the smallest one larger than $r_{n+1}$. Using Theorem 2.7 again, we can find $V_{r_{n+1}}$ so that

$$
\bar{V}_{r_{j}} \subset V_{r_{n+1}} \subset \bar{V}_{r_{n+1}} \subset V_{r_{i}} .
$$

Continuing, we obtain a collection $\left\{V_{r}\right\}$ of open sets, one for every rational $r \in[0,1]$, with the following properties: $K \subset V_{1}, \bar{V}_{0} \subset V$, each $\bar{V}_{r}$ is compact, and

$$
s>r \text { implies } \bar{V}_{s} \subset V_{r} .
$$

Define

$$
f_{r}(x)=\left\{\begin{array}{ll}
r & \text { if } x \in V_{r}, \\
0 & \text { otherwise, }
\end{array} \quad g_{s}(x)= \begin{cases}1 & \text { if } x \in \bar{V}_{s} \\
s & \text { otherwise }\end{cases}\right.
$$

and

$$
f=\sup _{r} f_{r}, \quad g=\inf _{s} g_{s} .
$$

The remarks following Definition 2.8 show that $f$ is lower semicontinuous and that $g$ is upper semicontinuous. It is clear that $0 \leq f \leq 1$, that
$f(x)=1$ if $x \in K$, and that $f$ has its support in $\bar{V}_{0}$. The proof will be completed by showing that $f=g$.

The inequality $f_{r}(x)>g_{s}(x)$ is possible only if $r>s, x \in V_{r}$, and $x \notin \bar{V}_{s}$. But $r>s$ implies $V_{r} \subset V_{s}$. Hence $f_{r} \leq g_{s}$ for all $r$ and $s$, so $f \leq g$.

Suppose $f(x)<g(x)$ for some $x$. Then there are rationals $r$ and $s$ such that $f(x)<r<s<g(x)$. Since $f(x)<r$, we have $x \notin V_{r}$; since $g(x)>s$, we have $x \in \bar{V}_{s}$. By (3), this is a contradiction. Hence $f=g$.

2.13 Theorem Suppose $V_{1}, \ldots, V_{n}$ are open subsets of a locally compact Hausdorff space $X, K$ is compact, and

$$
K \subset V_{1} \cup \cdots \cup V_{n}
$$

Then there exist functions $h_{i} \prec V_{i}(i=1, \ldots, n)$ such that

$$
h_{1}(x)+\cdots+h_{n}(x)=1 \quad(x \in K) .
$$

Because of (1), the collection $\left\{h_{1}, \ldots, h_{n}\right\}$ is called a partition of unity on $K$, subordinate to the cover $\left\{V_{1}, \ldots, V_{n}\right\}$.

Proof By Theorem 2.7, each $x \in K$ has a neighborhood $W_{x}$ with compact closure $\bar{W}_{x} \subset V_{i}$ for some $i$ (depending on $x$ ). There are points $x_{1}, \ldots, x_{m}$ such that $W_{x_{1}} \cup \cdots \cup W_{x_{m}} \supset K$. If $1 \leq i \leq n$, let $H_{i}$ be the union of those $W_{x_{j}}$ which lie in $V_{i}$. By Urysohn's lemma, there are functions $g_{i}$ such that $H_{i} \prec g_{i} \prec V_{i}$. Define

$$
\begin{aligned}
& h_{1}=g_{1} \\
& h_{2}=\left(1-g_{1}\right) g_{2} \\
& \ldots \ldots \ldots \\
& h_{n}=\left(1-g_{1}\right)\left(1-g_{2}\right) \cdots\left(1-g_{n-1}\right) g_{n} .
\end{aligned}
$$

Then $h_{i} \prec V_{i}$. It is easily verified, by induction, that

$$
h_{1}+h_{2}+\cdots+h_{n}=1-\left(1-g_{1}\right)\left(1-g_{2}\right) \cdots\left(1-g_{n}\right) .
$$

Since $K \subset H_{1} \cup \cdots \cup H_{n}$, at least one $g_{i}(x)=1$ at each point $x \in K$; hence (3) shows that (1) holds.

## The Riesz Representation Theorem

2.14 Theorem Let $X$ be a locally compact Hausdorff space, and let $\Lambda$ be a positive linear functional on $C_{c}(X)$. Then there exists a $\sigma$-algebra $\mathfrak{M}$ in $X$ which contains all Borel sets in $X$, and there exists a unique positive measure $\mu$ on $\mathfrak{M}$ which represents $\Lambda$ in the sense that

(a) $\Lambda f=\int_{X} f d \mu$ for every $f \in C_{c}(X)$,

and which has the following additional properties:
(b) $\mu(K)<\infty$ for every compact set $K \subset X$.

(c) For every $E \in \mathfrak{M}$, we have

$$
\mu(E)=\inf \{\mu(V): E \subset V, V \text { open }\} .
$$

(d) The relation

$$
\mu(E)=\sup \{\mu(K): K \subset E, K \text { compact }\}
$$

holds for every open set $E$, and for every $E \in \mathfrak{M}$ with $\mu(E)<\infty$.

(e) If $E \in \mathfrak{M}, A \subset E$, and $\mu(E)=0$, then $A \in \mathfrak{M}$.

For the sake of clarity, let us be more explicit about the meaning of the word "positive" in the hypothesis: $\Lambda$ is assumed to be a linear functional on the complex vector space $C_{c}(X)$, with the additional property that $\Lambda f$ is a nonnegative real number for every $f$ whose range consists of nonnegative real numbers. Briefly, if $f(X) \subset[0, \infty)$ then $\Lambda f \in[0, \infty)$.

Property $(a)$ is of course the one of greatest interest. After we define $\mathfrak{M}$ and $\mu$, (b) to $(d)$ will be established in the course of proving that $\mathfrak{M}$ is a $\sigma$-algebra and that $\mu$ is countably additive. We shall see later (Theorem 2.18) that in "reasonable" spaces $X$ every Borel measure which satisfies $(b)$ also satisfies $(c)$ and $(d)$ and that $(d)$ actually holds for every $E \in \mathfrak{M}$, in those cases. Property $(e)$ merely says that $(X, \mathfrak{M}, \mu)$ is a complete measure space, in the sense of Theorem 1.36.

Throughout the proof of this theorem, the letter $K$ will stand for a compact subset of $X$, and $V$ will denote an open set in $X$.

Let us begin by proving the uniqueness of $\mu$. If $\mu$ satisfies $(c)$ and $(d)$, it is clear that $\mu$ is determined on $\mathfrak{M}$ by its values on compact sets. Hence it suffices to prove that $\mu_{1}(K)=\mu_{2}(K)$ for all $K$, whenever $\mu_{1}$ and $\mu_{2}$ are measures for which the theorem holds. So, fix $K$ and $\epsilon>0$. By $(b)$ and (c), there exists a $V \supset K$ with $\mu_{2}(V)<\mu_{2}(K)+\epsilon$; by Urysohn's lemma, there exists an $f$ so that $K \prec f \prec V$; hence

$$
\begin{aligned}
\mu_{1}(K) & =\int_{X} \chi_{K} d \mu_{1} \leq \int_{X} f d \mu_{1}=\Lambda f=\int_{X} f d \mu_{2} \\
& \leq \int_{X} \chi_{V} d \mu_{2}=\mu_{2}(V)<\mu_{2}(K)+\epsilon
\end{aligned}
$$

Thus $\mu_{1}(K) \leq \mu_{2}(K)$. If we interchange the roles of $\mu_{1}$ and $\mu_{2}$, the opposite inequality is obtained, and the uniqueness of $\mu$ is proved.

Incidentally, the above computation shows that $(a)$ forces $(b)$.

Construction of $\mu$ and $\mathfrak{M}$

For every open set $V$ in $X$, define

$$
\mu(V)=\sup \{\Lambda f: f \prec V\} .
$$

If $V_{1} \subset V_{2}$, it is clear that (1) implies $\mu\left(V_{1}\right) \leq \mu\left(V_{2}\right)$. Hence

$$
\mu(E)=\inf \{\mu(V): E \subset V, V \text { open }\}
$$

if $E$ is an open set, and it is consistent with (1) to define $\mu(E)$ by (2), for every $E \subset X$.

Note that although we have defined $\mu(E)$ for every $E \subset X$, the countable additivity of $\mu$ will be proved only on a certain $\sigma$-algebra $\mathfrak{M}$ in $X$.

Let $\mathfrak{M}_{F}$ be the class of all $E \subset X$ which satisfy two conditions: $\mu(E)<\infty$, and

$$
\mu(E)=\sup \{\mu(K): K \subset E, K \text { compact }\}
$$

Finally, let $\mathfrak{M}$ be the class of all $E \subset X$ such that $E \cap K \in \mathfrak{M}_{F}$ for every compact $K$.

Proof that $\mu$ and $\mathfrak{M}$ have the required properties

It is evident that $\mu$ is monotone, i.e., that $\mu(A) \leq \mu(B)$ if $A \subset B$ and that $\mu(E)=0$ implies $E \in \mathfrak{M}_{F}$ and $E \in \mathfrak{M}$. Thus $(e)$ holds, and so does $(c)$, by definition.

Since the proof of the other assertions is rather long, it will be convenient to divide it into several steps.

Observe that the positivity of $\Lambda$ implies that $\Lambda$ is monotone: $f \leq g$ implies $\Lambda f \leq \Lambda g$. This is clear, since $\Lambda g=\Lambda f+\Lambda(g-f)$ and $g-f \geq 0$. This monotonicity will be used in Steps II and X.

STEP I If $E_{1}, E_{2}, E_{3}, \ldots$ are arbitrary subsets of $X$, then

$$
\mu\left(\bigcup_{i=1}^{\infty} E_{i}\right) \leq \sum_{i=1}^{\infty} \mu\left(E_{i}\right)
$$

Proof We first show that

$$
\mu\left(V_{1} \cup V_{2}\right) \leq \mu\left(V_{1}\right)+\mu\left(V_{2}\right)
$$

if $V_{1}$ and $V_{2}$ are open. Choose $g \prec V_{1} \cup V_{2}$. By Theorem 2.13 there are functions $h_{1}$ and $h_{2}$ such that $h_{i} \prec V_{i}$ and $h_{1}(x)+h_{2}(x)=1$ for all $x$ in the support of $g$. Hence $h_{i} g \prec V_{i}, g=h_{1} g+h_{2} g$, and so

$$
\Lambda g=\Lambda\left(h_{1} g\right)+\Lambda\left(h_{2} g\right) \leq \mu\left(V_{1}\right)+\mu\left(V_{2}\right)
$$

Since (6) holds for every $g \prec V_{1} \cup V_{2}$, (5) follows.

If $\mu\left(E_{i}\right)=\infty$ for some $i$, then (4) is trivially true. Suppose therefore that $\mu\left(E_{i}\right)<\infty$ for every $i$. Choose $\epsilon>0$. By (2) there are open sets $V_{i} \supset E_{i}$ such that

$$
\mu\left(V_{i}\right)<\mu\left(E_{i}\right)+2^{-i} \epsilon \quad(i=1,2,3, \ldots)
$$

Put $V=\bigcup_{1}^{\infty} V_{i}$, and choose $f \prec V$. Since $f$ has compact support, we see that $f \prec V_{1} \cup \cdots \cup V_{n}$ for some $n$. Applying induction to (5), we therefore obtain

$$
\Lambda f \leq \mu\left(V_{1} \cup \cdots \cup V_{n}\right) \leq \mu\left(V_{1}\right)+\cdots+\mu\left(V_{n}\right) \leq \sum_{i=1}^{\infty} \mu\left(E_{i}\right)+\epsilon
$$

Since this holds for every $f \prec V$, and since $\bigcup E_{i} \subset V$, it follows that

$$
\mu\left(\bigcup_{i=1}^{\infty} E_{i}\right) \leq \mu(V) \leq \sum_{i=1}^{\infty} \mu\left(E_{i}\right)+\epsilon
$$

which proves (4), since $\epsilon$ was arbitrary.

STEP II If $K$ is compact, then $K \in \mathfrak{M}_{F}$ and

$$
\mu(K)=\inf \{\Lambda f: K \prec f\}
$$

This implies assertion $(b)$ of the theorem.

ProOF If $K \prec f$ and $0<\alpha<1$, let $V_{\alpha}=\{x: f(x)>\alpha\}$. Then $K \subset V_{\alpha}$, and $\alpha g \leq f$ whenever $g \prec V_{\alpha}$. Hence

$$
\mu(K) \leq \mu\left(V_{\alpha}\right)=\sup \left\{\Lambda g: g \prec V_{\alpha}\right\} \leq \alpha^{-1} \Lambda f
$$

Let $\alpha \rightarrow 1$, to conclude that

$$
\mu(K) \leq \Lambda f
$$

Thus $\mu(K)<\infty$. Since $K$ evidently satisfies (3), $K \in \mathfrak{M}_{F}$.

If $\epsilon>0$, there exists $V \supset K$ with $\mu(V)<\mu(K)+\epsilon$. By Urysohn's lemma, $K \prec f \prec V$ for some $f$. Thus

$$
\Lambda f \leq \mu(V)<\mu(K)+\epsilon
$$

which, combined with (8), gives (7).

STEP III Every open set satisfies (3). Hence $\mathfrak{M}_{F}$ contains every open set $V$ with $\mu(V)<\infty$.

Proof Let $\alpha$ be a real number such that $\alpha<\mu(V)$. There exists an $f \prec V$ with $\alpha<\Lambda f$. If $W$ is any open set which contains the support $K$ of $f$, then $f<W$, hence $\Lambda f \leq \mu(W)$. Thus $\Lambda f \leq \mu(K)$. This exhibits a compact $K \subset V$ with $\alpha<\mu(K)$, so that (3) holds for $V$.

STEP IV Suppose $E=\bigcup_{i=1}^{\infty} E_{i}$, where $E_{1}, E_{2}, E_{3}, \ldots$ are pairwise disjoint members of $\mathfrak{M}_{\boldsymbol{F}}$. Then

$$
\mu(E)=\sum_{i=1}^{\infty} \mu\left(E_{i}\right)
$$

If, in addition, $\mu(E)<\infty$, then also $E \in \mathfrak{M}_{F}$.

Proof We first show that

$$
\mu\left(K_{1} \cup K_{2}\right)=\mu\left(K_{1}\right)+\mu\left(K_{2}\right)
$$

if $K_{1}$ and $K_{2}$ are disjoint compact sets. Choose $\epsilon>0$. By Urysohn's lemma, there exists $f \in C_{c}(X)$ such that $f(x)=1$ on $K_{1}, f(x)=0$ on $K_{2}$, and $0 \leq f \leq 1$. By Step II there exists $g$ such that

$$
K_{1} \cup K_{2} \prec g \text { and } \Lambda g<\mu\left(K_{1} \cup K_{2}\right)+\epsilon \text {. }
$$

Note that $K_{1} \prec f g$ and $K_{2} \prec(1-f) g$. Since $\Lambda$ is linear, it follows from (8) that

$$
\mu\left(K_{1}\right)+\mu\left(K_{2}\right) \leq \Lambda(f g)+\Lambda(g-f g)=\Lambda g<\mu\left(K_{1} \cup K_{2}\right)+\epsilon
$$

Since $\epsilon$ was arbitrary, (10) follows now from Step I.

If $\mu(E)=\infty$, (9) follows from Step I. Assume therefore that $\mu(E)<\infty$, and choose $\epsilon>0$. Since $E_{i} \in \mathfrak{M}_{F}$, there are compact sets $H_{i} \subset E_{i}$ with

$$
\mu\left(H_{i}\right)>\mu\left(E_{i}\right)-2^{-i} \epsilon \quad(i=1,2,3, \ldots)
$$

Putting $K_{n}=H_{1} \cup \cdots \cup H_{n}$ and using induction on (10), we obtain

$$
\mu(E) \geq \mu\left(K_{n}\right)=\sum_{i=1}^{n} \mu\left(H_{i}\right)>\sum_{i=1}^{n} \mu\left(E_{i}\right)-\epsilon
$$

Since (12) holds for every $n$ and every $\epsilon>0$, the left side of (9) is not smaller than the right side, and so (9) follows from Step I.

But if $\mu(E)<\infty$ and $\epsilon>0$, (9) shows that

$$
\mu(E) \leq \sum_{i=1}^{N} \mu\left(E_{i}\right)+\epsilon
$$

for some $N$. By (12), it follows that $\mu(E) \leq \mu\left(K_{N}\right)+2 \epsilon$, and this shows that $E$ satisfies (3); hence $E \in \mathfrak{M}_{F}$.

STEP $\vee$ If $E \in \mathfrak{M}_{F}$ and $\epsilon>0$, there is a compact $K$ and an open $V$ such that $K \subset E \subset V$ and $\mu(V-K)<\epsilon$.

Proof Our definitions show that there exist $K \subset E$ and $V \supset E$ so that

$$
\mu(V)-\frac{\epsilon}{2}<\mu(E)<\mu(K)+\frac{\epsilon}{2} .
$$

Since $V-K$ is open, $V-K \in \mathfrak{M}_{F}$, by Step III. Hence Step IV implies that

$$
\mu(K)+\mu(V-K)=\mu(V)<\mu(K)+\epsilon
$$

STEP VI If $A \in \mathfrak{M}_{F}$ and $B \in \mathfrak{M}_{F}$, then $A-B, A \cup B$, and $A \cap B$ belong to $\mathfrak{M}_{F}$.

PROOF If $\epsilon>0$, Step $\mathrm{V}$ shows that there are sets $K_{i}$ and $V_{i}$ such that $K_{1} \subset A \subset V_{1}, K_{2} \subset B \subset V_{2}$, and $\mu\left(V_{i}-K_{i}\right)<\epsilon$, for $i=1,2$. Since

$$
A-B \subset V_{1}-K_{2} \subset\left(V_{1}-K_{1}\right) \cup\left(K_{1}-V_{2}\right) \cup\left(V_{2}-K_{2}\right)
$$

Step I shows that

$$
\mu(A-B) \leq \epsilon+\mu\left(K_{1}-V_{2}\right)+\epsilon
$$

Since $K_{1}-V_{2}$ is a compact subset of $A-B$, (14) shows that $A-B$ satisfies (3), so that $A-B \in \mathfrak{M}_{F}$.

Since $A \cup B=(A-B) \cup B$, an application of Step IV shows that $A \cup B \in \mathfrak{M}_{F}$. Since $A \cap B=A-(A-B)$, we also have $A \cap B \in \mathfrak{M}_{F}$.

STEP VII $\mathfrak{M}$ is a $\sigma$-algebra in $X$ which contains all Borel sets.

PROOF Let $K$ be an arbitrary compact set in $X$.

If $A \in \mathfrak{M}$, then $A^{c} \cap K=K-(A \cap K)$, so that $A^{c} \cap K$ is a difference of two members of $\mathscr{M}_{F}$. Hence $A^{\mathfrak{c}} \cap K \in \mathfrak{M}_{F}$, and we conclude: $A \in \mathfrak{M}$ implies $A^{c} \in \mathfrak{M}$.

Next, suppose $A=\bigcup_{1}^{\infty} A_{i}$, where each $A_{i} \in \mathfrak{M}$. Put $B_{1}=A_{1} \cap K$, and

$$
B_{n}=\left(A_{n} \cap K\right)-\left(B_{1} \cup \cdots \cup B_{n-1}\right) \quad(n=2,3,4, \ldots)
$$

Then $\left\{B_{n}\right\}$ is a disjoint sequence of members of $\mathfrak{M}_{F}$, by Step VI, and $A \cap K=\bigcup_{1}^{\infty} B_{n}$. It follows from Step IV that $A \cap K \in \mathfrak{M}_{F}$. Hence $A \in \mathfrak{M}$.

Finally, if $C$ is closed, then $C \cap K$ is compact, hence $C \cap K \in \mathfrak{M}_{F}$, so $C \in \mathfrak{M}$. In particular, $X \in \mathfrak{M}$.

We have thus proved that $\mathfrak{M}$ is a $\sigma$-algebra in $X$ which contains all closed subsets of $X$. Hence $\mathfrak{M}$ contains all Borel sets in $X$.

STEP VIII $\mathfrak{M}_{F}$ consists of precisely those sets $E \in \mathfrak{M}$ for which $\mu(E)<\infty$.

This implies assertion $(d)$ of the theorem.

Proof If $E \in \mathfrak{M}_{F}$, Steps II and VI imply that $E \cap K \in \mathfrak{M}_{F}$ for every compact $K$, hence $E \in \mathfrak{M}$.

Conversely, suppose $E \in \mathfrak{M}$ and $\mu(E)<\infty$, and choose $\epsilon>0$. There is an open set $V \supset E$ with $\mu(V)<\infty$; by III and $\mathrm{V}$, there is a compact $K \subset V$ with $\mu(V-K)<\epsilon$. Since $E \cap K \in \mathfrak{M}_{F}$, there is a compact set $H \subset E \cap K$ with

$$
\mu(E \cap K)<\mu(H)+\epsilon
$$

Since $E \subset(E \cap K) \cup(V-K)$, it follows that

$$
\mu(E) \leq \mu(E \cap K)+\mu(V-K)<\mu(H)+2 \epsilon
$$

which implies that $E \in \mathfrak{M}_{F}$.

STEP IX $\mu$ is a measure on $\mathfrak{M}$.

Proof The countable additivity of $\mu$ on $\mathfrak{M}$ follows immediately from Steps IV and VIII.

$\operatorname{STEP} \times$ For every $f \in C_{c}(X), \Lambda f=\int_{X} f d \mu$.

This proves $(a)$, and completes the theorem.

Proof Clearly, it is enough to prove this for real $f$. Also, it is enough to prove the inequality

$$
\Lambda f \leq \int_{x} f d \mu
$$

for every real $f \in C_{c}(X)$. For once (16) is established, the linearity of $\Lambda$ shows that

$$
-\Lambda f=\Lambda(-f) \leq \int_{x}(-f) d \mu=-\int_{x} f d \mu
$$

which, together with (16), shows that equality holds in (16).

Let $K$ be the support of a real $f \in C_{c}(X)$, let $[a, b]$ be an interval which contains the range of $f$ (note the Corollary to Theorem 2.10), choose $\epsilon>0$, and choose $y_{i}$, for $i=0,1, \ldots, n$, so that $y_{i}-y_{i-1}<\epsilon$ and

$$
y_{0}<a<y_{1}<\cdots<y_{n}=b .
$$

Put

$$
E_{i}=\left\{x: y_{i-1}<f(x) \leq y_{i}\right\} \cap K \quad(i=1, \ldots, n)
$$

Since $f$ is continuous, $f$ is Borel measurable, and the sets $E_{i}$ are therefore disjoint Borel sets whose union is $K$. There are open sets $V_{i} \supset E_{i}$ such that

$$
\mu\left(V_{i}\right)<\mu\left(E_{i}\right)+\frac{\epsilon}{n} \quad(i=1, \ldots, n)
$$

and such that $f(x)<y_{i}+\epsilon$ for all $x \in V_{i}$. By Theorem 2.13, there are functions $h_{i} \prec V_{i}$ such that $\sum h_{i}=1$ on $K$. Hence $f=\sum h_{i} f$, and Step II shows that

$$
\mu(K) \leq \Lambda\left(\sum h_{i}\right)=\sum \Lambda h_{i}
$$

Since $h_{i} f \leq\left(y_{i}+\epsilon\right) h_{i}$, and since $y_{i}-\epsilon<f(x)$ on $E_{i}$, we have

$$
\begin{aligned}
\Lambda f & =\sum_{i=1}^{n} \Lambda\left(h_{i} f\right) \leq \sum_{i=1}^{n}\left(y_{i}+\epsilon\right) \Lambda h_{i} \\
& =\sum_{i=1}^{n}\left(|a|+y_{i}+\epsilon\right) \Lambda h_{i}-|a| \sum_{i=1}^{n} \Lambda h_{i} \\
& \leq \sum_{i=1}^{n}\left(|a|+y_{i}+\epsilon\right)\left[\mu\left(E_{i}\right)+\epsilon / n\right]-|a| \mu(K) \\
& =\sum_{i=1}^{n}\left(y_{i}-\epsilon\right) \mu\left(E_{i}\right)+2 \epsilon \mu(K)+\frac{\epsilon}{n} \sum_{i=1}^{n}\left(|a|+y_{i}+\epsilon\right) \\
& \leq \int_{X} f d \mu+\epsilon[2 \mu(K)+|a|+b+\epsilon] .
\end{aligned}
$$

Since $\epsilon$ was arbitrary, (16) is established, and the proof of the theorem is complete.

## Regularity Properties of Borel Measures

2.15 Definition A measure $\mu$ defined on the $\sigma$-algebra of all Borel sets in a locally compact Hausdorff space $X$ is called a Borel measure on $X$. If $\mu$ is positive, a Borel set $E \subset X$ is outer regular or inner regular, respectively, if $E$ has property $(c)$ or $(d)$ of Theorem 2.14. If every Borel set in $X$ is both outer and inner regular, $\mu$ is called regular.

In our proof of the Riesz theorem, outer regularity of every set $E$ was built into the construction, but inner regularity was proved only for the open sets and for those $E \in \mathfrak{M}$ for which $\mu(E)<\infty$. It turns out that this flaw is in the nature of things. One cannot prove regularity of $\mu$ under the hypothesis of Theorem 2.14; an example is described in Exercise 17.

However, a slight strengthening of the hypotheses does give us a regular measure. Theorem 2.17 shows this. And if we specialize a little more, Theorem 2.18 shows that all regularity problems neatly disappear.

2.16 Definition A set $E$ in a topological space is called $\sigma$-compact if $E$ is a countable union of compact sets.

A set $E$ in a measure space (with measure $\mu$ ) is said to have $\sigma$-finite measure if $E$ is a countable union of sets $E_{i}$ with $\mu\left(E_{i}\right)<\infty$.

For example, in the situation described in Theorem 2.14, every $\sigma$ compact set has $\sigma$-finite measure. Also, it is easy to see that if $E \in \mathfrak{M}$ and $E$ has $\sigma$-finite measure, then $E$ is inner regular.

2.17 Theorem Suppose $X$ is a locally compact, $\sigma$-compact Hausdorff space. If $\mathfrak{M}$ and $\mu$ are as described in the statement of Theorem 2.14, then $\mathfrak{M}$ and $\mu$ have the following properties:

(a) If $E \in \mathfrak{M}$ and $\epsilon>0$, there is a closed set $F$ and an open set $V$ such that $F \subset E \subset V$ and $\mu(V-F)<\epsilon$.

(b) $\mu$ is a regular Borel measure on $X$.

(c) If $E \in \mathfrak{M}$, there are sets $A$ and $B$ such that $A$ is an $F_{\sigma}, B$ is $a G_{\delta}$, $A \subset E \subset B$, and $\mu(B-A)=0$.

As a corollary of (c) we see that every $E \in \mathfrak{M}$ is the union of an $F_{\sigma}$ and a set of measure 0 .

ProOF Let $X=K_{1} \cup K_{2} \cup K_{3} \cup \cdots$, where each $K_{n}$ is compact. If $E \in \mathfrak{M}$ and $\epsilon>0$, then $\mu\left(K_{n} \cap E\right)<\infty$, and there are open sets $V_{n} \supset K_{n} \cap E$ such that

$$
\mu\left(V_{n}-\left(K_{n} \cap E\right)\right)<\frac{\epsilon}{2^{n+1}} \quad(n=1,2,3, \ldots)
$$

If $V=\bigcup V_{n}$, then $V-E \subset \bigcup\left(V_{n}-\left(K_{n} \cap E\right)\right)$, so that

$$
\mu(V-E)<\frac{\epsilon}{2}
$$

Apply this to $E^{c}$ in place of $E$ : There is an open set $W \supset E^{c}$ such that $\mu\left(W-E^{c}\right)<\epsilon / 2$. If $F=W^{c}$, then $F \subset E$, and $E-F=W-E^{c}$. Now (a) follows.

Every closed set $F \subset X$ is $\sigma$-compact, because $F=\bigcup\left(F \cap K_{n}\right)$. Hence (a) implies that every set $E \in \mathfrak{M}$ is inner regular. This proves (b).

If we apply $(a)$ with $\epsilon=1 / j(j=1,2,3, \ldots)$, we obtain closed sets $F_{j}$ and open sets $V_{j}$ such that $F_{j} \subset E \subset V_{j}$ and $\mu\left(V_{j}-F_{j}\right)<1 / j$. Put $A=\bigcup F_{j}$ and $B=\bigcap V_{j}$. Then $A \subset E \subset B, A$ is an $F_{\sigma}, B$ is a $G_{\delta}$, and $\mu(B-A)=0$ since $B-A \subset V_{j}-F_{j}$ for $j=1,2,3, \ldots$ This proves (c).

2.18 Theorem Let $X$ be a locally compact Hausdorff space in which every open set is $\sigma$-compact. Let $\lambda$ be any positive Borel measure on $X$ such that $\lambda(K)<\infty$ for every compact set $K$. Then $\lambda$ is regular.

Note that every euclidean space $R^{k}$ satisfies the present hypothesis, since every open set in $R^{k}$ is a countable union of closed balls.

Proof Put $\Lambda f=\int_{X} f d \lambda$, for $f \in C_{c}(X)$. Since $\lambda(K)<\infty$ for every compact $K$, $\Lambda$ is a positive linear functional on $C_{c}(X)$, and there is a regular measure $\mu$, satisfying the conclusions of Theorem 2.17 , such that

$$
\int_{X} f d \lambda=\int_{X} f d \mu \quad\left(f \in C_{c}(X)\right)
$$

We will show that $\lambda=\mu$.

Let $V$ be open in $X$. Then $V=\bigcup K_{i}$, where $K_{i}$ is compact, $i=1,2,3, \ldots$ By Urysohn's lemma we can choose $f_{i}$ so that $K_{i} \prec f_{i} \prec V$. Let $g_{n}=\max \left(f_{1}, \ldots, f_{n}\right)$. Then $g_{n} \in C_{c}(X)$ and $g_{n}(x)$ increases to $\chi_{V}(x)$ at every point $x \in X$. Hence (1) and the monotone convergence theorem imply

$$
\lambda(V)=\lim _{n \rightarrow \infty} \int_{X} g_{n} d \lambda=\lim _{n \rightarrow \infty} \int_{X} g_{n} d \mu=\mu(V)
$$

Now let $E$ be a Borel set in $X$, and choose $\epsilon>0$. Since $\mu$ satisfies Theorem 2.17, there is a closed set $F$ and an open set $V$ such that $F \subset E \subset V$ and $\mu(V-F)<\epsilon$. Hence $\mu(V) \leq \mu(F)+\epsilon \leq \mu(E)+\epsilon$.

Since $V-F$ is open, (2) shows that $\lambda(V-F)<\epsilon$, hence $\lambda(V) \leq \lambda(E)+\epsilon$. Consequently

and

$$
\lambda(E) \leq \lambda(V)=\mu(V) \leq \mu(E)+\epsilon
$$

$$
\mu(E) \leq \mu(V)=\lambda(V) \leq \lambda(E)+\epsilon,
$$

so that $|\lambda(E)-\mu(E)|<\epsilon$ for every $\epsilon>0$. Hence $\lambda(E)=\mu(E)$.

In Exercise 18 a compact Hausdorff space is described in which the complement of a certain point fails to be $\sigma$-compact and in which the conclusion of the preceding theorem is not true.

## Lebesgue Measure

2.19 Euclidean Spaces Euclidean $k$-dimensional space $R^{k}$ is the set of all points $x=\left(\xi_{1}, \ldots, \xi_{k}\right)$ whose coordinates $\xi_{i}$ are real numbers, with the following algebraic and topological structure:

If $x=\left(\xi_{1}, \ldots, \xi_{k}\right), y=\left(\eta_{1}, \ldots, \eta_{k}\right)$, and $\alpha$ is a real number, $x+y$ and $\alpha x$ are defined by

$$
x+y=\left(\xi_{1}+\eta_{1}, \ldots, \xi_{k}+\eta_{k}\right), \quad \alpha x=\left(\alpha \xi_{1}, \ldots, \alpha \xi_{k}\right)
$$

This makes $R^{k}$ into a real vector space. If $x \cdot y=\sum \xi_{i} \eta_{i}$ and $|x|=(x \cdot x)^{1 / 2}$, the Schwarz inequality $|x \cdot y| \leq|x||y|$ leads to the triangle inequality

$$
|x-y| \leq|x-z|+|z-y|
$$

hence we obtain a metric by setting $\rho(x, y)=|x-y|$. We assume that these facts are familiar and shall prove them in greater generality in Chap. 4.

If $E \subset R^{k}$ and $x \in R^{k}$, the translate of $E$ by $x$ is the set

$$
E+x=\{y+x: y \in E\}
$$

A set of the form

$$
W=\left\{x: \alpha_{i}<\xi_{i}<\beta_{i}, 1 \leq i \leq k\right\}
$$

or any set obtained by replacing any or all of the $<$ signs in (4) by $\leq$, is called a $k$-cell; its volume is defined to be

$$
\operatorname{vol}(W)=\prod_{i=1}^{k}\left(\beta_{i}-\alpha_{i}\right)
$$

If $a \in R^{k}$ and $\delta>0$, we shall call the set

$$
Q(a ; \delta)=\left\{x: \alpha_{i} \leq \xi_{i}<\alpha_{i}+\delta, 1 \leq i \leq k\right\}
$$

the $\delta$-box with corner at $a$. Here $a=\left(\alpha_{1}, \ldots, \alpha_{k}\right)$.

For $n=1,2,3, \ldots$, we let $P_{n}$ be the set of all $x \in R^{k}$ whose coordinates are integral multiples of $2^{-n}$, and we let $\Omega_{n}$ be the collection of all $2^{-n}$ boxes with corners at points of $P_{n}$. We shall need the following four properties of $\left\{\Omega_{n}\right\}$. The first three are obvious by inspection.

(a) If $n$ is fixed, each $x \in R^{k}$ lies in one and only one member of $\Omega_{n}$.

(b) If $Q^{\prime} \in \Omega_{n}, Q^{\prime \prime} \in \Omega_{r}$, and $r<n$, then either $Q^{\prime} \subset Q^{\prime \prime}$ or $Q^{\prime} \cap Q^{\prime \prime}=\varnothing$.

(c) If $Q \in \Omega_{r}$, then $\operatorname{vol}(Q)=2^{-r k}$; and if $n>r$, the set $P_{n}$ has exactly $2^{(n-r) k}$ points in $Q$.

(d) Every nonempty open set in $R^{k}$ is a countable union of disjoint boxes belonging to $\Omega_{1} \cup \Omega_{2} \cup \Omega_{3} \cup \cdots$.

ProOf OF (d) If $V$ is open, every $x \in V$ lies in an open ball which lies in $V$; hence $x \in Q \subset V$ for some $Q$ belonging to some $\Omega_{n}$. In other words, $V$ is the union of all boxes which lie in $V$ and which belong to some $\Omega_{n}$. From this collection of boxes, select those which belong to $\Omega_{1}$, and remove those in $\Omega_{2}$, $\Omega_{3}, \ldots$ which lie in any of the selected boxes. From the remaining collection, select those boxes of $\Omega_{2}$ which lie in $V$, and remove those in $\Omega_{3}, \Omega_{4}, \ldots$ which lie in any of the selected boxes. If we proceed in this way, $(a)$ and $(b)$ show that $(d)$ holds.

2.20 Theorem There exists a positive complete measure $m$ defined on a $\sigma$ algebra $\mathfrak{M}$ in $R^{k}$, with the following properties:

(a) $m(W)=\operatorname{vol}(W)$ for every $k$-cell $W$.

(b) $\mathfrak{M}$ contains all Borel sets in $R^{k}$; more precisely, $E \in \mathfrak{M}$ if and only if there are sets $A$ and $B \subset R^{k}$ such that $A \subset E \subset B, A$ is an $F_{\sigma}, B$ is $a G_{\delta}$, and $m(B-A)=0$. Also, $m$ is regular.
(c) $m$ is translation-invariant, i.e.,

$$
m(E+x)=m(E)
$$

for every $E \in \mathfrak{M}$ and every $x \in R^{k}$.

(d) If $\mu$ is any positive translation-invariant Borel measure on $R^{k}$ such that $\mu(K)<\infty$ for every compact set $K$, then there is a constant $c$ such that $\mu(E)=c m(E)$ for all Borel sets $E \subset R^{k}$.

(e) To every linear transformation $T$ of $R^{k}$ into $R^{k}$ corresponds a real number $\Delta(T)$ such that

$$
m(T(E))=\Delta(T) m(E)
$$

for every $E \in \mathfrak{M}$. In particular, $m(T(E))=m(E)$ when $T$ is a rotation.

The members of $\mathfrak{M}$ are the Lebesgue measurable sets in $R^{k} ; m$ is the Lebesgue measure on $R^{k}$. When clarity requires it, we shall write $m_{k}$ in place of $m$.

Proof If $f$ is any complex function on $R^{k}$, with compact support, define

$$
\Lambda_{n} f=2^{-n k} \sum_{x \in P_{n}} f(x) \quad(n=1,2,3, \ldots)
$$

where $P_{n}$ is as in Sec. 2.19.

Now suppose $f \in C_{c}\left(R^{k}\right), f$ is real, $W$ is an open $k$-cell which contains the support of $f$, and $\epsilon>0$. The uniform continuity of $f([26]$, Theorem 4.19) shows that there is an integer $N$ and that there are functions $g$ and $h$ with support in $W$, such that (i) $g$ and $h$ are constant on each box belonging to $\Omega_{N}$, (ii) $g \leq f \leq h$, and (iii) $h-g<\epsilon$. If $n>N$, Property $2.19(c)$ shows that

$$
\Lambda_{N} g=\Lambda_{n} g \leq \Lambda_{n} f \leq \Lambda_{n} h=\Lambda_{N} h
$$

Thus the upper and lower limits of $\left\{\Lambda_{n} f\right\}$ differ by at most $\epsilon$ vol $(W)$, and since $\epsilon$ was arbitrary, we have proved the existence of

$$
\Lambda f=\lim _{n \rightarrow \infty} \Lambda_{n} f \quad\left(f \in C_{c}\left(R^{k}\right)\right)
$$

It is immediate that $\Lambda$ is a positive linear functional on $C_{c}\left(R^{k}\right)$. (In fact, $\Lambda f$ is precisely the Riemann integral of $f$ over $R^{k}$. We went through the preceding construction in order not to have to rely on any theorems about Riemann integrals in several variables.)

We define $m$ and $\mathfrak{M}$ to be the measure and $\sigma$-algebra associated with this $\Lambda$ as in Theorem 2.14.

Since Theorem 2.14 gives us a complete measure and since $R^{k}$ is $\sigma$ compact, Theorem 2.17 implies assertion $(b)$ of Theorem 2.20.

To prove (a), let $W$ be the open cell 2.19(4), let $E_{r}$ be the union of those boxes belonging to $\Omega_{r}$ whose closures lie in $W$, choose $f_{r}$ so that $\bar{E}_{r} \prec$ $f_{r} \prec W$, and put $g_{r}=\max \left\{f_{1}, \ldots, f_{r}\right\}$. Our construction of $\Lambda$ shows that

$$
\operatorname{vol}\left(E_{r}\right) \leq \Lambda f_{r} \leq \Lambda g_{r} \leq \text { vol } W
$$

As $r \rightarrow \infty, \operatorname{vol}\left(E_{r}\right) \rightarrow \operatorname{vol}(W)$, and

$$
\Lambda g_{r}=\int g_{r} d m \rightarrow m(W)
$$

by the monotone convergence theorem, since $g_{r}(x) \rightarrow \chi_{W}(x)$ for all $x \in R^{k}$. Thus $m(W)=\operatorname{vol}(W)$ for every open cell $W$, and since every $k$-cell is the intersection of a decreasing sequence of open $k$-cells, we obtain $(a)$.

The proofs of $(c),(d)$, and $(e)$ will use the following observation: If $\lambda$ is a positive Borel measure on $R^{k}$ and $\lambda(E)=m(E)$ for all boxes $E$, then the same equality holds for all open sets $E$, by property $2.19(d)$, and therefore for all Borel sets $E$, since $\lambda$ and $m$ are regular (Theorem 2.18).

To prove (c), fix $x \in R^{k}$ and define $\lambda(E)=m(E+x)$. It is clear that $\lambda$ is then a measure; by $(a), \lambda(E)=m(E)$ for all boxes, hence $m(E+x)=m(E)$ for all Borel sets $E$. The same equality holds for every $E \in \mathfrak{M}$, because of $(b)$.

Suppose next that $\mu$ satisfies the hypotheses of $(d)$. Let $Q_{0}$ be a 1-box, put $c=\mu\left(Q_{0}\right)$. Since $Q_{0}$ is the union of $2^{n k}$ disjoint $2^{-n}$ boxes that are translates of each other, we have

$$
2^{n k} \mu(Q)=\mu\left(Q_{0}\right)=c m\left(Q_{0}\right)=c \cdot 2^{n k} m(Q)
$$

for every $2^{-n}$-box $Q$. Property $2.19(d)$ implies now that $\mu(E)=c m(E)$ for all open sets $E \subset R^{k}$. This proves $(d)$.

To prove (e), let $T: R^{k} \rightarrow R^{k}$ be linear. If the range of $T$ is a subspace $Y$ of lower dimension, then $m(Y)=0$ and the desired conclusion holds with $\Delta(T)=0$. In the other case, elementary linear algebra tells us that $T$ is a one-to-one map of $R^{k}$ onto $R^{k}$ whose inverse is also linear. Thus $T$ is a homeomorphism of $R^{k}$ onto $R^{k}$, so that $T(E)$ is a Borel set for every Borel set $E$, and we can therefore define a positive Borel measure $\mu$ on $R^{k}$ by

$$
\mu(E)=m(T(E))
$$

The linearity of $T$, combined with the translation-invariance of $m$, gives

$$
\mu(E+x)=m(T(E+x))=m(T(E)+T x)=m(T(E))=\mu(E)
$$

Thus $\mu$ is translation-invariant, and the first assertion of $(e)$ follows from (d), first for Borel sets $E$, then for all $E \in \mathfrak{M}$ by $(b)$.

To find $\Delta(T)$, we merely need to know $m(T(E)) / m(E)$ for one set $E$ with $0<m(E)<\infty$. If $T$ is a rotation, let $E$ be the unit ball of $R^{k}$; then $T(E)=E$, and $\Delta(T)=1$.

2.21 Remarks If $m$ is the Lebesgue measure on $R^{k}$, it is customary to write $L^{1}\left(R^{k}\right)$ in place of $L^{1}(m)$. If $E$ is a Lebesgue measurable subset of $R^{k}$, and if $m$ is restricted to the measurable subsets of $E$, a new measure space is obtained in an obvious fashion. The phrase " $f \in L^{1}$ on $E$ " or " $f \in L^{1}(E)$ " is used to indicate that $f$ is integrable on this measure space.

If $k=1$, if $I$ is any of the sets $(a, b),(a, b],[a, b),[a, b]$, and if $f \in L^{1}(I)$, it is customary to write

$$
\int_{a}^{b} f(x) d x \text { in place of } \int_{I} f d m
$$

Since the Lebesgue measure of any single point is 0 , it makes no difference over which of these four sets the integral is extended.

Everything learned about integration in elementary Calculus courses is still useful in the present context, for if $f$ is a continuous complex function on $[a, b]$, then the Riemann integral of $f$ and the Lebesgue integral of $f$ over $[a, b]$ coincide. This is obvious from our construction if $f(a)=f(b)=0$ and if $f(x)$ is defined to be 0 for $x<a$ and for $x>b$. The general case follows without difficulty. Actually the same thing is true for every Riemann integrable $f$ on $[a, b]$. Since we shall have no occasion to discuss Riemann integrable functions in the sequel, we omit the proof and refer to Theorem 11.33 of [26].

Two natural questions may have occurred to some readers by now: Is every Lebesgue measurable set a Borel set? Is every subset of $R^{k}$ Lebesgue measurable? The answer is negative in both cases, even when $k=1$.

The first question can be settled by a cardinality argument which we sketch briefly. Let $c$ be the cardinality of the continuum (the real line or, equivalently, the collection of all sets of integers). We know that $R^{k}$ has a countable base (open balls with rational radii and with centers in some countable dense subset of $R^{k}$ ), and that $\mathscr{B}_{k}$ (the collection of all Borel sets of $R^{k}$ ) is the $\sigma$-algebra generated by this base. It follows from this (we omit the proof) that $\mathscr{B}_{k}$ has cardinality $c$. On the other hand, there exist Cantor sets $E \subset R^{1}$ with $m(E)=0$. (Exercise 5.) The completeness of $m$ implies that each of the $2^{c}$ subsets of $E$ is Lebesgue measurable. Since $2^{c}>c$, most subsets of $E$ are not Borel sets.

The following theorem answers the second question.

2.22 Theorem If $A \subset R^{1}$ and every subset of $A$ is Lebesgue measurable then $m(A)=0$.

Corollary Every set of positive measure has nonmeasurable subsets.

Proof We shall use the fact that $R^{1}$ is a group, relative to addition. Let $Q$ be the subgroup that consists of the rational numbers, and let $E$ be a set that contains exactly one point from each coset of $Q$ in $R^{1}$. (The assertion that
there is such a set is a direct application of the axiom of choice.) Then $E$ has the following two properties.

(a) $(E+r) \cap(E+s)=\varnothing$ if $r \in Q, s \in Q, r \neq s$.

(b) Every $x \in R^{1}$ lies in $E+r$ for some $r \in Q$.

To prove (a), suppose $x \in(E+r) \cap(E+s)$. Then $x=y+r=z+s$ for some $y \in E, z \in E, y \neq z$. But $y-z=s-r \in Q$, so that $y$ and $z$ lie in the same coset of $Q$, a contradiction.

To prove (b), let $y$ be the point of $E$ that lies in the same coset as $x$, put $r=x-y$.

Fix $t \in Q$, for the moment, and put $A_{t}=A \cap(E+t)$. By hypothesis, $A_{t}$ is measurable. Let $K \subset A_{t}$ be compact, let $H$ be the union of the translates $K+r$, where $r$ ranges over $Q \cap[0,1]$. Then $H$ is bounded, hence $m(H)<\infty$. Since $K \subset E+t,(a)$ shows that the sets $K+r$ are pairwise disjoint. Thus $m(H)=\sum_{r} m(K+r)$. But $m(K+r)=m(K)$. It follows that $m(K)=0$. This holds for every compact $K \subset A_{t}$. Hence $m\left(A_{t}\right)=0$.

Finally, $(b)$ shows that $A=\bigcup A_{t}$, where $t$ ranges over $Q$. Since $Q$ is countable, we conclude that $m(A)=0$.

2.23 Determinants The scale factors $\Delta(T)$ that occur in Theorem $2.20(e)$ can be interpreted algebraically by means of determinants.

Let $\left\{e_{1}, \ldots, e_{k}\right\}$ be the standard basis for $R^{k}$ : the ith coordinate of $e_{j}$ is 1 if $i=j, 0$ if $i \neq j$. If $T: R^{k} \rightarrow R^{k}$ is linear and

$$
T e_{j}=\sum_{i=1}^{k} \alpha_{i j} e_{i} \quad(1 \leq j \leq k)
$$

then det $T$ is, by definition, the determinant of the matrix $[T]$ that has $\alpha_{i j}$ in row $i$ and column $j$.

We claim that

$$
\Delta(T)=|\operatorname{det} T|
$$

If $T=T_{1} T_{2}$, it is clear that $\Delta(T)=\Delta\left(T_{1}\right) \Delta\left(T_{2}\right)$. The multiplication theorem for determinants shows therefore that if (2) holds for $T_{1}$ and $T_{2}$, then (2) also holds for $T$. Since every linear operator on $R^{k}$ is a product of finitely many linear operators of the following three types, it suffices to establish (2) for each of these:

(I) $\left\{T e_{1}, \ldots, T e_{k}\right\}$ is a permutation of $\left\{e_{1}, \ldots, e_{k}\right\}$.

(II) $T e_{1}=\alpha e_{1}, T e_{i}=e_{i}$ for $i=2, \ldots, k$.

(III) $T e_{1}=e_{1}+e_{2}, T e_{i}=e_{i}$ for $i=2, \ldots, k$.

Let $Q$ be the cube consisting of all $x=\left(\xi_{1}, \ldots, \xi_{k}\right)$ with $0 \leq \xi_{i}<1$ for $i=1, \ldots, k$.

If $T$ is of type (I), then $[T]$ has exactly one 1 in each row and each column and has 0 in all other places. So $\operatorname{det} T= \pm 1$. Also, $T(Q)=Q$. So $\Delta(T)=1=|\operatorname{det} T|$.

If $T$ is of type (II), then clearly $\Delta(T)=|\alpha|=|\operatorname{det} T|$.

If $T$ is of type (III), then det $T=1$ and $T(Q)$ is the set of all points $\sum \xi_{i} e_{i}$ whose coordinates satisfy

$$
\xi_{1} \leq \xi_{2}<\xi_{1}+1, \quad 0 \leq \xi_{i}<1 \quad \text { if } \quad i \neq 2
$$

If $S_{1}$ is the set of points in $T(Q)$ that have $\xi_{2}<1$ and if $S_{2}$ is the rest of $T(Q)$, then

$$
S_{1} \cup\left(S_{2}-e_{2}\right)=Q
$$

and $S_{1} \cap\left(S_{2}-e_{2}\right)$ is empty. Hence $\Delta(T)=m\left(S_{1} \cup S_{2}\right)=m\left(S_{1}\right)+m\left(S_{2}-e_{2}\right)=$ $m(Q)=1$, so that we again have $\Delta(T)=|\operatorname{det} T|$.

## Continuity Properties of Measurable Functions

Since the continuous functions played such a prominent role in our construction of Borel measures, and of Lebesgue measure in particular, it seems reasonable to expect that there are some interesting relations between continuous functions and measurable functions. In this section we shall give two theorems of this kind.

We shall assume, in both of them, that $\mu$ is a measure on a locally compact Hausdorff space $X$ which has the properties stated in Theorem 2.14. In particular, $\mu$ could be Lebesgue measure on some $R^{k}$.

2.24 Lusin's Theorem Suppose $f$ is a complex measurable function on $X$, $\mu(A)<\infty, f(x)=0$ if $x \notin A$, and $\epsilon>0$. Then there exists a $g \in C_{c}(X)$ such that

$$
\mu(\{x: f(x) \neq g(x)\})<\epsilon .
$$

Furthermore, we may arrange it so that

$$
\sup _{x \in X}|g(x)| \leq \sup _{x \in X}|f(x)| .
$$

Proof Assume first that $0 \leq f<1$ and that $A$ is compact. Attach a sequence $\left\{s_{n}\right\}$ to $f$, as in the proof of Theorem 1.17, and put $t_{1}=s_{1}$ and $t_{n}=s_{n}-s_{n-1}$ for $n=2,3,4, \ldots$ Then $2^{n} t_{n}$ is the characteristic function of a set $T_{n} \subset A$, and

$$
f(x)=\sum_{n=1}^{\infty} t_{n}(x) \quad(x \in X)
$$

Fix an open set $V$ such that $A \subset V$ and $\bar{V}$ is compact. There are compact sets $K_{n}$ and open sets $V_{n}$ such that $K_{n} \subset T_{n} \subset V_{n} \subset V$ and $\mu\left(V_{n}-K_{n}\right)<2^{-n} \epsilon$. By Urysohn's lemma, there are functions $h_{n}$ such that $K_{n} \prec h_{n} \prec V_{n}$. Define

$$
g(x)=\sum_{n=1}^{\infty} 2^{-n} h_{n}(x) \quad(x \in X)
$$

This series converges uniformly on $X$, so $g$ is continuous. Also, the support of $g$ lies in $\bar{V}$. Since $2^{-n} h_{n}(x)=t_{n}(x)$ except in $V_{n}-K_{n}$, we have $g(x)=f(x)$
except in $\bigcup\left(V_{n}-K_{n}\right)$, and this latter set has measure less than $\epsilon$. Thus (1) holds if $A$ is compact and $0 \leq f \leq 1$.

It follows that (1) holds if $A$ is compact and $f$ is a bounded measurable function. The compactness of $A$ is easily removed, for if $\mu(A)<\infty$ then $A$ contains a compact set $K$ with $\mu(A-K)$ smaller than any preassigned positive number. Next, if $f$ is a complex measurable function and if $B_{n}=$ $\{x:|f(x)|>n\}$, then $\bigcap B_{n}=\varnothing$, so $\mu\left(B_{n}\right) \rightarrow 0$, by Theorem 1.19(e). Since $f$ coincides with the bounded function $\left(1-\chi_{B_{n}}\right) \cdot f$ except on $B_{n}$, (1) follows in the general case.

Finally, let $R=\sup \{|f(x)|: x \in X\}$, and define $\varphi(z)=z$ if $|z| \leq R$, $\varphi(z)=R z /|z|$ if $|z|>R$. Then $\varphi$ is a continuous mapping of the complex plane onto the disc of radius $R$. If $g$ satisfies (1) and $g_{1}=\varphi \circ g$, then $g_{1}$ satisfies (1) and (2).

Corollary Assume that the hypotheses of Lusin's theorem are satisfied and that $|f| \leq 1$. Then there is a sequence $\left\{g_{n}\right\}$ such that $g_{n} \in C_{c}(X),\left|g_{n}\right| \leq 1$, and

$$
f(x)=\lim _{n \rightarrow \infty} g_{n}(x) \quad \text { a.e. }
$$

Proof The theorem implies that to each $n$ there corresponds a $g_{n} \in C_{c}(X)$, with $\left|g_{n}\right| \leq 1$, such that $\mu\left(E_{n}\right) \leq 2^{-n}$, where $E_{n}$ is the set of all $x$ at which $f(x) \neq g_{n}(x)$. For almost every $x$ it is then true that $x$ lies in at most finitely many of the sets $E_{n}$ (Theorem 1.41). For any such $x$, it follows that $f(x)=$ $g_{n}(x)$ for all large enough $n$. This gives (5).

2.25 The Vitali-Carathéodory Theorem Suppose $f \in L^{1}(\mu), f$ is real-valued, and $\epsilon>0$. Then there exist functions $u$ and $v$ on $X$ such that $u \leq f \leq v, u$ is upper semicontinuous and bounded above, $v$ is lower semicontinuous and bounded below, and

$$
\int_{x}(v-u) d \mu<\epsilon
$$

Proof Assume first that $f \geq 0$ and that $f$ is not identically 0 . Since $f$ is the pointwise limit of an increasing sequence of simple functions $s_{n}, f$ is the sum of the simple functions $t_{n}=s_{n}-s_{n-1}$ (taking $s_{0}=0$ ), and since $t_{n}$ is a linear combination of characteristic functions, we see that there are measurable sets $E_{i}$ (not necessarily disjoint) and constants $c_{i}>0$ such that

$$
f(x)=\sum_{i=1}^{\infty} c_{i} \chi_{E_{i}}(x) \quad(x \in X)
$$

Since

$$
\int_{X} f d \mu=\sum_{i=1}^{\infty} c_{i} \mu\left(E_{i}\right)
$$

the series in (3) converges. There are compact sets $K_{i}$ and open sets $V_{i}$ such that $K_{i} \subset E_{i} \subset V_{i}$ and

$$
c_{i} \mu\left(V_{i}-K_{i}\right)<2^{-i-1} \epsilon \quad(i=1,2,3, \ldots)
$$

Put

$$
v=\sum_{i=1}^{\infty} c_{i} \chi_{V_{i}}, \quad u=\sum_{i=1}^{N} c_{i} \chi_{K_{i}}
$$

where $N$ is chosen so that

$$
\sum_{N+1}^{\infty} c_{i} \mu\left(E_{i}\right)<\frac{\epsilon}{2}
$$

Then $v$ is lower semicontinuous, $u$ is upper semicontinuous, $u \leq f \leq v$, and

$$
\begin{aligned}
v-u & =\sum_{i=1}^{N} c_{i}\left(\chi_{V_{i}}-\chi_{K_{i}}\right)+\sum_{N+1}^{\infty} c_{i} \chi_{V_{i}} \\
& \leq \sum_{i=1}^{\infty} c_{i}\left(\chi_{V_{i}}-\chi_{K_{i}}\right)+\sum_{N+1}^{\infty} c_{i} \chi_{E_{i}}
\end{aligned}
$$

so that (4) and (6) imply (1).

In the general case, write $f=f^{+}-f^{-}$, attach $u_{1}$ and $v_{1}$ to $f^{+}$, attach $u_{2}$ and $v_{2}$ to $f^{-}$, as above, and put $u=u_{1}-v_{2}, v=v_{1}-u_{2}$. Since $-v_{2}$ is upper semicontinuous and since the sum of two upper semicontinuous functions is upper semicontinuous (similarly for lower semicontinuous; we leave the proof of this as an exercise), $u$ and $v$ have the desired properties.

## Exercises

1 Let $\left\{f_{n}\right\}$ be a sequence of real nonnegative functions on $R^{1}$, and consider the following four statements:

(a) If $f_{1}$ and $f_{2}$ are upper semicontinuous, then $f_{1}+f_{2}$ is upper semicontinuous.

(b) If $f_{1}$ and $f_{2}$ are lower semicontinuous, then $f_{1}+f_{2}$ is lower semicontinuous.

(c) If each $f_{n}$ is upper semicontinuous, then $\sum_{1}^{\infty} f_{n}$ is upper semicontinuous.

(d) If each $f_{n}$ is lower semicontinuous, then $\sum_{1}^{\infty} f_{n}$ is lower semicontinuous.

Show that three of these are true and that one is false. What happens if the word "nonnegative" is omitted? Is the truth of the statements affected if $R^{1}$ is replaced by a general topological space? 2 Let $f$ be an arbitrary complex function on $R^{1}$, and define

$$
\begin{aligned}
\varphi(x, \delta) & =\sup \{|f(s)-f(t)|: s, t \in(x-\delta, x+\delta)\} \\
\varphi(x) & =\inf \{\varphi(x, \delta): \delta>0\}
\end{aligned}
$$

Prove that $\varphi$ is upper semicontinuous, that $f$ is continuous at a point $x$ if and only if $\varphi(x)=0$, and hence that the set of points of continuity of an arbitrary complex function is a $G_{\delta}$.

Formulate and prove an analogous statement for general topological spaces in place of $R^{1}$.

3 Let $X$ be a metric space, with metric $\rho$. For any nonempty $E \subset X$, define

$$
\rho_{E}(x)=\inf \{\rho(x, y): y \in E\}
$$

Show that $\rho_{E}$ is a uniformly continuous function on $X$. If $A$ and $B$ are disjoint nonempty closed subsets of $X$, examine the relevance of the function

$$
f(x)=\frac{\rho_{A}(x)}{\rho_{A}(x)+\rho_{B}(x)}
$$

to Urysohn's lemma.

4 Examine the proof of the Riesz theorem and prove the following two statements:

(a) If $E_{1} \subset V_{1}$ and $E_{2} \subset V_{2}$, where $V_{1}$ and $V_{2}$ are disjoint open sets, then $\mu\left(E_{1} \cup E_{2}\right)=$ $\mu\left(E_{1}\right)+\mu\left(E_{2}\right)$, even if $E_{1}$ and $E_{2}$ are not in $\mathfrak{M}$.

(b) If $E \in \mathfrak{M}_{F}$, then $E=N \cup K_{1} \cup K_{2} \cup \cdots$, where $\left\{K_{i}\right\}$ is a disjoint countable collection of compact sets and $\mu(N)=0$.

In Exercises 5 to $8, m$ stands for Lebesgue measure on $\boldsymbol{R}^{1}$.

5 Let $E$ be Cantor's familiar "middle thirds" set. Show that $m(E)=0$, even though $E$ and $R^{1}$ have the same cardinality.

6 Construct a totally disconnected compact set $K \subset R^{1}$ such that $m(K)>0$. ( $K$ is to have no connected subset consisting of more than one point.)

If $v$ is lower semicontinuous and $v \leq \chi_{K}$, show that actually $v \leq 0$. Hence $\chi_{K}$ cannot be approximated from below by lower semicontinuous functions, in the sense of the Vitali-Carathéodory theorem.

7 If $0<\epsilon<1$, construct an open set $E \subset[0,1]$ which is dense in [0,1], such that $m(E)=\epsilon$. (To say that $A$ is dense in $B$ means that the closure of $A$ contains $B$.)

8 Construct a Borel set $E \subset R^{1}$ such that

$$
0<m(E \cap I)<m(I)
$$

for every nonempty segment $I$. Is it possible to have $m(E)<\infty$ for such a set?

9 Construct a sequence of continuous function $f_{n}$ on $[0,1]$ such that $0 \leq f_{n} \leq 1$, such that

$$
\lim _{n \rightarrow \infty} \int_{0}^{1} f_{n}(x) d x=0
$$

but such that the sequence $\left\{f_{n}(x)\right\}$ converges for no $x \in[0,1]$.

10 If $\left\{f_{n}\right\}$ is a sequence of continuous functions on $[0,1]$ such that $0 \leq f_{n} \leq 1$ and such that $f_{n}(x) \rightarrow 0$ as $n \rightarrow \infty$, for every $x \in[0,1]$, then

$$
\lim _{n \rightarrow \infty} \int_{0}^{1} f_{n}(x) d x=0
$$

Try to prove this without using any measure theory or any theorems about Lebesgue integration. (This is to impress you with the power of the Lebesgue integral. A nice proof was given by W. F. Eberlein in Communications on Pure and Applied Mathematics, vol. X, pp. 357-360, 1957.)

11 Let $\mu$ be a regular Borel measure on a compact Hausdorff space $X$; assume $\mu(X)=1$. Prove that there is a compact set $K \subset X$ (the carrier or support of $\mu$ ) such that $\mu(K)=1$ but $\mu(H)<1$ for every proper compact subset $H$ of $K$. Hint: Let $K$ be the intersection of all compact $K_{\alpha}$ with $\mu\left(K_{\alpha}\right)=1$; show that every open set $V$ which contains $K$ also contains some $K_{\alpha}$. Regularity of $\mu$ is needed; compare Exercise 18. Show that $K^{c}$ is the largest open set in $X$ whose measure is 0 .

12 Show that every compact subset of $R^{1}$ is the support of a Borel measure.

13 Is it true that every compact subset of $R^{1}$ is the support of a continuous function? If not, can you describe the class of all compact sets in $R^{1}$ which are supports of continuous functions? Is your description valid in other topological spaces?

14 Let $f$ be a real-valued Lebesgue measurable function on $R^{k}$. Prove that there exist Borel functions $g$ and $h$ such that $g(x)=h(x)$ a.e. $[m]$, and $g(x) \leq f(x) \leq h(x)$ for every $x \in R^{k}$.

15 It is easy to guess the limits of

$$
\int_{0}^{n}\left(1-\frac{x}{n}\right)^{n} e^{x / 2} d x \text { and } \int_{0}^{n}\left(1+\frac{x}{n}\right)^{n} e^{-2 x} d x
$$

as $n \rightarrow \infty$. Prove that your guesses are correct.

16 Why is $m(Y)=0$ in the proof of Theorem $2.20(e)$ ?

17 Define the distance between points $\left(x_{1}, y_{1}\right)$ and $\left(x_{2}, y_{2}\right)$ in the plane to be

$$
\left|y_{1}-y_{2}\right| \text { if } x_{1}=x_{2}, \quad 1+\left|y_{1}-y_{2}\right| \quad \text { if } x_{1} \neq x_{2} \text {. }
$$

Show that this is indeed a metric, and that the resulting metric space $X$ is locally compact.

If $f \in C_{c}(X)$, let $x_{1}, \ldots, x_{n}$ be those values of $x$ for which $f(x, y) \neq 0$ for at least one $y$ (there are only finitely many such $x$ !), and define

$$
\Lambda f=\sum_{j=1}^{n} \int_{-\infty}^{\infty} f\left(x_{j}, y\right) d y
$$

Let $\mu$ be the measure associated with this $\Lambda$ by Theorem 2.14. If $E$ is the $x$-axis, show that $\mu(E)=\infty$ although $\mu(K)=0$ for every compact $K \subset E$.

18 This exercise requires more set-theoretic skill than the preceding ones. Let $X$ be a well-ordered uncountable set which has a last element $\omega_{1}$, such that every predecessor of $\omega_{1}$ has at most countably many predecessors. ("Construction": Take any well-ordered set which has elements with uncountably many predecessors, and let $\omega_{1}$ be the first of these; $\omega_{1}$ is called the first uncountable ordinal.) For $\alpha \in X$, let $P_{\alpha}\left[S_{\alpha}\right]$ be the set of all predecessors (successors) of $\alpha$, and call a subset of $X$ open if it is a $P_{\alpha}$ or an $S_{\beta}$ or a $P_{\alpha} \cap S_{\beta}$ or a union of such sets. Prove that $X$ is then a compact Hausdorff space. (Hint: No well-ordered set contains an infinite decreasing sequence.)

Prove that the complement of the point $\omega_{1}$ is an open set which is not $\sigma$-compact.

Prove that to every $f \in C(X)$ there corresponds an $\alpha \neq \omega_{1}$ such that $f$ is constant on $S_{\alpha}$.

Prove that the intersection of every countable collection $\left\{K_{n}\right\}$ of uncountable compact subsets of $X$ is uncountable. (Hint: Consider limits of increasing countable sequences in $X$ which intersect each $K_{n}$ in infinitely many points.)

Let $\mathfrak{M}$ be the collection of all $E \subset X$ such that either $E \cup\left\{\omega_{1}\right\}$ or $E^{\mathfrak{c}} \cup\left\{\omega_{1}\right\}$ contains an uncountable compact set; in the first case, define $\lambda(E)=1$; in the second case, define $\lambda(E)=0$. Prove that $\mathfrak{M}$ is a $\sigma$-algebra which contains all Borel sets in $X$, that $\lambda$ is a measure on $\mathfrak{M}$ which is not regular (every neighborhood of $\omega_{1}$ has measure 1 ), and that

$$
f\left(\omega_{1}\right)=\int_{x} f d \lambda
$$

for every $f \in C(X)$. Describe the regular $\mu$ which Theorem 2.14 associates with this linear functional.

19 Go through the proof of Theorem 2.14, assuming $X$ to be compact (or even compact metric) rather than just locally compact, and see what simplifications you can find.

20 Find continuous functions $f_{n}:[0,1] \rightarrow[0, \infty)$ such that $f_{n}(x) \rightarrow 0$ for all $x \in[0,1]$ as $n \rightarrow \infty$, $\int_{0}^{1} f_{n}(x) d x \rightarrow 0$, but $\sup _{n} f_{n}$ is not in $L^{1}$. (This shows that the conclusion of the dominated convergence theorem may hold even when part of its hypothesis is violated.)

21 If $X$ is compact and $f: X \rightarrow(-\infty, \infty)$ is upper semicontinuous, prove that $f$ attains its maximum at some point of $X$.

22 Suppose that $X$ is a metric space, with metric $d$, and that $f: X \rightarrow[0, \infty]$ is lower semicontinuous, $f(p)<\infty$ for at least one $p \in X$. For $n=1,2,3, \ldots, x \in X$, define

$$
g_{n}(x)=\inf \{f(p)+n d(x, p): p \in X\}
$$

and prove that

(i) $\left|g_{n}(x)-g_{n}(y)\right| \leq n d(x, y)$,

(ii) $0 \leq g_{1} \leq g_{2} \leq \cdots \leq f$,

(iii) $g_{n}(x) \rightarrow f(x)$ as $n \rightarrow \infty$, for all $x \in X$.

Thus $f$ is the pointwise limit of an increasing sequence of continuous functions. (Note that the converse is almost trivial.)

23 Suppose $V$ is open in $R^{k}$ and $\mu$ is a finite positive Borel measure on $R^{k}$. Is the function that sends $x$ to $\mu(V+x)$ necessarily continuous? lower semicontinuous? upper semicontinuous?

24 A step function is, by definition, a finite linear combination of characteristic functions of bounded intervals in $R^{1}$. Assume $f \in L^{1}\left(R^{1}\right)$, and prove that there is a sequence $\left\{g_{n}\right\}$ of step functions so that

$$
\lim _{n \rightarrow \infty} \int_{-\infty}^{\infty}\left|f(x)-g_{n}(x)\right| d x=0
$$

25 (i) Find the smallest constant $c$ such that

$$
\log \left(1+e^{t}\right)<c+t \quad(0<t<\infty)
$$

(ii) Does

$$
\lim _{n \rightarrow \infty} \frac{1}{n} \int_{0}^{1} \log \left\{1+e^{n f(x)}\right\} d x
$$

exist for every real $f \in L^{1}$ ? If it exists, what is it?

## $L^{p}$-SPACES

## Convex Functions and Inequalities

Many of the most common inequalities in analysis have their origin in the notion of convexity.

3.1 Definition A real function $\varphi$ defined on a segment $(a, b)$, where $-\infty \leq a<b \leq \infty$, is called convex if the inequality

$$
\varphi((1-\lambda) x+\lambda y) \leq(1-\lambda) \varphi(x)+\lambda \varphi(y)
$$

holds whenever $a<x<b, a<y<b$, and $0 \leq \lambda \leq 1$.

Graphically, the condition is that if $x<t<y$, then the point $(t, \varphi(t))$ should lie below or on the line connecting the points $(x, \varphi(x))$ and $(y, \varphi(y))$ in the plane. Also, (1) is equivalent to the requirement that

$$
\frac{\varphi(t)-\varphi(s)}{t-s} \leq \frac{\varphi(u)-\varphi(t)}{u-t}
$$

whenever $a<s<t<u<b$.

The mean value theorem for differentiation, combined with (2), shows immediately that a real differentiable function $\varphi$ is convex in $(a, b)$ if and only if $a<s<t<b$ implies $\varphi^{\prime}(s) \leq \varphi^{\prime}(t)$, i.e., if and only if the derivative $\varphi^{\prime}$ is a monotonically increasing function.

For example, the exponential function is convex on $(-\infty, \infty)$.

3.2 Theorem If $\varphi$ is convex on $(a, b)$ then $\varphi$ is continuous on $(a, b)$.

Proof The idea of the proof is most easily conveyed in geometric language. Those who may worry that this is not "rigorous" are invited to transcribe it in terms of epsilons and deltas.

Suppose $a<s<x<y<t<b$. Write $S$ for the point $(s, \varphi(s))$ in the plane, and deal similarly with $x, y$, and $t$. Then $X$ is on or below the line $S Y$, hence $Y$ is on or above the line through $S$ and $X$; also, $Y$ is on or below $X T$. As $y \rightarrow x$, it follows that $Y \rightarrow X$, i.e., $\varphi(y) \rightarrow \varphi(x)$. Left-hand limits are handled in the same manner, and the continuity of $\varphi$ follows.

Note that this theorem depends on the fact that we are working on an open segment. For instance, if $\varphi(x)=0$ on $[0,1)$ and $\varphi(1)=1$, then $\varphi$ satisfies 3.1(1) on $[0,1]$ without being continuous.

3.3 Theorem (Jensen's Inequality) Let $\mu$ be a positive measure on a $\sigma$-algebra $\mathfrak{M}$ in a set $\Omega$, so that $\mu(\Omega)=1$. If $f$ is a real function in $L^{1}(\mu)$, if $a<f(x)<b$ for all $x \in \Omega$, and if $\varphi$ is convex on $(a, b)$, then

$$
\varphi\left(\int_{\Omega} f d \mu\right) \leq \int_{\Omega}(\varphi \circ f) d \mu \text {. }
$$

Note: The cases $a=-\infty$ and $b=\infty$ are not excluded. It may happen that $\varphi \circ f$ is not in $L^{1}(\mu)$; in that case, as the proof will show, the integral of $\varphi \circ f$ exists in the extended sense described in Sec. 1.31, and its value is $+\infty$.

Proof Put $t=f_{\Omega} f d \mu$. Then $a<t<b$. If $\beta$ is the supremum of the quotients on the left of 3.1(2), where $a<s<t$, then $\beta$ is no larger than any of the quotients on the right of 3.1(2), for any $u \in(t, b)$. It follows that

$$
\varphi(s) \geq \varphi(t)+\beta(s-t) \quad(a<s<b)
$$

Hence

$$
\varphi(f(x))-\varphi(t)-\beta(f(x)-t) \geq 0
$$

for every $x \in \Omega$. Since $\varphi$ is continuous, $\varphi \circ f$ is measurable. If we integrate both sides of (3) with respect to $\mu$, (1) follows from our choice of $t$ and the assumption $\mu(\Omega)=1$.

To give an example, take $\varphi(x)=e^{x}$. Then (1) becomes

$$
\exp \left\{\int_{\Omega} f d \mu\right\} \leq \int_{\Omega} e^{f} d \mu
$$

If $\Omega$ is a finite set, consisting of points $p_{1}, \ldots, p_{n}$, say, and if

$$
\mu\left(\left\{p_{i}\right\}\right)=1 / n, \quad f\left(p_{i}\right)=x_{i}
$$

(4) becomes

$$
\exp \left\{\frac{1}{n}\left(x_{1}+\cdots+x_{n}\right)\right\} \leq \frac{1}{n}\left(e^{x_{1}}+\cdots+e^{x_{n}}\right)
$$

for real $x_{i}$. Putting $y_{i}=e^{x_{i}}$, we obtain the familiar inequality between the arithmetic and geometric means of $n$ positive numbers:

$$
\left(y_{1} y_{2} \cdots y_{n}\right)^{1 / n} \leq \frac{1}{n}\left(y_{1}+y_{2}+\cdots+y_{n}\right) .
$$

Going back from this to (4), it should become clear why the left and right sides of

$$
\exp \left\{\int_{\Omega} \log g d \mu\right\} \leq \int_{\Omega} g d \mu
$$

are often called the geometric and arithmetic means, respectively, of the positive function $g$.

If we take $\mu\left(\left\{p_{i}\right\}\right)=\alpha_{i}>0$, where $\sum \alpha_{i}=1$, then we obtain

$$
y_{1}^{\alpha_{1}} y_{2}^{\alpha_{2}} \cdots y_{n}^{\alpha_{n}} \leq \alpha_{1} y_{1}+\alpha_{2} y_{2}+\cdots+\alpha_{n} y_{n}
$$

in place of (6). These are just a few samples of what is contained in Theorem 3.3.

For a converse, see Exercise 20.

3.4 Definition If $p$ and $q$ are positive real numbers such that $p+q=p q$, or equivalently

$$
\frac{1}{p}+\frac{1}{q}=1
$$

then we call $p$ and $q$ a pair of conjugate exponents. It is clear that (1) implies $1<p<\infty$ and $1<q<\infty$. An important special case is $p=q=2$.

As $p \rightarrow 1$, (1) forces $q \rightarrow \infty$. Consequently 1 and $\infty$ are also regarded as a pair of conjugate exponents. Many analysts denote the exponent conjugate to $p$ by $p^{\prime}$, often without saying so explicitly.

3.5 Theorem Let $p$ and $q$ be conjugate exponents, $1<p<\infty$. Let $X$ be a measure space, with measure $\mu$. Let $f$ and $g$ be measurable functions on $X$, with range in $[0, \infty]$. Then

$$
\int_{X} f g d \mu \leq\left\{\int_{X} f^{p} d \mu\right\}^{1 / p}\left\{\int_{X} g^{q} d \mu\right\}^{1 / q}
$$

and

$$
\left\{\int_{X}(f+g)^{p} d \mu\right\}^{1 / p} \leq\left\{\int_{X} f^{p} d \mu\right\}^{1 / p}+\left\{\int_{X} g^{p} d \mu\right\}^{1 / p}
$$

The inequality (1) is Hölder's; (2) is Minkowski's. If $p=q=2$, (1) is known as the Schwarz inequality.

Proof Let $A$ and $B$ be the two factors on the right of (1). If $A=0$, then $f=0$ a.e. (by Theorem 1.39); hence $f g=0$ a.e., so (1) holds. If $A>0$ and $B=\infty$, (1) is again trivial. So we need consider only the case $0<A<\infty, 0<B<\infty$. Put

$$
F=\frac{f}{A}, \quad G=\frac{g}{B}
$$

This gives

$$
\int_{X} F^{p} d \mu=\int_{X} G^{q} d \mu=1
$$

If $x \in X$ is such that $0<F(x)<\infty$ and $0<G(x)<\infty$, there are real numbers $s$ and $t$ such that $F(x)=e^{s / p}, G(x)=e^{t / q}$. Since $1 / p+1 / q=1$, the convexity of the exponential function implies that

$$
e^{s / p+t / q} \leq p^{-1} e^{s}+q^{-1} e^{t}
$$

It follows that

$$
F(x) G(x) \leq p^{-1} F(x)^{p}+q^{-1} G(x)^{q}
$$

for every $x \in X$. Integration of (6) yields

$$
\int_{X} F G d \mu \leq p^{-1}+q^{-1}=1
$$

by (4); inserting (3) into (7), we obtain (1).

Note that (6) could also have been obtained as a special case of the inequality 3.3(8).

To prove (2), we write

$$
(f+g)^{p}=f \cdot(f+g)^{p-1}+g \cdot(f+g)^{p-1}
$$

Hölder's inequality gives

$$
\int f \cdot(f+g)^{p-1} \leq\left\{\int f^{p}\right\}^{1 / p}\left\{\int(f+g)^{(p-1) q}\right\}^{1 / q} .
$$

Let $\left(9^{\prime}\right)$ be the inequality (9) with $f$ and $g$ interchanged. Since $(p-1) q=p$, addition of $(9)$ and $\left(9^{\prime}\right)$ gives

$$
\int(f+g)^{p} \leq\left\{\int(f+g)^{p}\right\}^{1 / q}\left[\left\{\int f^{p}\right\}^{1 / p}+\left\{\int g^{p}\right\}^{1 / p}\right] \text {. }
$$

Clearly, it is enough to prove (2) in the case that the left side is greater than 0 and the right side is less than $\infty$. The convexity of the function $t^{p}$ for $0<t<\infty$ shows that

$$
\left(\frac{f+g}{2}\right)^{p} \leq \frac{1}{2}\left(f^{p}+g^{p}\right)
$$

Hence the left side of (2) is less than $\infty$, and (2) follows from (10) if we divide by the first factor on the right of (10), bearing in mind that $1-1 / q=1 / p$. This completes the proof.

It is sometimes useful to know the conditions under which equality can hold in an inequality. In many cases this information may be obtained by examining the proof of the inequality.

For instance, equality holds in (7) if and only if equality holds in (6) for almost every $x$. In (5), equality holds if and only if $s=t$. Hence " $F^{p}=G^{q}$ a.e." is a necessary and sufficient condition for equality in (7), if (4) is assumed. In terms of the original functions $f$ and $g$, the following result is then obtained:

Assuming $A<\infty$ and $B<\infty$, equality holds in (1) if and only if there are constants $\alpha$ and $\beta$, not both 0 , such that $\alpha f^{p}=\beta g^{q}$ a.e.

We leave the analogous discussion of equality in (2) as an exercise.

## The $L^{p}$-spaces

In this section, $X$ will be an arbitrary measure space with a positive measure $\mu$.

3.6 Definition If $0<p<\infty$ and if $f$ is a complex measurable function on $X$, define

$$
\|f\|_{p}=\left\{\int_{X}|f|^{p} d \mu\right\}^{1 / p}
$$

and let $L^{p}(\mu)$ consist of all $f$ for which

$$
\|f\|_{p}<\infty
$$

We call $\|f\|_{p}$ the $L^{p}$-norm of $f$.

If $\mu$ is Lebesgue measure on $R^{k}$, we write $L^{p}\left(R^{k}\right)$ instead of $L^{p}(\mu)$, as in Sec. 2.21. If $\mu$ is the counting measure on a set $A$, it is customary to denote the corresponding $L^{p}$-space by $\ell^{p}(A)$, or simply by $\ell^{p}$, if $A$ is countable. An element of $\ell^{p}$ may be regarded as a complex sequence $x=\left\{\xi_{n}\right\}$, and

$$
\|x\|_{p}=\left\{\sum_{n=1}^{\infty}\left|\xi_{n}\right|^{p}\right\}^{1 / p}
$$

3.7 Definition Suppose $g: X \rightarrow[0, \infty]$ is measurable. Let $S$ be the set of all real $\alpha$ such that

$$
\mu\left(g^{-1}((\alpha, \infty])\right)=0
$$

If $S=\varnothing$, put $\beta=\infty$. If $S \neq \varnothing$, put $\beta=\inf S$. Since

$$
g^{-1}((\beta, \infty])=\bigcup_{n=1}^{\infty} g^{-1}\left(\left(\beta+\frac{1}{n}, \infty\right]\right)
$$

and since the union of a countable collection of sets of measure 0 has measure 0 , we see that $\beta \in S$. We call $\beta$ the essential supremum of $g$.

If $f$ is a complex measurable function on $X$, we define $\|f\|_{\infty}$ to be the essential supremum of $|f|$, and we let $L^{\infty}(\mu)$ consist of all $f$ for which $\|f\|_{\infty}<\infty$. The members of $L^{\infty}(\mu)$ are sometimes called essentially bounded measurable functions on $X$.

It follows from this definition that the inequality $|f(x)| \leq \lambda$ holds for almost all $x$ if and only if $\lambda \geq\|f\|_{\infty}$.

As in Definition 3.6, $L^{\infty}\left(R^{k}\right)$ denotes the class of all essentially bounded (with respect to Lebesgue measure) functions on $R^{k}$, and $\ell^{\infty}(A)$ is the class of all bounded functions on $A$. (Here bounded means the same as essentially bounded, since every nonempty set has positive measure!)

3.8 Theorem If $p$ and $q$ are conjugate exponents, $1 \leq p \leq \infty$, and if $f \in L^{p}(\mu)$ and $g \in L^{q}(\mu)$, then $f g \in L^{1}(\mu)$, and

$$
\|f g\|_{1} \leq\|f\|_{p}\|g\|_{q} .
$$

ProOF For $1<p<\infty,(1)$ is simply Hölder's inequality, applied to $|f|$ and $|g|$. If $p=\infty$, note that

$$
|f(x) g(x)| \leq\|f\|_{\infty}|g(x)|
$$

for almost all $x$; integrating (2), we obtain (1). If $p=1$, then $q=\infty$, and the same argument applies.

3.9 Theorem Suppose $1 \leq p \leq \infty$, and $f \in L^{p}(\mu), g \in L^{p}(\mu)$. Then $f+g \in L^{p}(\mu)$, and

$$
\|f+g\|_{p} \leq\|f\|_{p}+\|g\|_{p} .
$$

ProOF For $1<p<\infty$, this follows from Minkowski's inequality, since

$$
\int_{X}|f+g|^{p} d \mu \leq \int_{X}(|f|+|g|)^{p} d \mu .
$$

For $p=1$ or $p=\infty$, (1) is a trivial consequence of the inequality $|f+g| \leq|f|+|g|$.

3.10 Remarks Fix $p, 1 \leq p \leq \infty$. If $f \in L^{p}(\mu)$ and $\alpha$ is a complex number, it is clear that $\alpha f \in L^{p}(\mu)$. In fact,

$$
\|\alpha f\|_{p}=|\alpha|\|f\|_{p}
$$

In conjunction with Theorem 3.9, this shows that $L^{p}(\mu)$ is a complex vector space.

Suppose $f, g$, and $h$ are in $L^{p}(\mu)$. Replacing $f$ by $f-g$ and $g$ by $g-h$ in Theorem 3.9, we obtain

$$
\|f-h\|_{p} \leq\|f-g\|_{p}+\|g-h\|_{p} .
$$

This suggests that a metric may be introduced in $L^{p}(\mu)$ by defining the distance between $f$ and $g$ to be $\|f-g\|_{p}$. Call this distance $d(f, g)$ for the moment. Then $0 \leq d(f, g)<\infty, d(f, f)=0, d(f, g)=d(g, f)$, and (2) shows that the triangle inequality $d(f, h) \leq d(f, g)+d(g, h)$ is satisfied. The only other property which $d$ should have to define a metric space is that $d(f, g)=0$ should imply that $f=g$. In our present situation this need not be so; we have $d(f, g)=0$ precisely when $f(x)=g(x)$ for almost all $x$.

Let us write $f \sim g$ if and only if $d(f, g)=0$. It is clear that this is an equivalence relation in $L^{p}(\mu)$ which partitions $L^{p}(\mu)$ into equivalence classes; each class consists of all functions which are equivalent to a given one. If $F$ and $G$ are two equivalence classes, choose $f \in F$ and $g \in G$, and define $d(F, G)=d(f, g)$; note that $f \sim f_{1}$ and $g \sim g_{1}$ implies

$$
d(f, g)=d\left(f_{1}, g_{1}\right)
$$

so that $d(F, G)$ is well defined.

With this definition, the set of equivalence classes is now a metric space. Note that it is also a vector space, since $f \sim f_{1}$ and $g \sim g_{1}$ implies $f+g \sim$ $f_{1}+g_{1}$ and $\alpha f \sim \alpha f_{1}$.

When $L^{p}(\mu)$ is regarded as a metric space, then the space which is really under consideration is therefore not a space whose elements are functions, but a space whose elements are equivalence classes of functions. For the sake of simplicity of language, it is, however, customary to relegate this distinction to the status of a tacit understanding and to continue to speak of $L^{p}(\mu)$ as a space of functions. We shall follow this custom.

If $\left\{f_{n}\right\}$ is a sequence in $L^{p}(\mu)$, if $f \in L^{p}(\mu)$, and if $\lim _{n \rightarrow \infty}\left\|f_{n}-f\right\|_{p}=0$, we say that $\left\{f_{n}\right\}$ converges to $f$ in $L^{p}(\mu)$ (or that $\left\{f_{n}\right\}$ converges to $f$ in the mean of order $p$, or that $\left\{f_{n}\right\}$ is $L^{p}$-convergent to $f$ ). If to every $\epsilon>0$ there corresponds an integer $N$ such that $\left\|f_{n}-f_{m}\right\|_{p}<\epsilon$ as soon as $n>N$ and $m>N$, we call $\left\{f_{n}\right\}$ a Cauchy sequence in $L^{p}(\mu)$. These definitions are exactly as in any metric space.

It is a very important fact that $L^{p}(\mu)$ is a complete metric space, i.e., that every Cauchy sequence in $L^{p}(\mu)$ converges to an element of $L^{p}(\mu)$ :

3.11 Theorem $L^{p}(\mu)$ is a complete metric space, for $1 \leq p \leq \infty$ and for every positive measure $\mu$.

Proof Assume first that $1 \leq p<\infty$. Let $\left\{f_{n}\right\}$ be a Cauchy sequence in $L^{p}(\mu)$. There is a subsequence $\left\{f_{n_{i}}\right\}, n_{1}<n_{2}<\cdots$, such that

$$
\left\|f_{n_{i+1}}-f_{n i}\right\|_{p}<2^{-i} \quad(i=1,2,3, \ldots)
$$

Put

$$
g_{k}=\sum_{i=1}^{k}\left|f_{n_{i+1}}-f_{n_{i}}\right|, \quad g=\sum_{i=1}^{\infty}\left|f_{n_{i+1}}-f_{n_{i}}\right|
$$

Since (1) holds, the Minkowski inequality shows that $\left\|g_{k}\right\|_{p}<1$ for $k=1$, $2,3, \ldots$. Hence an application of Fatou's lemma to $\left\{g_{k}^{p}\right\}$ gives $\|g\|_{p} \leq 1$. In particular, $g(x)<\infty$ a.e., so that the series

$$
f_{n_{1}}(x)+\sum_{i=1}^{\infty}\left(f_{n_{i+1}}(x)-f_{n_{i}}(x)\right)
$$

converges absolutely for almost every $x \in X$. Denote the sum of (3) by $f(x)$, for those $x$ at which (3) converges; put $f(x)=0$ on the remaining set of measure zero. Since

$$
f_{n_{1}}+\sum_{i=1}^{k-1}\left(f_{n_{i}+1}-f_{n_{i}}\right)=f_{n_{k}}
$$

we see that

$$
f(x)=\lim _{i \rightarrow \infty} f_{n_{i}}(x) \quad \text { a.e. }
$$

Having found a function $f$ which is the pointwise limit a.e. of $\left\{f_{n_{i}}\right\}$, we now have to prove that this $f$ is the $L^{p}$-limit of $\left\{f_{n}\right\}$. Choose $\epsilon>0$. There exists an $N$ such that $\left\|f_{n}-f_{m}\right\|_{p}<\epsilon$ if $n>N$ and $m>N$. For every $m>N$, Fatou's lemma shows therefore that

$$
\int_{X}\left|f-f_{m}\right|^{p} d \mu \leq \lim _{i \rightarrow \infty} \inf _{X}\left|f_{n_{i}}-f_{i m}\right|^{p} d \mu \leq \epsilon^{p}
$$

We conclude from (6) that $f-f_{m} \in L^{p}(\mu)$, hence that $f \in L^{p}(\mu)$ [since $f=$ $\left.\left(f-f_{m}\right)+f_{m}\right]$, and finally that $\left\|f-f_{m}\right\|_{p} \rightarrow 0$ as $m \rightarrow \infty$. This completes the proof for the case $1 \leq p<\infty$.

In $L^{\infty}(\mu)$ the proof is much easier. Suppose $\left\{f_{n}\right\}$ is a Cauchy sequence in $L^{\infty}(\mu)$, let $A_{k}$ and $B_{m, n}$ be the sets where $\left|f_{k}(x)\right|>\left\|f_{k}\right\|_{\infty}$ and where $\left|f_{n}(x)-f_{m}(x)\right|>\left\|f_{n}-f_{m}\right\|_{\infty}$, and let $E$ be the union of these sets, for $k, m$, $n=1,2,3, \ldots$ Then $\mu(E)=0$, and on the complement of $E$ the sequence $\left\{f_{n}\right\}$ converges uniformly to a bounded function $f$. Define $f(x)=0$ for $x \in E$. Then $f \in L^{\infty}(\mu)$, and $\left\|f_{n}-f\right\|_{\infty} \rightarrow 0$ as $n \rightarrow \infty$.

The preceding proof contains a result which is interesting enough to be stated separately:

3.12 Theorem If $1 \leq p \leq \infty$ and if $\left\{f_{n}\right\}$ is a Cauchy sequence in $L^{p}(\mu)$, with limit $f$, then $\left\{f_{n}\right\}$ has a subsequence which converges pointwise almost everywhere to $f(x)$.

The simple functions play an interesting role in $L^{p}(\mu)$ :

3.13 Theorem Let $S$ be the class of all complex, measurable, simple functions on $X$ such that

$$
\mu(\{x: s(x) \neq 0\})<\infty
$$

If $1 \leq p<\infty$, then $S$ is dense in $L^{p}(\mu)$.

Proof First, it is clear that $S \subset L^{p}(\mu)$. Suppose $f \geq 0, f \in L^{p}(\mu)$, and let $\left\{s_{n}\right\}$ be as in Theorem 1.17. Since $0 \leq s_{n} \leq f$, we have $s_{n} \in L^{p}(\mu)$, hence $s_{n} \in S$. Since $\left|f-s_{n}\right|^{p} \leq f^{p}$, the dominated convergence theorem shows that $\left\|f-s_{n}\right\|_{p} \rightarrow 0$ as $n \rightarrow \infty$. Thus $f$ is in the $L^{p}$-closure of $S$. The general case ( $f$ complex) follows from this.

## Approximation by Continuous Functions

So far we have considered $L^{p}(\mu)$ on any measure space. Now let $X$ be a locally compact Hausdorff space, and let $\mu$ be a measure on a $\sigma$-algebra $\mathfrak{M}$ in $X$, with the properties stated in Theorem 2.14. For example, $X$ might be $R^{k}$, and $\mu$ might be Lebesgue measure on $R^{k}$.

Under these circumstances, we have the following analogue of Theorem 3.13:

3.14 Theorem For $1 \leq p<\infty, C_{c}(X)$ is dense in $L^{p}(\mu)$.

Proof Define $S$ as in Theorem 3.13. If $s \in S$ and $\epsilon>0$, there exists a $g \in$ $C_{c}(X)$ such that $g(x)=s(x)$ except on a set of measure $<\epsilon$, and $|g| \leq\|s\|_{\infty}$ (Lusin's theorem). Hence

$$
\|g-s\|_{p} \leq 2 \epsilon^{1 / p}\|s\|_{\infty}
$$

Since $S$ is dense in $L^{p}(\mu)$, this completes the proof.

3.15 Remarks Let us discuss the relations between the spaces $L^{p}\left(R^{k}\right)$ (the $L^{p}$ spaces in which the underlying measure is Lebesgue measure on $R^{k}$ ) and the space $C_{c}\left(R^{k}\right)$ in some detail. We consider a fixed dimension $k$.

For every $p \in[1, \infty]$ we have a metric on $C_{c}\left(R^{k}\right)$; the distance between $f$ and $g$ is $\|f-g\|_{p}$. Note that this is a genuine metric, and that we do not have to pass to equivalence classes. The point is that if two continuous functions on $R^{k}$ are not identical, then they differ on some nonempty open set $V$, and $m(V)>0$, since $V$ contains a $k$-cell. Thus if two members of $C_{c}\left(R^{k}\right)$ are equal a.e., they are equal. It is also of interest to note that in $C_{c}\left(R^{k}\right)$ the essential supremum is the same as the actual supremum: for $f \in C_{c}\left(R^{k}\right)$

$$
\|f\|_{\infty}=\sup _{x \in R^{k}}|f(x)| .
$$

If $1 \leq p<\infty$, Theorem 3.14 says that $C_{c}\left(R^{k}\right)$ is dense in $L^{p}\left(R^{k}\right)$, and Theorem 3.11 shows that $L^{p}\left(R^{k}\right)$ is complete. Thus $L^{p}\left(R^{k}\right)$ is the completion of the metric space which is obtained by endowing $C_{c}\left(R^{k}\right)$ with the $L^{p}$-metric.

The cases $p=1$ and $p=2$ are the ones of greatest interest. Let us state once more, in different words, what the preceding result says if $p=1$ and $k=1$; the statement shows that the Lebesgue integral is indeed the "right" generalization of the Riemann integral:

If the distance between two continuous functions $f$ and $g$, with compact supports in $R^{1}$, is defined to be

$$
\int_{-\infty}^{\infty}|f(t)-g(t)| d t
$$

the completion of the resulting metric space consists precisely of the Lebesgue integrable functions on $R^{1}$, provided we identify any two that are equal almost everywhere.

Of course, every metric space $S$ has a completion $S^{*}$ whose elements may be viewed abstractly as equivalence classes of Cauchy sequences in $S$ (see [26], p. 82). The important point in the present situation is that the various $L^{p}$ completions of $C_{c}\left(R^{k}\right)$ again turn out to be spaces of functions on $R^{k}$.

The case $p=\infty$ differs from the cases $p<\infty$. The $L^{\infty}$-completion of $C_{c}\left(R^{k}\right)$ is not $L^{\infty}\left(R^{k}\right)$, but is $C_{0}\left(R^{k}\right)$, the space of all continuous functions on $R^{k}$ which "vanish at infinity," a concept which will be defined in Sec. 3.16. Since (1) shows that the $L^{\infty}$-norm coincides with the supremum norm on $C_{c}\left(R^{k}\right)$, the above assertion about $C_{0}\left(R^{k}\right)$ is a special case of Theorem 3.17.

3.16 Definition A complex function $f$ on a locally compact Hausdorff space $X$ is said to vanish at infinity if to every $\epsilon>0$ there exists a compact set $K \subset X$ such that $|f(x)|<\epsilon$ for all $x$ not in $K$.

The class of all continuous $f$ on $X$ which vanish at infinity is called $C_{0}(X)$.

It is clear that $C_{c}(X) \subset C_{0}(X)$, and that the two classes coincide if $X$ is compact. In that case we write $C(X)$ for either of them.

3.17 Theorem If $X$ is a locally compact Hausdorff space, then $C_{0}(X)$ is the completion of $C_{c}(X)$, relative to the metric defined by the supremum norm

$$
\|f\|=\sup _{x \in X}|f(x)|
$$

Proof An elementary verification shows that $C_{0}(X)$ satisfies the axioms of a metric space if the distance between $f$ and $g$ is taken to be $\|f-g\|$. We have to show that $(a) C_{c}(X)$ is dense in $C_{0}(X)$ and $(b) C_{0}(X)$ is a complete metric space.

Given $f \in C_{0}(X)$ and $\epsilon>0$, there is a compact set $K$ so that $|f(x)|<\epsilon$ outside $K$. Urysohn's lemma gives us a function $g \in C_{c}(X)$ such that $0 \leq g \leq 1$ and $g(x)=1$ on $K$. Put $h=f g$. Then $h \in C_{c}(X)$ and $\|f-h\|<\epsilon$. This proves $(a)$.

To prove $(b)$, let $\left\{f_{n}\right\}$ be a Cauchy sequence in $C_{0}(X)$, i.e., assume that $\left\{f_{n}\right\}$ converges uniformly. Then its pointwise limit function $f$ is continuous. Given $\epsilon>0$, there exists an $n$ so that $\left\|f_{n}-f\right\|<\epsilon / 2$ and there is a compact set $K$ so that $\left|f_{n}(x)\right|<\epsilon / 2$ outside $K$. Hence $|f(x)|<\epsilon$ outside $K$, and we have proved that $f$ vanishes at infinity. Thus $C_{0}(X)$ is complete.

## Exercises

1 Prove that the supremum of any collection of convex functions on $(a, b)$ is convex on $(a, b)$ (if it is finite) and that pointwise limits of sequences of convex functions are convex. What can you say about upper and lower limits of sequences of convex functions?

2 If $\varphi$ is convex on $(a, b)$ and if $\psi$ is convex and nondecreasing on the range of $\varphi$, prove that $\psi \circ \varphi$ is convex on $(a, b)$. For $\varphi>0$, show that the convexity of $\log \varphi$ implies the convexity of $\varphi$, but not vice versa.

3 Assume that $\varphi$ is a continuous real function on $(a, b)$ such that

$$
\varphi\left(\frac{x+y}{2}\right) \leq \frac{1}{2} \varphi(x)+\frac{1}{2} \varphi(y)
$$

for all $x$ and $y \in(a, b)$. Prove that $\varphi$ is convex. (The conclusion does not follow if continuity is omitted from the hypotheses.)

4 Suppose $f$ is a complex measurable function on $X, \mu$ is a positive measure on $X$, and

$$
\varphi(p)=\int_{x}|f|^{p} d \mu=\|f\|_{p}^{p} \quad(0<p<\infty)
$$

Let $E=\{p: \varphi(p)<\infty\}$. Assume $\|f\|_{\infty}>0$.

(a) If $r<p<s, r \in E$, and $s \in E$, prove that $p \in E$.

(b) Prove that $\log \varphi$ is convex in the interior of $E$ and that $\varphi$ is continuous on $E$.

(c) By $(a), E$ is connected. Is $E$ necessarily open? Closed? Can $E$ consist of a single point? Can $E$ be any connected subset of $(0, \infty)$ ?

(d) If $r<p<s$, prove that $\|f\|_{p} \leq \max \left(\|f\|_{r},\|f\|_{s}\right)$. Show that this implies the inclusion $L(\mu) \cap L^{s}(\mu) \subset L^{p}(\mu)$.

(e) Assume that $\|f\|_{r}<\infty$ for some $r<\infty$ and prove that

$$
\|f\|_{p} \rightarrow\|f\|_{\infty} \quad \text { as } p \rightarrow \infty
$$

5 Assume, in addition to the hypotheses of Exercise 4, that

$$
\mu(X)=1
$$

(a) Prove that $\|f\|_{r} \leq\|f\|_{s}$ if $0<r<s \leq \infty$.

(b) Under what conditions does it happen that $0<r<s \leq \infty$ and $\|f\|_{r}=\|f\|_{s}<\infty$ ?

(c) Prove that $L(\mu) \supset L^{s}(\mu)$ if $0<r<s$. Under what conditions do these two spaces contain the same functions?

(d) Assume that $\|f\|_{r}<\infty$ for some $r>0$, and prove that

if $\exp \{-\infty\}$ is defined to be 0 .

$$
\lim _{p \rightarrow 0}\|f\|_{p}=\exp \left\{\int_{x} \log |f| d \mu\right\}
$$

6 Let $m$ be Lebesgue measure on $[0,1]$, and define $\|f\|_{p}$ with respect to $m$. Find all functions $\Phi$ on $[0, \infty)$ such that the relation

$$
\Phi\left(\lim _{p \rightarrow 0}\|f\|_{p}\right)=\int_{0}^{1}(\Phi \circ f) d m
$$

holds for every bounded, measurable, positive $f$. Show first that

$$
c \Phi(x)+(1-c) \Phi(1)=\Phi\left(x^{c}\right) \quad(x>0,0 \leq c \leq 1)
$$

Compare with Exercise 5(d).

7 For some measures, the relation $r<s$ implies $L^{r}(\mu) \subset L^{s}(\mu)$; for others, the inclusion is reversed; and there are some for which $L^{r}(\mu)$ does not contain $L^{s}(\mu)$ if $r \neq s$. Give examples of these situations, and find conditions on $\mu$ under which these situations will occur.

8 If $g$ is a positive function on $(0,1)$ such that $g(x) \rightarrow \infty$ as $x \rightarrow 0$, then there is a convex function $h$ on $(0,1)$ such that $h \leq g$ and $h(x) \rightarrow \infty$ as $x \rightarrow 0$. True or false? Is the problem changed if $(0,1)$ is replaced by $(0, \infty)$ and $x \rightarrow 0$ is replaced by $x \rightarrow \infty$ ?

9 Suppose $f$ is Lebesgue measurable on $(0,1)$, and not essentially bounded. By Exercise $4(e)$, $\|f\|_{p} \rightarrow \infty$ as $p \rightarrow \infty$. Can $\|f\|_{p}$ tend to $\infty$ arbitrarily slowly? More precisely, is it true that to every positive function $\Phi$ on $(0, \infty)$ such that $\Phi(p) \rightarrow \infty$ as $p \rightarrow \infty$ one can find an $f$ such that $\|f\|_{p} \rightarrow \infty$ as $p \rightarrow \infty$, but $\|f\|_{p} \leq \Phi(p)$ for all sufficiently large $p$ ?

10 Suppose $f_{n} \in L^{p}(\mu)$, for $n=1,2,3, \ldots$, and $\left\|f_{n}-f\right\|_{p} \rightarrow 0$ and $f_{n} \rightarrow g$ a.e., as $n \rightarrow \infty$. What relation exists between $f$ and $g$ ?

11 Suppose $\mu(\Omega)=1$, and suppose $f$ and $g$ are positive measurable functions on $\Omega$ such that $f g \geq 1$. Prove that

$$
\int_{\Omega} f d \mu \cdot \int_{\Omega} g d \mu \geq 1
$$

12 Suppose $\mu(\Omega)=1$ and $h: \Omega \rightarrow[0, \infty]$ is measurable. If

$$
A=\int_{\Omega} h d \mu
$$

prove that

$$
\sqrt{1+A^{2}} \leq \int_{\Omega} \sqrt{1+h^{2}} d \mu \leq 1+A
$$

If $\mu$ is Lebesgue measure on $[0,1]$ and if $h$ is continuous, $h=f^{\prime}$, the above inequalities have a simple geometric interpretation. From this, conjecture (for general $\Omega$ ) under what conditions on $h$ equality can hold in either of the above inequalities, and prove your conjecture.

13 Under what conditions on $f$ and $g$ does equality hold in the conclusions of Theorems 3.8 and 3.9? You may have to treat the cases $p=1$ and $p=\infty$ separately.

14 Suppose $1<p<\infty, f \in L^{p}=L^{p}((0, \infty))$, relative to Lebesgue measure, and

$$
F(x)=\frac{1}{x} \int_{0}^{x} f(t) d t \quad(0<x<\infty)
$$

(a) Prove Hardy's inequality

$$
\|F\|_{p} \leq \frac{p}{p-1}\|f\|_{p}
$$

which shows that the mapping $f \rightarrow F$ carries $L^{p}$ into $L^{p}$.
(b) Prove that equality holds only if $f=0$ a.e.

(c) Prove that the constant $p /(p-1)$ cannot be replaced by a smaller one.

(d) If $f>0$ and $f \in L^{1}$, prove that $F \notin L^{1}$.

Suggestions: (a) Assume first that $f \geq 0$ and $f \in C_{c}((0, \infty))$. Integration by parts gives

$$
\int_{0}^{\infty} F^{p}(x) d x=-p \int_{0}^{\infty} F^{p-1}(x) x F^{\prime}(x) d x
$$

Note that $x F^{\prime}=f-F$, and apply Hölder's inequality to $\int F^{p-1} f$. Then derive the general case. (c) Take $f(x)=x^{-1 / p}$ on $[1, A], f(x)=0$ elsewhere, for large $A$. See also Exercise 14, Chap. 8.

15 Suppose $\left\{a_{n}\right\}$ is a sequence of positive numbers. Prove that

$$
\sum_{N=1}^{\infty}\left(\frac{1}{N} \sum_{n=1}^{N} a_{n}\right)^{p} \leq\left(\frac{p}{p-1}\right)^{p} \sum_{n=1}^{\infty} a_{n}^{p}
$$

if $1<p<\infty$. Hint: If $a_{n} \geq a_{n+1}$, the result can be made to follow from Exercise 14. This special case implies the general one.

16 Prove Egoroff's theorem: If $\mu(X)<\infty$, if $\left\{f_{n}\right\}$ is a sequence of complex measurable functions which converges pointwise at every point of $X$, and if $\epsilon>0$, there is a measurable set $E \subset X$, with $\mu(X-E)<\epsilon$, such that $\left\{f_{n}\right\}$ converges uniformly on $E$.

(The conclusion is that by redefining the $f_{n}$ on a set of arbitrarily small measure we can convert a pointwise convergent sequence to a uniformly convergent one; note the similarity with Lusin's theorem.)

Hint: Put

$$
S(n, k)=\bigcap_{i, j>n}\left\{x:\left|f_{i}(x)-f_{j}(x)\right|<\frac{1}{k}\right\}
$$

show that $\mu(S(n, k)) \rightarrow \mu(X)$ as $n \rightarrow \infty$, for each $k$, and hence that there is a suitably increasing sequence $\left\{n_{k}\right\}$ such that $E=\bigcap S\left(n_{k}, k\right)$ has the desired property.

Show that the theorem does not extend to $\sigma$-finite spaces.

Show that the theorem does extend, with essentially the same proof, to the situation in which the sequence $\left\{f_{n}\right\}$ is replaced by a family $\left\{f_{t}\right\}$, where $t$ ranges over the positive reals; the assumptions are now that, for all $x \in X$,

(i) $\lim f_{t}(x)=f(x)$ and

$t \rightarrow \infty$

(ii) $t \rightarrow f_{t}(x)$ is continuous.

17 (a) If $0<p<\infty$, put $\gamma_{p}=\max \left(1,2^{p-1}\right)$, and show that

$$
|\alpha-\beta|^{p} \leq \gamma_{p}\left(|\alpha|^{p}+|\beta|^{p}\right)
$$

for arbitrary complex numbers $\alpha$ and $\beta$.

(b) Suppose $\mu$ is a positive measure on $X, 0<p<\infty, f \in L^{p}(\mu), f_{n} \in L^{p}(\mu), f_{n}(x) \rightarrow f(x)$ a.e., and $\left\|f_{n}\right\|_{p} \rightarrow\|f\|_{p}$ as $n \rightarrow \infty$. Show that then $\lim \left\|f-f_{n}\right\|_{p}=0$, by completing the two proofs that are sketched below.

(i) By Egoroff's theorem, $X=A \cup B$ in such a way that $\int_{A}|f|^{p}<\epsilon, \mu(B)<\infty$, and $f_{n} \rightarrow f$ uniformly on $B$. Fatou's lemma, applied to $\int_{B}\left|f_{n}\right|^{p}$, leads to

$$
\lim \sup \int_{A}\left|f_{n}\right|^{p} d \mu \leq \epsilon
$$

(ii) Put $h_{n}=\gamma_{p}\left(|f|^{p}+\left|f_{n}\right|^{p}\right)-\left|f-f_{n}\right|^{p}$, and use Fatou's lemma as in the proof of Theorem 1.34 .

(c) Show that the conclusion of $(b)$ is false if the hypothesis $\left\|f_{n}\right\|_{p} \rightarrow\|f\|_{p}$ is omitted, even if $\mu(X)<\infty$.

18 Let $\mu$ be a positive measure on $X$. A sequence $\left\{f_{n}\right\}$ of complex measurable functions on $X$ is said to converge in measure to the measurable function $f$ if to every $\epsilon>0$ there corresponds an $N$ such that

$$
\mu\left(\left\{x:\left|f_{n}(x)-f(x)\right|>\epsilon\right\}\right)<\epsilon
$$

for all $n>N$. (This notion is of importance in probability theory.) Assume $\mu(X)<\infty$ and prove the following statements:

(a) If $f_{n}(x) \rightarrow f(x)$ a.e., then $f_{n} \rightarrow f$ in measure.

(b) If $f_{n} \in L^{p}(\mu)$ and $\left\|f_{n}-f\right\|_{p} \rightarrow 0$, then $f_{n} \rightarrow f$ in measure; here $1 \leq p \leq \infty$.

(c) If $f_{n} \rightarrow f$ in measure, then $\left\{f_{n}\right\}$ has a subsequence which converges to $f$ a.e.

Investigate the converses of $(a)$ and $(b)$. What happens to $(a),(b)$, and $(c)$ if $\mu(X)=\infty$, for instance, if $\mu$ is Lebesgue measure on $R^{1}$ ?

19 Define the essential range of a function $f \in L^{\infty}(\mu)$ to be the set $R_{f}$ consisting of all complex numbers $w$ such that

$$
\mu(\{x:|f(x)-w|<\epsilon\})>0
$$

for every $\epsilon>0$. Prove that $R_{f}$ is compact. What relation exists between the set $R_{f}$ and the number $\|f\|_{\infty}$ ?

Let $A_{f}$ be the set of all averages

$$
\frac{1}{\mu(E)} \int_{E} f d \mu
$$

where $E \in \mathfrak{M}$ and $\mu(E)>0$. What relations exist between $A_{f}$ and $R_{f}$ ? Is $A_{f}$ always closed? Are there measures $\mu$ such that $A_{f}$ is convex for every $f \in L^{\infty}(\mu)$ ? Are there measures $\mu$ such that $A_{f}$ fails to be convex for some $f \in L^{\infty}(\mu)$ ?

How are these results affected if $L^{\infty}(\mu)$ is replaced by $L^{1}(\mu)$, for instance?

20 Suppose $\varphi$ is a real function on $R^{1}$ such that

$$
\varphi\left(\int_{0}^{1} f(x) d x\right) \leq \int_{0}^{1} \varphi(f) d x
$$

for every real bounded measurable $f$. Prove that $\varphi$ is then convex.

21 Call a metric space $Y$ a completion of a metric space $X$ if $X$ is dense in $Y$ and $Y$ is complete. In Sec. 3.15 reference was made to "the" completion of a metric space. State and prove a uniqueness theorem which justifies this terminology.

22 Suppose $X$ is a metric space in which every Cauchy sequence has a convergent subsequence. Does it follow that $X$ is complete? (See the proof of Theorem 3.11.)

23 Suppose $\mu$ is a positive measure on $X, \mu(X)<\infty, f \in L^{\infty}(\mu),\|f\|_{\infty}>0$, and

$$
\alpha_{n}=\int_{x}|f|^{n} d \mu \quad(n=1,2,3, \ldots)
$$

Prove that

$$
\lim _{n \rightarrow \infty} \frac{\alpha_{n+1}}{\alpha_{n}}=\|f\|_{\infty}
$$

24 Suppose $\mu$ is a positive measure, $f \in L^{p}(\mu), g \in L^{p}(\mu)$.

(a) If $0<p<1$, prove that

$$
\left.\int|| f\right|^{p}-|g|^{p}\left|d \mu \leq \int\right| f-\left.g\right|^{p} d \mu
$$

that $\Delta(f, g)=\int|f-g|^{p} d \mu$ defines a metric on $L^{p}(\mu)$, and that the resulting metric space is complete.
(b) If $1 \leq p<\infty$ and $\|f\|_{p} \leq R,\|g\|_{p} \leq R$, prove that

$$
\left.\int|| f\right|^{p}-|g|^{p} \mid d \mu \leq 2 p R^{p-1}\|f-g\|_{p}
$$

Hint: Prove first, for $x \geq 0, y \geq 0$, that

$$
\left|x^{p}-y^{p}\right| \leq \begin{cases}|x-y|^{p} & \text { if } 0<p<1 \\ p|x-y|\left(x^{p-1}+y^{p-1}\right) & \text { if } 1 \leq p<\infty\end{cases}
$$

Note that $(a)$ and $(b)$ establish the continuity of the mapping $f \rightarrow|f|^{p}$ that carries $L^{p}(\mu)$ into $L^{1}(\mu)$. 25 Suppose $\mu$ is a positive measure on $X$ and $f: X \rightarrow(0, \infty)$ satisfies $\int_{X} f d \mu=1$. Prove, for every $E \subset X$ with $0<\mu(E)<\infty$, that

$$
\int_{E}(\log f) d \mu \leq \mu(E) \log \frac{1}{\mu(E)}
$$

and, when $0<p<1$,

$$
\int_{E} f^{p} d \mu \leq \mu(E)^{1-p}
$$

26 If $f$ is a positive measurable function on $[0,1]$, which is larger,

$$
\int_{0}^{1} f(x) \log f(x) d x \quad \text { or } \quad \int_{0}^{1} f(s) d s \int_{0}^{1} \log f(t) d t ?
$$

## ELEMENTARY HILBERT SPACE THEORY

## Inner Products and Linear Functionals

4.1 Definition A complex vector space $H$ is called an inner product space (or unitary space) if to each ordered pair of vectors $x$ and $y \in H$ there is associated a complex number $(x, y)$, the so-called "inner product" (or "scalar product") of $x$ and $y$, such that the following rules hold:

(a) $(y, x)=(\overline{x, y)}$. (The bar denotes complex conjugation.)

(b) $(x+y, z)=(x, z)+(y, z)$ if $x, y$, and $z \in H$.

(c) $(\alpha x, y)=\alpha(x, y)$ if $x$ and $y \in H$ and $\alpha$ is a scalar.

(d) $(x, x) \geq 0$ for all $x \in H$.

(e) $(x, x)=0$ only if $x=0$.

Let us list some immediate consequences of these axioms:

(c) implies that $(0, y)=0$ for all $y \in H$.

(b) and (c) may be combined into the statement: For every $y \in H$, the mapping $x \rightarrow(x, y)$ is a linear functional on $H$.

$(a)$ and $(c)$ show that $(x, \alpha y)=\bar{\alpha}(x, y)$.

$(a)$ and $(b)$ imply the second distributive law:

$$
(z, x+y)=(z, x)+(z, y)
$$

By $(d)$, we may define $\|x\|$, the norm of the vector $x \in H$, to be the nonnegative square root of $(x, x)$. Thus

$$
\|x\|^{2}=(x, x) .
$$

4.2 The Schwarz Inequality The properties $4.1(a)$ to $(d)$ imply that

$$
|(x, y)| \leq\|x\|\|y\|
$$

for all $x$ and $y \in H$.

Proof Put $A=\|x\|^{2}, B=|(x, y)|$, and $C=\|y\|^{2}$. There is a complex number $\alpha$ such that $|\alpha|=1$ and $\alpha(y, x)=B$. For any real $r$, we then have

$$
(x-r \alpha y, x-r \alpha y)=(x, x)-r \alpha(y, x)-r \bar{\alpha}(x, y)+r^{2}(y, y) .
$$

The expression on the left is real and not negative. Hence

$$
A-2 B r+C r^{2} \geq 0
$$

for every real $r$. If $C=0$, we must have $B=0$; otherwise (2) is false for large positive $r$. If $C>0$, take $r=B / C$ in (2), and obtain $B^{2} \leq A C$.

4.3 The Triangle Inequality For $x$ and $y \in H$, we have

$$
\|x+y\| \leq\|x\|+\|y\| .
$$

ProOF By the Schwarz inequality,

$$
\begin{aligned}
\|x+y\|^{2} & =(x+y, x+y)=(x, x)+(x, y)+(y, x)+(y, y) \\
& \leq\|x\|^{2}+2\|x\|\|y\|+\|y\|^{2}=(\|x\|+\|y\|)^{2} .
\end{aligned}
$$

4.4 Definition It follows from the triangle inequality that

$$
\|x-z\| \leq\|x-y\|+\|y-z\| \quad(x, y, z \in H) .
$$

If we define the distance between $x$ and $y$ to be $\|x-y\|$, all the axioms for a metric space are satisfied; here, for the first time, we use part $(e)$ of Definition 4.1.

Thus $H$ is now a metric space. If this metric space is complete, i.e., if every Cauchy sequence converges in $H$, then $H$ is called a Hilbert space.

Throughout the rest of this chapter, the letter $H$ will denote a Hilbert space.

### 4.5 Examples

(a) For any fixed $n$, the set $C^{n}$ of all $n$-tuples

$$
x=\left(\xi_{1}, \ldots, \xi_{n}\right)
$$

where $\xi_{1}, \ldots, \xi_{n}$ are complex numbers, is a Hilbert space if addition and scalar multiplication are defined componentwise, as usual, and if

$$
(x, y)=\sum_{j=1}^{n} \xi_{j} \bar{\eta}_{j} \quad\left(y=\left(\eta_{1}, \ldots, \eta_{n}\right)\right)
$$

(b) If $\mu$ is any positive measure, $L^{2}(\mu)$ is a Hilbert space, with inner product

$$
(f, g)=\int_{X} f \bar{g} d \mu
$$

The integrand on the right is in $L^{1}(\mu)$, by Theorem 3.8 , so that $(f, g)$ is well defined. Note that

$$
\|f\|=(f, f)^{1 / 2}=\left\{\int_{X}|f|^{2} d \mu\right\}^{1 / 2}=\|f\|_{2}
$$

The completeness of $L^{2}(\mu)$ (Theorem 3.11) shows that $L^{2}(\mu)$ is indeed a Hilbert space. [We recall that $L^{2}(\mu)$ should be regarded as a space of equivalence classes of functions; compare the discussion in Sec. 3.10.]

For $H=L^{2}(\mu)$, the inequalities 4.2 and 4.3 turn out to be special cases of the inequalities of Hölder and Minkowski.

Note that Example $(a)$ is a special case of $(b)$. What is the measure in $(a)$ ?

(c) The vector space of all continuous compiex functions on $[0,1]$ is an inner product space if

$$
(f, g)=\int_{0}^{1} f(t) \overline{g(t)} d t
$$

but is not a Hilbert space.

4.6 Theorem For any fixed $y \in H$, the mappings

$$
x \rightarrow(x, y), \quad x \rightarrow(y, x), \quad x \rightarrow\|x\|
$$

are continuous functions on $H$.

Proof The Schwarz inequality implies that

$$
\left|\left(x_{1}, y\right)-\left(x_{2}, y\right)\right|=\left|\left(x_{1}-x_{2}, y\right)\right| \leq\left\|x_{1}-x_{2}\right\|\|y\|,
$$

which proves that $x \rightarrow(x, y)$ is, in fact, uniformly continuous, and the same is true for $x \rightarrow(y, x)$. The triangle inequality $\left\|x_{1}\right\| \leq\left\|x_{1}-x_{2}\right\|+\left\|x_{2}\right\|$ yields

$$
\left\|x_{1}\right\|-\left\|x_{2}\right\| \leq\left\|x_{1}-x_{2}\right\|,
$$

and if we interchange $x_{1}$ and $x_{2}$ we see that

$$
\left|\left\|x_{1}\right\|-\left\|x_{2}\right\|\right| \leq\left\|x_{1}-x_{2}\right\|
$$

for all $x_{1}$ and $x_{2} \in H$. Thus $x \rightarrow\|x\|$ is also uniformly continuous.

4.7 Subspaces A subset $M$ of a vector space $V$ is called a subspace of $V$ if $M$ is itself a vector space, relative to the addition and scalar multiplication which are defined in $V$. A necessary and sufficient condition for a set $M \subset V$ to be a subspace is that $x+y \in M$ and $\alpha x \in M$ whenever $x$ and $y \in M$ and $\alpha$ is a scalar.

In the vector space context, the word "subspace" will always have this meaning. Sometimes, for emphasis, we may use the term "linear subspace" in place of subspace.

For example, if $V$ is the vector space of all complex functions on a set $S$, the set of all bounded complex functions on $S$ is a subspace of $V$, but the set of all $f \in V$ with $|f(x)| \leq 1$ for all $x \in S$ is not. The real vector space $R^{3}$ has the following subspaces, and no others: $(a) R^{3},(b)$ all planes through the origin $0,(c)$ all straight lines through 0 , and $(d)\{0\}$.

A closed subspace of $H$ is a subspace that is a closed set relative to the topology induced by the metric of $H$.

Note that if $M$ is a subspace of $H$, so is its closure $\bar{M}$. To see this, pick $x$ and $y$ in $\bar{M}$ and let $\alpha$ be a scalar. There are sequences $\left\{x_{n}\right\}$ and $\left\{y_{n}\right\}$ in $M$ that converge to $x$ and $y$, respectively. It is then easy to verify that $x_{n}+y_{n}$ and $\alpha x_{n}$ converge to $x+y$ and $\alpha x$, respectively. Thus $x+y \in \bar{M}$ and $\alpha x \in \bar{M}$.

4.8 Convex Sets A set $E$ in a vector space $V$ is said to be convex if it has the following geometric property: Whenever $x \in E, y \in E$, and $0<t<1$, the point

$$
z_{t}=(1-t) x+t y
$$

also lies in $E$. As $t$ runs from 0 to 1 , one may visualize $z_{t}$ as describing a straight line segment in $V$, from $x$ to $y$. Convexity requires that $E$ contain the segments between any two of its points.

It is clear that every subspace of $V$ is convex.

Also, if $E$ is convex, so is each of its translates

$$
E+x=\{y+x: y \in E\} .
$$

4.9 Orthogonality If $(x, y)=0$ for some $x$ and $y \in H$, we say that $x$ is orthogonal to $y$, and sometimes write $x \perp y$. Since $(x, y)=0$ implies $(y, x)=0$, the relation $\perp$ is symmetric.

Let $x^{\perp}$ denote the set of all $y \in H$ which are orthogonal to $x$; and if $M$ is a subspace of $H$, let $M^{\perp}$ be the set of all $y \in H$ which are orthogonal to every $x \in M$.

Note that $x^{\perp}$ is a subspace of $H$, since $x \perp y$ and $x \perp y^{\prime}$ implies $x \perp\left(y+y^{\prime}\right)$ and $x \perp \alpha y$. Also, $x^{\perp}$ is precisely the set of points where the continuous function $y \rightarrow(x, y)$ is 0 . Hence $x^{\perp}$ is a closed subspace of $H$. Since

$$
M^{\perp}=\bigcap_{x \in M} x^{\perp}
$$

$M^{\perp}$ is an intersection of closed subspaces, and it follows that $M^{\perp}$ is a closed subspace of $H$.

4.10 Theorem Every nonempty, closed, convex set $E$ in a Hilbert space $H$ contains a unique element of smallest norm.

In other words, there is one and only one $x_{0} \in E$ such that $\left\|x_{0}\right\| \leq\|x\|$ for every $x \in E$.

Proof An easy computation, using only the properties listed in Definition 4.1, establishes the identity

$$
\|x+y\|^{2}+\|x-y\|^{2}=2\|x\|^{2}+2\|y\|^{2} \quad(x \text { and } y \in H)
$$

This is known as the parallelogram law: If we interpret $\|x\|$ to be the length of the vector $x$, (1) says that the sum of the squares of the diagonals of a parallelogram is equal to the sum of the squares of its sides, a familiar proposition in plane geometry.

Let $\delta=\inf \{\|x\|: x \in E\}$. For any $x$ and $y \in E$, we apply (1) to $\frac{1}{2} x$ and $\frac{1}{2} y$ and obtain

$$
\frac{1}{4}\|x-y\|^{2}=\frac{1}{2}\|x\|^{2}+\frac{1}{2}\|y\|^{2}-\left\|\frac{x+y}{2}\right\|^{2}
$$

Since $E$ is convex, $(x+y) / 2 \in E$. Hence

$$
\|x-y\|^{2} \leq 2\|x\|^{2}+2\|y\|^{2}-4 \delta^{2} \quad(x \text { and } y \in E)
$$

If also $\|x\|=\|y\|=\delta$, then (3) implies $x=y$, and we have proved the uniqueness assertion of the theorem.

The definition of $\delta$ shows that there is a sequence $\left\{y_{n}\right\}$ in $E$ so that $\left\|y_{n}\right\| \rightarrow \delta$ as $n \rightarrow \infty$. Replace $x$ and $y$ in (3) by $y_{n}$ and $y_{m}$. Then, as $n \rightarrow \infty$ and $m \rightarrow \infty$, the right side of (3) will tend to 0 . This shows that $\left\{y_{n}\right\}$ is a Cauchy sequence. Since $H$ is complete, there exists an $x_{0} \in H$ so that $y_{n} \rightarrow x_{0}$, i.e., $\left\|y_{n}-x_{0}\right\| \rightarrow 0$, as $n \rightarrow \infty$. Since $y_{n} \in E$ and $E$ is closed, $x_{0} \in E$. Since the norm is a continuous function on $H$ (Theorem 4.6), it follows that

$$
\left\|x_{0}\right\|=\lim _{n \rightarrow \infty}\left\|y_{n}\right\|=\delta
$$

4.11 Theorem Let $M$ be a closed subspace of a Hilbert space $H$.

(a) Every $x \in H$ has then a unique decomposition

$$
x=P x+Q x
$$

into a sum of $P x \in M$ and $Q x \in M^{\perp}$.

(b) $P x$ and $Q x$ are the nearest points to $x$ in $M$ and in $M^{\perp}$, respectively.

(c) The mappings $P: H \rightarrow M$ and $Q: H \rightarrow M^{\perp}$ are linear.

(d) $\|x\|^{2}=\|P x\|^{2}+\|Q x\|^{2}$.

Corollary If $M \neq H$, then there exists $y \in H, y \neq 0$, such that $y \perp M$.

$P$ and $Q$ are called the orthogonal projections of $H$ onto $M$ and $M^{\perp}$.

Proof As regards the uniqueness in $(a)$, suppose that $x^{\prime}+y^{\prime}=x^{\prime \prime}+y^{\prime \prime}$ for some vectors $x^{\prime}, x^{\prime \prime}$ in $M$ and $y^{\prime}, y^{\prime \prime}$ in $M^{\perp}$. Then

$$
x^{\prime}-x^{\prime \prime}=y^{\prime \prime}-y^{\prime}
$$

Since $x^{\prime}-x^{\prime \prime} \in M, y^{\prime \prime}-y^{\prime} \in M^{\perp}$, and $M \cap M^{\perp}=\{0\}$ [an immediate consequence of the fact that $(x, x)=0$ implies $x=0]$, we have $x^{\prime \prime}=x^{\prime}, y^{\prime \prime}=y^{\prime}$.

To prove the existence of the decomposition, note that the set

$$
x+M=\{x+y: y \in M\}
$$

is closed and convex. Define $Q x$ to be the element of smallest norm in $x+M$; this exists, by Theorem 4.10. Define $P x=x-Q x$.

Since $Q x \in x+M$, it is clear that $P x \in M$. Thus $P$ maps $H$ into $M$.

To prove that $Q$ maps $H$ into $M^{\perp}$ we show that $(Q x, y)=0$ for all $y \in M$. Assume $\|y\|=1$, without loss of generality, and put $z=Q x$. The minimizing property of $Q x$ shows that

$$
(z, z)=\|z\|^{2} \leq\|z-\alpha y\|^{2}=(z-\alpha y, z-\alpha y)
$$

for every scalar $\alpha$. This simplifies to

$$
0 \leq-\alpha(y, z)-\bar{\alpha}(z, y)+\alpha \bar{\alpha} .
$$

With $\alpha=(z, y)$, this gives $0 \leq-|(z, y)|^{2}$, so that $(z, y)=0$. Thus $Q x \in M^{\perp}$.

We have already seen that $P x \in M$. If $y \in M$, it follows that

$$
\|x-y\|^{2}=\|Q x+(P x-y)\|^{2}=\|Q x\|^{2}+\|P x-y\|^{2}
$$

which is obviously minimized when $y=P x$.

We have now proved $(a)$ and $(b)$. If we apply $(a)$ to $x$, to $y$, and to $\alpha x+\beta y$, we obtain

$$
P(\alpha x+\beta y)-\alpha P x-\beta P y=\alpha Q x+\beta Q y-Q(\alpha x+\beta y) .
$$

The left side is in $M$, the right side in $M^{\perp}$. Hence both are 0 , so $P$ and $Q$ are linear.

Since $P x \perp Q x,(d)$ follows from (a).

To prove the corollary, take $x \in H, x \notin M$, and put $y=Q x$. Since $P x \in M, x \neq P x$, hence $y=x-P x \neq 0$.

We have already observed that $x \rightarrow(x, y)$ is, for each $y \in H$, a continuous linear functional on $H$. It is a very important fact that all continuous linear functionals on $H$ are of this type.

4.12 Theorem If $L$ is a continuous linear functional on $H$, then there is a unique $y \in H$ such that

$$
L x=(x, y) \quad(x \in H)
$$

ProOF If $L x=0$ for all $x$, take $y=0$. Otherwise, define

$$
M=\{x: L x=0\} .
$$

The linearity of $L$ shows that $M$ is a subspace. The continuity of $L$ shows that $M$ is closed. Since $L x \neq 0$ for some $x \in H$, Theorem 4.11 shows that $M^{\perp}$ does not consist of 0 alone.

Hence there exists $z \in M^{\perp}$, with $\|z\|=1$. Put

$$
u=(L x) z-(L z) x
$$

Since $L u=(L x)(L z)-(L z)(L x)=0$, we have $u \in M$. Thus $(u, z)=0$. This gives

$$
L x=(L x)(z, z)=(L z)(x, z)
$$

Thus (1) holds with $y=\alpha z$, where $\bar{\alpha}=L z$.

The uniqueness of $y$ is easily proved, for if $(x, y)=\left(x, y^{\prime}\right)$ for all $x \in H$, set $z=y-y^{\prime}$; then $(x, z)=0$ for all $x \in H$; in particular, $(z, z)=0$, hence $z=0$.

## Orthonormal Sets

4.13 Definitions If $V$ is a vector space, if $x_{1}, \ldots, x_{k} \in V$, and if $c_{1}, \ldots, c_{k}$ are scalars, then $c_{1} x_{1}+\cdots+c_{k} x_{k}$ is called a linear combination of $x_{1}, \ldots, x_{k}$. The set $\left\{x_{1}, \ldots, x_{k}\right\}$ is called independent if $c_{1} x_{1}+\cdots+c_{k} x_{k}=0$ implies that $c_{1}=\cdots=c_{k}=0$. A set $S \subset V$ is independent if every finite subset of $S$ is independent. The set $[S]$ of all linear combinations of all finite subsets of $S$ (also called the set of all finite linear combinations of members of $S$ ) is clearly a vector space; $[S]$ is the smallest subspace of $V$ which contains $S$; $[S]$ is called the span of $S$, or the space spanned by $S$.

A set of vectors $u_{\alpha}$ in a Hilbert space $H$, where $\alpha$ runs through some index set $A$, is called orthonormal if it satisfies the orthogonality relations $\left(u_{\alpha}, u_{\beta}\right)=0$ for all $\alpha \neq \beta, \alpha \in A$, and $\beta \in A$, and if it is normalized so that $\left\|u_{\alpha}\right\|=1$ for each $\alpha \in A$. In other words, $\left\{u_{\alpha}\right\}$ is orthonormal provided that

$$
\left(u_{\alpha}, u_{\beta}\right)= \begin{cases}1 & \text { if } \alpha=\beta \\ 0 & \text { if } \alpha \neq \beta\end{cases}
$$

If $\left\{u_{\alpha}: \alpha \in A\right\}$ is orthonormal, we associate with each $x \in H$ a complex function $\hat{x}$ on the index set $A$, defined by

$$
\hat{x}(\alpha)=\left(x, u_{\alpha}\right) \quad(\alpha \in A) .
$$

One sometimes calls the numbers $\hat{x}(\alpha)$ the Fourier coefficients of $x$, relative to the set $\left\{u_{\alpha}\right\}$.

We begin with some simple facts about finite orthonormal sets.

4.14 Theorem Suppose that $\left\{u_{\alpha}: \alpha \in A\right\}$ is an orthonormal set in $H$ and that $F$ is a finite subset of $A$. Let $M_{F}$ be the span of $\left\{u_{\alpha}: \alpha \in F\right\}$.

(a) If $\varphi$ is a complex function on $A$ that is 0 outside $F$, then there is a vector $y \in M_{F}$, namely

$$
y=\sum_{\alpha \in F} \varphi(\alpha) u_{\alpha}
$$

that has $\hat{y}(\alpha)=\varphi(\alpha)$ for every $\alpha \in A$. Also,

$$
\|y\|^{2}=\sum_{\alpha \in F}|\varphi(\alpha)|^{2}
$$

(b) If $x \in H$ and

$$
s_{F}(x)=\sum_{\alpha \in F} \hat{x}(\alpha) u_{\alpha}
$$

then

$$
\left\|x-s_{F}(x)\right\|<\|x-s\|
$$

for every $s \in M_{F}$, except for $s=s_{F}(x)$, and

$$
\sum_{\alpha \in F}|\hat{x}(\alpha)|^{2} \leq\|x\|^{2} .
$$

ProOf Part $(a)$ is an immediate consequence of the orthogonality relations 4.13(1).

In the proof of $(b)$, let us write $s_{F}$ in place of $s_{F}(x)$, and note that $\hat{s}_{F}(\alpha)=$ $\hat{x}(\alpha)$ for all $\alpha \in F$. This says that $\left(x-s_{F}\right) \perp u_{\alpha}$ if $\alpha \in F$, hence $\left(x-s_{F}\right) \perp$ $\left(s_{F}-s\right)$ for every $s \in M_{F}$, and therefore

$$
\|x-s\|^{2}=\left\|\left(x-s_{F}\right)+\left(s_{F}-s\right)\right\|^{2}=\left\|x-s_{F}\right\|^{2}+\left\|s_{F}-s\right\|^{2}
$$

This gives (4). With $s=0$, (6) gives $\left\|s_{F}\right\|^{2} \leq\|x\|^{2}$, which is the same as (5), because of (2).

The inequality (4) states that the "partial sum" $s_{F}(x)$ of the "Fourier series" $\sum \hat{x}(\alpha) u_{\alpha}$ of $x$ is the unique best approximation to $x$ in $M_{F}$, relative to the metric defined by the Hilbert space norm.

4.15 We want to drop the finiteness condition that appears in Theorem 4.14 (thus obtaining Theorems 4.17 and 4.18) without even restricting ourselves to sets that are necessarily countable. For this reason it seems advisable to clarify the meaning of the symbol $\sum_{\alpha \in \mathcal{A}} \varphi(\alpha)$ when $\alpha$ ranges over an arbitrary set $A$.

Assume $0 \leq \varphi(\alpha) \leq \infty$ for each $\alpha \in A$. Then

$$
\sum_{\alpha \in A} \varphi(\alpha)
$$

denotes the supremum of the set of all finite sums $\varphi\left(\alpha_{1}\right)+\cdots+\varphi\left(\alpha_{n}\right)$, where $\alpha_{1}, \ldots, \alpha_{n}$ are distinct members of $A$.

A moment's consideration will show that the sum (1) is thus precisely the Lebesgue integral of $\varphi$ relative to the counting measure $\mu$ on $A$.

In this context one usually writes $\ell^{p}(A)$ for $L^{p}(\mu)$. A complex function $\varphi$ with domain $A$ is thus in $\ell^{2}(A)$ if and only if

$$
\sum_{\alpha \in A}|\varphi(\alpha)|^{2}<\infty
$$

Example $4.5(b)$ shows that $\ell^{2}(A)$ is a Hilbert space, with inner product

$$
(\varphi, \psi)=\sum_{\alpha \in A} \varphi(\alpha) \overline{\psi(\alpha)}
$$

Here, again, the sum over $A$ stands for the integral of $\varphi \bar{\psi}$ with respect to the counting measure; note that $\varphi \bar{\psi} \in \ell^{1}(A)$ because $\varphi$ and $\psi$ are in $\ell^{2}(A)$.

Theorem 3.13 shows that the functions $\varphi$ that are zero except on some finite subset of $A$ are dense in $\ell^{2}(A)$.

Moreover, if $\varphi \in \ell^{2}(A)$, then $\{\alpha \in A: \varphi(\alpha) \neq 0\}$ is at most countable. For if $A_{n}$ is the set of all $\alpha$ where $|\varphi(\alpha)|>1 / n$, then the number of elements of $A$ is at most

$$
\sum_{\alpha \in A_{n}}|n \varphi(\alpha)|^{2} \leq n^{2} \sum_{\alpha \in A}|\varphi(\alpha)|^{2}
$$

Each $A_{n}(n=1,2,3, \ldots)$ is thus a finite set.

The following lemma about complete metric spaces will make it easy to pass from finite orthonormal sets to infinite ones.

### 4.16 Lemma Suppose that

(a) $X$ and $Y$ are metric spaces, $X$ is complete,

(b) $f: X \rightarrow Y$ is continuous,

(c) $X$ has a dense subset $X_{0}$ on which $f$ is an isometry, and

(d) $f\left(X_{0}\right)$ is dense in $Y$.

Then $f$ is an isometry of $X$ onto $Y$.

The most important part of the conclusion is that $f$ maps $X$ onto all of $Y$.

Recall that an isometry is simply a mapping that preserves distances. Thus, by assumption, the distance between $f\left(x_{1}\right)$ and $f\left(x_{2}\right)$ in $Y$ is equal to that between $x_{1}$ and $x_{2}$ in $X$, for all points $x_{1}, x_{2}$ in $X_{0}$.

Proof The fact that $f$ is an isometry on $X$ is an immediate consequence of the continuity of $f$, since $X_{0}$ is dense in $X$.

Pick $y \in Y$. Since $f\left(X_{0}\right)$ is dense in $Y$, there is a sequence $\left\{x_{n}\right\}$ in $X_{0}$ such that $f\left(x_{n}\right) \rightarrow y$ as $n \rightarrow \infty$. Thus $\left\{f\left(x_{n}\right)\right\}$ is a Cauchy sequence in $Y$. Since $f$ is an isometry on $X_{0}$, it follows that $\left\{x_{n}\right\}$ is also a Cauchy sequence. The completeness of $X$ implies now that $\left\{x_{n}\right\}$ converges to some $x \in X$, and the continuity of $f$ shows that $f(x)=\lim f\left(x_{n}\right)=y$.

4.17 Theorem Let $\left\{u_{\alpha}: \alpha \in A\right\}$ be an orthonormal set in $H$, and let $P$ be the space of all finite linear combinations of the vectors $u_{\alpha}$.

The inequality

$$
\sum_{\alpha \in A}|\hat{x}(\alpha)|^{2} \leq\|x\|^{2}
$$

holds then for every $x \in H$, and $x \rightarrow \hat{x}$ is a continuous linear mapping of $H$ onto $\ell^{2}(A)$ whose restriction to the closure $\bar{P}$ of $P$ is an isometry of $\bar{P}$ onto $\ell^{2}(A)$.

Proof Since the inequality 4.14(5) holds for every finite set $F \subset A$, we have (1), the so-called Bessel inequality.

Define $f$ on $H$ by $f(x)=\hat{x}$. Then (1) shows explicitly that $f$ maps $H$ into $\ell^{2}(A)$. The linearity of $f$ is obvious. If we apply (1) to $x-y$ we see that

$$
\|f(y)-f(x)\|_{2}=\|\hat{y}-\hat{x}\|_{2} \leq\|y-x\| .
$$

Thus $f$ is continuous. Theorem 4.14(a) shows that $f$ is an isometry of $P$ onto the dense subspace of $\ell^{2}(A)$ consisting of those functions whose support is a finite set $F \subset A$. The theorem follows therefore from Lemma 4.16, applied with $X=\bar{P}, X_{0}=P, Y=\ell^{2}(A)$; note that $\bar{P}$, being a closed subset of the complete metric space $H$, is itself complete.

The fact that the mapping $x \rightarrow \hat{x}$ carries $H$ onto $\ell^{2}(A)$ is known as the RieszFischer theorem.

4.18 Theorem Let $\left\{u_{\alpha}: \alpha \in A\right\}$ be an orthonormal set in $H$. Each of the following four conditions on $\left\{u_{\alpha}\right\}$ implies the other three:

(i) $\left\{u_{\alpha}\right\}$ is a maximal orthonormal set in $H$.

(ii) The set $P$ of all finite linear combinations of members of $\left\{u_{\alpha}\right\}$ is dense in $H$.

(iii) The equality

$$
\sum_{\alpha \in A}|\hat{x}(\alpha)|^{2}=\|x\|^{2}
$$

holds for every $x \in H$.

(iv) The equality

$$
\sum_{\alpha \in A} \hat{x}(\alpha) \overline{\hat{y}(\alpha)}=(x, y)
$$

holds for all $x \in H$ and $y \in H$.

The last formula is known as Parseval's identity. Observe that $\hat{x}$ and $\hat{y}$ are in $\ell^{2}(A)$, hence $\hat{x} \bar{y}$ is in $\ell^{1}(A)$, so that the sum in (iv) is well defined. Of course, (iii) is the special case $x=y$ of (iv).

Maximal orthonormal sets are often called complete orthonormal sets or orthonormal bases.

ProOF To say that $\left\{u_{\alpha}\right\}$ is maximal means simply that no vector of $H$ can be adjoined to $\left\{u_{\alpha}\right\}$ in such a way that the resulting set is still orthonormal. This happens precisely when there is no $x \neq 0$ in $H$ that is orthogonal to every $u_{\alpha}$.

We shall prove that (i) $\rightarrow$ (ii) $\rightarrow$ (iii) $\rightarrow$ (iv) $\rightarrow$ (i).

If $P$ is not dense in $H$, then its closure $\bar{P}$ is not all of $H$, and the corollary to Theorem 4.11 implies that $P^{\perp}$ contains a nonzero vector. Thus $\left\{u_{\alpha}\right\}$ is not maximal when $P$ is not dense, and (i) implies (ii).

If (ii) holds, so does (iii), by Theorem 4.17.

The implication (iii) $\rightarrow$ (iv) follows from the easily proved Hilbert space identity (sometimes called the "polarization identity")

$$
4(x, y)=\|x+y\|^{2}-\|x-y\|^{2}+i\|x+i y\|^{2}-i\|x-i y\|^{2}
$$

which expresses the inner product $(x, y)$ in terms of norms and which is equally valid with $\hat{x}, \hat{y}$ in place of $x, y$, simply because $\ell^{2}(A)$ is also a Hilbert space. (See Exercise 19 for other identities of this type.) Note that the sums in (iii) and (iv) are $\|\hat{x}\|_{2}^{2}$ and $(\hat{x}, \hat{y})$, respectively.

Finally, if (i) is false, there exists $u \neq 0$ in $H$ so that $\left(u, u_{\alpha}\right)=0$ for all $\alpha \in A$. If $x=y=u$, then $(x, y)=\|u\|^{2}>0$ but $\hat{x}(\alpha)=0$ for all $\alpha \in A$, hence (iv) fails. Thus (iv) implies (i), and the proof is complete.

4.19 Isomorphisms Speaking informally, two algebraic systems of the same nature are said to be isomorphic if there is a one-to-one mapping of one onto the other which preserves all relevant properties. For instance, we may ask whether two groups are isomorphic or whether two fields are isomorphic. Two vector spaces are isomorphic if there is a one-to-one linear mapping of one onto the other. The linear mappings are the ones which preserve the relevant concepts in a vector space, namely, addition and scalar multiplication.

In the same way, two Hilbert spaces $H_{1}$ and $H_{2}$ are isomorphic if there is a one-to-one linear mapping $\Lambda$ of $H_{1}$ onto $H_{2}$ which also preserves inner products: $(\Lambda x, \Lambda y)=(x, y)$ for all $x$ and $y \in H_{1}$. Such a $\Lambda$ is an isomorphism (or, more specifically, a Hilbert space isomorphism) of $H_{1}$ onto $H_{2}$. Using this terminology, Theorems 4.17 and 4.18 yield the following statement:

If $\left\{u_{\alpha}: \alpha \in A\right\}$ is a maximal orthonormal set in a Hilbert space $H$, and if $\hat{x}(\alpha)=$ $\left(x, u_{\alpha}\right)$, then the mapping $x \rightarrow \hat{x}$ is a Hilbert space isomorphism of $H$ onto $\ell^{2}(A)$.

One can prove (we shall omit this) that $\ell^{2}(A)$ and $\ell^{2}(B)$ are isomorphic if and only if the sets $A$ and $B$ have the same cardinal number. But we shall prove that every nontrivial Hilbert space (this means that the space does not consist of 0 alone) is isomorphic to some $\ell^{2}(A)$, by proving that every such space contains a maximal orthonormal set (Theorem 4.22). The proof will depend on a property of partially ordered sets which is equivalent to the axiom of choice.

4.20 Partially Ordered Sets A set $\mathscr{P}$ is said to be partially ordered by a binary relation $\leq$ if
(a) $a \leq b$ and $b \leq c$ implies $a \leq c$.

(b) $a \leq a$ for every $\alpha \in \mathscr{P}$.

(c) $a \leq b$ and $b \leq a$ implies $a=b$.

A subset $\mathscr{2}$ of a partially ordered set $\mathscr{P}$ is said to be totally ordered (or linearly ordered) if every pair $a, b \in 2$ satisfies either $\alpha \leq b$ or $b \leq a$.

For example, every collection of subsets of a given set is partially ordered by the inclusion relation $\subset$.

To give a more specific example, let $\mathscr{P}$ be the collection of all open subsets of the plane, partially ordered by set inclusion, and let 2 be the collection of all open circular discs with center at the origin. Then $\mathscr{Q} \subset \mathscr{P}, \mathscr{Q}$ is totally ordered by $\subset$, and 2 is a maximal totally ordered subset of $\mathscr{P}$. This means that if any member of $\mathscr{P}$ not in $\mathscr{2}$ is adjoined to 2 , the resulting collection of sets is no longer totally ordered by $\subset$.

4.21 The Hausdorff Maximality Theorem Every nonempty partially ordered set contains a maximal totally ordered subset.

This is a consequence of the axiom of choice and is, in fact, equivalent to it; another (very similar) form of it is known as Zorn's lemma. We give the proof in the Appendix.

If now $H$ is a nontrivial Hilbert space, then there exists a $u \in H$ with $\|u\|=1$, so that there is a nonempty orthonormal set in $H$. The existence of a maximal orthonormal set is therefore a consequence of the following theorem:

4.22 Theorem Every orthonormal set $B$ in a Hilbert space $H$ is contained in a maximal orthonormal set in $H$.

ProOF Let $\mathscr{P}$ be the class of all orthonormal sets in $H$ which contain the given set $B$. Partially order $\mathscr{P}$ by set inclusion. Since $B \in \mathscr{P}, \mathscr{P} \neq \varnothing$. Hence $\mathscr{P}$ contains a maximal totally ordered class $\Omega$. Let $S$ be the union of all members of $\Omega$. It is clear that $B \subset S$. We claim that $S$ is a maximal orthonormal set:

If $u_{1}$ and $u_{2} \in S$, then $u_{1} \in A_{1}$ and $u_{2} \in A_{2}$ for some $A_{1}$ and $A_{2} \in \Omega$. Since $\Omega$ is total ordered, $A_{1} \subset A_{2}$ (or $A_{2} \subset A_{1}$ ), so that $u_{1} \in A_{2}$ and $u_{2} \in A_{2}$. Since $A_{2}$ is orthonormal, $\left(u_{1}, u_{2}\right)=0$ if $u_{1} \neq u_{2},\left(u_{1}, u_{2}\right)=1$ if $u_{1}=u_{2}$. Thus $S$ is an orthonormal set.

Suppose $S$ is not maximal. Then $S$ is a proper subset of an orthonormal set $S^{*}$. Clearly, $S^{*} \notin \Omega$, and $S^{*}$ contains every member of $\Omega$. Hence we may adjoin $S^{*}$ to $\Omega$ and still have a total order. This contradicts the maximality of $\Omega$.

## Trigonometric Series

4.23 Definitions Let $T$ be the unit circle in the complex plane, i.e., the set of all complex numbers of absolute value 1 . If $F$ is any function on $T$ and if $f$ is defined on $R^{1}$ by

$$
f(t)=F\left(e^{i t}\right)
$$

then $f$ is a periodic function of period $2 \pi$. This means that $f(t+2 \pi)=f(t)$ for all real $t$. Conversely, if $f$ is a function on $R^{1}$, with period $2 \pi$, then there is a function $F$ on $T$ such that (1) holds. Thus we may identify functions on $T$ with $2 \pi$-periodic functions on $R^{1}$; and, for simplicity of notation, we shall sometimes write $f(t)$ rather than $f\left(e^{i t}\right)$, even if we think of $f$ as being defined on $T$.

With these conventions in mind, we define $L^{p}(T)$, for $1 \leq p<\infty$, to be the class of all complex, Lebesgue measurable, $2 \pi$-periodic functions on $R^{1}$ for which the norm

$$
\|f\|_{p}=\left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi}|f(t)|^{p} d t\right\}^{1 / p}
$$

is finite.

In other words, we are looking at $L^{p}(\mu)$, where $\mu$ is Lebesgue measure on $[0,2 \pi]$ (or on $T$ ), divided by $2 \pi$. $L^{\infty}(T)$ will be the class of all $2 \pi$-periodic members of $L^{\infty}\left(R^{1}\right)$, with the essential supremum norm, and $C(T)$ consists of all continuous complex functions on $T$ (or, equivalently, of all continuous, complex, $2 \pi$-periodic functions on $R^{1}$ ), with norm

$$
\|f\|_{\infty}=\sup |f(t)|,
$$

The factor $1 /(2 \pi)$ in (2) simplifies the formalism we are about to develop. For instance, the $L^{p}$-norm of the constant function 1 is 1.

A trigonometric polynomial is a finite sum of the form

$$
f(t)=a_{0}+\sum_{n=1}^{N}\left(a_{n} \cos n t+b_{n} \sin n t\right) \quad\left(t \in R^{1}\right)
$$

where $a_{0}, a_{1}, \ldots, a_{N}$ and $b_{1}, \ldots, b_{N}$ are complex numbers. On account of the Euler identities, (4) can also be written in the form

$$
f(t)=\sum_{n=-N}^{N} c_{n} e^{i n t}
$$

which is more convenient for most purposes. It is clear that every trigonometric polynomial has period $2 \pi$.

We shall denote the set of all integers (positive, zero, and negative) by $Z$, and put

$$
u_{n}(t)=e^{i n t} \quad(n \in Z)
$$

If we define the inner product in $L^{2}(T)$ by

$$
(f, g)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) \overline{g(t)} d t
$$

[note that this is in agreement with (2)], an easy computation shows that

$$
\left(u_{n}, u_{m}\right)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{i(n-m) t} d t= \begin{cases}1 & \text { if } n=m \\ 0 & \text { if } n \neq m\end{cases}
$$

Thus $\left\{u_{n}: n \in Z\right\}$ is an orthonormal set in $L^{2}(T)$, usually called the trigonometric system. We shall now prove that this system is maximal, and shall then derive concrete versions of the abstract theorems previously obtained in the Hilbert space context.

4.24 The Completeness of the Trigonometric System Theorem 4.18 shows that the maximality (or completeness) of the trigonometric system will be proved as soon as we can show that the set of all trigonometric polynomials is dense in $L^{2}(T)$. Since $C(T)$ is dense in $L^{2}(T)$, by Theorem 3.14 (note that $T$ is compact), it suffices to show that to every $f \in C(T)$ and to every $\epsilon>0$ there is a trigonometric polynomial $P$ such that $\|f-P\|_{2}<\epsilon$. Since $\|g\|_{2} \leq\|g\|_{\infty}$ for every $g \in C(T)$, the estimate $\|f-P\|_{2}<\epsilon$ will follow from $\|f-P\|_{\infty}<\epsilon$, and it is this estimate which we shall prove.

Suppose we had trigonometric polynomials $Q_{1}, Q_{2}, Q_{3}, \ldots$, with the following properties:

$$
Q_{k}(t) \geq 0 \text { for } t \in R^{1} \text {. }
$$

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} Q_{k}(t) d t=1
$$

(c) If $\eta_{k}(\delta)=\sup \left\{Q_{k}(t): \delta \leq|t| \leq \pi\right\}$, then

$$
\lim _{k \rightarrow \infty} \eta_{k}(\delta)=0
$$

for every $\delta>0$.

Another way of stating $(c)$ is to say: for every $\delta>0, Q_{k}(t) \rightarrow 0$ uniformly on $[-\pi,-\delta] \cup[\delta, \pi]$.

To each $f \in C(T)$ we associate the functions $P_{k}$ defined by

$$
P_{k}(t)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t-s) Q_{k}(s) d s \quad(k=1,2,3, \ldots)
$$

If we replace $s$ by $-s$ (using Theorem 2.20(e)) and then by $s-t$, the periodicity of $f$ and $Q_{k}$ shows that the value of the integral is not affected. Hence

$$
P_{k}(t)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(s) Q_{k}(t-s) d s \quad(k=1,2,3, \ldots)
$$

Since each $Q_{k}$ is a trigonometric polynomial, $Q_{k}$ is of the form

$$
Q_{k}(t)=\sum_{n=-N_{k}}^{N_{k}} a_{n, k} e^{i n t}
$$

and if we replace $t$ by $t-s$ in (3) and substitute the result in (2), we see that each $\boldsymbol{P}_{\boldsymbol{k}}$ is a trigonometric polynomial.

Let $\epsilon>0$ be given. Since $f$ is uniformly continuous on $T$, there exists a $\delta>0$ such that $|f(t)-f(s)|<\epsilon$ whenever $|t-s|<\delta$. By $(b)$, we have

$$
P_{k}(t)-f(t)=\frac{1}{2 \pi} \int_{-\pi}^{\pi}\{f(t-s)-f(t)\} Q_{k}(s) d s,
$$

and (a) implies, for all $t$, that

$$
\left|P_{k}(t)-f(t)\right| \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi}|f(t-s)-f(t)| Q_{k}(s) d s=A_{1}+A_{2}
$$

where $A_{1}$ is the integral over $[-\delta, \delta]$ and $A_{2}$ is the integral over $[-\pi,-\delta] \cup$ $[\delta, \pi]$. In $A_{1}$, the integrand is less than $\epsilon Q_{k}(s)$, so $A_{1}<\epsilon$, by $(b)$. In $A_{2}$, we have $Q_{k}(s) \leq \eta_{k}(\delta)$, hence

$$
A_{2} \leq 2\|f\|_{\infty} \cdot \eta_{k}(\delta)<\epsilon
$$

for sufficiently large $k$, by $(c)$. Since these estimates are independent of $t$, we have proved that

$$
\lim _{k \rightarrow \infty}\left\|f-P_{k}\right\|_{\infty}=0
$$

It remains to construct the $Q_{k}$. This can be done in many ways. Here is a simple one. Put

$$
Q_{k}(t)=c_{k}\left\{\frac{1+\cos t}{2}\right\}^{k}
$$

where $c_{k}$ is chosen so that $(b)$ holds. Since $(a)$ is clear, we only need to show $(c)$. Since $Q_{k}$ is even, $(b)$ shows that

$$
1=\frac{c_{k}}{\pi} \int_{0}^{\pi}\left\{\frac{1+\cos t}{2}\right\}^{k} d t>\frac{c_{k}}{\pi} \int_{0}^{\pi}\left\{\frac{1+\cos t}{2}\right\}^{k} \sin t d t=\frac{2 c_{k}}{\pi(k+1)} .
$$

Since $Q_{k}$ is decreasing on $[0, \pi]$, it follows that

$$
Q_{k}(t) \leq Q_{k}(\delta) \leq \frac{\pi(k+1)}{2}\left(\frac{1+\cos \delta}{2}\right)^{k} \quad(0<\delta \leq|t| \leq \pi)
$$

This implies $(c)$, since $1+\cos \delta<2$ if $0<\delta \leq \pi$.

We have proved the following important result:

4.25 Theorem If $f \in C(T)$ and $\epsilon>0$, there is a trigonometric polynomial $P$ such that

$$
|f(t)-P(t)|<\epsilon
$$

for every real $t$.

A more precise result was proved by Fejér (1904): The arithmetic means of the partial sums of the Fourier series of any $f \in C(T)$ converge uniformly to $f$. For a proof (quite similar to the above) see Theorem 3.1 of [45], or p. 89 of [36], vol. I.

4.26 Fourier Series For any $f \in L^{1}(T)$, we define the Fourier coefficients of $f$ by the formula

$$
\hat{f}(n)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) e^{-i n t} d t \quad(n \in Z)
$$

where, we recall, $Z$ is the set of all integers. We thus associate with each $f \in L^{1}(T)$ a function $\hat{f}$ on $Z$. The Fourier series of $f$ is

$$
\sum_{-\infty}^{\infty} \hat{f}(n) e^{i n t}
$$

and its partial sums are

$$
s_{N}(t)=\sum_{-N}^{N} \hat{f}(n) e^{i n t} \quad(N=0,1,2, \ldots)
$$

Since $L^{2}(T) \subset L^{1}(T)$, (1) can be applied to every $f \in L^{2}(T)$. Comparing the definitions made in Secs. 4.23 and 4.13, we can now restate Theorems 4.17 and 4.18 in concrete terms:

The Riesz-Fischer theorem asserts that if $\left\{c_{n}\right\}$ is a sequence of complex numbers such that

$$
\sum_{n=-\infty}^{\infty}\left|c_{n}\right|^{2}<\infty
$$

then there exists an $f \in L^{2}(T)$ such that

$$
c_{n}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) e^{-i n t} d t \quad(n \in Z)
$$

The Parseval theorem asserts that

$$
\sum_{n=-\infty}^{\infty} \hat{f}(n) \overline{\hat{g}(n)}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) \overline{g(t)} d t
$$

whenever $f \in L^{2}(T)$ and $g \in L^{2}(T)$; the series on the left of (6) converges absolutely; and if $s_{N}$ is as in (3), then

$$
\lim _{N \rightarrow \infty}\left\|f-s_{N}\right\|_{2}=0
$$

since a special case of (6) yields

$$
\left\|f-s_{N}\right\|_{2}^{2}=\sum_{|n|>N}|\hat{f}(n)|^{2}
$$

Note that (7) says that every $f \in L^{2}(T)$ is the $L^{2}$-limit of the partial sums of its Fourier series; i.e., the Fourier series of $f$ converges to $f$, in the $L^{2}$-sense. Pointwise convergence presents a more delicate problem, as we shall see in Chap. 5.

The Riesz-Fischer theorem and the Parseval theorem may be summarized by saying that the mapping $f \leftrightarrow \hat{f}$ is a Hilbert space isomorphism of $L^{2}(T)$ onto $\ell^{2}(Z)$.

The theory of Fourier series in other function spaces, for instance in $L^{1}(T)$, is much more difficult than in $L^{2}(T)$, and we shall touch only a few aspects of it.

Observe that the crucial ingredient in the proof of the Riesz-Fischer theorem is the fact that $L^{2}$ is complete. This is so well recognized that the name "RieszFischer theorem" is sometimes given to the theorem which asserts the completeness of $L^{2}$, or even of any $L^{p}$.

## Exercises

In this set of exercises, $H$ always denotes a Hilbert space.

1 If $M$ is a closed subspace of $H$, prove that $M=\left(M^{\perp}\right)^{\perp}$. Is there a similar true statement for subspaces $M$ which are not necessarily closed?

2 Let $\left\{x_{n}: n=1,2,3, \ldots\right\}$ be a linearly independent set of vectors in $H$. Show that the following construction yields an orthonormal set $\left\{u_{n}\right\}$ such that $\left\{x_{1}, \ldots, x_{N}\right\}$ and $\left\{u_{1}, \ldots, u_{N}\right\}$ have the same span for all $N$.

Put $u_{1}=x_{1} /\left\|x_{1}\right\|$. Having $u_{1}, \ldots, u_{n-1}$ define

$$
v_{n}=x_{n}-\sum_{i=1}^{n-1}\left(x_{n}, u_{i}\right) u_{i}, \quad u_{n}=v_{n} /\left\|v_{n}\right\|
$$

Note that this leads to a proof of the existence of a maximal orthonormal set in separable Hilbert spaces which makes no appeal to the Hausdorff maximality principle. (A space is separable if it contains a countable dense subset.)

3 Show that $L^{p}(T)$ is separable if $1 \leq p<\infty$, but that $L^{\infty}(T)$ is not separable.

4 Show that $H$ is separable if and only if $H$ contains a maximal orthonormal system which is at most countable.

5 If $M=\{x: L x=0\}$, where $L$ is a continuous linear functional on $H$, prove that $M^{\perp}$ is a vector space of dimension 1 (unless $M=H$ ).

6 Let $\left\{u_{n}\right\}(n=1,2,3, \ldots)$ be an orthonormal set in $H$. Show that this gives an example of a closed and bounded set which is not compact. Let $Q$ be the set of all $x \in H$ of the form

$$
x=\sum_{1}^{\infty} c_{n} u_{n} \quad\left(\text { where }\left|c_{n}\right| \leq \frac{1}{n}\right)
$$

Prove that $Q$ is compact. ( $Q$ is called the Hilbert cube.)
the form

More generally, let $\left\{\delta_{n}\right\}$ be a sequence of positive numbers, and let $S$ be the set of all $x \in H$ of

$$
x=\sum_{1}^{\infty} c_{n} u_{n} \quad\left(\text { where }\left|c_{n}\right| \leq \delta_{n}\right)
$$

Prove that $S$ is compact if and only if $\sum_{1}^{\infty} \delta_{n}^{2}<\infty$.

Prove that $H$ is not locally compact.

7 Suppose $\left\{a_{n}\right\}$ is a sequence of positive numbers such that $\sum a_{n} b_{n}<\infty$ whenever $b_{n} \geq 0$ and $\sum b_{n}^{2}<\infty$. Prove that $\sum a_{n}^{2}<\infty$.

Suggestion: If $\sum a_{n}^{2}=\infty$ then there are disjoint sets $E_{k}(k=1,2,3, \ldots)$ so that

$$
\sum_{n \in E_{k}} a_{n}^{2}>1
$$

Define $b_{n}$ so that $b_{n}=c_{k} a_{n}$ for $n \in E_{k}$. For suitably chosen $c_{k}, \sum a_{n} b_{n}=\infty$ although $\sum b_{n}^{2}<\infty$.

8 If $H_{1}$ and $H_{2}$ are two Hilbert spaces, prove that one of them is isomorphic to a subspace of the other. (Note that every closed subspace of a Hilbert space is a Hilbert space.)

9 If $A \subset[0,2 \pi]$ and $A$ is measurable, prove that

$$
\lim _{n \rightarrow \infty} \int_{A} \cos n x d x=\lim _{n \rightarrow \infty} \int_{A} \sin n x d x=0
$$

10 Let $n_{1}<n_{2}<n_{3}<\cdots$ be positive integers, and let $E$ be the set of all $x \in[0,2 \pi]$ at which $\left\{\sin n_{k} x\right\}$ converges. Prove that $m(E)=0$. Hint: $2 \sin ^{2} \alpha=1-\cos 2 \alpha$, so $\sin n_{k} x \rightarrow \pm 1 / \sqrt{2}$ a.e. on $E$, by Exercise 9 .

11 Find a nonempty closed set $E$ in $L^{2}(T)$ that contains no element of smallest norm.

12 The constants $c_{k}$ in Sec. 4.24 were shown to be such that $k^{-1} c_{k}$ is bounded. Estimate the relevant integral more precisely and show that

$$
0<\lim _{k \rightarrow \infty} k^{-1 / 2} c_{k}<\infty
$$

13 Suppose $f$ is a continuous function on $R^{1}$, with period 1 . Prove that

$$
\lim _{N \rightarrow \infty} \frac{1}{N} \sum_{n=1}^{N} f(n \alpha)=\int_{0}^{1} f(t) d t
$$

for every irrational real number $\alpha$. Hint : Do it first for

$$
f(t)=\exp (2 \pi i k t), \quad k=0, \pm 1, \pm 2, \ldots
$$

14 Compute

$$
\min _{a, b, c} \int_{-1}^{1}\left|x^{3}-a-b x-c x^{2}\right|^{2} d x
$$

and find

$$
\max \int_{-1}^{1} x^{3} g(x) d x
$$

where $g$ is subject to the restrictions

$$
\int_{-1}^{1} g(x) d x=\int_{-1}^{1} x g(x) d x=\int_{-1}^{1} x^{2} g(x) d x=0 ; \quad \int_{-1}^{1}|g(x)|^{2} d x=1 .
$$

15 Compute

$$
\min _{a, b, c} \int_{0}^{\infty}\left|x^{3}-a-b x-c x^{2}\right|^{2} e^{-x} d x
$$

State and solve the corresponding maximum problem, as in Exercise 14.

16 If $x_{0} \in H$ and $M$ is a closed linear subspace of $H$, prove that

$$
\min \left\{\left\|x-x_{0}\right\|: x \in M\right\}=\max \left\{\left|\left(x_{0}, y\right)\right|: y \in M^{\perp},\|y\|=1\right\}
$$

17 Show that there is a continuous one-to-one mapping $\gamma$ of $[0,1]$ into $H$ such that $\gamma(b)-\gamma(a)$ is orthogonal to $\gamma(d)-\gamma(c)$ whenever $0 \leq a \leq b \leq c \leq d \leq 1$. ( $\gamma$ may be called a "curve with orthogonal increments.") $H$ int : Take $H=L^{2}$, and consider characteristic functions of certain subsets of $[0,1]$.

18 Define $u_{s}(t)=e^{i s t}$ for all $s \in R^{1}, t \in R^{1}$. Let $X$ be the complex vector space consisting of all finite linear combinations of these functions $u_{s}$. If $f \in X$ and $g \in X$, show that

$$
(f, g)=\lim _{A \rightarrow \infty} \frac{1}{2 A} \int_{-A}^{A} f(t) \overline{g(t)} d t
$$

exists. Show that this inner product makes $X$ into a unitary space whose completion is a nonseparable Hilbert space $H$. Show also that $\left\{u_{s}: s \in R^{1}\right\}$ is a maximal orthonormal set in $H$. 19 Fix a positive integer $N$, put $\omega=e^{2 \pi i / N}$, prove the orthogonality relations

$$
\frac{1}{N} \sum_{n=1}^{N} \omega^{n k}=\left\{\begin{array}{lll}
1 & \text { if } \quad k=0 \\
0 & \text { if } \quad 1 \leq k \leq N-1
\end{array}\right.
$$

and use them to derive the identities

$$
(x, y)=\frac{1}{N} \sum_{n=1}^{N}\left\|x+\omega^{n} y\right\|^{2} \omega^{n}
$$

that hold in every inner product space if $N \geq 3$. Show also that

$$
(x, y)=\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left\|x+e^{i \theta} y\right\|^{2} e^{i \theta} d \theta .
$$

## EXAMPLES OF BANACH SPACE TECHNIQUES

## Banach Spaces

5.1 In the preceding chapter we saw how certain analytic facts about trigonometric series can be made to emerge from essentially goemetric considerations about general Hilbert spaces, involving the notions of convexity, subspaces, orthogonality, and completeness. There are many problems in analysis that can be attacked with greater ease when they are placed within a suitably chosen abstract framework. The theory of Hilbert spaces is not always suitable since orthogonality is something rather special. The class of all Banach spaces affords greater variety. In this chapter we shall develop some of the basic properties of Banach spaces and illustrate them by applications to concrete problems.

5.2 Definition A complex vector space $X$ is said to be a normed linear space if to each $x \in X$ there is associated a nonnegative real number $\|x\|$, called the norm of $x$, such that

(a) $\|x+y\| \leq\|x\|+\|y\|$ for all $x$ and $y \in X$,

(b) $\|a x\|=|\alpha|\|x\|$ if $x \in X$ and $\alpha$ is a scalar,

(c) $\|x\|=0$ implies $x=0$.

By $(a)$, the triangle inequality

$$
\|x-y\| \leq\|x-z\|+\|z-y\| \quad(x, y, z \in X)
$$

holds. Combined with $(b)$ (take $\alpha=0, \alpha=-1$ ) and (c) this shows that every normed linear space may be regarded as a metric space, the distance between $x$ and $y$ being $\|x-y\|$.

A Banach space is a normed linear space which is complete in the metric defined by its norm.

For instance, every Hilbert space is a Banach space, so is every $L^{p}(\mu)$ normed by $\|f\|_{p}$ (provided we identify functions which are equal a.e.) if $1 \leq p \leq \infty$, and so is $C_{0}(X)$ with the supremum norm. The simplest Banach space is of course the complex field itself, normed by $\|x\|=|x|$.

One can equally well discuss real Banach spaces; the definition is exactly the same, except that all scalars are assumed to be real.

5.3 Definition Consider a linear transformation $\Lambda$ from a normed linear space $X$ into a normed linear space $Y$, and define its norm by

$$
\|\Lambda\|=\sup \{\|\Lambda x\|: x \in X,\|x\| \leq 1\} .
$$

If $\|\Lambda\|<\infty$, then $\Lambda$ is called a bounded linear transformation.

In (1), $\|x\|$ is the norm of $x$ in $X,\|\Lambda x\|$ is the norm of $\Lambda x$ in $Y$; it will frequently happen that several norms occur together, and the context will make it clear which is which.

Observe that we could restrict ourselves to unit vectors $x$ in (1), i.e., to $x$ with $\|x\|=1$, without changing the supremum, since

$$
\|\Lambda(\alpha x)\|=\|\alpha \Lambda x\|=|\alpha|\|\Lambda x\| .
$$

Observe also that $\|\Lambda\|$ is the smallest number such that the inequality

$$
\|\Lambda x\| \leq\|\Lambda\|\|x\|
$$

holds for every $x \in X$.

The following geometric picture is helpful: $\Lambda$ maps the closed unit ball in $X$, i.e., the set

$$
\{x \in X:\|x\| \leq 1\}
$$

into the closed ball in $Y$ with center at 0 and radius $\|\Lambda\|$.

An important special case is obtained by taking the complex field for $Y$; in that case we talk about bounded linear functionals.

5.4 Theorem For a linear transformation $\Lambda$ of a normed linear space $X$ into a normed linear space $Y$, each of the following three conditions implies the other two:

(a) $\Lambda$ is bounded.

(b) $\Lambda$ is continuous.

(c) $\Lambda$ is continuous at one point of $X$.

ProOF Since $\left\|\Lambda\left(x_{1}-x_{2}\right)\right\| \leq\|\Lambda\|\left\|x_{1}-x_{2}\right\|$, it is clear that $(a)$ implies $(b)$, and $(b)$ implies (c) trivially. Suppose $\Lambda$ is continuous at $x_{0}$. To each $\epsilon>0$ one can then find a $\delta>0$ so that $\left\|x-x_{0}\right\|<\delta$ implies $\left\|\Lambda x-\Lambda x_{0}\right\|<\epsilon$. In other words, $\|x\|<\delta$ implies

$$
\left\|\Lambda\left(x_{0}+x\right)-\Lambda x_{0}\right\|<\epsilon .
$$

But then the linearity of $\Lambda$ shows that $\|\Lambda x\|<\epsilon$. Hence $\|\Lambda\| \leq \epsilon / \delta$, and (c) implies $(a)$.

## Consequences of Baire's Theorem

5.5 The manner in which the completeness of Banach spaces is frequently exploited depends on the following theorem about complete metric spaces, which also has many applications in other parts of mathematics. It implies two of the three most important theorems which make Banach spaces useful tools in analysis, the Banach-Steinhaus theorem and the open mapping theorem. The third is the Hahn-Banach extension theorem, in which completeness plays no role.

5.6 Baire's Theorem If $X$ is a complete metric space, the intersection of every countable collection of dense open subsets of $X$ is dense in $X$.

In particular (except in the trivial case $X=\varnothing$ ), the intersection is not empty. This is often the principal significance of the theorem.

Proof Suppose $V_{1}, V_{2}, V_{3}, \ldots$ are dense and open in $X$. Let $W$ be any open set in $X$. We have to show that $\cap V_{n}$ has a point in $W$ if $W \neq \varnothing$.

Let $\rho$ be the metric of $X$; let us write

$$
S(x, r)=\{y \in X: \rho(x, y)<r\}
$$

and let $\bar{S}(x, r)$ be the closure of $S(x, r)$. [Note: There exist situations in which $\bar{S}(x, r)$ does not contain all $y$ with $\rho(x, y) \leq r !]$

Since $V_{1}$ is dense, $W \cap V_{1}$ is a nonempty open set, and we can therefore find $x_{1}$ and $r_{1}$ such that

$$
\bar{S}\left(x_{1}, r_{1}\right) \subset W \cap V_{1} \quad \text { and } \quad 0<r_{1}<1
$$

If $n \geq 2$ and $x_{n-1}$ and $r_{n-1}$ are chosen, the denseness of $V_{n}$ shows that $V_{n} \cap$ $S\left(x_{n-1}, r_{n-1}\right)$ is not empty, and we can therefore find $x_{n}$ and $r_{n}$ such that

$$
\bar{S}\left(x_{n}, r_{n}\right) \subset V_{n} \cap S\left(x_{n-1}, r_{n-1}\right) \quad \text { and } \quad 0<r_{n}<\frac{1}{n}
$$

By induction, this process produces a sequence $\left\{x_{n}\right\}$ in $X$. If $i>n$ and $j>n$, the construction shows that $x_{i}$ and $x_{j}$ both lie in $S\left(x_{n}, r_{n}\right)$, so that $\rho\left(x_{i}, x_{j}\right)<2 r_{n}<2 / n$, and hence $\left\{x_{n}\right\}$ is a Cauchy sequence. Since $X$ is complete, there is a point $x \in X$ such that $x=\lim x_{n}$.

Since $x_{i}$ lies in the closed set $\bar{S}\left(x_{n}, r_{n}\right)$ if $i>n$, it follows that $x$ lies in each $\bar{S}\left(x_{n}, r_{n}\right)$, and (3) shows that $x$ lies in each $V_{n}$. By (2), $x \in W$. This completes the proof.

Corollary In a complete metric space, the intersection of any countable collection of dense $G_{\delta}$ 's is again a dense $G_{\delta}$.

This follows from the theorem, since every $G_{\delta}$ is the intersection of a countable collection of open sets, and since the union of countably many countable sets is countable.

5.7 Baire's theorem is sometimes called the category theorem, for the following reason.

Call a set $E \subset X$ nowhere dense if its closure $\bar{E}$ contains no nonempty open subset of $X$. Any countable union of nowhere dense sets is called a set of the first category; all other subsets of $X$ are of the second category (Baire's terminology). Theorem 5.6 is equivalent to the statement that no complete metric space is of the first category. To see this, just take complements in the statement of Theorem 5.6.

5.8 The Banach-Steinhaus Theorem Suppose $X$ is a Banach space, $Y$ is a normed linear space, and $\left\{\Lambda_{\alpha}\right\}$ is a collection of bounded linear transformations of $X$ into $Y$, where a ranges over some index set $A$. Then either there exists an $M<\infty$ such that

$$
\left\|\Lambda_{\alpha}\right\| \leq M
$$

for every $\alpha \in A$, or

$$
\sup _{\alpha \in A}\left\|\Lambda_{\alpha} x\right\|=\infty
$$

for all $x$ belonging to some dense $G_{\delta}$ in $X$.

In geometric terminology, the alternatives are as follows: Either there is a ball $B$ in $Y$ (with radius $M$ and center at 0 ) such that every $\Lambda_{\alpha}$ maps the unit ball of $X$ into $B$, or there exist $x \in X$ (in fact, a whole dense $G_{\delta}$ of them) such that no ball in $Y$ contains $\Lambda_{\alpha} x$ for all $\alpha$.

The theorem is sometimes referred to as the uniform boundedness principle.

Proof Put

$$
\varphi(x)=\sup _{\alpha \in A}\left\|\Lambda_{\alpha} x\right\| \quad(x \in X)
$$

and let

$$
V_{n}=\{x: \varphi(x)>n\} \quad(n=1,2,3, \ldots)
$$

Since each $\Lambda_{\alpha}$ is continuous and since the norm of $Y$ is a continuous function on $Y$ (an immediate consequence of the triangle inequality, as in the proof of Theorem 4.6), each function $x \rightarrow\left\|\Lambda_{\alpha} x\right\|$ is continuous on $X$. Hence $\varphi$ is lower semicontinuous, and each $V_{n}$ is open.

If one of these sets, say $V_{N}$, fails to be dense in $X$, then there exist an $x_{0} \in X$ and an $r>0$ such that $\|x\| \leq r$ implies $x_{0}+x \notin V_{N}$; this means that $\varphi\left(x_{0}+x\right) \leq N$, or

$$
\left\|\Lambda_{\alpha}\left(x_{0}+x\right)\right\| \leq N
$$

for all $\alpha \in A$ and all $x$ with $\|x\| \leq r$. Since $x=\left(x_{0}+x\right)-x_{0}$, we then have

$$
\left\|\Lambda_{\alpha} x\right\| \leq\left\|\Lambda_{\alpha}\left(x_{0}+x\right)\right\|+\left\|\Lambda_{\alpha} x_{0}\right\| \leq 2 N
$$

and it follows that (1) holds with $M=2 N / r$.

The other possibility is that every $V_{n}$ is dense in $X$. In that case, $\cap V_{n}$ is a dense $G_{\delta}$ in $X$, by Baire's theorem; and since $\varphi(x)=\infty$ for every $x \in \bigcap V_{n}$, the proof is complete.

5.9 The Open Mapping Theorem Let $U$ and $V$ be the open unit balls of the Banach spaces $X$ and $Y$. To every bounded linear transformation $\Lambda$ of $X$ onto $Y$ there corresponds a $\delta>0$ so that

$$
\Lambda(U) \supset \delta V
$$

Note the word "onto" in the hypothesis. The symbol $\delta V$ stands for the set $y: y \in V\}$, i.e., the set of all $y \in Y$ with $\|y\|<\delta$.

It follows from (1) and the linearity of $\Lambda$ that the image of every open ball in , with center at $x_{0}$, say, contains an open ball in $Y$ with center at $\Lambda x_{0}$. Hence e image of every open set is open. This explains the name of the theorem.

Here is another way of stating (1): To every $y$ with $\|y\|<\delta$ there corresponds $x$ with $\|x\|<1$ so that $\Lambda x=y$.

Proof Given $y \in Y$, there exists an $x \in X$ such that $\Lambda x=y$; if $\|x\|<k$, it follows that $y \in \Lambda(k U)$. Hence $Y$ is the union of the sets $\Lambda(k U)$, for $k=1,2,3, \ldots$. Since $Y$ is complete, the Baire theorem implies that there is a nonempty open set $W$ in the closure of some $\Lambda(k U)$. This means that every point of $W$ is the limit of a sequence $\left\{\Lambda x_{i}\right\}$, where $x_{i} \in k U$; from now on, $k$ and $W$ are fixed.

Choose $y_{0} \in W$, and choose $\eta>0$ so that $y_{0}+y \in W$ if $\|y\|<\eta$. For any such $y$ there are sequences $\left\{x_{i}^{\prime}\right\},\left\{x_{i}^{\prime \prime}\right\}$ in $k U$ such that

$$
\Lambda x_{i}^{\prime} \rightarrow y_{0}, \quad \Lambda x_{i}^{\prime \prime} \rightarrow y_{0}+y \quad(i \rightarrow \infty)
$$

Setting $x_{i}=x_{i}^{\prime \prime}-x_{i}^{\prime}$, we have $\left\|x_{i}\right\|<2 k$ and $\Lambda x_{i} \rightarrow y$. Since this holds for every $y$ with $\|y\|<\eta$, the linearity of $\Lambda$ shows that the following is true, if $\delta=\eta / 2 k$ :

To each $y \in Y$ and to each $\epsilon>0$ there corresponds an $x \in X$ such that

$$
\|x\| \leq \delta^{-1}\|y\| \quad \text { and } \quad\|y-\Lambda x\|<\epsilon .
$$

This is almost the desired conclusion, as stated just before the start of the proof, except that there we had $\epsilon=0$.

Fix $y \in \delta V$, and fix $\epsilon>0$. By (3) there exists an $x_{1}$ with $\left\|x_{1}\right\|<1$ and

$$
\left\|y-\Lambda x_{1}\right\|<\frac{1}{2} \delta \epsilon \text {. }
$$

Suppose $x_{1}, \ldots, x_{n}$ are chosen so that

$$
\left\|y-\Lambda x_{1}-\cdots-\Lambda x_{n}\right\|<2^{-n} \delta \epsilon .
$$

Use (3), with $y$ replaced by the vector on the left side of (5), to obtain an $x_{n+1}$ so that (5) holds with $n+1$ in place of $n$, and

$$
\left\|x_{n+1}\right\|<2^{-n} \epsilon \quad(n=1,2,3, \ldots)
$$

If we set $s_{n}=x_{1}+\cdots+x_{n}$, (6) shows that $\left\{s_{n}\right\}$ is a Cauchy sequence in $X$. Since $X$ is complete, there exists an $x \in X$ so that $s_{n} \rightarrow x$. The inequality $\left\|x_{1}\right\|<1$, together with (6), shows that $\|x\|<1+\epsilon$. Since $\Lambda$ is continuous, $\Lambda s_{n} \rightarrow \Lambda x$. By (5), $\Lambda s_{n} \rightarrow y$. Hence $\Lambda x=y$.

We have now proved that

$$
\Lambda((1+\epsilon) U) \supset \delta V
$$

or

$$
\Lambda(U) \supset(1+\epsilon)^{-1} \delta V
$$

for every $\epsilon>0$. The union of the sets on the right of (8), taken over all $\epsilon>0$, is $\delta V$. This proves (1).

5.10 Theorem If $X$ and $Y$ are Banach spaces and if $\Lambda$ is a bounded linear transformation of $X$ onto $Y$ which is also one-to-one, then there is a $\delta>0$ such that

$$
\|\Lambda x\| \geq \delta\|x\| \quad(x \in X) .
$$

In other words, $\Lambda^{-1}$ is a bounded linear transformation of $Y$ onto $X$.

Proof If $\delta$ is chosen as in the statement of Theorem 5.9, the conclusion of that theorem, combined with the fact that $\Lambda$ is now one-to-one, shows that $\|\Lambda x\|<\delta$ implies $\|x\|<1$. Hence $\|x\| \geq 1$ implies $\|\Lambda x\| \geq \delta$, and (1) is proved.

The transformation $\Lambda^{-1}$ is defined on $Y$ by the requirement that $\Lambda^{-1} y=x$ if $y=\Lambda x$. A trivial verification shows that $\Lambda^{-1}$ is linear, and (1) implies that $\left\|\Lambda^{-1}\right\| \leq 1 / \delta$.

## Fourier Series of Continuous Functions

5.11 A Convergence Problem Is it true for every $f \in C(T)$ that the Fourier series of $f$ converges to $f(x)$ at every point $x$ ?

Let us recall that the $n$th partial sum of the Fourier series of $f$ at the point $x$ is given by

$$
s_{n}(f ; x)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) D_{n}(x-t) d t \quad(n=0,1,2, \ldots)
$$

where

$$
D_{n}(t)=\sum_{k=-n}^{n} e^{i k t}
$$

This follows directly from formulas 4.26(1) and 4.26(3).

The problem is to determine whether

$$
\lim _{n \rightarrow \infty} s_{n}(f ; x)=f(x)
$$

for every $f \in C(T)$ and for every real $x$. We observed in Sec. 4.26 that the partial sums do converge to $f$ in the $L^{2}$-norm, and Theorem 3.12 implies therefore that each $f \in L^{2}(T)$ [hence also each $f \in C(T)$ ] is the pointwise limit a.e. of some subsequence of the full sequence of the partial sums. But this does not answer the present question.

We shall see that the Banach-Steinhaus theorem answers the question negatively. Put

$$
s^{*}(f ; x)=\sup _{n}\left|s_{n}(f ; x)\right| .
$$

To begin with, take $x=0$, and define

$$
\Lambda_{n} f=s_{n}(f ; 0) \quad(f \in C(T) ; n=1,2,3, \ldots)
$$

We know that $C(T)$ is a Banach space, relative to the supremum norm $\|f\|_{\infty}$. It follows from (1) that each $\Lambda_{n}$ is a bounded linear functional on $C(T)$, of norm

$$
\left\|\Lambda_{n}\right\| \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|D_{n}(t)\right| d t=\left\|D_{n}\right\|_{1}
$$

We claim that

$$
\left\|\Lambda_{n}\right\| \rightarrow \infty \quad \text { as } n \rightarrow \infty
$$

This will be proved by showing that equality holds in (6) and that

$$
\left\|D_{n}\right\|_{1} \rightarrow \infty \quad \text { as } n \rightarrow \infty \text {. }
$$

Multiply (2) by $e^{i t / 2}$ and by $e^{-i t / 2}$ and subtract one of the resulting two equations from the other, to obtain

$$
D_{n}(t)=\frac{\sin \left(n+\frac{1}{2}\right) t}{\sin (t / 2)}
$$

Since $|\sin x| \leq|x|$ for all real $x$, (9) shows that

$$
\begin{aligned}
\left\|D_{n}\right\|_{1} & >\frac{2}{\pi} \int_{0}^{\pi}\left|\sin \left(n+\frac{1}{2}\right) t\right| \frac{d t}{t}=\frac{2}{\pi} \int_{0}^{(n+1 / 2) \pi}|\sin t| \frac{d t}{t} \\
& >\frac{2}{\pi} \sum_{k=1}^{n} \frac{1}{k \pi} \int_{(k-1) \pi}^{k \pi}|\sin t| d t=\frac{4}{\pi^{2}} \sum_{k=1}^{n} \frac{1}{k} \rightarrow \infty,
\end{aligned}
$$

which proves (8).

Next, fix $n$, and put $g(t)=1$ if $D_{n}(t) \geq 0, g(t)=-1$ if $D_{n}(t)<0$. There exist $f_{j} \in C(T)$ such that $-1 \leq f_{j} \leq 1$ and $f_{j}(t) \rightarrow g(t)$ for every $t$, as $j \rightarrow \infty$. By the dominated convergence theorem,

$$
\lim _{j \rightarrow \infty} \Lambda_{n}\left(f_{j}\right)=\lim _{j \rightarrow \infty} \frac{1}{2 \pi} \int_{-\pi}^{\pi} f_{j}(-t) D_{n}(t) d t=\frac{1}{2 \pi} \int_{-\pi}^{\pi} g(-t) D_{n}(t) d t=\left\|D_{n}\right\|_{1} .
$$

Thus equality holds in (6), and we have proved (7).

Since (7) holds, the Banach-Steinhaus theorem asserts now that $s^{*}(f ; 0)=\infty$ for every $f$ in some dense $G_{\delta}$-set in $C(T)$.

We chose $x=0$ just for convenience. It is clear that the same result holds for every other $x$ :

To each real number $x$ there corresponds a set $E_{x} \subset C(T)$ which is a dense $G_{\delta}$ in $C(T)$, such that $s^{*}(f ; x)=\infty$ for every $f \in E_{x}$.

In particular, the Fourier series of each $f \in E_{x}$ diverges at $x$, and we have a negative answer to our question. (Exercise 22 shows the answer is positive if mere continuity is replaced by a somewhat stronger smoothness assumption.)

It is interesting to observe that the above result can be strengthened by another application of Baire's theorem. Let us take countably many points $x_{i}$, and let $E$ be the intersection of the corresponding sets

$$
E_{x_{i}} \subset C(T)
$$

By Baire's theorem, $E$ is a dense $G_{\delta}$ in $C(T)$. Every $f \in E$ has

$$
s^{*}\left(f ; x_{i}\right)=\infty
$$

at every point $x_{i}$.

For each $f, s^{*}(f ; x)$ is a lower semicontinuous function of $x$, since (4) exhibits it as the supremum of a collection of continuous functions. Hence $\left\{x: s^{*}(f ; x)=\infty\right\}$ is a $G_{\delta}$ in $R^{1}$, for each $f$. If the above points $x_{i}$ are taken so that their union is dense in $(-\pi, \pi)$, we obtain the following result:

5.12 Theorem There is a set $E \subset C(T)$ which is a dense $G_{\delta}$ in $C(T)$ and which has the following property: For each $f \in E$, the set

$$
Q_{f}=\left\{x: s^{*}(f ; x)=\infty\right\}
$$

is a dense $G_{\delta}$ in $R^{1}$.

This gains in interest if we realize that $E$, as well as each $Q_{f}$, is an uncountable set:

5.13 Theorem In a complete metric space $X$ which has no isolated points, no countable dense set is $a G_{\delta}$.

Proof Let $x_{k}$ be the points of a countable dense set $E$ in $X$. Assume that $E$ is a $G_{\delta}$. Then $E=\bigcap V_{n}$, where each $V_{n}$ is dense and open. Let

$$
W_{n}=V_{n}-\bigcup_{k=1}^{n}\left\{x_{k}\right\}
$$

Then each $W_{n}$ is still a dense open set, but $\bigcap W_{n}=\varnothing$, in contradiction to Baire's theorem.

Note: A slight change in the proof of Baire's theorem shows actually that every dense $G_{\delta}$ contains a perfect set if $X$ is as above.

## Fourier Coefficients of $L^{1}$-functions

5.14 As in Sec. 4.26, we associate to every $f \in L^{1}(T)$ a function $\hat{f}$ on $Z$ defined by

$$
\hat{f}(n)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) e^{-i n t} d t \quad(n \in Z)
$$

It is easy to prove that $\hat{f}(n) \rightarrow 0$ as $|n| \rightarrow \infty$, for every $f \in L^{1}$. For we know that $C(T)$ is dense in $L^{1}(T)$ (Theorem 3.14) and that the trigonometric polynomials are dense in $C(T)$ (Theorem 4.25). If $\epsilon>0$ and $f \in L^{1}(T)$, this says that there is a $g \in C(T)$ and a trigonometric polynomial $P$ such that $\|f-g\|_{1}<\epsilon$ and $\|g-P\|_{\infty}<\epsilon$. Since

$$
\|g-P\|_{1} \leq\|g-P\|_{\infty}
$$

if follows that $\|f-P\|_{1}<2 \epsilon$; and if $|n|$ is large enough (depending on $P$ ), then

$$
|\hat{f}(n)|=\left|\frac{1}{2 \pi} \int_{-\pi}^{\pi}\{f(t)-P(t)\} e^{-i n t} d t\right| \leq\|f-P\|_{1}<2 \epsilon
$$

Thus $\hat{f}(n) \rightarrow 0$ as $n \rightarrow \pm \infty$. This is known as the Riemann-Lebesgue lemma.

The question we wish to raise is whether the converse is true. That is to say, if $\left\{a_{n}\right\}$ is a sequence of complex numbers such that $a_{n} \rightarrow 0$ as $n \rightarrow \pm \infty$, does it follow that there is an $f \in L^{1}(T)$ such that $\hat{f}(n)=a_{n}$ for all $n \in Z$ ? In other words, is something like the Riesz-Fischer theorem true in this situation?

This can easily be answered (negatively) with the aid of the open mapping theorem.

Let $c_{0}$ be the space of all complex functions $\varphi$ on $Z$ such that $\varphi(n) \rightarrow 0$ as $n \rightarrow \pm \infty$, with the supremum norm

$$
\|\varphi\|_{\infty}=\sup \{|\varphi(n)|: n \in Z\}
$$

Then $c_{0}$ is easily seen to be a Banach space. In fact, if we declare every subset of $Z$ to be open, then $Z$ is a locally compact Hausdorff space, and $c_{0}$ is nothing but $C_{0}(Z)$.

The following theorem contains the answer to our question:

5.15 Theorem The mapping $f \rightarrow \hat{f}$ is a one-to-one bounded linear transformation of $L^{1}(T)$ into (but not onto) $c_{0}$.

Proof Define $\Lambda$ by $\Lambda f=\hat{f}$. It is clear that $\Lambda$ is linear. We have just proved that $\Lambda$ maps $L^{1}(T)$ into $c_{0}$, and formula 5.14(1) shows that $|\hat{f}(n)| \leq\|f\|_{1}$, so that $\|\Lambda\| \leq 1$. (Actually, $\|\Lambda\|=1$; to see this, take $f=1$.) Let us now prove that $\Lambda$ is one-to-one. Suppose $f \in L^{1}(T)$ and $\hat{f}(n)=0$ for every $n \in Z$. Then

$$
\int_{-\pi}^{\pi} f(t) g(t) d t=0
$$

if $g$ is any trigonometric polynomial. By Theorem 4.25 and the dominated convergence theorem, (1) holds for every $g \in C(T)$. Apply the dominated convergence theorem once more, in conjunction with the Corollary to Lusin's theorem, to conclude that (1) holds if $g$ is the characteristic function of any measurable set in $T$. Now Theorem $1.39(b)$ shows that $f=0$ a.e.

If the range of $\Lambda$ were all of $c_{0}$, Theorem 5.10 would imply the existence of a $\delta>0$ such that

$$
\|\hat{f}\|_{\infty} \geq \delta\|f\|_{1}
$$

for every $f \in L^{1}(T)$. But if $D_{n}(t)$ is defined as in Sec. 5.11, then $D_{n} \in L^{1}(T)$, $\left\|\hat{D}_{n}\right\|_{\infty}=1$ for $n=1,2,3, \ldots$, and $\left\|D_{n}\right\|_{1} \rightarrow \infty$ as $n \rightarrow \infty$. Hence there is no $\delta>0$ such that the inequalities

$$
\left\|\hat{D}_{n}\right\|_{\infty} \geq \delta\left\|D_{n}\right\|_{1}
$$

hold for every $n$.

This completes the proof.

## The Hahn-Banach Theorem

5.16 Theorem If $M$ is a subspace of a normed linear space $X$ and if $f$ is a bounded linear functional on $M$, then $f$ can be extended to a bounded linear functional $F$ on $X$ so that $\|F\|=\|f\|$.

Note that $M$ need not be closed.

Before we turn to the proof, some comments seem called for. First, to say (in the most general situation) that a function $F$ is an extension of $f$ means that the domain of $F$ includes that of $f$ and that $F(x)=f(x)$ for all $x$ in the domain of $f$. Second, the norms $\|F\|$ and $\|f\|$ are computed relative to the domains of $F$ and $f$; explicitly,

$$
\|f\|=\sup \{|f(x)|: x \in M,\|x\| \leq 1\}, \quad\|F\|=\sup \{|F(x)|: x \in X,\|x\| \leq 1\}
$$

The third comment concerns the field of scalars. So far everything has been stated for complex scalars, but the complex field could have been replaced by the real field without any changes in statements or proofs. The Hahn-Banach theorem is also true in both cases; nevertheless, it appears to be essentially a "real" theorem. The fact that the complex case was not yet proved when Banach wrote his classical book "Opérations linéaires" may be the main reason that real scalars are the only ones considered in his work.

It will be helpful to introduce some temporary terminology. Recall that $V$ is a complex (real) vector space if $x+y \in V$ for $x$ and $y \in V$, and if $a x \in V$ for all complex (real) numbers $\alpha$. It follows trivially that every complex vector space is also a real vector space. A complex function $\varphi$ on a complex vector space $V$ is a complex-linear functional if

$$
\varphi(x+y)=\varphi(x)+\varphi(y) \quad \text { and } \quad \varphi(\alpha x)=\alpha \varphi(x)
$$

for all $x$ and $y \in V$ and all complex $\alpha$. A real-valued function $\varphi$ on a complex (real) vector space $V$ is a real-linear functional if (1) holds for all real $\alpha$.

If $u$ is the real part of a complex-linear functional $f$, i.e., if $u(x)$ is the real part of the complex number $f(x)$ for all $x \in V$, it is easily seen that $u$ is a real-linear functional. The following relations hold between $f$ and $u$ :

5.17 Proposition Let $V$ be a complex vector space.

(a) If $u$ is the real part of a complex-linear functional $f$ on $V$, then

$$
f(x)=u(x)-i u(i x) \quad(x \in V) .
$$

(b) If $u$ is a real-linear functional on $V$ and if $f$ is defined by (1), then $f$ is a complex-linear functional on $V$.

(c) If $V$ is a normed linear space and $f$ and $u$ are related as in (1), then $\|f\|=\|u\|$.

Proof If $\alpha$ and $\beta$ are real numbers and $z=\alpha+i \beta$, the real part of $i z$ is $-\beta$. This gives the identity

$$
z=\operatorname{Re} z-i \operatorname{Re}(i z)
$$

for all complex numbers $z$. Since

$$
\operatorname{Re}(i f(x))=\operatorname{Re} f(i x)=u(i x)
$$

(1) follows from (2) with $z=f(x)$.

Under the hypotheses $(b)$, it is clear that $f(x+y)=f(x)+f(y)$ and that $f(\alpha x)=\alpha f(x)$ for all real $\alpha$. But we also have

$$
f(i x)=u(i x)-i u(-x)=u(i x)+i u(x)=i f(x)
$$

which proves that $f$ is complex-linear.

Since $|u(x)| \leq|f(x)|$, we have $\|u\| \leq\|f\|$. On the other hand, to every $x \in V$ there corresponds a complex number $\alpha,|\alpha|=1$, so that $\alpha f(x)=|f(x)|$. Then

$$
|f(x)|=f(\alpha x)=u(\alpha x) \leq\|u\| \cdot\|\alpha x\|=\|u\| \cdot\|x\|,
$$

which proves that $\|f\| \leq\|u\|$.

5.18 Proof of Theorem 5.16 We first assume that $X$ is a real normed linear space and, consequently, that $f$ is a real-linear bounded functional on $M$. If $\|f\|=0$, the desired extension is $F=0$. Omitting this case, there is no loss of generality in assuming that $\|f\|=1$.

Choose $x_{0} \in X, x_{0} \notin M$, and let $M_{1}$ be the vector space spanned by $M$ and $x_{0}$. Then $M_{1}$ consists of all vectors of the form $x+\lambda x_{0}$, where $x \in M$ and $\lambda$ is a real scalar. If we define $f_{1}\left(x+\lambda x_{0}\right)=f(x)+\lambda \alpha$, where $\alpha$ is any fixed real number, it is trivial to verify that an extension of $f$ to a linear functional on $M_{1}$ is obtained. The problem is to choose $\alpha$ so that the extended functional still has norm 1 . This will be the case provided that

$$
|f(x)+\lambda \alpha| \leq\left\|x+\lambda x_{0}\right\| \quad(x \in M, \lambda \text { real }) .
$$

Replace $x$ by $-\lambda x$ and divide both sides of (1) by $|\lambda|$. The requirement is then that

$$
|f(x)-\alpha| \leq\left\|x-x_{0}\right\| \quad(x \in M)
$$

i.e., that $A_{x} \leq \alpha \leq B_{x}$ for all $x \in M$, where

$$
A_{x}=f(x)-\left\|x-x_{0}\right\| \quad \text { and } \quad B_{x}=f(x)+\left\|x-x_{0}\right\| \text {. }
$$

There exists such an $\alpha$ if and only if all the intervals $\left[A_{x}, B_{x}\right]$ have a common point, i.e., if and only if

$$
A_{x} \leq B_{y}
$$

for all $x$ and $y \in M$. But

$$
f(x)-f(y)=f(x-y) \leq\|x-y\| \leq\left\|x-x_{0}\right\|+\left\|y-x_{0}\right\|,
$$

and so (4) follows from (3).

We have now proved that there exists a norm-preserving extension $f_{1}$ of $f$ on $M_{1}$.

Let $\mathscr{P}$ be the collection of all ordered pairs $\left(M^{\prime}, f^{\prime}\right)$, where $M^{\prime}$ is a subspace of $X$ which contains $M$ and where $f^{\prime}$ is a real-linear extension of $f$ to $M^{\prime}$, with $\left\|f^{\prime}\right\|=1$. Partially order $\mathscr{P}$ by declaring $\left(M^{\prime}, f^{\prime}\right) \leq\left(M^{\prime \prime}, f^{\prime \prime}\right)$ to mean that $M^{\prime} \subset M^{\prime \prime}$ and $f^{\prime \prime}(x)=f^{\prime}(x)$ for all $x \in M^{\prime}$. The axioms of a partial order
are clearly satisfied, $\mathscr{P}$ is not empty since it contains $(M, f)$, and so the Hausdorff maximality theorem asserts the existence of a maximal totally ordered subcollection $\Omega$ of $\mathscr{P}$.

Let $\Phi$ be the collection of all $M^{\prime}$ such that $\left(M^{\prime}, f^{\prime}\right) \in \Omega$. Then $\Phi$ is totally ordered, by set inclusion, and therefore the union $\tilde{M}$ of all members of $\Phi$ is a subspace of $X$. (Note that in general the union of two subspaces is not a subspace. An example is two planes through the origin in $R^{3}$.) If $x \in \tilde{M}$, then $x \in M^{\prime}$ for some $M^{\prime} \in \Phi$; define $F(x)=f^{\prime}(x)$, where $f^{\prime}$ is the function which occurs in the pair $\left(M^{\prime}, f^{\prime}\right) \in \Omega$. Our definition of the partial order in $\Omega$ shows that it is immaterial which $M^{\prime} \in \Phi$ we choose to define $F(x)$, as long as $M^{\prime}$ contains $x$.

It is now easy to check that $F$ is a linear functional on $\tilde{M}$, with $\|F\|=1$. If $\tilde{M}$ were a proper subspace $X$, the first part of the proof would give us a further extension of $F$, and this would contradict the maximality of $\Omega$. Thus $\tilde{M}=X$, and the proof is complete for the case of real scalars.

If now $f$ is a complex-linear functional on the subspace $M$ of the complex normed linear space $X$, let $u$ be the real part of $f$, use the real Hahn-Banach theorem to extend $u$ to a real-linear functional $U$ on $X$, with $\|U\|=\|u\|$, and define

$$
F(x)=U(x)-i U(i x) \quad(x \in X) .
$$

By Proposition 5.17, $F$ is a complex-linear extension of $f$, and

$$
\|F\|=\|U\|=\|u\|=\|f\| .
$$

This completes the proof.

Let us mention two important consequences of the Hahn-Banach theorem:

5.19 Theorem Let $M$ be a linear subspace of a normed linear space $X$, and let $x_{0} \in X$. Then $x_{0}$ is in the closure $\bar{M}$ of $M$ if and only if there is no bounded linear functional $f$ on $X$ such that $f(x)=0$ for all $x \in M$ but $f\left(x_{0}\right) \neq 0$.

ProOF If $x_{0} \in \bar{M}, f$ is a bounded linear functional on $X$, and $f(x)=0$ for all $x \in M$, the continuity of $f$ shows that we also have $f\left(x_{0}\right)=0$.

Conversely, suppose $x_{0} \notin \bar{M}$. Then there exists a $\delta>0$ such that $\left\|x-x_{0}\right\|>\delta$ for all $x \in M$. Let $M^{\prime}$ be the subspace generated by $M$ and $x_{0}$, and define $f\left(x+\lambda x_{0}\right)=\lambda$ if $x \in M$ and $\lambda$ is a scalar. Since

$$
\delta|\lambda| \leq|\lambda|\left\|x_{0}+\lambda^{-1} x\right\|=\left\|\lambda x_{0}+x\right\|,
$$

we see that $f$ is a linear functional on $M^{\prime}$ whose norm is at most $\delta^{-1}$. Also $f(x)=0$ on $M, f\left(x_{0}\right)=1$. The Hahn-Banach theorem allows us to extend this $f$ from $M^{\prime}$ to $X$.

5.20 Theorem If $X$ is a normed linear space and if $x_{0} \in X, x_{0} \neq 0$, there is a bounded linear functional $f$ on $X$, of norm 1 , so that $f\left(x_{0}\right)=\left\|x_{0}\right\|$.

Proof Let $M=\left\{\lambda x_{0}\right\}$, and define $f\left(\lambda x_{0}\right)=\lambda\left\|x_{0}\right\|$. Then $f$ is a linear functional of norm 1 on $M$, and the Hahn-Banach theorem can again be applied. I/I/

5.21 Remarks If $X$ is a normed linear space, let $X^{*}$ be the collection of all bounded linear functionals on $X$. If addition and scalar multiplication of linear functionals are defined in the obvious manner, it is easy to see that $X^{*}$ is again a normed linear space. In fact, $X^{*}$ is a Banach space; this follows from the fact that the field of scalars is a complete metric space. We leave the verification of these properties of $X^{*}$ as an exercise.

One of the consequences of Theorem 5.20 is that $X^{*}$ is not the trivial vector space (i.e., $X^{*}$ consists of more than 0 ) if $X$ is not trivial. In fact, $X^{*}$ separates points on $X$. This means that if $x_{1} \neq x_{2}$ in $X$ there exists an $f \in X^{*}$ such that $f\left(x_{1}\right) \neq f\left(x_{2}\right)$. To prove this, merely take $x_{0}=x_{2}-x_{1}$ in Theorem 5.20 .

Another consequence is that, for $x \in X$,

$$
\|x\|=\sup \left\{|f(x)|: f \in X^{*},\|f\|=1\right\} .
$$

Hence, for fixed $x \in X$, the mapping $f \rightarrow f(x)$ is a bounded linear functional on $X^{*}$, of norm $\|x\|$.

This interplay between $X$ and $X^{*}$ (the so-called "dual space" of $X$ ) forms the basis of a large portion of that part of mathematics which is known as functional analysis.

## An Abstract Approach to the Poisson Integral

5.22 Successful applications of the Hahn-Banach theorem to concrete problems depend of course on a knowledge of the bounded linear functionals on the normed linear space under consideration. So far we have only determined the bounded linear functionals on a Hilbert space (where a much simpler proof of the Hahn-Banach theorem exists; see Exercise 6), and we know the positive linear functionals on $C_{c}(X)$.

We shall now describe a general situation in which the last-mentioned functionals occur naturally.

Let $K$ be a compact Hausdorff space, let $H$ be a compact subset of $K$, and let $A$ be a subspace of $C(K)$ such that $1 \in A(1$ denotes the function which assigns the number 1 to each $x \in K$ ) and such that

$$
\|f\|_{K}=\|f\|_{H} \quad(f \in A) .
$$

Here we used the notation

$$
\|f\|_{E}=\sup \{|f(x)|: x \in E\}
$$

Because of the example discussed in Sec. 5.23, $H$ is sometimes called a boundary of $K$, corresponding to the space $A$.

If $f \in A$ and $x \in K$,(1) says that

$$
|f(x)| \leq\|f\|_{H} .
$$

In particular, if $f(y)=0$ for every $y \in H$, then $f(x)=0$ for all $x \in K$. Hence if $f_{1}$ and $f_{2} \in A$ and $f_{1}(y)=f_{2}(y)$ for every $y \in H$, then $f_{1}=f_{2}$; to see this, put $f=$ $f_{1}-f_{2}$.

Let $M$ be the set of all functions on $H$ that are restrictions to $H$ of members of $A$. It is clear that $M$ is a subspace of $C(H)$. The preceding remark shows that each member of $M$ has a unique extension to a member of $A$. Thus we have a natural one-to-one correspondence between $M$ and $A$, which is also normpreserving, by (1). Hence it will cause no confusion if we use the same letter to designate a member of $A$ and its restriction to $H$.

Fix a point $x \in K$. The inequality (3) shows that the mapping $f \rightarrow f(x)$ is a bounded linear functional on $M$, of norm 1 [since equality holds in (3) if $f=1$ ]. By the Hahn-Banach theorem there is a linear functional $\Lambda$ on $C(H)$, of norm 1, such that

$$
\Lambda f=f(x) \quad(f \in M)
$$

We claim that the properties

$$
\Lambda 1=1, \quad\|\Lambda\|=1
$$

imply that $\Lambda$ is a positive linear functional on $C(H)$.

To prove this, suppose $f \in C(H), 0 \leq f \leq 1$, put $g=2 f-1$, and put $\Lambda g=\alpha+i \beta$, where $\alpha$ and $\beta$ are real. Note that $-1 \leq g \leq 1$, so that $|g+i r|^{2} \leq 1+r^{2}$ for every real constant $r$. Hence (5) implies that

$$
(\beta+r)^{2} \leq|\alpha+i(\beta+r)|^{2}=|\Lambda(g+i r)|^{2} \leq 1+r^{2} .
$$

Thus $\beta^{2}+2 r \beta \leq 1$ for every real $r$, which forces $\beta=0$. Since $\|g\|_{H} \leq 1$, we have $|\alpha| \leq 1$; hence

$$
\Lambda f=\frac{1}{2} \Lambda(1+g)=\frac{1}{2}(1+\alpha) \geq 0
$$

Now Theorem 2.14 can be applied. It shows that there is a regular positive Borel measure $\mu_{x}$ on $H$ such that

$$
\Lambda f=\int_{H} f d \mu_{x} \quad(f \in C(H))
$$

In particular, we get the representation formula

$$
f(x)=\int_{H} f d \mu_{x} \quad(f \in A)
$$

What we have proved is that to each $x \in K$ there corresponds a positive measure $\mu_{x}$ on the "boundary" $H$ which "represents" $x$ in the sense that (9) holds for every $f \in A$.

Note that $\Lambda$ determines $\mu_{x}$ uniquely; but there is no reason to expect the Hahn-Banach extension to be unique. Hence, in general, we cannot say much about the uniqueness of the representing measures. Under special circumstances we do get uniqueness, as we shall see presently.

5.23 To see an example of the preceding situation, let $U=\{z:|z|<1\}$ be the open unit disc in the complex plane, put $K=\bar{U}$ (the closed unit disc), and take for $H$ the boundary $T$ of $U$. We claim that every polynomial $f$, i.e., every function of the form

$$
f(z)=\sum_{n=0}^{N} a_{n} z^{n}
$$

where $a_{0}, \ldots, a_{N}$ are complex numbers, satisfies the relation

$$
\|f\|_{U}=\|f\|_{T} \text {. }
$$

(Note that the continuity of $f$ shows that the supremum of $|f|$ over $U$ is the same as that over $\bar{U}$.)

Since $\bar{U}$ is compact, there exists a $z_{0} \in \bar{U}$ such that $\left|f\left(z_{0}\right)\right| \geq|f(z)|$ for all $z \in \bar{U}$. Assume $z_{0} \in U$. Then

$$
f(z)=\sum_{n=0}^{N} b_{n}\left(z-z_{0}\right)^{n}
$$

and if $0<r<1-\left|z_{0}\right|$, we obtain

$$
\sum_{n=0}^{N}\left|b_{n}\right|^{2} r^{2 n}=\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|f\left(z_{0}+r e^{i \theta}\right)\right|^{2} d \theta \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|f\left(z_{0}\right)\right|^{2} d \theta=\left|b_{0}\right|^{2}
$$

so that $b_{1}=b_{2}=\cdots=b_{N}=0$; i.e., $f$ is constant. Thus $z_{0} \in T$ for every nonconstant polynomial $f$, and this proves (2).

(We have just proved a special case of the maximum modulus theorem; we shall see later that this is an important property of all holomorphic functions.)

5.24 The Poisson Integral Let $A$ be any subspace of $C(\bar{U})$ (where $\bar{U}$ is the closed unit disc, as above) such that $A$ contains all polynomials and such that

$$
\|f\|_{U}=\|f\|_{T}
$$

holds for every $f \in A$. We do not exclude the possibility that $A$ consists of precisely the polynomials, but $A$ might be larger.

The general result obtained in Sec. 5.22 applies to $A$ and shows that to each $z \in U$ there corresponds a positive Borel measure $\mu_{z}$ on $T$ such that

$$
f(z)=\int_{T} f d \mu_{z} \quad(f \in A)
$$

(This also holds for $z \in T$, but is then trivial: $\mu_{z}$ is simply the unit mass concentrated at the point $z$.)

We now fix $z \in U$ and write $z=r e^{i \theta}, 0 \leq r<1, \theta$ real.

If $u_{n}(w)=w^{n}$, then $u_{n} \in A$ for $n=0,1,2, \ldots$; hence (2) shows that

$$
r^{n} e^{i n \theta}=\int_{T} u_{n} d \mu_{z} \quad(n=0,1,2, \ldots)
$$

Since $u_{-n}=\bar{u}_{n}$ on $T$, (3) leads to

$$
\int_{T} u_{n} d \mu_{z}=r^{|n|} e^{i n \theta} \quad(n=0, \pm 1, \pm 2, \ldots)
$$

This suggests that we look at the real function

$$
P_{r}(\theta-t)=\sum_{n=-\infty}^{\infty} r^{|n|} e^{i n(\theta-t)} \quad(t \text { real })
$$

since

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} P_{r}(\theta-t) e^{i n t} d t=r^{|n|} e^{i n \theta} \quad(n=0, \pm 1, \pm 2, \ldots)
$$

Note that the series (5) is dominated by the convergent geometric series $\sum r^{|n|}$, so that it is legitimate to insert the series into the integral (6) and to integrate term by term, which gives (6). Comparison of (4) and (6) gives

$$
\int_{T} f d \mu_{z}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f\left(e^{i t}\right) P_{r}(\theta-t) d t
$$

for $f=u_{n}$, hence for every trigonometric polynomial $f$, and Theorem 4.25 now implies that (7) holds for every $f \in C(T)$. [This shows that $\mu_{z}$ was uniquely determined by (2). Why?

In particular, (7) holds if $f \in A$, and then (2) gives the representation

$$
f(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f\left(e^{i \eta}\right) P_{r}(\theta-t) d t \quad(f \in A)
$$

The series (5) can be summed explicitly, since it is the real part of

$$
1+2 \sum_{1}^{\infty}\left(z e^{-i t}\right)^{n}=\frac{e^{i t}+z}{e^{i t}-z}=\frac{1-r^{2}+2 i r \sin (\theta-t)}{\left|1-z e^{-i t}\right|^{2}} .
$$

Thus

$$
P_{r}(\theta-t)=\frac{1-r^{2}}{1-2 r \cos (\theta-t)+r^{2}}
$$

This is the so-called "Poisson kernel." Note that $P_{r}(\theta-t) \geq 0$ if $0 \leq r<1$.

We now summarize what we have proved:

5.25 Theorem Suppose $A$ is a vector space of continuous complex functions on the closed unit disc $\bar{U}$. If $A$ contains all polynomials, and if

$$
\sup _{z \in U}|f(z)|=\sup _{z \in T}|f(z)|
$$

for every $f \in A$ (where $T$ is the unit circle, the boundary of $U$ ), then the Poisson integral representation

$$
f(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{1-r^{2}}{1-2 r \cos (\theta-t)+r^{2}} f\left(e^{i t}\right) d t \quad\left(z=r e^{i \theta}\right)
$$

is valid for every $f \in A$ and every $z \in U$.

## Exercises

1 Let $X$ consist of two points $a$ and $b$, put $\mu(\{a\})=\mu(\{b\})=\frac{1}{2}$, and let $L^{p}(\mu)$ be the resulting real $L^{p}$-space. Identify each real function $f$ on $X$ with the point $(f(a), f(b))$ in the plane, and sketch the unit balls of $L^{p}(\mu)$, for $0<p \leq \infty$. Note that they are convex if and only if $1 \leq p \leq \infty$. For which $p$ is this unit ball a square? A circle? If $\mu(\{a\}) \neq \mu(b)$, how does the situation differ from the preceding one?

2 Prove that the unit ball (open or closed) is convex in every normed linear space.

3 If $1<p<\infty$, prove that the unit ball of $L^{p}(\mu)$ is strictly convex; this means that if

$$
\|f\|_{p}=\|g\|_{p}=1, \quad f \neq g, \quad h=\frac{1}{2}(f+g)
$$

then $\|h\|_{p}<1$. (Geometrically, the surface of the ball contains no straight lines.) Show that this fails in every $L^{1}(\mu)$, in every $L^{\infty}(\mu)$, and in every $C(X)$. (Ignore trivialities, such as spaces consisting of only one point.)

4 Let $C$ be the space of all continuous functions on $[0,1]$, with the supremum norm. Let $M$ consist of all $f \in C$ for which

$$
\int_{0}^{1 / 2} f(t) d t-\int_{1 / 2}^{1} f(t) d t=1
$$

Prove that $M$ is a closed convex subset of $C$ which contains no element of minimal norm.

5 Let $M$ be the set of all $f \in L^{1}([0,1])$, relative to Lebesgue measure, such that

$$
\int_{0}^{1} f(t) d t=1
$$

Show that $M$ is a closed convex subset of $L^{1}([0,1])$ which contains infinitely many elements of minimal norm. (Compare this and Exercise 4 with Theorem 4.10.)

6 Let $f$ be a bounded linear functional on a subspace $M$ of a Hilbert space $H$. Prove that $f$ has a unique norm-preserving extension to a bounded linear functional on $H$, and that this extension vanishes on $M^{\perp}$.

7 Construct a bounded linear functional on some subspace of some $L^{1}(\mu)$ which has two (hence infinitely many) distinct norm-preserving linear extensions to $L^{1}(\mu)$.

8 Let $X$ be a normed linear space, and let $X^{*}$ be its dual space, as defined in Sec. 5.21, with the norm

$$
\|f\|=\sup \{|f(x)|:\|x\| \leq 1\}
$$

(a) Prove that $X^{*}$ is a Banach space.

(b) Prove that the mapping $f \rightarrow f(x)$ is, for each $x \in X$, a bounded linear functional on $X^{*}$, of norm $\|x\|$. (This gives a natural imbedding of $X$ in its "second dual " $X^{* *}$, the dual space of $X^{*}$.)
(c) Prove that $\left\{\left\|x_{n}\right\|\right\}$ is bounded if $\left\{x_{n}\right\}$ is a sequence in $X$ such that $\left\{f\left(x_{n}\right)\right\}$ is bounded for every $f \in X^{*}$.

9 Let $c_{0}, \ell^{1}$, and $\ell^{\infty}$ be the Banach spaces consisting of all complex sequences $x=\left\{\xi_{i}\right\}$, $i=1,2,3, \ldots$, defined as follows:

$$
\begin{aligned}
& x \in \ell^{1} \text { if and only if }\|x\|_{1}=\sum\left|\xi_{i}\right|<\infty . \\
& x \in \ell^{\infty} \text { if and only if }\|x\|_{\infty}=\sup \left|\xi_{i}\right|<\infty
\end{aligned}
$$

$c_{0}$ is the subspace of $\ell^{\infty}$ consisting of all $x \in \ell^{\infty}$ for which $\xi_{i} \rightarrow 0$ as $i \rightarrow \infty$.

Prove the following four statements.

(a) If $y=\left\{\eta_{i}\right\} \in \ell^{1}$ and $\Lambda x=\sum \xi_{i} \eta_{i}$ for every $x \in c_{0}$, then $\Lambda$ is a bounded linear functional on $c_{0}$, and $\|\Lambda\|=\|y\|_{1}$. Moreover, every $\Lambda \in\left(c_{0}\right)^{*}$ is obtained in this way. In brief, $\left(c_{0}\right)^{*}=\ell^{1}$.

(More precisely, these two spaces are not equal; the preceding statement exhibits an isometric vector space isomorphism between them.)

(b) In the same sense, $\left(\ell^{1}\right)^{*}=\ell^{\infty}$.

(c) Every $y \in \ell^{1}$ induces a bounded linear functional on $\ell^{\infty}$, as in $(a)$. However, this does not give all of $\left(\ell^{\infty}\right)^{*}$, since $\left(\ell^{\infty}\right)^{*}$ contains nontrivial functionals that vanish on all of $c_{0}$.

(d) $c_{0}$ and $\ell^{1}$ are separable but $\ell^{\infty}$ is not.

10 If $\sum \alpha_{i} \xi_{i}$ converges for every sequence $\left(\xi_{i}\right\}$ such that $\xi_{i} \rightarrow 0$ as $i \rightarrow \infty$, prove that $\sum\left|\alpha_{i}\right|<\infty$.

11 For $0<\alpha \leq 1$, let Lip $\alpha$ denote the space of all complex functions $f$ on $[a, b]$ for which

$$
M_{f}=\sup _{s \neq t} \frac{|f(s)-f(t)|}{|s-t|^{\alpha}}<\infty
$$

Prove that Lip $\alpha$ is a Banach space, if $\|f\|=|f(a)|+M_{f}$; also, if

$$
\|f\|=M_{f}+\sup |f(x)|
$$

(The members of Lip $\alpha$ are said to satisfy a Lipschitz condition of order $\alpha$.)

12 Let $K$ be a triangle (two-dimensional figure) in the plane, let $H$ be the set consisting of the vertices of $K$, and let $A$ be the set of all real functions $f$ on $K$, of the form

$$
f(x, y)=\alpha x+\beta y+\gamma \quad(\alpha, \beta \text {, and } \gamma \text { real }) .
$$

Show that to each $\left(x_{0}, y_{0}\right) \in K$ there corresponds a unique measure $\mu$ on $H$ such that

$$
f\left(x_{0}, y_{0}\right)=\int_{H} f d \mu
$$

(Compare Sec. 5.22.)

Replace $K$ by a square, let $H$ again be the set of its vertices, and let $A$ be as above. Show that to each point of $K$ there still corresponds a measure on $H$, with the above property, but that uniqueness is now lost. spaces.)

Can you extrapolate to a more general theorem? (Think of other figures, higher dimensional

13 Let $\left\{f_{n}\right\}$ be a sequence of continuous complex functions on a (nonempty) complete metric space $X$, such that $f(x)=\lim f_{n}(x)$ exists (as a complex number) for every $x \in X$

(a) Prove that there is an open set $V \neq \varnothing$ and a number $M<\infty$ such that $\left|f_{n}(x)\right|<M$ for all $x \in V$ and for $n=1,2,3, \ldots$

(b) If $\epsilon>0$, prove that there is an open set $V \neq \varnothing$ and an integer $N$ such that $\left|f(x)-f_{n}(x)\right| \leq \epsilon$ if $x \in V$ and $n \geq N$.

Hint for $(b)$ : For $N=1,2,3, \ldots$, put

$$
A_{N}=\left\{x:\left|f_{m}(x)-f_{n}(x)\right| \leq \epsilon \text { if } m \geq N \text { and } n \geq N\right\}
$$

Since $X=\bigcup A_{N}$, some $A_{N}$ has a nonempty interior.

14 Let $C$ be the space of all real continuous functions on $I=[0,1]$ with the supremum norm. Let $X_{n}$ be the subset of $C$ consisting of those $f$ for which there exists a $t \in I$ such that $|f(s)-f(t)| \leq n|s-t|$ for all $s \in I$. Fix $n$ and prove that each open set in $C$ contains an open set which does not intersect $X_{n}$. (Each $f \in C$ can be uniformly approximated by a zigzag function $g$ with very large slopes, and if $\|g-h\|$ is small, $h \notin X_{n}$.) Show that this implies the existence of a dense $G_{\delta}$ in $C$ which consists entirely of nowhere differentiable functions.

15 Let $A=\left(a_{i j}\right)$ be an infinite matrix with complex entries, where $i, j=0,1,2, \ldots A$ associates with each sequence $\left\{s_{j}\right\}$ a sequence $\left\{\sigma_{i}\right\}$, defined by

$$
\sigma_{i}=\sum_{j=0}^{\infty} a_{i j} s_{j} \quad(i=1,2,3, \ldots)
$$

provided that these series converge.

Prove that $A$ transforms every convergent sequence $\left\{s_{j}\right\}$ to a sequence $\left\{\sigma_{i}\right\}$ which converges to the same limit if and only if the following conditions are satisfied:

$$
\begin{aligned}
\lim _{i \rightarrow \infty} a_{i j} & =0 \quad \text { for each } j \\
\sup _{i} \sum_{j=0}^{\infty}\left|a_{i j}\right|<\infty & \\
\lim _{i \rightarrow \infty} \sum_{j=0}^{\infty} a_{i j} & =1
\end{aligned}
$$

The process of passing from $\left\{s_{j}\right\}$ to $\left\{\sigma_{i}\right\}$ is called a summability method. Two examples are:

and

$$
a_{i j}= \begin{cases}\frac{1}{i+1} & \text { if } 0 \leq j \leq \mathrm{i} \\ 0 & \text { if } i<j\end{cases}
$$

Prove that each of these also transforms some divergent sequences $\left\{s_{j}\right\}$ (even some unbounded ones) to convergent sequences $\left\{\sigma_{i}\right\}$.

16 Suppose $X$ and $Y$ are Banach spaces, and suppose $\Lambda$ is a linear mapping of $X$ into $Y$, with the following property: For every sequence $\left\{x_{n}\right\}$ in $X$ for which $x=\lim x_{n}$ and $y=\lim \Lambda x_{n}$ exist, it is true that $y=\Lambda x$. Prove that $\Lambda$ is continuous.

This is the so-called "closed graph theorem." Hint: Let $X \oplus Y$ be the set of all ordered pairs $(x, y), x \in X$ and $y \in Y$, with addition and scalar multiplication defined componentwise. Prove that $X \oplus Y$ is a Banach space, if $\|(x, y)\|=\|x\|+\|y\|$. The graph $G$ of $\Lambda$ is the subset of $X \oplus Y$ formed by the pairs $(x, \Lambda x), x \in X$. Note that our hypothesis says that $G$ is closed; hence $G$ is a Banach space. Note that $(x, \Lambda x) \rightarrow x$ is continuous, one-to-one, and linear and maps $G$ onto $X$.

Observe that there exist nonlinear mappings (of $R^{1}$ onto $R^{1}$, for instance) whose graph is closed although they are not continuous: $f(x)=1 / x$ if $x \neq 0, f(0)=0$.

17 If $\mu$ is a positive measure, each $f \in L^{\infty}(\mu)$ defines a multiplication operator $M_{f}$ on $L^{2}(\mu)$ into $L^{2}(\mu)$, such that $M_{f}(g)=f g$. Prove that $\left\|M_{f}\right\| \leq\|f\|_{\infty}$. For which measures $\mu$ is it true that $\left\|M_{f}\right\|=\|f\|_{\infty}$ for all $f \in L^{\infty}(\mu)$ ? For which $f \in L^{\infty}(\mu)$ does $M_{f}$ map $L^{2}(\mu)$ onto $L^{2}(\mu)$ ?

18 Suppose $\left\{\Lambda_{n}\right\}$ is a sequence of bounded linear transformations from a normed linear space $X$ to a Banach space $Y$, suppose $\left\|\Lambda_{n}\right\| \leq M<\infty$ for all $n$, and suppose there is a dense set $E \subset X$ such that $\left\{\Lambda_{n} x\right\}$ converges for each $x \in E$. Prove that $\left\{\Lambda_{n} x\right\}$ converges for each $x \in X$.

19 If $s_{n}$ is the $n$th partial sum of the Fourier series of a function $f \in C(T)$, prove that $s_{n} / \log n \rightarrow 0$ uniformly, as $n \rightarrow \infty$, for each $f \in C(T)$. That is, prove that

$$
\lim _{n \rightarrow \infty} \frac{\left\|s_{n}\right\|_{\infty}}{\log n}=0
$$

On the other hand, if $\lambda_{n} / \log n \rightarrow 0$, prove that there exists an $f \in C(T)$ such that the sequence $\left\{s_{n}(f ; 0) / \lambda_{n}\right\}$ is unbounded. Hint: Apply the reasoning of Exercise 18 and that of Sec. 5.11, with a better estimate of $\left\|D_{n}\right\|_{1}$ than was used there.

20 (a) Does there exist a sequence of continuous positive functions $f_{n}$ on $R^{1}$ such that $\left\{f_{n}(x)\right\}$ is unbounded if and only if $x$ is rational?

(b) Replace "rational" by "irrational" in (a) and answer the resulting question.

(c) Replace " $\left\{f_{n}(x)\right\}$ is unbounded" by " $f_{n}(x) \rightarrow \infty$ as $n \rightarrow \infty$ " and answer the resulting analogues of $(a)$ and $(b)$.

21 Suppose $E \subset R^{1}$ is measurable, and $m(E)=0$. Must there be a translate $E+x$ of $E$ that does not intersect $E$ ? Must there be a homeomorphism $h$ of $R^{1}$ onto $R^{1}$ so that $h(E)$ does not intersect $E$ ?

22 Suppose $f \in C(T)$ and $f \in \operatorname{Lip} \alpha$ for some $\alpha>0$. (See Exercise 11.) Prove that the Fourier series of $f$ converges to $f(x)$, by completing the following outline: It is enough to consider the case $x=0$, $f(0)=0$. The difference between the partial sums $s_{n}(f ; 0)$ and the integrals

$$
\frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \frac{\sin n t}{t} d t
$$

tends to 0 as $n \rightarrow \infty$. The function $f(t) / t$ is in $L^{1}(T)$. Apply the Riemann-Lebesgue lemma. More careful reasoning shows that the convergence is actually uniform on $T$.

## COMPLEX MEASURES

## Total Variation

6.1 Introduction Let $\mathfrak{M}$ be a $\sigma$-algebra in a set $X$. Call a countable collection $\left\{E_{i}\right\}$ of members of $\mathfrak{M}$ a partition of $E$ if $E_{i} \cap E_{j}=\varnothing$ whenever $i \neq j$, and if $E=$ $\bigcup E_{i}$. A complex measure $\mu$ on $\mathfrak{M}$ is then a complex function on $\mathfrak{M}$ such that

$$
\mu(E)=\sum_{i=1}^{\infty} \mu\left(E_{i}\right) \quad(E \in \mathfrak{M})
$$

for every partition $\left\{E_{i}\right\}$ of $E$.

Observe that the convergence of the series in (1) is now part of the requirement (unlike for positive measures, where the series could either converge or diverge to $\infty$ ). Since the union of the sets $E_{i}$ is not changed if the subscripts are permuted, every rearrangement of the series (1) must also converge. Hence ([26], Theorem 3.56) the series actually converges absolutely.

Let us consider the problem of finding a positive measure $\lambda$ which dominates a given complex measure $\mu$ on $\mathfrak{M}$, in the sense that $|\mu(E)| \leq \lambda(E)$ for every $E \in \mathfrak{M}$, and let us try to keep $\lambda$ as small as we can. Every solution to our problem (if there is one at all) must satisfy

$$
\lambda(E)=\sum_{i=1}^{\infty} \lambda\left(E_{i}\right) \geq \sum_{1}^{\infty}\left|\mu\left(E_{i}\right)\right|
$$

for every partition $\left\{E_{i}\right\}$ of any set $E \in \mathfrak{M}$, so that $\lambda(E)$ is at least equal to the supremum of the sums on the right of (2), taken over all partitions of $E$. This suggests that we define a set function $|\mu|$ on $\mathfrak{M}$ by

$$
|\mu|(E)=\sup \sum_{i=1}^{\infty}\left|\mu\left(E_{i}\right)\right| \quad(E \in \mathfrak{M})
$$

the supremum being taken over all partitions $\left\{E_{i}\right\}$ of $E$.

This notation is perhaps not the best, but it is the customary one. Note that $|\mu|(E) \geq|\mu(E)|$, but that in general $|\mu|(E)$ is not equal to $|\mu(E)|$.

It turns out, as will be proved below, that $|\mu|$ actually is a measure, so that our problem does have a solution. The discussion which led to (3) shows then clearly that $|\mu|$ is the minimal solution, in the sense that any other solution $\lambda$ has the property $\lambda(E) \geq|\mu|(E)$ for all $E \in \mathfrak{M}$.

The set function $|\mu|$ is called the total variation of $\mu$, or sometimes, to avoid misunderstanding, the total variation measure. The term "total variation of $\mu$ " is also frequently used to denote the number $|\mu|(X)$.

If $\mu$ is a positive measure, then of course $|\mu|=\mu$.

Besides being a measure, $|\mu|$ has another unexpected property: $|\mu|(X)<\infty$. Since $|\mu(E)| \leq|\mu|(E) \leq|\mu|(X)$, this implies that every complex measure $\mu$ on any $\sigma$-algebra is bounded: If the range of $\mu$ lies in the complex plane, then it actually lies in some disc of finite radius. This property (proved in Theorem 6.4) is sometimes expressed by saying that $\mu$ is of bounded variation.

6.2 Theorem The total variation $|\mu|$ of a complex measure $\mu$ on $\mathfrak{M}$ is a positive measure on $\mathfrak{M}$.

ProOF Let $\left\{E_{i}\right\}$ be a partition of $E \in \mathfrak{M}$. Let $t_{i}$ be real numbers such that $t_{i}<|\mu|\left(E_{i}\right)$. Then each $E_{i}$ has a partition $\left\{A_{i j}\right\}$ such that

$$
\sum_{j}\left|\mu\left(A_{i j}\right)\right|>t_{i} \quad(i=1,2,3, \ldots)
$$

Since $\left\{A_{i j}\right\}(i, j=1,2,3, \ldots)$ is a partition of $E$, it follows that

$$
\sum_{i} t_{i} \leq \sum_{i, j}\left|\mu\left(A_{i j}\right)\right| \leq|\mu|(E) .
$$

Taking the supremum of the left side of (2), over all admissible choices of $\left\{t_{i}\right\}$, we see that

$$
\sum_{i}|\mu|\left(E_{i}\right) \leq|\mu|(E) .
$$

To prove the opposite inequality, let $\left\{A_{j}\right\}$ be any partition of $E$. Then for any fixed $j,\left\{A_{j} \cap E_{i}\right\}$ is a partition of $A_{j}$, and for any fixed $i,\left\{A_{j} \cap E_{i}\right\}$ is a partition of $E_{i}$. Hence

$$
\begin{aligned}
\sum_{j}\left|\mu\left(A_{j}\right)\right| & =\sum_{j}\left|\sum_{i} \mu\left(A_{j} \cap E_{i}\right)\right| \\
& \leq \sum_{j} \sum_{i}\left|\mu\left(A_{j} \cap E_{i}\right)\right| \\
& =\sum_{i} \sum_{j}\left|\mu\left(A_{j} \cap E_{i}\right)\right| \leq \sum_{i}|\mu|\left(E_{i}\right) .
\end{aligned}
$$

Since (4) holds for every partition $\left\{A_{j}\right\}$ of $E$, we have

$$
|\mu|(E) \leq \sum_{i}|\mu|\left(E_{i}\right)
$$

By (3) and (5), $|\mu|$ is countably additive.

Note that the Corollary to Theorem 1.27 was used in (2) and (4).

That $|\mu|$ is not identically $\infty$ is a trivial consequence of Theorem 6.4 but can also be seen right now, since $|\mu|(\varnothing)=0$.

6.3 Lemma If $z_{1}, \ldots, z_{N}$ are complex numbers then there is a subset $S$ of $\{1, \ldots, N\}$ for which

$$
\left|\sum_{k \in S} z_{k}\right| \geq \frac{1}{\pi} \sum_{k=1}^{N}\left|z_{k}\right|
$$

ProOF Write $z_{k}=\left|z_{k}\right| e^{i \alpha_{k}}$. For $-\pi \leq \theta \leq \pi$, let $S(\theta)$ be the set of all $k$ for which $\cos \left(\alpha_{k}-\theta\right)>0$. Then

$$
\left|\sum_{S(\theta)} z_{k}\right|=\left|\sum_{S(\theta)} e^{-i \theta} z_{k}\right| \geq \operatorname{Re} \sum_{S(\theta)} e^{-i \theta} z_{k}=\sum_{k=1}^{N}\left|z_{k}\right| \cos ^{+}\left(\alpha_{k}-\theta\right)
$$

Choose $\theta_{0}$ so as to maximize the last sum, and put $S=S\left(\theta_{0}\right)$. This maximum is at least as large as the average of the sum over $[-\pi, \pi]$, and this average is $\pi^{-1} \sum\left|z_{k}\right|$, because

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \cos ^{+}(\alpha-\theta) d \theta=\frac{1}{\pi}
$$

for every $\alpha$.

6.4 Theorem If $\mu$ is a complex measure on $X$, then

$$
|\mu|(X)<\infty
$$

Proof Suppose first that some set $E \in \mathfrak{M}$ has $|\mu|(E)=\infty$. Put $t=\pi(1+|\mu(E)|)$. Since $|\mu|(E)>t$, there is a partition $\left\{E_{i}\right\}$ of $E$ such that

$$
\sum_{i=1}^{N}\left|\mu\left(E_{i}\right)\right|>t
$$

for some $N$. Apply Lemma 6.3 , with $z_{i}=\mu\left(E_{i}\right)$, to conclude that there is a set $A \subset E$ (a union of some of the sets $E_{i}$ ) for which

$$
|\mu(A)|>t / \pi>1
$$

Setting $B=E-A$, it follows that

$$
|\mu(B)|=|\mu(E)-\mu(A)| \geq|\mu(A)|-|\mu(E)|>\frac{t}{\pi}-|\mu(E)|=1
$$

We have thus split $E$ into disjoint sets $A$ and $B$ with $|\mu(A)|>1$ and $|\mu(B)|>1$. Evidently, at least one of $|\mu|(A)$ and $|\mu|(B)$ is $\infty$, by Theorem 6.2.

Now if $|\mu|(X)=\infty$, split $X$ into $A_{1}, B_{1}$, as above, with $\left|\mu\left(A_{1}\right)\right|>1$, $|\mu|\left(B_{1}\right)=\infty$. Split $B_{1}$ into $A_{2}, B_{2}$, with $\left|\mu\left(A_{2}\right)\right|>1,|\mu|\left(B_{2}\right)=\infty$. Continuing in this way, we get a countably infinite disjoint collection $\left\{A_{i}\right\}$, with $\left|\mu\left(A_{i}\right)\right|>1$ for each $i$. The countable additivity of $\mu$ implies that

$$
\mu\left(\bigcup_{i} A_{i}\right)=\sum_{i} \mu\left(A_{i}\right)
$$

But this series cannot converge, since $\mu\left(A_{i}\right)$ does not tend to 0 as $i \rightarrow \infty$. This contradiction shows that $|\mu|(X)<\infty$.

6.5 If $\mu$ and $\lambda$ are complex measures on the same $\sigma$-algebra $\mathfrak{M}$, we define $\mu+\lambda$ and $c \mu$ by

$$
\begin{aligned}
(\mu+\lambda)(E) & =\mu(E)+\lambda(E) \\
(c \mu)(E) & =c \mu(E)
\end{aligned}
$$

for any scalar $c$, in the usual manner. It is then trivial to verify that $\mu+\lambda$ and $c \mu$ are complex measures. The collection of all complex measures on $\mathfrak{M}$ is thus a vector space. If we put

$$
\|\mu\|=|\mu|(X)
$$

it is easy to verify that all axioms of a normed linear space are satisfied.

6.6 Positive and Negative Variations Let us now specialize and consider a real measure $\mu$ on a $\sigma$-algebra $\mathfrak{M}$. (Such measures are frequently called signed measures.) Define $|\mu|$ as before, and define

$$
\mu^{+}=\frac{1}{2}(|\mu|+\mu), \quad \mu^{-}=\frac{1}{2}(|\mu|-\mu)
$$

Then both $\mu^{+}$and $\mu^{-}$are positive measures on $\mathfrak{M}$, and they are bounded, by Theorem 6.4. Also,

$$
\mu=\mu^{+}-\mu^{-}, \quad|\mu|=\mu^{+}+\mu^{-} .
$$

The measures $\mu^{+}$and $\mu^{-}$are called the positive and negative variations of $\mu$, respectively. This representation of $\mu$ as the difference of the positive measures $\mu^{+}$ and $\mu^{-}$is known as the Jordan decomposition of $\mu$. Among all representations of $\mu$ as a difference of two positive measures, the Jordan decomposition has a certain minimum property which will be established as a corollary to Theorem 6.14 .

## Absolute Continuity

6.7 Definitions Let $\mu$ be a positive measure on a $\sigma$-algebra $\mathfrak{M}$, and let $\lambda$ be an arbitrary measure on $\mathfrak{M}$; $\lambda$ may be positive or complex. (Recall that a complex measure has its range in the complex plane, but that our usage of the term "positive measure" includes $\infty$ as an admissible value. Thus the positive measures do not form a subclass of the complex ones.)

We say that $\lambda$ is absolutely continuous with respect to $\mu$, and write

$$
\lambda \ll \mu
$$

if $\lambda(E)=0$ for every $E \in \mathfrak{M}$ for which $\mu(E)=0$.

If there is a set $A \in \mathfrak{M}$ such that $\lambda(E)=\lambda(A \cap E)$ for every $E \in \mathfrak{M}$, we say that $\lambda$ is concentrated on $A$. This is equivalent to the hypothesis that $\lambda(E)=0$ whenever $E \cap A=\varnothing$.

Suppose $\lambda_{1}$ and $\lambda_{2}$ are measures on $\mathfrak{M}$, and suppose there exists a pair of disjoint sets $A$ and $B$ such that $\lambda_{1}$ is concentrated on $A$ and $\lambda_{2}$ is concentrated on $B$. Then we say that $\lambda_{1}$ and $\lambda_{2}$ are mutually singular, and write

$$
\lambda_{1} \perp \lambda_{2} .
$$

Here are some elementary properties of these concepts.

6.8 Proposition Suppose, $\mu, \lambda, \lambda_{1}$, and $\lambda_{2}$ are measures on a $\sigma$-algebra $\mathfrak{M}$, and $\mu$ is positive.

(a) If $\lambda$ is concentrated on $A$, so is $|\lambda|$.

(b) If $\lambda_{1} \perp \lambda_{2}$, then $\left|\lambda_{1}\right| \perp\left|\lambda_{2}\right|$.

(c) If $\lambda_{1} \perp \mu$ and $\lambda_{2} \perp \mu$, then $\lambda_{1}+\lambda_{2} \perp \mu$.

(d) If $\lambda_{1} \ll \mu$ and $\lambda_{2} \ll \mu$, then $\lambda_{1}+\lambda_{2} \ll \mu$.

(e) If $\lambda \ll \mu$, then $|\lambda| \ll \mu$.

(f) If $\lambda_{1} \ll \mu$ and $\lambda_{2} \perp \mu$, then $\lambda_{1} \perp \lambda_{2}$.

(g) If $\lambda \ll \mu$ and $\lambda \perp \mu$, then $\lambda=0$.

## ProOF

(a) If $E \cap A=\varnothing$ and $\left\{E_{j}\right\}$ is any partition of $E$, then $\lambda\left(E_{j}\right)=0$ for all $j$. Hence $|\lambda|(E)=0$.

(b) This follows immediately from $(a)$.

(c) There are disjoint sets $A_{1}$ and $B_{1}$ such that $\lambda_{1}$ is concentrated on $A_{1}$ and $\mu$ on $B_{1}$, and there are disjoint sets $A_{2}$ and $B_{2}$ such that $\lambda_{2}$ is concentrated on $A_{2}$ and $\mu$ on $B_{2}$. Hence $\lambda_{1}+\lambda_{2}$ is concentrated on $A=A_{1} \cup$ $A_{2}, \mu$ is concentrated on $B=B_{1} \cap B_{2}$, and $A \cap B=\varnothing$.

(d) This is obvious.

(e) Suppose $\mu(E)=0$, and $\left\{E_{j}\right\}$ is a partition of $E$. Then $\mu\left(E_{j}\right)=0$; and since $\lambda \ll \mu, \lambda\left(E_{j}\right)=0$ for all $j$, hence $\sum\left|\lambda\left(E_{j}\right)\right|=0$. This implies $|\lambda|(E)=0$.
(f) Since $\lambda_{2} \perp \mu$, there is a set $A$ with $\mu(A)=0$ on which $\lambda_{2}$ is concentrated. Since $\lambda_{1} \ll \mu, \lambda_{1}(E)=0$ for every $E \subset A$. So $\lambda_{1}$ is concentrated on the complement of $A$.

(g) By $(f)$, the hypothesis of $(g)$ implies, that $\lambda \perp \lambda$, and this clearly forces $\lambda=0$.

We come now to the principal theorem about absolute continuity. In fact, it is probably the most important theorem in measure theory. Its statement will involve $\sigma$-finite measures. The following lemma describes one of their significant properties.

6.9 Lemma If $\mu$ is a positive $\sigma$-finite measure on a $\sigma$-algebra $\mathfrak{M}$ in a set $X$, then there is a function $w \in L^{1}(\mu)$ such that $0<w(x)<1$ for every $x \in X$.

Proof To say that $\mu$ is $\sigma$-finite means that $X$ is the union of countably many sets $E_{n} \in \mathfrak{M}(n=1,2,3, \ldots)$ for which $\mu\left(E_{n}\right)$ is finite. Put $w_{n}(x)=0$ if $x \in$ $X-E_{n}$ and put

$$
w_{n}(x)=2^{-n} /\left(1+\mu\left(E_{n}\right)\right)
$$

if $x \in E_{n}$. Then $w=\sum_{1}^{\infty} w_{n}$ has the required properties.

The point of the lemma is that $\mu$ can be replaced by a finite measure $\tilde{\mu}$ (namely, $d \tilde{\mu}=w d \mu$ ) which, because of the strict positivity of $w$, has precisely the same sets of measure 0 as $\mu$.

6.10 The Theorem of Lebesgue-Radon-Nikodym Let $\mu$ be a positive $\sigma$-finite measure on a $\sigma$-algebra $\mathfrak{M}$ in a set $X$, and let $\lambda$ be a complex measure on $\mathfrak{M}$.

(a) There is then a unique pair of complex measures $\lambda_{a}$ and $\lambda_{s}$ on $\mathfrak{M}$ such that

$$
\lambda=\lambda_{a}+\lambda_{s}, \quad \lambda_{a} \ll \mu, \quad \lambda_{s} \perp \mu .
$$

If $\lambda$ is positive and finite, then so are $\lambda_{a}$ and $\lambda_{s}$.

(b) There is a unique $h \in L^{1}(\mu)$ such that

$$
\lambda_{a}(E)=\int_{E} h d \mu
$$

for every set $\boldsymbol{E} \in \mathfrak{M}$.

The pair $\left(\lambda_{a}, \lambda_{s}\right)$ is called the Lebesgue decomposition of $\lambda$ relative to $\mu$. The uniqueness of the decomposition is easily seen, for if $\left(\lambda_{a}^{\prime}, \lambda_{s}^{\prime}\right)$ is another pair which satisfies (1), then

$$
\lambda_{a}^{\prime}-\lambda_{a}=\lambda_{s}-\lambda_{s}^{\prime}
$$

$\lambda_{a}^{\prime}-\lambda_{\alpha} \ll \mu$, and $\lambda_{s}-\lambda_{s}^{\prime} \perp \mu$, hence both sides of (3) are 0 ; we have used 6.8(c), $6.8(d)$, and $6.8(g)$.

The existence of the decomposition is the significant part of $(a)$.

Assertion (b). is known as the Radon-Nikodym theorem. Again, uniqueness of $h$ is immediate, from Theorem $1.39(b)$. Also, if $h$ is any member of $L^{1}(\mu)$, the integral in (2) defines a measure on $\mathfrak{M}$ (Theorem 1.29) which is clearly absolutely continuous with respect to $\mu$. The point of the Radon-Nikodym theorem is the converse: Every $\lambda \ll \mu$ (in which case $\lambda_{a}=\lambda$ ) is obtained in this way.

The function $h$ which occurs in (2) is called the Radon-Nikodym derivative of $\lambda_{a}$ with respect to $\mu$. As noted after Theorem 1.29, we may express (2) in the form $d \lambda_{a}=h d \mu$, or even in the form $h=d \lambda_{a} / d \mu$.

The idea of the following proof, which yields both $(a)$ and $(b)$ at one stroke, is due to von Neumann.

Proof Assume first that $\lambda$ is a positive bounded measure on $\mathfrak{M}$. Associate $w$ to $\mu$ as in Lemma 6.9. Then $d \varphi=d \lambda+w d \mu$ defines a positive bounded measure $\varphi$ on $\mathfrak{M}$. The definition of the sum of two measures shows that

$$
\int_{X} f d \varphi=\int_{X} f d \lambda+\int_{X} f w d \mu
$$

for $f=\chi_{E}$, hence for simple $f$, hence for any nonnegative measurable $f$. If $f \in L^{2}(\varphi)$, the Schwarz inequality gives

$$
\left|\int_{X} f d \lambda\right| \leq \int_{X}|f| d \lambda \leq \int_{X}|f| d \varphi \leq\left\{\int_{X}|f|^{2} d \varphi\right\}^{1 / 2}\{\varphi(X)\}^{1 / 2}
$$

Since $\varphi(X)<\infty$, we see that

$$
f \rightarrow \int_{X} f d \lambda
$$

is a bounded linear functional on $L^{2}(\varphi)$. We know that every bounded linear functional on a Hilbert space $H$ is given by an inner product with an element of $H$. Hence there exists a $g \in L^{2}(\varphi)$ such that

$$
\int_{X} f d \lambda=\int_{X} f g d \varphi
$$

for every $f \in L^{2}(\varphi)$.

Observe how the completeness of $L^{2}(\varphi)$ was used to guarantee the existence of $g$. Observe also that although $g$ is defined uniquely as an element of $L^{2}(\varphi), g$ is determined only a.e. $[\varphi]$ as a point function on $X$.

Put $f=\chi_{E}$ in (6), for any $E \in \mathfrak{M}$ with $\varphi(E)>0$. The left side of (6) is then $\lambda(E)$, and since $0 \leq \lambda \leq \varphi$, we have

$$
0 \leq \frac{1}{\varphi(E)} \int_{E} g d \varphi=\frac{\lambda(E)}{\varphi(E)} \leq 1
$$

Hence $g(x) \in[0,1]$ for almost all $x$ (with respect to $\varphi$ ), by Theorem 1.40. We may therefore assume that $0 \leq g(x) \leq 1$ for every $x \in X$, without affecting (6), and we rewrite (6) in the form

$$
\int_{X}(1-g) f d \lambda=\int_{X} f g w d \mu
$$

Put

$$
A=\{x: 0 \leq g(x)<1\}, \quad B=\{x: g(x)=1\}
$$

and define measures $\lambda_{a}$ and $\lambda_{s}$ by

$$
\lambda_{a}(E)=\lambda(A \cap E), \quad \lambda_{s}(E)=\lambda(B \cap E)
$$

for all $E \in \mathfrak{M}$.

If $f=\chi_{B}$ in (8), the left side is 0 , the right side is $\int_{B} w d \mu$. Since $w(x)>0$ for all $x$, we conclude that $\mu(B)=0$. Thus $\lambda_{s} \perp \mu$.

Since $g$ is bounded, (8) holds if $f$ is replaced by

$$
\left(1+g+\cdots+g^{n}\right) \chi_{E}
$$

for $n=1,2,3, \ldots, E \in \mathfrak{M}$. For $\operatorname{such} f,(8)$ becomes

$$
\int_{E}\left(1-g^{n+1}\right) d \lambda=\int_{E} g\left(1+g+\cdots+g^{n}\right) w d \mu
$$

At every point of $B, g(x)=1$, hence $1-g^{n+1}(x)=0$. At every point of $A$, $g^{n+1}(x) \rightarrow 0$ monotonically. The left side of (11) converges therefore to $\lambda(A \cap E)=\lambda_{a}(E)$ as $n \rightarrow \infty$.

The integrands on the right side of (11) increase monotonically to a nonnegative measurable limit $h$, and the monotone convergence theorem shows that the right side of (11) tends to $\int_{E} h d \mu$ as $n \rightarrow \infty$.

We have thus proved that (2) holds for every $E \in \mathfrak{M}$. Taking $E=X$, we see that $h \in L^{1}(\mu)$, since $\lambda_{a}(X)<\infty$.

Finally, (2) shows that $\lambda_{a} \ll \mu$, and the proof is complete for positive $\lambda$.

If $\lambda$ is a complex measure on $\mathfrak{M}$, then $\lambda=\lambda_{1}+i \lambda_{2}$, with $\lambda_{1}$ and $\lambda_{2}$ real, and we can apply the preceding case to the positive and negative variations of $\lambda_{1}$ and $\lambda_{2}$.

If both $\mu$ and $\lambda$ are positive and $\sigma$-finite, most of Theorem 6.10 is still true. We can now write $X=\bigcup X_{n}$, where $\mu\left(X_{n}\right)<\infty$ and $\lambda\left(X_{n}\right)<\infty$, for $n=1,2,3$, The Lebesgue decompositions of the measures $\lambda\left(E \cap X_{n}\right)$ still give us a Lebesgue decomposition of $\lambda$, and we still get a function $h$ which satisfies Eq. 6.10(2); however, it is no longer true that $h \in L^{1}(\mu)$, although $h$ is "locally in $L^{1}$," i.e., $\int_{X_{n}} h d \mu<\infty$ for each $n$.

Finally, if we go beyond $\sigma$-finiteness, we meet situations where the two theorems under consideration actually fail. For example, let $\mu$ be Lebesgue measure on $(0,1)$, and let $\lambda$ be the counting measure on the $\sigma$-algebra of all Lebesgue
measurable sets in $(0,1)$. Then $\lambda$ has no Lebesgue decomposition relative to $\mu$, and although $\mu \ll \lambda$ and $\mu$ is bounded, there is no $h \in L^{1}(\lambda)$ such that $d \mu=h d \lambda$. We omit the easy proof.

The following theorem may explain why the word "continuity" is used in connection with the relation $\lambda \ll \mu$.

6.11 Theorem Suppose $\mu$ and $\lambda$ are measures on a $\sigma$-algebra $\mathfrak{M}, \mu$ is positive, and $\lambda$ is complex. Then the following two conditions are equivalent:

(a) $\lambda \ll \mu$.

(b) To every $\epsilon>0$ corresponds a $\delta>0$ such that $|\lambda(E)|<\epsilon$ for all $E \in \mathfrak{M}$ with $\mu(E)<\delta$.

Property $(b)$ is sometimes used as the definition of absolute continuity. However, $(a)$ does not imply $(b)$ if $\lambda$ is a positive unbounded measure. For instance, let $\mu$ be Lebesgue measure on $(0,1)$, and put

$$
\lambda(E)=\int_{E} t^{-1} d t
$$

for every Lebesgue measurable set $E \subset(0,1)$.

Proof Suppose $(b)$ holds. If $\mu(E)=0$, then $\mu(E)<\delta$ for every $\delta>0$, hence $|\lambda(E)|<\epsilon$ for every $\epsilon>0$, so $\lambda(E)=0$. Thus $(b)$ implies $(a)$.

Suppose $(b)$ is false. Then there exists an $\epsilon>0$ and there exist sets $E_{n} \in$ $\mathfrak{M}(n=1,2,3, \ldots)$ such that $\mu\left(E_{n}\right)<2^{-n}$ but $\left|\lambda\left(E_{n}\right)\right| \geq \epsilon$. Hence $|\lambda|\left(E_{n}\right) \geq \epsilon$. Put

$$
A_{n}=\bigcup_{i=n}^{\infty} E_{i}, \quad A=\bigcap_{n=1}^{\infty} A_{n}
$$

Then $\mu\left(A_{n}\right)<2^{-n+1}, A_{n} \supset A_{n+1}$, and so Theorem 1.19(e) shows that $\mu(A)=0$ and that

$$
|\lambda|(A)=\lim _{n \rightarrow \infty}|\lambda|\left(A_{n}\right) \geq \epsilon>0
$$

since $|\lambda|\left(A_{n}\right) \geq|\lambda|\left(E_{n}\right)$.

It follows that we do not have $|\lambda| \ll \mu$, hence $(a)$ is false, by Proposition 6.8(e).

## Consequences of the Radon-Nikodym Theorem

6.12 Theorem Let $\mu$ be a complex measure on a $\sigma$-algebra $\mathfrak{M}$ in $X$. Then there is a measurable function $h$ such that $|h(x)|=1$ for all $x \in X$ and such that

$$
d \mu=h d|\mu|
$$

By analogy with the representation of a complex number as the product of ts absolute value and a number of absolute value 1, Eq. (1) is sometimes referred $\mathrm{o}$ as the polar representation (or polar decomposition) of $\mu$.

Proof It is trivial that $\mu \ll|\mu|$, and therefore the Radon-Nikodym theorem guarantees the existence of some $h \in L^{1}(|\mu|)$ which satisfies (1).

Let $A_{r}=\{x:|h(x)|<r\}$, where $r$ is some positive number, and let $\left\{E_{j}\right\}$ be a partition of $A_{r}$. Then

$$
\sum_{j}\left|\mu\left(E_{j}\right)\right|=\sum_{j}\left|\int_{E_{j}} h d\right| \mu|| \leq \sum_{j} r|\mu|\left(E_{j}\right)=r|\mu|\left(A_{r}\right)
$$

so that $|\mu|\left(A_{r}\right) \leq r|\mu|\left(A_{r}\right)$. If $r<1$, this forces $|\mu|\left(A_{r}\right)=0$. Thus $|h| \geq 1$ a.e.

On the other hand, if $|\mu|(E)>0$, (1) shows that

$$
\left|\frac{1}{|\mu|(E)} \int_{E} h d\right| \mu||=\frac{|\mu(E)|}{|\mu|(E)} \leq 1
$$

We now apply Theorem 1.40 (with the closed unit disc in place of $S$ ) and conclude that $|h| \leq 1$ a.e.

Let $B=\{x \in X:|h(x)| \neq 1\}$. We have shown that $|\mu|(B)=0$, and if we redefine $h$ on $B$ so that $h(x)=1$ on $B$, we obtain a function with the desired properties.

6.13 Theorem Suppose $\mu$ is a positive measure on $\mathfrak{M}, g \in L^{1}(\mu)$, and

$$
\lambda(E)=\int_{E} g d \mu \quad(E \in \mathfrak{M})
$$

Then

$$
|\lambda|(E)=\int_{E}|g| d \mu \quad(E \in \mathfrak{M})
$$

Proof By Theorem 6.12, there is a function $h$, of absolute value 1, such that $d \lambda=h d|\lambda|$. By hypothesis, $d \lambda=g d \mu$. Hence

$$
h d|\lambda|=g d \mu
$$

This gives $d|\lambda|=\bar{h} g d \mu$. (Compare with Theorem 1.29.)

Since $|\lambda| \geq 0$ and $\mu \geq 0$, it follows that $\bar{h} g \geq 0$ a.e. $[\mu]$, so that $\bar{h} g=|g|$ a.e. $[\mu]$.

6.14 The Hahn Decomposition Theorem Let $\mu$ be a real measure on a $\sigma$ algebra $\mathfrak{M}$ in a set $X$. Then there exist sets $A$ and $B \in \mathfrak{M}$ such that
$A \cup B=X, A \cap B=\varnothing$, and such that the positive and negative variations $\mu^{+}$and $\mu^{-}$of $\mu$ satisfy

$$
\mu^{+}(E)=\mu(A \cap E), \quad \mu^{-}(E)=-\mu(B \cap E) \quad(E \in \mathfrak{M})
$$

In other words, $X$ is the union of two disjoint measurable sets $A$ and $B$, such that " $A$ carries all the positive mass of $\mu$ " [since (1) implies that $\mu(E) \geq 0$ if $E \subset A]$ and " $B$ carries all the negative mass of $\mu$ " [since $\mu(E) \leq 0$ if $E \subset B]$. The pair $(A, B)$ is called a Hahn decomposition of $X$, induced by $\mu$.

ProOf By Theorem 6.12, $d \mu=h d|\mu|$, where $|h|=1$. Since $\mu$ is real, it follows that $h$ is real (a.e., and therefore everywhere, by redefining on a set of measure 0 ), hence $h= \pm 1$. Put

$$
A=\{x: h(x)=1\}, \quad B=\{x: h(x)=-1\} .
$$

Since $\mu^{+}=\frac{1}{2}(|\mu|+\mu)$, and since

$$
\frac{1}{2}(1+h)= \begin{cases}h & \text { on } A \\ 0 & \text { on } B\end{cases}
$$

we have, for any $E \in \mathfrak{M}$,

$$
\mu^{+}(E)=\frac{1}{2} \int_{E}(1+h) d|\mu|=\int_{E \cap A} h d|\mu|=\mu(E \cap A)
$$

Since $\mu(E)=\mu(E \cap A)+\mu(E \cap B)$ and since $\mu=\mu^{+}-\mu^{-}$, the second half of (1) follows from the first.

Corollary If $\mu=\lambda_{1}-\lambda_{2}$, where $\lambda_{1}$ and $\lambda_{2}$ are positive measures, then $\lambda_{1} \geq \mu^{+}$ and $\lambda_{2} \geq \mu^{-}$.

This is the minimum property of the Jordan decomposition which was mentioned in Sec. 6.6.

Proof Since $\mu \leq \lambda_{1}$, we have

$$
\mu^{+}(E)=\mu(E \cap A) \leq \lambda_{1}(E \cap A) \leq \lambda_{1}(E)
$$

## Bounded Linear Functionals on $L^{p}$

6.15 Let $\mu$ be a positive measure, suppose $1 \leq p \leq \infty$, and let $q$ be the exponent conjugate to $p$. The Hölder inequality (Theorem 3.8) shows that if $g \in L^{q}(\mu)$ and if $\Phi_{g}$ is defined by

$$
\Phi_{g}(f)=\int_{X} f g d \mu
$$

then $\Phi_{g}$ is a bounded linear functional on $L^{p}(\mu)$, of norm at most $\|g\|_{q}$. The question naturally arises whether all bounded linear functionals on $L^{p}(\mu)$ have this form, and whether the representation is unique.

For $p=\infty$, Exercise 13 shows that the answer is negative: $L^{1}(m)$ does not furnish all bounded linear functionals on $L^{\infty}(m)$. For $1<p<\infty$, the answer is affirmative. It is also affirmative for $p=1$, provided certain measure-theoretic pathologies are excluded. For $\sigma$-finite measure spaces, no difficulties arise, and we shall confine ourselves to this case.

6.16 Theorem Suppose $1 \leq p<\infty, \mu$ is a $\sigma$-finite positive measure on $X$, and $\Phi$ is a bounded linear functional on $L^{p}(\mu)$. Then there is a unique $g \in L^{q}(\mu)$, where $q$ is the exponent conjugate to $p$, such that

$$
\Phi(f)=\int_{x} f g d \mu \quad\left(f \in L^{p}(\mu)\right)
$$

Moreover, if $\Phi$ and $g$ are related as in (1), we have

$$
\|\Phi\|=\|g\|_{q} \text {. }
$$

In other words, $L^{q}(\mu)$ is isometrically isomorphic to the dual space of $L^{p}(\mu)$, under the stated conditions.

Proof The uniqueness of $g$ is clear, for if $g$ and $g^{\prime}$ satisfy (1), then the integral of $g-g^{\prime}$ over any measurable set $E$ of finite measure is 0 (as we see by taking $\chi_{E}$ for $f$ ), and the $\sigma$-finiteness of $\mu$ implies therefore that $g-g^{\prime}=0$ a.e.

Next, if (1) holds, Hölder's inequality implies

$$
\|\Phi\| \leq\|g\|_{q} .
$$

So it remains to prove that $g$ exists and that equality holds in (3). If $\|\Phi\|=0$, (1) and (2) hold with $g=0$. So assume $\|\Phi\|>0$.

We first consider the case $\mu(X)<\infty$.

For any measurable set $E \subset X$, define

$$
\lambda(E)=\Phi\left(\chi_{E}\right) .
$$

Since $\Phi$ is linear, and since $\chi_{A \cup B}=\chi_{A}+\chi_{B}$ if $A$ and $B$ are disjoint, we see that $\lambda$ is additive. To prove countable additivity, suppose $E$ is the union of countably many disjoint measurable sets $E_{i}$, put $A_{k}=E_{1} \cup \cdots \cup E_{k}$, and note that

$$
\left\|\chi_{E}-\chi_{A_{k}}\right\|_{p}=\left[\mu\left(E-A_{k}\right)\right]^{1 / p} \rightarrow 0 \quad(k \rightarrow \infty)
$$

the continuity of $\Phi$ shows now that $\lambda\left(A_{k}\right) \rightarrow \lambda(E)$. So $\lambda$ is a complex measure. [In (4) the assumption $p<\infty$ was used.] It is clear that $\lambda(E)=0$ if $\mu(E)=0$,
since then $\left\|\chi_{E}\right\|_{p}=0$. Thus $\lambda \ll \mu$, and the Radon-Nikodym theorem ensures the existence of a function $g \in L^{1}(\mu)$ such that, for every measurable $E \subset X$,

$$
\Phi\left(\chi_{E}\right)=\int_{E} g d \mu=\int_{X} \chi_{E} g d \mu
$$

By linearity it follows that

$$
\Phi(f)=\int_{X} f g d \mu
$$

holds for every simple measurable $f$, and so also for every $f \in L^{\infty}(\mu)$, since every $f \in L^{\infty}(\mu)$ is a uniform limit of simple functions $f_{i}$. Note that the uniform convergence of $f_{i}$ to $f$ implies $\left\|f_{i}-f\right\|_{p} \rightarrow 0$, hence $\Phi\left(f_{i}\right) \rightarrow \Phi(f)$, as $i \rightarrow \infty$.

We want to conclude that $g \in L^{q}(\mu)$ and that (2) holds; it is best to split the argument into two cases.

CASE $1 p=1$. Here (5) shows that

$$
\left|\int_{E} g d \mu\right| \leq\|\Phi\| \cdot\left\|\chi_{E}\right\|_{1}=\|\Phi\| \cdot \mu(E)
$$

for every $E \in \mathfrak{M}$. By Theorem 1.40, $|g(x)| \leq\|\Phi\|$ a.e., so that $\|g\|_{\infty} \leq\|\Phi\|$.

CASE $21<p<\infty$. There is a measurable function $\alpha,|\alpha|=1$, such that $\alpha g=|g|$ [Proposition 1.9(e)]. Let $E_{n}=\{x:|g(x)| \leq n\}$, and define $f=$ $\chi_{E_{n}}|g|^{q-1} \alpha$. Then $|f|^{p}=|g|^{q}$ on $E_{n}, f \in L^{\infty}(\mu)$, and (6) gives

$$
\int_{E_{n}}|g|^{q} d \mu=\int_{X} f g d \mu=\Phi(f) \leq\|\Phi\|\left\{\int_{E_{n}}|g|^{q}\right\}^{1 / p},
$$

so that

$$
\int_{X} \chi_{E_{n}}|g|^{q} d \mu \leq\|\Phi\|^{q} \quad(n=1,2,3, \ldots)
$$

If we apply the monotone convergence theorem to (7), we obtain $\|g\|_{a} \leq\|\Phi\|$.

Thus (2) holds and $g \in L^{q}(\mu)$. It follows that both sides of (6) are continuous functions on $L^{p}(\mu)$. They coincide on the dense subset $L^{\infty}(\mu)$ of $L^{p}(\mu)$; hence they coincide on all of $L^{p}(\mu)$, and this completes the proof if $\mu(X)<\infty$.

If $\mu(X)=\infty$ but $\mu$ is $\sigma$-finite, choose $w \in L^{1}(\mu)$ as in Lemma 6.9. Then $d \tilde{\mu}=w d \mu$ defines a finite measure on $\mathfrak{M}$, and

$$
F \rightarrow w^{1 / p} F
$$

is a linear isometry of $L^{p}(\tilde{\mu})$ onto $L^{p}(\mu)$, because $w(x)>0$ for every $x \in X$. Hence

$$
\Psi(F)=\Phi\left(w^{1 / p} F\right)
$$

defines a bounded linear functional $\Psi$ on $L^{p}(\tilde{\mu})$, with $\|\Psi\|=\|\Phi\|$.

The first part of the proof shows now that there exists $G \in L^{q}(\tilde{\mu})$ such that

$$
\Psi(F)=\int_{X} F G d \tilde{\mu} \quad\left(F \in L^{p}(\tilde{\mu})\right)
$$

Put $g=w^{1 / q} G$. (If $p=1, g=G$.) Then

$$
\int_{X}|g|^{q} d \mu=\int_{X}|G|^{q} d \tilde{\mu}=\|\Psi\|^{q}=\|\Phi\|^{q}
$$

if $p>1$, whereas $\|g\|_{\infty}=\|G\|_{\infty}=\|\Psi\|=\|\Phi\|$ if $p=1$. Thus (2) holds, and since $G d \tilde{\mu}=w^{1 / p} g d \mu$, we finally get

$$
\Phi(f)=\Psi\left(w^{-1 / p} f\right)=\int_{X} w^{-1 / p} f G d \tilde{\mu}=\int_{X} f g d \mu
$$

for every $f \in L^{p}(\mu)$.

6.17 Remark We have already encountered the special case $p=q=2$ of Theorem 6.16. In fact, the proof of the general case was based on this special case, for we used the knowledge of the bounded linear functionals on $L^{2}(\mu)$ in the proof of the Radon-Nikodym theorem, and the latter was the key to the proof of Theorem 6.16. The special case $p=2$, in turn, depended on the completeness of $L^{2}(\mu)$, on the fact that $L^{2}(\mu)$ is therefore a Hilbert space, and on the fact that the bounded linear functionals on a Hilbert space are given by inner products.

We now turn to the complex version of Theorem 2.14.

## The Riesz Representation Theorem

6.18 Let $X$ be a locally compact Hausdorff space. Theorem 2.14 characterizes the positive linear functionals on $C_{c}(X)$. We are now in a position to characterize the bounded linear functionals $\Phi$ on $C_{c}(X)$. Since $C_{c}(X)$ is a dense subspace of $C_{0}(X)$, relative to the supremum norm, every such $\Phi$ has a unique extension to a bounded linear functional on $C_{0}(X)$. Hence we may as well assume to begin with that we are dealing with the Banach space $C_{0}(X)$.

If $\mu$ is a complex Borel measure, Theorem 6.12 asserts that there is a complex Borel function $h$ with $|h|=1$ such that $d \mu=h d|\mu|$. It is therefore reasonable to lefine integration with respect to a complex measure $\mu$ by the formula

$$
\int f d \mu=\int f h d|\mu|
$$

The relation $\int \chi_{E} d \mu=\mu(E)$ is a special case of (1). Thus

$$
\int_{X} \chi_{E} d(\mu+\lambda)=(\mu+\lambda)(E)=\mu(E)+\lambda(E)=\int_{X} \chi_{E} d \mu+\int_{X} \chi_{E} d \lambda
$$

whenever $\mu$ and $\lambda$ are complex measures on $\mathfrak{M}$ and $E \in \mathfrak{M}$. This leads to the addition formula

$$
\int_{X} f d(\mu+\lambda)=\int_{X} f d \mu+\int_{X} f d \lambda
$$

which is valid (for instance) for every bounded measurable $f$.

We shall call a complex Borel measure $\mu$ on $X$ regular if $|\mu|$ is regular in the sense of Definition 2.15. If $\mu$ is a complex Borel measure on $X$, it is clear that the mapping

$$
f \rightarrow \int_{X} f d \mu
$$

is a bounded linear functional on $C_{0}(X)$, whose norm is no larger than $|\mu|(X)$. That all bounded linear functionals on $C_{0}(X)$ are obtained in this way is the content of the Riesz theorem:

6.19 Theorem If $X$ is a locally compact Hausdorff space, then every bounded linear functional $\Phi$ on $C_{0}(X)$ is represented by a unique regular complex Borel measure $\mu$, in the sense that

$$
\Phi f=\int_{X} f d \mu
$$

for every $f \in C_{0}(X)$. Moreover, the norm of $\Phi$ is the total variation of $\mu$ :

$$
\|\Phi\|=|\mu|(X)
$$

Proof We first settle the uniqueness question. Suppose $\mu$ is a regular complex Borel measure on $X$ and $\int f d \mu=0$ for all $f \in C_{0}(X)$. By Theorem 6.12 there is a Borel function $h$, with $|h|=1$, such that $d \mu=h d|\mu|$. For any sequence $\left\{f_{n}\right\}$ in $C_{0}(X)$ we then have

$$
|\mu|(X)=\int_{X}\left(\bar{h}-f_{n}\right) h d|\mu| \leq \int_{X}\left|\bar{h}-f_{n}\right| d|\mu|
$$

and since $C_{c}(X)$ is dense in $L^{1}(|\mu|)$ (Theorem 3.14), $\left\{f_{n}\right\}$ can be so chosen that the last expression in (3) tends to 0 as $n \rightarrow \infty$. Thus $|\mu|(X)=0$, and $\mu=0$. It is easy to see that the difference of two regular complex Borel measures on $X$ is regular. This shows that at most one $\mu$ corresponds to each $\Phi$.

Now consider a given bounded linear functional $\Phi$ on $C_{0}(X)$. Assume $\|\Phi\|=1$, without loss of generality. We shall construct a positive linear functional $\Lambda$ on $C_{c}(X)$, such that

$$
|\Phi(f)| \leq \Lambda(|f|) \leq\|f\| \quad\left(f \in C_{c}(X)\right)
$$

where $\|f\|$ denotes the supremum norm.

Once we have this $\Lambda$, we associate with it a positive Borel measure $\lambda$, as in Theorem 2.14. The conclusion of Theorem 2.14 shows that $\lambda$ is regular if $\lambda(X)<\infty$. Since

$$
\lambda(X)=\sup \left\{\Lambda f: 0 \leq f \leq 1, f \in C_{c}(X)\right\}
$$

and since $|\Lambda f| \leq 1$ if $\|f\| \leq 1$, we see that actually $\lambda(X) \leq 1$.

We also deduce from (4) that

$$
|\Phi(f)| \leq \Lambda(|f|)=\int_{X}|f| d \lambda=\|f\|_{1} \quad\left(f \in C_{c}(X)\right)
$$

The last norm refers to the space $L^{1}(\lambda)$. Thus $\Phi$ is a linear functional on $C_{c}(X)$ of norm at most 1 , with respect to the $L^{1}(\lambda)$-norm on $C_{c}(X)$. There is a normpreserving extension of $\Phi$ to a linear functional on $L^{1}(\lambda)$, and therefore Theorem 6.16 (the case $p=1$ ) gives a Borel function $g$, with $|g| \leq 1$, such that

$$
\Phi(f)=\int_{X} f g d \lambda \quad\left(f \in C_{c}(X)\right)
$$

Each side of (6) is a continuous functional on $C_{0}(X)$, and $C_{c}(X)$ is dense in $C_{0}(X)$. Hence (6) holds for all $f \in C_{0}(X)$, and we obtain the representation (1) with $d \mu=g d \lambda$.

Since $\|\Phi\|=1,(6)$ shows that

$$
\int_{X}|g| d \lambda \geq \sup \left\{|\Phi(f)|: f \in C_{0}(X),\|f\| \leq 1\right\}=1
$$

We also know that $\lambda(X) \leq 1$ and $|g| \leq 1$. These facts are compatible only if $\lambda(X)=1$ and $|g|=1$ a.e. [ $\lambda$ ]. Thus $d|\mu|=|g| d \lambda=d \lambda$, by Theorem 6.13, and

$$
|\mu|(X)=\lambda(X)=1=\|\Phi\|
$$

which proves (2).

So all depends on finding a positive linear functional $\Lambda$ that satisfies (4). If $f \in C_{c}^{+}(X)$ [the class of all nonnegative real members of $\left.C_{c}(X)\right]$, define

$$
\Lambda f=\sup \left\{|\Phi(h)|: h \in C_{c}(X),|h| \leq f\right\} .
$$

Then $\Lambda f \geq 0, \Lambda$ satisfies (4), $0 \leq f_{1} \leq f_{2}$ implies $\Lambda f_{1} \leq \Lambda f_{2}$, and $\Lambda(c f)=c \Lambda f$ if $c$ is a positive constant. We have to show that

$$
\Lambda(f+g)=\Lambda f+\Lambda g \quad\left(f \text { and } g \in C_{c}^{+}(X)\right)
$$

and we then have to extend $\Lambda$ to a linear functional on $C_{c}(X)$.

Fix $f$ and $g \in C_{c}^{+}(X)$. If $\epsilon>0$, there exist $h_{1}$ and $h_{2} \in C_{c}(X)$ such that $\left|h_{1}\right| \leq f,\left|h_{2}\right| \leq g$, and

$$
\Lambda f \leq\left|\Phi\left(h_{1}\right)\right|+\epsilon, \quad \Lambda g \leq\left|\Phi\left(h_{2}\right)\right|+\epsilon .
$$

There are complex numbers $\alpha_{i},\left|\alpha_{i}\right|=1$, so that $\alpha_{i} \Phi\left(h_{i}\right)=\left|\Phi\left(h_{i}\right)\right|, i=1,2$. Then

$$
\begin{aligned}
\Lambda f+\Lambda g & \leq\left|\Phi\left(h_{1}\right)\right|+\left|\Phi\left(h_{2}\right)\right|+2 \epsilon \\
& =\Phi\left(\alpha_{1} h_{1}+\alpha_{2} h_{2}\right)+2 \epsilon \\
& \leq \Lambda\left(\left|h_{1}\right|+\left|h_{2}\right|\right)+2 \epsilon \\
& \leq \Lambda(f+g)+2 \epsilon,
\end{aligned}
$$

so that the inequality $\geq$ holds in (10).

Next, choose $h \in C_{c}(X)$, subject only to the condition $|h| \leq f+g$, let $V=\{x: f(x)+g(x)>0\}$, and define

$$
\begin{aligned}
& h_{1}(x)=\frac{f(x) h(x)}{f(x)+g(x)}, \quad h_{2}(x)=\frac{g(x) h(x)}{f(x)+g(x)} \quad(x \in V), \\
& h_{1}(x)=h_{2}(x)=0 \quad(x \notin V) .
\end{aligned}
$$

It is clear that $h_{1}$ is continuous at every point of $V$. If $x_{0} \notin V$, then $h\left(x_{0}\right)=0$; since $h$ is continuous and since $\left|h_{1}(x)\right| \leq|h(x)|$ for all $x \in X$, it follows that $x_{0}$ is a point of continuity of $h_{1}$. Thus $h_{1} \in C_{c}(X)$, and the same holds for $h_{2}$.

Since $h_{1}+h_{2}=h$ and $\left|h_{1}\right| \leq f,\left|h_{2}\right| \leq g$, we have

$$
|\Phi(h)|=\left|\Phi\left(h_{1}\right)+\Phi\left(h_{2}\right)\right| \leq\left|\Phi\left(h_{1}\right)\right|+\left|\Phi\left(h_{2}\right)\right| \leq \Lambda f+\Lambda g .
$$

Hence $\Lambda(f+g) \leq \Lambda f+\Lambda g$, and we have proved (10).

If $f$ is now a real function, $f \in C_{c}(X)$, then $2 f^{+}=|f|+f$, so that $f^{+} \in$ $C_{c}^{+}(X)$; likewise, $f^{-} \in C_{c}^{+}(X)$; and since $f=f^{+}-f^{-}$, it is natural to define

$$
\Lambda f=\Lambda f^{+}-\Lambda f^{-} \quad\left(f \in C_{c}(X), f \text { real }\right)
$$

and

$$
\Lambda(u+i v)=\Lambda u+i \Lambda v .
$$

Simple algebraic manipulations, just like those which occur in the proof of Theorem 1.32, show now that our extended functional $\Lambda$ is linear on $C_{c}(X)$. This completes the proof.

## Exercises

1 If $\mu$ is a complex measure on a $\sigma$-algebra $\mathfrak{M}$, and if $E \in \mathfrak{M}$, define

$$
\lambda(E)=\sup \sum\left|\mu\left(E_{i}\right)\right|
$$

the supremum being taken over all finite partitions $\left\{E_{i}\right\}$ of $E$. Does it follow that $\lambda=|\mu|$ ?

2 Prove that the example given at the end of Sec. 6.10 has the stated properties.

3 Prove that the vector space $M(X)$ of all complex regular Borel measures on a locally compact Hausdorff space $X$ is a Banach space if $\|\mu\|=|\mu|(X)$. Hint: Compare Exercise 8, Chap. 5. [That the difference of any two members of $M(X)$ is in $M(X)$ was used in the first paragraph of the proof of Theorem 6.19 ; supply a proof of this fact.]

4 Suppose $1 \leq p \leq \infty$, and $q$ is the exponent conjugate to $p$. Suppose $\mu$ is a positive $\sigma$-finite measure and $g$ is a measurable function such that $f g \in L^{1}(\mu)$ for every $f \in L^{p}(\mu)$. Prove that then $g \in L^{q}(\mu)$.

5 Suppose $X$ consists of two points $a$ and $b$; define $\mu(\{a\})=1, \mu(\{b\})=\mu(X)=\infty$, and $\mu(\varnothing)=0$. Is it true, for this $\mu$, that $L^{\infty}(\mu)$ is the dual space of $L^{1}(\mu)$ ?

6 Suppose $1<p<\infty$ and prove that $L^{q}(\mu)$ is the dual space of $L^{p}(\mu)$ even if $\mu$ is not $\sigma$-finite. (As usual, $1 / p+1 / q=1$.)

7 Suppose $\mu$ is a complex Borel measure on $[0,2 \pi$ ) (or on the unit circle $T$ ), and define the Fourier coefficients of $\mu$ by

$$
\hat{\mu}(n)=\int e^{-i n t} d \mu(t) \quad(n=0, \pm 1, \pm 2, \ldots)
$$

Assume that $\hat{\mu}(n) \rightarrow 0$ as $n \rightarrow+\infty$ and prove that then $\hat{\mu}(n) \rightarrow 0$ as $n \rightarrow-\infty$.

Hint: The assumption also holds with $f d \mu$ in place of $d \mu$ if $f$ is any trigonometric polynomial, hence if $f$ is continuous, hence if $f$ is any bounded Borel function, hence if $d \mu$ is replaced by $d|\mu|$.

8 In the terminology of Exercise 7, find all $\mu$ such that $\hat{\mu}$ is periodic, with period $k$. [This means that $\hat{\mu}(n+k)=\hat{\mu}(n)$ for all integers $n$; of course, $k$ is also assumed to be an integer.]

9 Suppose that $\left\{g_{n}\right\}$ is a sequence of positive continuous functions on $I=[0,1]$, that $\mu$ is a positive Borel measure on $I$, and that

$\begin{array}{ll}\text { (i) } \lim _{n \rightarrow \infty} g_{n}(x)=0 \quad \text { a.e. }[m] \text {, } & \text {, }\end{array}$

(ii) $\int_{I} g_{n} d m=1 \quad$ for all $n$,

(iii) $\lim _{n \rightarrow \infty} \int_{I} f g_{n} d m=\int_{I} f d \mu \quad$ for every $f \in C(I)$.

Does it follow that $\mu \perp m$ ?

10 Let $(X, \mathfrak{M}, \mu)$ be a positive measure space. Call a set $\Phi \subset L^{1}(\mu)$ uniformly integrable if to each $\epsilon>0$ corresponds a $\delta>0$ such that

$$
\left|\int_{E} f d \mu\right|<\epsilon
$$

whenever $f \in \Phi$ and $\mu(E)<\delta$.

(a) Prove that every finite subset of $L^{1}(\mu)$ is uniformly integrable.

(b) Prove the following convergence theorem of Vitali:

If (i) $\mu(X)<\infty$, (ii) $\left\{f_{n}\right\}$ is uniformly integrable, (iii) $f_{n}(x) \rightarrow f(x)$ a.e. as $n \rightarrow \infty$, and (iv) $|f(x)|$ $<\infty$ a.e., then $f \in L^{1}(\mu)$ and

$$
\lim _{n \rightarrow \infty} \int_{X}\left|f_{n}-f\right| d \mu=0
$$

Suggestion: Use Egoroff's theorem.

(c) Show that $(b)$ fails if $\mu$ is Lebesgue measure on $(-\infty, \infty)$, even if $\left\{\left\|f_{n}\right\|_{1}\right\}$ is assumed to be bounded. Hypothesis (i) can therefore not be omitted in (b).

(d) Show that hypothesis (iv) is redundant in (b) for some $\mu$ (for instance, for Lebesgue measure on a bounded interval), but that there are finite measures for which the omission of (iv) would make (b) false.

(e) Show that Vitali's theorem implies Lebesgue's dominated convergence theorem, for finite measure spaces. Construct an example in which Vitali's theorem applies although the hypotheses of Lebesgue's theorem do not hold.

$(f)$ Construct a sequence $\left\{f_{n}\right\}$, say on $[0,1]$, so that $f_{n}(x) \rightarrow 0$ for every $x, \int f_{n} \rightarrow 0$, but $\left\{f_{n}\right\}$ is not uniformly integrable (with respect to Lebesgue measure).

(g) However, the following converse of Vitali's theorem is true:

If $\mu(X)<\infty, f_{n} \in L^{1}(\mu)$, and

$$
\lim _{n \rightarrow \infty} \int_{E} f_{n} d \mu
$$

exists for every $E \in \mathfrak{M}$, then $\left\{f_{n}\right\}$ is uniformly integrable.

Prove this by completing the following outline.

Define $\rho(A, B)=\int\left|\chi_{A}-\chi_{B}\right| d \mu$. Then $(\mathfrak{M}, \rho)$ is a complete metric space (modulo sets of measure 0 ), and $E \rightarrow \int_{E} f_{n} d \mu$ is continuous for each $n$. If $\epsilon>0$, there exist $E_{0}, \delta, N$ (Exercise 13, Chap. 5) so that

$$
\left|\int_{E}\left(f_{n}-f_{N}\right) d \mu\right|<\epsilon \quad \text { if } \quad \rho\left(E, E_{0}\right)<\delta, \quad n>N
$$

If $\mu(A)<\delta,\left({ }^{*}\right)$ holds with $B=E_{0}-A$ and $C=E_{0} \cup A$ in place of $E$. Thus $\left({ }^{*}\right)$ holds with $A$ in place of $E$ and $2 \epsilon$ in place of $\epsilon$. Now apply $(a)$ to $\left\{f_{1}, \ldots, f_{N}\right\}:$ There exists $\delta^{\prime}>0$ such that

$$
\left|\int_{A} f_{n} d \mu\right|<3 \epsilon \quad \text { if } \quad \mu(A)<\delta^{\prime}, \quad n=1,2,3, \ldots
$$

11 Suppose $\mu$ is a positive measure on $X, \mu(X)<\infty, f_{n} \in L^{1}(\mu)$ for $n=1,2,3, \ldots, f_{n}(x) \rightarrow f(x)$ a.e., and there exists $p>1$ and $C<\infty$ such that $\int_{X}\left|f_{n}\right|^{p} d \mu<C$ for all $n$. Prove that

$$
\lim _{n \rightarrow \infty} \int_{x}\left|f-f_{n}\right| d \mu=0
$$

Hint: $\left\{f_{n}\right\}$ is uniformly integrable.

12 Let $\mathfrak{M}$ be the collection of all sets $E$ in the unit interval $[0,1]$ such that either $E$ or its complement is at most countable. Let $\mu$ be the counting measure on this $\sigma$-algebra $\mathfrak{M}$. If $g(x)=x$ for $0 \leq x \leq 1$, show that $g$ is not $\mathfrak{M}$-measurable, although the mapping

$$
f \rightarrow \sum x f(x)=\int f g d \mu
$$

makes sense for every $f \in L^{1}(\mu)$ and defines a bounded linear functional on $L^{1}(\mu)$. Thus $\left(L^{1}\right)^{*} \neq L^{\infty}$ in this situation.

13 Let $L^{\infty}=L^{\infty}(m)$, where $m$ is Lebesgue measure on $I=[0,1]$. Show that there is a bounded linear functional $\Lambda \neq 0$ on $L^{\infty}$ that is 0 on $C(I)$, and that therefore there is no $g \in L^{1}(m)$ that satisfies $\Lambda f=$ $\int_{I} f g d m$ for every $f \in L^{\infty}$. Thus $\left(L^{\infty}\right)^{*} \neq L^{1}$.

## DIFFERENTIATION

In elementary Calculus we learn that integration and differentiation are inverses of each other. This fundamental relation persists to a large extent in the context of the Lebesgue integral. We shall see that some of the most important facts about differentiation of integrals and integration of derivatives can be obtained with a minimum of effort by first studying derivatives of measures and the associated maximal functions. The Radon-Nikodym theorem and the Lebesgue decomposition will play a prominent role.

## Derivatives of Measures

We begin with a simple, theorem whose main purpose is to motivate the definitions that follow.

7.1 Theorem Suppose $\mu$ is a complex Borel measure on $R^{1}$ and

$$
f(x)=\mu((-\infty, x)) \quad\left(x \in R^{1}\right)
$$

If $x \in R^{1}$ and $A$ is a complex number, each of the following two statements implies the other:

(a) $f$ is differentiable at $x$ and $f^{\prime}(x)=A$.

(b) To every $\epsilon>0$ corresponds a $\delta>0$ such that

$$
\left|\frac{\mu(I)}{m(I)}-A\right|<\epsilon
$$

for every open segment I that contains $x$ and whose length is less than $\delta$. Here $m$ denotes Lebesgue measure on $R^{1}$.

7.2 Definitions Theorem 7.1 suggests that one might define the derivative of $\mu$ at $x$ to be the limit of the quotients $\mu(I) / m(I)$, as the segments $I$ shrink to $x$, and that an analogous definition might be appropriate in several variables, i.e., in $R^{k}$ rather than in $R^{1}$.

Accordingly, let us fix a dimension $k$, denote the open ball with center $x \in R^{k}$ and radius $r>0$ by

$$
B(x, r)=\left\{y \in R^{k}:|y-x|<r\right\}
$$

(the absolute value indicates the euclidean metric, as in Sec. 2.19), associate to any complex Borel measure $\mu$ on $R^{k}$ the quotients

$$
\left(Q_{r} \mu\right)(x)=\frac{\mu(B(x, r))}{m(B(x, r))}
$$

where $m=m_{k}$ is Lebesgue measure on $R^{k}$, and define the symmetric derivative of $\mu$ at $x$ to be

$$
(D \mu)(x)=\lim _{r \rightarrow 0}\left(Q_{r} \mu\right)(x)
$$

at those points $x \in R^{k}$ at which this limit exists.

We shall study $D \mu$ by means of the maximal function $M \mu$. For $\mu \geq 0$, this is defined by

$$
(M \mu)(x)=\sup _{0<r<\infty}\left(Q_{r} \mu\right)(x)
$$

and the maximal function of a complex Borel measure $\mu$ is, by definition, that of its total variation $|\mu|$.

The functions $M \mu: R^{k} \rightarrow[0, \infty]$ are lower semicontinuous, hence measurable.

To see this, assume $\mu \geq 0$, pick $\lambda>0$, let $E=\{M \mu>\lambda\}$, and fix $x \in E$. Then there is an $r>0$ such that

$$
\mu(B(x, r))=\operatorname{tm}(B(x, r))
$$

for some $t>\lambda$, and there is a $\delta>0$ that satisfies

$$
(r+\delta)^{k}<r^{k} t / \lambda
$$

If $|y-x|<\delta$, then $B(y, r+\delta) \supset B(x, r)$, and therefore

$$
\mu(B(y, r+\delta)) \geq t m(B(x, r))=t[r /(r+\delta)]^{k} m(B(y, r+\delta))>\lambda m(B(y, r+\delta))
$$

Thus $B(x, \delta) \subset E$. This proves that $E$ is open.

Our first objective is the "maximal theorem" 7.4. The following covering lemma will be used in its proof.

7.3 Lemma If $W$ is the union of a finite collection of balls $B\left(x_{i}, r_{i}\right), 1 \leq i \leq N$, then there is a set $S \subset\{1, \ldots, N\}$ so that

(a) the balls $B\left(x_{i}, r_{i}\right)$ with $i \in S$ are disjoint,

(b) $W \subset \bigcup_{i \in S} B\left(x_{i}, 3 r_{i}\right)$, and

(c) $m(W) \leq 3^{k} \sum_{i \in S} m\left(B\left(x_{i}, r_{i}\right)\right)$.

Proof Order the balls $B_{i}=B\left(x_{i}, r_{i}\right)$ so that $r_{1} \geq r_{2} \geq \cdots \geq r_{N}$. Put $i_{1}=1$. Discard all $B_{j}$ that intersect $B_{i_{1}}$. Let $B_{i_{2}}$ be the first of the remaining $B_{j}$, if there are any. Discard all $B_{j}$ with $j>i_{2}$ that intersect $B_{i_{2}}$, let $B_{i_{3}}$ be the first of the remaining ones, and so on, as long as possible. This process stops after a finite number of steps and gives $S=\left\{i_{1}, i_{2}, \ldots\right\}$.

It is clear that $(a)$ holds. Every discarded $B_{j}$ is a subset of $B\left(x_{i}, 3 r_{i}\right)$ for some $i \in S$, for if $r^{\prime} \leq r$ and $B\left(x^{\prime}, r^{\prime}\right)$ intersects $B(x, r)$, then $B\left(x^{\prime}, r^{\prime}\right) \subset B(x, 3 r)$. This proves $(b)$, and $(c)$ follows from $(b)$ because

in $R^{k}$.

$$
m(B(x, 3 r))=3^{k} m(B(x, r))
$$

The following theorem says, roughly speaking, that the maximal function of a measure cannot be large on a large set.

7.4 Theorem If $\mu$ is a complex Borel measure on $R^{k}$ and $\lambda$ is a positive number, then

$$
m\{M \mu>\lambda\} \leq 3^{k} \lambda^{-1}\|\mu\|
$$

Here $\|\mu\|=|\mu|\left(R^{k}\right)$, and the left side of (1) is an abbreviation for the more cumbersome expression

$$
m\left(\left\{x \in R^{k}:(M \mu)(x)>\lambda\right\}\right)
$$

We shall often simplify notation in this way.

Proof Fix $\mu$ and $\lambda$. Let $K$ be a compact subset of the open set $\{M \mu>\lambda\}$. Each $x \in K$ is the center of an open ball $B$ for which

$$
|\mu|(B)>\lambda m(B)
$$

Some finite collection of these $B$ 's covers $K$, and Lemma 7.3 gives us a disjoint subcollection, say $\left\{B_{1}, \ldots, B_{n}\right\}$, that satisfies

$$
m(K) \leq 3^{k} \sum_{1}^{n} m\left(B_{i}\right) \leq 3^{k} \lambda^{-1} \sum_{1}^{n}|\mu|\left(B_{i}\right) \leq 3^{k} \lambda^{-1}\|\mu\|
$$

The disjointness of $\left\{B_{1}, \ldots, B_{n}\right\}$ was used in the last inequality.

Now (1) follows by taking the supremum over all compact $K \subset\{M \mu>\lambda\}$.

7.5 Weak $L^{1}$ If $f \in L^{1}\left(R^{k}\right)$ and $\lambda>0$, then

$$
m\{|f|>\lambda\} \leq \lambda^{-1}\|f\|_{1}
$$

because, putting $E=\{|f|>\lambda\}$, we have

$$
\lambda m(E) \leq \int_{E}|f| d m \leq \int_{R^{k}}|f| d m=\|f\|_{1}
$$

Accordingly, any measurable function $f$ for which

$$
\lambda \cdot m\{|f|>\lambda\}
$$

is a bounded function of $\lambda$ on $(0, \infty)$ is said to belong to weak $L^{1}$.

Thus weak $L^{1}$ contains $L^{1}$. That it is actually larger is shown most simply by the function $1 / x$ on $(0,1)$.

We associate to each $f \in L^{1}\left(R^{k}\right)$ its maximal function $M f: R^{k} \rightarrow[0, \infty]$, by setting

$$
(M f)(x)=\sup _{0<r<\infty} \frac{1}{m\left(B_{r}\right)} \int_{B(x, r)}|f| d m
$$

[We wrote $B_{r}$ in place of $B(x, r)$ because $m(B(x, r))$ depends only on the radius $r$.] If we identify $f$ with the measure $\mu$ given by $d \mu=f d m$, we see that (4) agrees with the previously defined $M \mu$. Theorem 7.4 states therefore that the "maximal operator" $M$ sends $L^{1}$ to weak $L^{1}$, with a bound (namely $3^{k}$ ) that depends only on the space $R^{k}$ :

For every $f \in L^{1}\left(R^{k}\right)$ and every $\lambda>0$,

$$
m\{M f>\lambda\} \leq 3^{k} \lambda^{-1}\|f\|_{1}
$$

7.6 Lebesgue points If $f \in L^{1}\left(R^{k}\right)$, any $x \in R^{k}$ for which it is true that

$$
\lim _{r \rightarrow 0} \frac{1}{m\left(B_{r}\right)} \int_{B(x, r)}|f(y)-f(x)| d m(y)=0
$$

is called a Lebesgue point of $f$.

For example, (1) holds if $f$ is continuous at the point $x$. In general, (1) means that the averages of $|f-f(x)|$ are small on small balls centered at $x$. The Lebesgue points of $f$ are thus points where $f$ does not oscillate too much, in an average sense.

It is probably far from obvious that every $f \in L^{1}$ has Lebesgue points. But the following remarkable theorem shows that they always exist. (See also Exercise 23.)

7.7 Theorem If $f \in L^{1}\left(R^{k}\right)$, then almost every $x \in R^{k}$ is a Lebesgue point of $f$.

Proof Define

$$
\left(T_{r} f\right)(x)=\frac{1}{m\left(B_{r}\right)} \int_{B(x, r)}|f-f(x)| d m
$$

for $x \in R^{k}, r>0$, and put

$$
(T f)(x)=\underset{r \rightarrow 0}{\lim \sup }\left(T_{r} f\right)(x)
$$

We have to prove that $T f=0$ a.e. $[m]$.

Pick $y>0$. Let $n$ be a positive integer. By Theorem 3.14, there exists $g \in C\left(R^{k}\right)$ so that $\|f-g\|_{1}<1 / n$ : Put $h=f-g$.

Since $g$ is continuous, $T g=0$. Since

$$
\left(T_{r} h\right)(x) \leq \frac{1}{m\left(B_{r}\right)} \int_{B(x, r)}|h| d m+|h(x)|
$$

we have

$$
T h \leq M h+|h|
$$

Since $T_{r} f \leq T_{r} g+T_{r} h$, it follows that

$$
T f \leq M h+|h|
$$

Therefore

$$
\{T f>2 y\} \subset\{M h>y\} \cup\{|h|>y\} .
$$

Denote the union on the right of (6) by $E(y, n)$. Since $\|h\|_{1}<1 / n$, Theorem 7.4 and the inequality $7.5(1)$ show that

$$
m(E(y, n)) \leq\left(3^{k}+1\right) /(y n)
$$

The left side of (6) is independent of $n$. Hence

$$
\{T f>2 y\} \subset \bigcap_{n=1}^{\infty} E(y, n)
$$

This intersection has measure 0 , by (7), so that $\{T f>2 y\}$ is a subset of a set of measure 0 . Since Lebesgue measure is complete, $\{T f>2 y\}$ is Lebesgue measurable, and has measure 0 . This holds for every positive $y$. Hence $T f=0$ a.e. $[m]$.

Theorem 7.7 yields interesting information, with very little effort, about topics such as

(a) differentiation of absolutely continuous measures,

(b) differentiation using sets other than balls,

(c) differentiation of indefinite integrals in $R^{1}$,

(d) metric density of measurable sets.

We shall now discuss these topics.

7.8 Theorem Suppose $\mu$ is a complex Borel measure on $R^{k}$, and $\mu \ll m$. Let $f$ be the Radon-Nikodym derivative of $\mu$ with respect to $m$. Then $D \mu=f$ a.e. $[m]$, and

$$
\mu(E)=\int_{E}(D \mu) d m
$$

for all Borel sets $E \subset R^{k}$.

In other words, the Radon-Nikodym derivative can also be obtained as a limit of the quotients $Q_{r} \mu$.

Proof The Radon-Nikodym theorem asserts that (1) holds with $f$ in place of $D \mu$. At any Lebesgue point $x$ of $f$, it follows that

$$
f(x)=\lim _{r \rightarrow 0} \frac{1}{m\left(B_{r}\right)} \int_{B(x, r)} f d m=\lim _{r \rightarrow 0} \frac{\mu(B(x, r))}{m(B(x, r))}
$$

Thus $(D \mu)(x)$ exists and equals $f(x)$ at every Lebesgue point of $f$, hence a.e. $[m]$.

7.9 Nicely shrinking sets Suppose $x \in R^{k}$. A sequence $\left\{E_{i}\right\}$ of Borel sets in $R^{k}$ is said to shrink to $x$ nicely if there is a number $\alpha>0$ with the following property: There is a sequence of balls $B\left(x, r_{i}\right)$, with $\lim r_{i}=0$, such that $E_{i} \subset B\left(x, r_{i}\right)$ and

$$
m\left(E_{i}\right) \geq \alpha \cdot m\left(B\left(x, r_{i}\right)\right)
$$

for $i=1,2,3, \ldots$.

Note that it is not required that $x \in E_{i}$, nor even that $x$ be in the closure of $E_{i}$. Condition (1) is a quantitative version of the requirement that each $E_{i}$ must occupy a substantial portion of some spherical neighborhood of $x$. For example, a nested sequence of $k$-cells whose longest edge is at most 1,000 times as long as its shortest edge and whose diameter tends to 0 shrinks nicely. A nested sequence of rectangles (in $R^{2}$ ) whose edges have lengths $1 / i$ and $(1 / i)^{2}$ does not shrink nicely.

7.10 Theorem Associate to each $x \in R^{k}$ a sequence $\left\{E_{i}(x)\right\}$ that shrinks to $x$ nicely, and let $f \in L^{1}\left(R^{k}\right)$. Then

$$
f(x)=\lim _{i \rightarrow \infty} \frac{1}{m\left(E_{i}(x)\right)} \int_{E_{i}(x)} f d m
$$

at every Lebesgue point of $f$, hence a.e. $[m]$.

Proof Let $x$ be a Lebesgue point of $f$ and let $\alpha(x)$ and $B\left(x, r_{i}\right)$ be the positive number and the balls that are associated to the sequence $\left\{E_{i}(x)\right\}$. Then, because $E_{i}(x) \subset B\left(x, r_{i}\right)$,

$$
\frac{\alpha(x)}{m\left(E_{i}(x)\right)} \int_{E_{i}(x)}|f-f(x)| d m \leq \frac{1}{m\left(B\left(x, r_{i}\right)\right)} \int_{B\left(x, r_{i}\right)}|f-f(x)| d m
$$

The right side converges to 0 as $i \rightarrow \infty$, because $r_{i} \rightarrow 0$ and $x$ is a Lebesgue point of $f$. Hence the left side converges to 0 , and (1) follows.

Note that no relation of any sort was assumed to exist between $\left\{E_{i}(x)\right\}$ and $\left\{E_{i}(y)\right\}$, for different points $x$ and $y$.

Note also that Theorem 7.10 leads to a correspondingly stronger form of Theorem 7.8. We omit the details.

7.11 Theorem If $f \in L^{1}\left(R^{1}\right)$ and

$$
F(x)=\int_{-\infty}^{x} f d m \quad(-\infty<x<\infty)
$$

then $F^{\prime}(x)=f(x)$ at every Lebesgue point of $f$, hence a.e. $[m]$.

(This is the easy half of the fundamental theorem of Calculus, extended to Lebesgue integrals.)

ProOF Let $\left\{\delta_{i}\right\}$ be a sequence of positive numbers that converges to 0 . Theorem 7.10, with $E_{i}(x)=\left[x, x+\delta_{i}\right]$, shows then that the right-hand derivative of $F$ exists at all Lebesgue points of $x$ of $f$ and that it is equal to $f(x)$ at these points. If we let $E_{i}(x)$ be $\left[x-\delta_{i}, x\right]$ instead, we obtain the same result for the left-hand derivative of $F$ at $x$.

7.12 Metric density Let $E$ be a Lebesgue measurable subset of $R^{k}$. The metric density of $E$ at a point $x \in R^{k}$ is defined to be

$$
\lim _{r \rightarrow 0} \frac{m(E \cap B(x, r))}{m(B(x, r))}
$$

provided, of course, that this limit exists.

If we let $f$ be the characteristic function of $E$ and apply Theorem 7.8 or Theorem 7.10, we see that the metric density of $E$ is 1 at almost every point of $E$, and that it is 0 at almost every point of the complement of $E$.

Here is a rather striking consequence of this, which should be compared with Exercise 8 in Chap. 2:

If $\epsilon>0$, there is no set $E \subset R^{1}$ that satisfies

for every segment $I$.

$$
\epsilon<\frac{m(E \cap I)}{m(I)}<1-\epsilon
$$

Having dealt with differentiation of absolutely continuous measures, we now turn to those that are singular with respect to $m$.

7.13 Theorem Associate to each $x \in R^{k}$ a sequence $\left\{E_{i}(x)\right\}$ that shrinks to $x$ nicely. If $\mu$ is a complex Borel measure and $\mu \perp m$, then

$$
\lim _{i \rightarrow \infty} \frac{\mu\left(E_{i}(x)\right)}{m\left(E_{i}(x)\right)}=0 \quad \text { a.e. }[m]
$$

ProOF The Jordan decomposition theorem shows that it suffices to prove (1) under the additional assumption that $\mu \geq 0$. In that case, arguing as in the proof of Theorem 7.10, we have

$$
\frac{\alpha(x) \mu\left(E_{i}(x)\right)}{m\left(E_{i}(x)\right)} \leq \frac{\mu\left(E_{i}(x)\right)}{m\left(B\left(x, r_{i}\right)\right)} \leq \frac{\mu\left(B\left(x, r_{i}\right)\right)}{m\left(B\left(x, r_{i}\right)\right)}
$$

Hence (1) is a consequence of the special case

$$
(D \mu)(x)=0 \quad \text { a.e. }[m]
$$

which will now be proved.

The upper derivative $\bar{D} \mu$, defined by

$$
(\bar{D} \mu)(x)=\lim _{n \rightarrow \infty}\left[\sup _{0<r<1 / n}\left(Q_{r} \mu\right)(x)\right] \quad\left(x \in R^{k}\right)
$$

is a Borel function, because the quantity in brackets decreases as $n$ increases and is, for each $n$, a lower semicontinuous function of $x$; the reasoning used in Sec. 7.2 proves this.

Choose $\lambda>0, \epsilon>0$. Since $\mu \perp m, \mu$ is concentrated on a set of Lebesgue measure 0 . The regularity of $\mu$ (Theorem 2.18) shows therefore that there is a compact set $K$, with $m(K)=0, \mu(K)>\|\mu\|-\epsilon$.

Define $\mu_{1}(E)=\mu(K \cap E)$, for any Borel set $E \subset R^{k}$, and put $\mu_{2}=\mu-\mu_{1}$. Then $\left\|\mu_{2}\right\|<\epsilon$, and, for every $x$ outside $K$,

$$
(\bar{D} \mu)(x)=\left(\bar{D} \mu_{2}\right)(x) \leq\left(M \mu_{2}\right)(x) .
$$

Hence

$$
\{\bar{D} \mu>\lambda\} \subset K \cup\left\{M \mu_{2}>\lambda\right\},
$$

and Theorem 7.4 shows that

$$
m\{\bar{D} \mu>\lambda\} \leq 3^{k} \lambda^{-1}\left\|\mu_{2}\right\|<3^{k} \lambda^{-1} \epsilon
$$

Since (6) holds for every $\epsilon>0$ and for every $\lambda>0$, we conclude that $\bar{D} \mu=0$ a.e. $[m]$, i.e., that (2) holds.

Theorems 7.10 and 7.13 can be combined in the following way:

7.14 Theorem Suppose that to each $x \in R^{k}$ is associated some sequence $\left\{E_{i}(x)\right\}$ that shrinks to $x$ nicely, and that $\mu$ is a complex Borel measure on $R^{k}$.

Let $d \mu=f d m+d \mu_{s}$ be the Lebesgue decomposition of $\mu$ with respect to $m$. Then

$$
\lim _{i \rightarrow \infty} \frac{\mu\left(E_{i}(x)\right)}{m\left(E_{i}(x)\right)}=f(x) \quad \text { a.e. }[m]
$$

In particular, $\mu \perp m$ if and only if $(D \mu)(x)=0$ a.e. $[m]$.

The following result contrasts strongly with Theorem 7.13:

7.15 Theorem If $\mu$ is a positive Borel measure on $R^{k}$ and $\mu \perp m$, then

$$
(D \mu)(x)=\infty \quad \text { a.e. }[\mu] .
$$

PROOF There is a Borel set $S \subset R^{k}$ with $m(S)=0$ and $\mu\left(R^{k}-S\right)=0$, and there are open sets $V_{j} \supset S$ with $m\left(V_{j}\right)<1 / j$, for $j=1,2,3, \ldots$.

For $N=1,2,3, \ldots$, let $E_{N}$ be the set of all $x \in S$ to which correspond radii $r_{i}=r_{i}(x)$, with $\lim r_{i}=0$, such that

$$
\mu\left(B\left(x, r_{i}\right)\right)<N m\left(B\left(x, r_{i}\right)\right)
$$

Then (1) holds for every $x \in S-\bigcup_{N} E_{N}$.

Fix $N$ and $j$, for the moment. Every $x \in E_{N}$ is then the center of a ball $B_{x} \subset V_{j}$ that satisfies (2). Let $\beta_{x}$ be the open ball with center $x$ whose radius is $1 / 3$ of that of $B_{x}$. The union of these balls $\beta_{x}$ is an open set $W_{j, N}$ that contains $E_{N}$ and lies in $V_{j}$. We claim that

$$
\mu\left(W_{j, N}\right)<3^{k} N / j
$$

To prove (3), let $K \subset W_{j, N}$ be compact. Finitely many $\beta_{x}$ cover $K$. Lemma 7.3 shows therefore that there is a finite set $F \subset E_{N}$ with the following properties:

(a) $\left\{\beta_{x}: x \in F\right\}$ is a disjoint collection, and

(b) $K \subset \bigcup_{x \in F} B_{x}$.

Thus

$$
\begin{aligned}
\mu(K) & \leq \sum_{x \in F} \mu\left(B_{x}\right)<N \sum_{x \in F} m\left(B_{x}\right) \\
& =3^{k} N \sum_{x \in F} m\left(\beta_{x}\right) \leq 3^{k} N m\left(V_{j}\right)<3^{k} N / j
\end{aligned}
$$

This proves (3).

Now put $\Omega_{N}=\bigcap_{j} W_{j, N}$. Then $E_{N} \subset \Omega_{N}, \Omega_{N}$ is a $G_{\delta}, \mu\left(\Omega_{N}\right)=0$, and $(D \mu)(x)=\infty$ at every point of $S-\bigcup_{N} \Omega_{N}$.

## The Fundamental Theorem of Calculus

7.16 This theorem concerns functions defined on some compact interval $[a, b]$ in $R^{1}$. It has two parts. The first asserts, roughly speaking, that the derivative of the indefinite integral of a function is that same function. We dealt with this in Theorem 7.11. The second part goes the other way: one returns to the original function by integrating its derivative. More precisely

$$
f(x)-f(a)=\int_{a}^{x} f^{\prime}(t) d t \quad(a \leq x \leq b)
$$

In the elementary version of this theorem, one assumes that $f$ is differentiable at every point of $[a, b]$ and that $f^{\prime}$ is a continuous function. The proof of $(1)$ is then easy.

In trying to extend (1) to the setting of the Lebesgue integral, questions such as the following come up naturally:

Is it enough to assume that $f^{\prime} \in L^{1}$, rather than that $f^{\prime}$ is continuous?

If $f$ is continuous and differentiable at almost all points of $[a, b]$, must (1) then hold?

Before proving any positive results, here are two examples that show how (1) can fail.

(a) Put $f(x)=x^{2} \sin \left(x^{-2}\right)$ if $x \neq 0, f(0)=0$. Then $f$ is differentiable at every point, but

$$
\int_{0}^{1}\left|f^{\prime}(t)\right| d t=\infty
$$

so $f^{\prime} \notin L^{1}$.

If we interpret the integral in (1) (with $[0,1]$ in place of $[a, b]$ ) as the limit, as $\epsilon \rightarrow 0$, of the integrals over $[\epsilon, 1]$, then (1) still holds for this $f$.

More complicated situations can arise where this kind of passage to the limit is of no use. There are integration processes, due to Denjoy and Perron (see [18], [28]), which are so designed that (1) holds whenever $f$ is differentiable at every point. These fail to have the property that the integrability of $f$ implies that of $|f|$, and therefore do not play such an important role in analysis.

(b) Suppose $f$ is continuous on $[a, b], f$ is differentiable at almost every point of $[a, b]$, and $f^{\prime} \in L^{1}$ on $[a, b]$. Do these assumptions imply that (1) holds?

Answer: No.

Choose $\left\{\delta_{n}\right\}$ so that $1=\delta_{0}>\delta_{1}>\delta_{2}>\cdots, \delta_{n} \rightarrow 0$. Put $E_{0}=[0,1]$. Suppose $n \geq 0$ and $E_{n}$ is constructed so that $E_{n}$ is the union of $2^{n}$ disjoint closed intervals, each of length $2^{-n} \delta_{n}$. Delete a segment in the center of each of these $2^{n}$ intervals, so that each of the remaining $2^{n+1}$ intervals has length
$2^{-n-1} \delta_{n+1}$ (this is possible, since $\delta_{n+1}<\delta_{n}$ ), and let $E_{n+1}$ be the union of these $2^{n+1}$ intervals. Then $E_{1} \supset E_{2} \supset \cdots, m\left(E_{n}\right)=\delta_{n}$, and if

$$
E=\bigcap_{n=1}^{\infty} E_{n}
$$

then $E$ is compact and $m(E)=0$. (In fact, $E$ is perfect.) Put

$$
g_{n}=\delta_{n}^{-1} \chi_{E_{n}} \quad \text { and } \quad f_{n}(x)=\int_{0}^{x} g_{n}(t) d t \quad(n=0,1,2, \ldots)
$$

Then $f_{n}(0)=0, f_{n}(1)=1$, and each $f_{n}$ is a monotonic function which is constant on each segment in the complement of $E_{n}$. If $I$ is one of the $2^{n}$ intervals whose union is $E_{n}$, then

$$
\int_{I} g_{n}(t) d t=\int_{I} g_{n+1}(t) d t=2^{-n}
$$

It follows from (5) that

$$
f_{n+1}(x)=f_{n}(x) \quad\left(x \notin E_{n}\right)
$$

and that

$$
\left|f_{n}(x)-f_{n+1}(x)\right| \leq \int_{I}\left|g_{n}-g_{n+1}\right|<2^{-n+1} \quad\left(x \in E_{n}\right) .
$$

Hence $\left\{f_{n}\right\}$ converges uniformly to a continuous monotonic function $f$, with $f(0)=0, f(1)=1$, and $f^{\prime}(x)=0$ for all $x \notin E$. Since $m(E)=0$, we have $f^{\prime}=0$ a.e.

Thus (1) fails.

If $\delta_{n}=(2 / 3)^{n}$, the set $E$ is Cantor's "middle thirds" set.

Having seen what can go wrong, assume now that $f^{\prime} \in L^{1}$ and that (1) does hold. There is then a measure $\mu$, defined by $d \mu=f^{\prime} d m$. Since $\mu \ll m$, Theorem 6.11 shows that there corresponds to each $\epsilon>0$ a $\delta>0$ so that $|\mu|(E)<\epsilon$ whenever $E$ is a union of disjoint segments whose total length is less than $\delta$. Since $f(y)-f(x)=\mu((x, y))$ if $a \leq x<y \leq b$, it follows that the absolute continuity of $f$, as defined below, is necessary for (1). Theorem 7.20 will show that this necessary condition is also sufficient.

7.17 Definition A complex function $f$, defined on an interval $I=[a, b]$, is said to be absolutely continuous on $I$ (briefly, $f$ is $\mathrm{AC}$ on $I$ ) if there corresponds to every $\epsilon>0$ a $\delta>0$ so that

$$
\sum_{i=1}^{n}\left|f\left(\beta_{i}\right)-f\left(\alpha_{i}\right)\right|<\epsilon
$$

for any $n$ and any disjoint collection of segments $\left(\alpha_{1}, \beta_{1}\right), \ldots,\left(\alpha_{n}, \beta_{n}\right)$ in $I$ whose lengths satisfy

$$
\sum_{i=1}^{n}\left(\beta_{i}-\alpha_{i}\right)<\delta
$$

Such an $f$ is obviously continuous: simply take $n=1$.

In the following theorem, the implication $(b) \rightarrow(c)$ is probably the most interesting. That $(a) \rightarrow(c)$ without assuming monotonicity of $f$ is the content of Theorem 7.20.

7.18 Theorem Let $I=[a, b]$, let $f: I \rightarrow R^{1}$ be continuous and nondecreasing. Each of the following three statements about $f$ implies the other two:

(a) $f$ is $\mathrm{AC}$ on $I$.

(b) f maps sets of measure 0 to sets of measure 0 .

(c) $f$ is differentiable a.e. on $I, f^{\prime} \in L^{1}$, and

$$
f(x)-f(a)=\int_{a}^{x} f^{\prime}(t) d t \quad(\alpha \leq x \leq b)
$$

Note that the functions constructed in Example 7.16(b) map certain compact sets of measure 0 onto the whole unit interval!

Exercise 12 complements this theorem.

Proof We will show that $(a) \rightarrow(b) \rightarrow(c) \rightarrow(a)$.

Let $\mathfrak{M}$ denote the $\sigma$-algebra of all Lebesgue measurable subsets of $R^{1}$.

Assume $f$ is $\mathrm{AC}$ on $I$, pick $E \subset I$ so that $E \in \mathfrak{M}$ and $m(E)=0$. We have to show that $f(E) \in \mathfrak{M}$ and $m(f(E))=0$. Without loss of generality, assume that neither $a$ nor $b$ lie in $E$.

Choose $\epsilon>0$. Associate $\delta>0$ to $f$ and $\epsilon$, as in Definition 7.17. There is then an open set $V$ with $m(V)<\delta$, so that $E \subset V \subset I$. Let $\left(\alpha_{i}, \beta_{i}\right)$ be the disjoint segments whose union is $V$. Then $\sum\left(\beta_{i}-\alpha_{i}\right)<\delta$, and our choice of $\delta$ shows that therefore

$$
\sum_{i}\left(f\left(\beta_{i}\right)-f\left(\alpha_{i}\right)\right) \leq \epsilon
$$

[Definition 7.17 was stated in terms of finite sums; thus (2) holds for every partial sum of the (possibly) infinite series, hence (2) holds also for the sum of the whole series, as stated.]

Since $E \subset V, f(E) \subset \bigcup\left[f\left(\alpha_{i}\right), f\left(\beta_{i}\right)\right]$. The Lebesgue measure of this union is the left side of (2). This says that $f(E)$ is a subset of Borel sets of arbitrarily small measure. Since Lebesgue measure is complete, it follows that $f(E) \in \mathfrak{M}$ and $m(f(E))=0$.

We have now proved that $(a)$ implies $(b)$.

Assume next that $(b)$ holds. Define

$$
g(x)=x+f(x) \quad(a \leq x \leq b)
$$

If the $f$-image of some segment of length $\eta$ has length $\eta^{\prime}$, then the $g$-image of that same segment has length $\eta+\eta^{\prime}$. From this it follows easily that $g$ satisfies $(b)$, since $f$ does.

Now suppose $E \subset I, E \in \mathfrak{M}$. Then $E=E_{1} \cup E_{0}$ where $m\left(E_{0}\right)=0$ and $E_{1}$ is an $F_{\sigma}$ (Theorem 2.20). Thus $E_{1}$ is a countable union of compact sets, and so is $g\left(E_{1}\right)$, because $g$ is continuous. Since $g$ satisfies $(b), m\left(g\left(E_{0}\right)\right)=0$. Since $g(E)=g\left(E_{1}\right) \cup g\left(E_{0}\right)$, we conclude: $g(E) \in \mathfrak{M}$.

Therefore we can define

$$
\mu(E)=m(g(E)) \quad(E \subset I, E \in \mathfrak{M})
$$

Since $g$ is one-to-one (this is our reason for working with $g$ rather than $f$ ), disjoint sets in $I$ have disjoint $g$-images. The countable additivity of $m$ shows therefore that $\mu$ is a (positive, bounded) measure on $\mathfrak{M}$. Also, $\mu \ll m$, because $g$ satisfies $(b)$. Thus

$$
d \mu=h d m
$$

for some $h \in L^{1}(m)$, by the Radon-Nikodym theorem.

If $E=[a, x]$, then $g(E)=[g(a), g(x)]$, and (5) gives

$$
g(x)-g(a)=m(g(E))=\mu(E)=\int_{E} h d m=\int_{a}^{x} h(t) d t .
$$

If we now use (3), we conclude that

$$
f(x)-f(a)=\int_{a}^{x}[h(t)-1] d t \quad(\alpha \leq x \leq b)
$$

Thus $f^{\prime}(x)=h(x)-1$ a.e. $[m]$, by Theorem 7.11.

We have now proved that $(b)$ implies $(c)$.

The discussion that preceded Definition 7.17 showed that $(c)$ implies $(a)$.

7.19 Theorem Suppose $f: I \rightarrow R^{1}$ is $\mathrm{AC}, I=[a, b]$. Define

$$
F(x)=\sup \sum_{i=1}^{N}\left|f\left(t_{i}\right)-f\left(t_{i-1}\right)\right| \quad(a \leq x \leq b)
$$

where the supremum is taken over all $N$ and over all choices of $\left\{t_{i}\right\}$ such that

$$
a=t_{0}<t_{1}<\cdots<t_{N}=x .
$$

The functions $F, F+f, F-f$ are then nondecreasing and $\mathrm{AC}$ on $I$.

[ $F$ is called the total variation function of $f$. If $f$ is any (complex) function on $I$, $\mathrm{AC}$ or not, and $F(b)<\infty$, then $f$ is said to have bounded variation on $I$, and $F(b)$ is the total variation of $f$ on $I$. Exercise 13 is relevant to this.]

Proof If (2) holds and $x<y \leq b$, then

$$
F(y) \geq|f(y)-f(x)|+\sum_{i=1}^{N}\left|f\left(t_{i}\right)-f\left(t_{i-1}\right)\right|
$$

Hence $F(y) \geq|f(y)-f(x)|+F(x)$. In particular

$$
F(y) \geq f(y)-f(x)+F(x) \text { and } \quad F(y) \geq f(x)-f(y)+F(x) \text {. }
$$

This proves that $F, F+f, F-f$ are nondecreasing.

Since sums of two AC functions are obviously $\mathrm{AC}$, it only remains to be proved that $F$ is $\mathrm{AC}$ on $I$.

If $(a, \beta) \subset I$ then

$$
F(\beta)-F(\alpha)=\sup \sum_{1}^{n}\left|f\left(t_{i}\right)-f\left(t_{i-1}\right)\right|
$$

the supremum being taken over all $\left\{t_{i}\right\}$ that satisfy $\alpha=t_{0}<\cdots<t_{n}=\beta$.

Note that $\sum\left(t_{i}-t_{i-1}\right)=\beta-\alpha$.

Now pick $\epsilon>0$, associate $\delta>0$ to $f$ and $\epsilon$ as in Definition 7.17, choose disjoint segments $\left(\alpha_{j}, \beta_{j}\right) \subset I$ with $\sum\left(\beta_{j}-\alpha_{j}\right)<\delta$, and apply (5) to each $\left(\alpha_{j}, \beta_{j}\right)$. It follows that

$$
\sum_{j}\left(F\left(\beta_{j}\right)-F\left(\alpha_{j}\right)\right) \leq \epsilon
$$

by our choice of $\delta$. Thus $F$ is AC on $I$.

We have now reached our main objective:

7.20 Theorem If $f$ is a complex function that is $\mathrm{AC}$ on $I=[a, b]$, then $f$ is differentiable at almost all points of $I, f^{\prime} \in L^{1}(m)$, and

$$
f(x)-f(a)=\int_{a}^{x} f^{\prime}(t) d t \quad(a \leq x \leq b)
$$

Proof It is of course enough to prove this for real $f$. Let $F$ be its total variation function, as in Theorem 7.19, define

$$
f_{1}=\frac{1}{2}(F+f), \quad f_{2}=\frac{1}{2}(F-f),
$$

and apply the implication $(a) \rightarrow(c)$ of Theorem 7.18 to $f_{1}$ and $f_{2}$. Since

$$
f=f_{1}-f_{2}
$$

this yields (1).

The next theorem derives (1) from a different set of hypotheses, by an entirely different method of proof.

7.21 Theorem If $f:[a, b] \rightarrow R^{1}$ is differentiable at every point of $[a, b]$ and $f^{\prime} \in L^{1}$ on $[a, b]$, then

$$
f(x)-f(a)=\int_{a}^{x} f^{\prime}(t) d t \quad(a \leq x \leq b)
$$

Note that differentiability is assumed to hold at every point of $[a, b]$.

Proof It is clear that it is enough to prove this for $x=b$. Fix $\epsilon>0$. Theorem 2.25 ensures the existence of a lower semicontinuous function $g$ on $[a, b]$ such that $g>f^{\prime}$ and

$$
\int_{a}^{b} g(t) d t<\int_{a}^{b} f^{\prime}(t) d t+\epsilon
$$

Actually, Theorem 2.25 only gives $g \geq f^{\prime}$, but since $m([a, b])<\infty$, we can add a small constant to $g$ without affecting (2). For any $\eta>0$, define

$$
F_{\eta}(x)=\int_{a}^{x} g(t) d t-f(x)+f(a)+\eta(x-a) \quad(a \leq x \leq b) .
$$

Keep $\eta$ fixed for the moment. To each $x \in[a, b)$ there corresponds a $\delta_{x}>0$ such that

$$
g(t)>f^{\prime}(x) \text { and } \frac{f(t)-f(x)}{t-x}<f^{\prime}(x)+\eta
$$

for all $t \in\left(x, x+\delta_{x}\right)$, since $g$ is lower semicontinuous and $g(x)>f^{\prime}(x)$. For any such $t$ we therefore have

$$
\begin{aligned}
F_{\eta}(t)-F_{\eta}(x) & =\int_{x}^{t} g(s) d s-[f(t)-f(x)]+\eta(t-x) \\
& >(t-x) f^{\prime}(x)-(t-x)\left[f^{\prime}(x)+\eta\right]+\eta(t-x)=0 .
\end{aligned}
$$

Since $F_{\eta}(a)=0$ and $F_{\eta}$ is continuous, there is a last point $x \in[a, b]$ at which $F_{\eta}(x)=0$. If $x<b$, the preceding computation implies that $F_{\eta}(t)>0$ for $t \in(x, b]$. In any case, $F_{\eta}(b) \geq 0$. Since this holds for every $\eta>0$, (2) and (3) now give

$$
f(b)-f(a) \leq \int_{a}^{b} g(t) d t<\int_{a}^{b} f^{\prime}(t) d t+\epsilon
$$

and since $\epsilon$ was arbitrary, we conclude that

$$
f(b)-f(a) \leq \int_{a}^{b} f^{\prime}(t) d t
$$

If $f$ satisfies the hypotheses of the theorem, so does $-f$; therefore (6) holds with $-f$ in place of $f$, and these two inequalities together give (1).

## Differentiable Transformations

7.22 Definitions Suppose $V$ is an open set in $R^{k}, T$ maps $V$ into $R^{k}$, and $x \in V$. If there exists a linear operator $A$ on $R^{k}$ (i.e., a linear mapping of $R^{k}$ into $R^{k}$, as in Definition 2.1) such that

$$
\lim _{h \rightarrow 0} \frac{|T(x+h)-T(x)-A h|}{|h|}=0
$$

(where, of course, $h \in R^{k}$ ), then we say that $T$ is differentiable at $x$, and define

$$
T^{\prime}(x)=A \text {. }
$$

The linear operator $T^{\prime}(x)$ is called the derivative of $T$ at $x$. (One shows easily that there is at most one linear $\boldsymbol{A}$ that satisfies the preceding requirements; thus it is legitimate to talk about the derivative of $T$.) The term differential is also often used for $T^{\prime}(x)$.

The point of (1) is of course that the difference $T(x+h)-T(x)$ is approximated by $T^{\prime}(x) h$, a linear function of $h$.

Since every real number $\alpha$ gives rise to a linear operator on $R^{1}$ (mapping $h$ to $\alpha h$ ), our definition of $T^{\prime}(x)$ coincides with the usual one when $k=1$.

When $A: R^{k} \rightarrow R^{k}$ is linear, Theorem $2.20(e)$ shows that there is a number $\Delta(A)$ such that

$$
m(A(E))=\Delta(A) m(E)
$$

for all measurable sets $E \subset R^{k}$. Since

$$
A^{\prime}(x)=A \quad\left(x \in R^{k}\right)
$$

and since every differentiable transformation $T$ can be locally approximated by a constant plus a linear transformation, one may conjecture that

$$
\frac{m(T(E))}{m(E)} \sim \Delta\left(T^{\prime}(x)\right)
$$

for suitable sets $E$ that are close to $x$. This will be proved in Theorem 7.24, and furnishes the motivation for Theorem 7.26.

Recall that $\Delta(A)=|\operatorname{det} A|$ was proved in Sec. 2.23. When $T$ is differentiable at $x$, the determinant of $T^{\prime}(x)$ is called the Jacobian of $T$ at $x$, and is denoted by $J_{T}(x)$. Thus

$$
\Delta\left(T^{\prime}(x)\right)=\left|J_{T}(x)\right|
$$

The following lemma seems geometrically obvious. Its proof depends on the Brouwer fixed point theorem. One can avoid the use of this theorem by imposing
stronger hypotheses on $F$, for example, by assuming that $F$ is an open mapping. But this would lead to unnecessarily strong assumptions in Theorem 7.26.

7.23 Lemma Let $S=\{x:|x|=1\}$ be the sphere in $R^{k}$ that is the boundary of the open unit ball $B=B(0,1)$.

If $F: \bar{B} \rightarrow R^{k}$ is continuous, $0<\epsilon<1$, and

$$
|F(x)-x|<\epsilon
$$

for all $x \in S$, then $F(B) \supset B(0,1-\epsilon)$.

Proof Assume, to reach a contradiction, that some point $a \in B(0,1-\epsilon)$ is not in $F(B)$. By (1), $|F(x)|>1-\epsilon$ if $x \in S$. Thus $a$ is not in $F(S)$, and therefore $a \neq F(x)$, for every $x \in \bar{B}$. This enables us to define a continuous map $G: \bar{B} \rightarrow \bar{B}$ by

$$
G(x)=\frac{a-F(x)}{|a-F(x)|}
$$

If $x \in S$, then $x \cdot x=|x|^{2}=1$, so that

$$
x \cdot(a-F(x))=x \cdot a+x \cdot(x-F(x))-1<|a|+\epsilon-1<0 .
$$

This shows that $x \cdot G(x)<0$, hence $x \neq G(x)$.

If $x \in B$, then obviously $x \neq G(x)$, simply because $G(x) \in S$.

Thus $G$ fixes no point of $\bar{B}$, contrary to Brouwer's theorem which states that every continuous map of $\bar{B}$ into $\bar{B}$ has at least one fixed point.

A proof of Brouwer's theorem that is both elementary and simple may be found on pp. 38-40 of "Dimension Theory" by Hurewicz and Wallman, Princeton University Press, 1948.

### 7.24 Theorem If

(a) $V$ is open in $R^{k}$,

(b) $T: V \rightarrow R^{k}$ is continuous, and

(c) $T$ is differentiable at some point $x \in V$, then

$$
\lim _{r \rightarrow 0} \frac{m(T(B(x, r)))}{m(B(x, r))}=\Delta\left(T^{\prime}(x)\right)
$$

Note that $T(B(x, r))$ is Lebesgue measurable; in fact, it is $\sigma$-compact, because $B(x, r)$ is $\sigma$-compact and $T$ is continuous.

Proof Assume, without loss of generality, that $x=0$ and $T(x)=0$. Put $A=T^{\prime}(0)$.

The following elementary fact about linear operators on finitedimensional vector spaces will be used: $A$ linear operator $A$ on $R^{k}$ is one-to-
one if and only if the range of $A$ is all of $R^{k}$. In that case, the inverse $A^{-1}$ of $A$ is also linear.

Accordingly, we split the proof into two cases.

CASE I $A$ is one-to-one. Define

$$
F(x)=A^{-1} T(x) \quad(x \in V) .
$$

Then $F^{\prime}(0)=A^{-1} T^{\prime}(0)=A^{-1} A=I$, the identity operator. We shall prove that

$$
\lim _{r \rightarrow 0} \frac{m(F(B(0, r)))}{m(B(0, r))}=1
$$

Since $T(x)=A F(x)$, we have

$$
m(T(B))=m(A(F(B)))=\Delta(A) m(F(B))
$$

for every ball $B$, by 7.22(3). Hence (3) will give the desired result.

Choose $\epsilon>0$. Since $F(0)=0$ and $F^{\prime}(0)=I$, there exists a $\delta>0$ such that $0<|x|<\delta$ implies

$$
|F(x)-x|<\epsilon|x| \text {. }
$$

We claim that the inclusions

$$
B(0,(1-\epsilon) r) \subset F(B(0, r)) \subset B(0,(1+\epsilon) r)
$$

hold if $0<r<\delta$. The first of these follows from Lemma 7.23, applied to $B(0, r)$ in place of $B(0,1)$, because $|F(x)-x|<\epsilon r$ for all $x$ with $|x|=r$. The second follows directly from (5), since $|F(x)|<(1+\epsilon)|x|$. It is clear that (6) implies

$$
(1-\epsilon)^{k} \leq \frac{m(F(B(0, r)))}{m(B(0, r))} \leq(1+\epsilon)^{k}
$$

and this proves (3).

CASE II $A$ is not one-to-one. In this case, $A$ maps $R^{k}$ into a subspace of lower dimension, i.e., into a set of measure 0 . Given $\epsilon>0$, there is therefore an $\eta>0$ such that $m\left(E_{\eta}\right)<\epsilon$ if $E_{\eta}$ is the set of all points in $R^{k}$ whose distance from $A(B(0,1))$ is less than $\eta$. Since $A=T^{\prime}(0)$, there is a $\delta>0$ such that $|x|<\delta$ implies

$$
|T(x)-A x| \leq \eta|x| \text {. }
$$

If $r<\delta$, then $T(B(0, r))$ lies therefore in the set $E$ that consists of the points whose distance from $A(B(0, r))$ is less than $\eta r$. Our choice of $\eta$ shows that $m(E)<\epsilon r^{k}$. Hence

$$
m(T(B(0, r)))<\epsilon r^{k} \quad(0<r<\delta) .
$$

Since $r^{k}=m(B(0, r)) / m(B(0,1)),(9)$ implies that

$$
\lim _{r \rightarrow 0} \frac{m(T(B(0, r)))}{m(B(0, r))}=0
$$

This proves (1), since $\Delta\left(T^{\prime}(0)\right)=\Delta(A)=0$.

7.25 Lemma Suppose $E \subset R^{k}, m(E)=0, T$ maps $E$ into $R^{k}$, and

$$
\lim \sup \frac{|T(y)-T(x)|}{|y-x|}<\infty
$$

for every $x \in E$, as $y$ tends to $x$ within $E$.

Then $m(T(E))=0$.

Proof Fix positive integers $n$ and $p$, let $F=F_{n, p}$ be the set of all $x \in E$ such that

$$
|T(y)-T(x)| \leq n|y-x|
$$

for all $y \in B(x, 1 / p) \cap E$, and choose $\epsilon>0$. Since $m(F)=0, F$ can be covered by balls $B_{i}=B\left(x_{i}, r_{i}\right)$, where $x_{i} \in F, r_{i}<1 / p$, in such a way that $\sum m\left(B_{i}\right)<\epsilon$. (To do this, cover $F$ by an open set $W$ of small measure, decompose $W$ into disjoint boxes of small diameter, as in Sec. 2.19, and cover each of those that intersect $F$ by a ball whose center lies in the box and in $F$.)

If $x \in F \cap B_{i}$ then $\left|x_{i}-x\right|<r_{i}<1 / p$ and $x_{i} \in F$. Hence

$$
\left|T\left(x_{i}\right)-T(x)\right| \leq n\left|x_{i}-x\right|<n r_{i}
$$

so that $T\left(F \cap B_{i}\right) \subset B\left(T\left(x_{i}\right), n r_{i}\right)$. Therefore

$$
T(F) \subset \bigcup_{i} B\left(T\left(x_{i}\right), n r_{i}\right)
$$

The measure of this union is at most

$$
\sum_{i} m\left(B\left(T\left(x_{i}\right), n r_{i}\right)=n^{k} \sum_{i} m\left(B_{i}\right)<n^{k} \epsilon\right.
$$

Since Lebesgue measure is complete and $\epsilon$ was arbitrary, it follows that $T(F)$ is measurable and $m(T(F))=0$.

To complete the proof, note that $E$ is the union of the countable collection $\left\{F_{n, p}\right\}$.

Here is a special case of the lemma:

If $V$ is open in $R^{k}$ and $T: V \rightarrow R^{k}$ is differentiable at every point of $V$, then $T$ maps sets of measure 0 to sets of measure 0 .

We now come to the change-of-variables theorem.

### 7.26 Theorem Suppose that

(i) $X \subset V \subset R^{k}, V$ is open, $T: V \rightarrow R^{k}$ is continuous;
(ii) $X$ is Lebesgue measurable, $T$ is one-to-one on $X$, and $T$ is differentiable at every point of $X$

(iii) $m(T(V-X))=0$.

Then, setting $Y=T(X)$,

$$
\int_{Y} f d m=\int_{X}(f \circ T)\left|J_{T}\right| d m
$$

for every measurable $f: R^{k} \rightarrow[0, \infty]$.

The case $X=V$ is perhaps the most interesting one. As regards condition (iii), it holds, for instance, when $m(V-X)=0$ and $T$ satisfies the hypotheses of Lemma 7.25 on $V-X$.

The proof has some elements in common with that of the implication $(b) \rightarrow(c)$ in Theorem 7.18.

It will be important in this proof to distinguish between Borel sets and Lebesgue measurable sets. The $\sigma$-algebra consisting of the Lebesgue measurable subsets of $R^{k}$ will be denoted by $\mathfrak{M}$.

ProOF We break the proof into the following three steps:

(I) If $E \in \mathfrak{M}$ and $E \subset V$, then $T(E) \in \mathfrak{M}$.

(II) For every $E \in \mathfrak{M}$,

$$
m(T(E \cap X))=\int_{X} \chi_{E}\left|J_{T}\right| d m
$$

(III) For every $A \in \mathfrak{M}$,

$$
\int_{Y} \chi_{A} d m=\int_{X}\left(\chi_{A} \circ T\right)\left|J_{T}\right| d m
$$

If $E_{0} \in \mathfrak{M}, E_{0} \subset V$, and $m\left(E_{0}\right)=0$, then $m\left(T\left(E_{0}-X\right)\right)=0$ by (iii), and $m\left(T\left(E_{0} \cap X\right)\right)=0$ by Lemma 7.25. Thus $m\left(T\left(E_{0}\right)\right)=0$.

If $E_{1} \subset V$ is an $F_{\sigma}$, then $E_{1}$ is $\sigma$-compact, hence $T\left(E_{1}\right)$ is $\sigma$-compact, because $T$ is continuous. Thus $T\left(E_{1}\right) \in \mathfrak{M}$.

Since every $E \in \mathfrak{M}$ is the union of an $F_{\sigma}$ and a set of measure 0 (Theorem 2.20), (I) is proved.

To prove (II), let $n$ be a positive integer, and put

$$
V_{n}=\{x \in V:|T(x)|<n\}, \quad X_{n}=X \cap V_{n}
$$

Because of (I), we can define

$$
\mu_{n}(E)=m\left(T\left(E \cap X_{n}\right)\right) \quad(E \in \mathfrak{M})
$$

Since $T$ is one-to-one on $X_{n}$, the countable additivity of $m$ shows that $\mu_{n}$ is a measure on $\mathfrak{M}$. Also, $\mu_{n}$ is bounded (this was the reason for replacing $X$ temporarily by $X_{n}$ ), and $\mu_{n} \ll m$, by another application of Lemma 7.25.

Theorem 7.8 tells us therefore that $\left(D \mu_{n}\right)(x)$ exists a.e. $[m]$, that $D \mu_{n} \in L^{1}(m)$, and that

$$
\mu_{n}(E)=\int_{E}\left(D \mu_{n}\right) d m \quad(E \in \mathfrak{M})
$$

We claim next that

$$
\left(D \mu_{n}\right)(x)=\left|J_{T}(x)\right| \quad\left(x \in X_{n}\right) .
$$

To see this, fix $x \in X_{n}$, and note that $B(x, r) \subset V_{n}$ for all sufficiently small $r>0$, because $V_{n}$ is open. Since $V_{n}-X_{n} \subset V-X$, hypothesis (iii) enables us to replace $X_{n}$ by $V_{n}$ in (3) without changing $\mu_{n}(E)$. Hence, for small $r>0$,

$$
\mu_{n}(B(x, r))=m(T(B(x, r)))
$$

If we divide both sides of $(6)$ by $m(B(x, r))$ and refer to Theorem 7.24 and formula 7.22(6), we obtain (5).

Since (3) implies that $\mu_{n}(E)=\mu_{n}\left(E \cap X_{n}\right)$, it follows from (3), (4), and (5) that

$$
m\left(T\left(E \cap X_{n}\right)\right)=\int_{X_{n}} \chi_{E}\left|J_{T}\right| d m \quad(E \in \mathfrak{M})
$$

If we apply the monotone convergence theorem to (7), letting $n \rightarrow \infty$, we obtain (II).

We begin the proof of (III) by letting $A$ be a Borel set in $R^{k}$. Put

$$
E=T^{-1}(A)=\{x \in V: T(x) \in A\} .
$$

Then $\chi_{E}=\chi_{A} \circ T$. Since $\chi_{A}$ is a Borel function and $T$ is continuous, $\chi_{E}$ is a Borel function (Theorem 1.12), hence $E \in \mathfrak{M}$. Also

$$
T(E \cap X)=A \cap Y
$$

which implies, by (II), that

$$
\int_{Y} \chi_{A} d m=m(T(E \cap X))=\int_{X}\left(\chi_{A} \circ T\right)\left|J_{T}\right| d m
$$

Finally, if $N \in \mathfrak{M}$ and $m(N)=0$, there is a Borel set $A \supset N$ with $m(A)=0$. For this $A,(10)$ shows that $\left(\chi_{A} \circ T\right)\left|J_{T}\right|=0$ a.e. $[m]$. Since $0 \leq$ $\chi_{N} \leq \chi_{A}$, it follows that both integrals in (10) are 0 if $A$ is replaced by $N$. Since every Lebesgue measurable set is the disjoint union of a Borel set and a set of measure $0,(10)$ holds for every $A \in \mathfrak{M}$. This proves (III).

Once we have (III), it is clear that (1) holds for every nonnegative Lebesgue measurable simple function $f$. Another application of the monotone convergence theorem completes the proof.

Note that we did not prove that $f \circ T$ is Lebesgue measurable for all Lebesgue measurable $f$. It need not be; see Exercise 8. What the proof does establish is the Lebesgue measurability of the product $(f \circ T)\left|J_{T}\right|$.

Here is a special case of the theorem:

Suppose $\varphi:[a, b] \rightarrow[\alpha, \beta]$ is $\mathrm{AC}$, monotonic, $\varphi(a)=\alpha, \varphi(b)=\beta$, and $f \geq 0$ is Lebesgue measurable. Then

$$
\int_{\alpha}^{\beta} f(t) d t=\int_{a}^{b} f(\varphi(x)) \varphi^{\prime}(x) d x
$$

To derive this from Theorem 7.26, put $V=(a, b), T=\varphi$, let $\Omega$ be the union of the maximal segments on which $\varphi$ is constant (if there are any) and let $X$ be the set of all $x \in V-\Omega$ where $\varphi^{\prime}(x)$ exists (and is finite).

## Exercises

1 Show that $|f(x)| \leq(M f)(x)$ at every Lebesgue point of $f$ if $f \in L^{1}\left(R^{k}\right)$.

2 For $\delta>0$, let $I(\delta)$ be the segment $(-\delta, \delta) \subset R^{1}$. Given $\alpha$ and $\beta, 0 \leq \alpha \leq \beta \leq 1$, construct a measurable set $E \subset R^{1}$ so that the upper and lower limits of

$$
\frac{m(E \cap I(\delta))}{2 \delta}
$$

are $\beta$ and $\alpha$, respectively, as $\delta \rightarrow 0$.

(Compare this with Section 7.12.)

3 Suppose that $E$ is a measurable set of real numbers with arbitrarily small periods. Explicitly, this means that there are positive numbers $p_{i}$, converging to 0 as $i \rightarrow \infty$, so that

$$
E+p_{i}=E \quad(i=1,2,3, \ldots)
$$

Prove that then either $E$ or its complement has measure 0 .

Hint: Pick $\alpha \in R^{1}$, put $F(x)=m(E \cap[\alpha, x])$ for $x>\alpha$, show that

$$
F\left(x+p_{i}\right)-F\left(x-p_{i}\right)=F\left(y+p_{i}\right)-F\left(y-p_{i}\right)
$$

if $\alpha+p_{i}<x<y$. What does this imply about $F^{\prime}(x)$ if $m(E)>0$ ?

4 Call $t$ a period of the function $f$ on $R^{1}$ if $f(x+t)=f(x)$ for all $x \in R^{1}$. Suppose $f$ is a real Lebesgue measurable function with periods $s$ and $t$ whose quotient $s / t$ is irrational. Prove that there is a constant $c$ such that $f(x)=c$ a.e., but that $f$ need not be constant.

Hint: Apply Exercise 3 to the sets $\{f>\lambda\}$.

5 If $A \subset R^{1}$ and $B \subset R^{1}$, define $A+B=\{a+b: a \in A, b \in B\}$. Suppose $m(A)>0, m(B)>0$. Prove that $A+B$ contains a segment, by completing the following outline.

There are points $a_{0}$ and $b_{0}$ where $A$ and $B$ have metric density 1 . Choose a small $\delta>0$. Put $c_{0}=a_{0}+b_{0}$. For each $\epsilon$, positive or negative, define $B_{\epsilon}$ to be the set of all $c_{0}+\epsilon-b$ for which $b \in B$ and $\left|b-b_{0}\right|<\delta$. Then $B_{\epsilon} \subset\left(a_{0}+\epsilon-\delta, a_{0}+\epsilon+\delta\right)$. If $\delta$ was well chosen and $|\epsilon|$ is sufficiently small, it follows that $A$ intersects $B_{\epsilon}$, so that $A+B \supset\left(c_{0}-\epsilon_{0}, c_{0}+\epsilon_{0}\right)$ for some $\epsilon_{0}>0$.

Let $C$ be Cantor's "middle thirds" set and show that $C+C$ is an interval, although $m(C)=0$. (See also Exercise 19, Chap. 9.)

6 Suppose $G$ is a subgroup of $R^{1}$ (relative to addition), $G \neq R^{1}$, and $G$ is Lebesgue measurable. Prove that then $m(G)=0$.

Hint: Use Exercise 5.

7 Construct a continuous monotonic function $f$ on $R^{1}$ so that $f$ is not constant on any segment although $f^{\prime}(x)=0$ a.e.

8 Let $V=(a, b)$ be a bounded segment in $R^{1}$. Choose segments $W_{n} \subset V$ in such a way that their union $W$ is dense in $V$ and the set $K=V-W$ has $m(K)>0$. Choose continuous functions $\varphi_{n}$ so that $\varphi_{n}(x)=0$ outside $W_{n}, 0<\varphi_{n}(x)<2^{-n}$ in $W_{n}$. Put $\varphi=\sum \varphi_{n}$ and define

$$
T(x)=\int_{a}^{x} \varphi(t) d t \quad(a<x<b)
$$

Prove the following statements:

(a) $T$ satisfies the hypotheses of Theorem 7.26, with $X=V$.

(b) $T^{\prime}$ is continuous, $T^{\prime}(x)=0$ on $K, m(T(K))=0$.

(c) If $E$ is a nonmeasurable subset of $K$ (see Theorem 2.22) and $A=T(E)$, then $\chi_{A}$ is Lebesgue measurable but $\chi_{A} \circ T$ is not.

(d) The functions $\varphi_{n}$ can be so chosen that the resulting $T$ is an infinitely differentiable homeomorphism of $V$ onto some segment in $R^{1}$ and $(c)$ still holds.

9 Suppose $0<\alpha<1$. Pick $t$ so that $t^{\alpha}=2$. Then $t>2$, and the construction of Example $(b)$ in Sec. 7.16 can be carried out with $\delta_{n}=(2 / t)^{n}$. Show that the resulting function $f$ belongs to Lip $\alpha$ on $[0,1]$.

10 If $f \in \operatorname{Lip} 1$ on $[a, b]$, prove that $f$ is absolutely continuous and that $f^{\prime} \in L^{\infty}$.

11 Assume that $1<p<\infty, f$ is absolutely continuous on $[a, b], f^{\prime} \in L^{p}$, and $\alpha=1 / q$, where $q$ is the exponent conjugate to $p$. Prove that $f \in \operatorname{Lip} \alpha$.

12 Suppose $\varphi:[a, b] \rightarrow R^{1}$ is nondecreasing.

(a) Show that there is a left-continuous nondecreasing $f$ on $[a, b]$ so that $\{f \neq \varphi\}$ is at most countable. [Left-continuous means: if $a<x \leq b$ and $\epsilon>0$, then there is a $\delta>0$ so that $|f(x)-f(x-t)|<\epsilon$ whenever $0<t<\delta$.]

(b) Imitate the proof of Theorem 7.18 to show that there is a positive Borel measure $\mu$ on $[a, b]$ for which

$$
f(x)-f(a)=\mu([a, x)) \quad(a \leq x \leq b)
$$

(c) Deduce from $(b)$ that $f^{\prime}(x)$ exists a.e. $[m]$, that $f^{\prime} \in L^{1}(m)$, and that

$$
f(x)-f(a)=\int_{a}^{x} f^{\prime}(t) d t+s(x) \quad(a \leq x \leq b)
$$

where $s$ is nondecreasing and $s^{\prime}(x)=0$ a.e. $[m]$. $[a, b]$

(d) Show that $\mu \perp m$ if and only if $f^{\prime}(x)=0$ a.e. $[m]$, and that $\mu \ll m$ if and only if $f$ is AC on

(e) Prove that $\varphi^{\prime}(x)=f^{\prime}(x)$ a.e. $[m]$.

13 Let $B V$ be the class of all $f$ on $[a, b]$ that have bounded variation on $[a, b]$, as defined after Theorem 7.19. Prove the following statements.

(a) Every monotonic bounded function on $[a, b]$ is in $B V$

(b) If $f \in B V$ is real, there exist bounded monotonic functions $f_{1}$ and $f_{2}$ so that $f=f_{1}-f_{2}$.

Hint: Imitate the proof of Theorem 7.19.

(c) If $f \in B V$ is left-continuous then $f_{1}$ and $f_{2}$ can be chosen in (b) so as to be also leftcontinuous.

(d) If $f \in B V$ is left-continuous then there is a Borel measure $\mu$ on $[a, b]$ that satisfies

$$
f(x)-f(a)=\mu([a, x)) \quad(a \leq x \leq b)
$$

$\mu \ll m$ if and only if $f$ is $\mathrm{AC}$ on $[a, b]$.

(e) Every $f \in B V$ is differentiable a.e. $[m]$, and $f^{\prime} \in L^{1}(m)$.

14 Show that the product of two absolutely continuous functions on $[a, b]$ is absolutely continuous. Use this to derive a theorem about integration by parts.

15 Construct a monotonic function $f$ on $R^{1}$ so that $f^{\prime}(x)$ exists (finitely) for every $x \in R^{1}$, but $f^{\prime}$ is not a continuous function.

16 Suppose $E \subset[a, b], m(E)=0$. Construct an absolutely continuous monotonic function $f$ on $[a, b]$ so that $f^{\prime}(x)=\infty$ at every $x \in E$.

$H$ int $: E \subset \bigcap V_{n}, V_{n}$ open, $m\left(V_{n}\right) \subset 2^{-n}$. Consider the sum of the characteristic functions of these sets.

17 Suppose $\left\{\mu_{n}\right\}$ is a sequence of positive Borel measures on $R^{k}$ and

$$
\mu(E)=\sum_{n=1}^{\infty} \mu_{n}(E)
$$

Assume $\mu\left(R^{k}\right)<\infty$. Show that $\mu$ is a Borel measure. What is the relation between the Lebesgue decompositions of the $\mu_{n}$ and that of $\mu$ ?

Prove that

$$
(D \mu)(x)=\sum_{n=1}^{\infty}\left(D \mu_{n}\right)(x) \quad \text { a.e. }[m]
$$

Derive corresponding theorems for sequences $\left\{f_{n}\right\}$ of positive nondecreasing functions on $R^{1}$ and their sums $f=\sum f_{n}$.

18 Let $\varphi_{0}(t)=1$ on $[0,1), \varphi_{0}(t)=-1$ on $[1,2)$, extend $\varphi_{0}$ to $R^{1}$ so as to have period 2 , and define $\varphi_{n}(t)=\varphi_{0}\left(2^{n} t\right), n=1,2,3, \ldots$.

Assume that $\sum\left|c_{n}\right|^{2}<\infty$ and prove that the series

$$
\sum_{n=1}^{\infty} c_{n} \varphi_{n}(t)
$$

converges then for almost every $t$.

Probabilistic interpretation: The series $\sum\left( \pm c_{n}\right)$ converges with probability 1.

Suggestion: $\left\{\varphi_{n}\right\}$ is orthonormal on $[0,1]$, hence $(*)$ is the Fourier series of some $f \in L^{2}$. If $a=j \cdot 2^{-N}, b=(j+1) \cdot 2^{-N}, a<t<b$, and $s_{N}=c_{1} \varphi_{1}+\cdots+c_{N} \varphi_{N}$, then, for $n>N$,

$$
s_{N}(t)=\frac{1}{b-a} \int_{a}^{b} s_{N} d m=\frac{1}{b-a} \int_{a}^{b} s_{n} d m
$$

and the last integral converges to $\int_{a}^{b} f d m$, as $n \rightarrow \infty$. Show that $\left(^{*}\right)$ converges to $f(t)$ at almost every Lebesgue point of $f$.

19 Suppose $f$ is continuous on $R^{1}, f(x)>0$ if $0<x<1, f(x)=0$ otherwise. Define

$$
h_{c}(x)=\sup \left\{n^{c} f(n x): n=1,2,3, \ldots\right\}
$$

Prove that

(a) $h_{c}$ is in $L^{1}\left(R^{1}\right)$ if $0<c<1$,

(b) $h_{1}$ is in weak $L^{1}$ but not in $L^{1}\left(R^{1}\right)$,

(c) $h_{c}$ is not in weak $L^{1}$ if $c>1$.

20 (a) For any set $E \subset R^{2}$, the boundary $\partial E$ of $E$ is, by definition, the closure of $E$ minus the interior of $E$. Show that $E$ is Lebesgue measurable whenever $m(\partial E)=0$.

(b) Suppose that $E$ is the union of a (possibly uncountable) collection of closed discs in $R^{2}$ whose radii are at least 1 . Use $(a)$ to show that $E$ is Lebesgue measurable.

(c) Show that the conclusion of $(b)$ is true even when the radii are unrestricted.

(d) Show that some unions of closed discs of radius 1 are not Borel sets. (See Sec. 2.21.)

(e) Can discs be replaced by triangles, rectangles, arbitrary polygons, etc., in all this? What is the relevant geometric property?

21 If $f$ is a real function on $[0,1]$ and

$$
\gamma(t)=t+\mathrm{if}(t)
$$

the length of the graph of $f$ is, by definition, the total variation of $\gamma$ on $[0,1]$. Show that this length is finite if and only if $f \in B V$. (See Exercise 13.) Show that it is equal to

$$
\int_{0}^{1} \sqrt{1+\left[f^{\prime}(t)\right]^{2}} d t
$$

if $f$ is absolutely continuous.

22 (a) Assume that both $f$ and its maximal function $M f$ are in $L^{1}\left(R^{k}\right)$. Prove that then $f(x)=0$ a.e. $[m]$. Hint: To every other $f \in L^{1}\left(R^{k}\right)$ corresponds a constant $c=c(f)>0$ such that

$$
(M f)(x) \geq c|x|^{-k}
$$

whenever $|x|$ is sufficiently large.

(b) Define $f(x)=x^{-1}(\log x)^{-2}$ if $0<x<\frac{1}{2}, f(x)=0$ on the rest of $R^{1}$. Then $f \in L^{1}\left(R^{1}\right)$. Show that

$$
(M f)(x) \geq|2 x \log (2 x)|^{-1} \quad(0<x<1 / 4)
$$

so that $\int_{0}^{1}(M f)(x) d x=\infty$.

23 The definition of Lebesgue points, as made in Sec. 7.6, applies to individual integrable functions, not to the equivalence classes discussed in Sec. 3.10. However, if $F \in L^{1}\left(R^{k}\right)$ is one of these equivalence classes, one may call a point $x \in R^{k}$ a Lebesgue point of $F$ if there is a complex number, let us call it $(S F)(x)$, such that

$$
\lim _{r \rightarrow 0} \frac{1}{m\left(B_{r}\right)} \int_{B(x, r)}|f-(S F)(x)| d m=0
$$

for one (hence for every) $f \in F$.

Define $(S F)(x)$ to be 0 at those points $x \in R^{k}$ that are not Lebesgue points of $F$

Prove the following statement: If $f \in F$, and $x$ is a Lebesgue point of $f$, then $x$ is also a Lebesgue point of $F$, and $f(x)=(S F)(x)$. Hence $S F \in F$.

Thus $S$ "selects" a member of $F$ that has a maximal set of Lebesgue points.

## INTEGRATION ON PRODUCT SPACES

This chapter is devoted to the proof and discussion of the theorem of Fubini concerning integration of functions of two variables. We first present the theorem in its abstract form.

## Measurability on Cartesian Products

8.1 Definitions If $X$ and $Y$ are two sets, their cartesian product $X \times Y$ is the set of all ordered pairs $(x, y)$, with $x \in X$ and $y \in Y$. If $A \subset X$ and $B \subset Y$, it follows that $A \times B \subset X \times Y$. We call any set of the form $A \times B$ a rectangle in $X \times Y$.

Suppose now that $(X, \mathscr{S})$ and $(Y, \mathscr{T})$ are measurable spaces. Recall that this simply means that $\mathscr{S}$ is a $\sigma$-algebra in $X$ and $\mathscr{T}$ is a $\sigma$-algebra in $Y$.

A measurable rectangle is any set of the form $A \times B$, where $A \in \mathscr{S}$ and $B \in \mathscr{T}$.

If $Q=R_{1} \cup \cdots \cup R_{n}$, where each $R_{i}$ is a measurable rectangle and $R_{i} \cap$ $R_{j}=\varnothing$ for $i \neq j$, we say that $Q \in \mathscr{E}$, the class of all elementary sets.

$\mathscr{S} \times \mathscr{T}$ is defined to be the smallest $\sigma$-algebra in $X \times Y$ which contains every measurable rectangle.

A monotone class $\mathfrak{M}$ is a collection of sets with the following properties: If $A_{i} \in \mathfrak{M}, B_{i} \in \mathfrak{M}, A_{i} \subset A_{i+1}, B_{i} \supset B_{i+1}$, for $i=1,2,3, \ldots$, and if

$$
A=\bigcup_{i=1}^{\infty} A_{i}, \quad B=\bigcap_{i=1}^{\infty} B_{i}
$$

then $A \in \mathfrak{M}$ and $B \in \mathfrak{M}$.

If $E \subset X \times Y, x \in X, y \in Y$, we define

$$
E_{x}=\{y:(x, y) \in E\}, \quad E^{y}=\{x:(x, y) \in E\}
$$

We call $E_{x}$ and $E^{y}$ the $x$-section and $y$-section, respectively, of $E$. Note that $E_{x} \subset Y, E^{y} \subset X$.

8.2 Theorem If $E \in \mathscr{S} \times \mathscr{T}$, then $E_{x} \in \mathscr{T}$ and $E^{y} \in \mathscr{S}$, for every $x \in X$ and $y \in Y$.

ProOF Let $\Omega$ be the class of all $E \in \mathscr{S} \times \mathscr{T}$ such that $E_{x} \in \mathscr{T}$ for every $x \in X$. If $E=A \times B$, then $E_{x}=B$ if $x \in A, E_{x}=\varnothing$ if $x \notin A$. Therefore every measurable rectangle belongs to $\Omega$. Since $\mathscr{T}$ is a $\sigma$-algebra, the following three statements are true. They prove that $\Omega$ is a $\sigma$-algebra and hence that $\Omega=\mathscr{S} \times \mathscr{T}:$

(a) $X \times Y \in \Omega$.

(b) If $E \in \Omega$, then $\left(E^{c}\right)_{x}=\left(E_{x}\right)^{c}$, hence $E^{c} \in \Omega$.

(c) If $E_{i} \in \Omega(i=1,2,3, \ldots)$ and $E=\bigcup E_{i}$, then $E_{x}=\bigcup\left(E_{i}\right)_{x}$, hence $E \in \Omega$.

The proof is the same for $E^{y}$.

8.3 Theorem $\mathscr{S} \times \mathscr{T}$ is the smallest monotone class which contains all elementary sets.

ProOF Let $\mathfrak{M}$ be the smallest monotone class which contains $\mathscr{E}$; the proof that this class exists is exactly like that of Theorem 1.10. Since $\mathscr{S} \times \mathscr{T}$ is a monotone class, we have $\mathfrak{M} \subset \mathscr{S} \times \mathscr{T}$.

The identities

$$
\begin{aligned}
& \left(A_{1} \times B_{1}\right) \cap\left(A_{2} \times B_{2}\right)=\left(A_{1} \cap A_{2}\right) \times\left(B_{1} \cap B_{2}\right) \\
& \left(A_{1} \times B_{1}\right)-\left(A_{2} \times B_{2}\right)=\left[\left(A_{1}-A_{2}\right) \times B_{1}\right] \cup\left[\left(A_{1} \cap A_{2}\right) \times\left(B_{1}-B_{2}\right)\right]
\end{aligned}
$$

show that the intersection of two measurable rectangles is a measurable rectangle and that their difference is the union of two disjoint measurable rectangles, hence is an elementary set. If $P \in \mathscr{E}$ and $Q \in \mathscr{E}$, it follows easily that $P \cap Q \in \mathscr{E}$ and $P-Q \in \mathscr{E}$. Since

$$
P \cup Q=(P-Q) \cup Q
$$

and $(P-Q) \cap Q=\varnothing$, we also have $P \cup Q \in \mathscr{E}$.

For any set $P \subset X \times Y$, define $\Omega(P)$ to be the class of all $Q \subset X \times Y$ such that $P-Q \in \mathfrak{M}, Q-P \in \mathfrak{M}$, and $P \cup Q \in \mathfrak{M}$. The following properties are obvious:

(a) $Q \in \Omega(P)$ if and only if $P \in \Omega(Q)$.

(b) Since $\mathfrak{M}$ is a monotone class, so is each $\Omega(P)$.

Fix $P \in \mathscr{E}$. Our preceding remarks about $\mathscr{E}$ show that $Q \in \Omega(P)$ for all $Q \in \mathscr{E}$, hence $\mathscr{E} \subset \Omega(P)$, and now $(b)$ implies that $\mathfrak{M} \subset \Omega(P)$.

Next, fix $Q \in \mathfrak{M}$. We just saw that $Q \in \Omega(P)$ if $P \in \mathscr{E}$. By $(a), P \in \Omega(Q)$, hence $\mathscr{E} \subset \Omega(Q)$, and if we refer to $(b)$ once more we obtain $\mathfrak{M} \subset \Omega(Q)$.

Summing up: If $P$ and $Q \in \mathfrak{M}$, then $P-Q \in \mathfrak{M}$ and $P \cup Q \in \mathfrak{M}$.

It now follows that $\mathfrak{M}$ is a $\sigma$-algebra in $X \times Y$ :

(i) $X \times Y \in \mathscr{E}$. Hence $X \times Y \in \mathfrak{M}$.

(ii) If $Q \in \mathfrak{M}$, then $Q^{c} \in \mathfrak{M}$, since the difference of any two members of $\mathfrak{M}$ is in $\mathfrak{M}$.

(iii) If $P_{i} \in \mathfrak{M}$ for $i=1,2,3, \ldots$, and $P=\bigcup P_{i}$, put

$$
Q_{n}=P_{1} \cup \cdots \cup P_{n} .
$$

Since $\mathfrak{M}$ is closed under the formation of finite unions, $Q_{n} \in \mathfrak{M}$.

Since $Q_{n} \subset Q_{n+1}$ and $P=\bigcup Q_{n}$, the monotonicity of $\mathfrak{M}$ shows that $P \in \mathfrak{M}$.

Thus $\mathfrak{M}$ is a $\sigma$-algebra, $\mathscr{E} \subset \mathfrak{M} \subset \mathscr{S} \times \mathscr{T}$, and (by definition) $\mathscr{S} \times \mathscr{T}$ is the smallest $\sigma$-algebra which contains $\mathscr{E}$. Hence $\mathfrak{M}=\mathscr{S} \times \mathscr{T}$.

8.4 Definition With each function $f$ on $X \times Y$ and with each $x \in X$ we associate a function $f_{x}$ defined on $Y$ by $f_{x}(y)=f(x, y)$.

Similarly, if $y \in Y, f^{y}$ is the function defined on $X$ by $f^{y}(x)=f(x, y)$.

Since we are now dealing with three $\sigma$-algebras, $\mathscr{S}, \mathscr{T}$, and $\mathscr{S} \times \mathscr{T}$, we shall, for the sake of clarity, indicate in the sequel to which of these three $\sigma$-algebras the word "measurable" refers.

8.5 Theorem Let $f$ be an $(\mathscr{S} \times \mathscr{T})$-measurable function on $X \times Y$. Then

(a) For each $x \in X, f_{x}$ is a $\mathscr{T}$-measurable function.

(b) For each $y \in Y, f^{y}$ is an $\mathscr{S}$-measurable function.

Proof For any open set $V$, put

$$
Q=\{(x, y): f(x, y) \in V\}
$$

Then $Q \in \mathscr{S} \times \mathscr{T}$, and

$$
Q_{x}=\left\{y: f_{x}(y) \in V\right\} .
$$

Theorem 8.2 shows that $Q_{x} \in \mathscr{T}$. This proves $(a)$; the proof of $(b)$ is similar.

## Product Measures

8.6 Theorem Let $(X, \mathscr{S}, \mu)$ and $(Y, \mathscr{T}, \lambda)$ be $\sigma$-finite measure spaces. Suppose $Q \in \mathscr{S} \times \mathscr{T}$. If

$$
\varphi(x)=\lambda\left(Q_{x}\right), \quad \psi(y)=\mu\left(Q^{y}\right)
$$

for every $x \in X$ and $y \in Y$, then $\varphi$ is $\mathscr{S}$-measurable, $\psi$ is $\mathscr{T}$-measurable, and

$$
\int_{X} \varphi d \mu=\int_{Y} \psi d \lambda
$$

Notes: The assumptions on the measure spaces are, more explicitly, that $\mu$ and $\lambda$ are positive measures on $\mathscr{S}$ and $\mathscr{T}$, respectively, that $X$ is the union of countably many disjoint sets $X_{n}$ with $\mu\left(X_{n}\right)<\infty$, and that $Y$ is the union of countably many disjoint sets $Y_{m}$ with $\lambda\left(Y_{m}\right)<\infty$.

Theorem 8.2 shows that the definitions (1) make sense. Since

$$
\lambda\left(Q_{x}\right)=\int_{Y} \chi_{Q}(x, y) d \lambda(y) \quad(x \in X)
$$

with a similar statement for $\mu\left(Q^{y}\right)$, the conclusion (2) can be written in the form

$$
\int_{X} d \mu(x) \int_{Y} \chi_{Q}(x, y) d \lambda(y)=\int_{Y} d \lambda(y) \int_{X} \chi_{Q}(x, y) d \mu(x)
$$

ProOF Let $\Omega$ be the class of all $Q \in \mathscr{S} \times \mathscr{T}$ for which the conclusion of the theorem holds. We claim that $\Omega$ has the following four properties:

(a) Every measurable rectangle belongs to $\Omega$.

(b) If $Q_{1} \subset Q_{2} \subset Q_{3} \subset \cdots$, if each $Q_{i} \in \Omega$, and if $Q=\bigcup Q_{i}$, then $Q \in \Omega$.

(c) If $\left\{Q_{i}\right\}$ is a disjoint countable collection of members of $\Omega$, and if $Q=\bigcup Q_{i}$, then $Q \in \Omega$.

(d) If $\mu(A)<\infty$ and $\lambda(B)<\infty$, if $A \times B \supset Q_{1} \supset Q_{2} \supset Q_{3} \supset \cdots$, if $Q=\bigcap Q_{i}$ and $Q_{i} \in \Omega$ for $i=1,2,3, \ldots$, then $Q \in \Omega$.

If $Q=A \times B$, where $A \in \mathscr{S}, B \in \mathscr{T}$, then

$$
\lambda\left(Q_{x}\right)=\lambda(B) \chi_{A}(x) \quad \text { and } \quad \mu\left(Q^{y}\right)=\mu(A) \chi_{B}(y)
$$

and therefore each of the integrals in (2) is equal to $\mu(A) \lambda(B)$. This gives $(a)$.

To prove $(b)$, let $\varphi_{i}$ and $\psi_{i}$ be associated with $Q_{i}$ in the way in which (1) associates $\varphi$ and $\psi$ with $Q$. The countable additivity of $\mu$ and $\lambda$ shows that

$$
\varphi_{i}(x) \rightarrow \varphi(x), \quad \psi_{i}(y) \rightarrow \psi(y) \quad(i \rightarrow \infty)
$$

the convergence being monotone increasing at every point. Since $\varphi_{i}$ and $\psi_{i}$ are assumed to satisfy the conclusion of the theorem, $(b)$ follows from the monotone convergence theorem.

For finite unions of disjoint sets, $(c)$ is clear, because the characteristic function of a union of disjoint sets is the sum of their characteristic functions. The general case of $(c)$ now follows from $(b)$.

The proof of $(d)$ is like that of $(b)$, except that we use the dominated convergence theorem in place of the monotone convergence theorem. This is legitimate, since $\mu(A)<\infty$ and $\lambda(B)<\infty$.

Now define

$$
Q_{m n}=Q \cap\left(X_{n} \times Y_{m}\right) \quad(m, n=1,2,3, \ldots)
$$

and let $\mathfrak{M}$ be the class of all $Q \in \mathscr{S} \times \mathscr{T}$ such that $Q_{m n} \in \Omega$ for all choices of $m$ and $n$. Then $(b)$ and $(d)$ show that $\mathfrak{M}$ is a monotone class; $(a)$ and $(c)$ show that $\mathscr{E} \subset \mathfrak{M}$; and since $\mathfrak{M} \subset \mathscr{S} \times \mathscr{T}$, Theorem 8.3 implies that $\mathfrak{M}=\mathscr{S} \times \mathscr{T}$.

Thus $Q_{m n} \in \Omega$ for every $Q \in \mathscr{S} \times \mathscr{T}$ and for all choices of $m$ and $n$. Since $Q$ is the union of the sets $Q_{m n}$ and since these sets are disjoint, we conclude from (c) that $Q \in \Omega$. This completes the proof.

8.7 Definition If $(X, \mathscr{S}, \mu)$ and $(Y, \mathscr{T}, \lambda)$ are as in Theorem 8.6, and if $Q \in \mathscr{S} \times \mathscr{T}$, we define

$$
(\mu \times \lambda)(Q)=\int_{X} \lambda\left(Q_{x}\right) d \mu(x)=\int_{Y} \mu\left(Q^{y}\right) d \lambda(y)
$$

The equality of the integrals in (1) is the content of Theorem 8.6. We call $\mu \times \lambda$ the product of the measures $\mu$ and $\lambda$. That $\mu \times \lambda$ is really a measure (i.e., that $\mu \times \lambda$ is countably additive on $\mathscr{S} \times \mathscr{T}$ ) follows immediately from Theorem 1.27.

Observe also that $\mu \times \lambda$ is $\sigma$-finite.

## The Fubini Theorem

8.8 Theorem Let $(X, \mathscr{S}, \mu)$ and $(Y, \mathscr{T}, \lambda)$ be $\sigma$-finite measure spaces, and let $f$ be an $(\mathscr{S} \times \mathscr{T})$-measurable function on $X \times Y$.

(a) If $0 \leq f \leq \infty$, and if

$$
\varphi(x)=\int_{Y} f_{x} d \lambda, \quad \psi(y)=\int_{X} f^{y} d \mu \quad(x \in X, y \in Y)
$$

then $\varphi$ is $\mathscr{S}$-measurable, $\psi$ is $\mathscr{T}$-measurable, and

$$
\int_{X} \varphi d \mu=\int_{X \times Y} f d(\mu \times \lambda)=\int_{Y} \psi d \lambda .
$$

(b) If $f$ is complex and if

$$
\varphi^{*}(x)=\int_{Y}|f|_{x} d \lambda \text { and } \int_{X} \varphi^{*} d \mu<\infty
$$

then $f \in L^{1}(\mu \times \lambda)$.
(c) If $f \in L^{1}(\mu \times \lambda)$, then $f_{x} \in L^{1}(\lambda)$ for almost all $x \in X, f^{y} \in L^{1}(\mu)$ for almost all $y \in Y$; the functions $\varphi$ and $\psi$, defined by (1) a.e., are in $L^{1}(\mu)$ and $L^{1}(\lambda)$, respectively, and (2) holds.

Notes: The first and last integrals in (2) can also be written in the more usual form

$$
\int_{X} d \mu(x) \int_{Y} f(x, y) d \lambda(y)=\int_{Y} d \lambda(y) \int_{X} f(x, y) d \mu(x)
$$

These are the so-called "iterated integrals" of $f$. The middle integral in (2) is often referred to as a double integral.

The combination of $(b)$ and $(c)$ gives the following useful result: If $f$ is $(\mathscr{S} \times \mathscr{T})$-measurable and if

$$
\int_{X} d \mu(x) \int_{Y}|f(x, y)| d \lambda(y)<\infty
$$

then the two iterated integrals (4) are finite and equal.

In other words, "the order of integration may be reversed" for $(\mathscr{S} \times \mathscr{T})$ measurable functions $f$ whenever $f \geq 0$ and also whenever one of the iterated integrals of $|f|$ is finite.

Proof We first consider (a). By Theorem 8.5, the definitions of $\varphi$ and $\psi$ make sense. Suppose $Q \in \mathscr{S} \times \mathscr{T}$ and $f=\chi_{Q}$. By Definition 8.7, (2) is then exactly the conclusion of Theorem 8.6. Hence $(a)$ holds for all nonnegative simple $(\mathscr{S} \times \mathscr{T})$-measurable functions $s$. In the general case, there is a sequence of such functions $s_{n}$, such that $0 \leq s_{1} \leq s_{2} \leq \cdots$ and $s_{n}(x, y) \rightarrow$ $f(x, y)$ at every point of $X \times Y$. If $\varphi_{n}$ is associated with $s_{n}$ in the same way in which $\varphi$ was associated to $f$, we have

$$
\int_{X} \varphi_{n} d \mu=\int_{X \times Y} s_{n} d(\mu \times \lambda) \quad(n=1,2,3, \ldots)
$$

The monotone convergence theorem, applied on $(Y, \mathscr{T}, \lambda)$, shows that $\varphi_{n}(x)$ increases to $\varphi(x)$, for every $x \in X$, as $n \rightarrow \infty$. Hence the monotone convergence theorem applies again, to the two integrals in (6), and the first equality (2) is obtained. The second half of (2) follows by interchanging the roles of $x$ and $y$. This completes $(a)$.

If we apply $(a)$ to $|f|$, we see that $(b)$ is true.

Obviously, it is enough to prove (c) for real $L^{1}(\mu \times \lambda)$; the complex case then follows. If $f$ is real, $(a)$ applies to $f^{+}$and to $f^{-}$. Let $\varphi_{1}$ and $\varphi_{2}$ correspond to $f^{+}$and $f^{-}$as $\varphi$ corresponds to $f$ in (1). Since $f \in L^{1}(\mu \times \lambda)$ and
$f^{+} \leq|f|$, and since $(a)$ holds for $f^{+}$, we see that $\varphi_{1} \in L^{1}(\mu)$. Similarly, $\varphi_{2} \in$ $L^{1}(\mu)$. Since

$$
f_{x}=\left(f^{+}\right)_{x}-\left(f^{-}\right)_{x}
$$

we have $f_{x} \in L^{1}(\lambda)$ for every $x$ for which $\varphi_{1}(x)<\infty$ and $\varphi_{2}(x)<\infty$; since $\varphi_{1}$ and $\varphi_{2}$ are in $L^{1}(\mu)$, this happens for almost all $x$; and at any such $x$, we have $\varphi(x)=\varphi_{1}(x)-\varphi_{2}(x)$. Hence $\varphi \in L^{1}(\mu)$. Now (2) holds with $\varphi_{1}$ and $f^{+}$and with $\varphi_{2}$ and $f^{-}$, in place of $\varphi$ and $f$; if we subtract the resulting equations, we obtain one half of $(c)$. The other half is proved in the same manner, with $f^{y}$ and $\psi$ in place of $f_{x}$ and $\varphi$.

8.9 Counterexamples The following three examples will show that the various hypotheses in Theorems 8.6 and 8.8 cannot be dispensed with.

(a) Let $X=Y=[0,1], \mu=\lambda=$ Lebesgue measure on $[0,1]$. Choose $\left\{\delta_{n}\right\}$ so that $0=\delta_{1}<\delta_{2}<\delta_{3}<\cdots, \delta_{n} \rightarrow 1$, and let $g_{n}$ be a real continuous function with support in $\left(\delta_{n}, \delta_{n+1}\right)$, such that $\int_{0}^{1} g_{n}(t) d t=1$, for $n=1,2,3, \ldots$. Define

$$
f(x, y)=\sum_{n=1}^{\infty}\left[g_{n}(x)-g_{n+1}(x)\right] g_{n}(y)
$$

Note that at each point $(x, y)$ at most one term in this sum is different from 0 . Thus no convergence problem arises in the definition of $f$. An easy computation shows that

$$
\int_{0}^{1} d x \int_{0}^{1} f(x, y) d y=1 \neq 0=\int_{0}^{1} d y \int_{0}^{1} f(x, y) d x
$$

so that the conclusion of the Fubini theorem fails, although both iterated integrals exist. Note that $f$ is continuous in this example, except at the point $(1,1)$, but that

$$
\int_{0}^{1} d x \int_{0}^{1}|f(x, y)| d y=\infty
$$

(b) Let $X=Y=[0,1], \mu=$ Lebesgue measure on $[0,1], \lambda=$ counting measure on $Y$, and put $f(x, y)=1$ if $x=y, f(x, y)=0$ if $x \neq y$. Then

$$
\int_{X} f(x, y) d \mu(x)=0, \quad \int_{Y} f(x, y) d \lambda(y)=1
$$

for all $x$ and $y$ in $[0,1]$, so that

$$
\int_{Y} d \lambda(y) \int_{X} f(x, y) d \mu(x)=0 \neq 1=\int_{X} d \mu(x) \int_{Y} f(x, y) d \lambda(y) .
$$

This time the failure is due to the fact that $\lambda$ is not $\sigma$-finite.

Observe that our function $f$ is $(\mathscr{S} \times \mathscr{T})$-measurable, if $\mathscr{S}$ is the class of all Lebesgue measurable sets in $[0,1]$ and $\mathscr{T}$ consists of all subsets of $[0,1]$.

To see this, note that $f=\chi_{D}$, where $D$ is the diagonal of the unit square. Given $n$, put

$$
I_{j}=\left[\frac{j-1}{n}, \frac{j}{n}\right]
$$

and put

$$
Q_{n}=\left(I_{1} \times I_{1}\right) \cup\left(I_{2} \times I_{2}\right) \cup \cdots \cup\left(I_{n} \times I_{n}\right) .
$$

Then $Q_{n}$ is a finite union of measurable rectangles, and $D=\bigcap Q_{n}$.

(c) In examples $(a)$ and $(b)$, the failure of the Fubini theorem was due to the fact that either the function or the space was "too big." We now turn to the role played by the requirement that $f$ be measurable with respect to the $\sigma$-algebra $\mathscr{S} \times \mathscr{T}$.

To pose the question more precisely, suppose $\mu(X)=\lambda(Y)=1,0 \leq f \leq 1$ (so that "bigness" is certainly avoided); assume $f_{x}$ is $\mathscr{T}$-measurable and $f^{y}$ is $\mathscr{S}$-measurable, for all $x$ and $y$; and assume $\varphi$ is $\mathscr{S}$-measurable and $\psi$ is $\mathscr{T}$-measurable, where $\varphi$ and $\psi$ are defined as in 8.8(1). Then $0 \leq \varphi \leq 1$, $0 \leq \psi \leq 1$, and both iterated integrals are finite. (Note that no reference to product measures is needed to define iterated integrals.) Does it follow that the two iterated integrals of $f$ are equal?

The (perhaps surprising) answer is no.

In the following example (due to Sierpinski), we take

$$
(X, \mathscr{S}, \mu)=(Y, \mathscr{T}, \lambda)=[0,1]
$$

with Lebesgue measure. The construction depends on the continuum hypothesis. It is a consequence of this hypothesis that there is a one-to-one mapping $j$ of the unit interval $[0,1]$ onto a well-ordered set $W$ such that $j(x)$ has at most countably many predecessors in $W$, for each $x \in[0,1]$. Taking this for granted, let $Q$ be the set of all $(x, y)$ in the unit square such that $j(x)$ precedes $j(y)$ in $W$. For each $x \in[0,1], Q_{x}$ contains all but countably many points of $[0,1]$; for each $y \in[0,1], Q^{y}$ contains at most countably many points of $[0,1]$. If $f=\chi_{Q}$, it follows that $f_{x}$ and $f^{y}$ are Borel measurable and that

$$
\varphi(x)=\int_{0}^{1} f(x, y) d y=1, \quad \psi(y)=\int_{0}^{1} f(x, y) d x=0
$$

for all $x$ and $y$. Hence

$$
\int_{0}^{1} d x \int_{0}^{1} f(x, y) d y=1 \neq 0=\int_{0}^{1} d y \int_{0}^{1} f(x, y) d x
$$

## Completion of Product Measures

8.10 If $(X, \mathscr{S}, \mu)$ and $(Y, \mathscr{T}, \lambda)$ are complete measure spaces, it need not be true that $(X \times Y, \mathscr{S} \times \mathscr{T}, \mu \times \lambda)$ is complete. There is nothing pathological about
this phenomenon: Suppose that there exists an $A \in \mathscr{S}, A \neq \varnothing$, with $\mu(A)=0$; and suppose that there exists a $B \subset Y$ so that $B \notin \mathscr{T}$. Then $A \times B \subset A \times Y$, $(\mu \times \lambda)(A \times Y)=0$, but $A \times B \notin \mathscr{S} \times \mathscr{T}$. (The last assertion follows from Theorem 8.2.)

For instance, if $\mu=\lambda=m_{1}$ (Lebesgue measure on $R^{1}$ ), let $A$ consist of any one point, and let $B$ be any nonmeasurable set in $R^{1}$. Thus $m_{1} \times m_{1}$ is not a complete measure; in particular, $m_{1} \times m_{1}$ is not $m_{2}$, since the latter is complete, by its construction. However, $m_{2}$ is the completion of $m_{1} \times m_{1}$. This result generalizes to arbitrary dimensions:

8.11 Theorem Let $m_{k}$ denote Lebesgue measure on $R^{k}$. If $k=r+s, r \geq 1$, $s \geq 1$, then $m_{k}$ is the completion of the product measure $m_{r} \times m_{s}$.

PROOF Let $\mathscr{B}_{k}$ and $\mathfrak{M}_{k}$ be the $\sigma$-algebras of all Borel sets and of all Lebesgue measurable sets in $R^{k}$, respectively. We shall first show that

$$
\mathscr{B}_{k} \subset \mathfrak{M}_{r} \times \mathfrak{M}_{s} \subset \mathfrak{M}_{k}
$$

Every $k$-cell belongs to $\mathfrak{M}_{r} \times \mathfrak{M}_{s}$. The $\sigma$-algebra generated by the $k$-cells is $\mathscr{B}_{k}$. Hence $\mathscr{B}_{k} \subset \mathfrak{M}_{r} \times \mathfrak{M}_{s}$. Next, suppose $E \in \mathfrak{M}_{r}$ and $F \in \mathfrak{M}_{s}$. It is easy to see, by Theorem $2.20(b)$, that both $E \times R^{s}$ and $R^{r} \times F$ belong to $\mathfrak{M}_{k}$. The same is true of their intersection $E \times F$. It follows that $\mathfrak{M}_{r} \times \mathfrak{M}_{s} \subset \mathfrak{M}_{k}$.

Choose $Q \in \mathfrak{M}_{r} \times \mathfrak{M}_{s}$. Then $Q \in \mathfrak{M}_{k}$, so there are sets $\boldsymbol{P}_{1}$ and $\boldsymbol{P}_{2} \in \mathscr{B}_{k}$ such that $P_{1} \subset Q \subset P_{2}$ and $m_{k}\left(P_{2}-P_{1}\right)=0$. Both $m_{k}$ and $m_{r} \times m_{s}$ are translation invariant Borel measures on $R^{k}$. They assign the same value to each $k$-cell. Hence they agree on $\mathscr{B}_{k}$, by Theorem $2.20(d)$. In particular,

$$
\left(m_{r} \times m_{s}\right)\left(Q-P_{1}\right) \leq\left(m_{r} \times m_{s}\right)\left(P_{2}-P_{1}\right)=m_{k}\left(P_{2}-P_{1}\right)=0
$$

and therefore

$$
\left(m_{r} \times m_{s}\right)(Q)=\left(m_{r} \times m_{s}\right)\left(P_{1}\right)=m_{k}\left(P_{1}\right)=m_{k}(Q)
$$

So $m_{r} \times m_{s}$ agrees with $m_{k}$ on $\mathfrak{M}_{r} \times \mathfrak{M}_{s}$.

It now follows that $\mathfrak{M}_{k}$ is the $\left(m_{r} \times m_{s}\right)$-completion of $\mathfrak{M}_{r} \times \mathfrak{M}_{s}$, and this is what the theorem asserts.

We conclude this section with an alternative statement of Fubini's theorem which is of special interest in view of Theorem 8.11.

8.12 Theorem Let $(X, \mathscr{S}, \mu)$ and $(Y, \mathscr{T}, \lambda)$ be complete $\sigma$-finite measure spaces. Let $(\mathscr{S} \times \mathscr{T})^{*}$ be the completion of $\mathscr{S} \times \mathscr{T}$, relative to the measure $\mu \times \lambda$. Let $f$ be an $(\mathscr{S} \times \mathscr{T})^{*}$-measurable function on $X \times Y$. Then all conclusions of Theorem 8.8 hold, the only difference being as follows:

The $\mathscr{T}$-measurability of $f_{x}$ can be asserted only for almost all $x \in X$, so that $\varphi(x)$ is only defined a.e. $[\mu]$ by 8.8(1); a similar statement holds for $f^{y}$ and $\psi$.

The proof depends on the following two lemmas:

Lemma 1 Suppose $v$ is a positive measure on a $\sigma$-algebra $\mathfrak{M}, \mathfrak{M} *$ is the completion of $\mathfrak{M}$ relative to $v$, and $f$ is an $\mathfrak{M}^{*}$-measurable function. Then there exists an $\mathfrak{M}$-measurable function $g$ such that $f=g$ a.e. $[v]$.

(An interesting special case of this arises when $v$ is Lebesgue measure on $R^{k}$ and $\mathfrak{M}$ is the class of all Borel sets in $R^{k}$.)

Lemma 2 Let $h$ be an $(\mathscr{S} \times \mathscr{T})^{*}$-measurable function on $X \times Y$ such that $h=0$ a.e. $[\mu \times \lambda]$. Then for almost all $x \in X$ it is true that $h(x, y)=0$ for almost all $y \in Y$; in particular, $h_{x}$ is $\mathscr{T}$-measurable for almost all $x \in X . A$ similar statement holds for $h^{\boldsymbol{y}}$.

If we assume the lemmas, the proof of the theorem is immediate: If $f$ is as in the theorem, Lemma 1 (with $v=\mu \times \lambda$ ) shows that $f=g+h$, where $h=0$ a.e. $[\mu \times \lambda]$ and $g$ is $(\mathscr{S} \times \mathscr{T})$-measurable. Theorem 8.8 applies to $g$. Lemma 2 shows that $f_{x}=g_{x}$ a.e. $[\lambda]$ for almost all $x$ and that $f^{y}=g^{y}$ a.e. $[\mu]$ for almost all $y$. Hence the two iterated integrals of $f$, as well as the double integral, are the same as those of $g$, and the theorem follows.

Proof OF Lemma 1 Suppose $f$ is $\mathfrak{M}^{*}$-measurable and $f \geq 0$. There exist $\mathfrak{M}_{\text {*- }}$ measurable simple functions $0=s_{0} \leq s_{1} \leq s_{2} \leq \cdots$ such that $s_{n}(x) \rightarrow f(x)$ for each $x \in X$, as $n \rightarrow \infty$. Hence $f=\sum\left(s_{n+1}-s_{n}\right)$. Since $s_{n+1}-s_{n}$ is a finite linear combination of characteristic functions, it follows that there are constants $c_{i}>0$ and sets $E_{i} \in \mathfrak{M}^{*}$ such that

$$
f(x)=\sum_{i=1}^{\infty} c_{i} \chi_{E_{i}}(x) \quad(x \in X)
$$

The definition of $\mathfrak{M}^{*}$ (see Theorem 1.36) shows that there are sets $A_{i} \in \mathfrak{M}$, $B_{i} \in \mathfrak{M}$, such that $A_{i} \subset E_{i} \subset B_{i}$ and $v\left(B_{i}-A_{i}\right)=0$. Define

$$
g(x)=\sum_{i=1}^{\infty} c_{i} \chi_{A_{i}}(x) \quad(x \in X)
$$

Then the function $g$ is $\mathfrak{M}$-measurable, and $g(x)=f(x)$, except possibly when $x \in \bigcup\left(E_{i}-A_{i}\right) \subset \bigcup\left(B_{i}-A_{i}\right)$. Since $v\left(B_{i}-A_{i}\right)=0$ for each $i$, we conclude that $g=f$ a.e. $[v]$. The general case ( $f$ real or complex) follows from this. ////

Proof of Lemma 2 Let $P$ be the set of all points in $X \times Y$ at which $h(x, y) \neq 0$. Then $P \in(\mathscr{S} \times \mathscr{T})^{*}$ and $(\mu \times \lambda)(P)=0$. Hence there exists a $Q \in \mathscr{S} \times \mathscr{T}$ such that $P \subset Q$ and $(\mu \times \lambda)(Q)=0$. By Theorem 8.6,

$$
\int_{x} \lambda\left(Q_{x}\right) d \mu(x)=0
$$

Let $N$ be the set of all $x \in X$ at which $\lambda\left(Q_{x}\right)>0$. It follows from (1) that $\mu(N)=0$. For every $x \notin N, \lambda\left(Q_{x}\right)=0$. Since $P_{x} \subset Q_{x}$ and $(Y, \mathscr{T}, \lambda)$ is a complete measure space, every subset of $P_{x}$ belongs to $\mathscr{T}$ if $x \notin N$. If $y \notin P_{x}$, then $h_{x}(y)=0$. Thus we see, for every $x \notin N$, that $h_{x}$ is $\mathscr{T}$-measurable and that $h_{x}(y)=0$ a.e. $[\lambda]$.

## Convolutions

8.13 It happens occasionally that one can prove that a certain set is not empty by proving that it is actually large. The word "large" may of course refer to various properties. One of these (a rather crude one) is cardinality. An example is furnished by the familiar proof that there exist transcendental numbers: There are only countably many algebraic numbers but uncountably many real numbers, hence the set of transcendental real numbers is not empty. Applications of Baire's theorem are based on a topological notion of largeness: The dense $G_{\delta}$ 's are "large" subsets of a complete metric space. A third type of largeness is measure-theoretic: One can try to show that a certain set in a measure space is not empty by showing that it has positive measure or, better still, by showing that its complement has measure zero. Fubini's theorem often occurs in this type of argument.

For example, let $f$ and $g \in L^{1}\left(R^{1}\right)$, assume $f \geq 0$ and $g \geq 0$ for the moment, and consider the integral

$$
h(x)=\int_{-\infty}^{\infty} f(x-t) g(t) d t \quad(-\infty<x<\infty)
$$

For any fixed $x$, the integrand in (1) is a measurable function with range in $[0, \infty]$, so that $h(x)$ is certainly well defined by (1), and $0 \leq h(x) \leq \infty$.

But is there any $x$ for which $h(x)<\infty$ ? Note that the integrand in (1) is, for each fixed $x$, the product of two members of $L^{1}$, and such a product is not always in $L^{1}$. [Example: $f(x)=g(x)=1 / \sqrt{x}$ if $0<x<1,0$ otherwise.] The Fubini theorem will give an affirmative answer. In fact, it will show that $h \in L^{1}\left(R^{1}\right)$, hence that $h(x)<\infty$ a.e.

8.14 Theorem Suppose $f \in L^{1}\left(R^{1}\right), g \in L^{1}\left(R^{1}\right)$. Then

$$
\int_{-\infty}^{\infty}|f(x-y) g(y)| d y<\infty
$$

for almost all $x$. For these $x$, define

$$
h(x)=\int_{-\infty}^{\infty} f(x-y) g(y) d y
$$

Then $h \in L^{1}\left(R^{1}\right)$, and

$$
\|h\|_{1} \leq\|f\|_{1}\|g\|_{1}
$$

where

$$
\|f\|_{1}=\int_{-\infty}^{\infty}|f(x)| d x
$$

We call $h$ the convolution of $f$ and $g$, and write $h=f * g$.

Proof There exist Borel functions $f_{0}$ and $g_{0}$ such that $f_{0}=f$ a.e. and $g_{0}=g$ a.e. The integrals (1) and (2) are unchanged, for every $x$, if we replace $f$ by $f_{0}$ and $g$ by $g_{0}$. Hence we may assume, to begin with, that $f$ and $g$ are Borel functions.

To apply Fubini's theorem, we shall first prove that the function $F$ defined by

$$
F(x, y)=f(x-y) g(y)
$$

is a Borel function on $R^{2}$.

Define $\varphi: R^{2} \rightarrow R^{1}$ and $\psi: R^{2} \rightarrow R^{1}$ by

$$
\varphi(x, y)=x-y, \quad \psi(x, y)=y
$$

Then $f(x-y)=(f \circ \varphi)(x, y)$ and $g(y)=(g \circ \psi)(x, y)$. Since $\varphi$ and $\psi$ are Borel functions, Theorem 1.12(d) shows that $f \circ \varphi$ and $g \circ \psi$ are Borel functions on $R^{2}$. Hence so is their product.

Next we observe that

$$
\int_{-\infty}^{\infty} d y \int_{-\infty}^{\infty}|F(x, y)| d x=\int_{-\infty}^{\infty}|g(y)| d y \int_{-\infty}^{\infty}|f(x-y)| d x=\|f\|_{1}\|g\|_{1},
$$

since

$$
\int_{-\infty}^{\infty}|f(x-y)| d x=\|f\|_{1}
$$

for every $y \in R^{1}$, by the translation-invariance of Lebesgue measure.

Thus $F \in L^{1}\left(R^{2}\right)$, and Fubini's theorem implies that the integral (2) exists for almost all $x \in R^{1}$ and that $h \in L^{1}\left(R^{1}\right)$. Finally,

$$
\begin{aligned}
\|h\|_{1} & =\int_{-\infty}^{\infty}|h(x)| d x \leq \int_{-\infty}^{\infty} d x \int_{-\infty}^{\infty}|F(x, y)| d y \\
& =\int_{-\infty}^{\infty} d y \int_{-\infty}^{\infty}|F(x, y)| d x=\|f\|_{1}\|g\|_{1},
\end{aligned}
$$

by (7). This gives (3), and completes the proof.

Convolutions will play an important role in Chap. 9.

## Distribution Functions

8.15 Definition Let $\mu$ be a $\sigma$-finite positive measure on some $\sigma$-algebra in some set $X$. Let $f: X \rightarrow[0, \infty]$ be measurable. The function that assigns to each $t \in[0, \infty)$ the number

$$
\mu\{f>t\}=\mu(\{x \in X: f(x)>t\})
$$

is called the distribution function of $f$. It is clearly a monotonic (nonincreasing) function of $t$ and is therefore Borel measurable.

One reason for introducing distribution functions is that they make it possible to replace integrals over $X$ by integrals over $[0, \infty)$; the formula

$$
\int_{x} f d \mu=\int_{0}^{\infty} \mu\{f>t\} d t
$$

is the special case $\varphi(t)=t$ of our next theorem. This will then be used to derive an $L^{p}$-property of the maximal functions that were introduced in Chap. 7.

8.16 Theorem Suppose that $f$ and $\mu$ are as above, that $\varphi:[0, \infty] \rightarrow[0, \infty]$ is monotonic, absolutely continuous on $[0, T]$ for every $T<\infty$, and that $\varphi(0)=0$ and $\varphi(t) \rightarrow \varphi(\infty)$ as $t \rightarrow \infty$. Then

$$
\int_{X}(\varphi \circ f) d \mu=\int_{0}^{\infty} \mu\{f>t\} \varphi^{\prime}(t) d t
$$

Proof Let $E$ be the set of all $(x, t) \in X \times[0, \infty)$ where $f(x)>t$. When $f$ is simple, then $E$ is a union of finitely many measurable rectangles, and is therefore measurable. In the general case, the measurability of $E$ follows via the standard approximation of $f$ by simple functions (Theorem 1.17). As in Sec. 8.1 , put

$$
E^{t}=\{x \in X:(x, t) \in E\} \quad(0 \leq t<\infty)
$$

The distribution function of $f$ is then

$$
\mu\left(E^{t}\right)=\int_{X} \chi_{E}(x, t) d \mu(x)
$$

The right side of (1) is therefore

$$
\int_{0}^{\infty} \mu\left(E^{t}\right) \varphi^{\prime}(t) d t=\int_{X} d \mu(x) \int_{0}^{\infty} \chi_{E}(x, t) \varphi^{\prime}(t) d t
$$

by Fubini's theorem.

For each $x \in X, \chi_{E}(x, t)=1$ if $t<f(x)$ and is 0 if $t \geq f(x)$. The inner integral in (4) is therefore

$$
\int_{0}^{f(x)} \varphi^{\prime}(t) d t=\varphi(f(x))
$$

by Theorem 7.20. Now (1) follows from (4) and (5).

8.17 Recall now that the maximal function $M f$ lies in weak $L^{1}$ when $f \in L^{1}\left(R^{k}\right)$ (Theorem 7.4). We also have the trivial estimate

$$
\|M f\|_{\infty} \leq\|f\|_{\infty}
$$

valid for all $f \in L^{\infty}\left(R^{k}\right)$. A technique invented by Marcinkiewicz makes it possible to "interpolate" between these two extremes and to prove the following theorem of Hardy and Littlewood (which fails when $p=1$; see Exercise 22, Chap. 7).

8.18 Theorem If $1<p<\infty$ and $f \in L^{p}\left(R^{k}\right)$ then $M f \in L^{p}\left(R^{k}\right)$.

Proof Since $M f=M(|f|)$ we may assume, without loss of generality, that $f \geq 0$. Theorem 7.4 shows that there is a constant $A$, depending only on the dimension $k$, such that

$$
m\{M g>t\} \leq \frac{A}{t}\|g\|_{1}
$$

for every $g \in L^{1}\left(R^{k}\right)$. Here, and in the rest of this proof, $m=m_{k}$, the Lebesgue measure on $R^{k}$.

Pick a constant $c, 0<c<1$, which will be specified later so as to minimize a certain upper bound. For each $t \in(0, \infty)$, split $f$ into a sum

$$
f=g_{t}+h_{t}
$$

where

$$
g_{t}(x)= \begin{cases}f(x) & \text { if } f(x)>c t \\ 0 & \text { if } f(x) \leq c t .\end{cases}
$$

Then $0 \leq h_{t}(x) \leq c t$ for every $x \in R^{k}$. Hence $h_{t} \in L^{\infty}, M h_{t} \leq c t$, and

$$
M f \leq M g_{t}+M h_{t} \leq M g_{t}+c t
$$

If $(M f)(x)>t$ for some $x$, it follows that

$$
\left(M g_{t}\right)(x)>(1-c) t
$$

Setting $E_{t}=\{f>c t\}$, (5), (1), and (3) imply that

$$
m\{M f>t\} \leq m\left\{M g_{t}>(1-c) t\right\} \leq \frac{A}{(1-c) t}\left\|g_{t}\right\|_{1}=\frac{A}{(1-c) t} \int_{E_{t}} f d m
$$

We now use Theorem 8.16, with $X=R^{k}, \mu=m, \varphi(t)=t^{p}$, to calculate

$$
\begin{aligned}
\int_{R^{k}}(M f)^{p} d m & =p \int_{0}^{\infty} m\{M f>t\} t^{p-1} d t \leq \frac{A p}{1-c} \int_{0}^{\infty} t^{p-2} d t \int_{E_{t}} f d m \\
& =\frac{A p}{1-c} \int_{R^{k}} f d m \int_{0}^{f / c} t^{p-2} d t=\frac{A p c^{1-p}}{(1-c)(p-1)} \int_{R^{k}} f^{p} d m .
\end{aligned}
$$

This proves the theorem. However, to get a good constant, let us choose $c$ so as to minimize that last expression. This happens when $c=(p-1) / p=1 / q$, where $q$ is the exponent conjugate to $p$. For this $c$,

$$
c^{1-p}=\left(1+\frac{1}{p-1}\right)^{p-1}<e
$$

and the preceding computation yields

$$
\|M f\|_{p} \leq C_{p}\|f\|_{p}
$$

where $C_{p}=(\text { Aepq })^{1 / p}$.

Note that $C_{p} \rightarrow 1$ as $p \rightarrow \infty$, which agrees with formula 8.17(1), and that $C_{p} \rightarrow \infty$ as $p \rightarrow 1$.

## Exercises

1 Find a monotone class $\mathfrak{M}$ in $R^{1}$ which is not a $\sigma$-algebra, even though $R^{1} \in \mathfrak{M}$ and $R^{1}-A \in \mathfrak{M}$ for every $A \in \mathfrak{M}$.

2 Suppose $f$ is a Lebesgue measurable nonnegative real function on $R^{1}$ and $A(f)$ is the ordinate set of $f$. This is the set of all points $(x, y) \in R^{2}$ for which $0<y<f(x)$.

(a) Is it true that $A(f)$ is Lebesgue measurable, in the two-dimensional sense?

(b) If the answer to $(a)$ is affirmative, is the integral of $f$ over $R^{1}$ equal to the measure of $A(f)$ ?

(c) Is the graph of $f$ a measurable subset of $R^{2}$ ?

$(d)$ If the answer to $(c)$ is affirmative, is the measure of the graph equal to zero?

3 Find an example of a positive continuous function $f$ in the open unit square in $R^{2}$, whose integral (relative to Lebesgue measure) is finite but such that $\varphi(x)$ (in the notation of Theorem 8.8) is infinite for some $x \in(0,1)$.

4 Suppose $1 \leq p \leq \infty, f \in L^{1}\left(R^{1}\right)$, and $g \in L^{p}\left(R^{1}\right)$.

(a) Imitate the proof of Theorem 8.14 to show that the integral defining $(f * g)(x)$ exists for almost all $x$, that $f * g \in L^{p}\left(R^{1}\right)$, and that

$$
\|f * g\|_{p} \leq\|f\|_{1}\|g\|_{p} .
$$

(b) Show that equality can hold in (a) if $p=1$ and if $p=\infty$, and find the conditions under which this happens.

(c) Assume $1<p<\infty$, and equality holds in (a). Show that then either $f=0$ a.e. or $g=0$ a.e.

(d) Assume $1 \leq p \leq \infty, \epsilon>0$, and show that there exist $f \in L^{1}\left(R^{1}\right)$ and $g \in L^{p}\left(R^{1}\right)$ such that

$$
\|f * g\|_{p}>(1-\epsilon)\|f\|_{1}\|g\|_{p}
$$

5 Let $M$ be the Banach space of all complex Borel measures on $R^{1}$. The norm in $M$ is $\|\mu\|=|\mu|\left(R^{1}\right)$. Associate to each Borel set $E \subset R^{1}$ the set

$$
E_{2}=\{(x, y): x+y \in E\} \subset R^{2} .
$$

If $\mu$ and $\lambda \in M$, define their convolution $\mu * \lambda$ to be the set function given by

$$
(\mu * \lambda)(E)=(\mu \times \lambda)\left(E_{2}\right)
$$

for every Borel set $E \subset R^{1} ; \mu \times \lambda$ is as in Definition 8.7.

(a) Prove that $\mu * \lambda \in M$ and that $\|\mu * \lambda\| \leq\|\mu\|\|\lambda\|$.

(b) Prove that $\mu * \lambda$ is the unique $v \in M$ such that

$$
\int f d v=\iint f(x+y) d \mu(x) d \lambda(y)
$$

for every $f \in C_{0}\left(R^{1}\right)$. (All integrals extend over $R^{1}$.)

(c) Prove that convolution in $M$ is commutative, associative, and distributive with respect to addition.

(d) Prove the formula

$$
(\mu * \lambda)(E)=\int \mu(E-t) d \lambda(t)
$$

for every $\mu$ and $\lambda \in M$ and every Borel set $E$. Here

$$
E-t=\{x-t: x \in E\}
$$

(e) Define $\mu$ to be discrete if $\mu$ is concentrated on a countable set; define $\mu$ to be continuous if $\mu(\{x\})=0$ for every point $x \in R^{1}$; let $m$ be Lebesgue measure on $R^{1}$ (note that $m \notin M$ ). Prove that $\mu * \lambda$ is discrete if both $\mu$ and $\lambda$ are discrete, that $\mu * \lambda$ is continuous if $\mu$ is continuous and $\lambda \in M$, and that $\mu * \lambda \ll m$ if $\mu \ll m$.

(f) Assume $d \mu=f d m, \quad d \lambda=g d m, \quad f \in L^{1}\left(R^{1}\right), \quad$ and $\quad g \in L^{1}\left(R^{1}\right), \quad$ and prove that $d(\mu * \lambda)=(f * g) d m$.

(g) Properties (a) and (c) show that the Banach space $M$ is what one calls a commutative Banach algebra. Show that $(e)$ and $(f)$ imply that the set of all discrete measures in $M$ is a subalgebra of $M$, that the continuous measures form an ideal in $M$, and that the absolutely continuous measures (relative to $m$ ) form an ideal in $M$ which is isomorphic (as an algebra) to $L^{1}\left(R^{1}\right)$.

(h) Show that $M$ has a unit, i.e., show that there exists a $\delta \in M$ such that $\delta * \mu=\mu$ for all $\mu \in M$.

(i) Only two properties of $R^{1}$ have been used in this discussion: $R^{1}$ is a commutative group (under addition), and there exists a translation invariant Borel measure $m$ on $R^{1}$ which is not identically 0 and which is finite on all compact subsets of $R^{1}$. Show that the same results hold if $R^{1}$ is replaced by $R^{k}$ or by $T$ (the unit circle) or by $T^{k}$ (the $k$-dimensional torus, the cartesian product of $k$ copies of $T$ ), as soon as the definitions are properly formulated.

6 (Polar coordinates in $R^{k}$.) Let $S_{k-1}$ be the unit sphere in $R^{k}$, i.e., the set of all $u \in R^{k}$ whose distance from the origin 0 is 1 . Show that every $x \in R^{k}$, except for $x=0$, has a unique representation of the form $x=r u$, where $r$ is a positive real number and $u \in S_{k-1}$. Thus $R^{k}-\{0\}$ may be regarded as the cartesian product $(0, \infty) \times S_{k-1}$.

Let $m_{k}$ be Lebesgue measure on $R^{k}$, and define a measure $\sigma_{k-1}$ on $S_{k-1}$ as follows: If $A \subset S_{k-1}$ and $A$ is a Borel set, let $\tilde{A}$ be the set of all points $r u$, where $0<r<1$ and $u \in A$, and define

$$
\sigma_{k-1}(A)=k \cdot m_{k}(\tilde{A})
$$

Prove that the formula

$$
\int_{R^{k}} f d m_{k}=\int_{0}^{\infty} r^{k-1} d r \int_{S_{k-1}} f(r u) d \sigma_{k-1}(u)
$$

is valid for every nonnegative Borel function $f$ on $R^{k}$. Check that this coincides with familiar results when $k=2$ and when $k=3$.

Suggestion: If $0<r_{1}<r_{2}$ and if $A$ is an open subset of $S_{k-1}$, let $E$ be the set of all $r u$ with $r_{1}<r<r_{2}, u \in A$, and verify that the formula holds for the characteristic function of $E$. Pass from these to characteristic functions of Borel sets in $R^{k}$.

7 Suppose $(X, \mathscr{S}, \mu)$ and $(Y, \mathscr{T}, \lambda)$ are $\sigma$-finite measure spaces, and suppose $\psi$ is a measure on $\mathscr{S} \times \mathscr{T}$ such that

$$
\psi(A \times B)=\mu(A) \lambda(B)
$$

whenever $A \in \mathscr{S}$ and $B \in \mathscr{T}$. Prove that then $\psi(E)=(\mu \times \lambda)(E)$ for every $E \in \mathscr{S} \times \mathscr{T}$.

8 (a) Suppose $f$ is a real function on $R^{2}$ such that each section $f_{x}$ is Borel measurable and each section $f^{y}$ is continuous. Prove that $f$ is Borel measurable on $R^{2}$. Note the contrast between this and Example $8.9(c)$.

(b) Suppose $g$ is a real function on $R^{k}$ which is continuous in each of the $k$ variables separately. More explicitly, for every choice of $x_{2}, \ldots, x_{k}$, the mapping $x_{1} \rightarrow g\left(x_{1}, x_{2}, \ldots, x_{k}\right)$ is continuous, etc. Prove that $g$ is a Borel function.

Hint: If $(i-1) / n=a_{i-1} \leq x \leq a_{i}=i / n$, put

$$
f_{n}(x, y)=\frac{a_{i}-x}{a_{i}-a_{i-1}} f\left(a_{i-1}, y\right)+\frac{x-a_{i-1}}{a_{i}-a_{i-1}} f\left(a_{i}, y\right)
$$

9 Suppose $E$ is a dense set in $R^{1}$ and $f$ is a real function on $R^{2}$ such that $(a) f_{x}$ is Lebesgue measurable for each $x \in E$ and $(b) f^{y}$ is continuous for almost all $y \in R^{1}$. Prove that $f$ is Lebesgue measurable on $R^{2}$.

10 Suppose $f$ is a real function on $R^{2}, f_{x}$ is Lebesgue measurable for each $x$, and $f^{y}$ is continuous for each $y$. Suppose $g: R^{1} \rightarrow R^{1}$ is Lebesgue measurable, and put $h(y)=f(g(y), y)$. Prove that $h$ is Lebesgue measurable on $R^{1}$.

Hint : Define $f_{n}$ as in Exercise 8, put $h_{n}(y)=f_{n}(g(y), y)$, show that each $h_{n}$ is measurable, and that $h_{n}(y) \rightarrow h(y)$.

11 Let $\mathscr{B}_{k}$ be the $\sigma$-algebra of all Borel sets in $R^{k}$. Prove that $\mathscr{B}_{m+n}=\mathscr{B}_{m} \times \mathscr{B}_{n}$. This is relevant in Theorem 8.14.

12 Use Fubini's theorem and the relation

$$
\frac{1}{x}=\int_{0}^{\infty} e^{-x t} d t \quad(x>0)
$$

to prove that

$$
\lim _{A \rightarrow \infty} \int_{0}^{A} \frac{\sin x}{x} d x=\frac{\pi}{2}
$$

13. If $\mu$ is a complex measure on a $\sigma$-algebra $\mathfrak{M}$, show that every set $E \in \mathfrak{M}$ has a subset $A$ for which

$$
|\mu(A)| \geq \frac{1}{\pi}|\mu|(E)
$$

Suggestion: There is a measurable real function $\theta$ so that $d \mu=e^{i \theta} d|\mu|$. Let $A_{\alpha}$ be the subset of $E$ where $\cos (\theta-\alpha)>0$, show that

$$
\operatorname{Re}\left[e^{-i \alpha} \mu\left(A_{\alpha}\right)\right]=\int_{E} \cos ^{+}(\theta-\alpha) d|\mu|
$$

and integrate with respect to $\alpha$ (as in Lemma 6.3).

Show, by an example, that $1 / \pi$ is the best constant in this inequality.

14 Complete the following proof of Hardy's inequality (Chap. 3, Exercise 14): Suppose $f \geq 0$ on $(0, \infty), f \in L^{p}, 1<p<\infty$, and

$$
F(x)=\frac{1}{x} \int_{0}^{x} f(t) d t
$$

Write $x F(x)=\int_{0}^{x} f(t) t^{\alpha} t^{-\alpha} d t$, where $0<\alpha<1 / q$, use Hölder's inequality to get an upper bound for $F(x)^{p}$, and integrate to obtain

$$
\int_{0}^{\infty} F^{p}(x) d x \leq(1-\alpha q)^{1-p}(\alpha p)^{-1} \int_{0}^{\infty} f^{p}(t) d t
$$

Show that the best choice of $\alpha$ yields

$$
\int_{0}^{\infty} F^{p}(x) d x \leq\left(\frac{p}{p-1}\right)^{p} \int_{0}^{\infty} f^{p}(t) d t
$$

15 Put $\varphi(t)=1-\cos t$ if $0 \leq t \leq 2 \pi, \varphi(t)=0$ for all other real $t$. For $-\infty<x<\infty$, define

$$
f(x)=1, \quad g(x)=\varphi^{\prime}(x), \quad h(x)=\int_{-\infty}^{x} \varphi(t) d t
$$

Verify the following statements about convolutions of these functions:

(i) $(f * g)(x)=0$ for all $x$.

(ii) $(g * h)(x)=(\varphi * \varphi)(x)>0$ on $(0,4 \pi)$.

(iii) Therefore $(f * g) * h=0$, whereas $f *(g * h)$ is a positive constant.

But convolution is supposedly associative, by Fubini's theorem (Exercise $5(c)$ ). What went wrong?

16 Prove the following analogue of Minkowski's inequality, for $f \geq 0$ :

$$
\left\{\int\left[\int f(x, y) d \lambda(y)\right]^{p} d \mu(x)\right\}^{1 / p} \leq \int\left[\int f^{p}(x, y) d \mu(x)\right]^{1 / p} d \lambda(y)
$$

Supply the required hypotheses. (Many further developments of this theme may be found in [9].)

## FOURIER TRANSFORMS

## Formal Properties

9.1 Definitions In this chapter we shall depart from the previous notation and use the letter $m$ not for Lebesgue measure on $R^{1}$ but for Lebesgue measure divided by $\sqrt{2 \pi}$. This convention simplifies the appearance of results such as the inversion theorem and the Plancherel theorem. Accordingly, we shall use the notation

$$
\int_{-\infty}^{\infty} f(x) d m(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} f(x) d x
$$

where $d x$ refers to ordinary Lebesgue measure, and we define

$$
\begin{aligned}
& \|f\|_{p}=\left\{\int_{-\infty}^{\infty}|f(x)|^{p} d m(x)\right\}^{1 / p} \quad(1 \leq p<\infty), \\
& (f * g)(x)=\int_{-\infty}^{\infty} f(x-y) g(y) d m(y) \quad\left(x \in R^{1}\right),
\end{aligned}
$$

and

$$
\hat{f}(t)=\int_{-\infty}^{\infty} f(x) e^{-i x t} d m(x) \quad\left(t \in R^{1}\right)
$$

Throughout this chapter, we shall write $L^{p}$ in place of $L^{p}\left(R^{1}\right)$, and $C_{0}$ will denote the space of all continuous functions on $R^{1}$ which vanish at infinity.

If $f \in L^{1}$, the integral (4) is well defined for every real $t$. The function $\hat{f}$ is called the Fourier transform of $f$. Note that the term "Fourier transform" is also applied to the mapping which takes $f$ to $\hat{f}$.

The formal properties which are listed in Theorem 9.2 depend intimately on the translation-invariance of $m$ and on the fact that for each real $\alpha$ the mapping $x \rightarrow e^{i \alpha x}$ is a character of the additive group $R^{1}$. By definition, a function $\varphi$ is a character of $R^{1}$ if $|\varphi(t)|=1$ and if

$$
\varphi(s+t)=\varphi(s) \varphi(t)
$$

for all real $s$ and $t$. In other words, $\varphi$ is to be a homomorphism of the additive group $R^{1}$ into the multiplicative group of the complex numbers of absolute value 1. We shall see later (in the proof of Theorem 9.23) that every continuous character of $R^{1}$ is given by an exponential.

9.2 Theorem Suppose $f \in L^{1}$, and $\alpha$ and $\lambda$ are real numbers.

(a) If $g(x)=f(x) e^{i \alpha x}$, then $\hat{g}(t)=\hat{f}(t-\alpha)$.

(b) If $g(x)=f(x-\alpha)$, then $\hat{g}(t)=\hat{f}(t) e^{-i \alpha t}$.

(c) If $g \in L^{1}$ and $h=f * g$, then $\hat{h}(t)=\hat{f}(t) \hat{g}(t)$.

Thus the Fourier transform converts multiplication by a character into translation, and vice versa, and it converts convolutions to pointwise products.

(d) If $g(x)=\overline{f(-x)}$, then $\hat{g}(t)=\overline{\hat{f}(t)}$.

(e) If $g(x)=f(x / \lambda)$ and $\lambda>0$, then $\hat{g}(t)=\lambda \hat{f}(\lambda t)$.

(f) If $g(x)=-i x f(x)$ and $g \in L^{1}$, then $\hat{f}$ is differentiable and $\hat{f}^{\prime}(t)=\hat{g}(t)$.

Proof $(a),(b),(d)$, and $(e)$ are proved by direct substitution into formula 9.1(4). The proof of $(c)$ is an application of Fubini's theorem (see Theorem 8.14 for the required measurability proof):

$$
\begin{aligned}
\hat{h}(t) & =\int_{-\infty}^{\infty} e^{-i t x} d m(x) \int_{-\infty}^{\infty} f(x-y) g(y) d m(y) \\
& =\int_{-\infty}^{\infty} g(y) e^{-i t y} d m(y) \int_{-\infty}^{\infty} f(x-y) e^{-i t(x-y)} d m(x) \\
& =\int_{-\infty}^{\infty} g(y) e^{-i t y} d m(y) \int_{-\infty}^{\infty} f(x) e^{-i t x} d m(x) \\
& =\hat{g}(t) \hat{f}(t) .
\end{aligned}
$$

Note how the translation-invariance of $m$ was used.

To prove $(f)$, note that

$$
\frac{\hat{f}(s)-\hat{f}(t)}{s-t}=\int_{-\infty}^{\infty} f(x) e^{-i x t} \varphi(x, s-t) d m(x) \quad(s \neq t)
$$

where $\varphi(x, u)=\left(e^{-i x u}-1\right) / u$. Since $|\varphi(x, u)| \leq|x|$ for all real $u \neq 0$ and since $\varphi(x, u) \rightarrow-i x$ as $u \rightarrow 0$, the dominated convergence theorem applies to (1), if $s$ tends to $t$, and we conclude that

$$
\hat{f}^{\prime}(t)=-i \int_{-\infty}^{\infty} x f(x) e^{-i x t} d m(x)
$$

### 9.3 Remarks

(a) In the preceding proof, the appeal to the dominated convergence theorem may seem to be illegitimate since the dominated convergence theorem deals only with countable sequences of functions. However, it does enable us to conclude that

$$
\lim _{n \rightarrow \infty} \frac{\hat{f}\left(s_{n}\right)-\hat{f}(t)}{s_{n}-t}=-i \int_{-\infty}^{\infty} x f(x) e^{-i x t} d m(t)
$$

for every sequence $\left\{s_{n}\right\}$ which converges to $t$, and this says exactly that

$$
\lim _{s \rightarrow t} \frac{\hat{f}(s)-\hat{f}(t)}{s-t}=-i \int_{-\infty}^{\infty} x f(x) e^{-i x t} d m(t)
$$

We shall encounter similar situations again, and shall apply convergence theorems to them without further comment.

(b) Theorem 9.2(b) shows that the Fourier transform of.

$$
[f(x+\alpha)-f(x)] / \alpha
$$

is

$$
\hat{f}(t) \frac{e^{i \alpha t}-1}{\alpha}
$$

This suggests that an analogue of Theorem $9.2(f)$ should be true under certain conditions, namely, that the Fourier transform of $f^{\prime}$ is $i t \hat{f}(t)$. If $f \in L^{1}, f^{\prime} \in L^{1}$, and if $f$ is the indefinite integral of $f^{\prime}$, the result is easily established by an integration by parts. We leave this, and some related results, as exercises. The fact that the Fourier transform converts differentiation to multiplication by $t i$ makes the Fourier transform a useful tool in the study of differential equations.

## The Inversion Theorem

9.4 We have just seen that certain operations on functions correspond nicely to operations on their Fourier transforms. The usefulness and interest of this correspondence will of course be enhanced if there is a way of returning from the transforms to the functions, that is to say, if there is an inversion formula.

Let us see what such a formula might look like, by analogy with Fourier series. If

$$
c_{n}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(x) e^{-i n x} d x \quad(n \in Z)
$$

then the inversion formula is

$$
f(x)=\sum_{-\infty}^{\infty} c_{n} e^{i n x}
$$

We know that (2) holds, in the sense of $L^{2}$-convergence, if $f \in L^{2}(T)$. We also know that (2) does not necessarily hold in the sense of pointwise convergence, even if $f$ is continuous. Suppose now that $f \in L^{1}(T)$, that $\left\{c_{n}\right\}$ is given by (1), and that

$$
\sum_{-\infty}^{\infty}\left|c_{n}\right|<\infty
$$

Put

$$
g(x)=\sum_{-\infty}^{\infty} c_{n} e^{i n x}
$$

By (3), the series in (4) converges uniformly (hence $g$ is continuous), and the Fourier coefficients of $g$ are easily computed:

$$
\begin{aligned}
\frac{1}{2 \pi} \int_{-\pi}^{\pi} g(x) e^{-i k x} d x & =\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left\{\sum_{n=-\infty}^{\infty} c_{n} e^{i n x}\right\} e^{-i k x} d x \\
& =\sum_{n=-\infty}^{\infty} c_{n} \frac{1}{2 \pi} \int_{-\pi}^{\pi} e^{i(n-k) x} d x \\
& =c_{k} .
\end{aligned}
$$

Thus $f$ and $g$ have the same Fourier coefficients. This implies $f=g$ a.e., so the Fourier series of $f$ converges to $f(x)$ a.e.

The analogous assumptions in the context of Fourier transforms are that $f \in L^{1}$ and $\hat{f} \in L^{1}$, and we might then expect that a formula like

$$
f(x)=\int_{-\infty}^{\infty} \hat{f}(t) e^{i t x} d m(t)
$$

is valid. Certainly, if $\hat{f} \in L^{1}$, the right side of (6) is well defined; call it $g(x)$; but if we want to argue as in (5), we run into the integral

$$
\int_{-\infty}^{\infty} e^{i(t-s) x} d x
$$

which is meaningless as it stands. Thus even under the strong assumption that $\hat{f} \in L^{1}$, a proof of (6) (which is true) has to proceed over a more devious route.

[It should be mentioned that (6) may hold even if $\hat{f} \notin L^{1}$, if the integral over $(-\infty, \infty)$ is interpreted as the limit, as $A \rightarrow \infty$, of integrals over $(-A, A)$. (Analogue: a series may converge without converging absolutely.) We shall not go into this.]

9.5 Theorem For any function $f$ on $R^{1}$ and every $y \in R^{1}$, let $f_{y}$ be the translate of $f$ defined by

$$
f_{y}(x)=f(x-y) \quad\left(x \in R^{1}\right)
$$

If $1 \leq p<\infty$ and if $f \in L^{p}$, the mapping

$$
y \rightarrow f_{y}
$$

is a uniformly continuous mapping of $R^{1}$ into $L^{p}\left(R^{1}\right)$.

Proof Fix $\epsilon>0$. Since $f \in L^{p}$, there exists a continuous function $g$ whose support lies in a bounded interval $[-A, A]$, such that

$$
\|f-g\|_{p}<\epsilon
$$

(Theorem 3.14). The uniform continuity of $g$ shows that there exists a $\delta \in(0, A)$ such that $|s-t|<\delta$ implies

$$
|g(s)-g(t)|<(3 A)^{-1 / p} \epsilon .
$$

If $|s-t|<\delta$, it follows that

$$
\int_{-\infty}^{\infty}|g(x-s)-g(x-t)|^{p} d x<(3 A)^{-1} \epsilon^{p}(2 A+\delta)<\epsilon^{p}
$$

so that $\left\|g_{s}-g_{t}\right\|_{p}<\epsilon$.

Note that $L^{p}$-norms (relative to Lebesgue measure) are translationinvariant: $\|f\|_{p}=\left\|f_{s}\right\|_{p}$. Thus

$$
\begin{aligned}
\left\|f_{s}-f_{t}\right\|_{p} & \leq\left\|f_{s}-g_{s}\right\|_{p}+\left\|g_{s}-g_{t}\right\|_{p}+\left\|g_{t}-f_{t}\right\|_{p} \\
& =\left\|(f-g)_{s}\right\|_{p}+\left\|g_{s}-g_{t}\right\|_{p}+\left\|(g-f)_{t}\right\|_{p}<3 \epsilon
\end{aligned}
$$

whenever $|s-t|<\delta$. This completes the proof.

9.6 Theorem If $f \in L^{1}$, then $\hat{f} \in C_{0}$ and

$$
\|\hat{f}\|_{\infty} \leq\|f\|_{1} \text {. }
$$

Proof The inequality (1) is obvious from 9.1(4). If $t_{n} \rightarrow t$, then

$$
\left|\hat{f}\left(t_{n}\right)-\hat{f}(t)\right| \leq \int_{-\infty}^{\infty}|f(x)|\left|e^{-i t_{n} x}-e^{-i t x}\right| d m(x)
$$

The integrand is bounded by $2|f(x)|$ and tends to 0 for every $x$, as $n \rightarrow \infty$. Hence $\hat{f}\left(t_{n}\right) \rightarrow \hat{f}(t)$, by the dominated convergence theorem. Thus $\hat{f}$ is continuous.

Since $e^{\pi i}=-1,9.1(4)$ gives

$$
\hat{f}(t)=-\int_{-\infty}^{\infty} f(x) e^{-i t(x+\pi / t)} d m(x)=-\int_{-\infty}^{\infty} f(x-\pi / t) e^{-i t x} d m(x)
$$

Hence

$$
2 \hat{f}(t)=\int_{-\infty}^{\infty}\left\{f(x)-f\left(x-\frac{\pi}{t}\right)\right\} e^{-i t x} d m(x)
$$

so that

$$
2|\hat{f}(t)| \leq\left\|f-f_{\pi / t}\right\|_{1},
$$

which tends to 0 as $t \rightarrow \pm \infty$, by Theorem 9.5 .

9.7 A Pair of Auxiliary Functions In the proof of the inversion theorem it will be convenient to know a positive function $H$ which has a positive Fourier transform whose integral is easily calculated. Among the many possibilities we choose one which is of interest in connection with harmonic functions in a half plane. (See Exercise 25, Chap. 11.)

Put

$$
H(t)=e^{-|t|}
$$

and define

$$
h_{\lambda}(x)=\int_{-\infty}^{\infty} H(\lambda t) e^{i t x} d m(t) \quad(\lambda>0)
$$

A simple computation gives

$$
h_{\lambda}(x)=\sqrt{\frac{2}{\pi}} \frac{\lambda}{\lambda^{2}+x^{2}}
$$

and hence

$$
\int_{-\infty}^{\infty} h_{\lambda}(x) d m(x)=1
$$

Note also that $0<H(t) \leq 1$ and that $H(\lambda t) \rightarrow 1$ as $\lambda \rightarrow 0$.

9.8 Proposition If $f \in L^{1}$, then

$$
\left(f * h_{\lambda}\right)(x)=\int_{-\infty}^{\infty} H(\lambda t) \hat{f}(t) e^{i x t} d m(t)
$$

Proof This is a simple application of Fubini's theorem.

$$
\begin{aligned}
\left(f * h_{\lambda}\right)(x) & =\int_{-\infty}^{\infty} f(x-y) d m(y) \int_{-\infty}^{\infty} H(\lambda t) e^{i t y} d m(t) \\
& =\int_{-\infty}^{\infty} H(\lambda t) d m(t) \int_{-\infty}^{\infty} f(x-y) e^{i t y} d m(y) \\
& =\int_{-\infty}^{\infty} H(\lambda t) d m(t) \int_{-\infty}^{\infty} f(y) e^{i t(x-y)} d m(y) \\
& =\int_{-\infty}^{\infty} H(\lambda t) \hat{f}(t) e^{i t x} d m(t) .
\end{aligned}
$$

9.9 Theorem If $g \in L^{\infty}$ and $g$ is continuous at a point $x$, then

$$
\lim _{\lambda \rightarrow 0}\left(g * h_{\lambda}\right)(x)=g(x)
$$

Proof On account of 9.7(4), we have

$$
\begin{aligned}
\left(g * h_{\lambda}\right)(x)-g(x) & =\int_{-\infty}^{\infty}[g(x-y)-g(x)] h_{\lambda}(y) d m(y) \\
& =\int_{-\infty}^{\infty}[g(x-y)-g(x)] \lambda^{-1} h_{1}\left(\frac{y}{\lambda}\right) d m(y) \\
& =\int_{-\infty}^{\infty}[g(x-\lambda s)-g(x)] h_{1}(s) d m(s)
\end{aligned}
$$

The last integrand is dominated by $2\|g\|_{\infty} h_{1}(s)$ and converges to 0 pointwise for every $s$, as $\lambda \rightarrow 0$. Hence (1) follows from the dominated convergence theorem.

9.10 Theorem If $1 \leq p<\infty$ and $f \in L^{p}$, then

$$
\lim _{\lambda \rightarrow 0}\left\|f * h_{\lambda}-f\right\|_{p}=0
$$

The cases $p=1$ and $p=2$ will be the ones of interest to us, but the general case is no harder to prove.

Proof Since $h_{\lambda} \in L^{q}$, where $q$ is the exponent conjugate to $p,\left(f * h_{\lambda}\right)(x)$ is defined for every $x$. (In fact, $f * h_{\lambda}$ is continuous; see Exercise 8.) Because of 9.7(4) we have

$$
\left(f * h_{\lambda}\right)(x)-f(x)=\int_{-\infty}^{\infty}[f(x-y)-f(x)] h_{\lambda}(y) d m(y)
$$

and Theorem 3.3 gives

$$
\left|\left(f * h_{\lambda}\right)(x)-f(x)\right|^{p} \leq \int_{-\infty}^{\infty}|f(x-y)-f(x)|^{p} h_{\lambda}(y) d m(y)
$$

Integrate (3) with respect to $x$ and apply Fubini's theorem:

$$
\left\|f * h_{\lambda}-f\right\|_{p}^{p} \leq \int_{-\infty}^{\infty}\left\|f_{y}-f\right\|_{p}^{p} h_{\lambda}(y) d m(y)
$$

If $g(y)=\left\|f_{y}-f\right\|_{p}^{p}$, then $g$ is bounded and continuous, by Theorem 9.5 , and $g(0)=0$. Hence the right side of (4) tends to 0 as $\lambda \rightarrow 0$, by Theorem 9.9.

9.11 The Inversion Theorem If $f \in L^{1}$ and $\hat{f} \in L^{1}$, and if

$$
g(x)=\int_{-\infty}^{\infty} \hat{f}(t) e^{i x t} d m(t) \quad\left(x \in R^{1}\right)
$$

then $g \in C_{0}$ and $f(x)=g(x)$ a.e.

Proof By Proposition 9.8,

$$
\left(f * h_{\lambda}\right)(x)=\int_{-\infty}^{\infty} H(\lambda t) \hat{f}(t) e^{i x t} d m(t)
$$

The integrands on the right side of (2) are bounded by $|\hat{f}(t)|$, and since $H(\lambda t) \rightarrow 1$ as $\lambda \rightarrow 0$, the right side of (2) converges to $g(x)$, for every $x \in R^{1}$, by the dominated convergence theorem.

If we combine Theorems 9.10 and 3.12, we see that there is a sequence $\left\{\lambda_{n}\right\}$ such that $\lambda_{n} \rightarrow 0$ and

$$
\lim _{n \rightarrow \infty}\left(f * h_{\lambda_{n}}\right)(x)=f(x) \text { a.e. }
$$

Hence $f(x)=g(x)$ a.e. That $g \in C_{0}$ follows from Theorem 9.6.

9.12 The Uniqueness Theorem If $f \in L^{1}$ and $\hat{f}(t)=0$ for all $t \in R^{1}$, then $f(x)=0$ a.e.

Proof Since $\hat{f}=0$ we have $\hat{f} \in L^{1}$, and the result follows from the inversion theorem.

## The Plancherel Theorem

Since the Lebesgue measure of $R^{1}$ is infinite, $L^{2}$ is not a subset of $L^{1}$, and the definition of the Fourier transform by formula 9.1(4) is therefore not directly applicable to every $f \in L^{2}$. The definition does apply, however, if $f \in L^{1} \cap L^{2}$, and it turns out that then $\hat{f} \in L^{2}$. In fact, $\|\hat{f}\|_{2}=\|f\|_{2}$ ! This isometry of $L^{1} \cap L^{2}$ into $L^{2}$ extends to an isometry of $L^{2}$ onto $L^{2}$, and this extension defines the Fourier
transform (sometimes called the Plancherel transform) of every $f \in L^{2}$. The resulting $L^{2}$-theory has in fact a great deal more symmetry than is the case in $L^{1}$. In $L^{2}, f$ and $\hat{f}$ play exactly the same role.

9.13 Theorem One can associate to each $f \in L^{2}$ a function $\hat{f} \in L^{2}$ so that the following properties hold:

(a) If $f \in L^{1} \cap L^{2}$, then $\hat{f}$ is the previously defined Fourier transform of $f$.

(b) For every $f \in L^{2},\|\hat{f}\|_{2}=\|f\|_{2}$.

(c) The mapping $f \rightarrow \hat{f}$ is a Hilbert space isomorphism of $L^{2}$ onto $L^{2}$.

(d) The following symmetric relation exists between $f$ and $\hat{f}:$ If

$$
\varphi_{A}(t)=\int_{-A}^{A} f(x) e^{-i x t} d m(x) \quad \text { and } \quad \psi_{A}(x)=\int_{-A}^{A} \hat{f}(t) e^{i x t} d m(t)
$$

then $\left\|\varphi_{A}-\hat{f}\right\|_{2} \rightarrow 0$ and $\left\|\psi_{A}-f\right\|_{2} \rightarrow 0$ as $A \rightarrow \infty$.

Note: Since $L^{1} \cap L^{2}$ is dense in $L^{2}$, properties $(a)$ and $(b)$ determine the mapping $f \rightarrow \hat{f}$ uniquely. Property $(d)$ may be called the $L^{2}$ inversion theorem.

Proof Our first objective is the relation

$$
\|\hat{f}\|_{2}=\|f\|_{2} \quad\left(f \in L^{1} \cap L^{2}\right)
$$

We fix $f \in L^{1} \cap L^{2}$, put $\tilde{f}(x)=\overline{f(-x)}$, and define $g=f * \tilde{f}$. Then

$$
g(x)=\int_{-\infty}^{\infty} f(x-y) \overline{f(-y)} d m(y)=\int_{-\infty}^{\infty} f(x+y) \overline{f(y)} d m(y)
$$

or

$$
g(x)=\left(f_{-x}, f\right)
$$

where the inner product is taken in the Hilbert space $L^{2}$ and $f_{-x}$ denotes a translate of $f$, as in Theorem 9.5. By that theorem, $x \rightarrow f_{-x}$ is a continuous mapping of $R^{1}$ into $L^{2}$, and the continuity of the inner product (Theorem 4.6) therefore implies that $g$ is a continuous function. The Schwarz inequality shows that

$$
|g(x)| \leq\left\|f_{-x}\right\|_{2}\|f\|_{2}=\|f\|_{2}^{2}
$$

so that $g$ is bounded. Also, $g \in L^{1}$ since $f \in L^{1}$ and $\tilde{f} \in L^{1}$.

Since $g \in L^{1}$, we may apply Proposition 9.8 :

$$
\left(g * h_{\lambda}\right)(0)=\int_{-\infty}^{\infty} H(\lambda t) \hat{g}(t) d m(t)
$$

Since $g$ is continuous and bounded, Theorem 9.9 shows that

$$
\lim _{\lambda \rightarrow 0}\left(g * h_{\lambda}\right)(0)=g(0)=\|f\|_{2}^{2}
$$

Theorem 9.2(d) shows that $\hat{g}=|\hat{f}|^{2} \geq 0$, and since $H(\lambda t)$ increases to 1 as $\lambda \rightarrow 0$, the monotone convergence theorem gives

$$
\lim _{\lambda \rightarrow 0} \int_{-\infty}^{\infty} H(\lambda t) \hat{g}(t) d m(t)=\int_{-\infty}^{\infty}|\hat{f}(t)|^{2} d m(t)
$$

Now (5), (6), and (7) shows that $\hat{f} \in L^{2}$ and that (1) holds.

This was the crux of the proof.

Let $Y$ be the space of all Fourier transforms $\hat{f}$ of functions $f \in L^{1} \cap L^{2}$. By (1), $Y \subset L^{2}$. We claim that $Y$ is dense in $L^{2}$, i.e., that $Y^{\perp}=\{0\}$.

The functions $x \rightarrow e^{i \alpha x} H(\lambda x)$ are in $L^{1} \cap L^{2}$, for all real $\alpha$ and all $\lambda>0$. Their Fourier transforms

$$
h_{\lambda}(\alpha-t)=\int_{-\infty}^{\infty} e^{i \alpha x} H(\lambda x) e^{-i x t} d m(x)
$$

are therefore in $Y$. If $w \in L^{2}, w \in Y^{\perp}$, it follows that

$$
\left(h_{\lambda} * \bar{w}\right)(\alpha)=\int_{-\infty}^{\infty} h_{\lambda}(\alpha-t) \bar{w}(t) d m(t)=0
$$

for all $\alpha$. Hence $w=0$, by Theorem 9.10, and therefore $Y$ is dense in $L^{2}$.

Let us introduce the temporary notation $\Phi f$ for $\hat{f}$. From what has been proved so far, we see that $\Phi$ is an $L^{2}$-isometry from one dense subspace of $L^{2}$, namely $L^{1} \cap L^{2}$, onto another, namely $Y$. Elementary Cauchy sequence arguments (compare with Lemma 4.16) imply therefore that $\Phi$ extends to an isometry $\tilde{\Phi}$ of $L^{2}$ onto $L^{2}$. If we write $\hat{f}$ for $\tilde{\Phi} f$, we obtain properties $(a)$ and $(b)$.

Property $(c)$ follows from $(b)$, as in the proof of Theorem 4.18. The Parseval formula

$$
\int_{-\infty}^{\infty} f(x) \overline{g(x)} d m(x)=\int_{-\infty}^{\infty} \hat{f}(t) \overline{\hat{g}(t)} d m(t)
$$

holds therefore for all $f \in L^{2}$ and $g \in L^{2}$.

To prove $(d)$, let $k_{A}$ be the characteristic function of $[-A, A]$. Then $k_{A} f \in L^{1} \cap L^{2}$ if $f \in L^{2}$, and

$$
\varphi_{A}=\left(k_{A} f\right) \hat{.}
$$

Since $\left\|f-k_{A} f\right\|_{2} \rightarrow 0$ as $A \rightarrow \infty$, it follows from (b) that

$$
\left\|\hat{f}-\varphi_{A}\right\|_{2}=\left\|\left(f-k_{A} f\right)^{\hat{\|}}\right\|_{2} \rightarrow 0
$$

as $A \rightarrow \infty$.

The other half of $(d)$ is proved the same way.

9.14 Theorem If $f \in L^{2}$ and $\hat{f} \in L^{1}$, then

$$
f(x)=\int_{-\infty}^{\infty} \hat{f}(t) e^{i x t} d m(t) \quad \text { a.e. }
$$

Proof This is corollary of Theorem $9.13(d)$.

9.15 Remark If $f \in L^{1}$, formula 9.1(4) defines $\hat{f}(t)$ unambiguously for every $t$. If $f \in L^{2}$, the Plancherel theorem defines $\hat{f}$ uniquely as an element of the Hilbert space $L^{2}$, but as a point function $\hat{f}(t)$ is only determined almost everywhere. This is an important difference between the theory of Fourier transforms in $L^{1}$ and in $L^{2}$. The indeterminacy of $\hat{f}(t)$ as a point function will cause some difficulties in the problem to which we now turn.

9.16 Translation-Invariant Subspaces of $L^{2}$ A subspace $M$ of $L^{2}$ is said to be translation-invariant if $f \in M$ implies that $f_{\alpha} \in M$ for every real $\alpha$, where $f_{\alpha}(x)=$ $f(x-\alpha)$. Translations have already played an important part in our study of Fourier transforms. We now pose a problem whose solution will afford an illustration of how the Plancherel theorem can be used. (Other applications will occur in Chap. 19.) The problem is:

Describe the closed translation-invariant subspaces of $L^{2}$.

Let $M$ be a closed translation-invariant subspace of $L^{2}$, and let $\hat{M}$ be the image of $M$ under the Fourier transform. Then $\hat{M}$ is closed (since the Fourier transform is an $L^{2}$-isometry). If $f_{\alpha}$ is a translate of $f$, the Fourier transform of $f_{\alpha}$ is $\hat{f}_{\alpha}$, where $e_{\alpha}(t)=e^{-i \alpha t}$; we proved this for $f \in L^{1}$ in Theorem 9.2; the result extends to $L^{2}$, as can be seen from Theorem 9.13(d). It follows that $\hat{M}$ is invariant under multiplication by $e_{\alpha}$, for all $\alpha \in R^{1}$.

Let $E$ be any measurable set in $R^{1}$. If $\hat{M}$ is the set of all $\varphi \in L^{2}$ which vanish a.e. on $E$, then $\hat{M}$ certainly is a subspace of $L^{2}$, which is invariant under multiplication by all $e_{\alpha}$ (note that $\left|e_{\alpha}\right|=1$, so $\varphi e_{\alpha} \in L^{2}$ if $\varphi \in L^{2}$ ), and $\hat{M}$ is also closed. Proof: $\varphi \in \hat{M}$ if and only if $\varphi$ is orthogonal to every $\psi \in L^{2}$ which vanishes a.e. on the complement of $E$.

If $M$ is the inverse image of this $\hat{M}$, under the Fourier transform, then $M$ is a space with the desired properties.

One may now conjecture that every one of our spaces $M$ is obtained in this manner, from a set $E \subset R^{1}$. To prove this, we have to show that to every closed translation-invariant $M \subset L^{2}$ there corresponds a set $E \subset R^{1}$ such that $f \in M$ if and only if $\hat{f}(t)=0$ a.e. on $E$. The obvious way of constructing $E$ from $M$ is to associate with each $f \in M$ the set $E_{f}$ consisting of all points at which $\hat{f}(t)=0$, and to define $E$ as the intersection of these sets $E_{f}$. But this obvious attack runs into a serious difficulty: Each $E_{f}$ is defined only up to sets of measure 0 . If $\left\{A_{i}\right\}$ is a countable collection of sets, each determined up to sets of measure 0 , then $\cap A_{i}$ is also determined up to sets of measure 0 . But there are uncountably many $f \in M$, so we lose all control over $\cap E_{f}$.

This difficulty disappears entirely if we think of our functions as elements of the Hilbert space $L^{2}$, and not primarily as point functions.

We shall now prove the conjecture. Let $\hat{M}$ be the image of a closed translation-invariant subspace $M \subset L^{2}$, under the Fourier transform. Let $P$ be the
orthogonal projection of $L^{2}$ onto $\hat{M}$ (Theorem 4.11): To each $f \in L^{2}$ there corresponds a unique $P f \in \hat{M}$ such that $f-P f$ is orthogonal to $\hat{M}$. Hence

$$
f-P f \perp P g \quad\left(f \text { and } g \in L^{2}\right)
$$

and since $\hat{M}$ is invariant under multiplication by $e_{\alpha}$, we also have

$$
f-P f \perp(P g) e_{\alpha} \quad\left(f \text { and } g \in L^{2}, \alpha \in R^{1}\right) .
$$

If we recall how the inner product is defined in $L^{2}$, we see that (2) is equivalent to

$$
\int_{-\infty}^{\infty}(f-P f) \cdot \overline{P g} \cdot e_{-\alpha} d m=0 \quad\left(f \text { and } g \in L^{2}, \alpha \in R^{1}\right)
$$

and this says that the Fourier transform of

$$
(f-P f) \cdot \overline{P g}
$$

is 0 . The function (4) is the product of two $L^{2}$-functions, hence is in $L^{1}$, and the uniqueness theorem for Fourier transforms shows now that the function (4) is 0 a.e. This remains true if $\overline{P g}$ is replaced by $P g$. Hence

$$
f \cdot P g=(P f) \cdot(P g) \quad\left(f \text { and } g \in L^{2}\right) .
$$

Interchanging the roles of $f$ and $g$ leads from (5) to

$$
f \cdot P g=g \cdot P f \quad\left(f \text { and } g \in L^{2}\right) .
$$

Now let $g$ be a fixed positive function in $L^{2}$; for instance, put $g(t)=e^{-|t|}$. Define

$$
\varphi(t)=\frac{(P g)(t)}{g(t)}
$$

$(P g)(t)$ may only be defined a.e.; choose any one determination in (7). Now (6) becomes

$$
P f=\varphi \cdot f \quad\left(f \in L^{2}\right)
$$

If $f \in \hat{M}$, then $P f=f$. This says that $P^{2}=P$, and it follows that $\varphi^{2}=\varphi$, because

$$
\varphi^{2} \cdot g=\varphi \cdot P g=P^{2} g=P g=\varphi \cdot g
$$

Since $\varphi^{2}=\varphi$, we have $\varphi=0$ or 1 a.e., and if we let $E$ be the set of all $t$ where $\varphi(t)=0$, then $\hat{M}$ consists precisely of those $f \in L^{2}$ which are 0 a.e. on $E$, since $f \in \hat{M}$ if and only if $f=P f=\varphi \cdot f$.

We therefore obtain the following solution to our problem.

9.17 Theorem Associate to each measurable set $E \subset R^{1}$ the space $M_{E}$ of all $f \in L^{2}$ such that $\hat{f}=0$ a.e. on $E$. Then $M_{E}$ is a closed translation-invariant subspace of $L^{2}$. Every closed translation-invariant subspace of $L^{2}$ is $M_{E}$ for some $E$, and $M_{A}=M_{B}$ if and only if

$$
m((A-B) \cup(B-A))=0 .
$$

The uniqueness statement is easily proved; we leave the details to the reader. The above problem can of course be posed in other function spaces. It has been studied in great detail in $L^{1}$. The known results show that the situation is infinitely more complicated there than in $L^{2}$.

## The Banach Algebra $L^{1}$

9.18 Definition A Banach space $A$ is said to be a Banach algebra if there is a multiplication defined in $A$ which satisfies the inequality

$$
\|x y\| \leq\|x\|\|y\| \quad(x \text { and } y \in A)
$$

the associative law $x(y z)=(x y) z$, the distributive laws

$$
x(y+z)=x y+x z, \quad(y+z) x=y x+z x \quad(x, y, \text { and } z \in A)
$$

and the relation

$$
(\alpha x) y=x(\alpha y)=\alpha(x y)
$$

where $\alpha$ is any scalar.

### 9.19 Examples

(a) Let $A=C(X)$, where $X$ is a compact Hausdorff space, with the supremum norm and the usual pointwise multiplication of functions: $(f g)(x)=f(x) g(x)$. This is a commutative Banach algebra $(f g=g f)$ with unit (the constant function 1).

(b) $C_{0}\left(R^{1}\right)$ is a commutative Banach algebra without unit, i.e., without an element $u$ such that $u f=f$ for all $f \in C_{0}\left(R^{1}\right)$.

(c) The set of all linear operators on $R^{k}$ (or on any Banach space), with the operator norm as in Definition 5.3, and with addition and multiplication defined by

$$
(A+B)(x)=A x+B x, \quad(A B) x=A(B x)
$$

is a Banach algebra with unit which is not commutative when $k>1$.

(d) $L^{1}$ is a Banach algebra if we define multiplication by convolution; since

$$
\|f * g\|_{1} \leq\|f\|_{1}\|g\|_{1},
$$

the norm inequality is satisfied. The associative law could be verified directly (an application of Fubini's theorem), but we can proceed as
follows: We know that the Fourier transform of $f * g$ is $\hat{f} \cdot \hat{g}$, and we know that the mapping $f \rightarrow f$ is one-to-one. For every $t \in R^{1}$,

$$
\hat{f}(t)[\hat{g}(t) \hat{h}(t)]=[\hat{f}(t) \hat{g}(t)] \hat{h}(t)
$$

by the associative law for complex numbers. It follows that

$$
f *(g * h)=(f * g) * h
$$

In the same way we see immediately that $f * g=g * f$. The remaining requirements of Definition 9.18 are also easily seen to hold in $L^{1}$.

Thus $L^{1}$ is a commutative Banach algebra. The Fourier transform is an algebra isomorphism of $L^{1}$ into $C_{0}$. Hence there is no $f \in L^{1}$ with $\hat{f} \equiv 1$, and therefore $L^{1}$ has no unit.

9.20 Complex Homomorphisms The most important complex functions on a Banach algebra $A$ are the homomorphisms of $A$ into the complex field. These are precisely the linear functionals which also preserve multiplication, i.e., the functions $\varphi$ such that

$$
\varphi(\alpha x+\beta y)=\alpha \varphi(x)+\beta \varphi(y), \quad \varphi(x y)=\varphi(x) \varphi(y)
$$

for all $x$ and $y \in A$ and all scalars $\alpha$ and $\beta$. Note that no boundedness assumption is made in this definition. It is a very interesting fact that this would be redundant:

9.21 Theorem If $\varphi$ is a complex homomorphism on a Banach algebra A, then the norm of $\varphi$, as a linear functional, is at most 1 .

Proof Assume, to get a contradiction, that $\left|\varphi\left(x_{0}\right)\right|>\left\|x_{0}\right\|$ for some $x_{0} \in A$. Put $\lambda=\varphi\left(x_{0}\right)$, and put $x=x_{0} / \lambda$. Then $\|x\|<1$ and $\varphi(x)=1$.

Since $\left\|x^{n}\right\| \leq\|x\|^{n}$ and $\|x\|<1$, the elements

$$
s_{n}=-x-x^{2}-\cdots-x^{n}
$$

form a Cauchy sequence in $A$. Since $A$ is complete, being a Banach space, there exists a $y \in A$ such that $\left\|y-s_{n}\right\| \rightarrow 0$, and it is easily seen that $x+s_{n}=$ $x s_{n-1}$, so that

$$
x+y=x y .
$$

Hence $\varphi(x)+\varphi(y)=\varphi(x) \varphi(y)$, which is impossible since $\varphi(x)=1$.

9.22 The Complex Homomorphisms of $L^{1}$ Suppose $\varphi$ is a complex homomorphism of $L^{1}$, i.e., a linear functional (of norm at most 1 , by Theorem 9.21) which also satisfies the relation

$$
\varphi(f * g)=\varphi(f) \varphi(g) \quad\left(f \text { and } g \in L^{1}\right)
$$

By Theorem 6.16, there exists a $\beta \in L^{\infty}$ such that

$$
\varphi(f)=\int_{-\infty}^{\infty} f(x) \beta(x) d m(x) \quad\left(f \in L^{1}\right)
$$

We now exploit the relation (1) to see what else we can say about $\beta$. On the one hand,

$$
\begin{aligned}
\varphi(f * g) & =\int_{-\infty}^{\infty}(f * g)(x) \beta(x) d m(x) \\
& =\int_{-\infty}^{\infty} \beta(x) d m(x) \int_{-\infty}^{\infty} f(x-y) g(y) d m(y) \\
& =\int_{-\infty}^{\infty} g(y) d m(y) \int_{-\infty}^{\infty} f_{y}(x) \beta(x) d m(x) \\
& =\int_{-\infty}^{\infty} g(y) \varphi\left(f_{y}\right) d m(y) .
\end{aligned}
$$

On the other hand,

$$
\varphi(f) \varphi(g)=\varphi(f) \int_{-\infty}^{\infty} g(y) \beta(y) d m(y)
$$

Let us now assume that $\varphi$ is not identically 0 . Fix $f \in L^{1}$ so that $\varphi(f) \neq 0$. Since the last integral in (3) is equal to the right side of (4) for every $g \in L^{1}$, the uniqueness assertion of Theorem 6.16 shows that

$$
\varphi(f) \beta(y)=\varphi\left(f_{y}\right)
$$

for almost all $y$. But $y \rightarrow f_{y}$ is a continuous mapping of $R^{1}$ into $L^{1}$ (Theorem 9.5) and $\varphi$ is continuous on $L^{1}$. Hence the right side of (5) is a continuous function of $y$, and we may assume [by changing $\beta(y)$ on a set of measure 0 if necessary, which does not affect (2)] that $\beta$ is continuous. If we replace $y$ by $x+y$ and then $f$ by $f_{x}$ in (5), we obtain

$$
\varphi(f) \beta(x+y)=\varphi\left(f_{x+y}\right)=\varphi\left(\left(f_{x}\right)_{y}\right)=\varphi\left(f_{x}\right) \beta(y)=\varphi(f) \beta(x) \beta(y)
$$

so that

$$
\beta(x+y)=\beta(x) \beta(y) \quad\left(x \text { and } y \in R^{1}\right) .
$$

Since $\beta$ is not identically $0,(6)$ implies that $\beta(0)=1$, and the continuity of $\beta$ shows that there is a $\delta>0$ such that

$$
\int_{0}^{\delta} \beta(y) d y=c \neq 0
$$

Then

$$
c \beta(x)=\int_{0}^{\delta} \beta(y) \beta(x) d y=\int_{0}^{\delta} \beta(y+x) d y=\int_{x}^{x+\delta} \beta(y) d y
$$

Since $\beta$ is continuous, the last integral is a differentiable function of $x$; hence (8) shows that $\beta$ is differentiable. Differentiate (6) with respect to $y$, then put $y=0$; the result is

$$
\beta^{\prime}(x)=A \beta(x), \quad A=\beta^{\prime}(0)
$$

Hence the derivative of $\beta(x) e^{-A x}$ is 0 , and since $\beta(0)=1$, we obtain

$$
\beta(x)=e^{A x}
$$

But $\beta$ is bounded on $R^{1}$. Therefore $A$ must be pure imaginary, and we conclude: There exists a $t \in R^{1}$ such that

$$
\beta(x)=e^{-i t x} \text {. }
$$

We have thus arrived at the Fourier transform.

9.23 Theorem To every complex homomorphism $\varphi$ on $L^{1}$ (except to $\varphi=0$ ) there corresponds a unique $t \in R^{1}$ such that $\varphi(f)=\hat{f}(t)$.

The existence of $t$ was proved above. The uniqueness follows from the observation that if $t \neq s$ then there exists an $f \in L^{1}$ such that $\hat{f}(t) \neq \hat{f}(s)$; take for $f(x)$ a suitable translate of $e^{-|x|}$.

## Exercises

1 Suppose $f \in L^{1}, f>0$. Prove that $|\hat{f}(y)|<\hat{f}(0)$ for every $y \neq 0$.

2 Compute the Fourier transform of the characteristic function of an interval. For $n=1,2,3, \ldots$, let $g_{n}$ be the characteristic function of $[-n, n]$, let $h$ be the characteristic function of $[-1,1]$, and compute $g_{n} * h$ explicitly. (The graph is piecewise linear.) Show that $g_{n} * h$ is the Fourier transform of a function $f_{n} \in L^{1}$; except for a multiplicative constant,

$$
f_{n}(x)=\frac{\sin x \sin n x}{x^{2}}
$$

Show that $\left\|f_{n}\right\|_{1} \rightarrow \infty$ and conclude that the mapping $f \rightarrow \hat{f}$ maps $L^{1}$ into a proper subset of $C_{0}$.

Show, however, that the range of this mapping is dense in $C_{0}$.

3 Find

$$
\lim _{A \rightarrow \infty} \int_{-A}^{A} \frac{\sin \lambda t}{t} e^{i t x} d t \quad(-\infty<x<\infty)
$$

where $\lambda$ is a positive constant.

4 Give examples of $f \in L^{2}$ such that $f \notin L^{1}$ but $\hat{f} \in L^{1}$. Under what circumstances can this happen?

5 If $f \in L^{1}$ and $\int|t \hat{f}(t)| d m(t)<\infty$, prove that $f$ coincides a.e. with a differentiable function whose derivative is

$$
i \int_{-\infty}^{\infty} t \hat{f}(t) e^{i x t} d m(t)
$$

6 Suppose $f \in L^{1}, f$ is differentiable almost everywhere, and $f^{\prime} \in L^{1}$. Does it follow that the Fourier transform of $f^{\prime}$ is $t i \hat{f}(t)$ ?

7 Let $S$ be the class of all functions $f$ on $R^{1}$ which have the following property: $f$ is infinitely differentiable, and there are numbers $A_{m n}(f)<\infty$, for $m$ and $n=0,1,2, \ldots$, such that

$$
\left|x^{n} D^{m} f(x)\right| \leq A_{m n}(f) \quad\left(x \in R^{1}\right)
$$

Here $D$ is the ordinary differentiation operator.

Prove that the Fourier transform maps $S$ onto $S$. Find examples of members of $S$.

8 If $p$ and $q$ are conjugate exponents, $f \in L^{p}, g \in L^{q}$, and $h=f * g$, prove that $h$ is uniformly continuous. If also $1<p<\infty$, then $h \in C_{0}$; show that this fails for some $f \in L^{1}, g \in L^{\infty}$.

9 Suppose $1 \leq p<\infty, f \in L^{p}$, and

$$
g(x)=\int_{x}^{x+1} f(t) d t
$$

Prove that $g \in C_{0}$. What can you say about $g$ if $f \in L^{\infty}$ ?

10 Let $C^{\infty}$ be the class of all infinitely differentiable complex functions on $R^{1}$, and let $C_{c}^{\infty}$ consist of all $g \in C^{\infty}$ whose supports are compact. Show that $C_{c}^{\infty}$ does not consist of 0 alone.

Let $L_{\mathrm{loc}}^{1}$ be the class of all $f$ which belong to $L^{1}$ locally; that is, $f \in L_{\mathrm{loc}}^{1}$ provided that $f$ is measurable and $\int_{I}|f|<\infty$ for every bounded interval $I$.

If $f \in L_{\mathrm{loc}}^{1}$ and $g \in C_{c}^{\infty}$, prove that $f * g \in C^{\infty}$.

Prove that there are sequences $\left\{g_{n}\right\}$ in $C_{c}^{\infty}$ such that

$$
\left\|f * g_{n}-f\right\|_{1} \rightarrow 0
$$

as $n \rightarrow \infty$, for every $f \in L^{1}$. (Compare Theorem 9.10.) Prove that $\left\{g_{n}\right\}$ can also be so chosen that $\left(f * g_{n}\right)(x) \rightarrow f(x)$ a.e., for every $f \in L_{\text {loc }}^{1}$; in fact, for suitable $\left\{g_{n}\right\}$ the convergence occurs at every point $x$ at which $f$ is the derivative of its indefinite integral.

Prove that $\left(f * h_{\lambda}\right)(x) \rightarrow f(x)$ a.e. if $f \in L^{1}$, as $\lambda \rightarrow 0$, and that $f * h_{\lambda} \in C^{\infty}$, although $h_{\lambda}$ does not have compact support. $\left(h_{\lambda}\right.$ is defined in Sec. 9.7.)

11 Find conditions on $f$ and/or $\hat{f}$ which ensure the correctness of the following formal argument: If

$$
\varphi(t)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} f(x) e^{-i t x} d x
$$

and

$$
F(x)=\sum_{k=-\infty}^{\infty} f(x+2 k \pi)
$$

then $F$ is periodic, with period $2 \pi$, the $n$th Fourier coefficient of $F$ is $\varphi(n)$, hence $F(x)=\sum \varphi(n) e^{i n x}$. In particular,

$$
\sum_{k=-\infty}^{\infty} f(2 k \pi)=\sum_{n=-\infty}^{\infty} \varphi(n)
$$

More generally,

$$
\sum_{k=-\infty}^{\infty} f(k \beta)=\alpha \sum_{n=-\infty}^{\infty} \varphi(n \alpha) \quad \text { if } \alpha>0, \beta>0, \alpha \beta=2 \pi
$$

What does $(*)$ say about the limit, as $\alpha \rightarrow 0$, of the right-hand side (for "nice" functions, of course)? Is this in agreement with the inversion theorem?

$[(*)$ is known as the Poisson summation formula. $]$

12 Take $f(x)=e^{-|x|}$ in Exercise 11 and derive the identity

$$
\frac{e^{2 \pi \alpha}+1}{e^{2 \pi \alpha}-1}=\frac{1}{\pi} \sum_{n=-\infty}^{\infty} \frac{\alpha}{\alpha^{2}+n^{2}}
$$

13 If $0<c<\infty$, define $f_{c}(x)=\exp \left(-c x^{2}\right)$.

(a) Compute $\hat{f}_{c}$. Hint: If $\varphi=\hat{f}_{c}$, an integration by parts gives $2 c \varphi^{\prime}(t)+t \varphi(t)=0$.

(b) Show that there is one (and only one) $c$ for which $\hat{f}_{c}=f_{c}$.

(c) Show that $f_{a} * f_{b}=\gamma f_{c}$; find $\gamma$ and $c$ explicitly in terms of $a$ and $b$.

(d) Take $f=f_{c}$ in Exercise 11. What is the resulting identity?

14 The Fourier transform can be defined for $f \in L^{1}\left(R^{k}\right)$ by

$$
\hat{f}(y)=\int_{R^{k}} f(x) e^{-i x \cdot y} d m_{k}(x) \quad\left(y \in R^{k}\right)
$$

where $x \cdot y=\sum \xi_{i} \eta_{i}$ if $x=\left(\xi_{1}, \ldots, \xi_{k}\right), y=\left(\eta_{1}, \ldots, \eta_{k}\right)$, and $m_{k}$ is Lebesgue measure on $R^{k}$, divided by $(2 \pi)^{k / 2}$ for convenience. Prove the inversion theorem and the Plancherel theorem in this context, as well as the analogue of Theorem 9.23.

15 If $f \in L^{1}\left(R^{k}\right), A$ is a linear operator on $R^{k}$, and $g(x)=f(A x)$, how is $\hat{g}$ related to $\hat{f}$ ? If $f$ is invariant under rotations, i.e., if $f(x)$ depends only on the euclidean distance of $x$ from the origin, prove that the same is true of $\hat{f}$.

16 The Laplacian of a function $f$ on $R^{k}$ is

$$
\Delta f=\sum_{j=1}^{k} \frac{\partial^{2} f}{\partial x_{j}^{2}}
$$

provided the partial derivatives exist. What is the relation between $\hat{f}$ and $\hat{g}$ if $g=\Delta f$ and all necessary integrability conditions are satisfied? It is clear that the Laplacian commutes with translations. Prove that it also commutes with rotations, i.e., that

$$
\Delta(f \circ A)=(\Delta f) \circ A
$$

whenever $f$ has continuous second derivatives and $A$ is a rotation of $R^{k}$. (Show that it is enough to do this under the additional assumption that $f$ has compact support.)

17 Show that every Lebesgue measurable character of $R^{1}$ is continuous. Do the same for $R^{k}$. (Adapt part of the proof of Theorem 9.23.) Compare with Exercise 18.

18 Show (with the aid of the Hausdorff maximality theorem) that there exist real discontinuous functions $f$ on $R^{1}$ such that

$$
f(x+y)=f(x)+f(y)
$$

for all $x$ and $y \in R^{1}$

Show that if (1) holds and $f$ is Lebesgue measurable, then $f$ is continuous.

Show that if (1) holds and the graph of $f$ is not dense in the plane, then $f$ is continuous.

Find all continuous functions which satisfy (1).

19 Suppose $A$ and $B$ are measurable subsets of $R^{1}$, having finite positive measure. Show that the convolution $\chi_{A} * \chi_{B}$ is continuous and not identically 0 . Use this to prove that $A+B$ contains a segment.

(A different proof was suggested in Exercise 5, Chap. 7.)

## ELEMENTARY PROPERTIES OF HOLOMORPHIC FUNCTIONS

## Complex Differentiation

We shall now study complex functions defined in subsets of the complex plane. It will be convenient to adopt some standard notations which will be used throughout the rest of this book.

10.1 Definitions If $r>0$ and $a$ is a complex number,

$$
D(a ; r)=\{z:|z-a|<r\}
$$

is the open circular disc with center at $a$ and radius $r . \bar{D}(a ; r)$ is the closure of $D(a ; r)$, and

$$
D^{\prime}(a ; r)=\{z: 0<|z-a|<r\}
$$

is the punctured disc with center at $a$ and radius $r$.

A set $E$ in a topological space $X$ is said to be not connected if $E$ is the union of two nonempty sets $A$ and $B$ such that

$$
\bar{A} \cap B=\varnothing=A \cap \bar{B}
$$

If $A$ and $B$ are as above, and if $V$ and $W$ are the complements of $\bar{A}$ and $\bar{B}$, respectively, it follows that $A \subset W$ and $B \subset V$. Hence

$$
E \subset V \cup W, \quad E \cap V \neq \varnothing, \quad E \cap W \neq \varnothing, \quad E \cap V \cap W=\varnothing
$$

Conversely, if open sets $V$ and $W$ exist such that (4) holds, it is easy to see that $E$ is not connected, by taking $A=E \cap W, B=E \cap V$.

If $E$ is closed and not connected, then (3) shows that $E$ is the union of two disjoint nonempty closed sets; for if $\bar{A} \subset A \cup B$ and $\bar{A} \cap B=\varnothing$, then $\bar{A}=A$.

If $E$ is open and not connected, then (4) shows that $E$ is the union of two disjoint nonempty open sets, namely $E \cap V$ and $E \cap W$.

Each set consisting of a single point is obviously connected. If $x \in E$, the family $\Phi_{x}$ of all connected subsets of $E$ that contain $x$ is therefore not empty. The union of all members of $\Phi_{x}$ is easily seen to be connected, and to be a maximal connected subset of $E$. These sets are called the components of $E$. Any two components of $E$ are thus disjoint, and $E$ is the union of its components.

By a region we shall mean a nonempty connected open subset of the complex plane. Since each open set $\Omega$ in the plane is a union of discs, and since all discs are connected, each component of $\Omega$ is open. Every plane open set is thus a union of disjoint regions. The letter $\Omega$ will from now on denote a plane open set.

10.2 Definition Suppose $f$ is a complex function defined in $\Omega$. If $z_{0} \in \Omega$ and if

$$
\lim _{z \rightarrow z_{0}} \frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}
$$

exists, we denote this limit by $f^{\prime}\left(z_{0}\right)$ and call it the derivative of $f$ at $z_{0}$. If $f^{\prime}\left(z_{0}\right)$ exists for every $z_{0} \in \Omega$, we say that $f$ is holomorphic (or analytic) in $\Omega$. The class of all holomorphic functions in $\Omega$ will be denoted by $H(\Omega)$.

To be quite explicit, $f^{\prime}\left(z_{0}\right)$ exists if to every $\epsilon>0$ there corresponds a $\delta>0$ such that

$$
\left|\frac{f(z)-f\left(z_{0}\right)}{z-z_{0}}-f^{\prime}\left(z_{0}\right)\right|<\epsilon \quad \text { for all } z \in D^{\prime}\left(z_{0} ; \delta\right)
$$

Thus $f^{\prime}\left(z_{0}\right)$ is a complex number, obtained as a limit of quotients of complex numbers. Note that $f$ is a mapping of $\Omega$ into $R^{2}$ and that Definition 7.22 associates with such mappings another kind of derivative, namely, a linear operator on $R^{2}$. In our present situation, if (2) is satisfied, this linear operator turns out to be multiplication by $f^{\prime}\left(z_{0}\right)$ (regarding $R^{2}$ as the complex field). We leave it to the reader to verify this.

10.3 Remarks If $f \in H(\Omega)$ and $g \in H(\Omega)$, then also $f+g \in H(\Omega)$ and $f g \in H(\Omega)$, so that $H(\Omega)$ is a ring; the usual differentiation rules apply.

More interesting is the fact that superpositions of holomorphic functions are holomorphic: If $f \in H(\Omega)$, if $f(\Omega) \subset \Omega_{1}$, if $g \in H\left(\Omega_{1}\right)$, and if $h=g \circ f$, then $h \in H(\Omega)$, and $h^{\prime}$ can be computed by the chain rule

$$
h^{\prime}\left(z_{0}\right)=g^{\prime}\left(f\left(z_{0}\right)\right) f^{\prime}\left(z_{0}\right) \quad\left(z_{0} \in \Omega\right)
$$

To prove this, fix $z_{0} \in \Omega$, and put $w_{0}=f\left(z_{0}\right)$. Then

$$
\begin{aligned}
f(z)-f\left(z_{0}\right) & =\left[f^{\prime}\left(z_{0}\right)+\epsilon(z)\right]\left(z-z_{0}\right) \\
g(w)-g\left(w_{0}\right) & =\left[g^{\prime}\left(w_{0}\right)+\eta(w)\right]\left(w-w_{0}\right)
\end{aligned}
$$

where $\epsilon(z) \rightarrow 0$ as $z \rightarrow z_{0}$ and $\eta(w) \rightarrow 0$ as $w \rightarrow w_{0}$. Put $w=f(z)$, and substitute (2) into (3): If $z \neq z_{0}$,

$$
\frac{h(z)-h\left(z_{0}\right)}{z-z_{0}}=\left[g^{\prime}\left(f\left(z_{0}\right)\right)+\eta(f(z))\right]\left[f^{\prime}\left(z_{0}\right)+\epsilon(z)\right]
$$

The differentiability of $f$ forces $f$ to be continuous at $z_{0}$. Hence (1) follows from (4).

10.4 Examples For $n=0,1,2, \ldots, z^{n}$ is holomorphic in the whole plane, and the same is true of every polynomial in $z$. One easily verifies directly that $1 / z$ is holomorphic in $\{z: z \neq 0\}$. Hence, taking $g(w)=1 / w$ in the chain rule, we see that if $f_{1}$ and $f_{2}$ are in $H(\Omega)$ and $\Omega_{0}$ is an open subset of $\Omega$ in which $f_{2}$ has no zero, then $f_{1} / f_{2} \in H\left(\Omega_{0}\right)$.

Another example of a function which is holomorphic in the whole plane (such functions are called entire) is the exponential function defined in the Prologue. In fact, we saw there that exp is differentiable everywhere, in the sense of Definition 10.2, and that $\exp ^{\prime}(z)=\exp (z)$ for every complex $z$.

10.5 Power Series From the theory of power series we shall assume only one fact as known, namely, that to each power series

$$
\sum_{n=0}^{\infty} c_{n}(z-a)^{n}
$$

there corresponds a number $R \in[0, \infty]$ such that the series converges absolutely and uniformly in $\bar{D}(a ; r)$, for every $r<R$, and diverges if $z \notin \bar{D}(a ; R)$. The "radius of convergence" $R$ is given by the root test:

$$
\frac{1}{R}=\lim _{n \rightarrow \infty} \sup _{n}\left|c_{n}\right|^{1 / n}
$$

Let us say that a function $f$ defined in $\Omega$ is representable by power series in $\Omega$ if to every disc $D(a ; r) \subset \Omega$ there corresponds a series (1) which converges to $f(z)$ for all $z \in D(a ; r)$.

10.6 Theorem If $f$ is representable by power series in $\Omega$, then $f \in H(\Omega)$ and $f^{\prime}$ is also representable by power series in $\Omega$. In fact, if

$$
f(z)=\sum_{n=0}^{\infty} c_{n}(z-a)^{n}
$$

for $z \in D(a ; r)$, then for these $z$ we also have

$$
f^{\prime}(z)=\sum_{n=1}^{\infty} n c_{n}(z-a)^{n-1}
$$

Proof If the series (1) converges in $D(a ; r)$, the root test shows that the series (2) also converges there. Take $a=0$, without loss of generality, denote the sum of the series (2) by $g(z)$, fix $w \in D(a ; r)$, and choose $\rho$ so that $|w|<\rho<r$. If $z \neq w$, we have

$$
\frac{f(z)-f(w)}{z-w}-g(w)=\sum_{n=1}^{\infty} c_{n}\left[\frac{z^{n}-w^{n}}{z-w}-n w^{n-1}\right]
$$

The expression in brackets is 0 if $n=1$, and is

$$
(z-w) \sum_{k=1}^{n-1} k w^{k-1} z^{n-k-1}
$$

if $n \geq 2$. If $|z|<\rho$, the absolute value of the sum in (4) is less than

$$
\frac{n(n-1)}{2} \rho^{n-2}
$$

so

$$
\left|\frac{f(z)-f(w)}{z-w}-g(w)\right| \leq|z-w| \sum_{n=2}^{\infty} n^{2}\left|c_{n}\right| \rho^{n-2}
$$

Since $\rho<r$, the last series converges. Hence the left side of (6) tends to 0 as $z \rightarrow w$. This says that $f^{\prime}(w)=g(w)$, and completes the proof.

Corollary Since $f^{\prime}$ is seen to satisfy the same hypothesis as $f$ does, the theorem can be applied to $f^{\prime}$. It follows that $f$ has derivatives of all orders, that each derivative is representable by power series in $\Omega$, and that

$$
f^{(k)}(z)=\sum_{n=k}^{\infty} n(n-1) \cdots(n-k+1) c_{n}(z-a)^{n-k}
$$

if (1) holds. Hence (1) implies that

$$
k ! c_{k}=f^{(k)}(a) \quad(k=0,1,2, \ldots)
$$

so that for each $a \in \Omega$ there is a unique sequence $\left\{c_{n}\right\}$ for which (1) holds.

We now describe a process which manufactures functions that are representable by power series. Special cases will be of importance later.

10.7 Theorem Suppose $\mu$ is a complex (finite) measure on a measurable space $X, \varphi$ is a complex measurable function on $X, \Omega$ is an open set in the plane which does not intersect $\varphi(X)$, and

$$
f(z)=\int_{X} \frac{d \mu(\zeta)}{\varphi(\zeta)-z} \quad(z \in \Omega)
$$

Then $f$ is representable by power series in $\Omega$.

Proof Suppose $D(a ; r) \subset \Omega$. Since

$$
\left|\frac{z-a}{\varphi(\zeta)-a}\right| \leq \frac{|z-a|}{r}<1
$$

for every $z \in D(a ; r)$ and every $\zeta \in X$, the geometric series

$$
\sum_{n=0}^{\infty} \frac{(z-a)^{n}}{(\varphi(\zeta)-a)^{n+1}}=\frac{1}{\varphi(\zeta)-z}
$$

converges uniformly on $X$, for every fixed $z \in D(a ; r)$. Hence the series (3) may be substituted into (1), and $f(z)$ may be computed by interchanging summation and integration. It follows that

$$
f(z)=\sum_{0}^{\infty} c_{n}(z-a)^{n} \quad(z \in D(a ; r))
$$

where

$$
c_{n}=\int_{X} \frac{d \mu(\zeta)}{(\varphi(\zeta)-a)^{n+1}} \quad(n=0,1,2, \ldots)
$$

Note: The convergence of the series (4) in $D(a ; r)$ is a consequence of the proof. We can also derive it from (5), since (5) shows that

$$
\left|c_{n}\right| \leq \frac{|\mu|(X)}{r^{n+1}} \quad(n=0,1,2, \ldots)
$$

## Integration over Paths

Our first major objective in this chapter is the converse of Theorem 10.6: Every $f \in H(\Omega)$ is representable by power series in $\Omega$. The quickest route to this is via Cauchy's theorem which leads to an important integral representation of holomorphic functions. In this section the required integration theory will be developed; we shall keep it as simple as possible, and shall regard it merely as a useful tool in the investigation of properties of holomorphic functions.

10.8 Definitions If $X$ is a topological space, a curve in $X$ is a continuous mapping $\gamma$ of a compact interval $[\alpha, \beta] \subset R^{1}$ into $X$; here $\alpha<\beta$. We call $[\alpha, \beta]$ the parameter interval of $\gamma$ and denote the range of $\gamma$ by $\gamma^{*}$. Thus $\gamma$ is a mapping, and $\gamma^{*}$ is the set of all points $\gamma(t)$, for $\alpha \leq t \leq \beta$.

If the initial point $\gamma(\alpha)$ of $\gamma$ coincides with its end point $\gamma(\beta)$, we call $\gamma$ a closed curve.

A path is a piecewise continuously differentiable curve in the plane. More explicitly, a path with parameter interval $[\alpha, \beta]$ is a continuous complex function $\gamma$ on $[\alpha, \beta]$, such that the following holds: There are finitely many
points $s_{j}, \alpha=s_{0}<s_{1}<\cdots<s_{n}=\beta$, and the restriction of $\gamma$ to each interval $\left[s_{j-1}, s_{j}\right]$ has a continuous derivative on $\left[s_{j-1}, s_{j}\right]$; however, at the points $s_{1}, \ldots, s_{n-1}$ the left- and right-hand derivatives of $\gamma$ may differ.

A closed path is a closed curve which is also a path.

Now suppose $\gamma$ is a path, and $f$ is a continuous function on $\gamma^{*}$. The integral of $f$ over $\gamma$ is defined as an integral over the parameter interval $[\alpha, \beta]$ of $\gamma$ :

$$
\int_{\gamma} f(z) d z=\int_{\alpha}^{\beta} f(\gamma(t)) \gamma^{\prime}(t) d t
$$

Let $\varphi$ be a continuously differentiable one-to-one mapping of an interval $\left[\alpha_{1}, \beta_{1}\right]$ onto $[\alpha, \beta]$, such that $\varphi\left(\alpha_{1}\right)=\alpha, \varphi\left(\beta_{1}\right)=\beta$, and put $\gamma_{1}=\gamma \circ \varphi$. Then $\gamma_{1}$ is a path with parameter interval $\left[\alpha_{1}, \beta_{1}\right]$; the integral of $f$ over $\gamma_{1}$ is

$$
\int_{\alpha_{1}}^{\beta_{1}} f\left(\gamma_{1}(t)\right) \gamma_{1}^{\prime}(t) d t=\int_{\alpha_{1}}^{\beta_{1}} f(\gamma(\varphi(t))) \gamma^{\prime}(\varphi(t)) \varphi^{\prime}(t) d t=\int_{\alpha}^{\beta} f(\gamma(s)) \gamma^{\prime}(s) d s
$$

so that our "reparametrization" has not changed the integral:

$$
\int_{\gamma_{1}} f(z) d z=\int_{\gamma} f(z) d z
$$

Whenever (2) holds for a pair of paths $\gamma$ and $\gamma_{1}$ (and for all $f$ ), we shall regard $\gamma$ and $\gamma_{1}$ as equivalent.

It is convenient to be able to replace a path by an equivalent one, i.e., to choose parameter intervals at will. For instance, if the end point of $\gamma_{1}$ coincides with the initial point of $\gamma_{2}$, we may locate their parameter intervals so that $\gamma_{1}$ and $\gamma_{2}$ join to form one path $\gamma$, with the property that

$$
\int_{\gamma} f=\int_{\gamma_{1}} f+\int_{\gamma_{2}} f
$$

for every continuous $f$ on $\gamma^{*}=\gamma_{1}^{*} \cup \gamma_{2}^{*}$.

However, suppose that $[0,1]$ is the parameter interval of a path $\gamma$, and $\gamma_{1}(t)=\gamma(1-t), 0 \leq t \leq 1$. We call $\gamma_{1}$ the path opposite to $\gamma$, for the following reason: For any $f$ continuous on $\gamma_{1}^{*}=\gamma^{*}$, we have

$$
\int_{0}^{1} f\left(\gamma_{1}(t)\right) \gamma_{1}^{\prime}(t) d t=-\int_{0}^{1} f(\gamma(1-t)) \gamma^{\prime}(1-t) d t=-\int_{0}^{1} f(\gamma(s)) \gamma^{\prime}(s) d s
$$

so that

$$
\int_{\gamma_{1}} f=-\int_{\gamma} f .
$$

From (1) we obtain the inequality

$$
\left|\int_{\gamma} f(z) d z\right| \leq\|f\|_{\infty} \int_{\alpha}^{\beta}\left|\gamma^{\prime}(t)\right| d t
$$

where $\|f\|_{\infty}$ is the maximum of $|f|$ on $\gamma^{*}$ and the last integral in (5) is (by definition) the length of $\gamma$.

### 10.9 Special Cases

(a) If $a$ is a complex number and $r>0$, the path defined by

$$
\gamma(t)=a+r e^{i t} \quad(0 \leq t \leq 2 \pi)
$$

is called the positively oriented circle with center at $a$ and radius $r$; we have

$$
\int_{\gamma} f(z) d z=i r \int_{0}^{2 \pi} f\left(a+r e^{i \theta}\right) e^{i \theta} d \theta
$$

and the length of $\gamma$ is $2 \pi r$, as expected.

(b) If $a$ and $b$ are complex numbers, the path $\gamma$ given by

$$
\gamma(t)=a+(b-a) t \quad(0 \leq t \leq 1)
$$

is the oriented interval $[a, b]$; its length is $|b-a|$, and

$$
\int_{[a, b]} f(z) d z=(b-a) \int_{0}^{1} f[a+(b-a) t] d t
$$

If

$$
\gamma_{1}(t)=\frac{a(\beta-t)+b(t-\alpha)}{\beta-\alpha} \quad(\alpha \leq t \leq \beta)
$$

we obtain an equivalent path, which we still denote by $[a, b]$. The path opposite to $[a, b]$ is $[b, a]$.

(c) Let $\{a, b, c\}$ be an ordered triple of complex numbers, let

$$
\Delta=\Delta(a, b, c)
$$

be the triangle with vertices at $a, b$, and $c$ ( $\Delta$ is the smallest convex set which contains $a, b$, and $c$ ), and define

$$
\int_{\partial \Delta} f=\int_{[a, b]} f+\int_{[b, c]} f+\int_{[c, a]} f
$$

for any $f$ continuous on the boundary of $\Delta$. We may regard (6) as the definition of its left side. Or we may regard $\partial \Delta$ as a path obtained by joining $[a, b]$ to $[b, c]$ to $[c, a]$, as outlined in Definition 10.8, in which case (6) is easily proved to be true.

If $\{a, b, c\}$ is permuted cyclically, we see from (6) that the left side of (6) is unaffected. If $\{a, b, c\}$ is replaced by $\{a, c, b\}$, then the left side of (6) changes sign. theory.

We now come to a theorem which plays a very important role in function

10.10 Theorem Let $\gamma$ be a closed path, let $\Omega$ be the complement of $\gamma^{*}$ (relative to the plane), and define

$$
\operatorname{Ind}_{\gamma}(z)=\frac{1}{2 \pi i} \int_{\gamma} \frac{d \zeta}{\zeta-z} \quad(z \in \Omega)
$$

Then $\operatorname{Ind}_{y}$ is an integer-valued function on $\Omega$ which is constant in each component of $\Omega$ and which is 0 in the unbounded component of $\Omega$.

We call $\operatorname{Ind}_{\gamma}(z)$ the index of $z$ with respect to $\gamma$. Note that $\gamma^{*}$ is compact, hence $\gamma^{*}$ lies in a bounded disc $D$ whose complement $D^{c}$ is connected; thus $D^{c}$ lies in some component of $\Omega$. This shows that $\Omega$ has precisely one unbounded component.

ProOF Let $[\alpha, \beta]$ be the parameter interval of $\gamma$, fix $z \in \Omega$, then

$$
\operatorname{Ind}_{\gamma}(z)=\frac{1}{2 \pi i} \int_{\alpha}^{\beta} \frac{\gamma^{\prime}(s)}{\gamma(s)-z} d s
$$

Since $w / 2 \pi i$ is an integer if and only if $e^{w}=1$, the first assertion of the theorem, namely, that $\operatorname{Ind}_{v}(z)$ is an integer, is equivalent to the assertion that $\varphi(\beta)=1$, where

$$
\varphi(t)=\exp \left\{\int_{\alpha}^{t} \frac{\gamma^{\prime}(s)}{\gamma(s)-z} d s\right\} \quad(\alpha \leq t \leq \beta)
$$

Differentiation of (3) shows that

$$
\frac{\varphi^{\prime}(t)}{\varphi(t)}=\frac{\gamma^{\prime}(t)}{\gamma(t)-z}
$$

except possibly on a finite set $S$ where $\gamma$ is not differentiable. Therefore $\varphi /(\gamma-z)$ is a continuous function on $[\alpha, \beta]$ whose derivative is zero in $[\alpha, \beta]-S$. Since $S$ is finite, $\varphi /(\gamma-z)$ is constant on $[\alpha, \beta]$; and since $\varphi(\alpha)=1$, we obtain

$$
\varphi(t)=\frac{\gamma(t)-z}{\gamma(\alpha)-z} \quad(\alpha \leq t \leq \beta)
$$

We now use the assumption that $\gamma$ is a closed path, i.e., that $\gamma(\beta)=\gamma(\alpha)$; (5) shows that $\varphi(\beta)=1$, and this, as we observed above, implies that $\operatorname{Ind}_{\nu}(z)$ is an integer.

By Theorem 10.7, (1) shows that $\operatorname{Ind}_{y} \in H(\Omega)$. The image of a connected set under a continuous mapping is connected ([26], Theorem 4.22), and since Ind $_{\gamma}$ is an integer-valued function, Ind $_{\gamma}$ must be constant on each component of $\Omega$.

Finally, (2) shows that $\left|\operatorname{Ind}_{y}(z)\right|<1$ if $|z|$ is sufficiently large. This implies that $\operatorname{Ind}_{\gamma}(z)=0$ in the unbounded component of $\Omega$.

Remark: If $\lambda(t)$ denotes the integral in (3), the preceding proof shows that $2 \pi \operatorname{Ind}_{y}(z)$ is the net increase in the imaginary part of $\lambda(t)$, as $t$ runs from $\alpha$ to $\beta$, and this is the same as the net increase of the argument of $\gamma(t)-z$. (We have not defined "argument" and will have no need for it.) If we divide this increase by $2 \pi$, we obtain "the number of times that $\gamma$ winds around $z$," and this explains why the term "winding number" is frequently used for the index. One virtue of the preceding proof is that it establishes the main properties of the index without any reference to the (multiple-valued) argument of a complex number.

10.11 Theorem If $\gamma$ is the positively oriented circle with center at a and radius $r$, then

$$
\operatorname{Ind}_{\gamma}(z)= \begin{cases}1 & \text { if }|z-a|<r \\ 0 & \text { if }|z-a|>r\end{cases}
$$

Proof We take $\gamma$ as in Sec. 10.9(a). By Theorem 10.10, it is enough to compute $\operatorname{Ind}_{\gamma}(a)$, and 10.9(2) shows that this equals

$$
\frac{1}{2 \pi i} \int_{\gamma} \frac{d z}{z-a}=\frac{r}{2 \pi} \int_{0}^{2 \pi}\left(r e^{i t}\right)^{-1} e^{i t} d t=1
$$

## The Local Cauchy Theorem

There are several forms of Cauchy's theorem. They all assert that if $\gamma$ is a closed path or cycle in $\Omega$, and if $\gamma$ and $\Omega$ satisfy certain topological conditions, then the integral of every $f \in H(\Omega)$ over $\gamma$ is 0 . We shall first derive a simple local version of this (Theorem 10.14) which is quite sufficient for many applications. A more general global form will be established later.

10.12 Theorem Suppose $F \in H(\Omega)$ and $F^{\prime}$ is continuous in $\Omega$. Then

$$
\int_{\gamma} F^{\prime}(z) d z=0
$$

for every closed path $\gamma$ in $\Omega$.

ProOF If $[\alpha, \beta]$ is the parameter interval of $\gamma$, the fundamental theorem of calculus shows that

$$
\int_{\gamma} F^{\prime}(z) d z=\int_{\alpha}^{\beta} F^{\prime}(\gamma(t)) \gamma^{\prime}(t) d t=F(\gamma(\beta))-F(\gamma(\alpha))=0,
$$

since $\gamma(\beta)=\gamma(\alpha)$.

Corollary Since $z^{n}$ is the derivative of $z^{n+1} /(n+1)$ for all integers $n \neq-1$, we have

$$
\int_{\gamma} z^{n} d z=0
$$

for every closed path $\gamma$ if $n=0,1,2, \ldots$, and for those closed paths $\gamma$ for which $0 \notin \gamma^{*}$ if $n=-2,-3,-4, \ldots$

The case $n=-1$ was dealt with in Theorem 10.10.

10.13 Cauchy's Theorem for a Triangle Suppose $\Delta$ is a closed triangle in a plane open set $\Omega, p \in \Omega, f$ is continuous on $\Omega$, and $f \in H(\Omega-\{p\})$. Then

$$
\int_{\partial \Delta} f(z) d z=0
$$

For the definition of $\partial \Delta$ we refer to Sec. $10.9(c)$. We shall see later that our hypothesis actually implies that $f \in H(\Omega)$, i.e., that the exceptional point $p$ is not really exceptional. However, the above formulation of the theorem will be useful in the proof of the Cauchy formula.

Proof We assume first that $p \notin \Delta$. Let $a, b$, and $c$ be the vertices of $\Delta$, let $a^{\prime}$, $b^{\prime}$, and $c^{\prime}$ be the midpoints of $[b, c],[c, a]$, and $[a, b]$, respectively, and consider the four triangles $\Delta^{j}$ formed by the ordered triples

$$
\left\{a, c^{\prime}, b^{\prime}\right\}, \quad\left\{b, a^{\prime}, c^{\prime}\right\}, \quad\left\{c, b^{\prime}, a^{\prime}\right\}, \quad\left\{a^{\prime}, b^{\prime}, c^{\prime}\right\}
$$

If $J$ is the value of the integral (1), it follows from 10.9(6) that

$$
J=\sum_{j=1}^{4} \int_{\partial \Delta^{\prime}} f(z) d z
$$

The absolute value of at least one of the integrals on the right of (3) is therefore at least $|J / 4|$. Call the corresponding triangle $\Delta_{1}$, repeat the argument with $\Delta_{1}$ in place of $\Delta$, and so forth. This generates a sequence of triangles $\Delta_{n}$
such that $\Delta \supset \Delta_{1} \supset \Delta_{2} \supset \cdots$, such that the length of $\partial \Delta_{n}$ is $2^{-n} L$, if $L$ is the length of $\partial \Delta$, and such that

$$
|J| \leq 4^{n}\left|\int_{\partial \Delta_{n}} f(z) d z\right| \quad(n=1,2,3, \ldots)
$$

There is a (unique) point $z_{0}$ which the triangles $\Delta_{n}$ have in common. Since $\Delta$ is compact, $z_{0} \in \Delta$, so $f$ is differentiable at $z_{0}$.

Let $\epsilon>0$ be given. There exists an $r>0$ such that

$$
\left|f(z)-f\left(z_{0}\right)-f^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)\right| \leq \epsilon\left|z-z_{0}\right|
$$

whenever $\left|z-z_{0}\right|<r$, and there exists an $n$ such that $\left|z-z_{0}\right|<r$ for all $z \in \Delta_{n}$. For this $n$ we also have $\left|z-z_{0}\right| \leq 2^{-n} L$ for all $z \in \Delta_{n}$. By the Corollary to Theorem 10.12,

$$
\int_{\partial \Delta_{n}} f(z) d z=\int_{\partial \Delta_{n}}\left[f(z)-f\left(z_{0}\right)-f^{\prime}\left(z_{0}\right)\left(z-z_{0}\right)\right] d z,
$$

so that (5) implies

$$
\left|\int_{\partial \Delta_{n}} f(z) d z\right| \leq \epsilon\left(2^{-n} L\right)^{2}
$$

and now (4) shows that $|J| \leq \epsilon L^{2}$. Hence $J=0$ if $p \notin \Delta$.

Assume next that $p$ is a vertex of $\Delta$, say $p=a$. If $a, b$, and $c$ are collinear, then (1) is trivial, for any continuous $f$. If not, choose points $x \in[a, b]$ and $y \in[a, c]$, both close to $a$, and observe that the integral of $f$ over $\partial \Delta$ is the sum of the integrals over the boundaries of the triangles $\{a, x, y\},\{x, b, y\}$, and $\{b, c, y\}$. The last two of these are 0 , since these triangles do not contain $p$. Hence the integral over $\partial \Delta$ is the sum of the integrals over $[a, x],[x, y]$, and $[y, a]$, and since these intervals can be made arbitrarily short and $f$ is bounded on $\Delta$, we again obtain (1).

Finally, if $p$ is an arbitrary point of $\Delta$, apply the preceding result to $\{a, b, p\},\{b, c, p\}$, and $\{c, a, p\}$ to complete the proof.

10.14 Cauchy's Theorem in a Convex Set Suppose $\Omega$ is a convex open set, $p \in \Omega, f$ is continuous on $\Omega$, and $f \in H(\Omega-\{p\})$. Then $f=F^{\prime}$ for some $F \in H(\Omega)$. Hence

$$
\int_{\gamma} f(z) d z=0
$$

for every closed path $\gamma$ in $\Omega$.

Proof Fix $a \in \Omega$. Since $\Omega$ is convex, $\Omega$ contains the straight line interval from $a$ to $z$ for every $z \in \Omega$, so we can define

$$
F(z)=\int_{[a, z]} f(\xi) d \xi \quad(z \in \Omega)
$$

For any $z$ and $z_{0} \in \Omega$, the triangle with vertices at $a, z_{0}$, and $z$ lies in $\Omega$; hence $F(z)-F\left(z_{0}\right)$ is the integral of $f$ over $\left[z_{0}, z\right]$, by Theorem 10.13. Fixing $z_{0}$, we thus obtain

$$
\frac{F(z)-F\left(z_{0}\right)}{z-z_{0}}-f\left(z_{0}\right)=\frac{1}{z-z_{0}} \int_{\left[z_{0}, z\right]}\left[f(\xi)-f\left(z_{0}\right)\right] d \xi
$$

if $z \neq z_{0}$. Given $\epsilon>0$, the continuity of $f$ at $z_{0}$ shows that there is a $\delta>0$ such that $\left|f(\xi)-f\left(z_{0}\right)\right|<\epsilon$ if $\left|\xi-z_{0}\right|<\delta$; hence the absolute value of the left side of (3) is less than $\epsilon$ as soon as $\left|z-z_{0}\right|<\delta$. This proves that $f=F^{\prime}$. In particular, $F \in H(\Omega)$. Now (1) follows from Theorem 10.12.

10.15 Cauchy's Formula in a Convex Set Suppose $\gamma$ is a closed path in a convex open set $\Omega$, and $f \in H(\Omega)$. If $z \in \Omega$ and $z \notin \gamma^{*}$, then

$$
f(z) \cdot \operatorname{Ind}_{\gamma}(z)=\frac{1}{2 \pi i} \int_{\nu} \frac{f(\xi)}{\xi-z} d \xi
$$

The case of greatest interest is, of course, $\operatorname{Ind}_{\nu}(z)=1$.

Proof Fix $z$ so that the above conditions hold, and define

$$
g(\xi)= \begin{cases}\frac{f(\xi)-f(z)}{\xi-z} & \text { if } \xi \in \Omega, \xi \neq z \\ f^{\prime}(z) & \text { if } \xi=z\end{cases}
$$

Then $g$ satisfies the hypotheses of Theorem 10.14. Hence

$$
\frac{1}{2 \pi i} \int_{\gamma} g(\xi) d \xi=0
$$

If we substitute (2) into (3) we obtain (1).

The theorem concerning the representability of holomorphic functions by power series is an easy consequence of Theorem 10.15, if we take a circle for $\gamma$ :

10.16 Theorem For every open set $\Omega$ in the plane, every $f \in H(\Omega)$ is representable by power series in $\Omega$.

Proof Suppose $f \in H(\Omega)$ and $D(a ; R) \subset \Omega$. If $\gamma$ is a positively oriented circle with center at $a$ and radius $r<R$, the convexity of $D(a ; R)$ allows us to apply Theorem 10.15; by Theorem 10.11, we obtain

$$
f(z)=\frac{1}{2 \pi i} \int_{\gamma} \frac{f(\xi)}{\xi-z} d \xi \quad(z \in D(a ; r))
$$

But now we can apply Theorem 10.7, with $X=[0,2 \pi], \varphi=\gamma$, and $d \mu(t)=f(\gamma(t)) \gamma^{\prime}(t) d t$, and we conclude that there is a sequence $\left\{c_{n}\right\}$ such that

$$
f(z)=\sum_{n=0}^{\infty} c_{n}(z-a)^{n} \quad(z \in D(a ; r))
$$

The uniqueness of $\left\{c_{n}\right\}$ (see the Corollary to Theorem 10.6) shows that the same power series is obtained for every $r<R$ (as long as $a$ is fixed). Hence the representation (2) is valid for every $z \in D(a ; R)$, and the proof is complete.

Corollary If $f \in H(\Omega)$, then $f^{\prime} \in H(\Omega)$.

ProOF Combine Theorems 10.6 and 10.16.

The Cauchy theorem has a useful converse:

10.17 Morera's Theorem Suppose $f$ is a continuous complex function in an open set $\Omega$ such that

$$
\int_{\partial \Delta} f(z) d z=0
$$

for every closed triangle $\Delta \subset \Omega$. Then $f \in H(\Omega)$.

ProOf Let $V$ be a convex open set in $\Omega$. As in the proof of Theorem 10.14, we can construct $F \in H(V)$ such that $F^{\prime}=f$. Since derivatives of holomorphic functions are holomorphic (Theorem 10.16), we have $f \in H(V)$, for every convex open $V \subset \Omega$, hence $f \in H(\Omega)$.

## The Power Series Representation

The fact that every holomorphic function is locally the sum of a convergent power series has a large number of interesting consequences. A few of these are developed in this section.

10.18 Theorem Suppose $\Omega$ is a region, $f \in H(\Omega)$, and

$$
Z(f)=\{a \in \Omega: f(a)=0\}
$$

Then either $Z(f)=\Omega$, or $Z(f)$ has no limit point in $\Omega$. In the latter case there corresponds to each $a \in Z(f) a$ unique positive integer $m=m(a)$ such that

$$
f(z)=(z-a)^{m} g(z) \quad(z \in \Omega)
$$

where $g \in H(\Omega)$ and $g(a) \neq 0$; furthermore, $Z(f)$ is at most countable.

(We recall that regions are connected open sets.)

The integer $m$ is called the order of the zero which $f$ has at the point $a$. Clearly, $Z(f)=\Omega$ if and only if $f$ is identically 0 in $\Omega$. We call $Z(f)$ the zero set of $f$. Analogous results hold of course for the set of $\alpha$-points of $f$, i.e., the zero set of $f-\alpha$, where $\alpha$ is any complex number.

Proof Let $A$ be the set of all limit points of $Z(f)$ in $\Omega$. Since $f$ is continuous, $A \subset Z(f)$.

Fix $a \in Z(f)$, and choose $r>0$ so that $D(a ; r) \subset \Omega$. By Theorem 10.16,

$$
f(z)=\sum_{n=0}^{\infty} c_{n}(z-a)^{n} \quad(z \in D(a ; r))
$$

There are now two possibilities. Either all $c_{n}$ are 0 , in which case $D(a ; r) \subset A$ and $a$ is an interior point of $A$, or there is a smallest integer $m$ [necessarily positive, since $f(a)=0]$ such that $c_{m} \neq 0$. In that case, define

$$
g(z)= \begin{cases}(z-a)^{-m} f(z) & (z \in \Omega-\{a\}) \\ c_{m} & (z=a)\end{cases}
$$

Then (2) holds. It is clear that $g \in H(\Omega-\{a\})$. But (3) implies

$$
g(z)=\sum_{k=0}^{\infty} c_{m+k}(z-a)^{k} \quad(z \in D(a ; r))
$$

Hence $g \in H(D(a ; r))$, so actually $g \in H(\Omega)$.

Moreover, $g(a) \neq 0$, and the continuity of $g$ shows that there is a neighborhood of $a$ in which $g$ has no zero. Thus $a$ is an isolated point of $Z(f)$, by (2).

If $a \in A$, the first case must therefore occur. So $A$ is open. If $B=\Omega-A$, it is clear from the definition of $A$ as a set of limit points that $B$ is open. Thus $\Omega$ is the union of the disjoint open sets $A$ and $B$. Since $\Omega$ is connected, we have either $A=\Omega$, in which case $Z(f)=\Omega$, or $A=\varnothing$. In the latter case, $Z(f)$ has at most finitely many points in each compact subset of $\Omega$, and since $\Omega$ is $\sigma$-compact, $Z(f)$ is at most countable.

Corollary If $f$ and $g$ are holomorphic functions in a region $\Omega$ and if $f(z)=g(z)$ for all $z$ in some set which has a limit point in $\Omega$, then $f(z)=g(z)$ for all $z \in \Omega$.

In other words, a holomorphic function in a region $\Omega$ is determined by its values on any set which has a limit point in $\Omega$. This is an important uniqueness theorem.

Note: The theorem fails if we drop the assumption that $\Omega$ is connected: If $\Omega=\Omega_{0} \cup \Omega_{1}$, and $\Omega_{0}$ and $\Omega_{1}$ are disjoint open sets, put $f=0$ in $\Omega_{0}$ and $f=1$ in $\Omega_{1}$.

10.19 Definition If $a \in \Omega$ and $f \in H(\Omega-\{a\})$, then $f$ is said to have an isolated singularity at the point $a$. If $f$ can be so defined at $a$ that the extended function is holomorphic in $\Omega$, the singularity is said to be removable.

10.20 Theorem Suppose $f \in H(\Omega-\{a\})$ and $f$ is bounded in $D^{\prime}(a ; r)$, for some $r>0$. Then $f$ has a removable singularity at a.

Recall that $D^{\prime}(a ; r)=\{z: 0<|z-a|<r\}$.

Proof Define $h(a)=0$, and $h(z)=(z-a)^{2} f(z)$ in $\Omega-\{a\}$. Our boundedness assumption shows that $h^{\prime}(a)=0$. Since $h$ is evidently differentiable at every other point of $\Omega$, we have $h \in H(\Omega)$, so

$$
h(z)=\sum_{n=2}^{\infty} c_{n}(z-a)^{n} \quad(z \in D(a ; r))
$$

We obtain the desired holomorphic extension of $f$ by setting $f(a)=c_{2}$, for then

$$
f(z)=\sum_{n=0}^{\infty} c_{n+2}(z-a)^{n} \quad(z \in D(a ; r))
$$

10.21 Theorem If $a \in \Omega$ and $f \in H(\Omega-\{a\})$, then one of the following three cases must occur:

(a) f has a removable singularity at a.

(b) There are complex numbers $c_{1}, \ldots, c_{m}$, where $m$ is a positive integer and $c_{m} \neq 0$, such that

$$
f(z)-\sum_{k=1}^{m} \frac{c_{k}}{(z-a)^{k}}
$$

has a removable singularity at a.

(c) If $r>0$ and $D(a ; r) \subset \Omega$, then $f\left(D^{\prime}(a ; r)\right)$ is dense in the plane.

In case $(b), f$ is said to have a pole of order $m$ at $a$. The function

$$
\sum_{k=1}^{m} c_{k}(z-a)^{-k}
$$

a polynomial in $(z-a)^{-1}$, is called the principal part of $f$ at $a$. It is clear in this situation that $|f(z)| \rightarrow \infty$ as $z \rightarrow a$.

In case $(c), f$ is said to have an essential singularity at $a$. A statement equivalent to $(c)$ is that to each complex number $w$ there corresponds a sequence $\left\{z_{n}\right\}$ such that $z_{n} \rightarrow a$ and $f\left(z_{n}\right) \rightarrow w$ as $n \rightarrow \infty$.

Proof Suppose (c) fails. Then there exist $r>0, \delta>0$, and a complex number $w$ such that $|f(z)-w|>\delta$ in $D^{\prime}(a ; r)$. Let us write $D$ for $D(a ; r)$ and $D^{\prime}$ for $D^{\prime}(a ; r)$. Define

$$
g(z)=\frac{1}{f(z)-w} \quad\left(z \in D^{\prime}\right)
$$

Then $g \in H\left(D^{\prime}\right)$ and $|g|<1 / \delta$. By Theorem 10.20, $g$ extends to a holomorphic function in $D$.

If $g(a) \neq 0,(1)$ shows that $f$ is bounded in $D^{\prime}(a ; \rho)$ for some $\rho>0$. Hence (a) holds, by Theorem 10.20 .

If $g$ has a zero of order $m \geq 1$ at $a$, Theorem 10.18 shows that

$$
g(z)=(z-a)^{m} g_{1}(z) \quad(z \in D)
$$

where $g_{1} \in H(D)$ and $g_{1}(a) \neq 0$. Also, $g_{1}$ has no zero in $D^{\prime}$, by (1). Put $h=$ $1 / g_{1}$ in $D$. Then $h \in H(D), h$ has no zero in $D$, and

$$
f(z)-w=(z-a)^{-m} h(z) \quad\left(z \in D^{\prime}\right)
$$

But $h$ has an expansion of the form

$$
h(z)=\sum_{n=0}^{\infty} b_{n}(z-a)^{n} \quad(z \in D)
$$

with $b_{0} \neq 0$. Now (3) shows that (b) holds, with $c_{k}=b_{m-k}, k=1, \ldots, m$.

This completes the proof.

We shall now exploit the fact that the restriction of a power series $\sum c_{n}(z-a)^{n}$ to a circle with center at $a$ is a trigonometric series.

10.22 Theorem If

$$
f(z)=\sum_{n=0}^{\infty} c_{n}(z-a)^{n} \quad(z \in D(a ; R))
$$

and if $0<r<R$, then

$$
\sum_{n=0}^{\infty}\left|c_{n}\right|^{2} r^{2 n}=\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|f\left(a+r e^{i \theta}\right)\right|^{2} d \theta
$$

Proof We have

$$
f\left(a+r e^{i \theta}\right)=\sum_{n=0}^{\infty} c_{n} r^{n} e^{i n \theta}
$$

For $r<R$, the series (3) converges uniformly on $[-\pi, \pi]$. Hence

$$
c_{n} r^{n}=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f\left(a+r e^{i \theta}\right) e^{-i n \theta} d \theta \quad(n=0,1,2, \ldots)
$$

and (2) is seen to be a special case of Parseval's formula.

Here are some consequences:

10.23 Liouville's Theorem Every bounded entire function is constant.

Recall that a function is entire if it is holomorphic in the whole plane.

Proof Suppose $f$ is entire, $|f(z)|<M$ for all $z$, and $f(z)=\sum c_{n} z^{n}$ for all $z$. By Theorem 10.22,

$$
\sum_{n=0}^{\infty}\left|c_{n}\right|^{2} r^{2 n}<M^{2}
$$

for all $r$, which is possible only if $c_{n}=0$ for all $n \geq 1$.

10.24 The Maximum Modulus Theorem Suppose $\Omega$ is a region, $f \in H(\Omega)$, and $\bar{D}(a ; r) \subset \Omega$. Then

$$
|f(a)| \leq \max _{\theta}\left|f\left(a+r e^{i \theta}\right)\right| .
$$

Equality occurs in (1) if and only if $f$ is constant in $\Omega$. stant.

Consequently, $|f|$ has no local maximum at any point of $\Omega$, unless $f$ is con-

Proof Assume that $\left|f\left(a+r e^{i \theta}\right)\right| \leq|f(a)|$ for all real $\theta$. In the notation of Theorem 10.22 it follows then that

$$
\sum_{n=0}^{\infty}\left|c_{n}\right|^{2} r^{2 n} \leq|f(a)|^{2}=\left|c_{0}\right|^{2}
$$

Hence $c_{1}=c_{2}=c_{3}=\cdots=0$, which implies that $f(z)=f(a)$ in $D(a ; r)$. Since $\Omega$ is connected, Theorem 10.18 shows that $f$ is constant in $\Omega$.

Corollary Under the same hypotheses,

$$
|f(a)| \geq \min _{\theta}\left|f\left(a+r e^{i \theta}\right)\right|
$$

if $f$ has no zero in $D(a ; r)$.

ProOF If $f\left(a+r e^{i \theta}\right)=0$ for some $\theta$ then (2) is obvious. In the other case, there is a region $\Omega_{0}$ that contains $\bar{D}(a ; r)$ and in which $f$ has no zero; hence (1) can be applied to $1 / f$, and (2) follows.

10.25 Theorem If $n$ is a positive integer and

$$
P(z)=z^{n}+a_{n-1} z^{n-1}+\cdots+a_{1} z+a_{0},
$$

where $a_{0}, \ldots, a_{n-1}$ are complex numbers, then $P$ has precisely $n$ zeros in the plane.

Of course, these zeros are counted according to their multiplicities: A zero of order $m$, say, is counted as $m$ zeros. This theorem contains the fact that the complex field is algebraically closed, i.e., that every nonconstant polynomial with complex coefficients has at least one complex zero.

Proof Choose $r>1+2\left|a_{0}\right|+\left|a_{1}\right|+\cdots+\left|a_{n-1}\right|$. Then

$$
\left|P\left(r e^{i \theta}\right)\right|>|P(0)| \quad(0 \leq \theta \leq 2 \pi) .
$$

If $P$ had no zeros, then the function $f=1 / P$ would be entire and would satisfy $|f(0)|>\left|f\left(r e^{i \theta}\right)\right|$ for all $\theta$, which contradicts the maximum modulus theorem. Thus $P\left(z_{1}\right)=0$ for some $z_{1}$. Consequently, there is a polynomial $Q$, of degree $n-1$, such that $P(z)=\left(z-z_{1}\right) Q(z)$. The proof is completed by induction on $n$.

10.26 Theorem (Cauchy's Estimates) If $f \in H(D(a ; R))$ and $|f(z)| \leq M$ for all $z \in D(a ; R)$, then

$$
\left|f^{(n)}(a)\right| \leq \frac{n ! M}{R^{n}} \quad(n=1,2,3, \ldots)
$$

PrOOF For each $r<R$, each term of the series 10.22(2) is bounded above by $M^{2}$.

If we take $a=0, R=1$, and $f(z)=z^{n}$, then $M=1, f^{(n)}(0)=n !$, and we see that (1) cannot be improved.

10.27 Definition A sequence $\left\{f_{j}\right\}$ of functions in $\Omega$ is said to converge to $f$ uniformly on compact subsets of $\Omega$ if to every compact $K \subset \Omega$ and to every $\epsilon>0$ there corresponds an $N=N(K, \epsilon)$ such that $\left|f_{j}(z)-f(z)\right|<\epsilon$ for all $z \in K$ if $j>N$.

For instance, the sequence $\left\{z^{n}\right\}$ converges to 0 uniformly on compact subsets of $D(0 ; 1)$, but the convergence is not uniform in $D(0 ; 1)$.

It is uniform convergence on compact subsets which arises most naturally in connection with limit operations on holomorphic functions. The term "almost uniform convergence" is sometimes used for this concept.

10.28 Theorem Suppose $f_{j} \in H(\Omega)$, for $j=1,2,3, \ldots$, and $f_{j} \rightarrow f$ uniformly on compact subsets of $\Omega$. Then $f \in H(\Omega)$, and $f_{j}^{\prime} \rightarrow f^{\prime}$ uniformly on compact subsets of $\Omega$.

ProOF Since the convergence is uniform on each compact disc in $\Omega, f$ is continuous. Let $\Delta$ be a triangle in $\Omega$. Then $\Delta$ is compact, so

$$
\int_{\partial \Delta} f(z) d z=\lim _{j \rightarrow \infty} \int_{\partial \Delta} f_{j}(z) d z=0
$$

by Cauchy's theorem. Hence Morera's theorem implies that $f \in H(\Omega)$.

Let $K$ be compact, $K \subset \Omega$. There exists an $r>0$ such that the union $E$ of the closed discs $\bar{D}(z ; r)$, for all $z \in K$, is a compact subset of $\Omega$. Applying Theorem 10.26 to $f-f_{j}$, we have

$$
\left|f^{\prime}(z)-f_{j}^{\prime}(z)\right| \leq r^{-1}\left\|f-f_{j}\right\|_{E} \quad(z \in K)
$$

where $\|f\|_{E}$ denotes the supremum of $|f|$ on $E$. Since $f_{j} \rightarrow f$ uniformly on $E$, it follows that $f_{j}^{\prime} \rightarrow f^{\prime}$ uniformly on $K$.

Corollary Under the same hypothesis, $f_{j}^{(n)} \rightarrow f^{(n)}$ uniformly, as $j \rightarrow \infty$, on every compact set $K \subset \Omega$, and for every positive integer $n$.

Compare this with the situation on the real line, where sequences of infinitely differentiable functions can converge uniformly to nowhere differentiable functions!

## The Open Mapping Theorem

If $\Omega$ is a region and $f \in H(\Omega)$, then $f(\Omega)$ is either a region or a point.

This important property of holomorphic functions will be proved, in more detailed form, in Theorem 10.32.

10.29 Lemma If $f \in H(\Omega)$ and $g$ is defined in $\Omega \times \Omega$ by

$$
g(z, w)= \begin{cases}\frac{f(z)-f(w)}{z-w} & \text { if } w \neq z \\ f^{\prime}(z) & \text { if } w=z\end{cases}
$$

then $g$ is continuous in $\Omega \times \Omega$.

Proof The only points $(z, w) \in \Omega \times \Omega$ at which the continuity of $g$ is possibly in doubt have $z=w$.

Fix $a \in \Omega$. Fix $\epsilon>0$. There exists $r>0$ such that $D(a ; r) \subset \Omega$ and $\left|f^{\prime}(\zeta)-f^{\prime}(a)\right|<\epsilon$ for all $\zeta \in D(a ; r)$. If $z$ and $w$ are in $D(a ; r)$ and if

$$
\zeta(t)=(1-t) z+t w
$$

then $\zeta(t) \in D(a ; r)$ for $0 \leq t \leq 1$, and

$$
g(z, w)-g(a, a)=\int_{0}^{1}\left[f^{\prime}(\zeta(t))-f^{\prime}(a)\right] d t
$$

The absolute value of the integrand is $<\epsilon$, for every $t$. Thus $|g(z, w)-g(a, a)|<\epsilon$. This proves that $g$ is continuous at $(a, a)$.

10.30 Theorem Suppose $\varphi \in H(\Omega), z_{0} \in \Omega$, and $\varphi^{\prime}\left(z_{0}\right) \neq 0$. Then $\Omega$ contains a neighborhood $V$ of $z_{0}$ such that

(a) $\varphi$ is one-to-one in $V$,

(b) $W=\varphi(V)$ is an open set, and

(c) if $\psi: W \rightarrow V$ is defined by $\psi(\varphi(z))=z$, then $\psi \in H(W)$.

Thus $\varphi: V \rightarrow W$ has a holomorphic inverse.

Proof Lemma 10.29, applied to $\varphi$ in place of $f$, shows that $\Omega$ contains a neighborhood $V$ of $z_{0}$ such that

$$
\left|\varphi\left(z_{1}\right)-\varphi\left(z_{2}\right)\right| \geq \frac{1}{2}\left|\varphi^{\prime}\left(z_{0}\right)\right|\left|z_{1}-z_{2}\right|
$$

if $z_{1} \in V$ and $z_{2} \in V$. Thus $(a)$ holds, and also

$$
\varphi^{\prime}(z) \neq 0 \quad(z \in V) .
$$

To prove $(b)$, pick $a \in V$ and choose $r>0$ so that $\bar{D}(a, r) \subset V$. By (1) there exists $c>0$ such that

$$
\left|\varphi\left(a+r e^{i \theta}\right)-\varphi(a)\right|>2 c \quad(-\pi \leq \theta \leq \pi)
$$

If $\lambda \in D(\varphi(a) ; c)$, then $|\lambda-\varphi(a)|<c$, hence (3) implies

$$
\min _{\theta}\left|\lambda-\varphi\left(a+r e^{i \theta}\right)\right|>c .
$$

By the corollary to Theorem 10.24, $\lambda-\varphi$ must therefore have a zero in $D(a ; r)$. Thus $\lambda=\varphi(z)$ for some $z \in D(a ; r) \subset V$.

This proves that $D(\varphi(a) ; c) \subset \varphi(V)$. Since $a$ was an arbitrary point of $V$, $\varphi(V)$ is open.

To prove (c), fix $w_{1} \in W$. Then $\varphi\left(z_{1}\right)=w_{1}$ for a unique $z_{1} \in V$. If $w \in W$ and $\psi(w)=z \in V$, we have

$$
\frac{\psi(w)-\psi\left(w_{1}\right)}{w-w_{1}}=\frac{z-z_{1}}{\varphi(z)-\varphi\left(z_{1}\right)}
$$

By (1), $z \rightarrow z_{1}$ when $w \rightarrow w_{1}$. Hence (2) implies that $\psi^{\prime}\left(w_{1}\right)=1 / \varphi^{\prime}\left(z_{1}\right)$. Thus $\psi \in H(W)$.

10.31 Definition For $m=1,2,3, \ldots$, we denote the " $m^{\text {th }}$ power function" $z \rightarrow z^{m}$ by $\pi_{m}$.

Each $w \neq 0$ is $\pi_{m}(z)$ for precisely $m$ distinct values of $z$ : If $w=r e^{i \theta}, r>0$, then $\pi_{m}(z)=w$ if and only if $z=r^{1 / m} e^{i(\theta+2 k \pi) / m}, k=1, \ldots, m$.

Note also that each $\pi_{m}$ is an open mapping: If $V$ is open and does not contain 0 , then $\pi_{m}(V)$ is open by Theorem 10.30 . On the other hand, $\pi_{m}(D(0 ; r))=D\left(0 ; r^{m}\right)$.

Compositions of open mappings are clearly open. In particular, $\pi_{m} \circ \varphi$ is open, by Theorem 10.30, if $\varphi^{\prime}$ has no zero. The following theorem (which contains the more detailed version of the open mapping theorem that was mentioned prior to Lemma 10.29) states a converse: Every nonconstant holomorphic function in a region is locally of the form $\pi_{m} \circ \varphi$, except for an additive constant.

10.32 Theorem Suppose $\Omega$ is a region, $f \in H(\Omega), f$ is not constant, $z_{0} \in \Omega$, and $w_{0}=f\left(z_{0}\right)$. Let $m$ be the order of the zero which the function $f-w_{0}$ has at $z_{0}$.

Then there exists a neighborhood $V$ of $z_{0}, V \subset \Omega$, and there exists $\varphi \in H(V)$, such that

(a) $f(z)=w_{0}+[\varphi(z)]^{m}$ for all $z \in V$,

(b) $\varphi^{\prime}$ has no zero in $V$ and $\varphi$ is an invertible mapping of $V$ onto a disc $D(0 ; r)$.

Thus $f-w_{0}=\pi_{m} \circ \varphi$ in $V$. It follows that $f$ is an exactly $m$-to-1 mapping of $V-\left\{z_{0}\right\}$ onto $D^{\prime}\left(w_{0} ; r^{m}\right)$, and that each $w_{0} \in f(\Omega)$ is an interior point of $f(\Omega)$. Hence $f(\Omega)$ is open.

Proof Without loss of generality we may assume that $\Omega$ is a convex neighborhood of $z_{0}$ which is so small that $f(z) \neq w_{0}$ if $z \in \Omega-\left\{z_{0}\right\}$. Then

$$
f(z)-w_{0}=\left(z-z_{0}\right)^{m} g(z) \quad(z \in \Omega)
$$

for some $g \in H(\Omega)$ which has no zero in $\Omega$. Hence $g^{\prime} / g \in H(\Omega)$. By Theorem $10.14, g^{\prime} / g=h^{\prime}$ for some $h \in H(\Omega)$. The derivative of $g \cdot \exp (-h)$ is 0 in $\Omega$. If $h$ is modified by the addition of a suitable constant, it follows that $g=\exp (h)$. Define

$$
\varphi(z)=\left(z-z_{0}\right) \exp \frac{h(z)}{m} \quad(z \in \Omega)
$$

Then $(a)$ holds, for all $z \in \Omega$.

Also, $\varphi\left(z_{0}\right)=0$ and $\varphi^{\prime}\left(z_{0}\right) \neq 0$. The existence of an open set $V$ that satisfies $(b)$ follows now from Theorem 10.30. This completes the proof.

The next theorem is really contained in the preceding results, but it seems advisable to state it explicitly.

10.33 Theorem Suppose $\Omega$ is a region, $f \in H(\Omega)$, and $f$ is one-to-one in $\Omega$. Then $f^{\prime}(z) \neq 0$ for every $z \in \Omega$, and the inverse of $f$ is holomorphic.

Proof If $f^{\prime}\left(z_{0}\right)$ were 0 for some $z_{0} \in \Omega$, the hypotheses of Theorem 10.32 would hold with some $m>1$, so that $f$ would be $m$-to-1 in some deleted neighborhood of $z_{0}$. Now apply part (c) of Theorem 10.30.

Note that the converse of Theorem 10.33 is false: If $f(z)=e^{z}$, then $f^{\prime}(z) \neq 0$ for every $z$, but $f$ is not one-to-one in the whole complex plane.

## The Global Cauchy Theorem

Before we state and prove this theorem, which will remove the restriction to convex regions that was imposed in Theorem 10.14, it will be convenient to add a little to the integration apparatus which was sufficient up to now. Essentially, it is a matter of no longer restricting ourselves to integrals over single paths, but to consider finite "sums" of paths instead. A simple instance of this occurred already in Sec. 10.9(c).

10.34 Chains and Cycles Suppose $\gamma_{1}, \ldots, \gamma_{n}$ are paths in the plane, and put $K=$ $\gamma_{1}^{*} \cup \cdots \cup \gamma_{n}^{*}$. Each $\gamma_{i}$ induces a linear functional $\tilde{\gamma}_{i}$ on the vector space $C(K)$, by the formula

$$
\tilde{\gamma}_{i}(f)=\int_{\gamma_{i}} f(z) d z
$$

Define

$$
\tilde{\Gamma}=\tilde{\gamma}_{1}+\cdots+\tilde{\gamma}_{n} .
$$

Explicitly, $\tilde{\Gamma}(f)=\tilde{\gamma}_{1}(f)+\cdots+\tilde{\gamma}_{n}(f)$ for all $f \in C(K)$. The relation (2) suggests that we introduce a "formal sum"

$$
\Gamma=\gamma_{1} \dot{+} \cdots \dot{+} \gamma_{n}
$$

and define

$$
\int_{\Gamma} f(z) d z=\tilde{\Gamma}(f)
$$

Then (3) is merely an abbreviation for the statement

$$
\int_{\Gamma} f(z) d z=\sum_{i=1}^{n} \int_{\gamma_{i}} f(z) d z \quad(f \in C(K)) .
$$

Note that (5) serves as the definition of its left side.

The objects $\Gamma$ so defined are called chains. If each $\gamma_{j}$ in (3) is a closed path, then $\Gamma$ is called a cycle. If each $\gamma_{j}$ in (3) is a path in some open set $\Omega$, we say that $\Gamma$ is a chain in $\Omega$.

If (3) holds, we define

$$
\Gamma^{*}=\gamma_{1}^{*} \cup \cdots \cup \gamma_{n}^{*}
$$

If $\Gamma$ is a cycle and $\alpha \notin \Gamma^{*}$, we define the index of $\alpha$ with respect to $\Gamma$ by

$$
\operatorname{Ind}_{\Gamma}(\alpha)=\frac{1}{2 \pi i} \int_{\Gamma} \frac{d z}{z-\alpha}
$$

just as in Theorem 10.10. Obviously, (3) implies

$$
\operatorname{Ind}_{\Gamma}(\alpha)=\sum_{i=1}^{n} \operatorname{Ind}_{\gamma_{i}}(\alpha)
$$

If each $\gamma_{i}$ in (3) is replaced by its opposite path (see Sec. 10.8), the resulting chain will be denoted by $-\Gamma$. Then

$$
\int_{-\Gamma} f(z) d z=-\int_{\Gamma} f(z) d z \quad\left(f \in C\left(\Gamma^{*}\right)\right)
$$

In particular, $\operatorname{Ind}_{-\Gamma}(\alpha)=-\operatorname{Ind}_{\Gamma}(\alpha)$ if $\Gamma$ is a cycle and $\alpha \notin \Gamma^{*}$.

Chains can be added and subtracted in the obvious way, by adding or subtracting the corresponding functionals: The statement $\Gamma=\Gamma_{1}+\Gamma_{2}$ means

$$
\int_{\Gamma} f(z) d z=\int_{\Gamma_{1}} f(z) d z+\int_{\Gamma_{2}} f(z) d z
$$

for every $f \in C\left(\Gamma_{1}^{*} \cup \Gamma_{2}^{*}\right)$.

Finally, note that a chain may be represented as a sum of paths in many ways. To say that

$$
\gamma_{1} \dot{+} \cdots \dot{+} \gamma_{n}=\delta_{1} \dot{+} \cdots \dot{+} \delta_{k}
$$

means simply that

$$
\sum_{i} \int_{\gamma_{i}} f(z) d z=\sum_{j} \int_{\delta_{j}} f(z) d z
$$

for every $f$ that is continuous on $\gamma_{1}^{*} \cup \cdots \cup \gamma_{n}^{*} \cup \delta_{1}^{*} \cup \cdots \cup \delta_{k}^{*}$. In particular, a cycle may very well be represented as a sum of paths that are not closed.

10.35 Cauchy's Theorem Suppose $f \in H(\Omega)$, where $\Omega$ is an arbitrary open set in the complex plane. If $\Gamma$ is a cycle in $\Omega$ that satisfies

$$
\operatorname{Ind}_{\Gamma}(\alpha)=0 \quad \text { for every } \alpha \text { not in } \Omega
$$

then

$$
f(z) \cdot \operatorname{Ind}_{\Gamma}(z)=\frac{1}{2 \pi i} \int_{\Gamma} \frac{f(w)}{w-z} d w \quad \text { for } z \in \Omega-\Gamma^{*}
$$

and

$$
\int_{\Gamma} f(z) d z=0
$$

If $\Gamma_{0}$ and $\Gamma_{1}$ are cycles in $\Omega$ such that

$$
\operatorname{Ind}_{\Gamma_{0}}(\alpha)=\operatorname{Ind}_{\Gamma_{1}}(\alpha) \quad \text { for every } \alpha \text { not in } \Omega
$$

then

$$
\int_{\Gamma_{0}} f(z) d z=\int_{\Gamma_{1}} f(z) d z
$$

Proof The function $g$ defined in $\Omega \times \Omega$ by

$$
g(z, w)= \begin{cases}\frac{f(w)-f(z)}{w-z} & \text { if } w \neq z \\ f^{\prime}(z) & \text { if } w=z\end{cases}
$$

is continuous in $\Omega \times \Omega$ (Lemma 10.29). Hence we can define

$$
h(z)=\frac{1}{2 \pi i} \int_{\Gamma} g(z, w) d w \quad(z \in \Omega)
$$

For $z \in \Omega-\Gamma^{*}$, the Cauchy formula (2) is clearly equivalent to the assertion that

$$
h(z)=0 \text {. }
$$

To prove (8), let us first prove that $h \in H(\Omega)$. Note that $g$ is uniformly continuous on every compact subset of $\Omega \times \Omega$. If $z \in \Omega, z_{n} \in \Omega$, and $z_{n} \rightarrow z$, it follows that $g\left(z_{n}, w\right) \rightarrow g(z, w)$ uniformly for $w \in \Gamma^{*}$ (a compact subset of $\Omega$ ). Hence $h\left(z_{n}\right) \rightarrow h(z)$. This proves that $h$ is continuous in $\Omega$. Let $\Delta$ be a closed triangle in $\Omega$. Then

$$
\int_{\partial \Delta} h(z) d z=\frac{1}{2 \pi i} \int_{\Gamma}\left(\int_{\partial \Delta} g(z, w) d z\right) d w
$$

For each $w \in \Omega, z \rightarrow g(z, w)$ is holomorphic in $\Omega$. (The singularity at $z=w$ is removable.) The inner integral on the right side of (9) is therefore 0 for every $w \in \Gamma^{*}$. Morera's theorem shows now that $h \in H(\Omega)$.

Next, we let $\Omega_{1}$ be the set of all complex numbers $z$ for which $\operatorname{Ind}_{\Gamma}(z)=$ 0 , and we define

$$
h_{1}(z)=\frac{1}{2 \pi i} \int_{\Gamma} \frac{f(w)}{w-z} d w \quad\left(z \in \Omega_{1}\right)
$$

If $z \in \Omega \cap \Omega_{1}$, the definition of $\Omega_{1}$ makes it clear that $h_{1}(z)=h(z)$. Hence there is a function $\varphi \in H\left(\Omega \cup \Omega_{1}\right)$ whose restriction to $\Omega$ is $h$ and whose restriction to $\Omega_{1}$ is $h_{1}$.

Our hypothesis (1) shows that $\Omega_{1}$ contains the complement of $\Omega$. Thus $\varphi$ is an entire function. $\Omega_{1}$ also contains the unbounded component of the complement of $\Gamma^{*}$, since $\operatorname{Ind}_{\Gamma}(z)$ is 0 there. Hence

$$
\lim _{|z| \rightarrow \infty} \varphi(z)=\lim _{|z| \rightarrow \infty} h_{1}(z)=0
$$

Liouville's theorem implies now that $\varphi(z)=0$ for every $z$. This proves (8), and hence (2).

To deduce (3) from (2), pick $a \in \Omega-\Gamma^{*}$ and define $F(z)=(z-a) f(z)$. Then

$$
\frac{1}{2 \pi i} \int_{\Gamma} f(z) d z=\frac{1}{2 \pi i} \int_{\Gamma} \frac{F(z)}{z-a} d z=F(a) \cdot \operatorname{Ind}_{\Gamma}(a)=0
$$

because $F(a)=0$.

Finally, (5) follows from (4) if (3) is applied to the cycle $\Gamma=\Gamma_{1}-\Gamma_{0}$. This completes the proof.

### 10.36 Remarks

(a) If $\gamma$ is a closed path in a convex region $\Omega$ and if $\alpha \notin \Omega$, an application of Theorem 10.14 to $f(z)=(z-\alpha)^{-1}$ shows that $\operatorname{Ind}_{\nu}(\alpha)=0$. Hypothesis (1) of Theorem 10.35 is therefore satisfied by every cycle in $\Omega$ if $\Omega$ is convex. This shows that Theorem 10.35 generalizes Theorems 10.14 and 10.15 .

(b) The last part of Theorem 10.35 shows under what circumstances integration over one cycle can be replaced by integration over another, without changing the value of the integral. For example, let $\Omega$ be the plane with three disjoint closed discs $D_{i}$ removed. If $\Gamma, \gamma_{1}, \gamma_{2}, \gamma_{3}$ are positively oriented circles in $\Omega$ such that $\Gamma$ surrounds $D_{1} \cup D_{2} \cup D_{3}$ and $\gamma_{i}$ surrounds $D_{i}$ but not $D_{j}$ for $j \neq i$, then

$$
\int_{\Gamma} f(z) d z=\sum_{i=1}^{3} \int_{\gamma_{i}} f(z) d z
$$

for every $f \in H(\Omega)$.

(c) In order to apply Theorem 10.35, it is desirable to have a reasonably efficient method of finding the index of a point with respect to a closed path. The following theorem does this for all paths that occur in practice.

It says, essentially, that the index increases by 1 when the path is crossed "from right to left." If we recall that $\operatorname{Ind}_{\gamma}(\alpha)=0$ if $\alpha$ is in the unbounded component of the complement $W$ of $\gamma^{*}$, we can then successively determine $\operatorname{Ind}_{\nu}(\alpha)$ in the other components of $W$, provided that $W$ has only finitely many components and that $\gamma$ traverses no arc more than once.

10.37 Theorem Suppose $\gamma$ is a closed path in the plane, with parameter interval $[\alpha, \beta]$. Suppose $\alpha<u<v<\beta$, $a$ and $b$ are complex numbers, $|b|=r>0$, and

(i) $\gamma(u)=a-b, \gamma(v)=a+b$,

(ii) $|\gamma(s)-a|<r$ if and only if $u<s<v$,

(iii) $|\gamma(s)-a|=r$ if and only if $s=u$ or $s=v$.

Assume furthermore that $D(a ; r)-\gamma^{*}$ is the union of two regions, $D_{+}$and $D_{-}$, labeled so that $a+b i \in \bar{D}_{+}$and $a-b i \in \bar{D}_{-}$. Then

$$
\operatorname{Ind}_{\gamma}(z)=1+\operatorname{Ind}_{\gamma}(w)
$$

if $x \in D_{+}$and $w \in D_{-}$.

As $\gamma(t)$ traverses $D(a ; r)$ from $a-b$ to $a+b, D_{-}$is "on the right" and $D_{+}$is "on the left" of the path.

Proof To simplify the writing, reparametrize $\gamma$ so that $u=0$ and $v=\pi$. Define

$$
\begin{aligned}
C(s) & =a-b e^{i s} \\
f(s) & = \begin{cases}C(s) & (0 \leq s \leq 2 \pi) \\
\gamma(2 \pi-s) & (0 \leq s \leq \pi)\end{cases} \\
g(s) & = \begin{cases}\gamma(s) & (0 \leq s \leq 2 \pi) \\
C(s) & (\pi \leq s \leq 2 \pi)\end{cases} \\
h(s) & = \begin{cases}\gamma(s) & (\alpha \leq s \leq 0 \text { or } \pi \leq s \leq \beta) \\
C(s) & (0 \leq s \leq \pi) .\end{cases}
\end{aligned}
$$

Since $\gamma(0)=C(0)$ and $\gamma(\pi)=C(\pi), f, g$, and $h$ are closed paths.

If $E \subset \bar{D}(a ; r),|\zeta-a|=r$, and $\zeta \notin E$, then $E$ lies in the disc $D(2 a-\zeta ; 2 r)$ which does not contain $\zeta$. Apply this to $E=g^{*}, \zeta=a-b i$, to see [from Remark $10.36(a)]$ that $\operatorname{Ind}_{g}(a-b i)=0$. Since $\bar{D}_{-}$is connected and $D_{-}$does not intersect $g^{*}$, it follows that

$$
\operatorname{Ind}_{g}(w)=0 \quad \text { if } w \in D_{-} .
$$

The same reasoning shows that

$$
\operatorname{Ind}_{f}(z)=0 \quad \text { if } z \in D_{+} .
$$

We conclude that

$$
\begin{aligned}
\operatorname{Ind}_{\gamma}(z) & =\operatorname{Ind}_{h}(z)=\operatorname{Ind}_{h}(w) \\
& =\operatorname{Ind}_{C}(w)+\operatorname{Ind}_{\gamma}(w)=1+\operatorname{Ind}_{\gamma}(w)
\end{aligned}
$$

The first of these equalities follows from (2), since $h=\gamma \dot{+} f$. The second holds because $z$ and $w$ lie in $D(a ; r)$, a connected set which does not intersect $h^{*}$. The third follows from (1), since $h \dot{+} g=C \dot{+} \gamma$, and the fourth is a consequence of Theorem 10.11. This completes the proof.

We now turn to a brief discussion of another topological concept that is relevant to Cauchy's theorem.

10.38 Homotopy Suppose $\gamma_{0}$ and $\gamma_{1}$ are closed curves in a topological space $X$, both with parameter interval $I=[0,1]$. We say that $\gamma_{0}$ and $\gamma_{1}$ are $X$-homotopic if there is a continuous mapping $H$ of the unit square $I^{2}=I \times I$ into $X$ such that

$$
H(s, 0)=\gamma_{0}(s), \quad H(s, 1)=\gamma_{1}(s), \quad H(0, t)=H(1, t)
$$

for all $s \in I$ and $t \in I$. Put $\gamma_{t}(s)=H(s, t)$. Then (1) defines a one-parameter family of closed curves $\gamma_{t}$ in $X$, which connects $\gamma_{0}$ and $\gamma_{1}$. Intuitively, this means that $\gamma_{0}$ can be continuously deformed to $\gamma_{1}$, within $X$.

If $\gamma_{0}$ is $X$-homotopic to a constant mapping $\gamma_{1}$ (i.e., if $\gamma_{1}^{*}$ consists of just one point), we say that $\gamma_{0}$ is null-homotopic in $X$. If $X$ is connected and if every closed curve in $X$ is null-homotopic, $X$ is said to be simply connected.

For example, every convex region $\Omega$ is simply connected. To see this, let $\gamma_{0}$ be a closed curve in $\Omega$, fix $z_{1} \in \Omega$, and define

$$
H(s, t)=(1-t) \gamma_{0}(s)+t z_{1} \quad(0 \leq s \leq 1, \quad 0 \leq t \leq 1) .
$$

Theorem 10.40 will show that condition (4) of Cauchy's theorem 10.35 holds whenever $\Gamma_{0}$ and $\Gamma_{1}$ are $\Omega$-homotopic closed paths. As a special case of this, note that condition (1) of Theorem 10.35 holds for every closed path $\Gamma$ in $\Omega$ if $\Omega$ is simply connected.

10.39 Lemma If $\gamma_{0}$ and $\gamma_{1}$ are closed paths with parameter interval $[0,1]$, if $\alpha$ is a complex number, and if

$$
\left|\gamma_{1}(s)-\gamma_{0}(s)\right|<\left|\alpha-\gamma_{0}(s)\right| \quad(0 \leq s \leq 1)
$$

then $\operatorname{Ind}_{\gamma_{1}}(\alpha)=\operatorname{Ind}_{\gamma_{0}}(\alpha)$.

Proof Note first that (1) implies that $\alpha \notin \gamma_{0}^{*}$ and $\alpha \notin \gamma_{1}^{*}$. Hence one can define $\gamma=\left(\gamma_{1}-\alpha\right) /\left(\gamma_{0}-\alpha\right)$. Then

$$
\frac{\gamma^{\prime}}{\gamma}=\frac{\gamma_{1}^{\prime}}{\gamma_{1}-\alpha}-\frac{\gamma_{0}^{\prime}}{\gamma_{0}-\alpha}
$$

and $|1-\gamma|<1$, by (1). Hence $\gamma^{*} \subset D(1 ; 1)$, which implies that $\operatorname{Ind}_{\gamma}(0)=0$. Integration of (2) over $[0,1]$ now gives the desired result.

10.40 Theorem If $\Gamma_{0}$ and $\Gamma_{1}$ are $\Omega$-homotopic closed paths in a region $\Omega$, and if $\alpha \notin \Omega$, then

$$
\operatorname{Ind}_{\Gamma_{1}}(\alpha)=\operatorname{Ind}_{\Gamma_{0}}(\alpha)
$$

Proof By definition, there is a continuous $H: I^{2} \rightarrow \Omega$ such that

$$
H(s, 0)=\Gamma_{0}(s), \quad H(s, 1)=\Gamma_{1}(s), \quad H(0, t)=H(1, t)
$$

Since $I^{2}$ is compact, so is $H\left(I^{2}\right)$. Hence there exists $\epsilon>0$ such that

$$
|\alpha-H(s, t)|>2 \epsilon \quad \text { if } \quad(s, t) \in I^{2} .
$$

Since $H$ is uniformly continuous, there is a positive integer $n$ such that

$$
\left|H(s, t)-H\left(s^{\prime}, t^{\prime}\right)\right|<\epsilon \quad \text { if } \quad\left|s-s^{\prime}\right|+\left|t-t^{\prime}\right| \leq 1 / n \text {. }
$$

Define polygonal closed paths $\gamma_{0}, \ldots, \gamma_{n}$ by

$$
\gamma_{k}(s)=H\left(\frac{i}{n}, \frac{k}{n}\right)(n s+1-i)+H\left(\frac{i-1}{n}, \frac{k}{n}\right)(i-n s)
$$

if $i-1 \leq n s \leq i$ and $i=1, \ldots, n$. By (4) and (5),

$$
\left|\gamma_{k}(s)-H(s, k / n)\right|<\epsilon \quad(k=0, \ldots, n ; 0 \leq s \leq 1)
$$

In particular, taking $k=0$ and $k=n$,

$$
\left|\gamma_{0}(s)-\Gamma_{0}(s)\right|<\epsilon, \quad\left|\gamma_{n}(s)-\Gamma_{1}(s)\right|<\epsilon .
$$

By (6) and (3),

$$
\left|\alpha-\gamma_{k}(s)\right|>\epsilon \quad(k=0, \ldots, n ; 0 \leq s \leq 1)
$$

On the other hand, (4) and (5) also give

$$
\left|\gamma_{k-1}(s)-\gamma_{k}(s)\right|<\epsilon \quad(k=1, \ldots, n ; 0 \leq s \leq 1)
$$

Now it follows from (7), (8), (9), and $n+2$ applications of Lemma 10.39 that $\alpha$ has the same index with respect to each of the paths $\Gamma_{0}, \gamma_{0}, \gamma_{1}, \ldots, \gamma_{n}$, $\Gamma_{1}$. This proves the theorem.

Note: If $\Gamma_{t}(s)=H(s, t)$ in the preceding proof, then each $\Gamma_{t}$ is a closed curve, but not necessarily a path, since $H$ is not assumed to be differentiable. The paths $\gamma_{k}$ were introduced for this reason. Another (and perhaps more satisfactory) way to circumvent this difficulty is to extend the definition of index to closed curves. This is sketched in Exercise 28.

## The Calculus of Residues

10.41 Definition A function $f$ is said to be meromorphic in an open set $\Omega$ if there is a set $A \subset \Omega$ such that

(a) $A$ has no limit point in $\Omega$,

(b) $f \in H(\Omega-A)$,

(c) $f$ has a pole at each point of $A$.

Note that the possibility $A=\varnothing$ is not excluded. Thus every $f \in H(\Omega)$ is meromorphic in $\Omega$.

Note also that $(a)$ implies that no compact subset of $\Omega$ contains infinitely many points of $A$, and that $A$ is therefore at most countable.

If $f$ and $A$ are as above, if $a \in A$, and if

$$
Q(z)=\sum_{k=1}^{m} c_{k}(z-a)^{-k}
$$

is the principal part of $f$ at $a$, as defined in Theorem 10.21 (i.e., if $f-Q$ has a removable singularity at $a$ ), then the number $c_{1}$ is called the residue of $f$ at $a$ :

$$
c_{1}=\operatorname{Res}(f ; a) .
$$

If $\Gamma$ is a cycle and $a \notin \Gamma^{*},(1)$ implies

$$
\frac{1}{2 \pi i} \int_{\Gamma} Q(z) d z=c_{1} \operatorname{Ind}_{\Gamma}(a)=\operatorname{Res}(Q ; a) \operatorname{Ind}_{\Gamma}(a)
$$

This very special case of the following theorem will be used in its proof.

10.42 The Residue Theorem Suppose $f$ is a meromorphic function in $\Omega$. Let $A$ be the set of points in $\Omega$ at which $f$ has poles. If $\Gamma$ is a cycle in $\Omega-A$ such that

$$
\operatorname{Ind}_{\Gamma}(\alpha)=0 \quad \text { for all } \quad \alpha \notin \Omega
$$

then

$$
\frac{1}{2 \pi i} \int_{\Gamma} f(z) d z=\sum_{a \in A} \operatorname{Res}(f ; a) \operatorname{Ind}_{\Gamma}(a)
$$

Proof Let $B=\left\{a \in A: \operatorname{Ind}_{\Gamma}(a) \neq 0\right\}$. Let $W$ be the complement of $\Gamma^{*}$. Then $\operatorname{Ind}_{\Gamma}(z)$ is constant in each component $V$ of $W$. If $V$ is unbounded, or if $V$ intersects $\Omega^{c}$, (1) implies that $\operatorname{Ind}_{\Gamma}(z)=0$ for every $z \in V$. Since $A$ has no limit point in $\Omega$, we conclude that $B$ is a finite set.

The sum in (2), though formally infinite, is therefore actually finite.

Let $a_{1}, \ldots, a_{n}$ be the points of $B$, let $Q_{1}, \ldots, Q_{n}$ be the principal parts of $f$ at $a_{1}, \ldots, a_{n}$, and put $g=f-\left(Q_{1}+\cdots+Q_{n}\right)$. (If $B=\varnothing$, a possibility which is not excluded, then $g=f$.) Put $\Omega_{0}=\Omega-(A-B)$. Since $g$ has removable
singularities at $a_{1}, \ldots, a_{n}$, Theorem 10.35 , applied to the function $g$ and the open set $\Omega_{0}$, shows that

$$
\int_{\Gamma} g(z) d z=0
$$

Hence

$$
\frac{1}{2 \pi i} \int_{\Gamma} f(z) d z=\sum_{i=1}^{n} \frac{1}{2 \pi i} \int_{\Gamma} Q_{k}(z) d z=\sum_{k=1}^{n} \operatorname{Res}\left(Q_{k} ; a_{k}\right) \operatorname{Ind}_{\Gamma}\left(a_{k}\right)
$$

and since $f$ and $Q_{k}$ have the same residue at $a_{k}$, we obtain (2).

We conclude this chapter with two typical applications of the residue theorem. The first one concerns zeros of holomorphic functions, the second is the evaluation of a certain integral.

10.43 Theorem Suppose $\gamma$ is a closed path in a region $\Omega$, such that $\operatorname{Ind}_{\gamma}(\alpha)=0$ for every $\alpha$ not in $\Omega$. Suppose also that $\operatorname{Ind}_{\gamma}(\alpha)=0$ or 1 for every $\alpha \in \Omega-\gamma^{*}$, and let $\Omega_{1}$ be the set of all $\alpha$ with $\operatorname{Ind}_{\gamma}(\alpha)=1$.

For any $f \in H(\Omega)$ let $N_{f}$ be the number of zeros of $f$ in $\Omega_{1}$, counted according to their multiplicities.

(a) If $f \in H(\Omega)$ and $f$ has no zeros on $\gamma^{*}$ then

$$
N_{f}=\frac{1}{2 \pi i} \int_{\gamma} \frac{f^{\prime}(z)}{f(z)} d z=\operatorname{Ind}_{\Gamma}(0)
$$

where $\Gamma=f \circ \gamma$.

(b) If also $g \in H(\Omega)$ and

$$
|f(z)-g(z)|<|f(z)| \quad \text { for all } z \in \gamma^{*}
$$

then $N_{g}=N_{f}$.

Part $(b)$ is usually called Rouché's theorem. It says that two holomorphic functions have the same number of zeros in $\Omega_{1}$ if they are close together on the boundary of $\Omega_{1}$, as specified by (2).

Proof Put $\varphi=f^{\prime} / f$, a meromorphic function in $\Omega$. If $a \in \Omega$ and $f$ has a zero of order $m=m(a)$ at $a$, then $f(z)=(z-a)^{m} h(z)$, where $h$ and $1 / h$ are holomorphic in some neighborhood $V$ of $a$. In $V-\{a\}$,

$$
\varphi(z)=\frac{f^{\prime}(z)}{f(z)}=\frac{m}{z-a}+\frac{h^{\prime}(z)}{h(z)}
$$

Thus

$$
\operatorname{Res}(\varphi ; a)=m(a)
$$

Let $A=\left\{a \in \Omega_{1}: f(a)=0\right\}$. If our assumptions about the index of $\gamma$ are combined with the residue theorem one obtains

$$
\frac{1}{2 \pi i} \int_{\nu} \frac{f^{\prime}(z)}{f(z)} d z=\sum_{a \in A} \operatorname{Res}(\varphi ; a)=\sum_{a \in A} m(a)=N_{f}
$$

This proves one half of (1). The other half is a matter of direct computation:

$$
\begin{aligned}
\operatorname{Ind}_{\Gamma}(0) & =\frac{1}{2 \pi i} \int_{\Gamma} \frac{d z}{z}=\frac{1}{2 \pi i} \int_{0}^{2 \pi} \frac{\Gamma^{\prime}(s)}{\Gamma(s)} d s \\
& =\frac{1}{2 \pi i} \int_{0}^{2 \pi} \frac{f^{\prime}(\gamma(s))}{f(\gamma(s))} \gamma^{\prime}(s) d s=\frac{1}{2 \pi i} \int_{\nu} \frac{f^{\prime}(z)}{f(z)} d z
\end{aligned}
$$

The parameter interval of $\gamma$ was here taken to be $[0,2 \pi]$.

Next, (2) shows that $g$ has no zero on $\gamma^{*}$. Hence (1) holds with $g$ in place of $f$. Put $\Gamma_{0}=g \circ \gamma$. Then it follows from (1), (2), and Lemma 10.39 that

$$
N_{g}=\operatorname{Ind}_{\Gamma_{0}}(0)=\operatorname{Ind}_{\Gamma}(0)=N_{f}
$$

10.44 Problem For real $t$, find the limit, as $A \rightarrow \infty$, of

$$
\int_{-A}^{A} \frac{\sin x}{x} e^{i x t} d x
$$

Solution Since $z^{-1} \cdot \sin z \cdot e^{i t z}$ is entire, its integral over $[-A, A]$ equals that over the path $\Gamma_{A}$ obtained by going from $-A$ to -1 along the real axis, from -1 to 1 along the lower half of the unit circle, and from 1 to $A$ along the real axis. This follows from Cauchy's theorem. $\Gamma_{A}$ avoids the origin, and we may therefore use the identity

$$
2 i \sin z=e^{i z}-e^{-i z}
$$

to see that (1) equals $\varphi_{A}(t+1)-\varphi_{A}(t-1)$, where

$$
\frac{1}{\pi} \varphi_{A}(s)=\frac{1}{2 \pi i} \int_{\Gamma_{A}} \frac{e^{i s z}}{z} d z
$$

Complete $\Gamma_{A}$ to a closed path in two ways: First, by the semicircle from $A$ to $-A i$ to $-A$; secondly, by the semicircle from $A$ to $A i$ to $-A$. The function $e^{i s z} / z$ has a single pole, at $z=0$, where its residue is 1 . It follows that

$$
\frac{1}{\pi} \varphi_{A}(s)=\frac{1}{2 \pi} \int_{-\pi}^{0} \exp \left(i s A e^{i \theta}\right) d \theta
$$

and

$$
\frac{1}{\pi} \varphi_{A}(s)=1-\frac{1}{2 \pi} \int_{0}^{\pi} \exp \left(i s A e^{i \theta}\right) d \theta
$$

Note that

$$
\left|\exp \left(i s A e^{i \theta}\right)\right|=\exp (-A s \sin \theta)
$$

and that this is $<1$ and tends to 0 as $A \rightarrow \infty$ if $s$ and $\sin \theta$ have the same sign. The dominated convergence theorem shows therefore that the integral in (3) tends to 0 if $s<0$, and the one in (4) tends to 0 if $s>0$. Thus

$$
\lim _{A \rightarrow \infty} \varphi_{A}(s)= \begin{cases}\pi & \text { if } s>0 \\ 0 & \text { if } s<0\end{cases}
$$

and if we apply (6) to $s=t+1$ and to $s=t-1$, we get

$$
\lim _{A \rightarrow \infty} \int_{-A}^{A} \frac{\sin x}{x} e^{i t x} d x= \begin{cases}\pi & \text { if }-1<t<1 \\ 0 & \text { if }|t|>1\end{cases}
$$

Since $\varphi_{A}(0)=\pi / 2$, the limit in (7) is $\pi / 2$ when $t= \pm 1$.

Note that (7) gives the Fourier transform of $(\sin x) / x$. We leave it as an exercise to check the result against the inversion theorem.

## Exercises

1 The following fact was tacitly used in this chapter: If $A$ and $B$ are disjoint subsets of the plane, if $A$ is compact, and if $B$ is closed, then there exists a $\delta>0$ such that $|\alpha-\beta| \geq \delta$ for all $\alpha \in A$ and $\beta \in B$. Prove this, with an arbitrary metric space in place of the plane.

2 Suppose that $f$ is an entire function, and that in every power series

$$
f(z)=\sum_{n=0}^{\infty} c_{n}(z-a)^{n}
$$

at least one coefficient is 0 . Prove that $f$ is a polynomial.

Hint: $n ! c_{n}=f^{(n)}(a)$.

3 Suppose $f$ and $g$ are entire functions, and $|f(z)| \leq|g(z)|$ for every $z$. What conclusion can you draw?

4 Suppose $f$ is an entire function, and

$$
|f(z)| \leq A+B|z|^{k}
$$

for all $z$, where $A, B$, and $k$ are positive numbers. Prove that $f$ must be a polynomial.

5 Suppose $\left\{f_{n}\right\}$ is a uniformly bounded sequence of holomorphic functions in $\Omega$ such that $\left\{f_{n}(z)\right\}$ converges for every $z \in \Omega$. Prove that the convergence is uniform on every compact subset of $\Omega$.

Hint: Apply the dominated convergence theorem to the Cauchy formula for $f_{n}-f_{m}$.

6 There is a region $\Omega$ that $\exp (\Omega)=D(1 ; 1)$. Show that $\exp$ is one-to-one in $\Omega$, but that there are many such $\Omega$. Fix one, and define $\log z$, for $|z-1|<1$, to be that $\dot{w} \in \Omega$ for which $e^{w}=z$. Prove that $\log ^{\prime}(z)=1 / z$. Find the coefficients $a_{n}$ in

$$
\frac{1}{z}=\sum_{n=0}^{\infty} a_{n}(z-1)^{n}
$$

and hence find the coefficients $c_{n}$ in the expansion

$$
\log z=\sum_{n=0}^{\infty} c_{n}(z-1)^{n}
$$

In what other discs can this be done?

7 If $f \in H(\Omega)$, the Cauchy formula for the derivatives of $f$,

$$
f^{(n)}(z)=\frac{n !}{2 \pi i} \int_{\Gamma} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta \quad(n=1,2,3, \ldots)
$$

is valid under certain conditions on $z$ and $\Gamma$. State these, and prove the formula.

8 Suppose $P$ and $Q$ are polynomials, the degree of $Q$ exceeds that of $P$ by at least 2 , and the rational function $R=P / Q$ has no pole on the real axis. Prove that the integral of $R$ over $(-\infty, \infty)$ is $2 \pi i$ times the sum of the residues of $R$ in the upper half plane. [Replace the integral over $(-A, A)$ by one over a suitable semicircle, and apply the residue theorem.] What is the analogous statement for the lower half plane? Use this method to compute

$$
\int_{-\infty}^{\infty} \frac{x^{2}}{1+x^{4}} d x
$$

9 Compute $\int_{-\infty}^{\infty} e^{i t x} /\left(1+x^{2}\right) d x$ for real $t$, by the method described in Exercise 8 . Check your answer against the inversion theorem for Fourier transforms.

10 Let $\gamma$ be the positively oriented unit circle, and compute

$$
\frac{1}{2 \pi i} \int_{\gamma} \frac{e^{z}-e^{-z}}{z^{4}} d z
$$

11 Suppose $\alpha$ is a complex number, $|\alpha| \neq 1$, and compute

$$
\int_{0}^{2 \pi} \frac{d \theta}{1-2 \alpha \cos \theta+\alpha^{2}}
$$

by integrating $(z-\alpha)^{-1}(z-1 / \alpha)^{-1}$ over the unit circle.

12 Compute

$$
\left.\int_{-\infty}^{\infty}\left(\frac{\sin x}{x}\right)^{2} e^{i t x} d x \quad \text { (for real } t\right)
$$

13 Compute

$$
\int_{0}^{\infty} \frac{d x}{1+x^{n}} \quad(n=2,3,4, \ldots)
$$

[For even $n$, the method of Exercise 8 can be used. However, a different path can be chosen, which simplifies the computation and which also works for odd $n$ : from 0 to $R$ to $R \exp (2 \pi i / n)$ to 0 .]

Answer: $(\pi / n) / \sin (\pi / n)$.

14 Suppose $\Omega_{1}$ and $\Omega_{2}$ are plane regions, $f$ and $g$ are nonconstant complex functions defined in $\Omega_{1}$ and $\Omega_{2}$, respectively, and $f\left(\Omega_{1}\right) \subset \Omega_{2}$. Put $h=g \circ f$. If $f$ and $g$ are holomorphic, we know that $h$ is holomorphic. Suppose we know that $f$ and $h$ are holomorphic. Can we conclude anything about $g$ ? What if we know that $g$ and $h$ are holomorphic?

15 Suppose $\Omega$ is a region, $\varphi \in H(\Omega), \varphi^{\prime}$ has no zero in $\Omega, f \in H(\varphi(\Omega)), g=f \circ \varphi, z_{0} \in \Omega$, and $w_{0}=$ $\varphi\left(z_{0}\right)$. Prove that if $f$ has a zero of order $m$ at $w_{0}$, then $g$ also has a zero of order $m$ at $z_{0}$. How is this modified if $\varphi^{\prime}$ has a zero of order $k$ at $z_{0}$ ?

16 Suppose $\mu$ is a complex measure on a measure space $X, \Omega$ is an open set in the plane, $\varphi$ is a bounded function on $\Omega \times X$ such that $\varphi(z, t)$ is a measurable function of $t$, for each $z \in \Omega$, and $\varphi(z, t)$ is holomorphic in $\Omega$, for each $t \in X$. Define

$$
f(z)=\int_{x} \varphi(z, t) d \mu(t)
$$

for $z \in \Omega$. Prove that $f \in H(\Omega)$. Hint : Show that to every compact $K \subset \Omega$ there corresponds a constant $M<\infty$ such that

$$
\left|\frac{\varphi(z, t)-\varphi\left(z_{0}, t\right)}{z-z_{0}}\right|<M \quad\left(z \text { and } z_{0} \in K, t \in X\right)
$$

17 Determine the regions in which the following functions are defined and holomorphic:

$$
f(z)=\int_{0}^{1} \frac{d t}{1+t z}, \quad g(z)=\int_{0}^{\infty} \frac{e^{t z}}{1+t^{2}} d t, \quad h(z)=\int_{-1}^{1} \frac{e^{t z}}{1+t^{2}} d t
$$

Hint: Either use Exercise 16, or combine Morera's theorem with Fubini's.

18 Suppose $f \in H(\Omega), \vec{D}(a ; r) \subset \Omega, \gamma$ is the positively oriented circle with center at $a$ and radius $r$, and $f$ has no zero on $\gamma^{*}$. For $p=0$, the integral

$$
\frac{1}{2 \pi i} \int_{\gamma} \frac{f^{\prime}(z)}{f(z)} z^{p} d z
$$

is equal to the number of zeros of $f$ in $D(a ; r)$. What is the value of this integral (in terms of the zeros of $f$ ) for $p=1,2,3, \ldots$ ? What is the answer if $z^{p}$ is replaced by any $\varphi \in H(\Omega)$ ?

19 Suppose $f \in H(U), g \in H(U)$, and neither $f$ nor $g$ has a zero in $U$. If

$$
\frac{f^{\prime}}{f}\left(\frac{1}{n}\right)=\frac{g^{\prime}}{g}\left(\frac{1}{n}\right) \quad(n=1,2,3, \ldots)
$$

find another simple relation between $f$ and $g$.

20 Suppose $\Omega$ is a region, $f_{n} \in H(\Omega)$ for $n=1,2,3, \ldots$, none of the functions $f_{n}$ has a zero in $\Omega$, and $\left\{f_{n}\right\}$ converges to $f$ uniformly on compact subsets of $\Omega$. Prove that either $f$ has no zero in $\Omega$ or $f(z)=0$ for all $z \in \Omega$.

If $\Omega^{\prime}$ is a region that contains every $f_{n}(\Omega)$, and if $f$ is not constant, prove that $f(\Omega) \subset \Omega^{\prime}$.

21 Suppose $f \in H(\Omega), \Omega$ contains the closed unit disc, and $|f(z)|<1$ if $|z|=1$. How many fixed points must $f$ have in the disc? That is, how many solutions does the equation $f(z)=z$ have there?

22 Suppose $f \in H(\Omega), \Omega$ contains the closed unit disc, $|f(z)|>2$ if $|z|=1$, and $f(0)=1$. Must $f$ have a zero in the unit disc?

23 Suppose $P_{n}(z)=1+z / 1 !+\cdots+z^{n} / n !, Q_{n}(z)=P_{n}(z)-1$, where $n=1,2,3, \ldots$. What can you say about the location of the zeros of $P_{n}$ and $Q_{n}$ for large $n$ ? Be as specific as you can.

24 Prove the following general form of Rouche's theorem: Let $\Omega$ be the interior of a compact set $K$ in the plane. Suppose $f$ and $g$ are continuous on $K$ and holomorphic in $\Omega$, and $|f(z)-g(z)|<|f(z)|$ for all $z \in K-\Omega$. Then $f$ and $g$ have the same number of zeros in $\Omega$.

25 Let $A$ be the annulus $\left\{z: r_{1}<|z|<r_{2}\right\}$, where $r_{1}$ and $r_{2}$ are given positive numbers.

(a) Show that the Cauchy formula

$$
f(z)=\frac{1}{2 \pi i}\left(\int_{\gamma_{1}}+\int_{\gamma_{2}}\right) \frac{f(\zeta)}{\zeta-z} d \zeta
$$

is valid under the following conditions: $f \in H(A)$,

$$
r_{1}+\epsilon<|z|<r_{2}-\epsilon,
$$

and

$$
\gamma_{1}(t)=\left(r_{1}+\epsilon\right) e^{-i t}, \quad \gamma_{2}(t)=\left(r_{2}-\epsilon\right) e^{i t} \quad(0 \leq t \leq 2 \pi)
$$

(b) Show by means of $(a)$ that every $f \in H(A)$ can be decomposed into a sum $f=f_{1}+f_{2}$, where $f_{1}$ is holomorphic outside $\bar{D}\left(0 ; r_{1}\right)$ and $f_{2} \in H\left(D\left(0 ; r_{2}\right)\right)$; the decomposition is unique if we require that $f_{1}(z) \rightarrow 0$ as $|z| \rightarrow \infty$.

(c) Use this decomposition to associate with each $f \in H(A)$ its so-called "Laurent series"

$$
\sum_{-\infty}^{\infty} c_{n} z^{n}
$$

which converges to $f$ in $A$. Show that there is only one such series for each $f$. Show that it converges to $f$ uniformly on compact subsets of $A$.

(d) If $f \in H(A)$ and $f$ is bounded in $A$, show that the components $f_{1}$ and $f_{2}$ are also bounded.

(e) How much of the foregoing can you extend to the case $r_{1}=0$ (or $r_{2}=\infty$, or both)? two) circles?

$(f)$ How much of the foregoing can you extend to regions bounded by finitely many (more than

26 It is required to expand the function

$$
\frac{1}{1-z^{2}}+\frac{1}{3-z}
$$

in a series of the form $\sum_{-\infty}^{\infty} c_{n} z^{n}$.

How many such expansions are there? In which region is each of them valid? Find the coefficients $c_{n}$ explicitly for each of these expansions.

27 Suppose $\Omega$ is a horizontal strip, determined by the inequalities $a<y<b$, say. Suppose $f \in H(\Omega)$, and $f(z)=f(z+1)$ for all $z \in \Omega$. Prove that $f$ has a Fourier expansion in $\Omega$,

$$
f(z)=\sum_{-\infty}^{\infty} c_{n} e^{2 \pi i n z}
$$

which converges uniformly in $\{z: a+\epsilon \leq y \leq b-\epsilon\}$, for every $\epsilon>0$. Hint: The map $z \rightarrow e^{2 \pi i z}$ converts $f$ to a function in an annulus.

Find the integral formulas by means of which the coefficients $c_{n}$ can be computed from $f$.

28 Suppose $\Gamma$ is a closed curve in the plane, with parameter interval $[0,2 \pi]$. Take $\alpha \notin \Gamma^{*}$. Approximate $\Gamma$ uniformly by trigonometric polynomials $\Gamma_{n}$. Show that $\operatorname{Ind}_{\Gamma_{n}}(\alpha)=\operatorname{Ind}_{\Gamma_{m}}(\alpha)$ if $m$ and $n$ are sufficiently large. Define this common value to be $\operatorname{Ind}_{\Gamma}(\alpha)$. Prove that the result does not depend on the choice of $\left\{\Gamma_{n}\right\}$; prove that Lemma 10.39 is now true for closed curves, and use this to give a different proof of Theorem 10.40 .

29 Define

$$
f(z)=\frac{1}{\pi} \int_{0}^{1} r d r \int_{-\pi}^{\pi} \frac{d \theta}{r e^{i \theta}+z}
$$

Show that $f(z)=\bar{z}$ if $|z|<1$ and that $f(z)=1 / z$ if $|z| \geq 1$.

Thus $f$ is not holomorphic in the unit disc, although the integrand is a holomorphic function of z. Note the contrast between this, on the one hand, and Theorem 10.7 and Exercise 16 on the other.

Suggestion: Compute the inner integral separately for $r\langle|z|$ and for $r>|z|$.

30 Let $\Omega$ be the plane minus two points, and show that some closed paths $\Gamma$ in $\Omega$ satisfy assumption (1) of Theorem 10.35 without being null-homotopic in $\Omega$.

## HARMONIC FUNCTIONS

## The Cauchy-Riemann Equations

11.1 The Operators $\partial$ and $\bar{\partial}$ Suppose $f$ is a complex function defined in a plane open set $\Omega$. Regard $f$ as a transformation which maps $\Omega$ into $R^{2}$, and assume that $f$ has a differential at some point $z_{0} \in \Omega$, in the sense of Definition 7.22. For simplicity, suppose $z_{0}=f\left(z_{0}\right)=0$. Our differentiability assumption is then equivalent to the existence of two complex numbers $\alpha$ and $\beta$ (the partial derivatives of $f$ with respect to $x$ and $y$ at $z_{0}=0$ ) such that

$$
f(z)=\alpha x+\beta y+\eta(z) z \quad(z=x+i y)
$$

where $\eta(z) \rightarrow 0$ as $z \rightarrow 0$.

Since $2 x=z+\bar{z}$ and $2 i y=z-\bar{z}$, (1) can be rewritten in the form

$$
f(z)=\frac{\alpha-i \beta}{2} z+\frac{\alpha+i \beta}{2} \bar{z}+\eta(z) z
$$

This suggests the introduction of the differential operators

$$
\partial=\frac{1}{2}\left(\frac{\partial}{\partial x}-i \frac{\partial}{\partial y}\right), \quad \bar{\partial}=\frac{1}{2}\left(\frac{\partial}{\partial x}+i \frac{\partial}{\partial y}\right)
$$

Now (2) becomes

$$
\frac{f(z)}{z}=(\partial f)(0)+(\bar{\partial} f)(0) \cdot \frac{\bar{z}}{z}+\eta(z) \quad(z \neq 0)
$$

For real $z, \bar{z} / z=1$; for pure imaginary $z, \bar{z} / z=-1$. Hence $f(z) / z$ has a limit at 0 if and only if $(\bar{\partial} f)(0)=0$, and we obtain the following characterization of holomorphic functions:

11.2 Theorem Suppose $f$ is a complex function in $\Omega$ that has a differential at every point of $\Omega$. Then $f \in H(\Omega)$ if and only if the Cauchy-Riemann equation

$$
(\bar{\partial} f)(z)=0
$$

holds for every $z \in \Omega$. In that case we have

$$
f^{\prime}(z)=(\partial f)(z) \quad(z \in \Omega)
$$

If $f=u+i v, u$ and $v$ real, (1) splits into the pair of equations

$$
u_{x}=v_{y}, \quad u_{y}=-v_{x}
$$

where the subscripts refer to partial differentiation with respect to the indicated variable. These are the Cauchy-Riemann equations which must be satisfied by the real and imaginary parts of a holomorphic function.

11.3 The Laplacian Let $f$ be a complex function in a plane open set $\Omega$, such that $f_{x x}$ and $f_{y y}$ exist at every point of $\Omega$. The Laplacian of $f$ is then defined to be

$$
\Delta f=f_{x x}+f_{y y}
$$

If $f$ is continuous in $\Omega$ and if

$$
\Delta f=0
$$

at every point of $\Omega$, then $f$ is said to be harmonic in $\Omega$.

Since the Laplacian of a real function is real (if it exists), it is clear that $a$ complex function is harmonic in $\Omega$ if and only if both its real part and its imaginary part are harmonic in $\Omega$.

Note that

$$
\Delta f=4 \partial \bar{\partial} f
$$

provided that $f_{x y}=f_{y x}$, and that this happens for all $f$ which have continuous second-order derivatives.

If $f$ is holomorphic, then $\bar{\partial} f=0, f$ has continuous derivatives of all orders, and therefore (3) shows:

### 11.4 Theorem Holomorphic functions are harmonic.

We shall now turn our attention to an integral representation of harmonic functions which is closely related to the Cauchy formula for holomorphic functions. It will show, among other things, that every real harmonic function is locally the real part of a holomorphic function, and it will yield information about the boundary behavior of certain classes of holomorphic functions in open discs.

## The Poisson Integral

11.5 The Poisson Kernel This is the function

$$
P_{r}(t)=\sum_{-\infty}^{\infty} r^{|n|} e^{i n t} \quad(0 \leq r<1, t \text { real })
$$

We may regard $P_{r}(t)$ as a function of two variables $r$ and $t$ or as a family of functions of $t$, indexed by $r$.

If $z=r e^{i \theta}(0 \leq r<1, \theta$ real), a simple calculation, made in Sec. 5.24, shows that

$$
P_{r}(\theta-t)=\operatorname{Re}\left[\frac{e^{i t}+z}{e^{i t}-z}\right]=\frac{1-r^{2}}{1-2 r \cos (\theta-t)+r^{2}} .
$$

From (1) we see that

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} P_{r}(t) d t=1 \quad(0 \leq r<1)
$$

From (2) it follows that $P_{r}(t)>0, P_{r}(t)=P_{r}(-t)$, that

$$
P_{r}(t)<P_{r}(\delta) \quad(0<\delta<|t| \leq \pi)
$$

and that

$$
\lim _{r \rightarrow 1} P_{r}(\delta)=0 \quad(0<\delta \leq \pi)
$$

These properties are reminiscent of the trigonometric polynomials $Q_{k}(t)$ that were discussed in Sec. 4.24.

The open unit disc $D(0 ; 1)$ will from now on be denoted by $U$. The unit circle - the boundary of $U$ in the complex plane - will be denoted by $T$. Whenever it is convenient to do so, we shall identify the spaces $L^{p}(T)$ and $C(T)$ with the corresponding spaces of $2 \pi$-periodic functions on $R^{1}$, as in Sec. 4.23. becomes

One can also regard $P_{r}(\theta-t)$ as a function of $z=r e^{i \theta}$ and $e^{i t}$. Then (2)

$$
P\left(z, e^{i t}\right)=\frac{1-|z|^{2}}{\left|e^{i t}-z\right|^{2}}
$$

for $z \in U, e^{i t} \in T$.

11.6 The Poisson Integral If $f \in L^{1}(T)$ and

$$
F\left(r e^{i \theta}\right)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} P_{r}(\theta-t) f(t) d t
$$

then the function $F$ so defined in $U$ is called the Poisson integral of $f$. We shall sometimes abbreviate the relation (1) to

$$
F=P[f] .
$$

If $f$ is real, formula $11.5(2)$ shows that $P[f]$ is the real part of

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{e^{i t}+z}{e^{i t}-z} f(t) d t
$$

which is a holomorphic function of $z=r e^{i \theta}$ in $U$, by Theorem 10.7. Hence $P[f]$ is harmonic in $U$. Since linear combinations (with constant coefficients) of harmonic functions are harmonic, we see that the following is true:

11.7 Theorem If $f \in L^{1}(T)$ then the Poisson integral $P[f]$ is a harmonic function in $U$.

The following theorem shows that Poisson integrals of continuous functions behave particularly well near the boundary of $U$.

11.8 Theorem If $f \in C(T)$ and if $H f$ is defined on the closed unit disc $\bar{U}$ by

$$
(H f)\left(r e^{i \theta}\right)= \begin{cases}f\left(e^{i \theta}\right) & \text { if } r=1, \\ P[f]\left(r e^{i \theta}\right) & \text { if } 0 \leq r<1,\end{cases}
$$

then $H f \in C(\bar{U})$.

Proof Since $P_{r}(t)>0$, formula 11.5(3) shows, for every $g \in C(T)$, that

$$
\left|P[g]\left(r e^{i \theta}\right)\right| \leq\|g\|_{T} \quad(0 \leq r<1)
$$

so that

$$
\|H g\|_{\bar{U}}=\|g\|_{T} \quad(g \in C(T)) .
$$

(As in Sec. 5.22, we use the notation $\|g\|_{E}$ to denote the supremum of $|g|$ on the set $E$.) If

$$
g\left(e^{i \theta}\right)=\sum_{n=-N}^{N} c_{n} e^{i n \theta}
$$

is any trigonometric polynomial, it follows from 11.5(1) that

$$
(H g)\left(r e^{i \theta}\right)=\sum_{n=-N}^{N} c_{n} r^{|n|} e^{i n \theta}
$$

so that $H g \in C(\bar{U})$.

Finally, there are trigonometric polynomials $g_{k}$ such that $\left\|g_{k}-f\right\|_{T} \rightarrow 0$ as $k \rightarrow \infty$. (See Sec. 4.24.) By (3), it follows that

$$
\left\|H g_{k}-H f\right\|_{\bar{U}}=\left\|H\left(g_{k}-f\right)\right\|_{\bar{U}} \rightarrow 0
$$

as $k \rightarrow \infty$. This says that the functions $H g_{k} \in C(\bar{U})$ converge, uniformly on $\bar{U}$, to $H f$. Hence $H f \in C(\bar{U})$.

Note: This theorem provides the solution of a boundary value problem (the Dirichlet problem): A continuous function $f$ is given on $T$ and it is required to find a harmonic function $F$ in $U$ "whose boundary values are $f$." The theorem exhibits a solution, by means of the Poisson integral of $f$, and it states the relation between $f$ and $F$ more precisely. The uniqueness theorem which corresponds to this existence theorem is contained in the following result.

11.9 Theorem Suppose $u$ is a continuous real function on the closed unit disc $\bar{U}$, and suppose $u$ is harmonic in $U$. Then (in $U$ ) $u$ is the Poisson integral of its restriction to $T$, and $u$ is the real part of the holomorphic function

$$
f(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{e^{i t}+z}{e^{i t}-z} u\left(e^{i t}\right) d t \quad(z \in U)
$$

Proof Theorem 10.7 shows that $f \in H(U)$. If $u_{1}=\operatorname{Re} f$, then (1) shows that $u_{1}$ is the Poisson integral of the boundary values of $u$, and the theorem will be proved as soon as we show that $u=u_{1}$.

Put $h=u-u_{1}$. Then $h$ is continuous on $\bar{U}$ (apply Theorem 11.8 to $u_{1}$ ), $h$ is harmonic in $U$, and $h=0$ at all points of $T$. Assume (this will lead to a contradiction) that $h\left(z_{0}\right)>0$ for some $z_{0} \in U$. Fix $\epsilon$ so that $0<\epsilon<h\left(z_{0}\right)$, and define

$$
g(z)=h(z)+\epsilon|z|^{2} \quad(z \in \bar{U}) .
$$

Then $g\left(z_{0}\right) \geq h\left(z_{0}\right)>\epsilon$. Since $g \in C(\bar{U})$ and since $g=\epsilon$ at all points of $T$, there exists a point $z_{1} \in U$ at which $g$ has a local maximum. This implies that $g_{x x} \leq 0$ and $g_{y y} \leq 0$ at $z_{1}$. But (2) shows that the Laplacian of $g$ is $4 \epsilon>0$, and we have a contradiction.

Thus $u-u_{1} \leq 0$. The same argument shows that $u_{1}-u \leq 0$. Hence $u=$ $u_{1}$, and the proof is complete.

11.10 So far we have considered only the unit disc $U=D(0 ; 1)$. It is clear that the preceding work can be carried over to arbitrary circular discs, by a simple change of variables. Hence we shall merely summarize some of the results:

If $u$ is a continuous real function on the boundary of the disc $D(a ; R)$ and if $u$ is defined in $D(a ; R)$ by the Poisson integral

$$
u\left(a+r e^{i \theta}\right)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{R^{2}-r^{2}}{R^{2}-2 R r \cos (\theta-t)+r^{2}} u\left(a+R e^{i t}\right) d t
$$

then $u$ is continuous on $\bar{D}(a ; R)$ and harmonic in $D(a ; R)$.

If $u$ is harmonic (and real) in an open set $\Omega$ and if $\bar{D}(a ; R) \subset \Omega$, then $u$ satisfies (1) in $D(a ; R)$ and there is a holomorphic function $f$ defined in $D(a ; R)$ whose real part is $u$. This $f$ is uniquely defined, up to a pure imaginary additive constant. For if two functions, holomorphic in the same region, have the same real part, their difference must be constant (a corollary of the open mapping theorem, or the Cauchy-Riemann equations).

We may summarize this by saying that every real harmonic function is locally the real part of a holomorphic function.

Consequently, every harmonic function has continuous partial derivatives of all orders.

The Poisson integral also yields information about sequences of harmonic functions:

11.11 Harnack's Theorem Let $\left\{u_{n}\right\}$ be a sequence of harmonic functions in a region $\Omega$.

(a) If $u_{n} \rightarrow u$ uniformly on compact subsets of $\Omega$, then $u$ is harmonic in $\Omega$.

(b) If $u_{1} \leq u_{2} \leq u_{3} \leq \cdots$, then either $\left\{u_{n}\right\}$ converges uniformly on compact subsets of $\Omega$, or $u_{n}(z) \rightarrow \infty$ for every $z \in \Omega$.

Proof To prove $(a)$, assume $\bar{D}(a ; R) \subset \Omega$, and replace $u$ by $u_{n}$ in the Poisson integral 11.10(1). Since $u_{n} \rightarrow u$ uniformly on the boundary of $\bar{D}(a ; R)$, we conclude that $u$ itself satisfies $11.10(1)$ in $D(a ; R)$.

In the proof of $(b)$, we may assume that $u_{1} \geq 0$. (If not, replace $u_{n}$ by $u_{n}-u_{1}$.) Put $u=\sup u_{n}$, let $A=\{z \in \Omega: u(z)<\infty\}$, and $B=\Omega-A$. Choose $\bar{D}(a ; R) \subset \Omega$. The Poisson kernel satisfies the inequalities

$$
\frac{R-r}{R+r} \leq \frac{R^{2}-r^{2}}{R^{2}-2 r R \cos (\theta-t)+r} \leq \frac{R+r}{R-r}
$$

for $0 \leq r<R$. Hence

$$
\frac{R-r}{R+r} u_{n}(a) \leq u_{n}\left(a+r e^{i \theta}\right) \leq \frac{R+r}{R-r} u_{n}(a)
$$

The same inequalities hold with $u$ in place of $u_{n}$. It follows that either $u(z)=\infty$ for all $z \in D(a ; R)$ or $u(z)<\infty$ for all $z \in D(a ; R)$.

Thus both $A$ and $B$ are open; and since $\Omega$ is connected, we have either $A=\varnothing$ (in which case there is nothing to prove) or $A=\Omega$. In the latter case, the monotone convergence theorem shows that the Poisson formula holds for $u$ in every disc in $\Omega$. Hence $u$ is harmonic in $\Omega$. Whenever a sequence of continuous functions converges monotonically to a continuous limit, the convergence is uniform on compact sets ([26], Theorem 7.13). This completes the proof.

## The Mean Value Property

11.12 Definition We say that a continuous function $u$ in an open set $\Omega$ has the mean value property if to every $z \in \Omega$ there corresponds a sequence $\left\{r_{n}\right\}$ such that $r_{n}>0, r_{n} \rightarrow 0$ as $n \rightarrow \infty$, and

$$
u(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} u\left(z+r_{n} e^{i t}\right) d t \quad(n=1,2,3, \ldots)
$$

In other words, $u(z)$ is to be equal to the mean value of $u$ on the circles of radius $r_{n}$ and with center at $z$.

Note that the Poisson formula shows that (1) holds for every harmonic function $u$, and for every $r$ such that $\bar{D}(z ; r) \subset \Omega$. Thus harmonic functions satisfy a much stronger mean value property than the one that we just defined. The following theorem may therefore come as a surprise:

11.13 Theorem If a continuous function $u$ has the mean value property in an open set $\Omega$, then $u$ is harmonic in $\Omega$.

Proof It is enough to prove this for real $u$. Fix $\bar{D}(a ; R) \subset \Omega$. The Poisson integral gives us a continuous function $h$ on $\bar{D}(a ; R)$ which is harmonic in $D(a ; R)$ and which coincides with $u$ on the boundary of $D(a ; R)$. Put $v=u-h$, and let $m=\sup \{v(z): z \in \bar{D}(a ; R)\}$. Assume $m>0$, and let $E$ be the set of all $z \in \bar{D}(a ; R)$ at which $v(z)=m$. Since $v=0$ on the boundary of $D(a ; R), E$ is a compact subset of $D(a ; R)$. Hence there exists a $z_{0} \in E$ such that

$$
\left|z_{0}-a\right| \geq|z-a|
$$

for all $z \in E$. For all small enough $r$, at least half the circle with center $z_{0}$ and radius $r$ lies outside $E$, so that the corresponding mean values of $v$ are all less than $m=v\left(z_{0}\right)$. But $v$ has the mean value property, and we have a contradiction. Thus $m=0$, so $v \leq 0$. The same reasoning applies to $-v$. Hence $v=0$, or $u=h$ in $D(a ; R)$, and since $\bar{D}(a ; R)$ was an arbitrary closed disc in $\Omega, u$ is harmonic in $\Omega$.

Theorem 11.13 leads to a reflection theorem for holomorphic functions. By the upper half plane $\Pi^{+}$we mean the set of all $z=x+i y$ with $y>0$; the lower half plane $\Pi^{-}$consists of all $z$ whose imaginary part is negative.

11.14 Theorem (The Schwarz reflection principle) Suppose $L$ is a segment of the real axis, $\Omega^{+}$is a region in $\Pi^{+}$, and every $t \in L$ is the center of an open disc $D_{t}$ such that $\Pi^{+} \cap D_{t}$ lies in $\Omega^{+}$. Let $\Omega^{-}$be the reflection of $\Omega^{+}$:

$$
\Omega^{-}=\left\{z: \bar{z} \in \Omega^{+}\right\}
$$

Suppose $f=u+i v$ is holomorphic in $\Omega^{+}$, and

$$
\lim _{n \rightarrow \infty} v\left(z_{n}\right)=0
$$

for every sequence $\left\{z_{n}\right\}$ in $\Omega^{+}$which converges to a point of $L$.

Then there is a function $F$, holomorphic in $\Omega^{+} \cup L \cup \Omega^{-}$, such that $F(z)=f(z)$ in $\Omega^{+} ;$this $F$ satisfies the relation

$$
F(\bar{z})=\overline{F(z)} \quad\left(z \in \Omega^{+} \cup L \cup \Omega^{-}\right)
$$

The theorem asserts that $f$ can be extended to a function which is holomorphic in a region symmetric with respect to the real axis, and (3) states that $F$ preserves this symmetry. Note that the continuity hypothesis (2) is merely imposed on the imaginary part of $f$.

Proof Put $\Omega=\Omega^{+} \cup L \cup \Omega^{-}$. We extend $v$ to $\Omega$ by defining $v(z)=0$ for $z \in L$ and $v(z)=-v(\bar{z})$ for $z \in \Omega^{-}$. It is then inmediate that $v$ is continuous and that $v$ has the mean value property in $\Omega$, so that $v$ is harmonic in $\Omega$, by Theorem 11.13 .

Hence $v$ is locally the imaginary part of a holomorphic function. This means that to each of the discs $D_{t}$ there corresponds an $f_{t} \in H\left(D_{t}\right)$ such that $\operatorname{Im} f_{t}=v$. Each $f_{t}$ is determined by $v$ up to a real additive constant. If this constant is chosen so that $f_{t}(z)=f(z)$ for some $z \in D_{t} \cap \Pi^{+}$, the same will hold for all $z \in D_{t} \cap \Pi^{+}$, since $f-f_{t}$ is constant in the region $D_{t} \cap \Pi^{+}$. We assume that the functions $f_{t}$ are so adjusted.

The power series expansion of $f_{t}$ in powers of $z-t$ has only real coefficients, since $v=0$ on $L$, so that all derivatives of $f_{t}$ are real at $t$. It follows that

$$
f_{t}(\bar{z})=\overline{f_{t}(z)} \quad\left(z \in D_{t}\right)
$$

Next, assume that $D_{s} \cap D_{t} \neq \varnothing$. Then $f_{t}=f=f_{s}$ in $D_{t} \cap D_{s} \cap \Pi^{+}$; and since $D_{t} \cap D_{s}$ is connected, Theorem 10.18 shows that

$$
f_{t}(z)=f_{s}(z) \quad\left(z \in D_{t} \cap D_{s}\right)
$$

Thus it is consistent to define

$$
F(z)= \begin{cases}f(z) & \text { for } z \in \Omega^{+} \\ f_{t}(z) & \text { for } z \in D_{t} \\ \frac{f(\bar{z})}{} & \text { for } z \in \Omega^{-}\end{cases}
$$

and it remains to show that $F$ is holomorphic in $\Omega^{-}$. If $D(a ; r) \subset \Omega^{-}$, then $D(\bar{a} ; r) \subset \Omega^{+}$, so for every $z \in D(a ; r)$ we have

$$
f(\bar{z})=\sum_{n=0}^{\infty} c_{n}(\bar{z}-\bar{a})^{n}
$$

Hence

$$
F(z)=\sum_{n=0}^{\infty} \bar{c}_{n}(z-a)^{n} \quad(z \in D(a ; r))
$$

This completes the proof.

## Boundary Behavior of Poisson Integrals

11.15 Our next objective is to find analogues of Theorem 11.8 for Poisson integrals of $L^{p}$-functions and measures on $T$. by

Let us associate to any function $u$ in $U$ a family of functions $u_{r}$ on $T$, defined

$$
u_{r}\left(e^{i \theta}\right)=u\left(r e^{i \theta}\right) \quad(0 \leq r<1)
$$

Thus $u_{r}$ is essentially the restriction of $u$ to the circle with radius $r$, center 0 , but we shift the domain of $u_{r}$ to $T$.

Using this terminology, Theorem 11.8 can be stated in the following form: words,

If $f \in C(T)$ and $F=P[f]$, then $F_{r} \rightarrow f$ uniformly on $T$, as $r \rightarrow 1$. In other

$$
\lim _{r \rightarrow 1}\left\|F_{r}-f\right\|_{\infty}=0
$$

which implies of course that

$$
\lim _{r \rightarrow 1} F_{r}\left(e^{i \theta}\right)=f\left(e^{i \theta}\right)
$$

at every point of $T$.

As regards (2), we shall now see (Theorem 11.16) that the corresponding norm-convergence result is just as easy in $L^{p}$. Instead of confining ourselves to investigating radial limits, as in (3), we shall then study nontangential limits of Poisson integrals of measures and $L^{p}$-functions; the differentiation theory developed in Chap. 7 will play an essential role in that study.

11.16 Theorem If $1 \leq p \leq \infty, f \in L^{p}(T)$, and $u=P[f]$, then

$$
\left\|u_{r}\right\|_{p} \leq\|f\|_{p} \quad(0 \leq r<1) .
$$

If $1 \leq p<\infty$, then

$$
\lim _{r \rightarrow 1}\left\|u_{r}-f\right\|_{p}=0
$$

Proof If we apply Jensen's inequality (or Hölder's) to

$$
u_{r}\left(e^{i \theta}\right)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t) P_{r}(\theta-t) d t
$$

we obtain

$$
\left|u_{r}\left(e^{i \theta}\right)\right|^{p} \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi}|f(t)|^{p} P_{r}(\theta-t) d t
$$

If we integrate (4) with respect to $\theta$, over $[-\pi, \pi]$ and use Fubini's theorem, we obtain (1).

Note that formula 11.5(3) was used twice in this argument.

To prove (2), choose $\epsilon>0$, and choose $g \in C(T)$ so that $\|g-f\|_{p}<\epsilon$ (Theorem 3.14). Let $v=P[g]$. Then

$$
u_{r}-f=\left(u_{r}-v_{r}\right)+\left(v_{r}-g\right)+(g-f)
$$

By (1), $\left\|u_{r}-v_{r}\right\|_{p}=\left\|(u-v)_{r}\right\|_{p} \leq\|f-g\|_{p}<\epsilon$. Thus

$$
\left\|u_{r}-f\right\|_{p} \leq 2 \epsilon+\left\|v_{r}-g\right\|_{p}
$$

for all $r<1$. Also, $\left\|v_{r}-g\right\|_{p} \leq\left\|v_{r}-g\right\|_{\infty}$, and the latter converges to 0 as $r \rightarrow 1$, by Theorem 11.8. This proves (2).

11.17 Poisson Integrals of Measures If $\mu$ is a complex measure on $T$, and if we want to replace integrals over $T$ by integrals over intervals of length $2 \pi$ in $R^{1}$, these intervals have to be taken half open, because of the possible presence of point masses in $\mu$. To avoid this (admittedly very minor) problem, we shall keep integration on the circle in what follows, and will write the Poisson integral $u=P[d \mu]$ of $\mu$ in the form

$$
u(z)=\int_{T} P\left(z, e^{i t}\right) d \mu\left(e^{i t}\right) \quad(z \in U)
$$

where $P\left(z, e^{i t}\right)=\left(1-|z|^{2}\right) /\left|e^{i t}-z\right|^{2}$, as in formula 11.5(6).

The reasoning that led to Theorem 11.7 applies without change to Poisson integrals of measures. Thus $u$, defined by (1), is harmonic in $U$.

Setting $\|\mu\|=|\mu|(T)$, the analogue of the first half of Theorem 11.16 is

$$
\left\|u_{r}\right\|_{1}=\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|u\left(r e^{i \theta}\right)\right| d \theta \leq\|\mu\|
$$

To see this, replace $\mu$ by $|\mu|$ in (1), apply Fubini's theorem, and refer to formula 11.5(3).

11.18 Approach Regions For $0<\alpha<1$, we define $\Omega_{\alpha}$ to be the union of the disc $D(0 ; \alpha)$ and the line segments from $z=1$ to points of $D(0 ; \alpha)$.

In other words, $\Omega_{\alpha}$ is the smallest convex open set that contains $D(0 ; \alpha)$ and has the point 1 in its boundary. Near $z=1, \Omega_{\alpha}$ is an angle, bisected by the radius of $U$ that terminates at 1 , of opening $2 \theta$, where $\alpha=\sin \theta$. Curves that approach 1 within $\Omega_{\alpha}$ cannot be tangent to $T$. Therefore $\Omega_{\alpha}$ is called a nontangential approach region, with vertex 1 .

The regions $\Omega_{\alpha}$ expand when $\alpha$ increases. Their union is $U$, their intersection is the radius $[0,1)$.

Rotated copies of $\Omega_{\alpha}$, with vertex at $e^{i t}$, will be denoted by $e^{i t} \Omega_{\alpha}$.

11.19 Maximal Functions If $0<\alpha<1$ and $u$ is any complex function with domain $U$, its nontangential maximal function $N_{\alpha} u$ is defined on $T$ by

$$
\left(N_{\alpha} u\right)\left(e^{i t}\right)=\sup \left\{|u(z)|: z \in e^{i t} \Omega_{\alpha}\right\} .
$$

Similarly, the radial maximal function of $u$ is

$$
\left(M_{\mathrm{rad}} u\right)\left(e^{i t}\right)=\sup \left\{\left|u\left(r e^{i t}\right)\right|: 0 \leq r<1\right\} .
$$

If $u$ is continuous and $\lambda$ is a positive number, then the set where either of these maximal functions is $\leq \lambda$ is a closed subset of $T$. Consequently, $N_{\alpha} u$ and $M_{\mathrm{rad}} u$ are lower semicontinuous on $T$; in particular, they are measurable.

Clearly, $M_{\mathrm{rad}} u \leq N_{\alpha} u$, and the latter increases with $\alpha$. If $u=P[d \mu]$, Theorem 11.20 will show that the size of $N_{\alpha} u$ is, in turn, controlled by the maximal function $M \mu$ that was defined in Sec. 7.2 (taking $k=1$ ). However, it will simplify the notation if we replace ordinary Lebesgue measure $m$ on $T$ by $\sigma=m / 2 \pi$. Then $\sigma$ is a rotation-invariant positive Borel measure on $T$, so normalized that $\sigma(T)=1$.

Accordingly, $M \mu$ is now defined by

$$
(M \mu)\left(e^{i \theta}\right)=\sup \frac{|\mu|(I)}{\sigma(I)}
$$

The supremum is taken over all open arcs $I \subset T$ whose centers are at $e^{i \theta}$, including $T$ itself (even though $T$ is of course not an arc).

Similarly, the derivative $D \mu$ of a measure $\mu$ on $T$ is now

$$
(D \mu)\left(e^{i \theta}\right)=\lim \frac{\mu(I)}{\sigma(I)}
$$

as the open arcs $I \subset T$ shrink to their center $e^{i \theta}$, and $e^{i \theta}$ is a Lebesgue point of $f \in L^{1}(T)$ if

$$
\lim \frac{1}{\sigma(I)} \int_{I}\left|f-f\left(e^{i \theta}\right)\right| d \sigma=0
$$

where $\{I\}$ is as in (4).

If $d \mu=f d \sigma+d \mu_{s}$ is the Lebesgue decomposition of a complex Borel measure $\mu$ on $T$, where $f \in L^{1}(T)$ and $\mu_{s} \perp \sigma$, Theorems 7.4, 7.7, and 7.14 assert that

$$
\sigma\{M \mu>\lambda\} \leq \frac{3}{\lambda}\|\mu\|,
$$

that almost every point of $T$ is a Lebesgue point of $f$, and that $D \mu=f, D \mu_{s}=0$ a.e. $[\sigma]$.

We will now see, for any complex Borel measure $\mu$ on $T$, that the nontangential and radial maximal functions of the harmonic function $P[d \mu]$ are controlled by $M \mu$. In fact, if any one of them is finite at some point of $T$, so are the others; this can be seen by combining Theorem 11.20 with Exercise 19.

11.20 Theorem Assume $0<\alpha<1$. Then there is a constant $c_{\alpha}>0$ with the following property: If $\mu$ is a positive finite Borel measure on $T$ and $u=P[d \mu]$ is its Poisson integral, then the inequalities

$$
c_{\alpha}\left(N_{\alpha} u\right)\left(e^{i \theta}\right) \leq\left(M_{\mathrm{rad}} u\right)\left(e^{i \theta}\right) \leq(M \mu)\left(e^{i \theta}\right)
$$

hold at every point $e^{i \theta} \in T$.

Proof We shall prove (1) for $\theta=0$. The general case follows then if the special case is applied to the rotated measure $\mu_{\theta}(E)=\mu\left(e^{i \theta} E\right)$.

Since $u(z)=\int_{T} P\left(z, e^{i t}\right) d \mu\left(e^{i t}\right)$, the first inequality in (1) will follow if we can show that

$$
c_{\alpha} P\left(z, e^{i t}\right) \leq P\left(|z|, e^{i t}\right)
$$

holds for all $z \in \Omega_{\alpha}$ and all $e^{i t} \in T$. By formula 11.5(6), (2) is the same as

$$
c_{\alpha}\left|e^{i t}-r\right|^{2} \leq\left|e^{i t}-z\right|^{2}
$$

where $r=|z|$.

The definition of $\Omega_{\alpha}$ shows that $|z-r| /(1-r)$ is bounded in $\Omega_{\alpha}$, say by $\gamma_{\alpha}$. Hence

$$
\begin{aligned}
\left|e^{i t}-r\right| & \leq\left|e^{i t}-z\right|+|z-r| \\
& \leq\left|e^{i t}-z\right|+\gamma_{\alpha}(1-r) \leq\left(1+\gamma_{\alpha}\right)\left|e^{i t}-z\right|
\end{aligned}
$$

so that (3) holds with $c_{\alpha}=\left(1+\gamma_{\alpha}\right)^{-2}$. This proves the first half of (1).

For the second half, we have to prove that

$$
\int_{T} P_{r}(t) d \mu\left(e^{i t}\right) \leq(M \mu)(1) \quad(0 \leq r \leq 1)
$$

Fix $r$. Choose open arcs $I_{j} \subset T$, centered at 1 , so that $I_{1} \subset I_{2} \subset \cdots \subset I_{n-1}$, put $I_{n}=T$. For $1 \leq j \leq n$, let $\chi_{j}$ be the characteristic function of $I_{j}$, and let $h_{j}$ be the largest positive number for which $h_{j} \chi_{j} \leq P_{r}$ on $T$. Define

$$
K=\sum_{j=1}^{n}\left(h_{j}-h_{j+1}\right) \chi_{j}
$$

where $h_{n+1}=0$. Since $P_{r}(t)$ is an even function of $t$ that decreases as $t$ increases from 0 to $\pi$, we see that $h_{j}-h_{j+1} \geq 0$, that $K=h_{j}$ on $I_{j}-I_{j-1}$ (putting $I_{0}=\varnothing$ ), and that $K \leq P_{r}$. The definition of $M \mu$ shows that

$$
\mu\left(I_{j}\right) \leq(M \mu)(1) \sigma\left(I_{j}\right)
$$

Hence, setting $(M \mu)(1)=M$,

$$
\begin{aligned}
\int_{T} K d \mu & =\sum_{j=1}^{n}\left(h_{j}-h_{j+1}\right) \mu\left(I_{j}\right) \leq M \sum_{j=1}^{n}\left(h_{j}-h_{j+1}\right) \sigma\left(I_{j}\right) \\
& =M \int_{T} K d \sigma \leq M \int_{T} P_{r} d \sigma=M
\end{aligned}
$$

Finally, if we choose the $\operatorname{arcs} I_{j}$ so that their endpoints form a sufficiently fine partition of $T$, we obtain step functions $K$ that converge to $P_{r}$, uniformly on $T$. Hence (4) follows from (7).

11.21 Nontangential Limits A function $F$, defined in $U$, is said to have nontangential limit $\lambda$ at $e^{i \theta} \in T$ if, for each $\alpha<1$,

$$
\lim _{j \rightarrow \infty} F\left(z_{j}\right)=\lambda
$$

for every sequence $\left\{z_{j}\right\}$ that converges to $e^{i \theta}$ and that lies in $e^{i \theta} \Omega_{\alpha}$.

11.22 Theorem If $\mu$ is a positive Borel measure on $T$ and $(D \mu)\left(e^{i \theta}\right)=0$ for some $\theta$, then its Poisson integral $u=P[d \mu]$ has nontangential limit 0 at $e^{i \theta}$.

Proof By definition, the assumption $(D \mu)\left(e^{i \theta}\right)=0$ means that

$$
\lim \mu(I) / \sigma(I)=0
$$

as the open arcs $I \subset T$ shrink to their center $e^{i \theta}$. Pick $\epsilon>0$. One of these arcs, say $I_{0}$, is then small enough to ensure that

$$
\mu(I)<\epsilon \sigma(I)
$$

for every $I \subset I_{0}$ that has $e^{i \theta}$ as center.

Let $\mu_{0}$ be the restriction of $\mu$ to $I_{0}$, put $\mu_{1}=\mu-\mu_{0}$, and let $u_{i}$ be the Poisson integral of $\mu_{i}(i=0,1)$. Suppose $z_{j}$ converges to $e^{i \theta}$ within some region $e^{i \theta} \Omega_{\alpha}$. Then $z_{j}$ stays at a positive distance from $T-I_{0}$. The integrands in

$$
u_{1}\left(z_{j}\right)=\int_{T-I_{0}} P\left(z_{j}, e^{i t}\right) d \mu\left(e^{i t}\right)
$$

converge therefore to 0 as $j \rightarrow \infty$, uniformly on $T-I_{0}$. Hence

$$
\lim _{j \rightarrow \infty} u_{1}\left(z_{j}\right)=0
$$

Next, use (2) together with Theorem 11.20 to see that

$$
c_{\alpha}\left(N_{\alpha} u_{0}\right)\left(e^{i \theta}\right) \leq\left(M \mu_{0}\right)\left(e^{i \theta}\right) \leq \epsilon
$$

In $e^{i \theta} \Omega_{\alpha}, u_{0}(z) \leq\left(N_{\alpha} u_{0}\right)\left(e^{i \theta}\right)$. Hence (5) implies that

$$
\limsup _{j \rightarrow \infty} u_{0}\left(z_{j}\right) \leq \epsilon / c_{\alpha} .
$$

Since $u=u_{0}+u_{1}$ and $\epsilon$ was arbitrary, (4) and (6) give

$$
\lim _{j \rightarrow \infty} u\left(z_{j}\right)=0 .
$$

11.23 Theorem If $f \in L^{1}(T)$, then $P[f]$ has nontangential limit $f\left(e^{i \theta}\right)$ at every Lebesgue point $e^{i \theta}$ of $f$.

Proof Suppose $e^{i \theta}$ is a Lebesgue point of $f$. By subtracting a constant from $f$ we may assume, without loss of generality, that $f\left(e^{i \theta}\right)=0$. Then

$$
\lim \frac{1}{\sigma(I)} \int_{I}|f| d \sigma=0
$$

as the open arcs $I \subset T$ shrink to their center $e^{i \theta}$. Define a Borel measure $\mu$ on $T$ by

$$
\mu(E)=\int_{E}|f| d \sigma
$$

Then (1) says that $(D \mu)\left(e^{i \theta}\right)=0$; hence $P[d \mu]$ has nontangential limit 0 at $e^{i \theta}$, by Theorem 11.22. The same is true of $P[f]$, because

$$
|P[f]| \leq P[|f|]=P[d \mu] .
$$

The last two theorems can be combined as follows.

11.24 Theorem If $d \mu=f d \sigma+d \mu_{s}$ is the Lebesgue decomposition of a complex Borel measure $\mu$ on $T$, where $f \in L^{1}(T), \mu_{s} \perp \sigma$, then $P[d \mu]$ has nontangential limit $f\left(e^{i \theta}\right)$ at almost all points of $T$.

ProOF Apply Theorem 11.22 to the positive and negative variations of the real and imaginary parts of $\mu_{s}$, and apply Theorem 11.23 to $f$.

Here is another consequence of Theorem 11.20.

11.25 Theorem For $0<\alpha<1$ and $1 \leq p \leq \infty$, there are constants $A(\alpha, p)<\infty$ with the following properties:
(a) If $\mu$ is a complex Borel measure on $T$, and $u=P[d \mu]$, then

$$
\sigma\left\{N_{\alpha} u>\lambda\right\} \leq \frac{A(\alpha, 1)}{\lambda}\|\mu\| \quad(0<\lambda<\infty)
$$

(b) If $1<p \leq \infty, f \in L^{p}(T)$, and $u=P[f]$, then

$$
\left\|N_{\alpha} u\right\|_{p} \leq A(\alpha, p)\|f\|_{p}
$$

Proof Combine Theorem 11.20 with Theorem 7.4 and the inequality (7) in the proof of Theorem 8.18.

The nontangential maximal functions $N_{\alpha} u$ are thus in weak $L^{1}$ if $u=P[d \mu]$, and they are in $L^{p}(T)$ if $u=P[f]$ for some $f \in L^{p}(T), p>1$. This latter result may be regarded as a strengthened form of the first part of Theorem 11.16.

## Representation Theorems

11.26 How can one tell whether a harmonic function $u$ in $U$ is a Poisson integral or not? The preceding theorems (11.16 to 11.25$)$ contain a number of necessary conditions. It turns out that the simplest of these, the $L^{p}$-boundedness of the family $\left\{u_{r}: 0 \leq r<1\right\}$ is also sufficient! Thus, in particular, the boundedness of $\left\|u_{r}\right\|_{1}$, as $r \rightarrow 1$, implies the existence of nontangential limits a.e. on $T$, since, as we will see in Theorem 11.30, $u$ can then be represented as the Poisson integral of a measure.

This measure will be obtained as a so-called "weak limit" of the functions $u_{r}$. Weak convergence is an important topic in functional analysis. We will approach it through another important concept, called equicontinuity, which we will meet again later, in connection with the so-called "normal families" of holomorphic functions.

11.27 Definition Let $\mathscr{F}$ be a collection of complex functions on a metric space $X$ with metric $\rho$.

We say that $\mathscr{F}$ is equicontinuous if to every $\epsilon>0$ corresponds a $\delta>0$ such that $|f(x)-f(y)|<\epsilon$ for every $f \in \mathscr{F}$ and for all pairs of points $x, y$ with $\rho(x, y)<\delta$. (In particular, every $f \in \mathscr{F}$ is then uniformly continuous.)

We say that $\mathscr{F}$ is pointwise bounded if to every $x \in X$ corresponds an $M(x)<\infty$ such that $|f(x)| \leq M(x)$ for every $f \in \mathscr{F}$.

11.28 Theorem (Arzela-Ascoli) Suppose that $\mathscr{F}$ is a pointwise bounded equicontinuous collection of complex functions on a metric space $X$, and that $X$ contains a countable dense subset $E$.

Every sequence $\left\{f_{n}\right\}$ in $\mathscr{F}$ has then a subsequence that converges uniformly on every compact subset of $X$.

Proof Let $x_{1}, x_{2}, x_{3}, \ldots$ be an enumeration of the points of $E$. Let $S_{0}$ be the set of all positive integers. Suppose $k \geq 1$ and an infinite set $S_{k-1} \subset S_{0}$ has been chosen. Since $\left\{f_{n}\left(x_{k}\right): n \in S_{k-1}\right\}$ is a bounded sequence of complex numbers, it has a convergent subsequence. In other words, there is an infinite set $S_{k} \subset S_{k-1}$ so that $\lim f_{n}\left(x_{k}\right)$ exists as $n \rightarrow \infty$ within $S_{k}$.

Continuing in this way, we obtain infinite sets $S_{0} \supset S_{1} \supset S_{2} \supset \cdots$ with the property that $\lim f_{n}\left(x_{j}\right)$ exists, for $1 \leq j \leq k$, if $n \rightarrow \infty$ within $S_{k}$.

Let $r_{k}$ be the $k$ th term of $S_{k}$ (with respect to the natural order of the positive integers) and put

$$
S=\left\{r_{1}, r_{2}, r_{3}, \ldots\right\}
$$

For each $k$ there are then at most $k-1$ terms of $S$ that are not in $S_{k}$.

Hence $\lim f_{n}(x)$ exists, for every $x \in E$, as $n \rightarrow \infty$ within $S$.

(The construction of $S$ from $\left\{S_{k}\right\}$ is the so-called diagonal process.)

Now let $K \subset X$ be compact, pick $\epsilon>0$. By equicontinuity, there is a $\delta>0$ so that $\rho(p, q)<\delta$ implies $\left|f_{n}(p)-f_{n}(q)\right|<\epsilon$, for all $n$. Cover $K$ with open balls $B_{1}, \ldots, B_{M}$ of radius $\delta / 2$. Since $E$ is dense in $X$ there are points $p_{i} \in B_{i} \cap E$ for $1 \leq i \leq M$. Since $p_{i} \in E, \lim f_{n}\left(p_{i}\right)$ exists, as $n \rightarrow \infty$ within $S$. Hence there is an integer $N$ such that

$$
\left|f_{m}\left(p_{i}\right)-f_{n}\left(p_{i}\right)\right|<\epsilon
$$

for $i=1, \ldots, M$, if $m>N, n>N$, and $m$ and $n$ are in $S$.

To finish, pick $x \in K$. Then $x \in B_{i}$ for some $i$, and $\rho\left(x, p_{i}\right)<\delta$. Our choice of $\delta$ and $N$ shows that

$$
\begin{aligned}
\left|f_{m}(x)-f_{n}(x)\right| & \leq\left|f_{m}(x)-f_{m}\left(p_{i}\right)\right|+\left|f_{m}\left(p_{i}\right)-f_{n}\left(p_{i}\right)\right|+\left|f_{n}\left(p_{i}\right)-f_{n}(x)\right| \\
& <\epsilon+\epsilon+\epsilon=3 \epsilon
\end{aligned}
$$

if $m>N, n>N, m \in S, n \in S$.

### 11.29 Theorem Suppose that

(a) $X$ is a separable Banach space,

(b) $\left\{\Lambda_{n}\right\}$ is a sequence of linear functionals on $X$,

(c) $\sup \left\|\Lambda_{n}\right\|=M<\infty$.

Then there is a subsequence $\left\{\Lambda_{n_{i}}\right\}$ such that the limit

$$
\Lambda x=\lim _{i \rightarrow \infty} \Lambda_{n_{i}} x
$$

exists for every $x \in X$. Moreover, $\Lambda$ is linear, and $\|\Lambda\| \leq M$.

(In this situation, $\Lambda$ is said to be the weak limit of $\left\{\Lambda_{n_{i}}\right\}$; see Exercise 18.)

Proof To say that $X$ is separable means, by definition, that $X$ has a countable dense subset. The inequalities

$$
\left|\Lambda_{n} x\right| \leq M\|x\|, \quad\left|\Lambda_{n} x^{\prime}-\Lambda_{n} x^{\prime \prime}\right| \leq M\left\|x^{\prime}-x^{\prime \prime}\right\|
$$

show that $\left\{\Lambda_{n}\right\}$ is pointwise bounded and equicontinuous. Since each point of $X$ is a compact set, Theorem 11.28 implies that there is a subsequence $\left\{\Lambda_{n_{i}}\right\}$ such that $\left\{\Lambda_{n_{i}} x\right\}$ converges, for every $x \in X$, as $i \rightarrow \infty$. To finish, define $\Lambda$ by (1). It is then clear that $\Lambda$ is linear and that $\|\Lambda\| \leq M$.

Let us recall, for the application that follows, that $C(T)$ and $L^{p}(T)(p<\infty)$ are separable Banach spaces, because the trigonometric polynomials are dense in them, and because it is enough to confine ourselves to trigonometric polynomials whose coefficients lie in some prescribed countable dense subset of the complex field.

11.30 Theorem Suppose $u$ is harmonic in $U, 1 \leq p \leq \infty$, and

$$
\sup _{0<r<1}\left\|u_{r}\right\|_{p}=M<\infty
$$

(a) If $p=1$, it follows that there is a unique complex Borel measure $\mu$ on $T$ so that $u=P[d \mu]$.

(b) If $p>1$, it follows that there is a unique $f \in L^{p}(T)$ so that $u=P[f]$.

(c) Every positive harmonic function in $U$ is the Poisson integral of a unique positive Borel measure on $T$.

Proof Assume first that $p=1$. Define linear functionals $\Lambda_{r}$ on $C(T)$ by

$$
\Lambda_{r} g=\int_{T} g u_{r} d \sigma \quad(0 \leq r<1)
$$

By (1), $\left\|\Lambda_{r}\right\| \leq M$. By Theorems 11.29 and 6.19 there is a measure $\mu$ on $T$, with $\|\mu\| \leq M$, and a sequence $r_{j} \rightarrow 1$, so that

$$
\lim _{j \rightarrow \infty} \int_{T} g u_{r_{j}} d \sigma=\int_{T} g d \mu
$$

for every $g \in C(T)$.

Put $h_{j}(z)=u\left(r_{j} z\right)$. Then $h_{j}$ is harmonic in $U$, continuous on $\bar{U}$, and is therefore the Poisson integral of its restriction to $T$ (Theorem 11.9). Fix $z \in U$, and apply (3) with

$$
g\left(e^{i t}\right)=P\left(z, e^{i t}\right)
$$

Since $h_{j}\left(e^{i t}\right)=u_{r_{j}}\left(e^{i t}\right)$, we obtain

$$
\begin{aligned}
u(z) & =\lim _{j} u\left(r_{j} z\right)=\lim _{j} h_{j}(z) \\
& =\lim _{j} \int_{T} P\left(z, e^{i t}\right) h_{j}\left(e^{i t}\right) d \sigma\left(e^{i t}\right) \\
& =\int_{T} P\left(z, e^{i t}\right) d \mu\left(e^{i t}\right)=P[d \mu](z)
\end{aligned}
$$

If $1<p \leq \infty$, let $q$ be the exponent conjugate to $p$. Then $L^{q}(T)$ is separable. Define $\Lambda_{r}$ as in (2), but for all $g \in L^{q}(T)$. Again, $\left\|\Lambda_{r}\right\| \leq M$. Refer to Theorems 6.16 and 11.29 to deduce, as above, that there is an $f \in L^{p}(T)$, with $\|f\|_{p} \leq M$, so that (3) holds, with $f d \sigma$ in place of $d \mu$, for every $g \in L^{q}(T)$. The rest of the proof is as it was in the case $p=1$.

This establishes the existence assertions in $(a)$ and $(b)$. To prove uniqueness, it suffices to show that $P[d \mu]=0$ implies $\mu=0$.

Pick $f \in C(T)$, put $u=P[f], v=P[d \mu]$. By Fubini's theorem, and the symmetry $P\left(r e^{i \theta}, e^{i t}\right)=P\left(r e^{i t}, e^{i \theta}\right)$,

$$
\int_{T} u_{r} d \mu=\int_{T} v_{r} f d \sigma \quad(0 \leq r<1)
$$

When $v=0$ then $v_{r}=0$, and since $u_{r} \rightarrow f$ uniformly, as $r \rightarrow 1$, we conclude that

$$
\int_{T} f d \mu=0
$$

for every $f \in C(T)$ if $P[d \mu]=0$. By Theorem 6.19, (6) implies that $\mu=0$.

Finally, $(c)$ is a corollary of $(a)$, since $u>0$ implies (1) with $p=1$ :

$$
\int_{T}\left|u_{r}\right| d \sigma=\int_{T} u_{r} d \sigma=u(0) \quad(0 \leq r<1)
$$

by the mean value property of harmonic functions. The functionals $\Lambda_{r}$ used in the proof of $(a)$ are now positive, hence $\mu \geq 0$.

11.31 Since holomorphic functions are harmonic, all of the preceding results (of which Theorems 11.16, 11.24, 11.25, 11.30 are the most significant) apply to holomorphic functions in $U$. This leads to the study of the $H^{p}$-spaces, a topic that will be taken up in Chap. 17.

At present we shall only give one application, to functions in the space $H^{\infty}$. This, by definition, is the space of all bounded holomorphic functions in $U$; the norm

$$
\|f\|_{\infty}=\sup \{|f(z)|: z \in U\}
$$

turns $H^{\infty}$ into a Banach space.

As before, $L^{\infty}(T)$ is the space of all (equivalence classes of) essentially bounded functions on $T$, normed by the essential supremum norm, relative to Lebesgue measure. For $g \in L^{\infty}(T)$, $\|g\|_{\infty}$ stands for the essential supremum of $|g|$.

11.32 Theorem To every $f \in H^{\infty}$ corresponds a function $f^{*} \in L^{\infty}(T)$, defined almost everywhere by

$$
f^{*}\left(e^{i \theta}\right)=\lim _{r \rightarrow 1} f\left(r e^{i \theta}\right)
$$

The equality $\|f\|_{\infty}=\left\|f^{*}\right\|_{\infty}$ holds. $z \in U$.

If $f^{*}\left(e^{i \theta}\right)=0$ for almost all $e^{i \theta}$ on some arc $I \subset T$, then $f(z)=0$ for every

(A considerably stronger uniqueness theorem will be obtained later, in Theorem 15.19. See also Theorem 17.18 and Sec. 17.19.)

Proof By Theorem 11.30, there is a unique $g \in L^{\infty}(T)$ such that $f=P[g]$. By Theorem 11.23, (1) holds with $f^{*}=g$. The inequality $\|f\|_{\infty} \leq\left\|f^{*}\right\|_{\infty}$ follows from Theorem 11.16(1); the opposite inequality is obvious.

In particular, if $f^{*}=0$ a.e., then $\left\|f^{*}\right\|_{\infty}=0$, hence $\|f\|_{\infty}=0$, hence $f=0$.

Now choose a positive integer $n$ so that the length of $I$ is larger than $2 \pi / n$. Let $\alpha=\exp \{2 \pi i / n\}$ and define

$$
F(z)=\prod_{k=1}^{n} f\left(\alpha^{k} z\right) \quad(z \in U)
$$

Then $F \in H^{\infty}$ and $F^{*}=0$ a.e. on $T$, hence $F(z)=0$ for all $z \in U$. If $Z(f)$, the zero set of $f$ in $U$, were at most countable, the same would be true of $Z(F)$, since $Z(F)$ is the union of $n$ sets obtained from $Z(f)$ by rotations. But $Z(F)=U$. Hence $f=0$, by Theorem 10.18 .

## Exercises

1 Suppose $u$ and $v$ are real harmonic functions in a plane region $\Omega$. Under what conditions is $u v$ harmonic? (Note that the answer depends strongly on the fact that the question is one about real functions.) Show that $u^{2}$ cannot be harmonic in $\Omega$, unless $u$ is constant. For which $f \in H(\Omega)$ is $|f|^{2}$ harmonic?

2 Suppose $f$ is a complex function in a region $\Omega$, and both $f$ and $f^{2}$ are harmonic in $\Omega$. Prove that either $f$ or $\bar{f}$ is holomorphic in $\Omega$.

3 If $u$ is a harmonic function in a region $\Omega$, what can you say about the set of points at which the gradient of $u$ is 0 ? (This is the set on which $u_{x}=u_{y}=0$.)

4 Prove that every partial derivative of every harmonic function is harmonic.

Verify, by direct computation, that $P_{r}(\theta-t)$ is, for each fixed $t$, a harmonic function of $r e^{i \theta}$. Deduce (without referring to holomorphic functions) that the Poisson integral $P[d \mu]$ of every finite Borel measure $\mu$ on $T$ is harmonic in $U$, by showing that every partial derivative of $P[d \mu]$ is equal to the integral of the corresponding partial derivative of the kernel.

5 Suppose $f \in H(\Omega)$ and $f$ has no zero in $\Omega$. Prove that $\log |f|$ is harmonic in $\Omega$, by computing its Laplacian. Is there an easier way?

6 Suppose $f \in H(U)$, where $U$ is the open unit disc, $f$ is one-to-one in $U, \Omega=f(U)$, and $f(z)=\sum c_{n} z^{n}$. Prove that the area of $\Omega$ is

$$
\pi \sum_{n=1}^{\infty} n\left|c_{n}\right|^{2}
$$

Hint: The Jacobian of $f$ is $\left|f^{\prime}\right|^{2}$.

7 (a) If $f \in H(\Omega), f(z) \neq 0$ for $z \in \Omega$, and $-\infty<\alpha<\infty$, prove that

$$
\Delta\left(|f|^{\alpha}\right)=\alpha^{2}|f|^{\alpha-2}\left|f^{\prime}\right|^{2}
$$

by proving the formula

$$
\partial \bar{\partial}(\psi \circ(\bar{f}))=\left(\varphi \circ|f|^{2}\right) \cdot\left|f^{\prime}\right|^{2},
$$

in which $\psi$ is twice differentiable on $(0, \infty)$ and

$$
\varphi(t)=t \psi^{\prime \prime}(t)+\psi^{\prime}(t)
$$

(b) Assume $f \in H(\Omega)$ and $\Phi$ is a complex function with domain $f(\Omega)$, which has continuous second-order partial derivatives. Prove that

$$
\Delta[\Phi \circ f]=[(\Delta \Phi) \circ f] \cdot\left|f^{\prime}\right|^{2}
$$

Show that this specializes to the result of $(a)$ if $\Phi(w)=\Phi(|w|)$.

8 Suppose $\Omega$ is a region, $f_{n} \in H(\Omega)$ for $n=1,2,3, \ldots, u_{n}$ is the real part of $f_{n},\left\{u_{n}\right\}$ converges uniformly on compact subsets of $\Omega$, and $\left\{f_{n}(z)\right\}$ converges for at least one $z \in \Omega$. Prove that then $\left\{f_{n}\right\}$ converges uniformly on compact subsets of $\Omega$.

9 Suppose $u$ is a Lebesgue measurable function in a region $\Omega$, and $u$ is locally in $L^{1}$. This means that the integral of $|u|$ over any compact subset of $\Omega$ is finite. Prove that $u$ is harmonic if it satisfies the following form of the mean value property:

$$
u(a)=\frac{1}{\pi r^{2}} \iint_{D(a ; r)} u(x, y) d x d y
$$

whenever $\bar{D}(a ; r) \subset \Omega$.

10 Suppose $I=[a, b]$ is an interval on the real axis, $\varphi$ is a continuous function on $I$, and

$$
f(z)=\frac{1}{2 \pi i} \int_{a}^{b} \frac{\varphi(t)}{t-z} d t \quad(z \notin I)
$$

Show that

$$
\lim _{\epsilon \rightarrow 0}[f(x+i \epsilon)-f(x-i \epsilon)] \quad(\epsilon>0)
$$

exists for every real $x$, and find it in terms of $\varphi$.

How is the result affected if we assume merely that $\varphi \in L^{1}$ ? What happens then at points $x$ at which $\varphi$ has right- and left-hand limits?

11 Suppose that $I=[a, b], \Omega$ is a region, $I \subset \Omega, f$ is continuous in $\Omega$, and $f \in H(\Omega-I)$. Prove that actually $f \in H(\Omega)$.

Replace $I$ by some other sets for which the same conclusion can be drawn.

12 (Harnack's Inequalities) Suppose $\Omega$ is a region, $K$ is a compact subset of $\Omega, z_{0} \in \Omega$. Prove that there exist positive numbers $\alpha$ and $\beta$ (depending on $z_{0}, K$, and $\Omega$ ) such that

$$
\alpha u\left(z_{0}\right) \leq u(z) \leq \beta u\left(z_{0}\right)
$$

for every positive harmonic function $u$ in $\Omega$ and for all $z \in K$.

If $\left\{u_{n}\right\}$ is a sequence of positive harmonic functions in $\Omega$ and if $u_{n}\left(z_{0}\right) \rightarrow 0$, describe the behavior of $\left\{u_{n}\right\}$ in the rest of $\Omega$. Do the same if $u_{n}\left(z_{0}\right) \rightarrow \infty$. Show that the assumed positivity of $\left\{u_{n}\right\}$ is essential for these results.

13 Suppose $u$ is a positive harmonic function in $U$ and $u(0)=1$. How large can $u\left(\frac{1}{2}\right)$ be? How small? Get the best possible bounds.

14 For which pairs of lines $L_{1}, L_{2}$ do there exist real functions, harmonic in the whole plane, that are 0 at all points of $L_{1} \cup L_{2}$ without vanishing identically?

15 Suppose $u$ is a positive harmonic function in $U$, and $u\left(r e^{i \theta}\right) \rightarrow 0$ as $r \rightarrow 1$, for every $e^{i \theta} \neq 1$. Prove that there is a constant $c$ such that

$$
u\left(r e^{i \theta}\right)=c P_{r}(\theta) .
$$

16 Here is an example of a harmonic function in $U$ which is not identically 0 but all of whose radial limits are 0 :

$$
u(z)=\operatorname{Im}\left[\left(\frac{1+z}{1-z}\right)^{2}\right]
$$

Prove that this $u$ is not the Poisson integral of any measure on $T$ and that it is not the difference of two positive harmonic functions in $U$.

17 Let $\Phi$ be the set of all positive harmonic functions $u$ in $U$ such that $u(0)=1$. Show that $\Phi$ is a convex set and find the extreme points of $\Phi$. (A point $x$ in a convex set $\Phi$ is called an extreme point of $\Phi$ if $x$ lies on no segment both of whose end points lie in $\Phi$ and are different from $x$.) Hint: If $C$ is the convex set whose members are the positive Borel measures on $T$, of total variation 1 , show that the extreme points of $C$ are precisely those $\mu \in C$ whose supports consist of only one point of $T$.

18 Let $X^{*}$ be the dual space of the Banach space $X$. A sequence $\left\{\Lambda_{n}\right\}$ in $X^{*}$ is said to converge weakly to $\Lambda \in X^{*}$ if $\Lambda_{n} x \rightarrow \Lambda x$ as $n \rightarrow \infty$, for every $x \in X$. Note that $\Lambda_{n} \rightarrow \Lambda$ weakly whenever $\Lambda_{n} \rightarrow \Lambda$ in the norm of $X^{*}$. (See Exercise 8, Chap. 5.) The converse need not be true. For example, the functionals $f \rightarrow \hat{f}(n)$ on $L^{2}(T)$ tend to 0 weakly (by the Bessel inequality), but each of these functionals has norm 1.

Prove that $\left\{\left\|\Lambda_{n}\right\|\right\}$ must be bounded if $\left\{\Lambda_{n}\right\}$ converges weakly.

19 (a) Show that $\delta P_{r}(\delta)>1$ if $\delta=1-r$.

(b) If $\mu \geq 0, u=P[d \mu]$, and $I_{\delta} \subset T$ is the arc with center 1 and length $2 \delta$, show that

$$
\mu\left(I_{\delta}\right) \leq \delta u(1-\delta)
$$

and that therefore

$$
(M \mu)(1) \leq \pi\left(M_{\mathrm{rad}} u\right)(1)
$$

(c) If, furthermore, $\mu \perp m$, show that

$$
u\left(r e^{i \theta}\right) \rightarrow \infty \quad \text { a.e. }[\mu] .
$$

Hint: Use Theorem 7.15.

20 Suppose $E \subset T, m(E)=0$. Prove that there is an $f \in H^{\infty}$, with $f(0)=1$, that has

$$
\lim _{r \rightarrow 1} f\left(r e^{i \theta}\right)=0
$$

at every $e^{i \theta} \in E$.

Suggestion: Find a lower semicontinuous $\psi \in L^{1}(T), \psi>0, \psi=+\infty$ at every point of $E$. There is a holomorphic $g$ whose real part is $P[\psi]$. Let $f=1 / g$.

21 Define $f \in H(U)$ and $g \in H(U)$ by $f(z)=\exp \{(1+z) /(1-z)\}, g(z)=(1-z) \exp \{-f(z)\}$. Prove that

$$
g^{*}\left(e^{i \theta}\right)=\lim _{r \rightarrow 1} g\left(r e^{i \theta}\right)
$$

exists at every $e^{i \theta} \in T$, that $g^{*} \in C(T)$, but that $g$ is not in $H^{\infty}$.

Suggestion: Fix $s$, put

$$
z_{t}=\frac{t+i s-1}{t+i s+1} \quad(0<t<\infty)
$$

For certain values of $s,\left|g\left(z_{t}\right)\right| \rightarrow \infty$ as $t \rightarrow \infty$.

22 Suppose $u$ is harmonic in $U$, and $\left\{u_{r}: 0 \leq r<1\right\}$ is a uniformly integrable subset of $L^{1}(T)$. (See Exercise 10, Chap. 6.) Modify the proof of Theorem 11.30 to show that $u=P[f]$ for some $f \in L^{1}(T)$.

23 Put $\theta_{n}=2^{-n}$ and define

$$
u(z)=\sum_{n=1}^{\infty} n^{-2}\left\{P\left(z, e^{i \theta_{n}}\right)-P\left(z, e^{-i \theta_{n}}\right)\right\}
$$

for $z \in U$. Show that $u$ is the Poisson integral of a measure on $T$, that $u(x)=0$ if $-1<x<1$, but that

$$
u(1-\epsilon+i \epsilon)
$$

is unbounded, as $\epsilon$ decreases to 0 . (Thus $u$ has a radial limit, but no nontangential limit, at 1.)

Hint: If $\epsilon=\sin \theta$ is small and $z=1-\epsilon+i \epsilon$, then

$$
P\left(z, e^{i \theta}\right)-P\left(z, e^{-i \theta}\right)>1 / \epsilon
$$

24 Let $D_{n}(t)$ be the Dirichlet kernel, as in Sec. 5.11, define the Fejér kernel by

$$
K_{N}=\frac{1}{N+1}\left(D_{0}+D_{1}+\cdots+D_{N}\right)
$$

put $L_{N}(t)=\min \left(N, \pi^{2} / N t^{2}\right)$. Prove that

$$
K_{N-1}(t)=\frac{1}{N} \cdot \frac{1-\cos N t}{1-\cos t} \leq L_{N}(t)
$$

and that $\int_{T} L_{N} d \sigma \leq 2$.

Use this to prove that the arithmetic means

$$
\sigma_{N}=\frac{S_{0}+S_{1}+\cdots+S_{N}}{N+1}
$$

of the partial sums $s_{n}$ of the Fourier series of a function $f \in L^{1}(T)$ converge to $f\left(e^{i \theta}\right)$ at every Lebesgue point of $f$. (Show that sup $\left|\sigma_{N}\right|$ is dominated by $M f$, then proceed as in the proof of Theorem 11.23.) 25 If $1 \leq p \leq \infty$ and $f \in L^{p}\left(R^{1}\right)$, prove that $\left(f * h_{\lambda}\right)(x)$ is a harmonic function of $x+i \lambda$ in the upper half plane. ( $h_{\lambda}$ is defined in Sec. 9.7; it is the Poisson kernel for the half plane.)

## THE MAXIMUM MODULUS PRINCIPLE

## Introduction

12.1 The maximum modulus theorem (10.24) asserts that the constants are the only homomorphic functions in a region $\Omega$ whose absolute values have a local maximum at any point of $\Omega$.

Here is a restatement: If $K$ is the closure of a bounded region $\Omega$, if $f$ is continuous on $K$ and holomorphic in $\Omega$, then

$$
|f(z)| \leq\|f\|_{\partial \Omega}
$$

for every $z \in \Omega$. If equality holds at one point $z \in \Omega$, then $f$ is constant.

[The right side of (1) is the supremum of $|f|$ on the boundary $\partial \Omega$ of $\Omega$.]

For if $|f(z)| \geq\|f\|_{\partial \Omega}$ at some $z \in \Omega$, then the maximum of $|f|$ on $K$ (which is attained at some point of $K$, since $K$ is compact) is actually attained at some point of $\Omega$, so $f$ is constant, by Theorem 10.24.

The equality $\|f\|_{\infty}=\left\|f^{*}\right\|_{\infty}$, which is part of Theorem 11.32, implies that

$$
|f(z)| \leq\left\|f^{*}\right\|_{\infty} \quad\left(z \in U, f \in H^{\infty}(U)\right)
$$

This says (roughly speaking) that $|f(z)|$ is no larger than the supremum of the boundary values of $f$, a statement similar to (1). But this time boundedness on $U$ is enough; we do not need continuity on $\bar{U}$.

This chapter contains further generalizations of the maximum modulus theorem, as well as some rather striking applications of it, and it concludes with a theorem which shows that the maximum property "almost" characterizes the class of holomorphic functions.

## The Schwarz Lemma

This is the name usually given to the following theorem. We use the notation established in Sec. 11.31.

12.2 Theorem Suppose $f \in H^{\infty},\|f\|_{\infty} \leq 1$, and $f(0)=0$. Then

$$
\begin{aligned}
|f(z)| & \leq|z| \quad(z \in U) \\
\left|f^{\prime}(0)\right| & \leq 1
\end{aligned}
$$

if equality holds in (1) for one $z \in U-\{0\}$, or if equality holds in (2), then $f(z)=\lambda z$, where $\lambda$ is a constant,$|\lambda|=1$.

In geometric language, the hypothesis is that $f$ is a holomorphic mapping of $U$ into $U$ which keeps the origin fixed; part of the conclusion is that either $f$ is a rotation or $f$ moves each $z \in U-\{0\}$ closer to the origin than it was.

PROOF Since $f(0)=0, f(z) / z$ has a removable singularity at $z=0$. Hence there exists $g \in H(U)$ such that $f(z)=z g(z)$. If $z \in U$ and $|z|<r<1$, then

$$
|g(z)| \leq \max _{\theta} \frac{\left|f\left(r e^{i \theta}\right)\right|}{r} \leq \frac{1}{r}
$$

Letting $r \rightarrow 1$, we see that $|g(z)| \leq 1$ at every $z \in U$. This gives (1). Since $f^{\prime}(0)=g(0)$, (2) follows. If $|g(z)|=1$ for some $z \in U$, then $g$ is constant, by another application of the maximum modulus theorem.

Many variants of the Schwarz lemma can be obtained with the aid of the following mappings of $U$ onto $U$ :

12.3 Definition For any $\alpha \in U$, define

$$
\varphi_{\alpha}(z)=\frac{z-\alpha}{1-\bar{\alpha} z}
$$

12.4 Theorem Fix $\alpha \in U$. Then $\varphi_{\alpha}$ is a one-to-one mapping which carries $T$ onto $T, U$ onto $U$, and $\alpha$ to 0 . The inverse of $\varphi_{\alpha}$ is $\varphi_{-\alpha}$. We have

$$
\varphi_{\alpha}^{\prime}(0)=1-|\alpha|^{2}, \quad \varphi_{\alpha}^{\prime}(\alpha)=\frac{1}{1-|\alpha|^{2}}
$$

ProOF $\varphi_{\alpha}$ is holomorphic in the whole plane, except for a pole at $1 / \bar{\alpha}$ which lies outside $\bar{U}$. Straightforward substitution shows that

$$
\varphi_{-\alpha}\left(\varphi_{\alpha}(z)\right)=z
$$

Thus $\varphi_{\alpha}$ is one-to-one, and $\varphi_{-\alpha}$ is its inverse. Since, for real $t$,

$$
\left|\frac{e^{i t}-\alpha}{1-\bar{\alpha} e^{i t}}\right|=\frac{\left|e^{i t}-\alpha\right|}{\left|e^{-i t}-\bar{\alpha}\right|}=1
$$

( $z$ and $\bar{z}$ have the same absolute value), $\varphi_{\alpha}$ maps $T$ into $T$; the same is true of $\varphi_{-\alpha} ;$ hence $\varphi_{\alpha}(T)=T$. It now follows from the maximum modulus theorem that $\varphi_{\alpha}(U) \subset U$, and consideration of $\varphi_{-\alpha}$ shows that actually $\varphi_{\alpha}(U)=U$. ////

12.5 An Extremal Problem Suppose $\alpha$ and $\beta$ are complex numbers, $|\alpha|<1$, and $|\beta|<1$. How large can $\left|f^{\prime}(\alpha)\right|$ be if $f$ is subject to the conditions $f \in H^{\infty},\|f\|_{\infty} \leq 1$, and $f(\alpha)=\beta$ ?

To solve this, put

$$
g=\varphi_{\beta} \circ f \circ \varphi_{-\alpha} .
$$

Since $\varphi_{-\alpha}$ and $\varphi_{\beta}$ map $U$ onto $U$, we see that $g \in H^{\infty}$ and $\|g\|_{\infty} \leq 1$; also, $g(0)=0$. The passage from $f$ to $g$ has reduced our problem to the Schwarz lemma, which gives $\left|g^{\prime}(0)\right| \leq 1$. By (1), the chain rule gives

$$
g^{\prime}(0)=\varphi_{\beta}^{\prime}(\beta) f^{\prime}(\alpha) \varphi_{-\alpha}^{\prime}(0)
$$

If we use Eqs. 12.4(1), we obtain the inequality

$$
\left|f^{\prime}(\alpha)\right| \leq \frac{1-|\beta|^{2}}{1-|\alpha|^{2}}
$$

This solves our problem, since equality can occur in (3). This happens if and only if $\left|g^{\prime}(0)\right|=1$, in which case $g$ is a rotation (Theorem 12.2), so that

$$
f(z)=\varphi_{-\beta}\left(\lambda \varphi_{\alpha}(z)\right) \quad(z \in U)
$$

for some constant $\lambda$ with $|\lambda|=1$.

A remarkable feature of the solution should be stressed. We imposed no smoothness conditions (such as continuity on $\bar{U}$, for instance) on the behavior of $f$ near the boundary of $U$. Nevertheless, it turns out that the functions $f$ which maximize $\left|f^{\prime}(\alpha)\right|$ under the stated restrictions are actually rational functions. Note also that these extremal functions map $U$ onto $U$ (not just into) and that they are one-to-one. This observation may serve as the motivation for the proof of the Riemann mapping theorem in Chap. 14.

At present, we shall merely show how this extremal problem can be used to characterize the one-to-one holomorphic mappings of $U$ onto $U$.

12.6 Theorem Suppose $f \in H(U), f$ is one-to-one, $f(U)=U, \alpha \in U$, and $f(\alpha)=0$. Then there is a constant $\lambda,|\lambda|=1$, such that

$$
f(z)=\lambda \varphi_{\alpha}(z) \quad(z \in U) .
$$

In other words, we obtain $f$ by composing the mapping $\varphi_{\alpha}$ with a rotation.

ProOF Let $g$ be the inverse of $f$, defined by $g(f(z))=z, z \in U$. Since $f$ is oneto-one, $f^{\prime}$ has no zero in $U$, so $g \in H(U)$, by Theorem 10.33. By the chain rule,

$$
g^{\prime}(0) f^{\prime}(\alpha)=1
$$

The solution of 12.5 , applied to $f$ and to $g$, yields the inequalities

$$
\left|f^{\prime}(\alpha)\right| \leq \frac{1}{1-|\alpha|^{2}}, \quad\left|g^{\prime}(0)\right| \leq 1-|\alpha|^{2}
$$

By (2), equality must hold in (3). As we observed in the preceding problem (with $\beta=0$ ), this forces $f$ to satisfy (1).

## The Phragmen-Lindelöf Method

12.7 For a bounded region $\Omega$, we saw in Sec. 12.1 that if $f$ is continuous on the closure of $\Omega$ and if $f \in H(\Omega)$, the maximum modulus theorem implies

$$
\|f\|_{\Omega}=\|f\|_{\partial \Omega}
$$

For unbounded regions, this is no longer true.

To see an example, let

$$
\Omega=\left\{z=x+i y:-\frac{\pi}{2}<y<\frac{\pi}{2}\right\}
$$

$\Omega$ is the open strip bounded by the parallel lines $y= \pm \pi / 2$; its boundary $\partial \Omega$ is the union of these two lines. Put

$$
f(z)=\exp (\exp (z))
$$

For real $x$,

$$
f\left(x \pm \frac{\pi i}{2}\right)=\exp \left( \pm i e^{x}\right)
$$

since $\exp (\pi i / 2)=i$, so $|f(z)|=1$ for $z \in \partial \Omega$. But $f(z) \rightarrow \infty$ very rapidly as $x \rightarrow \infty$ along the positive real axis, which lies in $\Omega$.

"Very" is the key word in the preceding sentence. A method developed by Phragmen and Lindelöf makes it possible to prove theorems of the following kind: If $f \in H(\Omega)$ and if $|f|<g$, where $g(z) \rightarrow \infty$ "slowly" as $z \rightarrow \infty$ in $\Omega$ (just what "slowly" means depends on $\Omega$ ), then $f$ is actually bounded in $\Omega$, and this usually implies further conclusions about $f$, by the maximum modulus theorem.

Rather than describe the method by a theorem which would cover a large number of situations, we shall show how it works in two cases. In both, $\Omega$ will be a strip. In the first, $f$ will be assumed to be bounded, and the theorem will improve the bound; in the second, a growth condition will be imposed on $f$ which just excludes the function (3). In view of later applications, $\Omega$ will be a vertical strip in Theorem 12.8 .

First, however, let us mention another example which also has this general flavor: Suppose $f$ is an entire function and

$$
|f(z)|<1+|z|^{1 / 2}
$$

for all $z$. Then $f$ is constant.

This follows immediately from the Cauchy estimates 10.26 , since they show that $f^{(n)}(0)=0$ for $n=1,2,3, \ldots$

12.8 Theorem Suppose

$$
\Omega=\{x+i y: a<x<b\}, \quad \bar{\Omega}=\{x+i y: a \leq x \leq b\}
$$

$f$ is continuous on $\bar{\Omega}, f \in H(\Omega)$, and suppose that $|f(z)|<B$ for all $z \in \Omega$ and some fixed $B<\infty$. If

$$
M(x)=\sup \{|f(x+i y)|:-\infty<y<\infty\} \quad(a \leq x \leq b)
$$

then we actually have

$$
M(x)^{b-a} \leq M(a)^{b-x} M(b)^{x-a} \quad(a<x<b)
$$

Note: The conclusion (3) implies that the inequality $|f|<B$ can be replaced by $|f| \leq \max (M(a), M(b))$, so that $|f|$ is no larger in $\Omega$ than the supremum of $|f|$ on the boundary of $\Omega$.

If we apply the theorem to strips bounded by lines $x=\alpha$ and $x=\beta$, where $a \leq \alpha<\beta \leq b$, the conclusion can be stated in the following way:

Corollary Under the hypotheses of the theorem, $\log M$ is a convex function on $(a, b)$.

Proof We assume first that $M(a)=M(b)=1$. In this case we have to prove that $|f(z)| \leq 1$ for all $z \in \Omega$.

For each $\epsilon>0$, we define an auxiliary function

$$
h_{\epsilon}(z)=\frac{1}{1+\epsilon(z-a)} \quad(z \in \bar{\Omega})
$$

Since $\operatorname{Re}\{1+\epsilon(z-a)\}=1+\epsilon(x-a) \geq 1$ in $\bar{\Omega}$, we have $\left|h_{\epsilon}\right| \leq 1$ in $\bar{\Omega}$, so that

$$
\left|f(z) h_{\epsilon}(z)\right| \leq 1 \quad(z \in \partial \Omega)
$$

Also, $|1+\epsilon(z-a)| \geq \epsilon|y|$, so that

$$
\left|f(z) h_{\epsilon}(z)\right| \leq \frac{B}{\epsilon|y|} \quad(z=x+i y \in \bar{\Omega})
$$

Let $R$ be the rectangle cut off from $\bar{\Omega}$ by the lines $y= \pm B / \epsilon$. By (5) and (6), $\left|f h_{\epsilon}\right| \leq 1$ on $\partial R$, hence $\left|f h_{\epsilon}\right| \leq 1$ on $R$, by the maximum modulus theorem. But (6) shows that $\left|f h_{\epsilon}\right| \leq 1$ on the rest of $\bar{\Omega}$. Thus $\left|f(z) h_{\epsilon}(z)\right| \leq 1$
for all $z \in \Omega$ and all $\epsilon>0$. If we fix $z \in \Omega$ and then let $\epsilon \rightarrow 0$, we obtain the desired result $|f(z)| \leq 1$.

We now turn to the general case. Put

$$
g(z)=M(a)^{(b-z) /(b-a)} M(b)^{(z-a) /(b-a)}
$$

where, for $M>0$ and $w$ complex, $M^{w}$ is defined by

$$
M^{w}=\exp (w \log M)
$$

and $\log M$ is real. Then $g$ is entire, $g$ has no zero, $1 / g$ is bounded in $\bar{\Omega}$,

$$
|g(a+i y)|=M(a), \quad|g(b+i y)|=M(b)
$$

and hence $f / g$ satisfies our previous assumptions. Thus $|f / g| \leq 1$ in $\Omega$, and this gives (3). (See Exercise 7.)

12.9 Theorem Suppose

$$
\Omega=\left\{x+i y:|y|<\frac{\pi}{2}\right\}, \quad \bar{\Omega}=\left\{x+i y:|y| \leq \frac{\pi}{2}\right\} .
$$

Suppose $f$ is continuous on $\bar{\Omega}, f \in H(\Omega)$, there are constants $\alpha<1, A<\infty$, such that

$$
|f(z)|<\exp \{A \exp (\alpha|x|)\} \quad(z=x+i y \in \Omega)
$$

and

$$
\left|f\left(x \pm \frac{\pi i}{2}\right)\right| \leq 1 \quad(-\infty<x<\infty)
$$

Then $|f(z)| \leq 1$ for all $z \in \Omega$.

Note that the conclusion does not follow if $\alpha=1$, as is shown by the function $\exp (\exp z)$.

Proof Choose $\beta>0$ so that $\alpha<\beta<1$. For $\epsilon>0$, define

$$
h_{\epsilon}(z)=\exp \left\{-\epsilon\left(e^{\beta z}+e^{-\beta z}\right)\right\}
$$

For $z \in \bar{\Omega}$,

$$
\operatorname{Re}\left[e^{\beta z}+e^{-\beta z}\right]=\left(e^{\beta x}+e^{-\beta x}\right) \cos \beta y \geq \delta\left(e^{\beta x}+e^{-\beta x}\right)
$$

where $\delta=\cos (\beta \pi / 2)>0$, since $|\beta|<1$. Hence

$$
\left|h_{\epsilon}(z)\right| \leq \exp \left\{-\epsilon \delta\left(e^{\beta x}+e^{-\beta x}\right)\right\}<1 \quad(z \in \bar{\Omega}) .
$$

It follows that $\left|f h_{\epsilon}\right| \leq 1$ on $\partial \Omega$ and that

$$
\left|f(z) h_{\epsilon}(z)\right| \leq \exp \left\{A e^{\alpha|x|}-\epsilon \delta\left(e^{\beta x}+e^{-\beta x}\right)\right\} \quad(z \in \bar{\Omega})
$$

Fix $\epsilon>0$. Since $\epsilon \delta>0$ and $\beta>\alpha$, the exponent in (7) tends to $-\infty$ as $x \rightarrow \pm \infty$. Hence there exists an $x_{0}$ so that the right side of (7) is less than 1 for all $x>x_{0}$. Since $\left|f h_{\epsilon}\right| \leq 1$ on the boundary of the rectangle whose vertices are $\pm x_{0} \pm(\pi i / 2)$, the maximum modulus theorem shows that actually $\left|f h_{\epsilon}\right| \leq 1$ on this rectangle. Thus $\left|f h_{\epsilon}\right| \leq 1$ at every point of $\Omega$, for every $\epsilon>0$. As $\epsilon \rightarrow 0, h_{\epsilon}(z) \rightarrow 1$ for every $z$, so we conclude that $|f(z)| \leq 1$ for all $z \in \Omega$.

Here is a slightly different application of the same method. It will be used in the proof of Theorem 14.18.

12.10 Lindelöf's Theorem Suppose $\Gamma$ is a curve, with parameter interval $[0,1]$, such that $|\Gamma(t)|<1$ if $t<1$ and $\Gamma(1)=1$. If $g \in H^{\infty}$ and

$$
\lim _{t \rightarrow 1} g(\Gamma(t))=L
$$

then $g$ has radial limit $L$ at 1 .

(It follows from Exercise 14, Chap. 14, that $g$ actually has nontangential limit $L$ at 1.)

Proof Assume $|g|<1, L=0$, without loss of generality. Let $\epsilon>0$ be given. There exists $t_{0}<1$ so that, setting $r_{0}=\operatorname{Re} \Gamma\left(t_{0}\right)$, we have

$$
|g(\Gamma(t))|<\epsilon \quad \text { and } \quad \operatorname{Re} \Gamma(t)>r_{0}>\frac{1}{2}
$$

as soon as $t_{0}<t<1$.

Pick $r, r_{0}<r<1$.

Define $h$ in $\Omega=D(0 ; 1) \cap D(2 r ; 1)$ by

$$
h(z)=g(z) \overline{g(\bar{z})} g(2 r-z) \overline{g(2 r-\bar{z})}
$$

Then $h \in H(\Omega)$ and $|h|<1$. We claim that

$$
|h(r)|<\epsilon .
$$

Since $h(r)=|g(r)|^{4}$, the theorem follows from (4).

To prove (4), let $E_{1}=\Gamma\left(\left[t_{1}, 1\right]\right)$, where $t_{1}$ is the largest $t$ for which $\operatorname{Re} \Gamma(t)=r$, let $E_{2}$ be the reflection of $E_{1}$ in the real axis, and let $E$ be the union of $E_{1} \cup E_{2}$ and its reflection in the line $x=r$. Then (2) and (3) imply that

$$
|h(z)|<\epsilon \quad \text { if } \quad z \in \Omega \cap E \text {. }
$$

Pick $c>0$, define

$$
h_{c}(z)=h(z)(1-z)^{c}(2 r-1-z)^{c}
$$

for $z \in \Omega$, and put $h_{c}(1)=h_{c}(2 r-1)=0$. If $K$ is the union of $E$ and the bounded components of the complement of $E$, then $K$ is compact, $h_{\mathrm{c}}$ is continuous on $K$, holomorphic in the interior of $K$, and (5) implies that $\left|h_{c}\right|<\epsilon$ on the boundary of $K$. Since the construction of $E$ shows that $r \in K$, the maximum modulus theorem implies that $\left|h_{c}(r)\right|<\epsilon$.

Letting $c \rightarrow 0$, we obtain (4).

## An Interpolation Theorem

12.11 The convexity theorem 12.8 can sometimes be used to prove that certain linear transformations are bounded with respect to certain $L^{p}$-norms. Rather than discuss this in full generality, let us look at a particular situation of this kind.

Let $X$ be a measure space, with a positive measure $\mu$, and suppose $\left\{\psi_{n}\right\}$ $(n=1,2,3, \ldots)$ is an orthonormal set of functions in $L^{2}(\mu)$; we recall what this means:

$$
\int_{X} \psi_{n} \bar{\psi}_{m} d \mu= \begin{cases}1 & \text { if } m=n \\ 0 & \text { if } m \neq n\end{cases}
$$

Let us also assume that $\left\{\psi_{n}\right\}$ is a bounded sequence in $L^{\infty}(\mu)$ : There exists an $M<\infty$ such that

$$
\left|\psi_{n}(x)\right| \leq M \quad(n=1,2,3, \ldots ; x \in X)
$$

Then for any $f \in L^{p}(\mu)$, where $1 \leq p \leq 2$, the integrals

$$
\hat{f}(n)=\int_{X} f \bar{\psi}_{n} d \mu \quad(n=1,2,3, \ldots)
$$

exist and define a function $\hat{f}$ on the set of all positive integers.

There are now two very easy theorems: For $f \in L^{1}(\mu)$, (2) gives

$$
\|\hat{f}\|_{\infty} \leq M\|f\|_{1}
$$

and for $f \in L^{2}(\mu)$, the Bessel inequality gives

$$
\|\hat{f}\|_{2} \leq\|f\|_{2}
$$

where the norms are defined as usual:

$$
\|f\|_{p}=\left[\int|f|^{p} d \mu\right]^{1 / p}, \quad\|\hat{f}\|_{q}=\left[\sum|\hat{f}(n)|^{q}\right]^{1 / q}
$$

and $\|\hat{f}\|_{\infty}=\sup _{n}|\hat{f}(n)|$.

Since $(1, \infty)$ and $(2,2)$ are pairs of conjugate exponents, one may conjecture that $\|\hat{f}\|_{q}$ is finite whenever $f \in L^{p}(\mu)$ and $1<p<2, q=p /(p-1)$. This is indeed true and can be proved by "interpolation" between the preceding trivial cases $p=1$ and $p=2$.

12.12 The Hausdorff-Young Theorem Under the above assumptions, the inequality

$$
\|\hat{f}\|_{q} \leq M^{(2-p) / p}\|f\|_{p}
$$

holds if $1 \leq p \leq 2$ and if $f \in L^{p}(\mu)$.

Proof We first prove a reduced form of the theorem.

Fix $p, 1<p<2$. Let $f$ be a simple complex function such that $\|f\|_{p}=1$, and let $b_{1}, \ldots, b_{N}$ be complex numbers such that $\sum\left|b_{n}\right|^{p}=1$. Our objective is the inequality

$$
\left|\sum_{n=1}^{N} b_{n} \hat{f}(n)\right| \leq M^{(2-p) / p}
$$

Put $F=|f|^{p}$, and put $B_{n}=\left|b_{n}\right|^{p}$. Then there is a function $\varphi$ and there are complex numbers $\beta_{1}, \ldots, \beta_{N}$ such that

$$
f=F^{1 / p} \varphi, \quad|\varphi|=1, \quad \int_{X} F d \mu=1,
$$

and

$$
b_{n}=B_{n}^{1 / p} \beta_{n}, \quad\left|\beta_{n}\right|=1, \quad \sum_{n=1}^{N} B_{n}=1
$$

If we use these relations and the definition of $\hat{f}(n)$ given in Sec. 12.11, we obtain

$$
\sum_{n=1}^{N} b_{n} \hat{f}(n)=\sum_{n=1}^{N} B_{n}^{1 / p} \beta_{n} \int_{X} F^{1 / p} \varphi \bar{\psi}_{n} d \mu
$$

Now replace $1 / p$ by $z$ in (5), and define

$$
\Phi(z)=\sum_{n=1}^{N} B_{n}^{z} \beta_{n} \int_{X} F^{z} \varphi \bar{\psi}_{n} d \mu
$$

for any complex number $z$. Recall that $A^{z}=\exp (z \log A)$ if $A>0$; if $A=0$, we agree that $A^{z}=0$. Since $F$ is simple, since $F \geq 0$, and since $B_{n} \geq 0$, we see that $\Phi$ is a finite linear combination of such exponentials, so $\Phi$ is an entire function which is bounded on

$$
\{z: a \leq \operatorname{Re}(z) \leq b\}
$$

for any finite $a$ and $b$. We shall take $a=\frac{1}{2}$ and $b=1$, shall estimate $\Phi$ on the edges of this strip, and shall then apply Theorem 12.8 to estimate $\Phi(1 / p)$.

For $-\infty<y<\infty$, define

$$
c_{n}(y)=\int_{x} F^{1 / 2} F^{i y} \varphi \bar{\psi}_{n} d \mu
$$

The Bessel inequality gives

$$
\sum_{n=1}^{N}\left|c_{n}(y)\right|^{2} \leq \int_{X}\left|F^{1 / 2} F^{i y} \varphi\right|^{2} d \mu=\int_{X}|F| d \mu=1
$$

and then the Schwarz inequality shows that

$$
\left|\Phi\left(\frac{1}{2}+i y\right)\right|=\left|\sum_{n=1}^{N} B_{n}^{1 / 2} B_{n}^{i y} \beta_{n} c_{n}\right| \leq\left\{\sum_{n=1}^{N} B_{n} \cdot \sum_{n=1}^{N}\left|c_{n}\right|^{2}\right\}^{1 / 2} \leq 1
$$

The estimate

$$
|\Phi(1+i y)| \leq M \quad(-\infty<y<\infty)
$$

follows trivially from (3), (4), and (6), since $\left\|\psi_{n}\right\|_{\infty} \leq M$.

We now conclude from (9), (10), and Theorem 12.8 that

$$
|\Phi(x+i y)| \leq M^{2 x-1} \quad\left(\frac{1}{2} \leq x \leq 1,-\infty<y<\infty\right)
$$

With $x=1 / p$ and $y=0$, this gives the desired inequality (2).

The proof is now easily completed. Note first that

$$
\left\{\sum_{n=1}^{N}|\hat{f}(n)|^{q}\right\}^{1 / q}=\sup \left|\sum_{n=1}^{N} b_{n} \hat{f}(n)\right|
$$

the supremum being taken over all $\left\{b_{1}, \ldots, b_{N}\right\}$ with $\sum\left|b_{n}\right|^{p}=1$, since the $L^{q}$ norm of any function on any measure space is equal to its norm as a linear functional on $L^{p}$. Hence (2) shows that

$$
\left\{\sum_{n=1}^{N}|\hat{f}(n)|^{q}\right\}^{1 / q} \leq M^{(2-p) / p}\|f\|_{p}
$$

for every simple complex $f \in L^{p}(\mu)$.

If now $f \in L^{p}(\mu)$, there are simple functions $f_{j}$ such that $\left\|f_{j}-f\right\|_{p} \rightarrow 0$ as $j \rightarrow \infty$. Then $\hat{f}_{j}(n) \rightarrow \hat{f}(n)$ for every $n$, because $\psi_{n} \in L^{q}(\mu)$. Thus since (13) holds for each $f_{j}$, it also holds for $f$. Since $N$ was arbitrary, we finally obtain (1).

## A Converse of the Maximum Modulus Theorem

We now come to the theorem which was alluded to in the introduction of the present chapter.

The letter $j$ will denote the identity function: $j(z)=z$.

The function which assigns the number 1 to each $z \in \bar{U}$ will be denoted by 1 .

12.13 Theorem Suppose $M$ is a vector space of continuous complex functions on the closed unit disc $\bar{U}$, with the following properties:

(a) $1 \in M$.

(b) If $f \in M$, then also if $\in M$.

(c) If $f \in M$, then $\|f\|_{U}=\|f\|_{T}$.

Then every $f \in M$ is holomorphic in $U$.

Note that $(c)$ is a rather weak form of the maximum modulus principle; $(c)$ asserts only that the overall maximum of $|f|$ on $\bar{U}$ is attained at some point of the boundary $T$, but $(c)$ does not a priori exclude the existence of local maxima of $|f|$ in $U$.

ProOF By $(a)$ and $(b), M$ contains all polynomials. In conjunction with $(c)$, this shows that $M$ satisfies the hypotheses of Theorem 5.25. Thus every $f \in M$ is harmonic in $U$. We shall use (b) to show that every $f \in M$ actually satisfies the Cauchy-Riemann equation.

Let $\partial$ and $\bar{\partial}$ be the differential operators introduced in Sec. 11.1. The product rule for differentiation gives

$$
(\partial \bar{\partial})(f g)=f \cdot(\partial \bar{\partial} g)+(\partial f) \cdot(\bar{\partial} g)+(\bar{\partial} f) \cdot(\partial g)+(\partial \bar{\partial} f) \cdot g .
$$

Fix $f \in M$, and take $g=j$. Then $f j \in M$. Hence $f$ and $f j$ are harmonic, so $\partial \bar{\partial} f=0$ and $(\partial \bar{\partial})(f j)=0$. Also, $\bar{\partial} j=0$ and $\partial j=1$. The above identity therefore reduces to $\bar{\partial} f=0$. Thus $f \in H(U)$.

This result will be used in the following proof.

12.14 Radó's Theorem Assume $f \in C(\bar{U}), \Omega$ is the set of all $z \in U$ at which $f(z) \neq 0$, and $f$ is holomorphic in $\Omega$. Then $f$ is holomorphic in $U$. $\Omega=\varnothing$.

In particular, the theorem asserts that $U-\Omega$ is at most countable, unless

Proof Assume $\Omega \neq \varnothing$. We shall first prove that $\Omega$ is dense in $U$. If not, there exist $\alpha \in \Omega$ and $\beta \in U-\bar{\Omega}$ such that $2|\beta-\alpha|<1-|\beta|$. Choose $n$ so that $2^{n}|f(\alpha)|>\|f\|_{T}$. Define $h(z)=(z-\beta)^{-n} f(z)$, for $z \in \bar{\Omega}$. If $z \in U \cap \partial \Omega$, then $f(z)=0$, hence $h(z)=0$. If $z \in T \cap \partial \Omega$, then

$$
|h(z)| \leq(1-|\beta|)^{-n}\|f\|_{T}<|\alpha-\beta|^{-n}|f(\alpha)|=|h(\alpha)| .
$$

This contradicts the maximum modulus theorem.

Thus $\Omega$ is dense in $U$.

Next, let $M$ be the vector space of all $g \in C(\bar{U})$ that are holomorphic in $\Omega$. Fix $g \in M$. For $n=1,2,3, \ldots, f g^{n}=0$ on $U \cap \partial \Omega$. The maximum modulus theorem implies therefore, for every $\alpha \in \Omega$, that

$$
|f(\alpha)||g(\alpha)|^{n} \leq\left\|f g^{n}\right\|_{\partial \Omega}=\left\|f g^{n}\right\|_{T} \leq\|f\|_{T}\|g\|_{T}^{n}
$$

If we take $n$th roots and then let $n \rightarrow \infty$, we see that $|g(\alpha)| \leq\|g\|_{T}$, for every $\alpha \in \Omega$. Since $\Omega$ is dense in $U,\|g\|_{U}=\|g\|_{T}$.

It follows that $M$ satisfies the hypotheses of Theorem 12.13. Since $f \in M$, $f$ is holomorphic in $U$.

## Exercises

1 Suppose $\Delta$ is a closed equilateral triangle in the plane, with vertices $a, b, c$. Find $\max (|z-a||z-b||z-c|)$ as $z$ ranges over $\Delta$.

2 Suppose $f \in H\left(\mathrm{II}^{+}\right)$, where $\mathrm{II}^{+}$is the upper half plane, and $|f| \leq 1$. How large can $\left|f^{\prime}(i)\right|$ be? Find the extremal functions. (Compare the discussion in Sec. 12.5.)

3 Suppose $f \in H(\Omega)$. Under what conditions can $|f|$ have a local minimum in $\Omega$ ?

4 (a) Suppose $\Omega$ is a region, $D$ is a disc, $\bar{D} \subset \Omega, f \in H(\Omega), f$ is not constant, and $|f|$ is constant on the boundary of $D$. Prove that $f$ has at least one zero in $D$.

(b) Find all entire functions $f$ such that $|f(z)|=1$ whenever $|z|=1$.

5 Suppose $\Omega$ is a bounded region, $\left\{f_{n}\right\}$ is a sequence of continuous functions on $\bar{\Omega}$ which are holomorphic in $\Omega$, and $\left\{f_{n}\right\}$ converges uniformly on the boundary of $\Omega$. Prove that $\left\{f_{n}\right\}$ converges uniformly on $\bar{\Omega}$.

6 Suppose $f \in H(\Omega), \Gamma$ is a cycle in $\Omega$ such that $\operatorname{Ind}_{\Gamma}(\alpha)=0$ for all $\alpha \notin \Omega,|f(\zeta)| \leq 1$ for every $\zeta \in \Gamma^{*}$, and $\operatorname{Ind}_{\Gamma}(z) \neq 0$. Prove that $|f(z)| \leq 1$.

7 In the proof of Theorem 12.8 it was tacitly assumed that $M(a)>0$ and $M(b)>0$. Show that the theorem is true if $M(a)=0$, and that then $f(z)=0$ for all $z \in \Omega$.

8 If $0<R_{1}<R_{2}<\infty$, let $A\left(R_{1}, R_{2}\right)$ denote the annulus

$$
\left\{z: R_{1}<|z|<R_{2}\right\} .
$$

There is a vertical strip which the exponential function maps onto $A\left(R_{1}, R_{2}\right)$. Use this to prove Hadamard's three-circle theorem: If $f \in H\left(A\left(R_{1}, R_{2}\right)\right)$, if

$$
M(r)=\max _{\theta}\left|f\left(r e^{i \theta}\right)\right| \quad\left(R_{1}<r<R_{2}\right)
$$

and if $R_{1}<a<r<b<R_{2}$, then

$$
\log M(r) \leq \frac{\log (b / r)}{\log (b / a)} \log M(a)+\frac{\log (r / a)}{\log (b / a)} \log M(b)
$$

[In other words, $\log M(r)$ is a convex function of $\log r$.] For which $f$ does equality hold in this inequality?

9 Let $\Pi$ be the open right half plane $(z \in \Pi$ if and only if $\operatorname{Re} z>0)$. Suppose $f$ is continuous on the closure of $\Pi(\operatorname{Re} z \geq 0), f \in H(\Pi)$, and there are constants $A<\infty$ and $\alpha<1$ such that

$$
|f(z)|<A \exp \left(|z|^{\alpha}\right)
$$

for all $z \in \Pi$. Furthermore, $|f(i y)| \leq 1$ for all real $y$. Prove that $|f(z)| \leq 1$ in $\Pi$.

Show that the conclusion is false for $\alpha=1$.

How does the result have to be modified if $\Pi$ is replaced by a region bounded by two rays through the origin, at an angle not equal to $\pi$ ?

10 Let $\Pi$ be the open right half plane. Suppose that $f \in H(\Pi)$, that $|f(z)|<1$ for all $z \in \Pi$, and that there exists $\alpha,-\pi / 2<\alpha<\pi / 2$, such that

$$
\frac{\log \left|f\left(r e^{i \alpha}\right)\right|}{r} \rightarrow-\infty \quad \text { as } \quad r \rightarrow \infty
$$

Prove that $f=0$.

Hint: Put $g_{n}(z)=f(z) e^{n z}, n=1,2,3, \ldots$ Apply Exercise 9 to the two angular regions defined by $-\pi / 2<\theta<\alpha, \alpha<\theta<\pi / 2$. Conclude that each $g_{n}$ is bounded in $\Pi$, and hence that $\left|g_{n}\right|<1$ in $\Pi$, for all $n$.

11 Suppose $\Gamma$ is the boundary of an unbounded region $\Omega, f \in H(\Omega), f$ is continuous on $\Omega \cup \Gamma$, and there are constants $B<\infty$ and $M<\infty$ such that $|f| \leq M$ on $\Gamma$ and $|f| \leq B$ in $\Omega$. Prove that we then actually have $|f| \leq M$ in $\Omega$.

Suggestion: Show that it involves no loss of generality to assume that $U \cap \Omega=\varnothing$. Fix $z_{0} \in \Omega$, let $n$ be a large integer, let $V$ be a large disc with center at 0 , and apply the maximum modulus theorem to the function $f^{n}(z) / z$ in the component of $V \cap \Omega$ which contains $z_{0}$.

12 Let $f$ be an entire function. If there is a continuous mapping $\gamma$ of $[0,1)$ into the complex plane such that $\gamma(t) \rightarrow \infty$ and $f(\gamma(t)) \rightarrow \alpha$ as $t \rightarrow 1$, we say that $\alpha$ is an asymptotic value of $f$. [In the complex plane, " $\gamma(t) \rightarrow \infty$ as $t \rightarrow 1$ " means that to each $R<\infty$ there corresponds a $t_{R}<1$ such that $|\gamma(t)|>R$ if $t_{R}<t<1$.] Prove that every nonconstant entire function has $\infty$ as an asymptotic value.

Suggestion: Let $E_{n}=\{z:|f(z)|>n\}$. Each component of $E_{n}$ is unbounded (proof?) and contains a component of $E_{n+1}$, by Exercise 11 .

13 Show that exp has exactly two asymptotic values: 0 and $\infty$. How about $\sin$ and $\cos$ ? Note: $\sin z$ and $\cos z$ are defined, for all complex $z$, by

$$
\sin z=\frac{e^{i z}-e^{-i z}}{2 i}, \quad \cos z=\frac{e^{i z}+e^{-i z}}{2}
$$

14 If $f$ is entire and if $\alpha$ is not in the range of $f$, prove that $\alpha$ is an asymptotic value of $f$ unless $f$ is constant.

15 Suppose $f \in H(U)$. Prove that there is a sequence $\left\{z_{n}\right\}$ in $U$ such that $\left|z_{n}\right| \rightarrow 1$ and $\left\{f\left(z_{n}\right)\right\}$ is bounded.

16 Suppose $\Omega$ is a bounded region, $f \in H(\Omega)$, and

$$
\limsup _{n \rightarrow \infty}\left|f\left(z_{n}\right)\right| \leq M
$$

for every sequence $\left\{z_{n}\right\}$ in $\Omega$ which converges to a boundary point of $\Omega$. Prove that $|f(z)| \leq M$ for all $z \in \Omega$.

17 Let $\Phi$ be the set of all $f \in H(U)$ such that $0<|f(z)|<1$ for $z \in U$, and let $\Phi_{c}$ be the set all $f \in \Phi$ that have $f(0)=c$. Define

$$
M(c)=\sup \left\{\left|f^{\prime}(0)\right|: f \in \Phi_{c}\right\}, \quad M=\sup \left\{\left|f^{\prime}(0)\right|: f \in \Phi\right\}
$$

Find $M$, and $M(c)$ for $0<c<1$. Find an $f \in \Phi$ with $f^{\prime}(0)=M$, or prove that there is no such $f$.

Suggestion: $\log f$ maps $U$ into the left half plane. Compose $\log f$ with a properly chosen map that takes this half plane to $U$. Apply the Schwarz lemma.

## CHAPTER <br> THIRTEEN

## APPROXIMATIONS BY RATIONAL FUNCTIONS

## Preparation

13.1 The Riemann Sphere It is often convenient in the study of holomorphic functions to compactify the complex plane by the adjunction of a new point called $\infty$. The resulting set $S^{2}$ (the Riemann sphere, the union of $R^{2}$ and $\{\infty\}$ ) is topologized in the following manner. For any $r>0$, let $D^{\prime}(\infty ; r)$ be the set of all complex numbers $z$ such that $|z|>r$, put $D(\infty ; r)=D^{\prime}(\infty ; r) \cup\{\infty\}$, and declare a subset of $S^{2}$ to be open if and only if it is the union of discs $D(a ; r)$, where the $a$ 's are arbitrary points of $S^{2}$ and the $r$ 's are arbitrary positive numbers. On $S^{2}-\{\infty\}$, this gives of course the ordinary topology of the plane. It is easy to see that $S^{2}$ is homeomorphic to a sphere (hence the notation). In fact, a homeomorphism $\varphi$ of $S^{2}$ onto the unit sphere in $R^{3}$ can be explicitly exhibited: Put $\varphi(\infty)=(0,0,1)$, and put

$$
\varphi\left(r e^{i \theta}\right)=\left(\frac{2 r \cos \theta}{r^{2}+1}, \frac{2 r \sin \theta}{r^{2}+1}, \frac{r^{2}-1}{r^{2}+1}\right)
$$

for all complex numbers $r e^{i \theta}$. We leave it to the reader to construct the geometric picture that goes with (1).

If $f$ is holomorphic in $D^{\prime}(\infty ; r)$, we say that $f$ has an isolated singularity at $\infty$. The nature of this singularity is the same as that which the function $\tilde{f}$, defined in $D^{\prime}(0 ; 1 / r)$ by $\tilde{f}(z)=f(1 / z)$, has at 0 .

Thus if $f$ is bounded in $D^{\prime}(\infty ; r)$, then $\lim _{z \rightarrow \infty} f(z)$ exists and is a complex number (as we see if we apply Theorem 10.20 to $f$ ), we define $f(\infty)$ to be this limit, and we thus obtain a function in $D(\infty ; r)$ which we call holomorphic: note that this is defined in terms of the behavior of $\tilde{f}$ near 0 , and not in terms of differentiability of $f$ at $\infty$.

If $\tilde{f}$ has a pole of order $m$ at 0 , then $f$ is said to have a pole of order $m$ at $\infty$; the principal part of $f$ at $\infty$ is then an ordinary polynomial of degree $m$ (compare Theorem 10.21), and if we subtract this polynomial from $f$, we obtain a function with a removable singularity at $\infty$.

Finally, if $\tilde{f}$ has an essential singularity at 0 , then $f$ is said to have an essential singularity at $\infty$. For instance, every entire function which is not a polynomial has an essential singularity at $\infty$.

Later in this chapter we shall encounter the condition " $S^{2}-\Omega$ is connected," where $\Omega$ is an open set in the plane. Note that this is not equivalent to the condition "the complement of $\Omega$ relative to the plane is connected." For example, if $\Omega$ consists of all complex $z=x+i y$ with $0<y<1$, the complement of $\Omega$ relative to the plane has two components, but $S^{2}-\Omega$ is connected.

13.2 Rational Functions A rational function $f$ is, by definition, a quotient of two polynomials $P$ and $Q: f=P / Q$. It follows from Theorem 10.25 that every nonconstant polynomial is a product of factors of degree 1 . We may assume that $P$ and $Q$ have no such factors in common. Then $f$ has a pole at each zero of $Q$ (the pole of $f$ has the same order as the zero of $Q$ ). If we subtract the corresponding principal parts, we obtain a rational function whose only singularity is at $\infty$ and which is therefore a polynomial.

Every rational function $f=P / Q$ has thus a representation of the form

$$
f(z)=A_{0}(z)+\sum_{j=1}^{k} A_{j}\left(\left(z-a_{j}\right)^{-1}\right)
$$

where $A_{0}, A_{1}, \ldots, A_{k}$ are polynomials, $A_{1}, \ldots, A_{k}$ have no constant term, and $a_{1}$, $\ldots, a_{k}$ are the distinct zeros of $Q ;(1)$ is called the partial fractions decomposition of $f$.

We turn to some topological considerations. We know that every open set in the plane is a countable union of compact sets (closed discs, for instance). However, it will be convenient to have some additional properties satisfied by these compact sets:

13.3 Theorem Every open set $\Omega$ in the plane is the union of a sequence $\left\{K_{n}\right\}$, $n=1,2,3, \ldots$, of compact sets such that

(a) $K_{n}$ lies in the interior of $K_{n+1}$, for $n=1,2,3, \ldots$

(b) Every compact subset of $\Omega$ lies in some $K_{n}$.

(c) Every component of $S^{2}-K_{n}$ contains a component of $S^{2}-\Omega$, for $n=1,2$, $3, \ldots$.

Property $(c)$ is, roughly speaking, that $K_{n}$ has no holes except those which are forced upon it by the holes in $\Omega$. Note that $\Omega$ is not assumed to be connected. The interior of a set $E$ is, by definition, the largest open subset of $E$.

ProOf For $n=1,2,3, \ldots$, put

$$
V_{n}=D(\infty ; n) \cup \bigcup_{a \notin \Omega} D\left(a ; \frac{1}{n}\right)
$$

and put $K_{n}=S^{2}-V_{n}$. [Of course, $a \neq \infty$ in (1).] Then $K_{n}$ is a closed and bounded (hence compact) subset of $\Omega$, and $\Omega=\bigcup K_{n}$. If $z \in K_{n}$ and $r=n^{-1}-(n+1)^{-1}$, one verifies easily that $D(z ; r) \subset K_{n+1}$. This gives $(a)$. Hence $\Omega$ is the union of the interiors $W_{n}$ of $K_{n}$. If $K$ is a compact subset of $\Omega$, then $K \subset W_{1} \cup \cdots \cup W_{N}$ for some $N$, hence $K \subset K_{N}$.

Finally, each of the discs in (1) intersects $S^{2}-\Omega$; each disc is connected; hence each component of $V_{n}$ intersects $S^{2}-\Omega$; since $V_{n} \supset S^{2}-\Omega$, no component of $S^{2}-\Omega$ can intersect two components of $V_{n}$. This gives $(c)$.

13.4 Sets of Oriented Intervals Let $\Phi$ be a finite collection of oriented intervals in the plane. For each point $p$, let $m_{I}(p)\left[m_{E}(p)\right]$ be the number of members of $\Phi$ that have initial point [end point] $p$. If $m_{I}(p)=m_{E}(p)$ for every $p$, we shall say that $\Phi$ is balanced.

If $\Phi$ is balanced (and nonempty), the following construction can be carried out.

Pick $\gamma_{1}=\left[a_{0}, a_{1}\right] \in \Phi$. Assume $k \geq 1$, and assume that distinct members $\gamma_{1}$, $\ldots, \gamma_{k}$ of $\Phi$ have been chosen in such a way that $\gamma_{i}=\left[a_{i-1}, a_{i}\right]$ for $1 \leq i \leq k$. If $a_{k}=a_{0}$, stop. If $a_{k} \neq a_{0}$, and if precisely $r$ of the intervals $\gamma_{1}, \ldots, \gamma_{k}$ have $a_{k}$ as end point, then only $r-1$ of them have $a_{k}$ as initial point; since $\Phi$ is balanced, $\Phi$ contains at least one other interval, say $\gamma_{k+1}$, whose initial point is $a_{k}$. Since $\Phi$ is finite, we must return to $a_{0}$ eventually, say at the $n$th step.

Then $\gamma_{1}, \ldots, \gamma_{n}$ join (in this order) to form a closed path.

The remaining members of $\Phi$ still form a balanced collection to which the above construction can be applied. It follows that the members of $\Phi$ can be so numbered that they form finitely many closed paths. The sum of these paths is a cycle. The following conclusion is thus reached.

If $\Phi=\left\{\gamma_{1}, \ldots, \gamma_{N}\right\}$ is a balanced collection of oriented intervals, and if

$$
\Gamma=\gamma_{1} \dot{+} \cdots \dot{+} \gamma_{N}
$$

then $\Gamma$ is a cycle.

13.5 Theorem If $K$ is a compact subset of a plane open set $\Omega(\neq \varnothing)$, then there is a cycle $\Gamma$ in $\Omega-K$ such that the Cauchy formula

$$
f(z)=\frac{1}{2 \pi i} \int_{\Gamma} \frac{f(\zeta)}{\zeta-z} d \zeta
$$

holds for every $f \in H(\Omega)$ and for every $z \in K$.

Proof Since $K$ is compact and $\Omega$ is open, there exists an $\eta>0$ such that the distance from any point of $K$ to any point outside $\Omega$ is at least $2 \eta$. Construct
a grid of horizontal and vertical lines in the plane, such that the distance between any two adjacent horizontal lines is $\eta$, and likewise for the vertical lines. Let $Q_{1}, \ldots, Q_{m}$ be those squares (closed 2-cells) of edge $\eta$ which are formed by this grid and which intersect $K$. Then $Q_{r} \subset \Omega$ for $r=1, \ldots, m$.

If $a_{r}$ is the center of $Q_{r}$ and $a_{r}+b$ is one of its vertices, let $\gamma_{r k}$ be the oriented interval

$$
\gamma_{r k}=\left[a_{r}+i^{k} b, a_{r}+i^{k+1} b\right]
$$

and define

$$
\partial Q_{r}=\gamma_{r 1} \dot{+} \gamma_{r 2} \dot{+} \gamma_{r 3} \dot{+} \gamma_{r 4} \quad(r=1, \ldots, m)
$$

It is then easy to check (for example, as a special case of Theorem 10.37, or by means of Theorems 10.11 and 10.40) that

$$
\operatorname{Ind}_{\partial Q_{r}}(\alpha)= \begin{cases}1 & \text { if } \alpha \text { is in the interior of } Q_{r} \\ 0 & \text { if } \alpha \text { is not in } Q_{r}\end{cases}
$$

Let $\Sigma$ be the collection of all $\gamma_{r k}(1 \leq r \leq m, 1 \leq k \leq 4)$. It is clear that $\Sigma$ is balanced. Remove those members of $\Sigma$ whose opposites (see Sec. 10.8) also belong to $\Sigma$. Let $\Phi$ be the collection of the remaining members of $\Sigma$. Then $\Phi$ is balanced. Let $\Gamma$ be the cycle constructed from $\Phi$, as in Sec. 13.4.

If an edge $E$ of some $Q_{r}$ intersects $K$, then the two squares in whose boundaries $E$ lies intersect $K$. Hence $\Sigma$ contains two oriented intervals which are each other's opposites and whose range is $E$. These intervals do not occur in $\Phi$. Thus $\Gamma$ is a cycle in $\Omega-K$.

The construction of $\Phi$ from $\Sigma$ shows also that

$$
\operatorname{Ind}_{\Gamma}(\alpha)=\sum_{r=1}^{m} \operatorname{Ind}_{\partial Q_{r}}(\alpha)
$$

if $\alpha$ is not in the boundary of any $Q_{r}$. Hence (4) implies

$$
\operatorname{Ind}_{\Gamma}(\alpha)= \begin{cases}1 & \text { if } \alpha \text { is in the interior of some } Q_{r} \\ 0 & \text { if } \alpha \text { lies in no } Q_{r}\end{cases}
$$

If $z \in K$, then $z \notin \Gamma^{*}$, and $z$ is a limit point of the interior of some $Q_{r}$. Since the left side of (6) is constant in each component of the complement of $\Gamma^{*},(6)$ gives

$$
\operatorname{Ind}_{\Gamma}(z)= \begin{cases}1 & \text { if } z \in K \\ 0 & \text { if } z \notin \Omega\end{cases}
$$

Now (1) follows from Cauchy's theorem 10.35.

## Runge's Theorem

The main objective of this section is Theorem 13.9. We begin with a slightly different version in which the emphasis is on uniform approximation on one compact set.

13.6 Theorem Suppose $K$ is a compact set in the plane and $\left\{\alpha_{j}\right\}$ is a set which contains one point in each component of $S^{2}-K$. If $\Omega$ is open, $\Omega \supset K, f \in H(\Omega)$, and $\epsilon>0$, there exists a rational function $R$, all of whose poles lie in the prescribed set $\left\{\alpha_{j}\right\}$, such that

$$
|f(z)-R(z)|<\epsilon
$$

for every $z \in K$.

Note that $S^{2}-K$ has at most countably many components. Note also that the preassigned point in the unbounded component of $S^{2}-K$ may very well be $\infty$; in fact, this happens to be the most interesting choice.

Proof We consider the Banach space $C(K)$ whose members are the continuous complex functions on $K$, with the supremum norm. Let $M$ be the subspace of $C(K)$ which consists of the restrictions to $K$ of those rational functions which have all their poles in $\left\{\alpha_{j}\right\}$. The theorem asserts that $f$ is in the closure of $M$. By Theorem 5.19 (a consequence of the Hahn-Banach theorem), this is equivalent to saying that every bounded linear functional on $C(K)$ which vanishes on $M$ also vanishes at $f$, and hence the Riesz representation theorem (Theorem 6.19) shows that we must prove the following assertion:

If $\mu$ is a complex Borel measure on $K$ such that

$$
\int_{K} R d \mu=0
$$

for every rational function $R$ with poles only in the set $\left\{\alpha_{j}\right\}$, and if $f \in H(\Omega)$, then we also have

$$
\int_{K} f d \mu=0
$$

So let us assume that $\mu$ satisfies (2). Define

$$
h(z)=\int_{K} \frac{d \mu(\zeta)}{\zeta-z} \quad\left(z \in S^{2}-K\right)
$$

By Theorem 10.7 (with $X=K, \varphi(\zeta)=\zeta), h \in H\left(S^{2}-K\right.$ ).

Let $V_{j}$ be the component of $S^{2}-K$ which contains $\alpha_{j}$, and suppose $D\left(\alpha_{j} ; r\right) \subset V_{j}$. If $\alpha_{j} \neq \infty$ and if $z$ is fixed in $D\left(\alpha_{j} ; r\right)$, then

$$
\frac{1}{\zeta-z}=\lim _{N \rightarrow \infty} \sum_{n=0}^{N} \frac{\left(z-\alpha_{j}\right)^{n}}{\left(\zeta-\alpha_{j}\right)^{n+1}}
$$

uniformly for $\zeta \in K$. Each of the functions on the right of (5) is one to which (2) applies. Hence $h(z)=0$ for all $z \in D\left(\alpha_{j} ; r\right)$. This implies that $h(z)=0$ for all $z \in V_{j}$, by the uniqueness theorem 10.18 .

If $\alpha_{j}=\infty$, (5) is replaced by

$$
\frac{1}{\zeta-z}=-\lim _{N \rightarrow \infty} \sum_{n=0}^{N} z^{-n-1} \zeta^{n} \quad(\zeta \in K,|z|>r)
$$

which implies again that $h(z)=0$ in $D(\infty ; r)$, hence in $V_{j}$. We have thus proved from (2) that

$$
h(z)=0 \quad\left(z \in S^{2}-K\right)
$$

Now choose a cycle $\Gamma$ in $\Omega-K$, as in Theorem 13.5, and integrate this Cauchy integral representation of $f$ with respect to $\mu$. An application of Fubini's theorem (legitimate, since we are dealing with Borel measures and continuous functions on compact spaces), combined with (7), gives

$$
\begin{aligned}
\int_{K} f d \mu & =\int_{K} d \mu(\zeta)\left[\frac{1}{2 \pi i} \int_{\Gamma} \frac{f(w)}{w-\zeta} d w\right] \\
& =\frac{1}{2 \pi i} \int_{\Gamma} f(w) d w \int_{K} \frac{d \mu(\zeta)}{w-\zeta} \\
& =-\frac{1}{2 \pi i} \int_{\Gamma} f(w) h(w) d w=0
\end{aligned}
$$

The last equality depends on the fact that $\Gamma^{*} \subset \Omega-K$, where $h(w)=0$.

Thus (3) holds, and the proof is complete.

The following special case is of particular interest.

13.7 Theorem Suppose $K$ is a compact set in the plane, $S^{2}-K$ is connected, and $f \in H(\Omega)$, where $\Omega$ is some open set containing $K$. Then there is a sequence $\left\{P_{n}\right\}$ of polynomials such that $P_{n}(z) \rightarrow f(z)$ uniformly on $K$.

Proof Since $S^{2}-K$ has now only one component, we need only one point $\alpha_{j}$ to apply Theorem 13.6, and we may take $\alpha_{j}=\infty$.

13.8 Remark The preceding result is false for every compact $K$ in the plane such that $S^{2}-K$ is not connected. For in that case $S^{2}-K$ has a bounded component $V$. Choose $\alpha \in V$, put $f(z)=(z-\alpha)^{-1}$, and put
$m=\max \{|z-\alpha|: \quad z \in K\}$. Suppose $P$ is a polynomial, such that $|P(z)-f(z)|<1 / m$ for all $z \in K$. Then

$$
|(z-\alpha) P(z)-1|<1 \quad(z \in K)
$$

In particular, (1) holds if $z$ is in the boundary of $V$; since the closure of $V$ is compact, the maximum modulus theorem shows that (1) holds for every $z \in V$; taking $z=\alpha$, we obtain $1<1$. Hence the uniform approximation is not possible.

The same argument shows that none of the $\alpha_{j}$ can be dispensed with in Theorem 13.6.

We now apply the preceding approximation theorems to approximation in open sets. Let us emphasize that $K$ was not assumed to be connected in Theorems 13.6 and 13.7 and that $\Omega$ will not be assumed to be connected in the theorem which follows.

13.9 Theorem Let $\Omega$ be an open set in the plane, let $A$ be a set which has one point in each component of $S^{2}-\Omega$, and assume $f \in H(\Omega)$. Then there is a sequence $\left\{R_{n}\right\}$ of rational functions, with poles only in $A$, such that $R_{n} \rightarrow f$ uniformly on compact subsets of $\Omega$.

In the special case in which $S^{2}-\Omega$ is connected, we may take $A=\{\infty\}$ and thus obtain polynomials $P_{n}$ such that $P_{n} \rightarrow f$ uniformly on compact subsets of $\Omega$.

Observe that $S^{2}-\Omega$ may have uncountably many components; for instance, we may have $S^{2}-\Omega=\{\infty\} \cup C$, where $C$ is a Cantor set.

Proof Choose a sequence of compact sets $K_{n}$ in $\Omega$, with the properties specified in Theorem 13.3. Fix $n$, for the moment. Since each component of $S^{2}-K_{n}$ contains a component of $S^{2}-\Omega$, each component of $S^{2}-K_{n}$ contains a point of $A$, so Theorem 13.6 gives us a rational function $R_{n}$ with poles in $A$ such that

$$
\left|R_{n}(z)-f(z)\right|<\frac{1}{n} \quad\left(z \in K_{n}\right) .
$$

If now $K$ is any compact set in $\Omega$, there exists an $N$ such that $K \subset K_{n}$ for all $n \geq N$. It follows from (1) that

$$
\left|R_{n}(z)-f(z)\right|<\frac{1}{n} \quad(z \in K, n \geq N)
$$

which completes the proof.

## The Mittag-Leffler Theorem

Runge's theorem will now be used to prove that meromorphic functions can be constructed with arbitrarily preassigned poles.

13.10 Theorem Suppose $\Omega$ is an open set in the plane, $A \subset \Omega, A$ has no limit point in $\Omega$, and to each $\alpha \in A$ there are associated a positive integer $m(\alpha)$ and $a$ rational function

$$
P_{\alpha}(z)=\sum_{j=1}^{m(\alpha)} c_{j, \alpha}(z-\alpha)^{-j}
$$

Then there exists a meromorphic function $f$ in $\Omega$, whose principal part at each $\alpha \in A$ is $P_{\alpha}$ and which has no other poles in $\Omega$.

ProOF We choose a sequence $\left\{K_{n}\right\}$ of compact sets in $\Omega$, as in Theorem 13.3: For $n=1,2,3, \ldots, K_{n}$ lies in the interior of $K_{n+1}$, every compact subset of $\Omega$ lies in some $K_{n}$, and every component of $S^{2}-K_{n}$ contains a component of $S^{2}-\Omega$. Put $A_{1}=A \cap K_{1}$, and $A_{n}=A \cap\left(K_{n}-K_{n-1}\right)$ for $n=2,3,4, \ldots$ Since $A_{n} \subset K_{n}$ and $A$ has no limit point in $\Omega$ (hence none in $K_{n}$ ), each $A_{n}$ is a finite set. Put

$$
Q_{n}(z)=\sum_{\alpha \in A_{n}} P_{\alpha}(z) \quad(n=1,2,3, \ldots)
$$

Since each $A_{n}$ is finite, each $Q_{n}$ is a rational function. The poles of $Q_{n}$ lie in $K_{n}-K_{n-1}$, for $n \geq 2$. In particular, $Q_{n}$ is holomorphic in an open set containing $K_{n-1}$. It now follows from Theorem 13.6 that there exist rational functions $R_{n}$, all of whose poles are in $S^{2}-\Omega$, such that

$$
\left|R_{n}(z)-Q_{n}(z)\right|<2^{-n} \quad\left(z \in K_{n-1}\right)
$$

We claim that

$$
f(z)=Q_{1}(z)+\sum_{n=2}^{\infty}\left(Q_{n}(z)-R_{n}(z)\right) \quad(z \in \Omega)
$$

has the desired properties.

Fix $N$. On $K_{N}$, we have

$$
f=Q_{1}+\sum_{n=2}^{N}\left(Q_{n}-R_{n}\right)+\sum_{N+1}^{\infty}\left(Q_{n}-R_{n}\right)
$$

By (2), each term in the last sum in (4) is less than $2^{-n}$ on $K_{N}$; hence this last series converges uniformly on $K_{N}$, to a function which is holomorphic in the interior of $K_{N}$. Since the poles of each $R_{n}$ are outside $\Omega$,

$$
f-\left(Q_{1}+\cdots+Q_{N}\right)
$$

is holomorphic in the interior of $K_{N}$. Thus $f$ has precisely the prescribed principal parts in the interior of $K_{N}$, and hence in $\Omega$, since $N$ was arbitrary.

## Simply Connected Regions

We shall now summarize some properties of simply connected regions (see Sec. 10.38) which illustrate the important role that they play in the theory of holomorphic functions. Of these properties, $(a)$ and $(b)$ are what one might call internal topological properties of $\Omega ;(c)$ and $(d)$ refer to the way in which $\Omega$ is embedded in $S^{2}$; properties $(e)$ to $(h)$ are analytic in character; $(j)$ is an algebraic statement about the ring $H(\Omega)$. The Riemann mapping theorem 14.8 is another very important property of simply connected regions. In fact, we shall use it to prove the implication $(j) \rightarrow(a)$.

13.11 Theorem For a plane region $\Omega$, each of the following nine conditions implies all the others.

(a) $\Omega$ is homeomorphic to the open unit disc $U$.

(b) $\Omega$ is simply connected.

(c) $\operatorname{Ind}_{\gamma}(\alpha)=0$ for every closed path $\gamma$ in $\Omega$ and for every $\alpha \in S^{2}-\Omega$.

(d) $S^{2}-\Omega$ is connected.

(e) Every $f \in H(\Omega)$ can be approximated by polynomials, uniformly on compact subsets of $\Omega$.

( $f)$ For every $f \in H(\Omega)$ and every closed path $\gamma$ in $\Omega$,

$$
\int_{\gamma} f(z) d z=0
$$

(g) To every $f \in H(\Omega)$ corresponds an $F \in H(\Omega)$ such that $F^{\prime}=f$.

(h) If $f \in H(\Omega)$ and $1 / f \in H(\Omega)$, there exists a $g \in H(\Omega)$ such that $f=\exp (g)$.

(j) If $f \in H(\Omega)$ and $1 / f \in H(\Omega)$, there exists $a \varphi \in H(\Omega)$ such that $f=\varphi^{2}$.

The assertion of $(h)$ is that $f$ has a "holomorphic logarithm" $g$ in $\Omega ;(j)$ asserts that $f$ has a "holomorphic square root" $\varphi$ in $\Omega$; and $(f)$ says that the Cauchy theorem holds for every closed path in a simply connected region.

In Chapter 16 we shall see that the monodromy theorem describes yet another characteristic property of simply connected regions.

Proof $(a)$ implies $(b)$. To say that $\Omega$ is homeomorphic to $U$ means that there is a continuous one-to-one mapping $\psi$ of $\Omega$ onto $U$ whose inverse $\psi^{-1}$ is also continuous. If $\gamma$ is a closed curve in $\Omega$, with parameter interval $[0,1]$, put

$$
H(s, t)=\psi^{-1}(t \psi(\gamma(s)))
$$

Then $H: I^{2} \rightarrow \Omega$ is continuous; $H(s, 0)=\psi^{-1}(0)$, a constant; $H(s, 1)=\gamma(s)$; and $H(0, t)=H(1, t)$ because $\gamma(0)=\gamma(1)$. Thus $\Omega$ is simply connected.
(b) implies (c). If $(b)$ holds and $\gamma$ is a closed path in $\Omega$, then $\gamma$ is (by definition of "simply connected") $\Omega$-homotopic to a constant path. Hence (c) holds, by Theorem 10.40 .

(c) implies $(d)$. Assume $(d)$ is false. Then $S^{2}-\Omega$ is a closed subset of $S^{2}$ which is not connected. As noted in Sec. 10.1, it follows that $S^{2}-\Omega$ is the union of two nonempty disjoint closed sets $H$ and $K$. Let $H$ be the one that contains $\infty$. Let $W$ be the complement of $H$, relative to the plane. Then $W=\Omega \cup K$. Since $K$ is compact, Theorem 13.5 (with $f=1$ ) shows that there is a cycle $\Gamma$ in $W-K=\Omega$ such that $\operatorname{Ind}_{\Gamma}(z)=1$ for $z \in K$. Since $K \neq \varnothing,(c)$ fails.

(d) implies $(e)$. This is part of Theorem 13.9.

$(e)$ implies $(f)$. Choose $f \in H(\Omega)$, let $\gamma$ be a closed path in $\Omega$, and choose polynomials $P_{n}$ which converge to $f$, uniformly on $\gamma^{*}$. Since $\int_{\gamma} P_{n}(z) d z=0$ for all $n$, we conclude that $(f)$ holds.

$(f)$ implies $(g)$. Assume $(f)$ holds, fix $z_{0} \in \Omega$, and put

$$
F(z)=\int_{\Gamma(z)} f(\zeta) d \zeta \quad(z \in \Omega)
$$

where $\Gamma(z)$ is any path in $\Omega$ from $z_{0}$ to $z$. This defines a function $F$ in $\Omega$. For if $\Gamma_{1}(z)$ is another path from $z_{0}$ to $z$ (in $\Omega$ ), then $\Gamma$ followed by the opposite of $\Gamma_{1}$ is a closed path in $\Omega$, the integral of $f$ over this closed path is 0 , so (1) is not affected if $\Gamma(z)$ is replaced by $\Gamma_{1}(z)$. We now verify that $F^{\prime}=f$. Fix $a \in \Omega$. There exists an $r>0$ such that $D(a ; r) \subset \Omega$. For $z \in D(a ; r)$ we can compute $F(z)$ by integrating $f$ over a path $\Gamma(a)$, followed by the interval $[a, z]$. Hence, for $z \in D^{\prime}(a ; r)$,

$$
\frac{F(z)-F(a)}{z-a}=\frac{1}{z-a} \int_{[a, z]} f(\zeta) d \zeta
$$

and the continuity of $f$ at $a$ implies now that $F^{\prime}(a)=f(a)$, as in the proof of Theorem 10.14.

$(g)$ implies $(h)$. If $f \in H(\Omega)$ and $f$ has no zero in $\Omega$, then $f^{\prime} / f \in H(\Omega)$, and $(g)$ implies that there exists a $g \in H(\Omega)$ so that $g^{\prime}=f^{\prime} / f$. We can add a constant to $g$, so that $\exp \left\{g\left(z_{0}\right)\right\}=f\left(z_{0}\right)$ for some $z_{0} \in \Omega$. Our choice of $g$ shows that the derivative of $f e^{-g}$ is 0 in $\Omega$, hence $f e^{-g}$ is constant (since $\Omega$ is connected), and it follows that $f=e^{g}$.

(h) implies $(j)$. By $(h), f=e^{g}$. Put $\varphi=\exp \left(\frac{1}{2} g\right)$.

(j) implies $(a)$. If $\Omega$ is the whole plane, then $\Omega$ is homeomorphic to $U$ : $\operatorname{map} z$ to $z /(1+|z|)$.

If $\Omega$ is a proper subregion of the plane which satisfies $(j)$, then there actually exists a holomorphic homeomorphism of $\Omega$ onto $U$ (a conformal mapping). This assertion is the Riemann mapping theorem, which is the main objective of the next chapter. Hence the proof of Theorem 13.11 will be complete as soon as the Riemann mapping theorem is proved. (See the note following the statement of Theorem 14.8.)

The fact that $(h)$ holds in every simply connected region has the following consequence (which can also be proved by quite elementary means):

13.12 Theorem If $f \in H(\Omega)$, where $\Omega$ is any open set in the plane, and if $f$ has no zero in $\Omega$, then $\log |f|$ is harmonic in $\Omega$.

Proof To every disc $D \subset \Omega$ there corresponds a function $g \in H(D)$ such that $f=e^{g}$ in $D$. If $u=\operatorname{Re} g$, then $u$ is harmonic in $D$, and $|f|=e^{u}$. Thus $\log |f|$ is harmonic in every disc in $\Omega$, and this gives the desired conclusion.

## Exercises

1 Prove that every meromorphic function on $S^{2}$ is rational.

2 Let $\Omega=\{z:|z|<1$ and $|2 z-1|>1\}$, and suppose $f \in H(\Omega)$.

(a) Must there exist a sequence of polynomials $P_{n}$ such that $P_{n} \rightarrow f$ uniformly on compact subsets of $\Omega$ ?

(b) Must there exist such a sequence which converges to $f$ uniformly in $\Omega$ ?

(c) Is the answer to $(b)$ changed if we require more of $f$, namely, that $f$ be holomorphic in some open set which contains the closure of $\Omega$ ?

3 Is there a sequence of polynomials $P_{n}$ such that $P_{n}(0)=1$ for $n=1,2,3, \ldots$, but $P_{n}(z) \rightarrow 0$ for every $z \neq 0$, as $n \rightarrow \infty$ ?

4 Is there a sequence of polynomials $P_{n}$ such that

$$
\lim _{n \rightarrow \infty} P_{n}(z)=\left\{\begin{aligned}
1 & \text { if } \operatorname{Im} z>0 \\
0 & \text { if } z \text { is real } \\
-1 & \text { if } \operatorname{Im} z<0
\end{aligned}\right.
$$

5 For $n=1,2,3, \ldots$, let $\Delta_{n}$ be a closed disc in $U$, and let $L_{n}$ be an arc (a homeomorphic image of $[0,1])$ in $U-\Delta_{n}$ which intersects every radius of $U$. There are polynomials $P_{n}$ which are very small on $\Delta_{n}$ and more or less arbitrary on $L_{n}$. Show that $\left\{\Delta_{n}\right\},\left\{L_{n}\right\}$, and $\left\{P_{n}\right\}$ can be so chosen that the series $f=\Sigma P_{n}$ defines a function $f \in H(U)$ which has no radial limit at any point of $T$. In other words, for no real $\theta$ does $\lim _{r \rightarrow 1} f\left(r e^{i \theta}\right)$ exist.

6 Here is another construction of such a function. Let $\left\{n_{k}\right\}$ be a sequence of integers such that $n_{1}>1$ and $n_{k+1}>2 k n_{k}$. Define

$$
h(z)=\sum_{k=1}^{\infty} 5^{k} z^{n_{k}}
$$

Prove that the series converges if $|z|<1$ and prove that there is a constant $c>0$ such that $|h(z)|>c \cdot 5^{m}$ for all $z$ with $|z|=1-\left(1 / n_{m}\right)$. [Hint: For such $z$ the $m$ th term in the series defining $h(z)$ is much larger than the sum of all the others.]

Hence $h$ has no finite radial limits.

Prove also that $h$ must have infinitely many zeros in $U$. (Compare with Exercise 15, Chap. 12.) In fact, prove that to every complex number $\alpha$ there correspond infinitely many $z \in U$ at which $h(z)=\alpha$.

7 Show that in Theorem 13.9 we need not assume that $A$ intersects each component of $S^{2}-\Omega$. It is enough to assume that the closure of $A$ intersects each component of $S^{2}-\Omega$.

8 Prove the Mittag-Leffler theorem for the case in which $\Omega$ is the whole plane, by a direct argument which makes no appeal to Runge's theorem.

9 Suppose $\Omega$ is a simply connected region, $f \in H(\Omega), f$ has no zero in $\Omega$, and $n$ is a positive integer. Prove that there exists a $g \in H(\Omega)$ such that $g^{n}=f$.

10 Suppose $\Omega$ is a region, $f \in H(\Omega)$, and $f \not \equiv 0$. Prove that $f$ has a holomorphic logarithm in $\Omega$ if and only if $f$ has holomorphic $n$th roots in $\Omega$ for every positive integer $n$.

11 Suppose that $f_{n} \in H(\Omega)(n=1,2,3, \ldots), f$ is a complex function in $\Omega$, and $f(z)=\lim _{n \rightarrow \infty} f_{n}(z)$ for every $z \in \Omega$. Prove that $\Omega$ has a dense open subset $V$ on which $f$ is holomorphic. Hint: Put $\varphi=\sup \left|f_{n}\right|$. Use Baire's theorem to prove that every disc in $\Omega$ contains a disc on which $\varphi$ is bounded. Apply Exercise 5, Chap. 10. (In general, $V \neq \Omega$. Compare Exercises 3 and 4.)

12 Suppose, however, that $f$ is any complex-valued measurable function defined in the complex plane, and prove that there is a sequence of holomorphic polynomials $P_{n}$ such that $\lim _{n \rightarrow \infty} P_{n}(z)=f(z)$ for almost every $z$ (with respect to two-dimensional Lebesgue measure).

## CONFORMAL MAPPING

## Preservation of Angles

14.1 Definition Each complex number $z \neq 0$ determines a direction from the origin, defined by the point

$$
A[z]=\frac{z}{|z|}
$$

on the unit circle.

Suppose $f$ is a mapping of a region $\Omega$ into the plane, $z_{0} \in \Omega$, and $z_{0}$ has a deleted neighborhood $D^{\prime}\left(z_{0} ; r\right) \subset \Omega$ in which $f(z) \neq f\left(z_{0}\right)$. We say that $f$ preserves angles at $z_{0}$ if

$$
\lim _{r \rightarrow 0} e^{-i \theta} A\left[f\left(z_{0}+r e^{i \theta}\right)-f\left(z_{0}\right)\right] \quad(r>0)
$$

exists and is independent of $\theta$.

In less precise language, the requirement is that for any two rays $L^{\prime}$ and $L^{\prime \prime}$, starting at $z_{0}$, the angle which their images $f\left(L^{\prime}\right)$ and $f\left(L^{\prime \prime}\right)$ make at $f\left(z_{0}\right)$ is the same as that made by $L^{\prime}$ and $L^{\prime \prime}$, in size as well as in orientation.

The property of preserving angles at each point of a region is characteristic of holomorphic functions whose derivative has no zero in that region. This is a corollary of Theorem 14.2 and is the reason for calling holomorphic functions with nonvanishing derivative conformal mappings.

14.2 Theorem Let $f$ map a region $\Omega$ into the plane. If $f^{\prime}\left(z_{0}\right)$ exists at some $z_{0} \in \Omega$ and $f^{\prime}\left(z_{0}\right) \neq 0$, then $f$ preserves angles at $z_{0}$. Conversely, if the differential of $f$ exists and is different from 0 at $z_{0}$, and if $f$ preserves angles at $z_{0}$, then $f^{\prime}\left(z_{0}\right)$ exists and is different from 0.

Here $f^{\prime}\left(z_{0}\right)=\lim \left[f(z)-f\left(z_{0}\right)\right] /\left(z-z_{0}\right)$, as usual. The differential of $f$ at $z_{0}$ is a linear transformation $L$ of $R^{2}$ into $R^{2}$ such that, writing $z_{0}=\left(x_{0}, y_{0}\right)$,

$$
f\left(x_{0}+x, y_{0}+y\right)=f\left(x_{0}, y_{0}\right)+L(x, y)+\left(x^{2}+y^{2}\right)^{1 / 2} \eta(x, y)
$$

where $\eta(x, y) \rightarrow 0$ as $x \rightarrow 0$ and $y \rightarrow 0$, as in Definition 7.22.

ProOF Take $z_{0}=f\left(z_{0}\right)=0$, for simplicity. If $f^{\prime}(0)=a \neq 0$, then it is immediate that

$$
e^{-i \theta} A\left[f\left(r e^{i \theta}\right)\right]=\frac{e^{-i \theta} f\left(r e^{i \theta}\right)}{\left|f\left(r e^{i \theta}\right)\right|} \rightarrow \frac{a}{|a|} \quad(r \rightarrow 0)
$$

so $f$ preserves angles at 0 . Conversely, if the differential of $f$ exists at 0 and is different from 0 , then (1) can be rewritten in the form

$$
f(z)=\alpha z+\beta \bar{z}+|z| \eta(z)
$$

where $\eta(z) \rightarrow 0$ as $z \rightarrow 0$, and $\alpha$ and $\beta$ are complex numbers, not both 0 . If $f$ also preserves angles at 0 , then

$$
\lim _{r \rightarrow 0} e^{-i \theta} A\left[f\left(r e^{i \theta}\right)\right]=\frac{\alpha+\beta e^{-2 i \theta}}{\left|\alpha+\beta e^{-2 i \theta}\right|}
$$

exists and is independent of $\theta$. We may exclude those $\theta$ for which the denominator in (4) is 0 ; there are at most two such $\theta$ in $[0,2 \pi)$. For all other $\theta$, we conclude that $\alpha+\beta e^{-2 i \theta}$ lies on a fixed ray through 0 , and this is possible only when $\beta=0$. Hence $\alpha \neq 0$, and (3) implies that $f^{\prime}(0)=\alpha$.

Note: No holomorphic function preserves angles at any point where its derivative is 0 . We omit the easy proof of this. However, the differential of a transformation may be 0 at a point where angles are preserved. Example: $f(z)=$ $|z| z, z_{0}=0$.

## Linear Fractional Transformations

14.3 If $a, b, c$, and $d$ are complex numbers such that $a d-b c \neq 0$, the mapping

$$
z \rightarrow \frac{a z+b}{c z+d}
$$

is called a linear fractional transformation. It is convenient to regard (1) as a mapping of the sphere $S^{2}$ into $S^{2}$, with the obvious conventions concerning the point $\infty$. For instance, $-d / c$ maps to $\infty$ and $\infty$ maps to $a / c$, if $c \neq 0$. It is then easy to see that each linear fractional transformation is a one-to-one mapping of $S^{2}$ onto $S^{2}$. Furthermore, each is obtained by a superposition of transformations of the following types:

(a) Translations: $z \rightarrow z+b$.

(b) Rotations: $z \rightarrow a z,|a|=1$.
(c) Homotheties: $z \rightarrow r z, r>0$.

(d) Inversion: $z \rightarrow 1 / z$.

If $c=0$ in (1), this is obvious. If $c \neq 0$, it follows from the identity

$$
\frac{a z+b}{c z+d}=\frac{a}{c}+\frac{\lambda}{c z+d}, \quad \lambda=\frac{b c-a d}{c}
$$

The first three types evidently carry lines to lines and circles to circles. This is not true of $(d)$. But if we let $\mathscr{F}$ be the family consisting of all straight lines and all circles, then $\mathscr{F}$ is preserved by $(d)$, and hence we have the important result that $\mathscr{F}$ is preserved by every linear fractional transformation. [It may be noted that when $\mathscr{F}$ is regarded as a family of subsets of $S^{2}$, then $\mathscr{F}$ consists of all circles on $S^{2}$, via the stereographic projection $13.1(1)$; we shall not use this property of $\mathscr{F}$ and omit its proof.]

The proof that $\mathscr{F}$ is preserved by inversion is quite easy. Elementary analytic geometry shows that every member of $\mathscr{F}$ is the locus of an equation

$$
\alpha z \bar{z}+\beta z+\bar{\beta} \bar{z}+\gamma=0
$$

where $\alpha$ and $\gamma$ are real constants and $\beta$ is a complex constant, provided that $\beta \bar{\beta}>\alpha \gamma$. If $\alpha \neq 0$, (3) defines a circle; $\alpha=0$ gives the straight lines. Replacement of $z$ by $1 / z$ transforms (3) into

$$
\alpha+\beta \bar{z}+\bar{\beta} z+\gamma z \bar{z}=0
$$

which is an equation of the same type.

Suppose $a, b$, and $c$ are distinct complex numbers. We construct a linear fractional transformation $\varphi$ which maps the ordered triple $\{a, b, c\}$ into $\{0,1, \infty\}$, namely,

$$
\varphi(z)=\frac{(b-c)(z-a)}{(b-a)(z-c)}
$$

There is only one such $\varphi$. For if $\varphi(a)=0$, we must have $z-a$ in the numerator; if $\varphi(c)=\infty$, we must have $z-c$ in the denominator; and if $\varphi(b)=1$, we are led to (5). If $a$ or $b$ or $c$ is $\infty$, formulas analogous to (5) can easily be written down. If we follow (5) by the inverse of a transformation of the same type, we obtain the following result:

For any two ordered triples $\{a, b, c\}$ and $\left\{a^{\prime}, b^{\prime}, c^{\prime}\right\}$ in $S^{2}$ there is one and only one linear fractional transformation which maps a to $a^{\prime}, b$ to $b^{\prime}$, and $c$ to $c^{\prime}$.

(It is of course assumed that $a \neq b, a \neq c$, and $b \neq c$, and likewise for $a^{\prime}, b^{\prime}$, and $c^{\prime}$.)

We conclude from this that every circle can be mapped onto every circle by a linear fractional transformation. Of more interest is the fact that every circle can be mapped onto every straight line (if $\infty$ is regarded as part of the line), and hence that every open disc can be conformally mapped onto every open half plane.

Let us discuss one such mapping more explicitly, namely,

$$
\varphi(z)=\frac{1+z}{1-z}
$$

This $\varphi$ maps $\{-1,0,1\}$ to $\{0,1, \infty\}$; the segment $(-1,1)$ maps onto the positive real axis. The unit circle $T$ passes through -1 and 1 ; hence $\varphi(T)$ is a straight line through $\varphi(-1)=0$. Since $T$ makes a right angle with the real axis at $-1, \varphi(T)$ makes a right angle with the real axis at 0 . Thus $\varphi(T)$ is the imaginary axis. Since $\varphi(0)=1$, it follows that $\varphi$ is a conformal one-to-one mapping of the open unit disc onto the open right half plane.

The role of linear fractional transformations in the theory of conformal mapping is also well illustrated by Theorem 12.6.

14.4 Linear fractional transformations make it possible to transfer theorems concerning the behavior of holomorphic functions near straight lines to situations where circular arcs occur instead. It will be enough to illustrate the method with an informal discussion of the reflection principle.

Suppose $\Omega$ is a region in $U$, bounded in part by an $\operatorname{arc} L$ on the unit circle, and $f$ is continuous on $\bar{\Omega}$, holomorphic in $\Omega$, and real on $L$. The function

$$
\psi(z)=\frac{z-i}{z+i}
$$

maps the upper half plane onto $U$. If $g=f \circ \psi$, Theorem 11.14 gives is a holomorphic extension $G$ of $g$, and then $F=G \circ \psi^{-1}$ gives a holomorphic extension $F$ of $f$ which satisfies the relation

$$
f\left(z^{*}\right)=\overline{F(z)}
$$

where $z^{*}=1 / \bar{z}$.

The last assertion follows from a property of $\psi$ : If $w=\psi(z)$ and $w_{1}=\psi(\bar{z})$, then $w_{1}=w^{*}$, as is easily verified by computation.

Exercises 2 to 5 furnish other applications of this technique.

## Normal Families

The Riemann mapping theorem will be proved by exhibiting the mapping function as the solution of a certain extremum problem. The existence of this solution depends on a very useful compactness property of certain families of holomorphic functions which we now formulate.

14.5 Definition Suppose $\mathscr{F} \subset H(\Omega)$, for some region $\Omega$. We call $\mathscr{F}$ a normal family if every sequence of members of $\mathscr{F}$ contains a subsequence which converges uniformly on compact subsets of $\Omega$. The limit function is not required to belong to $\mathscr{F}$.

(Sometimes a wider definition is adopted, by merely requiring that every sequence in $\mathscr{F}$ either converges or tends to $\infty$, uniformly on compact subsets of $\Omega$. This is well adapted for dealing with meromorphic functions.)

14.6 Theorem Suppose $\mathscr{F} \subset H(\Omega)$ and $\mathscr{F}$ is uniformly bounded on each compact subset of the region $\Omega$. Then $\mathscr{F}$ is a normal family.

ProOF The hypothesis means that to each compact $K \subset \Omega$ there corresponds a number $M(K)<\infty$ such that $|f(z)| \leq M(K)$ for all $f \in \mathscr{F}$ and all $z \in K$.

Let $\left\{K_{n}\right\}$ be a sequence of compact sets whose union is $\Omega$, such that $K_{n}$ lies in the interior of $K_{n+1}$; such a sequence was constructed in Theorem 13.3. Then there exist positive numbers $\delta_{n}$ such that

$$
D\left(z ; 2 \delta_{n}\right) \subset K_{n+1} \quad\left(z \in K_{n}\right)
$$

Consider two points $z^{\prime}$ and $z^{\prime \prime}$ in $K_{n}$, such that $\left|z^{\prime}-z^{\prime \prime}\right|<\delta_{n}$, let $\gamma$ be the positively oriented circle with center at $z^{\prime}$ and radius $2 \delta_{n}$, and estimate $\left|f\left(z^{\prime}\right)-f\left(z^{\prime \prime}\right)\right|$ by the Cauchy formula. Since

$$
\frac{1}{\zeta-z^{\prime}}-\frac{1}{\zeta-z^{\prime \prime}}=\frac{z^{\prime}-z^{\prime \prime}}{\left(\zeta-z^{\prime}\right)\left(\zeta-z^{\prime \prime}\right)}
$$

we have

$$
f\left(z^{\prime}\right)-f\left(z^{\prime \prime}\right)=\frac{z^{\prime}-z^{\prime \prime}}{2 \pi i} \int_{\gamma} \frac{f(\zeta)}{\left(\zeta-z^{\prime}\right)\left(\zeta-z^{\prime \prime}\right)} d \zeta
$$

and since $\left|\zeta-z^{\prime}\right|=2 \delta_{n}$ and $\left|\zeta-z^{\prime \prime}\right|>\delta_{n}$ for all $\zeta \in \gamma^{*}$, (2) gives the inequality

$$
\left|f\left(z^{\prime}\right)-f\left(z^{\prime \prime}\right)\right|<\frac{M\left(K_{n+1}\right)}{\delta_{n}}\left|z^{\prime}-z^{\prime \prime}\right|
$$

valid for all $f \in \mathscr{F}$ and all $z^{\prime}$ and $z^{\prime \prime} \in K_{n}$, provided that $\left|z^{\prime}-z^{\prime \prime}\right|<\delta_{n}$.

This was the crucial step in the proof: We have proved, for each $K_{n}$, that the restrictions of the members of $\mathscr{F}$ to $K_{n}$ form an equicontinuous family.

If $f_{j} \in \mathscr{F}$, for $j=1,2,3, \ldots$, Theorem 11.28 implies therefore that there are infinite sets $S_{n}$ of positive integers, $S_{1} \supset S_{2} \supset S_{3} \supset \cdots$, so that $\left\{f_{j}\right\}$ converges uniformly on $K_{n}$ as $j \rightarrow \infty$ within $S_{n}$. The diagonal process yields then an infinite set $S$ such that $\left\{f_{j}\right\}$ converges uniformly on every $K_{n}$ (and hence on every compact $K \subset \Omega$ ) as $j \rightarrow \infty$ within $S$.

## The Riemann Mapping Theorem

14.7 Conformal Equivalence We call two regions $\Omega_{1}$ and $\Omega_{2}$ conformally equivalent if there exists a $\varphi \in H\left(\Omega_{1}\right)$ such that $\varphi$ is one-to-one in $\Omega_{1}$ and such that $\varphi\left(\Omega_{1}\right)=\Omega_{2}$, i.e., if there exists a conformal one-to-one mapping of $\Omega_{1}$ onto $\Omega_{2}$.

Under these conditions, the inverse of $\varphi$ is holomorphic in $\Omega_{2}$ (Theorem 10.33) and hence is a conformal mapping of $\Omega_{2}$ onto $\Omega_{1}$.

It follows that conformally equivalent regions are homeomorphic. But there is a much more important relation between conformally equivalent regions: If $\varphi$ is as above, $f \rightarrow f \circ \varphi$ is a one-to-one mapping of $H\left(\Omega_{2}\right)$ onto $H\left(\Omega_{1}\right)$ which preserves sums and products, i.e., which is a ring isomorphism of $H\left(\Omega_{2}\right)$ onto $H\left(\Omega_{1}\right)$. If $\Omega_{1}$ has a simple structure, problems about $H\left(\Omega_{2}\right)$ can be transferred to problems in $H\left(\Omega_{1}\right)$ and the solutions can be carried back to $H\left(\Omega_{2}\right)$ with the aid of the mapping function $\varphi$. The most important case of this is based on the Riemann mapping theorem (where $\Omega_{2}$ is the unit disc $U$ ), which reduces the study of $H(\Omega)$ to the study of $H(U)$, for any simply connected proper subregion of the plane. Of course, for explicit solutions of problems, it may be necessary to have rather precise information about the mapping function.

14.8 Theorem Every simply connected region $\Omega$ in the plane (other than the plane itself) is conformally equivalent to the open unit disc $U$.

Note: The case of the plane clearly has to be excluded, by Liouville's theorem. Thus the plane is not conformally equivalent to $U$, although the two regions are homeomorphic.

The only property of simply connected regions which will be used in the proof is that every holomorphic function which has no zero in such a region has a holomorphic square root there. This will furnish the conclusion " $(j)$ implies $(a)$ " in Theorem 13.11 and will thus complete the proof of that theorem.

Proof Suppose $\Omega$ is a simply connected region in the plane and let $w_{0}$ be a complex number, $w_{0} \notin \Omega$. Let $\Sigma$ be the class of all $\psi \in H(\Omega)$ which are oneto-one in $\Omega$ and which map $\Omega$ into $U$. We have to prove that some $\psi \in \Sigma$ maps $\Omega$ onto $U$.

We first prove that $\Sigma$ is not empty. Since $\Omega$ is simply connected, there exists a $\varphi \in H(\Omega)$ so that $\varphi^{2}(z)=z-w_{0}$ in $\Omega$. If $\varphi\left(z_{1}\right)=\varphi\left(z_{2}\right)$, then also $\varphi^{2}\left(z_{1}\right)=\varphi^{2}\left(z_{2}\right)$, hence $z_{1}=z_{2}$; thus $\varphi$ is one-to-one. The same argument shows that there are no two distinct points $z_{1}$ and $z_{2}$ in $\Omega$ such that $\varphi\left(z_{1}\right)=$ $-\varphi\left(z_{2}\right)$. Since $\varphi$ is an open mapping, $\varphi(\Omega)$ contains a disc $D(a ; r)$, with $0<r<|a|$. The disc $D(-a ; r)$ therefore fails to intersect $\varphi(\Omega)$, and if we define $\psi=r /(\varphi+a)$, we see that $\psi \in \Sigma$.

The next step consists in showing that if $\psi \in \Sigma$, if $\psi(\Omega)$ does not cover all of $U$, and if $z_{0} \in \Omega$, then there exists a $\psi_{1} \in \Sigma$ with

$$
\left|\psi_{1}^{\prime}\left(z_{0}\right)\right|>\left|\psi^{\prime}\left(z_{0}\right)\right| .
$$

It will be convenient to use the functions $\varphi_{\alpha}$ defined by

$$
\varphi_{\alpha}(z)=\frac{z-\alpha}{1-\bar{\alpha} z} .
$$

For $\alpha \in U, \varphi_{\alpha}$ is a one-to-one mapping of $U$ onto $U$; its inverse is $\varphi_{-\alpha}$ (Theorem 12.4).

Suppose $\psi \in \Sigma, \alpha \in U$, and $\alpha \notin \psi(\Omega)$. Then $\varphi_{\alpha} \circ \psi \in \Sigma$, and $\varphi_{\alpha} \circ \psi$ has no zero in $\Omega$; hence there exists a $g \in H(\Omega)$ such that $g^{2}=\varphi_{\alpha} \circ \psi$. We see that $g$ is one-to-one (as in the proof that $\Sigma \neq \varnothing$ ), hence $g \in \Sigma$; and if $\psi_{1}=\varphi_{\beta} \circ g$, where $\beta=g\left(z_{0}\right)$, it follows that $\psi_{1} \in \Sigma$. With the notation $w^{2}=s(w)$, we now have

$$
\psi=\varphi_{-\alpha} \circ S \circ g=\varphi_{-\alpha} \circ S \circ \varphi_{-\beta} \circ \psi_{1} .
$$

Since $\psi_{1}\left(z_{0}\right)=0$, the chain rule gives

$$
\psi^{\prime}\left(z_{0}\right)=F^{\prime}(0) \psi_{1}^{\prime}\left(z_{0}\right)
$$

where $F=\varphi_{-\alpha} \circ S \circ \varphi_{-\beta}$. We see that $F(U) \subset U$ and that $F$ is not one-toone in $U$. Therefore $\left|F^{\prime}(0)\right|<1$, by the Schwarz lemma (see Sec. 12.5), so that $\left|\psi^{\prime}\left(z_{0}\right)\right|<\left|\psi_{1}^{\prime}\left(z_{0}\right)\right|$. [Note that $\psi^{\prime}\left(z_{0}\right) \neq 0$, since $\psi$ is one-to-one in $\Omega$.]

Fix $z_{0} \in \Omega$, and put

$$
\eta=\sup \left\{\left|\psi^{\prime}\left(z_{0}\right)\right|: \psi \in \Sigma\right\} .
$$

The foregoing makes it clear that any $h \in \Sigma$ for which $\left|h^{\prime}\left(z_{0}\right)\right|=\eta$ will map $\Omega$ onto $U$. Hence the proof will be completed as soon as we prove the existence of such an $h$.

Since $|\psi(z)|<1$ for all $\psi \in \Sigma$ and $z \in \Omega$, Theorem 14.6 shows that $\Sigma$ is a normal family. The definition of $\eta$ shows that there is a sequence $\left\{\psi_{n}\right\}$ in $\Sigma$ such that $\left|\psi_{n}^{\prime}\left(z_{0}\right)\right| \rightarrow \eta$, and by normality of $\Sigma$ we can extract a subsequence (again denoted by $\left\{\psi_{n}\right\}$, for simplicity) which converges, uniformly on compact subsets of $\Omega$, to a limit $h \in H(\Omega)$. By Theorem 10.28, $\left|h^{\prime}\left(z_{0}\right)\right|=\eta$. Since $\Sigma \neq \varnothing, \eta>0$, so $h$ is not constant. Since $\psi_{n}(\Omega) \subset U$, for $n=1,2,3, \ldots$, we have $h(\Omega) \subset \bar{U}$, but the open mapping theorem shows that actually $h(\Omega) \subset U$.

So all that remains to be shown is that $h$ is one-to-one. Fix distinct points $z_{1}$ and $z_{2} \in \Omega$; put $\alpha=h\left(z_{1}\right)$ and $\alpha_{n}=\psi_{n}\left(z_{1}\right)$ for $n=1,2,3, \ldots$; and let $\bar{D}$ be a closed circular disc in $\Omega$ with center at $z_{2}$, such that $z_{1} \notin \bar{D}$ and such that $h-\alpha$ has no zero on the boundary of $\bar{D}$. This is possible, since the zeros of $h-\alpha$ have no limit point in $\Omega$. The functions $\psi_{n}-\alpha_{n}$ converge to $h-\alpha$, uniformly on $\bar{D}$; they have no zero in $D$ since they are one-to-one and have a zero at $z_{1}$; it now follows from Rouché's theorem that $h-\alpha$ has no zero in $D$; in particular, $h\left(z_{2}\right) \neq h\left(z_{1}\right)$.

Thus $h \in \Sigma$, and the proof is complete.

14.9 Remarks The preceding proof also shows that $h\left(z_{0}\right)=0$. For if $h\left(z_{0}\right)=\beta$ and $\beta \neq 0$, then $\varphi_{\beta} \circ h \in \Sigma$, and

$$
\left|\left(\varphi_{\beta} \circ h\right)^{\prime}\left(z_{0}\right)\right|=\left|\varphi_{\beta}^{\prime}(\beta) h^{\prime}\left(z_{0}\right)\right|=\frac{\left|h^{\prime}\left(z_{0}\right)\right|}{1-|\beta|^{2}}>\left|h^{\prime}\left(z_{0}\right)\right|
$$

It is interesting to observe that although $h$ was obtained by maximizing $\left|\psi^{\prime}\left(z_{0}\right)\right|$ for $\psi \in \Sigma, h$ also maximizes $\left|f^{\prime}\left(z_{0}\right)\right|$ if $f$ is allowed to range over the class consisting of all holomorphic mappings of $\Omega$ into $U$ (not necessarily one-to-one). For if $f$ is such a function, then $g=f \circ h^{-1}$ maps $U$ into $U$, hence $\left|g^{\prime}(0)\right| \leq 1$, with equality holding (by the Schwarz lemma) if and only if $g$ is a rotation, so the chain rule gives the following result:

If $f \in H(\Omega), f(\Omega) \subset U$, and $z_{0} \in \Omega$, then $\left|f^{\prime}\left(z_{0}\right)\right| \leq\left|h^{\prime}\left(z_{0}\right)\right|$. Equality holds if and only if $f(z)=\lambda h(z)$, for some constant $\lambda$ with $|\lambda|=1$.

## The Class $\mathscr{S}$

14.10 Definition $\mathscr{S}$ is the class of all $f \in H(U)$ which are one-to-one in $U$ and which satisfy

$$
f(0)=0, \quad f^{\prime}(0)=1
$$

Thus every $f \in \mathscr{S}$ has a power series expansion

$$
f(z)=z+\sum_{n=2}^{\infty} a_{n} z^{n} \quad(z \in U)
$$

The class $\mathscr{S}$ is not closed under addition or multiplication, but has many other interesting properties. We shall develop only a few of these in this section. Theorem 14.15 will be used in the proof of Mergelyan's theorem, in Chap. 20.

14.11 Example If $|\alpha| \leq 1$ and

$$
f_{\alpha}(z)=\frac{z}{(1-\alpha z)^{2}}=\sum_{n=1}^{\infty} n \alpha^{n-1} z^{n}
$$

then $f_{\alpha} \in \mathscr{S}$.

For if $f_{\alpha}(z)=f_{\alpha}(w)$, then $(z-w)\left(1-\alpha^{2} z w\right)=0$, and the second factor is not 0 if $|z|<1$ and $|w|<1$.

When $|\alpha|=1, f_{\alpha}$ is called a Koebe function. We leave it as an exercise to find the regions $f_{\alpha}(U)$.

14.12 Theorem (a) If $f \in \mathscr{S},|\alpha|=1$, and $g(z)=\bar{\alpha} f(\alpha z)$, then $g \in \mathscr{S}$. (b) If $f \in \mathscr{S}$ there exists a $g \in \mathscr{S}$ such that

$$
g^{2}(z)=f\left(z^{2}\right) \quad(z \in U)
$$

Proof $(a)$ is clear. To prove $(b)$, write $f(z)=z \varphi(z)$. Then $\varphi \in H(U), \varphi(0)=1$, and $\varphi$ has no zero in $U$, since $f$ has no zero in $U-\{0\}$. Hence there exists an $h \in H(U)$ with $h(0)=1, h^{2}(z)=\varphi(z)$. Put

$$
g(z)=z h\left(z^{2}\right) \quad(z \in U) .
$$

Then $g^{2}(z)=z^{2} h^{2}\left(z^{2}\right)=z^{2} \varphi\left(z^{2}\right)=f\left(z^{2}\right)$, so that (1) holds. It is clear that $g(0)=0$ and $g^{\prime}(0)=1$. We have to show that $g$ is one-to-one.

Suppose $z$ and $w \in U$ and $g(z)=g(w)$. Since $f$ is one-to-one, (1) implies that $z^{2}=w^{2}$. So either $z=w$ (which is what we want to prove) or $z=-w$. In the latter case, (2) shows that $g(z)=-g(w)$; it follows that $g(z)=g(w)=0$, and since $g$ has no zero in $U-\{0\}$, we have $z=w=0$.

14.13 Theorem If $F \in H(U-\{0\}), F$ is one-to-one in $U$, and

$$
F(z)=\frac{1}{z}+\sum_{n=0}^{\infty} \alpha_{n} z^{n} \quad(z \in U)
$$

then

$$
\sum_{n=1}^{\infty} n\left|\alpha_{n}\right|^{2} \leq 1
$$

This is usually called the area theorem, for reasons which will become apparent in the proof.

Proof The choice of $\alpha_{0}$ is clearly irrelevant. So assume $\alpha_{0}=0$. Neither the hypothesis nor the conclusion is affected if we replace $F(z)$ by $\lambda F(\lambda z)$ $(|\lambda|=1)$. So we may assume that $\alpha_{1}$ is real.

Put $U_{r}=\{z:|z|<r\}, C_{r}=\{z:|z|=r\}$, and $V_{r}=\{z: r<|z|<1\}$, for $0<r<1$. Then $F\left(U_{r}\right)$ is a neighborhood of $\infty$ (by the open mapping theorem, applied to $1 / F)$; the sets $F\left(U_{r}\right), F\left(C_{r}\right)$, and $F\left(V_{r}\right)$ are disjoint, since $F$ is one-to-one. Write

$$
F(z)=\frac{1}{z}+\alpha_{1} z+\varphi(z) \quad(z \in U)
$$

$F=u+i v$, and

$$
A=\frac{1}{r}+\alpha_{1} r, \quad B=\frac{1}{r}-\alpha_{1} r .
$$

For $z=r e^{i \theta}$, we then obtain

$$
u=A \cos \theta+\operatorname{Re} \varphi \quad \text { and } \quad v=-B \sin \theta+\operatorname{Im} \varphi
$$

Divide Eqs. (5) by $A$ and $B$, respectively, square, and add:

$$
\frac{u^{2}}{A^{2}}+\frac{v^{2}}{B^{2}}=1+\frac{2 \cos \theta}{A} \operatorname{Re} \varphi+\left(\frac{\operatorname{Re} \varphi}{A}\right)^{2}-\frac{2 \sin \theta}{B} \operatorname{Im} \varphi+\left(\frac{\operatorname{Im} \varphi}{B}\right)^{2}
$$

By (3), $\varphi$ has a zero of order at least 2 at the origin. If we keep account of (4), it follows that there exists an $\eta>0$ such that, for all sufficiently small $r$,

$$
\frac{u^{2}}{A^{2}}+\frac{v^{2}}{B^{2}}<1+\eta r^{3} \quad\left(z=r e^{i \theta}\right)
$$

This says that $F\left(C_{r}\right)$ is in the interior of the ellipse $E_{r}$ whose semiaxes are $A \sqrt{1+\eta r^{3}}$ and $B \sqrt{1+\eta r^{3}}$, and which therefore bounds an area

$$
\pi A B\left(1+\eta r^{3}\right)=\pi\left(\frac{1}{r}+\alpha_{1} r\right)\left(\frac{1}{r}-\alpha_{1} r\right)\left(1+\eta r^{3}\right) \leq \frac{\pi}{r^{2}}\left(1+\eta r^{3}\right)
$$

Since $F\left(C_{r}\right)$ is in the interior of $E_{r}$, we have $E_{r} \subset F\left(U_{r}\right)$; hence $F\left(V_{r}\right)$ is in the interior of $E_{r}$, so the area of $F\left(V_{r}\right)$ is no larger than (7). The CauchyRiemann equations show that the Jacobian of the mapping $(x, y) \rightarrow(u, v)$ is $\left|F^{\prime}\right|^{2}$. Theorem 7.26 therefore gives the following result:

$$
\begin{aligned}
\frac{\pi}{r^{2}}\left(1+\eta r^{3}\right) & \geq \iint_{V_{r}}\left|F^{\prime}\right|^{2} \\
& =\int_{r}^{1} t d t \int_{0}^{2 \pi}\left|-t^{-2} e^{-2 i \theta}+\sum_{1}^{\infty} n \alpha_{n} t^{n-1} e^{i(n-1) \theta}\right|^{2} d \theta \\
& =2 \pi \int_{r}^{1}\left(t^{-3}+\sum_{1}^{\infty} n^{2}\left|\alpha_{n}\right|^{2} t^{2 n-1}\right) d t \\
& =\pi\left\{r^{-2}-1+\sum_{1}^{\infty} n\left|\alpha_{n}\right|^{2}\left(1-r^{2 n}\right)\right\}
\end{aligned}
$$

If we divide (8) by $\pi$ and then subtract $r^{-2}$ from each side, we obtain

$$
\sum_{n=1}^{N} n\left|\alpha_{n}\right|^{2}\left(1-r^{2 n}\right) \leq 1+\eta r
$$

for all sufficiently small $r$ and for all positive integers $N$. Let $r \rightarrow 0$ in (9), then let $N \rightarrow \infty$. This gives (2).

Corollary Under the same hypothesis, $\left|\alpha_{1}\right| \leq 1$.

That this is in fact best possible is shown by $F(z)=(1 / z)+\alpha z,|\alpha|=1$, which is one-to-one in $U$.

14.14 Theorem If $f \in \mathscr{S}$, and

$$
f(z)=z+\sum_{n=2}^{\infty} a_{n} z^{n}
$$

then $(a)\left|a_{2}\right| \leq 2$, and $(b) f(U) \supset D\left(0 ; \frac{1}{4}\right)$.

The second assertion is that $f(U)$ contains all $w$ with $|w|<\frac{1}{4}$.

ProOF By Theorem 14.12 , there exists a $g \in \mathscr{S}$ so that $g^{2}(z)=f\left(z^{2}\right)$. If $G=1 / g$, then Theorem 14.13 applies to $G$, and this will give $(a)$. Since

$$
f\left(z^{2}\right)=z^{2}\left(1+a_{2} z^{2}+\cdots\right)
$$

we have

$$
g(z)=z\left(1+\frac{1}{2} a_{2} z^{2}+\cdots\right)
$$

and hence

$$
G(z)=\frac{1}{z}\left(1-\frac{1}{2} a_{2} z^{2}+\cdots\right)=\frac{1}{z}-\frac{a_{2}}{2} z+\cdots .
$$

The Corollary to Theorem 14.13 shows now that $\left|a_{2}\right| \leq 2$.

To prove $(b)$, suppose $w \notin f(U)$. Define

$$
h(z)=\frac{f(z)}{1-f(z) / w}
$$

Then $h \in H(U), h$ is one-to-one in $U$, and

$$
h(z)=\left(z+a_{2} z^{2}+\cdots\right)\left(1+\frac{z}{w}+\cdots\right)=z+\left(a_{2}+\frac{1}{w}\right) z^{2}+\cdots,
$$

so that $h \in \mathscr{S}$. Apply $(a)$ to $h$ : We have $\left|a_{2}+(1 / w)\right| \leq 2$, and since $\left|a_{2}\right| \leq 2$, we finally obtain $|1 / w| \leq 4$. So $|w| \geq \frac{1}{4}$ for every $w \notin f(U)$.

This completes the proof.

Example 14.11 shows that both $(a)$ and $(b)$ are best possible.

Moreover, given any $\alpha \neq 0$, one can find entire functions $f$, with $f(0)=0$, $f^{\prime}(0)=1$, that omit the value $\alpha$. For example,

$$
f(z)=\alpha\left(1-e^{-z / \alpha}\right) .
$$

Of course, no such $f$ can be one-to-one in $U$ if $|\alpha|<\frac{1}{4}$.

14.15 Theorem Suppose $F \in H(U-\{0\}), F$ is one-to-one in $U, F$ has a pole of order 1 at $z=0$, with residue 1 , and neither $w_{1}$ nor $w_{2}$ are in $F(U)$.

Then $\left|w_{1}-w_{2}\right| \leq 4$.

Proof If $f=1 /\left(F-w_{1}\right)$, then $f \in \mathscr{S}$, hence $f(U) \supset D\left(0, \frac{1}{4}\right)$, so the image of $U$ under $F-w_{1}$ contains all $w$ with $|w|>4$. Since $w_{2}-w_{1}$ is not in this image, we have $\left|w_{2}-w_{1}\right| \leq 4$.

Note that this too is best possible: If $F(z)=z^{-1}+z$, then $F(U)$ does not contain the points $2,-2$. In fact, the complement of $F(U)$ is precisely the interval $[-2,2]$ on the real axis.

## Continuity at the Boundary

Under certain conditions, every conformal mapping of a simply connected region $\Omega$ onto $U$ can be extended to a homeomorphism of its closure $\bar{\Omega}$ onto $\bar{U}$. The nature of the boundary of $\Omega$ plays a decisive role here.

14.16 Definition A boundary point $\beta$ of a simply connected plane region $\Omega$ will be called a simple boundary point of $\Omega$ if $\beta$ has the following property: To every sequence $\left\{\alpha_{n}\right\}$ in $\Omega$ such that $\alpha_{n} \rightarrow \beta$ as $n \rightarrow \infty$ there corresponds a curve $\gamma$, with parameter interval $[0,1]$, and a sequence $\left\{t_{n}\right\}, 0<t_{1}<t_{2}<$ $\cdots, t_{n} \rightarrow 1$, such that $\gamma\left(t_{n}\right)=\alpha_{n}(n=1,2,3, \ldots)$ and $\gamma(t) \in \Omega$ for $0 \leq t<1$.

In other words, there is a curve in $\Omega$ which passes through the points $\alpha_{n}$ and which ends at $\beta$.

14.17 Examples Since examples of simple boundary points are obvious, let us look at some that are not simple.

If $\Omega$ is $U-\{x: 0 \leq x<1\}$, then $\Omega$ is simply connected; and if $0<\beta \leq 1$, $\beta$ is a boundary point of $\Omega$ which is not simple.

To get a more complicated example, let $\Omega_{0}$ be the interior of the square with vertices at the points $0,1,1+i$, and $i$. Remove the intervals

$$
\left[\frac{1}{2 n}, \frac{1}{2 n}+\frac{n-1}{n} i\right] \text { and }\left[\frac{1}{2 n+1}+\frac{i}{n}, \frac{1}{2 n+1}+i\right]
$$

from $\Omega_{0}$. The resulting region $\Omega$ is simply connected. If $0 \leq y \leq 1$, then $i y$ is a boundary point which is not simple.

14.18 Theorem Let $\Omega$ be a bounded simply connected region in the plane, and let $f$ be a conformal mapping of $\Omega$ onto $U$.

(a) If $\beta$ is a simple boundary point of $\Omega$, then $f$ has a continuous extension to $\Omega \cup\{\beta\}$. If $f$ is so extended, then $|f(\beta)|=1$.

(b) If $\beta_{1}$ and $\beta_{2}$ are distinct simple boundary points of $\Omega$ and if $f$ is extended to $\Omega \cup\left\{\beta_{1}\right\} \cup\left\{\beta_{2}\right\}$ as in $(a)$, then $f\left(\beta_{1}\right) \neq f\left(\beta_{2}\right)$.

Proof Let $g$ be the inverse of $f$. Then $g \in H(U)$, by Theorem 10.33, $g(U)=\Omega$, $g$ is one-to-one, and $g \in H^{\infty}$, since $\Omega$ is bounded.

Suppose $(a)$ is false. Then there is a sequence $\left\{\alpha_{n}\right\}$ in $\Omega$ such that $\alpha_{n} \rightarrow \beta$, $f\left(\alpha_{2 n}\right) \rightarrow w_{1}, f\left(\alpha_{2 n+1}\right) \rightarrow w_{2}$, and $w_{1} \neq w_{2}$. Choose $\gamma$ as in Definition 14.16, and put $\Gamma(t)=f(\gamma(t))$, for $0 \leq t<1$. Put $K_{r}=g(\bar{D}(0 ; r))$, for $0<r<1$. Then $K_{r}$ is a compact subset of $\Omega$. Since $\gamma(t) \rightarrow \beta$ as $t \rightarrow 1$, there exists a $t^{*}<1$ (depending on $r$ ) such that $\gamma(t) \notin K_{r}$ if $t^{*}<t<1$. Thus $|\Gamma(t)|>r$ if $t^{*}<t<1$. This says that $|\Gamma(t)| \rightarrow 1$ as $t \rightarrow 1$. Since $\Gamma\left(t_{2 n}\right) \rightarrow w_{1}$ and $\Gamma\left(t_{2 n+1}\right) \rightarrow w_{2}$, we also have $\left|w_{1}\right|=\left|w_{2}\right|=1$.

It now follows that one of the two open arcs $J$ whose union is $T-\left(\left\{w_{1}\right\} \cup\left\{w_{2}\right\}\right)$ has the property that every radius of $U$ which ends at a point of $J$ intersects the range of $\Gamma$ in a set which has a limit point on $T$. Note that $g(\Gamma(t))=\gamma(t)$ for $0 \leq t<1$ and that $g$ has radial limits a.e. on $T$, since $g \in H^{\infty}$. Hence

$$
\lim _{r \rightarrow 1} g\left(r e^{i t}\right)=\beta \quad(\text { a.e. on } J)
$$

since $g(\Gamma(t)) \rightarrow \beta$ as $t \rightarrow 1$. By Theorem 11.32, applied to $g-\beta$, (1) shows that $g$ is constant. But $g$ is one-to-one in $U$, and we have a contradiction. Thus $w_{1}=w_{2}$, and $(a)$ is proved.

Suppose $(b)$ is false. If we multiply $f$ by a suitable constant of absolute value 1 , we then have $\beta_{1} \neq \beta_{2}$ but $f\left(\beta_{1}\right)=f\left(\beta_{2}\right)=1$.

Since $\beta_{1}$ and $\beta_{2}$ are simple boundary points of $\Omega$, there are curves $\gamma_{i}$ with parameter interval $[0,1]$ such that $\gamma_{i}([0,1)) \subset \Omega$ for $i=1$ and 2 and $\gamma_{i}(1)=$ $\beta_{i}$. Put $\Gamma_{i}(t)=f\left(\gamma_{i}(t)\right)$. Then $\Gamma_{i}([0,1)) \subset U$, and $\Gamma_{1}(1)=\Gamma_{2}(1)=1$. Since $g\left(\Gamma_{i}(t)\right)=\gamma_{i}(t)$ on $[0,1)$, we have

$$
\lim _{t \rightarrow 1} g\left(\Gamma_{i}(t)\right)=\beta_{i} \quad(i=1,2)
$$

Theorem 12.10 implies therefore that the radial limit of $g$ at 1 is $\beta_{1}$ as well as $\beta_{2}$. This is impossible if $\beta_{1} \neq \beta_{2}$.

14.19 Theorem If $\Omega$ is a bounded simply connected region in the plane and if every boundary point of $\Omega$ is simple, then every conformal mapping of $\Omega$ onto $U$ extends to a homeomorphism of $\bar{\Omega}$ onto $\bar{U}$.

Proof Suppose $f \in H(\Omega), f(\Omega)=U$, and $f$ is one-to-one. By Theorem 14.18 we can extend $f$ to a mapping of $\bar{\Omega}$ into $\bar{U}$ such that $f\left(\alpha_{n}\right) \rightarrow f(z)$ whenever $\left\{\alpha_{n}\right\}$ is a sequence in $\Omega$ which converges to $z$. If $\left\{z_{n}\right\}$ is a sequence in $\bar{\Omega}$ which converges to $z$, there exist points $\alpha_{n} \in \Omega$ such that $\left|\alpha_{n}-z_{n}\right|<1 / n$ and $\left|f\left(\alpha_{n}\right)-f\left(z_{n}\right)\right|<1 / n$. Thus $\alpha_{n} \rightarrow z$, hence $f\left(\alpha_{n}\right) \rightarrow f(z)$, and this shows that $f\left(z_{n}\right) \rightarrow f(z)$.

We have now proved that our extension of $f$ is continuous on $\bar{\Omega}$. Also $U \subset f(\bar{\Omega}) \subset \bar{U}$. The compactness of $\bar{U}$ implies that $f(\bar{\Omega})$ is compact. Hence $f(\bar{\Omega})=\bar{U}$.

Theorem $14.18(b)$ shows that $f$ is one-to-one on $\bar{\Omega}$. Since every continuous one-to-one mapping of a compact set has a continuous inverse ([26], Theorem 4.17), the proof is complete.

### 14.20 Remarks

(a) The preceding theorem has a purely topological corollary: If every boundary point of a bounded simply connected plane region $\Omega$ is simple, then the boundary of $\Omega$ is a Jordan curve, and $\bar{\Omega}$ is homeomorphic to $\bar{U}$. circle.)

(A Jordan curve is, by definition, a homeomorphic image of the unit

The converse is true, but we shall not prove it: If the boundary of $\Omega$ is a Jordan curve, then every boundary point of $\Omega$ is simple.

(b) Suppose $f$ is as in Theorem $14.19, a, b$, and $c$ are distinct boundary points of $\Omega$, and $A, B$, and $C$ are distinct points of $T$. There is a linear fractional transformation $\varphi$ which maps the triple $\{f(a), f(b), f(c)\}$ to $\{A, B, C\}$; suppose the orientation of $\{A, B, C\}$ agrees with that of $\{f(a), f(b), f(c)\}$; then $\varphi(U)=U$, and the function $g=\varphi \circ f$ is a homeomorphism of $\bar{\Omega}$ onto $\bar{U}$ which is holomorphic in $\Omega$ and which maps $\{a, b, c\}$ to prescribed values $\{A, B, C\}$. It follows from Sec. 14.3 that $g$ is uniquely determined by these requirements.

(c) Theorem 14.19, as well as the above remark (b), extends without difficulty to simply connected regions $\Omega$ in the Riemann sphere $S_{2}$, all of whose boundary points are simple, provided that $S^{2}-\Omega$ has a nonempty interior, for then a linear fractional transformation brings us back to the case in which $\Omega$ is a bounded region in the plane. Likewise, $U$ can be replaced, for instance, by a half plane.

(d) More generally, if $f_{1}$ and $f_{2} \operatorname{map} \Omega_{1}$ and $\Omega_{2}$ onto $U$, as in Theorem 14.19, then $f=f_{2}^{-1} \circ f_{1}$ is a homeomorphism of $\bar{\Omega}_{1}$ onto $\bar{\Omega}_{2}$ which is holomorphic in $\Omega_{1}$.

## Conformal Mapping of an Annulus

14.21 It is a consequence of the Riemann mapping theorem that any two simply connected proper subregions of the plane are conformally equivalent, since each of them is conformally equivalent to the unit disc. This is a very special property of simply connected regions. One may ask whether it extends to the next simplest situation, i.e., whether any two annuli are conformally equivalent. The answer is negative.

For $0<r<R$, let

$$
A(r, R)=\{z: r<|z|<R\}
$$

be the annulus with inner radius $r$ and outer radius $R$. If $\lambda>0$, the mapping $z \rightarrow \lambda z$ maps $A(r, R)$ onto $A(\lambda r, \lambda R)$. Hence $A(r, R)$ and $A\left(r_{1}, R_{1}\right)$ are conformally equivalent if $R / r=R_{1} / r_{1}$. The surprising fact is that this sufficient condition is
also necessary; thus among the annuli there is a different conformal type associated with each real number greater than 1 .

14.22 Theorem $A\left(r_{1}, R_{1}\right)$ and $A\left(r_{2}, R_{2}\right)$ are conformally equivalent if and only if $R_{1} / r_{1}=R_{2} / r_{2}$.

ProOF Assume $r_{1}=r_{2}=1$, without loss of generality. Put

$$
A_{1}=A\left(1, R_{1}\right), \quad A_{2}=A\left(1, R_{2}\right)
$$

and assume there exists $f \in H\left(A_{1}\right)$ such that $f$ is one-to-one and $f\left(A_{1}\right)=A_{2}$. Let $K$ be the circle with center at 0 and radius $r=\sqrt{R_{2}}$. Since $f^{-1}: A_{2} \rightarrow A_{1}$ is also holomorphic, $f^{-1}(K)$ is compact. Hence

$$
A(1,1+\epsilon) \cap f^{-1}(K)=\varnothing
$$

for some $\epsilon>0$. Then $V=f(A(1,1+\epsilon))$ is a connected subset of $A_{2}$ which does not intersect $K$, so that $V \subset A(1, r)$ or $V \subset A\left(r, R_{2}\right)$. In the latter case, replace $f$ by $R_{2} / f$. So we can assume that $V \subset A(1, r)$. If $1<\left|z_{n}\right|<1+\epsilon$ and $\left|z_{n}\right| \rightarrow 1$, then $f\left(z_{n}\right) \in V$ and $\left\{f\left(z_{n}\right)\right\}$ has no limit point in $A_{2}$ (since $f^{-1}$ is continuous); thus $\left|f\left(z_{n}\right)\right| \rightarrow 1$. In the same manner we see that $\left|f\left(z_{n}\right)\right| \rightarrow R_{2}$ if $\left|z_{n}\right| \rightarrow R_{1}$.

Now define

$$
\alpha=\frac{\log R_{2}}{\log R_{1}}
$$

and

$$
u(z)=2 \log |f(z)|-2 \alpha \log |z| \quad\left(z \in A_{1}\right)
$$

Let $\partial$ be one of the Cauchy-Riemann operators. Since $\partial \bar{f}=0$ and $\partial f=f^{\prime}$, the chain rule gives

$$
\partial(2 \log |f|)=\partial(\log (\overline{f f}))=f^{\prime} / f
$$

so that

$$
(\partial u)(z)=\frac{f^{\prime}(z)}{f(z)}-\frac{\alpha}{z} \quad\left(z \in A_{1}\right)
$$

Thus $u$ is a harmonic function in $A_{1}$ which, by the first paragraph of this proof, extends to a continuous function on $\bar{A}_{1}$ which is 0 on the boundary of $A_{1}$. Since nonconstant harmonic functions have no local maxima or minima, we conclude that $u=0$. Thus

$$
\frac{f^{\prime}(z)}{f(z)}=\frac{\alpha}{z} \quad\left(z \in A_{1}\right)
$$

Put $\gamma(t)=\sqrt{R_{1}} e^{i t}(-\pi \leq t \leq \pi)$; put $\Gamma=f \circ \gamma$. As in the proof of Theorem 10.43, (7) gives

$$
\alpha=\frac{1}{2 \pi i} \int_{\gamma} \frac{f^{\prime}(z)}{f(z)} d z=\operatorname{Ind}_{\Gamma}(0)
$$

Thus $\alpha$ is an integer. By (3), $\alpha>0$. By (7), the derivative of $z^{-\alpha} f(z)$ is 0 in $A_{1}$. Thus $f(z)=c z^{\alpha}$. Since $f$ is one-to-one in $A_{1}, \alpha=1$. Hence $R_{2}=R_{1}$.

## Exercises

1 Find necessary and sufficient conditions which the complex numbers $a, b, c$, and $d$ have to satisfy so that the linear fractional transformation $z \rightarrow(a z+b) /(c z+d)$ maps the upper half plane onto itself. 2 In Theorem 11.14 the hypotheses were, in simplified form, that $\Omega \subset \Pi^{+}, L$ is on the real axis, and $\operatorname{Im} f(z) \rightarrow 0$ as $z \rightarrow L$. Use this theorem to establish analogous reflection theorems under the following hypotheses:

(a) $\Omega \subset \Pi^{+}, L$ on real axis, $|f(z)| \rightarrow 1$ as $z \rightarrow L$.

(b) $\Omega \subset U, L \subset T,|f(z)| \rightarrow 1$ as $z \rightarrow L$.

(c) $\Omega \subset U, L \subset T, \operatorname{Im} f(z) \rightarrow 0$ as $z \rightarrow L$.

In case $(b)$, if $f$ has a zero at $\alpha \in \Omega$, show that its extension has a pole at $1 / \bar{\alpha}$. What are the analogues of this in cases $(a)$ and $(c)$ ?

3 Suppose $R$ is a rational function such that $|R(z)|=1$ if $|z|=1$. Prove that

$$
R(z)=c z^{m} \prod_{n=1}^{k} \frac{z-\alpha_{n}}{1-\bar{\alpha}_{n} z}
$$

where $c$ is a constant, $m$ is an integer, and $\alpha_{1}, \ldots, \alpha_{k}$ are complex numbers such that $\alpha_{n} \neq 0$ and $\left|\alpha_{n}\right| \neq 1$. Note that each of the above factors has absolute value 1 if $|z|=1$.

4 Obtain an analogous description of those rational functions which are positive on $T$.

Hint: Such a function must have the same number of zeros as poles in $U$. Consider products of factors of the form

$$
\frac{(z-\alpha)(1-\bar{\alpha} z)}{(z-\beta)(1-\bar{\beta} z)}
$$

where $|\alpha|<1$ and $|\beta|<1$.

5 Suppose $f$ is a trigonometric polynomial,

$$
f(\theta)=\sum_{k=-n}^{n} a_{k} e^{i k \theta}
$$

and $f(\theta)>0$ for all real $\theta$. Prove that there is a polynomial $P(z)=c_{0}+c_{1} z+\cdots+c_{n} z^{n}$ such that

$$
f(\theta)=\left|P\left(e^{i \theta}\right)\right|^{2} \quad(\theta \text { real })
$$

Hint: Apply Exercise 4 to the rational function $\Sigma a_{k} z^{k}$. Is the result still valid if we assume $f(\theta) \geq 0$ instead of $f(\theta)>0$ ?

6 Find the fixed points of the mappings $\varphi_{\alpha}$ (Definition 12.3). Is there a straight line which $\varphi_{\alpha}$ maps to itself?

7 Find all complex numbers $\alpha$ for which $f_{\alpha}$ is one-to-one in $U$, where

$$
f_{\alpha}(z)=\frac{z}{1+\alpha z^{2}}
$$

Describe $f_{\alpha}(U)$ for all these cases.

8 Suppose $f(z)=z+(1 / z)$. Describe the families of ellipses and hyperbolas onto which $f$ maps circles with center at 0 and rays through 0 .

9 (a) Suppose $\Omega=\{z:-1<\operatorname{Re} z<1\}$. Find an explicit formula for the one-to-one conformal mapping $f$ of $\Omega$ onto $U$ for which $f(0)=0$ and $f^{\prime}(0)>0$. Compute $f^{\prime}(0)$.

(b) Note that the inverse of the function constructed in $(a)$ has its real part bounded in $U$, whereas its imaginary part is unbounded. Show that this implies the existence of a continuous real function $u$ on $\bar{U}$ which is harmonic in $U$ and whose harmonic conjugate $v$ is unbounded in $U$. [ $v$ is the function which makes $u+i v$ holomorphic in $U$; we can determine $v$ uniquely by the requirement $v(0)=0$.]

(c) Suppose $g \in H(U),|\operatorname{Re} g|<1$ in $U$, and $g(0)=0$. Prove that

$$
\left|g\left(r e^{i \theta}\right)\right| \leq \frac{2}{\pi} \log \frac{1+r}{1-r}
$$

Hint: See Exercise 10.

(d) Let $\Omega$ be the strip that occurs in Theorem 12.9. Fix a point $\alpha+i \beta$ in $\Omega$. Let $h$ be a conformal one-to-one mapping of $\Omega$ onto $\Omega$ that carries $\alpha+i \beta$ to 0 . Prove that

$$
\left|h^{\prime}(\alpha+i \beta)\right|=1 / \cos \beta
$$

10 Suppose $f$ and $g$ are holomorphic mappings of $U$ into $\Omega, f$ is one-to-one, $f(U)=\Omega$, and $f(0)=g(0)$. Prove that

$$
g(D(0 ; r)) \subset f(D(0 ; r)) \quad(0<r<1)
$$

11 Let $\Omega$ be the upper half of the unit disc $U$. Find the conformal mapping $f$ of $\Omega$ onto $U$ that carries $\{-1,0,1\}$ to $\{-1,-i, 1\}$. Find $z \in \Omega$ such that $f(z)=0$. Find $f(i / 2)$. Hint: $f=\varphi \circ s \circ \psi$, where $\varphi$ and $\psi$ are linear fractional transformations and $s(\lambda)=\lambda^{2}$.

12 Suppose $\Omega$ is a convex region, $f \in H(\Omega)$, and $\operatorname{Re} f^{\prime}(z)>0$ for all $z \in \Omega$. Prove that $f$ is one-to-one in $\Omega$. Is the result changed if the hypothesis is weakened to $\operatorname{Re} f^{\prime}(z) \geq 0$ ? (Exclude the trivial case $f=$ constant.) Show by an example that "convex" cannot be replaced by "simply connected."

13 Suppose $\Omega$ is a region, $f_{n} \in H(\Omega)$ for $n=1,2,3, \ldots$, each $f_{n}$ is one-to-one in $\Omega$, and $f_{n} \rightarrow f$ uniformly on compact subsets of $\Omega$. Prove that $f$ is either constant or one-to-one in $\Omega$. Show that both cases can occur.

14 Suppose $\Omega=\{x+i y:-1<y<1\}, f \in H(\Omega),|f|<1$, and $f(x) \rightarrow 0$ as $x \rightarrow \infty$. Prove that

$$
\lim _{x \rightarrow \infty} f(x+i y)=0 \quad(-1<y<1)
$$

and that the passage to the limit is uniform if $y$ is confined to an interval $[-\alpha, \alpha]$, where $\alpha<1$. Hint: Consider the sequence $\left\{f_{n}\right\}$, where $f_{n}(z)=z+n$, in the square $|x|<1,|y|<1$.

What does this theorem tell about the behavior of a function $g \in H^{\infty}$ near a boundary point of $U$ at which the radial limit of $g$ exists?

15 Let $\mathscr{F}$ be the class of all $f \in H(U)$ such that $\operatorname{Re} f>0$ and $f(0)=1$. Show that $\mathscr{F}$ is a normal family. Can the condition " $f(0)=1$ " be omitted? Can it be replaced by " $|f(0)| \leq 1$ "?

16 Let $\mathscr{F}$ be the class of all $f \in H(U)$ for which

$$
\iint_{U}|f(z)|^{2} d x d y \leq 1
$$

Is this a normal family?

17 Suppose $\Omega$ is a region, $f_{n} \in H(\Omega)$ for $n=1,2,3, \ldots, f_{n} \rightarrow f$ uniformly on compact subsets of $\Omega$, and $f$ is one-to-one in $\Omega$. Does it follow that to each compact $K \subset \Omega$ there corresponds an integer $N(K)$ such that $f_{n}$ is one-to-one on $K$ for all $n>N(K)$ ? Give proof or counterexample.

18 Suppose $\Omega$ is a simply coniected region, $z_{0} \in \Omega$, and $f$ and $g$ are one-to-one conformal mappings of $\Omega$ onto $U$ which carry $z_{0}$ to 0 . What relation exists between $f$ and $g$ ? Answer the same question if $f\left(z_{0}\right)=g\left(z_{0}\right)=a$, for some $a \in U$.

19 Find a homeomorphism of $U$ onto $U$ which cannot be extended to a continuous function on $\bar{U}$.

20 If $f \in \mathscr{S}$ (Definition 14.10) and $n$ is a positive integer, prove that there exists a $g \in \mathscr{S}$ such that $g^{n}(z)=f\left(z^{n}\right)$ for all $z \in U$.

21 Find all $f \in \mathscr{S}$ such that $(a) f(U) \supset U,(b) f(U) \supset \bar{U},(c)\left|a_{2}\right|=2$.

22 Suppose $f$ is a one-to-one conformal mapping of $U$ onto a square with center at 0 , and $f(0)=0$. Prove that $f(i z)=i f(z)$. If $f(z)=\Sigma c_{n} z^{n}$, prove that $c_{n}=0$ unless $n-1$ is a multiple of 4 . Generalize this: Replace the square by other simply connected regions with rotational symmetry.

23 Let $\Omega$ be a bounded region whose boundary consists of two nonintersecting circles. Prove that there is a one-to-one conformal mapping of $\Omega$ onto an annulus. (This is true for every region $\boldsymbol{\Omega}$ such that $S^{2}-\Omega$ has exactly two components, each of which contains more than one point, but this general situation is harder to handle.)

24 Complete the details in the following proof of Theorem 14.22. Suppose $1<R_{2}<R_{1}$ and $f$ is a one-to-one conformal mapping of $A\left(1, R_{1}\right)$ onto $A\left(1, R_{2}\right)$. Define $f_{1}=f$ and $f_{n}=f \circ f_{n-1}$. Then a subsequence of $\left\{f_{n}\right\}$ converges uniformly on compact subsets of $A\left(1, R_{1}\right)$ to a function $g$. Show that the range of $g$ cannot contain any nonempty open set (by the three-circle theorem, for instance). On the other hand, show that $g$ cannot be constant on the circle $\left\{z:|z|^{2}=R_{1}\right\}$. Hence $f$ cannot exist.

25 Here is yet another proof of Theorem 14.22. If $f$ is as in 14.22, repeated use of the reflection principle extends $f$ to an entire function such that $|f(z)|=1$ whenever $|z|=1$. This implies $f(z)=\alpha z^{n}$, where $|\alpha|=1$ and $n$ is an integer. Complete the details.

26 Iteration of Step 2 in the proof of Theorem 14.8 leads to a proof (due to Koebe) of the Riemann mapping theorem which is constructive in the sense that it makes no appeal to the theory of normal families and so does not depend on the existence of some unspecified subsequence. For the final step of the proof it is convenient to assume that $\Omega$ has property $(h)$ of Theorem 13.11. Then any region conformally equivalent to $\Omega$ will satisfy $(h)$. Recall also that $(h)$ implies $(j)$, trivially.

By Step 1 in Theorem 14.8 we may assume, without loss of generality, that $0 \in \Omega, \Omega \subset U$, and $\Omega \neq U$. Put $\Omega=\Omega_{0}$. The proof consists in the construction of regions $\Omega_{1}, \Omega_{2}, \Omega_{3}, \ldots$ and of functions $f_{1}, f_{2}, f_{3}, \ldots$, so that $f_{n}\left(\Omega_{n-1}\right)=\Omega_{n}$ and so that the functions $f_{n} \circ f_{n-1} \circ \cdots \circ f_{2} \circ f_{1}$ converge to a conformal mapping of $\Omega$ onto $U$.

Complete the details in the following outline.

(a) Suppose $\Omega_{n-1}$ is constructed, let $r_{n}$ be the largest number such that $D\left(0 ; r_{n}\right) \subset \Omega_{n-1}$, let $\alpha_{n}$ be a boundary point of $\Omega_{n-1}$ with $\left|\alpha_{n}\right|=r_{n}$, choose $\beta_{n}$ so that $\beta_{n}^{2}=-\alpha_{n}$, and put

$$
F_{n}=\varphi_{-\alpha_{n}} \circ s \circ \varphi_{-\beta_{n}} .
$$

(The notation is as in the proof of Theorem 14.8.) Show that $F_{n}$ has a holomorphic inverse $G_{n}$ in $\Omega_{n-1}$, and put $f_{n}=\lambda_{n} G_{n}$, where $\lambda_{n}=|c| / c$ and $c=G_{n}^{\prime}(0)$. (This $f_{n}$ is the Koebe mapping associated with $\Omega_{n-1}$. Note that $f_{n}$ is an elementary function. It involves only two linear fractional transformations and a square root.)

(b) Compute that $f_{n}^{\prime}(0)=\left(1+r_{n}\right) / 2 \sqrt{r_{n}}>1$.

(c) Put $\psi_{0}(z)=z$ and $\psi_{n}(z)=f_{n}\left(\psi_{n-1}(z)\right)$. Show that $\psi_{n}$ is a one-to-one mapping of $\Omega$ onto a region $\Omega_{n} \subset U$, that $\left\{\psi_{n}^{\prime}(0)\right\}$ is bounded, that

$$
\psi_{n}^{\prime}(0)=\prod_{k=1}^{n} \frac{1+r_{k}}{2 \sqrt{r_{k}}}
$$

and that therefore $r_{n} \rightarrow 1$ as $n \rightarrow \infty$.

(d) Write $\psi_{n}(z)=z h_{n}(z)$, for $z \in \Omega$, show that $\left|h_{n}\right| \leq\left|h_{n+1}\right|$, apply Harnack's theorem and Exercise 8 of Chap. 11 to $\left\{\log \left|h_{n}\right|\right\}$ to prove that $\left\{\psi_{n}\right\}$ converges uniformly on compact subsets of $\Omega$, and show that $\lim \psi_{n}$ is a one-to-one mapping of $\Omega$ onto $U$.

27 Prove that $\sum_{n=1}^{\infty}\left(1-r_{n}\right)^{2}<\infty$, where $\left\{r_{n}\right\}$ is the sequence which occurs in Exercise 26. Hint:

$$
\frac{1+r}{2 \sqrt{r}}=1+\frac{(1-\sqrt{r})^{2}}{2 \sqrt{r}}
$$

28 Suppose that in Exercise 26 we choose $\alpha_{n} \in U-\Omega_{n-1}$ without insisting that $\left|\alpha_{n}\right|=r_{n}$. For example, insist only that

$$
\left|\alpha_{n}\right| \leq \frac{1+r_{n}}{2}
$$

Will the resulting sequence $\left\{\psi_{n}\right\}$ still converge to the desired mapping function?

29 Suppose $\Omega$ is a bounded region, $a \in \Omega, f \in H(\Omega), f(\Omega) \subset \Omega$, and $f(a)=a$.

(a) Put $f_{1}=f$ and $f_{n}=f \circ f_{n-1}$, compute $f_{n}^{\prime}(a)$, and conclude that $\left|f^{\prime}(a)\right| \leq 1$.

(b) If $f^{\prime}(a)=1$, prove that $f(z)=z$ for all $z \in \Omega$. Hint: If

$$
f(z)=z+c_{m}(z-a)^{m}+\cdots
$$

compute the coefficient of $(z-a)^{m}$ in the expansion of $f_{n}(z)$.

(c) If $\left|f^{\prime}(a)\right|=1$, prove that $f$ is one-to-one and that $f(\Omega)=\Omega$.

Hint: If $\gamma=f^{\prime}(a)$, there are integers $n_{k} \rightarrow \infty$ such that $\gamma^{n_{k}} \rightarrow 1$ and $f_{n_{k}} \rightarrow g$. Then $g^{\prime}(a)=1$, $g(\Omega) \subset \Omega$ (by Exercise 20, Chap. 10), hence $g(z)=z$, by part (b). Use $g$ to draw the desired conclusions about $f$.

30 Let $\Lambda$ be the set of all linear fractional transformations.

If $\{\alpha, \beta, \gamma, \delta\}$ is an ordered quadruple of distinct complex numbers, its cross ratio is defined to be

$$
[\alpha, \beta, \gamma, \delta]=\frac{(\alpha-\beta)(\gamma-\delta)}{(\alpha-\delta)(\gamma-\beta)}
$$

If one of these numbers is $\infty$, the definition is modified in the obvious way, by continuity. The same applies if $\alpha$ coincides with $\beta$ or $\gamma$ or $\delta$.

(a) If $\varphi(z)=[z, \alpha, \beta, \gamma]$, show that $\varphi \in \Lambda$ and $\varphi$ maps $\{\alpha, \beta, \gamma\}$ to $\{0,1, \infty\}$.

(b) Show that the equation $[w, a, b, c]=[z, \alpha, \beta, \gamma]$ can be solved in the form $w=\varphi(z)$; then $\varphi \in \Lambda$ maps $\{\alpha, \beta, \gamma\}$ to $\{a, b, c\}$.

(c) If $\varphi \in \Lambda$, show that

$$
[\varphi(\alpha), \varphi(\beta), \varphi(\gamma), \varphi(\delta)]=[\alpha, \beta, \gamma, \delta]
$$

(d) Show that $[\alpha, \beta, \gamma, \delta]$ is real if and only if the four points lie on the same circle or straight line.

(e) Two points $z$ and $z^{*}$ are said to be symmetric with respect to the circle (or straight line) $C$ through $\alpha, \beta$, and $\gamma$ if $\left[z^{*}, \alpha, \beta, \gamma\right]$ is the complex conjugate of $[z, \alpha, \beta, \gamma]$. If $C$ is the unit circle, find a simple geometric relation between $z$ and $z^{*}$. Do the same if $C$ is a straight line.

$(f)$ Suppose $z$ and $z^{*}$ are symmetric with respect to $C$. Show that $\varphi(z)$ and $\varphi\left(z^{*}\right)$ are symmetric with respect to $\varphi(C)$, for every $\varphi \in \Lambda$.

31 (a) Show that $\Lambda$ (see Exercise 30) is a group, with composition as group operation. That is, if $\varphi \in \Lambda$ and $\psi \in \Lambda$, show that $\varphi \circ \psi \in \Lambda$ and that the inverse $\varphi^{-1}$ of $\varphi$ is in $\Lambda$. Show that $\Lambda$ is not commutative.

(b) Show that each member of $\Lambda$ (other than the identity mapping) has either one or two fixed points on $S^{2}$. [A fixed point of $\varphi$ is a point $\alpha$ such that $\varphi(\alpha)=\alpha$.]

(c) Call two mappings $\varphi$ and $\varphi_{1} \in \Lambda$ conjugate if there exists a $\psi \in \Lambda$ such that $\varphi_{1}=\psi^{-1} \circ \varphi \circ \psi$. Prove that every $\varphi \in \Lambda$ with a unique fixed point is conjugate to the mapping $z \rightarrow z+1$. Prove that every $\varphi \in \Lambda$ with two distinct fixed points is conjugate to the mapping $z \rightarrow \alpha z$, where $\alpha$ is a complex number; to what extent is $\alpha$ determined by $\varphi$ ?
(d) Let $\alpha$ be a complex number. Show that to every $\varphi \in \Lambda$ which has $\alpha$ for its unique fixed point there corresponds a $\beta$ such that

$$
\frac{1}{\varphi(z)-\alpha}=\frac{1}{z-\alpha}+\beta
$$

Let $G_{\alpha}$ be the set of all these $\varphi$, plus the identity transformation. Prove that $G_{\alpha}$ is a subgroup of $\Lambda$ and that $G_{\alpha}$ is isomorphic to the additive group of all complex numbers.

(e) Let $\alpha$ and $\beta$ be distinct complex numbers, and let $G_{\alpha, \beta}$ be the set of all $\varphi \in \Lambda$ which have $\alpha$ and $\beta$ as fixed points. Show that every $\varphi \in G_{\alpha, \beta}$ is given by

$$
\frac{\varphi(z)-\alpha}{\varphi(z)-\beta}=\gamma \cdot \frac{z-\alpha}{z-\beta}
$$

where $\gamma$ is a complex number. Show that $G_{\alpha, \beta}$ is a subgroup of $\Lambda$ which is isomorphic to the multiplicative group of all nonzero complex numbers.

$(f)$ If $\varphi$ is as in $(d)$ or $(e)$, for which circles $C$ is it true that $\varphi(C)=C$ ? The answer should be in terms of the parameters $\alpha, \beta$, and $\gamma$.

32 For $z \in \bar{U}, z^{2} \neq 1$, define

$$
f(z)=\exp \left\{i \log \frac{1+z}{1-z}\right\}
$$

choosing the branch of $\log$ that has $\log 1=0$. Describe $f(E)$ if $E$ is

(a) $U$,

(b) the upper half of $T$,

(c) the lower half of $T$,

(d) any circular arc (in $U$ ) from -1 to 1 ,

(e) the radius $[0,1)$,

(f) any disc $\{z:|z-r|<1-r\}, 0<r<1$.

$(g)$ any curve in $U$ tending to 1 .

33 If $\varphi_{\alpha}$ is as in Definition 12.3, show that

(a) $\frac{1}{\pi} \int_{U}\left|\varphi_{\alpha}^{\prime}\right|^{2} d m=1$,

(b) $\frac{1}{\pi} \int_{U}\left|\varphi_{\alpha}^{\prime}\right| d m=\frac{1-|\alpha|^{2}}{|\alpha|^{2}} \log \frac{1}{1-|\alpha|^{2}}$.

Here $m$ denotes Lebesgue measure in $R^{2}$.

## CHAPTER <br> FIFTEEN

## ZEROS OF HOLOMORPHIC FUNCTIONS

## Infinite Products

15.1 So far we have met only one result concerning the zero set $Z(f)$ of a nonconstant holomorphic function $f$ in a region $\Omega$, namely, $Z(f)$ has no limit point in $\Omega$. We shall see presently that this is all that can be said about $Z(f)$, if no other conditions are imposed on $f$, because of the theorem of Weierstrass (Theorem 15.11) which asserts that every $A \subset \Omega$ without limit point in $\Omega$ is $Z(f)$ for some $f \in H(\Omega)$. If $A=\left\{\alpha_{n}\right\}$, a natural way to construct such an $f$ is to choose functions $f_{n} \in H(\Omega)$ so that $f_{n}$ has only one zero, at $\alpha_{n}$, and to consider the limit of the products

$$
p_{n}=f_{1} f_{2} \cdots f_{n} \text {, }
$$

as $n \rightarrow \infty$. One has to arrange it so that the sequence $\left\{p_{n}\right\}$ converges to some $f \in H(\Omega)$ and so that the limit function $f$ is not 0 except at the prescribed points $\alpha_{n}$. It is therefore advisable to begin by studying some general properties of infinite products.

15.2 Definition Suppose $\left\{u_{n}\right\}$ is a sequence of complex numbers,

$$
p_{n}=\left(1+u_{1}\right)\left(1+u_{2}\right) \cdots\left(1+u_{n}\right)
$$

and $p=\lim _{n \rightarrow \infty} p_{n}$ exists. Then we write

$$
p=\prod_{n=1}^{\infty}\left(1+u_{n}\right)
$$

The $p_{n}$ are the partial products of the infinite product (2). We shall say that the infinite product (2) converges if the sequence $\left\{p_{n}\right\}$ converges.

In the study of infinite series $\Sigma a_{n}$ it is of significance whether the $a_{n}$ approach 0 rapidly. Analogously, in the study of infinite products it is of interest whether the factors are or are not close to 1 . This accounts for the above notation: $1+u_{n}$ is close to 1 if $u_{n}$ is close to 0 .

15.3 Lemma If $u_{1}, \ldots, u_{N}$ are complex numbers, and if

$$
p_{N}=\prod_{n=1}^{N}\left(1+u_{n}\right), \quad p_{N}^{*}=\prod_{n=1}^{N}\left(1+\left|u_{n}\right|\right)
$$

then

$$
p_{N}^{*} \leq \exp \left(\left|u_{1}\right|+\cdots+\left|u_{N}\right|\right)
$$

and

$$
\left|p_{N}-1\right| \leq p_{N}^{*}-1
$$

ProOF For $x \geq 0$, the inequality $1+x \leq e^{x}$ is an immediate consequence of the expansion of $e^{x}$ in powers of $x$. Replace $x$ by $\left|u_{1}\right|, \ldots,\left|u_{N}\right|$ and multiply the resulting inequalities. This gives (2). For $N=1,(3)$ is trivial. The general case follows by induction: For $k=1, \ldots, N-1$,

$$
p_{k+1}-1=p_{k}\left(1+u_{k+1}\right)-1=\left(p_{k}-1\right)\left(1+u_{k+1}\right)+u_{k+1},
$$

so that if (3) holds with $k$ in place of $N$, then also

$$
\left|p_{k+1}-1\right| \leq\left(p_{k}^{*}-1\right)\left(1+\left|u_{k+1}\right|\right)+\left|u_{k+1}\right|=p_{k+1}^{*}-1
$$

15.4 Theorem Suppose $\left\{u_{n}\right\}$ is a sequence of bounded complex functions on a set $S$, such that $\Sigma\left|u_{n}(s)\right|$ converges uniformly on $S$. Then the product

$$
f(s)=\prod_{n=1}^{\infty}\left(1+u_{n}(s)\right)
$$

converges uniformly on $S$, and $f\left(s_{0}\right)=0$ at some $s_{0} \in S$ if and only if $u_{n}\left(s_{0}\right)=$ -1 for some $n$.

Furthermore, if $\left\{n_{1}, n_{2}, n_{3}, \ldots\right\}$ is any permutation of $\{1,2,3, \ldots\}$, then we also have

$$
f(s)=\prod_{k=1}^{\infty}\left(1+u_{n_{k}}(s)\right) \quad(s \in S)
$$

Proof The hypothesis implies that $\Sigma\left|u_{n}(s)\right|$ is bounded on $S$, and if $p_{N}$ denotes the $N$ th partial product of (1), we conclude from Lemma 15.3 that there is a constant $C<\infty$ such that $\left|p_{N}(s)\right| \leq C$ for all $N$ and all $s$.

Choose $\epsilon, 0<\epsilon<\frac{1}{2}$. There exists an $N_{0}$ such that

$$
\sum_{n=N_{0}}^{\infty}\left|u_{n}(s)\right|<\epsilon \quad(s \in S)
$$

Let $\left\{n_{1}, n_{2}, n_{3}, \ldots\right\}$ be a permutation of $\{1,2,3, \ldots\}$. If $N \geq N_{0}$, if $M$ is so large that

$$
\{1,2, \ldots, N\} \subset\left\{n_{1}, n_{2}, \ldots, n_{M}\right\}
$$

and if $q_{M}(s)$ denotes the $M$ th partial product of (2), then

$$
q_{M}-p_{N}=p_{N}\left\{\prod\left(1+u_{n_{k}}\right)-1\right\} .
$$

The $n_{k}$ which occur in (5) are all distinct and are larger than $N_{0}$. Therefore (3) and Lemma 15.3 show that

$$
\left|q_{M}-p_{N}\right| \leq\left|p_{N}\right|\left(e^{\epsilon}-1\right) \leq 2\left|p_{N}\right| \epsilon \leq 2 C \epsilon .
$$

If $n_{k}=k(k=1,2,3, \ldots)$, then $q_{M}=p_{M}$, and (6) shows that $\left\{p_{N}\right\}$ converges uniformly to a limit function $f$. Also, (6) shows that

$$
\left|p_{M}-p_{N_{0}}\right| \leq 2\left|p_{N_{0}}\right| \epsilon \quad\left(M>N_{0}\right)
$$

so that $\left|p_{M}\right| \geq(1-2 \epsilon)\left|p_{N_{0}}\right|$. Hence

$$
|f(s)| \geq(1-2 \epsilon)\left|p_{N_{0}}(s)\right| \quad(s \in S)
$$

which shows that $f(s)=0$ if and only if $p_{N_{0}}(s)=0$.

Finally, (6) also shows that $\left\{q_{M}\right\}$ converges to the same limit as $\left\{p_{N}\right\}$. I///

15.5 Theorem Suppose $0 \leq u_{n}<1$. Then

$$
\prod_{n=1}^{\infty}\left(1-u_{n}\right)>0 \quad \text { if and only if } \quad \sum_{n=1}^{\infty} u_{n}<\infty
$$

ProOF If $p_{N}=\left(1-u_{1}\right) \cdots\left(1-u_{N}\right)$, then $p_{1} \geq p_{2} \geq \cdots, p_{N}>0$, hence $p=$ $\lim p_{N}$ exists. If $\Sigma u_{n}<\infty$, Theorem 15.4 implies $p>0$. On the other hand,

$$
p \leq p_{N}=\prod_{1}^{N}\left(1-u_{n}\right) \leq \exp \left\{-u_{1}-u_{2}-\cdots-u_{N}\right\}
$$

and the last expression tends to 0 as $N \rightarrow \infty$, if $\Sigma u_{n}=\infty$.

We shall frequently use the following consequence of Theorem 15.4:

15.6 Theorem Suppose $f_{n} \in H(\Omega)$ for $n=1,2,3, \ldots$, no $f_{n}$ is identically 0 in any component of $\Omega$, and

$$
\sum_{n=1}^{\infty}\left|1-f_{n}(z)\right|
$$

converges uniformly on compact subsets of $\Omega$. Then the product

$$
f(z)=\prod_{n=1}^{\infty} f_{n}(z)
$$

converges uniformly on compact subsets of $\Omega$. Hence $f \in H(\Omega)$.

Furthermore, we have

$$
m(f ; z)=\sum_{n=1}^{\infty} m\left(f_{n} ; z\right) \quad(z \in \Omega)
$$

where $m(f ; z)$ is defined to be the multiplicity of the zero of $f$ at $z$. [If $f(z) \neq 0$, then $m(f ; z)=0$.]

Proof The first part follows immediately from Theorem 15.4. For the second part, observe that each $z \in \Omega$ has a neighborhood $V$ in which at most finitely many of the $f_{n}$ have a zero, by (1). Take these factors first. The product of the remaining ones has no zero in $V$, by Theorem 15.4, and this gives (3). Incidentally, we see also that at most finitely many terms in the series (3) can be positive for any given $z \in \Omega$.

## The Weierstrass Factorization Theorem

15.7 Definition Put $E_{0}(z)=1-z$, and for $p=1,2,3, \ldots$,

$$
E_{p}(z)=(1-z) \exp \left\{z+\frac{z^{2}}{2}+\cdots+\frac{z^{p}}{p}\right\}
$$

These functions, introduced by Weierstrass, are sometimes called elementary factors. Their only zero is at $z=1$. Their utility depends on the fact that they are close to 1 if $|z|<1$ and $p$ is large, although $E_{p}(1)=0$.

15.8 Lemma For $|z| \leq 1$ and $p=0,1,2, \ldots$,

$$
\left|1-E_{p}(z)\right| \leq|z|^{p+1}
$$

Proof For $p=0$, this is obvious. For $p \geq 1$, direct computation shows that

$$
-E_{p}^{\prime}(z)=z^{p} \exp \left\{z+\frac{z^{2}}{2}+\cdots+\frac{z^{p}}{p}\right\}
$$

So $-E_{p}^{\prime}$ has a zero of order $p$ at $z=0$, and the expansion of $-E_{p}^{\prime}$ in powers of $z$ has nonnegative real coefficients. Since

$$
1-E_{p}(z)=-\int_{[0, z]} E_{p}^{\prime}(w) d w
$$

$1-E_{p}$ has a zero of order $p+1$ at. $z=0$, and if

$$
\varphi(z)=\frac{1-E_{p}(z)}{z^{p+1}},
$$

then $\varphi(z)=\Sigma a_{n} z^{n}$, with all $a_{n} \geq 0$. Hence $|\varphi(z)| \leq \varphi(1)=1$ if $|z| \leq 1$, and this gives the assertion of the lemma.

15.9 Theorem Let $\left\{z_{n}\right\}$ be a sequence of complex numbers such that $z_{n} \neq 0$ and $\left|z_{n}\right| \rightarrow \infty$ as $n \rightarrow \infty$. If $\left\{p_{n}\right\}$ is a sequence of nonnegative integers such that

$$
\sum_{n=1}^{\infty}\left(\frac{r}{r_{n}}\right)^{1+p_{n}}<\infty
$$

for every positive $r$ (where $r_{n}=\left|z_{n}\right|$ ), then the infinite product

$$
P(z)=\prod_{n=1}^{\infty} E_{p_{n}}\left(\frac{z}{z_{n}}\right)
$$

defines an entire function $P$ which has a zero at each point $z_{n}$ and which has no other zeros in the plane.

More precisely, if $\alpha$ occurs $m$ times in the sequence $\left\{z_{n}\right\}$, then $P$ has a zero of order $m$ at $\alpha$.

Condition (1) is always satisfied if $p_{n}=n-1$, for instance.

PROOF For every $r, r_{n}>2 r$ for all but finitely many $n$, hence $r / r_{n}<\frac{1}{2}$ for these $n$, so (1) holds with $1+p_{n}=n$.

Now fix $r$. If $|z| \leq r$, Lemma 15.8 shows that

$$
\left|1-E_{p_{n}}\left(\frac{z}{z_{n}}\right)\right| \leq\left|\frac{z}{z_{n}}\right|^{1+p_{n}} \leq\left(\frac{r}{r_{n}}\right)^{1+p_{n}}
$$

if $r_{n} \geq r$, which holds for all but finitely many $n$. It now follows from (1) that the series

$$
\sum_{n=1}^{\infty}\left|1-E_{p_{n}}\left(\frac{z}{z_{n}}\right)\right|
$$

converges uniformly on compact sets in the plane, and Theorem 15.6 gives the desired conclusion.

Note: For certain sequences $\left\{r_{n}\right\}$, (1) holds for a constant sequence $\left\{p_{n}\right\}$. It is of interest to take this constant as small as possible; the resulting function (2) is then called the canonical product corresponding to $\left\{z_{n}\right\}$. For instance, if $\Sigma 1 / r_{n}<\infty$, we can take $p_{n}=0$, and the canonical product is simply

$$
\prod_{n=1}^{\infty}\left(1-\frac{z}{z_{n}}\right)
$$

If $\Sigma 1 / r_{n}=\infty$ but $\Sigma 1 / r_{n}^{2}<\infty$, the canonical product is

$$
\prod_{n=1}^{\infty}\left(1-\frac{z}{z_{n}}\right) e^{z / z_{n}}
$$

Canonical products are of great interest in the study of entire functions of finite order. (See Exercise 2 for the definition.)

We now state the Weierstrass factorization theorem.

15.10 Theorem Let $f$ be an entire function, suppose $f(0) \neq 0$, and let $z_{1}, z_{2}, z_{3}$, $\ldots$ be the zeros of $f$, listed according to their multiplicities. Then there exist an entire function $g$ and a sequence $\left\{p_{n}\right\}$ of nonnegative integers, such that

$$
f(z)=e^{g(z)} \prod_{n=1}^{\infty} E_{p_{n}}\left(\frac{z}{z_{n}}\right)
$$

Note: (a) If $f$ has a zero of order $k$ at $z=0$, the preceding applies to $f(z) / z^{k}$. (b) The factorization (1) is not unique; a unique factorization can be associated with those $f$ whose zeros satisfy the condition required for the convergence of a canonical product.

Proof Let $P$ be the product in Theorem 15.9, formed with the zeros of $f$. Then $f / P$ has only removable singularities in the plane, hence is (or can be extended to) an entire function. Also, $f / P$ has no zero, and since the plane is simply connected, $f / P=e^{g}$ for some entire function $g$.

The proof of Theorem 15.9 is easily adapted to any open set:

15.11 Theorem Let $\Omega$ be an open set in $S^{2}, \Omega \neq S^{2}$. Suppose $A \subset \Omega$ and $A$ has no limit point in $\Omega$. With each $\alpha \in A$ associate a positive integer $m(\alpha)$. Then there exists an $f \in H(\Omega)$ all of whose zeros are in $A$, and such that $f$ has a zero of $\operatorname{order} m(\alpha)$ at each $\alpha \in A$.

Proof It simplifies the argument, and causes no loss of generality, to assume that $\infty \in \Omega$ but $\infty \notin A$. (If this is not so, a linear fractional transformation will make it so.) Then $S^{2}-\Omega$ is a nonempty compact subset of the plane, and $\infty$ is not a limit point of $A$.

If $A$ is finite, we can take a rational function for $f$.

If $A$ is infinite, then $A$ is countable (otherwise there would be a limit point in $\Omega$ ). Let $\left\{\alpha_{n}\right\}$ be a sequence whose terms are in $A$ and in which each $\alpha \in A$ is listed precisely $m(\alpha)$ times. Associate with each $\alpha_{n}$ a point $\beta_{n} \in$ $S^{2}-\Omega$ such that $\left|\beta_{n}-\alpha_{n}\right| \leq\left|\beta-a_{n}\right|$ for all $\beta \in S^{2}-\Omega$; this is possible since $S^{2}-\Omega$ is compact. Then

$$
\left|\beta_{n}-\alpha_{n}\right| \rightarrow 0
$$

as $n \rightarrow \infty$; otherwise $A$ would have a limit point in $\Omega$. We claim that

$$
f(z)=\prod_{n=1}^{\infty} E_{n}\left(\frac{\alpha_{n}-\beta_{n}}{z-\beta_{n}}\right)
$$

has the desired properties.

Put $r_{n}=2\left|\alpha_{n}-\beta_{n}\right|$. Let $K$ be a compact subset of $\Omega$. Since $r_{n} \rightarrow 0$, there exists an $N$ such that $\left|z-\beta_{n}\right|>r_{n}$ for all $z \in K$ and all $n \geq N$. Hence

$$
\left|\frac{\alpha_{n}-\beta_{n}}{z-\beta_{n}}\right| \leq \frac{1}{2}
$$

which implies, by Lemma 15.8, that

$$
\left|1-E_{n}\left(\frac{\alpha_{n}-\beta_{n}}{z-\beta_{n}}\right)\right| \leq\left(\frac{1}{2}\right)^{n+1} \quad(z \in K, n \geq N)
$$

and this again completes the proof, by Theorem 15.6.

As a consequence, we can now obtain a characterization of meromorphic functions (see Definition 10.41):

15.12 Theorem Every meromorphic function in an open set $\Omega$ is a quotient of two functions which are holomorphic in $\Omega$.

The converse is obvious: If $g \in H(\Omega), h \in H(\Omega)$, and $h$ is not identically 0 in any component of $\Omega$, then $g / h$ is meromorphic in $\Omega$.

Proof Suppose $f$ is meromorphic in $\Omega$; let $A$ be the set of all poles of $f$ in $\Omega$; and for each $\alpha \in A$, let $m(\alpha)$ be the order of the pole of $f$ at $\alpha$. By Theorem 15.11 there exists an $h \in H(\Omega)$ such that $h$ has a zero of multiplicity $m(\alpha)$ at each $\alpha \in A$, and $h$ has no other zeros. Put $g=f h$. The singularities of $g$ at the points of $A$ are removable, hence we can extend $g$ so that $g \in H(\Omega)$. Clearly, $f=g / h$ in $\Omega-A$.

## An Interpolation Problem

The Mittag-Leffler theorem may be combined with the Weierstrass theorem 15.11 to give a solution of the following problem: Can we take an arbitrary set $A \subset \Omega$, without limit point in $\Omega$, and find a function $f \in H(\Omega)$ which has prescribed values at every point of $A$ ? The answer is affirmative. In fact, we can do even better, and also prescribe finitely many derivatives at each point of $A$ :

15.13 Theorem Suppose $\Omega$ is an open set in the plane, $A \subset \Omega, A$ has no limit point in $\Omega$, and to each $\alpha \in A$ there are associated a nonnegative integer $m(\alpha)$
and complex numbers $w_{n, \alpha}, 0 \leq n \leq m(\alpha)$. Then there exists an $f \in H(\Omega)$ such that

$$
f^{(n)}(\alpha)=n ! w_{n, \alpha} \quad(\alpha \in A, 0 \leq n \leq m(\alpha))
$$

Proof By Theorem 15.11, there exists a $g \in H(\Omega)$ whose only zeros are in $A$ and such that $g$ has a zero of order $m(\alpha)+1$ at each $\alpha \in A$. We claim we can associate to each $\alpha \in A$ a function $P_{\alpha}$ of the form

$$
P_{\alpha}(z)=\sum_{j=1}^{1+m(\alpha)} c_{j, \alpha}(z-\alpha)^{-j}
$$

such that $g P_{\alpha}$ has the power series expansion

$$
g(z) P_{\alpha}(z)=w_{0, \alpha}+w_{1, \alpha}(z-\alpha)+\cdots+w_{m(\alpha), \alpha}(z-\alpha)^{m(\alpha)}+\cdots
$$

in some disc with center at $\alpha$.

To simplify the writing, take $\alpha=0$ and $m(\alpha)=m$, and omit the subscripts $\alpha$. For $z$ near 0 , we have

$$
g(z)=b_{1} z^{m+1}+b_{2} z^{m+2}+\cdots,
$$

where $b_{1} \neq 0$. If

$$
P(z)=c_{1} z^{-1}+\cdots+c_{m+1} z^{-m-1},
$$

then

$$
g(z) P(z)=\left(c_{m+1}+c_{m} z+\cdots+c_{1} z^{m}\right) \quad\left(b_{1}+b_{2} z+b_{3} z^{2}+\cdots\right)
$$

The $b$ 's are given, and we want to choose the $c$ 's so that

$$
g(z) P(z)=w_{0}+w_{1} z+\cdots+w_{m} z^{m}+\cdots .
$$

If we compare the coefficients of $1, z, \ldots, z^{m}$ in (6) and (7), we can solve the resulting equations successively for $c_{m+1}, c_{m}, \ldots, c_{1}$, since $b_{1} \neq 0$.

In this way we obtain the desired $P_{\alpha}$ 's. The Mittag-Leffler theorem now gives us a meromorphic $h$ in $\Omega$ whose principal parts are these $P_{\alpha}$ 's, and if we put $f=g h$ we obtain a function with the desired properties.

The solution of this interpolation problem can be used to determine the structure of all finitely generated ideals in the rings $H(\Omega)$.

15.14 Definition The ideal $\left[g_{1}, \ldots, g_{n}\right]$ generated by the functions $g_{1}, \ldots, g_{n} \in$ $H(\Omega)$ is the set of all functions of the form $\Sigma f_{i} g_{i}$, where $f_{i} \in H(\Omega)$ for $i=1, \ldots, n$ A principal ideal is one that is generated by a single function. Note that $[1]=H(\Omega)$.

If $f \in H(\Omega), \alpha \in \Omega$, and $f$ is not identically 0 in a neighborhood of $\alpha$, the multiplicity of the zero of $f$ at $\alpha$ will be denoted by $m(f ; \alpha)$. If $f(\alpha) \neq 0$, then $m(f ; \alpha)=0$, as in Theorem 15.6.

15.15 Theorem Every finitely generated ideal in $H(\Omega)$ is principal.

More explicitly: If $g_{1}, \ldots, g_{n} \in H(\Omega)$, then there exist functions $g, f_{i}, h_{i} \in H(\Omega)$ such that

$$
g=\sum_{i=1}^{n} f_{i} g_{i} \quad \text { and } \quad g_{i}=h_{i} g \quad(1 \leq i \leq n)
$$

Proof We shall assume that $\Omega$ is a region. This is done to avoid problems posed by functions that are identically 0 in some components of $\Omega$ but not in all. Once the theorem is proved for regions, that case can be applied to each component of an arbitrary open set $\Omega$, and the full theorem can be deduced. We leave the details of this as an exercise.

Let $P(n)$ be the following proposition:

If $g_{1}, \ldots, g_{n} \in H(\Omega)$, if no $g_{i}$ is identically 0 , and if no point of $\Omega$ is a zero of every $g_{i}$, then $\left[g_{1}, \ldots, g_{n}\right]=[1]$.

$P(1)$ is trivial. Assume that $n>1$ and that $P(n-1)$ is true. Take $g_{1}, \ldots$, $g_{n} \in H(\Omega)$, without common zero. By the Weierstrass theorem 15.11 there exists $\varphi \in H(\Omega)$ such that

$$
m(\varphi ; \alpha)=\min \left\{m\left(g_{i} ; \alpha\right): 1 \leq i \leq n-1\right\} \quad(\alpha \in \Omega)
$$

The functions $f_{i}=g_{i} / \varphi(1 \leq i \leq n-1)$ are in $H(\Omega)$ and have no common zero in $\Omega$. Since $P(n-1)$ is true, $\left[f_{1}, \ldots, f_{n-1}\right]=[1]$. Hence

$$
\left[g_{1}, \ldots, g_{n-1}, g_{n}\right]=\left[\varphi, g_{n}\right]
$$

Moreover, our choice of $\varphi$ shows that $g_{n}(\alpha) \neq 0$ at every point of the set $A=\{\alpha \in \Omega: \varphi(\alpha)=0\}$. Hence it follows from Theorem 15.13 that there exists $h \in H(\Omega)$ such that

$$
m\left(1-h g_{n} ; \alpha\right) \geq m(\varphi ; \alpha) \quad(\alpha \in \Omega)
$$

Such an $h$ is obtained by a suitable choice of the prescribed values of $h^{(k)}(\alpha)$ for $\alpha \in A$ and for $0 \leq k \leq m(\varphi ; \alpha)$.

By (3), $\left(1-h g_{n}\right) / \varphi$ has removable singularities. Thus

$$
1=h g_{n}+f \varphi
$$

for some $f \in H(\Omega)$. By (2) and (4), $1 \in\left[g_{1}, \ldots, g_{n}\right]$.

We have shown that $P(n-1)$ implies $P(n)$. Hence $P(n)$ is true for all $n$.

Finally, suppose $G_{1}, \ldots, G_{n} \in H(\Omega)$, and no $G_{i}$ is identically 0 . (This involves no loss of generality.) Another application of Theorem 15.11 yields $\varphi \in H(\Omega)$ with $m(\varphi ; \alpha)=\min m\left(G_{i} ; \alpha\right)$ for all $\alpha \in \Omega$. Put $g_{i}=G_{i} / \varphi$. Then $g_{i} \in$ $H(\Omega)$, and the functions $g_{1}, \ldots, g_{n}$ have no common zeros in $\Omega$. By $P(n)$, $\left[g_{1}, \ldots, g_{n}\right]=[1]$. Hence $\left[G_{1}, \ldots, G_{n}\right]=[\varphi]$. This completes the proof. I///

## Jensen's Formula

15.16 As we see from Theorem 15.11, the location of the zeros of a holomorphic function in a region $\Omega$ is subject to no restriction except the obvious one concerning the absence of limit points in $\Omega$. The situation is quite different if we replace $H(\Omega)$ by certain subclasses which are defined by certain growth conditions. In those situations the distribution of the zeros has to satisfy certain quantitative conditions. The basis of most of these theorems is Jensen's formula (Theorem 15.18). We shall apply it to certain classes of entire functions and to certain subclasses of $H(U)$.

The following lemma affords an opportunity to apply Cauchy's theorem to the evaluation of a definite integral.

15.17 Lemma $\frac{1}{2 \pi} \int_{0}^{2 \pi} \log \left|1-e^{i \theta}\right| d \theta=0$.

ProOF Let $\Omega=\{z: \operatorname{Re} z<1\}$. Since $1-z \neq 0$ in $\Omega$ and $\Omega$ is simply connected, there exists an $h \in H(\Omega)$ such that

$$
\exp \{h(z)\}=1-z
$$

in $\Omega$, and this $h$ is uniquely determined if we require that $h(0)=0$. Since $\operatorname{Re}(1-z)>0$ in $\Omega$, we then have

$$
\operatorname{Re} h(z)=\log |1-z|, \quad|\operatorname{Im} h(z)|<\frac{\pi}{2} \quad(z \in \Omega)
$$

For small $\delta>0$, let $\Gamma$ be the path

$$
\Gamma(t)=e^{i t} \quad(\delta \leq t \leq 2 \pi-\delta)
$$

and let $\gamma$ be the circular arc whose center is at 1 and which passes from $e^{i \delta}$ to $e^{-i \delta}$ within $U$. Then

$$
\frac{1}{2 \pi} \int_{\delta}^{2 \pi-\delta} \log \left|1-e^{i \theta}\right| d \theta=\operatorname{Re}\left[\frac{1}{2 \pi i} \int_{\Gamma} h(z) \frac{d z}{z}\right]=\operatorname{Re}\left[\frac{1}{2 \pi i} \int_{\gamma} h(z) \frac{d z}{z}\right]
$$

The last equality depended on Cauchy's theorem; note that $h(0)=0$.

The length of $\gamma$ is less than $\pi \delta$, so (1) shows that the absolute value of the last integral in (3) is less than $C \delta \log (1 / \delta)$, where $C$ is a constant. This gives the result if $\delta \rightarrow 0$ in (3).

15.18 Theorem Suppose $\Omega=D(0 ; R), f \in H(\Omega), f(0) \neq 0,0<r<R$, and $\alpha_{1}$, $\ldots, \alpha_{N}$ are the zeros of $f$ in $\bar{D}(0 ; r)$, listed according to their multiplicities. Then

$$
|f(0)| \prod_{n=1}^{N} \frac{r}{\left|\alpha_{n}\right|}=\exp \left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f\left(r e^{i \theta}\right)\right| d \theta\right\}
$$

This is known as Jensen's formula. The hypothesis $f(0) \neq 0$ causes no harm in applications, for if $f$ has a zero of order $k$ at 0 , the formula can be applied to $f(z) / z^{k}$.

Proof Order the points $\alpha_{j}$ so that $\alpha_{1}, \ldots, \alpha_{m}$ are in $D(0 ; r)$ and $\left|\alpha_{m+1}\right|=$ $\cdots=\left|\alpha_{N}\right|=r$. (Of course, we may have $m=N$ or $m=0$.) Put

$$
g(z)=f(z) \prod_{n=1}^{m} \frac{r^{2}-\bar{\alpha}_{n} z}{r\left(\alpha_{n}-z\right)} \prod_{n=m+1}^{N} \frac{\alpha_{n}}{\alpha_{n}-z} .
$$

Then $g \in H(D)$, where $D=D(0 ; r+\epsilon)$ for some $\epsilon>0, g$ has no zero in $D$, hence $\log |g|$ is harmonic in $D$ (Theorem 13.12), and so

$$
\log |g(0)|=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|g\left(r e^{i \theta}\right)\right| d \theta
$$

By (2),

$$
|g(0)|=|f(0)| \prod_{n=1}^{m} \frac{r}{\left|\alpha_{n}\right|}
$$

For $1 \leq n \leq m$, the factors in (2) have absolute value 1 if $|z|=r$. If $\alpha_{n}=r e^{i \theta_{n}}$ for $m<n \leq N$, it follows that

$$
\log \left|g\left(r e^{i \theta}\right)\right|=\log \left|f\left(r e^{i \theta}\right)\right|-\sum_{n=m+1}^{N} \log \left|1-e^{i\left(\theta-\theta_{n}\right)}\right| \text {. }
$$

Lemma 15.17 shows therefore that the integral in (3) is unchanged if $g$ is replaced by $f$. Comparison with (4) now gives (1).

Jensen's formula gives rise to an inequality which involves the boundary values of bounded holomorphic functions in $U$ (we recall that the class of these functions has been denoted by $H^{\infty}$ ):

15.19 Theorem If $f \in H^{\infty}, f$ not identically 0 , define

$$
\mu_{r}(f)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f\left(r e^{i \theta}\right)\right| d \theta \quad(0<r<1)
$$

and

$$
\mu^{*}(f)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f^{*}\left(e^{i \theta}\right)\right| d \theta
$$

where $f^{*}$ is the radial limit function of $f$, as in Theorem 11.32. Then

$$
\begin{aligned}
& \mu_{r}(f) \leq \mu_{s}(f) \quad \text { if } \quad 0<r<s<1, \\
& \mu_{r}(f) \rightarrow \log |f(0)| \quad \text { as } \quad r \rightarrow 0
\end{aligned}
$$

and

$$
\mu_{r}(f) \leq \mu^{*}(f) \quad \text { if } \quad 0<r<1
$$

Note the following consequence: One can choose $r$ so that $f(z) \neq 0$ if $|z|=r$; then $\mu_{r}(f)$ is finite, and so is $\mu^{*}(f)$, by (5). Thus $\log \left|f^{*}\right| \in L^{1}(T)$, and $f^{*}\left(e^{i \theta}\right) \neq 0$ at almost every point of $T$.

ProOF There is an integer $m \geq 0$ such that $f(z)=z^{m} g(z), g \in H^{\infty}$, and $g(0) \neq$ 0 . Apply Jensen's formula 15.18(1) to $g$ in place of $f$. Its left side obviously cannot decrease if $r$ increases. Thus $\mu_{r}(g) \leq \mu_{s}(g)$ if $r<s$. Since

$$
\mu_{r}(f)=\mu_{r}(g)+m \log r
$$

we have proved (3).

Let us now assume, without loss of generality, that $|f| \leq 1$. Write $f_{r}\left(e^{i \theta}\right)$ in place of $f\left(r e^{i \theta}\right)$. Then $f_{r} \rightarrow f(0)$ as $r \rightarrow 0$, and $f_{r} \rightarrow f^{*}$ a.e. as $r \rightarrow 1$. Since $\log \left(1 /\left|f_{r}\right|\right) \geq 0$, two applications of Fatou's lemma, combined with (3), give (4) and (5).

15.20 Zeros of Entire Functions Suppose $f$ is an entire function,

$$
M(r)=\sup _{\theta}\left|f\left(r e^{i \theta}\right)\right| \quad(0<r<\infty)
$$

and $n(r)$ is the number of zeros of $f$ in $\bar{D}(0 ; r)$. Assume $f(0)=1$, for simplicity. Jensen's formula gives

$$
M(2 r) \geq \exp \left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f\left(2 r e^{i \theta}\right)\right| d \theta\right\}=\prod_{n=1}^{n(2 r)} \frac{2 r}{\left|\alpha_{n}\right|} \geq \prod_{n=1}^{n(r)} \frac{2 r}{\left|\alpha_{n}\right|} \geq 2^{n(r)}
$$

if $\left\{\alpha_{n}\right\}$ is the sequence of zeros of $f$, arranged so that $\left|\alpha_{1}\right| \leq\left|\alpha_{2}\right| \leq \cdots$. Hence

$$
n(r) \log 2 \leq \log M(2 r) .
$$

Thus the rapidity with which $n(r)$ can increase (i.e., the density of the zeros of $f)$ is controlled by the rate of growth of $M(r)$. Suppose, to look at a more specific situation, that for large $r$

$$
M(r)<\exp \left\{A r^{k}\right\}
$$

where $A$ and $k$ are given positive numbers. Then (2) leads to

$$
\limsup _{r \rightarrow \infty} \frac{\log n(r)}{\log r} \leq k
$$

For example, if $k$ is a positive integer and

$$
f(z)=1-e^{z^{k}}
$$

then $n(r)$ is about $\pi^{-1} k r^{k}$, so that

$$
\lim _{r \rightarrow \infty} \frac{\log n(r)}{\log r}=k
$$

This shows that the estimate (4) cannot be improved.

## Blaschke Products

Jensen's formula makes it possible to determine the precise conditions which the zeros of a nonconstant $f \in H^{\infty}$ must satisfy.

15.21 Theorem If $\left\{\alpha_{n}\right\}$ is a sequence in $U$ such that $\alpha_{n} \neq 0$ and

$$
\sum_{n=1}^{\infty}\left(1-\left|\alpha_{n}\right|\right)<\infty
$$

if $k$ is a nonnegative integer, and if

$$
B(z)=z^{k} \prod_{n=1}^{\infty} \frac{\alpha_{n}-z}{1-\bar{\alpha}_{n} z} \frac{\left|\alpha_{n}\right|}{\alpha_{n}} \quad(z \in U)
$$

then $B \in H^{\infty}$, and $B$ has no zeros except at the points $\alpha_{n}$ (and at the origin, if $k>0$ ).

We call this function $B$ a Blaschke product. Note that some of the $\alpha_{n}$ may be repeated, in which case $B$ has multiple zeros at those points. Note also that each factor in (2) has absolute value 1 on $T$.

The term "Blaschke product" will also be used if there are only finitely many factors, and even if there are none, in which case $B(z)=1$.

Proof The $n$th term in the series

$$
\begin{array}{cc} 
& \sum_{n=1}^{\infty}\left|1-\frac{\alpha_{n}-z}{1-\bar{\alpha}_{n} z} \cdot \frac{\left|\alpha_{n}\right|}{\alpha_{n}}\right| \\
\text { is } & \left|\frac{\alpha_{n}+\left|\alpha_{n}\right| z}{\left(1-\bar{\alpha}_{n} z\right) \alpha_{n}}\right|\left(1-\left|\alpha_{n}\right|\right) \leq \frac{1+r}{1-r}\left(1-\left|\alpha_{n}\right|\right)
\end{array}
$$

if $|z| \leq r$. Hence Theorem 15.6 shows that $B \in H(U)$ and that $B$ has only the prescribed zeros. Since each factor in (2) has absolute value less than 1 in $U$, it follows that $|B(z)|<1$, and the proof is complete.

15.22 The preceding theorem shows that

$$
\sum_{n=1}^{\infty}\left(1-\left|\alpha_{n}\right|\right)<\infty
$$

is a sufficient condition for the existence of an $f \in H^{\infty}$ which has only the prescribed zeros $\left\{\alpha_{n}\right\}$. This condition also turns out to be necessary: If $f \in H^{\infty}$ and $f$ is not identically zero, the zeros of $f$ must satisf $y$ (1). This is a special case of Theorem 15.23. It is interesting that (1) is a necessary condition in a much larger class of functions, which we now describe.

For any real number $t$, define $\log ^{+} t=\log t$ if $t \geq 1$ and $\log ^{+} t=0$ if $t<1$. We let $N$ (for Nevanlinna) be the class of all $f \in H(U)$ for which

$$
\sup _{0<r<1} \frac{1}{2 \pi} \int_{-\pi}^{\pi} \log ^{+}\left|f\left(r e^{i \theta}\right)\right| d \theta<\infty
$$

It is clear that $H^{\infty} \subset N$. Note that (2) imposes a restriction on the rate of growth of $|f(z)|$ as $|z| \rightarrow 1$, whereas the boundedness of the integrals

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f\left(r e^{i \theta}\right)\right| d \theta
$$

imposes no such restriction. For instance, (3) is independent of $r$ if $f=e^{g}$ for any $g \in H(U)$. The point is that (3) can stay small because $\log |f|$ assumes large negative values as well as large positive ones, whereas $\log ^{+}|f| \geq 0$. The class $N$ will be discussed further in Chap. 17.

15.23 Theorem Suppose $f \in N, f$ is not identically 0 in $U$, and $\alpha_{1}, \alpha_{2}, \alpha_{3}, \ldots$ are the zeros of $f$, listed according to their multiplicities. Then

$$
\sum_{n=1}^{\infty}\left(1-\left|\alpha_{n}\right|\right)<\infty
$$

(We tacitly assume that $f$ has infinitely many zeros in $U$. If there are only finitely many, the above sum has only finitely many terms, and there is nothing to prove. Also, $\left|\alpha_{n}\right| \leq\left|\alpha_{n+1}\right|$.)

Proof If $f$ has a zero of order $m$ at the origin, and $g(z)=z^{-m} f(z)$, then $g \in N$, and $g$ has the same zeros as $f$, except at the origin. Hence we may assume, without loss of generality, that $f(0) \neq 0$. Let $n(r)$ be the number of zeros of $f$ in $\bar{D}(0 ; r)$, fix $k$, and take $r<1$ so that $n(r)>k$. Then Jensen's formula

$$
|f(0)| \prod_{n=1}^{n(r)} \frac{r}{\left|\alpha_{n}\right|}=\exp \left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f\left(r e^{i \theta}\right)\right| d \theta\right\}
$$

implies that

$$
|f(0)| \prod_{n=1}^{k} \frac{r}{\left|\alpha_{n}\right|} \leq \exp \left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log ^{+}\left|f\left(r e^{i \theta}\right)\right| d \theta\right\}
$$

Our assumption that $f \in N$ is equivalent to the existence of a constant $C<\infty$ which exceeds the right side of (3) for all $r, 0<r<1$. It follows that

$$
\prod_{n=1}^{k}\left|\alpha_{n}\right| \geq C^{-1}|f(0)| r^{k}
$$

The inequality persists, for every $k$, as $r \rightarrow 1$. Hence

$$
\prod_{n=1}^{\infty}\left|\alpha_{n}\right| \geq C^{-1}|f(0)|>0
$$

By Theorem 15.5, (5) implies (1).

Corollary If $f \in H^{\infty}$ (or even if $\left.f \in N\right)$, if $\alpha_{1}, \alpha_{2}, \alpha_{3}, \ldots$ are the zeros of $f$ in $U$, and if $\Sigma\left(1-\left|\alpha_{n}\right|\right)=\infty$, then $f(z)=0$ for all $z \in U$.

For instance, no nonconstant bounded holomorphic function in $U$ can have a zero at each of the points $(n-1) / n(n=1,2,3, \ldots)$.

We conclude this section with a theorem which describes the behavior of a Blaschke product near the boundary of $U$. Recall that as a member of $H^{\infty}, B$ has radial limits $B^{*}\left(e^{i \theta}\right)$ at almost all points of $T$.

15.24 Theorem If $B$ is a Blaschke product, then $\left|B^{*}\left(e^{i \theta}\right)\right|=1$ a.e. and

$$
\lim _{r \rightarrow 1} \frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|B\left(r e^{i \theta}\right)\right| d \theta=0
$$

ProOF The existence of the limit is a consequence of the fact that the integral is a monotonic function of $r$. Suppose $B(z)$ is as in Theorem 15.21, and put

$$
B_{N}(z)=\prod_{n=N}^{\infty} \frac{\alpha_{n}-z}{1-\bar{\alpha}_{n} z} \cdot \frac{\left|\alpha_{n}\right|}{\alpha_{n}}
$$

Since $\log \left(\left|B / B_{N}\right|\right)$ is continuous in an open set containing $T$, the limit (1) is unchanged if $B$ is replaced by $B_{N}$. If we apply Theorem 15.19 to $B_{N}$ we therefore obtain

$$
\log \left|B_{N}(0)\right| \leq \lim _{r \rightarrow 1} \frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|B\left(r e^{i \theta}\right)\right| d \theta \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|B^{*}\left(e^{i \theta}\right)\right| d \theta \leq 0
$$

As $N \rightarrow \infty$, the first term in (3) tends to 0 . This gives (1), and shows that $\int \log \left|B^{*}\right|=0$. Since $\log \left|B^{*}\right| \leq 0$ a.e., Theorem 1.39(a) now implies that $\log \left|B^{*}\right|=0$ a.e.

## The Müntz-Szasz Theorem

15.25 A classical theorem of Weierstrass ([26], Theorem 7.26) states that the polynomials are dense in $C(I)$, the space of all continuous complex functions on
the closed interval $I=[0,1]$, with the supremum norm. In other words, the set of all finite linear combinations of the functions

$$
1, t, t^{2}, t^{3}, \ldots
$$

is dense in $C(I)$. This is sometimes expressed by saying that the functions (1) span $C(I)$.

This suggests a question: If $0<\lambda_{1}<\lambda_{2}<\lambda_{3}<\cdots$, under what conditions is it true that the functions

$$
1, t^{\lambda_{1}}, t^{\lambda_{2}}, t^{\lambda_{3}}, \ldots
$$

$\operatorname{span} C(I) ?$

It turns out that this problem has a very natural connection with the problem of the distribution of the zeros of a bounded holomorphic function in a half plane (or in a disc; the two are conformally equivalent). The surprisingly neat answer is that the functions (2) span $C(I)$ if and only if $\Sigma 1 / \lambda_{n}=\infty$.

Actually, the proof gives an even more precise conclusion:

15.26 Theorem Suppose $0<\lambda_{1}<\lambda_{2}<\lambda_{3}<\cdots$ and let $X$ be the closure in $C(I)$ of the set of all finite linear combinations of the functions

$$
1, t^{\lambda_{1}}, t^{\lambda_{2}}, t^{\lambda_{3}}, \ldots
$$

(a) If $\Sigma 1 / \lambda_{n}=\infty$, then $X=C(I)$.

(b) If $\Sigma 1 / \lambda_{n}<\infty$, and if $\lambda \notin\left\{\lambda_{n}\right\}, \lambda \neq 0$, then $X$ does not contain the function $t^{\lambda}$.

Proof It is a consequence of the Hahn-Banach theorem (Theorem 5.19) that $\varphi \in C(I)$ but $\varphi \notin X$ if and only if there is a bounded linear functional on $C(I)$ which does not vanish at $\varphi$ but which vanishes on all of $X$. Since every bounded linear functional on $C(I)$ is given by integration with respect to a complex Borel measure on $I,(a)$ will be a consequence of the following proposition:

If $\Sigma 1 / \lambda_{n}=\infty$ and if $\mu$ is a complex Borel measure on I such that

$$
\int_{I} t^{\lambda_{n}} d \mu(t)=0 \quad(n=1,2,3, \ldots)
$$

then also

$$
\int_{I} t^{k} d \mu(t)=0 \quad(k=1,2,3, \ldots)
$$

For if this is proved, the preceding remark shows that $X$ contains all functions $t^{k}$; since $1 \in X$, all polynomials are then in $X$, and the Weierstrass theorem therefore implies that $X=C(I)$.

So assume that (1) holds. Since the integrands in (1) and (2) vanish at 0 , we may as well assume that $\mu$ is concentrated on $(0,1]$. We associate with $\mu$ the function

$$
f(z)=\int_{I} t^{z} d \mu(t)
$$

For $t>0, t^{z}=\exp (z \log t)$, by definition. We claim that $f$ is holomorphic in the right half plane. The continuity of $f$ is easily checked, and we can then apply Morera's theorem. Furthermore, if $z=x+i y$, if $x>0$, and if $0<t \leq 1$, then $\left|t^{z}\right|=t^{x} \leq 1$. Thus $f$ is bounded in the right half plane, and (1) says that $f\left(\lambda_{n}\right)=0$, for $n=1,2,3, \ldots$. Define

$$
g(z)=f\left(\frac{1+z}{1-z}\right) \quad(z \in U)
$$

Then $g \in H^{\infty}$ and $g\left(\alpha_{n}\right)=0$, where $\alpha_{n}=\left(\lambda_{n}-1\right) /\left(\lambda_{n}+1\right)$. A simple computation shows that $\Sigma\left(1-\left|\alpha_{n}\right|\right)=\infty$ if $\Sigma 1 / \lambda_{n}=\infty$. The Corollary to Theorem 15.23 therefore tells us that $g(z)=0$ for all $z \in U$. Hence $f=0$. In particular, $f(k)=0$ for $k=1,2,3, \ldots$, and this is (2). We have thus proved part $(a)$ of the theorem.

To prove $(b)$ it will be enough to construct a measure $\mu$ on $I$ such that (3) defines a function $f$ which is holomorphic in the half plane $\operatorname{Re} z>-1$ (anything negative would do here), which is 0 at $0, \lambda_{1}, \lambda_{2}, \lambda_{3}, \ldots$ and which has no other zeros in this half plane. For the functional induced by this measure $\mu$ will then vanish on $X$ but will not vanish at any function $t^{\lambda}$ if $\lambda \neq 0$ and $\lambda \notin\left\{\lambda_{n}\right\}$.

We begin by constructing a function $f$ which has these prescribed zeros, and we shall then show that this $f$ can be represented in the form (3). Define

$$
f(z)=\frac{z}{(2+z)^{3}} \prod_{n=1}^{\infty} \frac{\lambda_{n}-z}{2+\lambda_{n}+z}
$$

Since

$$
1-\frac{\lambda_{n}-z}{2+\lambda_{n}+z}=\frac{2 z+2}{2+\lambda_{n}+z}
$$

the infinite product in (5) converges uniformly on every compact set which contains none of the points $-\lambda_{n}-2$. It follows that $f$ is a meromorphic function in the whole plane, with poles at -2 and $-\lambda_{n}-2$, and with zeros at $0, \lambda_{1}, \lambda_{2}, \lambda_{3}, \ldots$. Also, each factor in the infinite product (5) is less than 1 in absolute value if $\operatorname{Re} z>-1$. Thus $|f(z)| \leq 1$ if $\operatorname{Re} z \geq-1$. The factor $(2+z)^{3}$ ensures that the restriction of $f$ to the line $\operatorname{Re} z=-1$ is in $L^{1}$.

Fix $z$ so that $\operatorname{Re} z>-1$, and consider the Cauchy formula for $f(z)$, where the path of integration consists of the semicircle with center at -1 , radius $R>1+|z|$, from $-1-i R$ to $-1+R$ to $-1+i R$, followed by the
interval from $-1+i R$ to $-1-i R$. The integral over the semicircle tends to 0 as $R \rightarrow \infty$, so we are left with

$$
f(z)=-\frac{1}{2 \pi} \int_{-\infty}^{\infty} \frac{f(-1+i s)}{-1+i s-z} d s \quad(\operatorname{Re} z>-1)
$$

But

$$
\frac{1}{1+z-i s}=\int_{0}^{1} t^{z-i s} d t \quad(\operatorname{Re} z>-1)
$$

Hence (6) can be rewritten in the form

$$
f(z)=\int_{0}^{1} t^{z}\left\{\frac{1}{2 \pi} \int_{-\infty}^{\infty} f(-1+i s) e^{-i s \log t} d s\right\} d t
$$

The interchange in the order of integration was legitimate: If the integrand in $(8)$ is replaced by its absolute value, a finite integral results.

Put $g(s)=f(-1+i s)$. Then the inner integral in (8) is. $\hat{g}(\log t)$, where $\hat{g}$ is the Fourier transform of $g$. This is a bounded continuous function on $(0,1]$, and if we set $d \mu(t)=\hat{g}(\log t) d t$ we obtain a measure which represents $f$ in the desired form (3).

This completes the proof.

15.27 Remark The theorem implies that whenever $\left\{1, t^{\lambda_{1}}, t^{\lambda_{2}}, \ldots\right\}$ spans $C(I)$, then some infinite subcollection of the $t^{\lambda_{i}}$ can be removed without altering the span. In particular, $C(I)$ contains no minimal spanning sets of this type. This is in marked contrast to the behavior of orthonormal sets in a Hilbert space: if any element is removed from an orthonormal set, its span is diminished. Likewise, if $\left\{1, t^{\lambda_{1}}, t^{\lambda_{2}} \ldots\right\}$ does not span $C(I)$, removal of any of its elements will diminish the span; this follows from Theorem 15.26(b).

## Exercises

1 Suppose $\left\{a_{n}\right\}$ and $\left\{b_{n}\right\}$ are sequences of complex numbers such that $\Sigma\left|a_{n}-b_{n}\right|<\infty$. On what sets will the product

$$
\prod_{n=1}^{\infty} \frac{z-a_{n}}{z-b_{n}}
$$

converge uniformly? Where will it define a holomorphic function?

2 Suppose $f$ is entire, $\lambda$ is a positive number, and the inequality

$$
|f(z)|<\exp \left(|z|^{\lambda}\right)
$$

holds for all large enough $|z|$. (Such functions $f$ are said to be of finite order. The greatest lower bound of all $\lambda$ for which the above condition holds is the order of $f$.) If $f(z)=\Sigma a_{n} z^{n}$, prove that the inequality

$$
\left|a_{n}\right| \leq\left(\frac{e \lambda}{n}\right)^{n / \lambda}
$$

holds for all large enough $n$. Consider the functions $\exp \left(z^{k}\right), k=1,2,3, \ldots$, to determine whether the above bound on $\left|a_{n}\right|$ is close to best possible.

3 Find all complex $z$ for which $\exp (\exp (z))=1$. Sketch them as points in the plane. Show that there is no entire function of finite order which has a zero at each of these points (except, of course, $f \equiv 0$ ).

4 Show that the function

$$
\pi \cot \pi z=\pi \mathrm{i} \frac{e^{\pi i z}+e^{-\pi i z}}{e^{\pi i z}-e^{-\pi i z}}
$$

has a simple pole with residue 1 at each integer. The same is true of the function

$$
f(z)=\frac{1}{z}+\sum_{n=1}^{\infty} \frac{2 z}{z^{2}-n^{2}}=\lim _{N \rightarrow \infty} \sum_{n=-N}^{N} \frac{1}{z-n}
$$

Show that both functions are periodic $[f(z+1)=f(z)]$, that their difference is a bounded entire function, hence a constant, and that this constant is actually 0 , since

$$
\lim _{y \rightarrow \infty} f(\mathrm{i} y)=-2 \mathrm{i} \int_{0}^{\infty} \frac{d t}{1+t^{2}}=-\pi \mathrm{i}
$$

This gives the partial fractions decomposition

$$
\pi \cot \pi z=\frac{1}{z}+\sum_{1}^{\infty} \frac{2 z}{z^{2}-n^{2}}
$$

(Compare with Exercise 12, Chap. 9.) Note that $\pi$ cot $\pi z$ is $\left(g^{\prime} / g\right)(z)$ if $g(z)=\sin \pi z$. Deduce the product representation

$$
\frac{\sin \pi z}{\pi z}=\prod_{n=1}^{\infty}\left(1-\frac{z^{2}}{n^{2}}\right)
$$

5 Suppose $k$ is a positive integer, $\left\{z_{n}\right\}$ is a sequence of complex numbers such that $\Sigma\left|z_{n}\right|^{-k-1}<\infty$, and

$$
f(z)=\prod_{n=1}^{\infty} E_{k}\left(\frac{z}{z_{n}}\right)
$$

(See Definition 15.7.) What can you say about the rate of growth of

$$
M(r)=\max _{\theta}\left|f\left(r e^{i \theta}\right)\right| ?
$$

6 Suppose $f$ is entire, $f(0) \neq 0,|f(z)|<\exp \left(|z|^{p}\right)$ for large $|z|$, and $\left\{z_{n}\right\}$ is the sequence of zeros of $f$, counted according to their multiplicities. Prove that $\Sigma\left|z_{n}\right|^{-p-\epsilon}<\infty$ for every $\epsilon>0$. (Compare with Sec. 15.20.)

7 Suppose $f$ is an entire function, $f(\sqrt{n})=0$ for $n=1,2,3, \ldots$, and there is a positive constant $\alpha$ such that $|f(z)|<\exp \left(|z|^{\alpha}\right)$ for all large enough $|z|$. For which $\alpha$ does it follow that $f(z)=0$ for all $z$ ? [Consider $\sin \left(\pi z^{2}\right)$.]

8 Let $\left\{z_{n}\right\}$ be a sequence of distinct complex numbers, $z_{n} \neq 0$, such that $z_{n} \rightarrow \infty$ as $n \rightarrow \infty$, and let $\left\{m_{n}\right\}$ be a sequence of positive integers. Let $g$ be a meromorphic function in the plane, which has a simple pole with residue $m_{n}$ at each $z_{n}$ and which has no other poles. If $z \notin\left\{z_{n}\right\}$, let $\gamma(z)$ be any path from 0 to $z$ which passes through none of the points $z_{n}$, and define

$$
f(z)=\exp \left\{\int_{y(z)} g(\zeta) d \zeta\right\}
$$

Prove that $f(z)$ is independent of the choice of $\gamma(z)$ (although the integral itself is not), that $f$ is holomorphic in the complement of $\left\{z_{n}\right\}$, that $f$ has a removable singularity at each of the points $z_{n}$, and that the extension of $f$ has a zero of order $m_{n}$ at $z_{n}$.

The existence theorem contained in Theorem 15.9 can thus be deduced from the Mittag-Leffler theorem.

9 Suppose $0<\alpha<1,0<\beta<1, f \in H(U), f(U) \subset U$, and $f(0)=\alpha$. How many zeros can $f$ have in the $\operatorname{disc} \bar{D}(0 ; \beta)$ ? What is the answer if $(a) \alpha=\frac{1}{2}, \beta=\frac{1}{2} ;(b) \alpha=\frac{1}{4}, \beta=\frac{1}{2} ;(c) \alpha=\frac{2}{3}, \beta=\frac{1}{3} ;(d) \alpha=1 / 1,000$, $\beta=1 / 10$ ?

10 For $N=1,2,3, \ldots$, define

$$
g_{N}(z)=\prod_{n=N}^{\infty}\left(1-\frac{z^{2}}{n^{2}}\right)
$$

Prove that the ideal generated by $\left\{g_{N}\right\}$ in the ring of entire functions is not a principal ideal.

11 Under what conditions on a sequence of real numbers $y_{n}$ does there exist a bounded holomorphic function in the open right half plane which is not identically zero but which has a zero at each point $1+i y_{n}$ ? In particular, can this happen if (a) $y_{n}=\log n,(b) y_{n}=\sqrt{n}$, (c) $y_{n}=n,(d) y_{n}=n^{2}$ ?

12 Suppose $0<\left|\alpha_{n}\right|<1, \Sigma\left(1-\left|\alpha_{n}\right|\right)<\infty$, and $B$ is the Blaschke product with zeros at the points $\alpha_{n}$. Let $E$ be the set of all points $1 / \bar{\alpha}_{n}$ and let $\Omega$ be the complement of the closure of $E$. Prove that the product actually converges uniformly on every compact subset of $\Omega$, so that $B \in H(\Omega)$, and that $B$ has a pole at each point of $E$. (This is of particular interest in those cases in which $\Omega$ is connected.)

13 Put $\alpha_{n}=1-n^{-2}$, for $n=1,2,3, \ldots$, let $B$ be the Blaschke product with zeros at these points $\alpha$, and prove that $\lim _{r \rightarrow 1} B(r)=0$. (It is understood that $0<r<1$.)

More precisely, show that the estimate

$$
|B(r)|<\prod_{1}^{N-1} \frac{r-\alpha_{n}}{1-\alpha_{n} r}<\prod_{1}^{N-1} \frac{\alpha_{N}-\alpha_{n}}{1-\alpha_{n}}<2 e^{-N / 3}
$$

is valid if $\alpha_{N-1}<r<\alpha_{N}$.

14 Prove that there is a sequence $\left\{\alpha_{n}\right\}$ with $0<\alpha_{n}<1$, which tends to 1 so rapidly that the Blaschke product with zeros at the points $\alpha_{n}$ satisfies the condition

$$
\limsup _{r \rightarrow 1}|B(r)|=1
$$

Hence this $B$ has no radial limit at $z=1$.

15 Let $\varphi$ be a linear fractional transformation which maps $U$ onto $U$. For any $z \in U$ define the $\varphi$-orbit of $z$ to be the set $\left\{\varphi_{n}(z)\right\}$, where $\varphi_{0}(z)=z, \varphi_{n}(z)=\varphi\left(\varphi_{n-1}(z)\right), n=1,2,3, \ldots$. Ignore the case $\varphi(z)=z$.

(a) For which $\varphi$ is it true that the $\varphi$-orbits satisfy the Blaschke condition $\Sigma\left(1-\left|\varphi_{n}(z)\right|\right)<\infty$ ? [The answer depends in part on the location of the fixed points of $\varphi$. There may be one fixed point in $U$, or one fixed point on $T$, or two fixed points on $T$. In the last two cases it is advantageous to transfer the problem to (say) the upper half plane, and to consider transformations on it which either leave only $\infty$ fixed or leave 0 and $\infty$ fixed.]

(b) For which $\varphi$ do there exist nonconstant functions $f \in H^{\infty}$ which are invariant under $\varphi$, i.e., which satisfy the relation $f(\varphi(z))=f(z)$ for all $z \in U$ ?

16 Suppose $\left|\alpha_{1}\right| \leq\left|\alpha_{2}\right| \leq\left|\alpha_{3}\right| \leq \cdots<1$, and let $n(r)$ be the number of terms in the sequence $\left\{\alpha_{j}\right\}$ such that $\left|\alpha_{j}\right| \leq r$. Prove that

$$
\int_{0}^{1} n(r) d r=\sum_{j=1}^{\infty}\left(1-\left|\alpha_{j}\right|\right)
$$

17 If $B(z)=\Sigma c_{k} z^{k}$ is a Blaschke product with at least one zero off the origin, is it possible to have $c_{k} \geq 0$ for $k=0,1,2, \ldots$ ?

18 Suppose $B$ is a Blaschke product all of whose zeros lie on the segment $(0,1)$ and

$$
f(z)=(z-1)^{2} B(z)
$$

Prove that the derivative of $f$ is bounded in $U$.

19 Put $f(z)=\exp [-(1+z) /(1-z)]$. Using the notation of Theorem 15.19 , show that

$$
\lim _{r \rightarrow 1} \mu_{r}(f)<\mu^{*}(f)
$$

although $f \in H^{\infty}$. Note the contrast with Theorem 15.24.

20 Suppose $\lambda_{1}>\lambda_{2}>\cdots$, and $\lambda_{n} \rightarrow 0$ in the Müntz-Szasz theorem. What is the conclusion of the theorem, under these conditions?

21 Prove an analogue of the Müntz-Szasz theorem, with $L^{2}(I)$ in place of $C(I)$.

22 Put $f_{n}(t)=t^{n} e^{-t}(0 \leq t<\infty, n=0,1,2, \ldots)$ and prove that the set of all finite linear combinations of the functions $f_{n}$ is dense in $L^{2}(0, \infty)$. Hint: If $g \in L^{2}(0, \infty)$ is orthogonal to each $f_{n}$ and if

$$
F(z)=\int_{0}^{\infty} e^{-t z} \overline{g(t)} d t \quad(\operatorname{Re} z>0)
$$

then all derivatives of $F$ are 0 at $z=1$. Consider $F(1+i y)$.

23 Suppose $\Omega \supset \bar{U}, f \in H(\Omega),\left|f\left(e^{i \theta}\right)\right| \geq 3$ for all real $\theta, f(0)=0$, and $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{N}$ are the zeros of $1-f$ in $U$, counted according to their multiplicities. Prove that

$$
\left|\lambda_{1} \lambda_{2} \cdots \lambda_{N}\right|<\frac{1}{2} .
$$

Suggestion: Look at $B /(1-f)$, where $B$ is a certain Blaschke product.

## CHAPTER <br> SIXTEEN

## ANALYTIC CONTINUATION

In this chapter we shall be concerned with questions which arise because functions which are defined and holomorphic in some region can frequently be extended to holomorphic functions in some larger region. Theorem 10.18 shows that these extensions are uniquely determined by the given functions. The extension process is called analytic continuation. It leads in a very natural way to the consideration of functions which are defined on Riemann surfaces rather than in plane regions. This device makes it possible to replace "multiple-valued functions" (such as the square-root function or the logarithm) by functions. A systematic treatment of Riemann surfaces would take us too far afield, however, and we shall restrict the discussion to plane regions.

## Regular Points and Singular Points

16.1 Definition Let $D$ be an open circular disc, suppose $f \in H(D)$, and let $\beta$ be a boundary point of $D$. We call $\beta$ a regular point of $f$ if there exists a disc $D_{1}$ with center at $\beta$ and a function $g \in H\left(D_{1}\right)$ such that $g(z)=f(z)$ for all $z \in D \cap$ $D_{1}$. Any boundary point of $D$ which is not a regular point of $f$ is called a singular point of $f$.

It is clear from the definition that the set of all regular points of $f$ is an open (possibly empty) subset of the boundary of $D$.

In the following theorems we shall take the unit disc $U$ for $D$, without any loss of generality.

16.2 Theorem Suppose $f \in H(U)$, and the power series

$$
f(z)=\sum_{n=0}^{\infty} a_{n} z^{n} \quad(z \in U)
$$

has radius of convergence 1 . Then $f$ has at least one singular point on the unit circle $T$.

Proof Suppose, on the contrary, that every point of $T$ is a regular point of $f$. The compactness of $T$ implies then that there are open $\operatorname{discs} D_{1}, \ldots, D_{n}$ and functions $g_{j} \in H\left(D_{j}\right)$ such that the center of each $D_{j}$ is on $T$, such that $T \subset$ $D_{1} \cup \cdots \cup D_{n}$, and such that $g_{j}(z)=f(z)$ in $D_{j} \cap U$, for $j=1, \ldots, n$.

If $D_{i} \cap D_{j} \neq \varnothing$ and $V_{i j}=D_{i} \cap D_{j} \cap U$, then $V_{i j} \neq \varnothing$ (since the centers of the $D_{j}$ are on $T$ ), and $g_{i}=f=g_{j}$ in $V_{i j}$. Since $D_{i} \cap D_{j}$ is connected, it follows from Theorem 10.18 that $g_{i}=g_{j}$ in $D_{i} \cap D_{j}$. Hence we may define a function $h$ in $\Omega=U \cup D_{1} \cup \cdots \cup D_{n}$ by

$$
h(z)= \begin{cases}f(z) & (z \in U), \\ g_{i}(z) & \left(z \in D_{i}\right)\end{cases}
$$

Since $\Omega \supset \bar{U}$ and $\Omega$ is open, there exists an $\epsilon>0$ such that the disc $D(0 ; 1+\epsilon) \subset \Omega$. But $h \in H(\Omega), h(z)$ is given by (1) in $U$, and now Theorem 10.16 implies that the radius of convergence of (1) is at least $1+\epsilon$, contrary to our assumption.

16.3 Definition If $f \in H(U)$ and if every point of $T$ is a singular point of $f$, then $T$ is said to be the natural boundary of $f$. In this case, $f$ has no holomorphic extension to any region which properly contains $U$.

16.4 Remark It is very easy to see that there exist $f \in H(U)$ for which $T$ is a natural boundary. In fact, if $\Omega$ is any region, it is easy to find an $f \in H(\Omega)$ which has no holomorphic extension to any larger region. To see this, let $\boldsymbol{A}$ be any countable set in $\Omega$ which has no limit point in $\Omega$ but such that every boundary point of $\Omega$ is a limit point of $A$. Apply Theorem 15.11 to get a function $f \in H(\Omega)$ which is 0 at every point of $A$ but is not identically 0 . If $g \in H\left(\Omega_{1}\right)$, where $\Omega_{1}$ is a region which properly contains $\Omega$, and if $g=f$ in $\Omega$, the zeros of $g$ would have a limit point in $\Omega_{1}$, and we have a contradiction.

A simple explicit example is furnished by

$$
f(z)=\sum_{n=0}^{\infty} z^{2^{n}}=z+z^{2}+z^{4}+z^{8}+\cdots \quad(z \in U)
$$

This $f$ satisfies the functional equation

$$
f\left(z^{2}\right)=f(z)-z,
$$

from which it follows (we leave the details to the reader) that $f$ is unbounded on every radius of $U$ which ends at $\exp \left\{2 \pi i k / 2^{n}\right\}$, where $k$ and $n$ are positive
integers. These points form a dense subset of $T$; and since the set of all singular points of $f$ is closed, $f$ has $T$ as its natural boundary.

That this example is a power series with large gaps (i.e., with many zero coefficients) is no accident. The example is merely a special case of Theorem 16.6, due to Hadamard, which we shall derive from the following theorem of Ostrowski:

16.5 Theorem Suppose $\lambda, p_{k}$, and $q_{k}$ are positive integers,

$$
p_{1}<p_{2}<p_{3}<\cdots,
$$

and

$$
\lambda q_{k}>(\lambda+1) p_{k} \quad(k=1,2,3, \ldots)
$$

Suppose

$$
f(z)=\sum_{n=0}^{\infty} a_{n} z^{n}
$$

has radius of convergence 1 , and $a_{n}=0$ whenever $p_{k}<n<q_{k}$ for some $k$. If $s_{p}(z)$ is the pth partial sum of (2), and if $\beta$ is a regular point of $f$ on $T$, then the sequence $\left\{s_{p_{k}}(z)\right\}$ converges in some neighborhood of $\beta$.

Note that the full sequence $\left\{s_{p}(z)\right\}$ cannot converge at any point outside $\bar{U}$. The gap condition (1) ensures the existence of a subsequence which converges in a neighborhood of $\beta$, hence at some points outside $\bar{U}$. This phenomenon is called overconvergence.

Proof If $g(z)=f(\beta z)$, then $g$ also satisfies the gap condition. Hence we may assume, without loss of generality, that $\beta=1$. Then $f$ has a holomorphic extension to a region $\Omega$ which contains $U \cup\{1\}$. Put

$$
\varphi(w)=\frac{1}{2}\left(w^{\lambda}+w^{\lambda+1}\right)
$$

and define $F(w)=f(\varphi(w))$ for all $w$ such that $\varphi(w) \in \Omega$. If $|w| \leq 1$ but $w \neq 1$, then $|\varphi(w)|<1$, since $|1+w|<2$. Also, $\varphi(1)=1$. It follows that there exists an $\epsilon>0$ such that $\varphi(D(0 ; 1+\epsilon)) \subset \Omega$. Note that the region $\varphi(D(0 ; 1+\epsilon))$ contains the point 1 . The series

$$
F(w)=\sum_{m=0}^{\infty} b_{m} w^{m}
$$

converges if $|w|<1+\epsilon$.

The highest and lowest powers of $w$ in $[\varphi(w)]^{n}$ have exponents $(\lambda+1) n$ and $\lambda n$. Hence the highest exponent in $[\varphi(w)]^{p k}$ is less than the lowest exponent in $[\varphi(w)]^{q_{k}}$, by (1). Since

$$
F(w)=\sum_{n=0}^{\infty} a_{n}[\varphi(w)]^{n} \quad(|w|<1)
$$

the gap condition satisfied by $\left\{a_{n}\right\}$ now implies that

$$
\sum_{n=0}^{p_{k}} a_{n}[\varphi(w)]^{n}=\sum_{m=0}^{(\lambda+1) p_{k}} b_{m} w^{m} \quad(k=1,2,3, \ldots)
$$

The right side of (6) converges, as $k \rightarrow \infty$, whenever $|w|<1+\epsilon$. Hence $\left\{s_{p_{k}}(z)\right\}$ converges for all $z \epsilon \varphi(D(0 ; 1+\epsilon))$. This is the desired conclusion. ////

Note: Actually, $\left\{s_{p_{k}}(z)\right\}$ converges uniformly in some neighborhood of $\beta$. We leave it to the reader to verify this by a more careful examination of the preceding proof.

16.6 Theorem Suppose $\lambda$ is a positive integer, $\left\{p_{k}\right\}$ is a sequence of positive integers such that

$$
p_{k+1}>\left(1+\frac{1}{\lambda}\right) p_{k} \quad(k=1,2,3, \ldots)
$$

and the power series

$$
f(z)=\sum_{k=1}^{\infty} c_{k} z^{p_{k}}
$$

has radius of convergence 1 . Then f has $T$-as its natural boundary.

ProOF The subsequence $\left\{s_{p k}\right\}$ of Theorem 16.5 is now the same (except for repetitions) as the full sequence of partial sums of (2). The latter cannot converge at any point outside $\bar{U}$; hence Theorem $16.5 \mathrm{implies}$ that no point of $T$ can be a regular point of $f$.

16.7 Example Put $a_{n}=1$ if $n$ is a power of 2, put $a_{n}=0$ otherwise, put $\eta_{n}=$ $\exp (-\sqrt{n})$, and define

$$
f(z)=\sum_{n=0}^{\infty} a_{n} \eta_{n} z^{n}
$$

Since

$$
\limsup _{n \rightarrow \infty}\left|a_{n} \eta_{n}\right|^{1 / n}=1,
$$

the radius of convergence of (1) is 1 . By Hadamard's theorem, $f$ has $T$ as its natural boundary. Nevertheless, the power series of each derivative of $f$,

$$
f^{(k)}(z)=\sum_{n=k}^{\infty} n(n-1) \cdots(n-k+1) a_{n} \eta_{n} z^{n-k},
$$

converges uniformly on the closed unit disc. Each $f^{(k)}$ is therefore uniformly continuous on $\bar{U}$, and the restriction of $f$ to $T$ is infinitely differentiable, as a function of $\theta$, in spite of the fact that $T$ is the natural boundary of $f$.

The example demonstrates rather strikingly that the presence of singularities, in the sense of Definition 16.1, does not imply the presence of discontinuities or (stated less precisely) of any lack of smoothness.

This seems to be the natural place to insert a theorem in which continuity does preclude the existence of singularities:

16.8 Theorem Suppose $\Omega$ is a region, $L$ is a straight line or a circular arc, $\Omega-L$ is the union of two regions $\Omega_{1}$ and $\Omega_{2}, f$ is continuous in $\Omega$, and $f$ is holomorphic in $\Omega_{1}$ and in $\Omega_{2}$. Then $f$ is holomorphic in $\Omega$.

Proof The use of linear fractional transformations shows that the general case follows if we prove the theorem for straight lines $L$. By Morera's theorem, it is enough to show that the integral of $f$ over the boundary $\partial \Delta$ is 0 for every triangle $\Delta$ in $\Omega$. The Cauchy theorem implies that the integral of $f$ vanishes over every closed path $\gamma$ in $\Delta \cap \Omega_{1}$ or in $\Delta \cap \Omega_{2}$. The continuity of $f$ shows that this is still true if part of $\gamma$ is in $L$, and the integral over $\partial \Delta$ is the sum of at most two terms of this sort.

## Continuation along Curves

16.9 Definitions A function element is an ordered pair $(f, D)$, where $D$ is an open circular disc and $f \in H(D)$. Two function elements $\left(f_{0}, D_{0}\right)$ and $\left(f_{1}, D_{1}\right)$ are direct continuations of each other if two conditions hold: $D_{0} \cap D_{1} \neq \varnothing$, and $f_{0}(z)=f_{1}(z)$ for all $z \in D_{0} \cap D_{1}$. In this case we write

$$
\left(f_{0}, D_{0}\right) \sim\left(f_{1}, D_{1}\right)
$$

A chain is a finite sequence $\mathscr{C}$ of discs, say $\mathscr{C}=\left\{D_{0}, D_{1}, \ldots, D_{n}\right\}$, such that $D_{i-1} \cap D_{i} \neq \varnothing$ for $i=1, \ldots, n$. If $\left(f_{0}, D_{0}\right)$ is given and if there exist elements $\left(f_{i}, D_{i}\right)$ such that $\left(f_{i-1}, D_{i-1}\right) \sim\left(f_{i}, D_{i}\right)$ for $i=1, \ldots, n$, then $\left(f_{n}, D_{n}\right)$ is said to be the analytic continuation of $\left(f_{0}, D_{0}\right)$ along $\mathscr{C}$. Note that $f_{n}$ is uniquely determined by $f_{0}$ and $\mathscr{C}$ (if it exists at all). To see this, suppose (1) holds, and suppose (1) also holds with $g_{1}$ in place of $f_{1}$. Then $g_{1}=f_{0}=f_{1}$ in $D_{0} \cap D_{1}$; and since $D_{1}$ is connected, we have $g_{1}=f_{1}$ in $D_{1}$. The uniqueness of $f_{n}$ now follows by induction on the number of terms in $\mathscr{C}$.

If $\left(f_{n}, D_{n}\right)$ is the continuation of $\left(f_{0}, D_{0}\right)$ along $\mathscr{C}$, and if $D_{n} \cap D_{0} \neq \varnothing$, it need not be true that $\left(f_{0}, D_{0}\right) \sim\left(f_{n}, D_{n}\right)$; in other words, the relation $\sim$ is not transitive. The simplest example of this is furnished by the square-root function: Let $D_{0}, D_{1}$, and $D_{2}$ be discs of radius 1 , with centers $1, \omega$, and $\omega^{2}$, where $\omega^{3}=1$, choose $f_{j} \in H\left(D_{j}\right)$ so that $f_{j}^{2}(z)=z$ and so that $\left(f_{0}, D_{0}\right) \sim$ $\left(f_{1}, D_{1}\right),\left(f_{1}, D_{1}\right) \sim\left(f_{2}, D_{2}\right)$. In $D_{0} \cap D_{2}$ we have $f_{2}=-f_{0} \neq f_{0}$.

A chain $\mathscr{C}=\left\{D_{0}, \ldots, D_{n}\right\}$ is said to cover a curve $\gamma$ with parameter interval $[0,1]$ if there are numbers $0=s_{0}<s_{1}<\cdots<s_{n}=1$ such that $\gamma(0)$ is the center of $D_{0}, \gamma(1)$ is the center of $D_{n}$, and

$$
\gamma\left(\left[s_{i}, s_{i+1}\right]\right) \subset D_{i} \quad(i=0, \ldots, n-1)
$$

If $\left(f_{0}, D_{0}\right)$ can be continued along this $\mathscr{C}$ to $\left(f_{n}, D_{n}\right)$, we call $\left(f_{n}, D_{n}\right)$ an analytic continuation of $\left(f_{0}, D_{0}\right)$ along $\gamma$ (uniqueness will be proved in Theorem 16.11); $\left(f_{0}, D_{0}\right)$ is then said to admit an analytic continuation along $\gamma$.

Although the relation (1) is not transitive, a restricted form of transitivity does hold. It supplies the key to the proof of Theorem 16.11.

16.10 Proposition Suppose that $D_{0} \cap D_{1} \cap D_{2} \neq \varnothing,\left(D_{0}, f_{0}\right) \sim\left(D_{1}, f_{1}\right)$, and $\left(D_{1}, f_{1}\right) \sim\left(D_{2}, f_{2}\right)$. Then $\left(D_{0}, f_{0}\right) \sim\left(D_{2}, f_{2}\right)$.

Proof By assumption, $f_{0}=f_{1}$ in $D_{0} \cap D_{1}$ and $f_{1}=f_{2}$ in $D_{1} \cap D_{2}$. Hence $f_{0}=f_{2}$ in the nonempty open set $D_{0} \cap D_{1} \cap D_{2}$. Since $f_{0}$ and $f_{2}$ are holomorphic in $D_{0} \cap D_{2}$ and $D_{0} \cap D_{2}$ is connected, it follows that $f_{0}=f_{2}$ in $D_{0} \cap D_{2}$.

16.11 Theorem If $(f, D)$ is a function element and if $\gamma$ is a curve which starts at the center of $D$, then $(f, D)$ admits at most one analytic continuation along $\gamma$.

Here is a more explicit statement of what the theorem asserts: If $\gamma$ is covered by chains $\mathscr{C}_{1}=\left\{A_{0}, A_{1}, \ldots, A_{m}\right\}$ and $\mathscr{C}_{2}=\left\{B_{0}, B_{1}, \ldots B_{n}\right\}$, where $A_{0}=B_{0}=D$, if $(f, D)$ can be analytically continued along $\mathscr{C}_{1}$ to a function element $\left(g_{m}, A_{m}\right)$, and if $(f, D)$ can be analytically continued along $\mathscr{C}_{2}$ to $\left(h_{n}, B_{n}\right)$, then $g_{m}=h_{n}$ in $A_{m} \cap B_{n}$.

Since $A_{m}$ and $B_{n}$ are, by assumption, discs with the same center $\gamma(1)$, it follows that $g_{m}$ and $h_{n}$ have the same expansion in powers of $z-\gamma(1)$, and we may as well replace $A_{m}$ and $B_{n}$ by whichever is the larger one of the two. With this agreement, the conclusion is that $g_{m}=h_{n}$.

ProOF Let $\mathscr{C}_{1}$ and $\mathscr{C}_{2}$ be as above. There are numbers

$$
0=s_{0}<s_{1}<\cdots<s_{m}=1=s_{m+1}
$$

and $0=\sigma_{0}<\sigma_{1}<\cdots<\sigma_{n}=1=\sigma_{n+1}$ such that

$$
\gamma\left(\left[s_{i}, s_{i+1}\right]\right) \subset A_{i}, \quad \gamma\left(\left[\sigma_{j}, \sigma_{j+1}\right]\right) \subset B_{j} \quad(0 \leq i \leq m, 0 \leq j \leq n) .
$$

There are function elements $\left(g_{i}, A_{i}\right) \sim\left(g_{i+1}, A_{i+1}\right)$ and $\left(h_{j}, B_{j}\right) \sim\left(h_{j+1}, B_{j+1}\right)$, for $0 \leq i \leq m-1$ and $0 \leq j \leq n-1$. Here $g_{0}=h_{0}=f$.

We claim that if $0 \leq i \leq m$ and $0 \leq j \leq n$, and if $\left[s_{i}, s_{i+1}\right]$ intersects $\left[\sigma_{j}, \sigma_{j+1}\right]$, then $\left(g_{i}, A_{i}\right) \sim\left(h_{j}, B_{j}\right)$.

Assume there are pairs $(i, j)$ for which this is wrong. Among them there is one for which $i+j$ is minimal. It is clear that then $i+j>0$. Suppose $s_{i} \geq \sigma_{j}$. Then $i \geq 1$, and since $\left[s_{i}, s_{i+1}\right]$ intersects $\left[\sigma_{j}, \sigma_{j+1}\right]$, we see that

$$
\gamma\left(s_{i}\right) \in A_{i-1} \cap A_{i} \cap B_{j}
$$

The minimality of $i+j$ shows that $\left(g_{i-1}, A_{i-1}\right) \sim\left(h_{j}, B_{j}\right)$; and since $\left(g_{i-1}, A_{i-1}\right) \sim\left(g_{i}, A_{i}\right)$, Proposition 16.10 implies that $\left(g_{i}, A_{i}\right) \sim\left(h_{j}, B_{j}\right)$. This contradicts our assumption. The possibility $s_{i} \leq \sigma_{j}$ is ruled out in the same way.

So our claim is established. In particular, it holds for the pair $(m, n)$, and this is what we had to prove.

16.12 Definition Suppose $\alpha$ and $\beta$ are points in a topological space $X$ and $\varphi$ is a continuous mapping of the unit square $I^{2}=I \times I$ (where $I=[0,1]$ ) into $X$ such that $\varphi(0, t)=\alpha$ and $\varphi(1, t)=\beta$ for all $t \in I$. The curves $\gamma_{t}$ defined by

$$
\gamma_{t}(s)=\varphi(s, t) \quad(s \in I, t \in I)
$$

are then said to form a one-parameter family $\left\{\gamma_{t}\right\}$ of curves from $\alpha$ to $\beta$ in $X$.

We now come to a very important property of analytic continuation:

16.13 Theorem Suppose $\left\{\gamma_{t}\right\}(0 \leq t \leq 1)$ is a one-parameter family of curves from $\alpha$ to $\beta$ in the plane, $D$ is a disc with center at $\alpha$, and the function element $(f, D)$ admits analytic continuation along each $\gamma_{t}$, to an element $\left(g_{t}, D_{t}\right)$. Then $g_{1}=g_{0}$.

The last equality is to be interpreted as in Theorem 16.11:

$$
\left(g_{1}, D_{1}\right) \sim\left(g_{0}, D_{0}\right)
$$

and $D_{0}$ and $D_{1}$ are discs with the same center, namely, $\beta$.

Proof Fix $t \in I$. There is a chain $\mathscr{C}=\left\{A_{0}, \ldots, A_{n}\right\}$ which covers $\gamma_{t}$, with $A_{0}=D$, such that $\left(g_{t}, D_{t}\right)$ is obtained by continuation of $(f, D)$ along $\mathscr{C}$. There are numbers $0=s_{0}<\cdots<s_{n}=1$ such that

$$
E_{i}=\gamma_{t}\left(\left[s_{i}, s_{i+1}\right]\right) \subset A_{i} \quad(i=0,1, \ldots, n-1)
$$

There exists an $\epsilon>0$ which is less than the distance from any of the compact sets $E_{i}$ to the complement of the corresponding open disc $A_{i}$. The uniform continuity of $\varphi$ on $I^{2}$ (see Definition 16.12) shows that there exists a $\delta>0$ such that

$$
\left|\gamma_{t}(s)-\gamma_{u}(s)\right|<\epsilon \quad \text { if } s \in I, u \in I,|u-t|<\delta \text {. }
$$

Suppose $u$ satisfies these conditions. Then (2) shows that $\mathscr{C}$ covers $\gamma_{u}$, and therefore Theorem 16.11 shows that both $g_{t}$ and $g_{u}$ are obtained by continuation of $(f, D)$ along this same chain $\mathscr{C}$. Hence $g_{t}=g_{u}$.

Thus each $t \in I$ is covered by a segment $J_{t}$ such that $g_{u}=g_{t}$ for all $u \in$ $I \cap J_{t}$. Since $I$ is compact, $I$ is covered by finitely many $J_{t}$; and since $I$ is connected, we see in a finite number of steps that $g_{1}=g_{0}$.

Our next item is an intuitively obvious topological fact.

16.14 Theorem Suppose $\Gamma_{0}$ and $\Gamma_{1}$ are curves in a topological space $X$, with common initial point $\alpha$ and common end point $\beta$. If $X$ is simply connected, then there exists a one-parameter family $\left\{\gamma_{t}\right\}(0 \leq t \leq 1)$ of curves from $\alpha$ to $\beta$ in $X$, such that $\gamma_{0}=\Gamma_{0}$ and $\gamma_{1}=\Gamma_{1}$.

Proof Let $[0, \pi]$ be the parameter interval of $\Gamma_{0}$ and $\Gamma_{1}$. Then

$$
\Gamma(s)= \begin{cases}\Gamma_{0}(s) & (0 \leq s \leq \pi) \\ \Gamma_{1}(2 \pi-s) & (\pi \leq s \leq 2 \pi)\end{cases}
$$

defines a closed curve in $X$. Since $X$ is simply connected, $\Gamma$ is null-homotopic in $X$. Hence there is a continuous $H:[0,2 \pi] \times[0,1] \rightarrow X$ such that

$$
H(s, 0)=\Gamma(s), \quad H(s, 1)=c \in X, \quad H(0, t)=H(2 \pi, t)
$$

If $\Phi: \bar{U} \rightarrow X$ is defined by

$$
\Phi\left(r e^{i \theta}\right)=H(\theta, 1-r) \quad(0 \leq r \leq 1,0 \leq \theta \leq 2 \pi)
$$

(2) implies that $\Phi$ is continuous. Put

$$
\gamma_{t}(\theta)=\Phi\left[(1-t) e^{i \theta}+t e^{-i \theta}\right] \quad(0 \leq \theta \leq \pi, 0 \leq t \leq 1)
$$

Since $\Phi\left(e^{i \theta}\right)=H(\theta, 0)=\Gamma(\theta)$, it follows that

$$
\begin{array}{lr}
\gamma_{t}(0)=\Phi(1)=\Gamma(0)=\alpha & (0 \leq t \leq 1) \\
\gamma_{t}(\pi)=\Phi(-1)=\Gamma(\pi)=\beta & (0 \leq t \leq 1) \\
\gamma_{0}(\theta)=\Phi\left(e^{i \theta}\right)=\Gamma(\theta)=\Gamma_{0}(\theta) & (0 \leq \theta \leq \pi)
\end{array}
$$

and

$$
\gamma_{1}(\theta)=\Phi\left(e^{-i \theta}\right)=\Phi\left(e^{i(2 \pi-\theta)}\right)=\Gamma(2 \pi-\theta)=\Gamma_{1}(\theta) \quad(0 \leq \theta \leq \pi)
$$

This completes the proof.

## The Monodromy Theorem

The preceding considerations have essentially proved the following important theorem.

16.15 Theorem Suppose $\Omega$ is a simply connected region, $(f, D)$ is a function element, $D \subset \Omega$, and $(f, D)$ can be analytically continued along every curve in $\Omega$ that starts at the center of $D$. Then there exists $g \in H(\Omega)$ such that $g(z)=f(z)$ for all $z \in D$.

ProOF Let $\Gamma_{0}$ and $\Gamma_{1}$ be two curves in $\Omega$ from the center $\alpha$ of $D$ to some point $\beta \in \Omega$. It follows from Theorems 16.13 and 16.14 that the analytic continuations of $(f, D)$ along $\Gamma_{0}$ and $\Gamma_{1}$ lead to the same element $\left(g_{\beta}, D_{\beta}\right)$, where $D_{\beta}$ is a disc with center at $\beta$. If $D_{\beta_{1}}$ intersects $D_{\beta}$, then $\left(g_{\beta_{1}}, D_{\beta_{1}}\right)$ can be obtained by first continuing $(f, D)$ to $\beta$, then along the straight line from $\beta$ to $\beta_{1}$. This shows that $g_{\beta_{1}}=g_{\beta}$ in $D_{\beta_{1}} \cap D_{\beta}$.

The definition

$$
g(z)=g_{\beta}(z) \quad\left(z \in D_{\beta}\right)
$$

is therefore consistent and gives the desired holomorphic extension of $f$.

16.16 Remark Let $\Omega$ be a plane region, fix $w \notin \Omega$, let $D$ be a disc in $\Omega$. Since $D$ is simply connected, there exists $f \in H(D)$ such that $\exp [f(z)]=z-w$. Note that $f^{\prime}(z)=(z-w)^{-1}$ in $D$, and that the latter function is holomorphic in all of $\Omega$. This implies that $(f, D)$ can be analytically continued along every path $\gamma$ in $\Omega$ that starts at the center $\alpha$ of $D$ : If $\gamma$ goes from $\alpha$ to $\beta$, if $D_{\beta}=$ $D(\beta ; r) \subset \Omega$, if

$$
\Gamma_{z}=\gamma \dot{+}[\beta, z] \quad\left(z \in D_{\beta}\right)
$$

and if

$$
g_{\beta}(z)=\int_{\Gamma_{z}}(\zeta-w)^{-1} d \zeta+f(\alpha) \quad\left(z \in D_{\beta}\right)
$$

then $\left(g_{\beta}, D_{\beta}\right)$ is the continuation of $(f, D)$ along $\gamma$.

Note that $g_{\beta}^{\prime}(z)=(z-w)^{-1}$ in $D_{\beta}$.

Assume now that there exists $g \in H(\Omega)$ such that $g(z)=f(z)$ in $D$. Then $g^{\prime}(z)=(z-w)^{-1}$ for all $z \in \Omega$. If $\Gamma$ is a closed path in $\Omega$, it follows that

$$
\operatorname{Ind}_{\Gamma}(w)=\frac{1}{2 \pi i} \int_{\Gamma} g^{\prime}(z) d z=0
$$

We conclude (with the aid of Theorem 13.11) that the monodromy theorem fails in every plane region that is not simply connected.

## Construction of a Modular Function

16.17 The Modular Group This is the set $G$ of all linear fractional transformations $\varphi$ of the form

$$
\varphi(z)=\frac{a z+b}{c z+d}
$$

where $a, b, c$, and $d$ are integers and $a d-b c=1$.

Since $a, b, c$, and $d$ are real, each $\varphi \in G$ maps the real axis onto itself (except for $\infty)$. The imaginary part of $\varphi(i)$ is $\left(c^{2}+d^{2}\right)^{-1}>0$. Hence

$$
\varphi\left(\Pi^{+}\right)=\Pi^{+} \quad(\varphi \in G)
$$

where $\Pi^{+}$is the open upper half plane. If $\varphi$ is given by (1), then

$$
\varphi^{-1}(w)=\frac{d w-b}{-c w+a}
$$

so that $\varphi^{-1} \in G$. Also $\varphi \circ \psi \in G$ if $\varphi \in G$ and $\psi \in G$.

Thus $G$ is a group, with composition as group operation. In view of (2) it is customary to regard $G$ as a group of transformations on $\Pi^{+}$.

The transformations $z \rightarrow z+1 \quad(a=b=d=1, \quad c=0)$ and $z \rightarrow-1 / z$ $(a=d=0, b=-1, c=1)$ belong to $G$. In fact, they generate $G$ (i.e., there is no proper subgroup of $G$ which contains these two transformations). This can be proved by the same method which will be used in Theorem 16.19(c).

A modular function is a holomorphic (or meromorphic) function $f$ on $\Pi^{+}$ which is invariant under $G$ or at least under some nontrivial subgroup $\Gamma$ of $G$. This means that $f \circ \varphi=f$ for every $\varphi \in \Gamma$.

16.18 A Subgroup We shall take for $\Gamma$ the group generated by $\sigma$ and $\tau$, where

$$
\sigma(z)=\frac{z}{2 z+1}, \quad \tau(z)=z+2
$$

One of our objectives is the construction of a certain function $\lambda$ which is invariant under $\Gamma$ and which leads to a quick proof of the Picard theorem. Actually, it is the mapping properties of $\lambda$ which are important in this proof, not its invariance, and a quicker construction (using just the Riemann mapping theorem and the reflection principle) can be given. But it is instructive to study the action of $\Gamma$ on $\Pi^{+}$, in geometric terms, and we shall proceed along this route.

Let $Q$ be the set of all $z$ which satisfy the following four conditions, where $z=x+i y$ :

$$
y>0, \quad-1 \leq x<1, \quad|2 z+1| \geq 1, \quad|2 z-1|>1
$$

$Q$ is bounded by the vertical lines $x=-1$ and $x=1$ and is bounded below by two semicircles of radius $\frac{1}{2}$, with centers at $-\frac{1}{2}$ and at $\frac{1}{2}$. $Q$ contains those of its boundary points which lie in the left half of $\Pi^{+} . Q$ contains no point of the real axis.

We claim that $Q$ is a fundamental domain of $\Gamma$. This means that statements $(a)$ and $(b)$ of the following theorem are true.

16.19 Theorem Let $\Gamma$ and $Q$ be as above.

(a) If $\varphi_{1}$ and $\varphi_{2} \in \Gamma$ and $\varphi_{1} \neq \varphi_{2}$, then $\varphi_{1}(Q) \cap \varphi_{2}(Q)=\varnothing$.

(b) $\bigcup_{\varphi \in \Gamma} \varphi(Q)=\Pi^{+}$.

(c) $\Gamma$ contains all transformations $\varphi \in G$ of the form

$$
\varphi(z)=\frac{a z+b}{c z+d}
$$

for which $a$ and $d$ are odd integers, $b$ and $c$ are even.

Proof Let $\Gamma_{1}$ be the set of all $\varphi \in G$ described in (c). It is easily verified that $\Gamma_{1}$ is a subgroup of $G$. Since $\sigma \in \Gamma_{1}$ and $\tau \in \Gamma_{1}$, it follows that $\Gamma \subset \Gamma_{1}$. To show that $\Gamma=\Gamma_{1}$, i.e., to prove $(c)$, it is enough to prove that $\left(a^{\prime}\right)$ and $(b)$ hold, where $\left(a^{\prime}\right)$ is the statement obtained from $(a)$ by replacing $\Gamma$ by $\Gamma_{1}$. For if $\left(a^{\prime}\right)$ and $(b)$ hold, it is clear that $\Gamma$ cannot be a proper subset of $\Gamma_{1}$.

We shall need the relation

$$
\operatorname{Im} \varphi(z)=\frac{\operatorname{Im} z}{|c z+d|^{2}}
$$

which is valid for every $\varphi \in G$ given by (1). The proof of (2) is a matter of straightforward computation, and depends on the relation $a d-b c=1$.

We now prove $\left(a^{\prime}\right)$. Suppose $\varphi_{1}$ and $\varphi_{2} \in \Gamma_{1}, \varphi_{1} \neq \varphi_{2}$, and define $\varphi=$ $\varphi_{1}^{-1} \circ \varphi_{2}$. If $z \in \varphi_{1}(Q) \cap \varphi_{2}(Q)$, then $\varphi_{1}^{-1}(z) \in Q \cap \varphi(Q)$. It is therefore enough to show that

$$
Q \cap \varphi(Q)=\varnothing
$$

if $\varphi \in \Gamma_{1}$ and $\varphi$ is not the identity transformation.

The proof of (3) splits into three cases.

If $c=0$ in (1), then $a d=1$, and since $a$ and $d$ are integers, we have $a=d= \pm 1$. Hence $\varphi(z)=z+2 n$ for some integer $n \neq 0$, and the description of $Q$ makes it evident that (3) holds.

If $c=2 d$, then $c= \pm 2$ and $d= \pm 1$ (since $a d-b c=1$ ). Therefore $\varphi(z)=\sigma(z)+2 m$, where $m$ is an integer. Since $\sigma(Q) \subset \bar{D}\left(\frac{1}{2} ; \frac{1}{2}\right),(3)$ holds.

If $c \neq 0$ and $c \neq 2 d$, we claim that $|c z+d|>1$ for all $z \in Q$. Otherwise, the disc $\bar{D}(-d / c ; 1 /|c|)$ would intersect $Q$. The description of $Q$ shows that if $\alpha \neq-\frac{1}{2}$ is a real number and if $\bar{D}(\alpha ; r)$ intersects $Q$, then at least one of the points $-1,0,1$ lies in $D(\alpha ; r)$. Hence $|c w+d|<1$, for $w=-1$ or 0 or 1 . But for these $w, c w+d$ is an odd integer whose absolute value cannot be less than 1. So $|c z+d|>1$, and it now follows from (2) that $\operatorname{Im} \varphi(z)<\operatorname{Im} z$ for
every $z \in Q$. If it were true for some $z \in Q$ that $\varphi(z) \in Q$, the same argument would apply to $\varphi^{-1}$ and would show that

$$
\operatorname{Im} z=\operatorname{Im} \varphi^{-1}(\varphi(z)) \leq \operatorname{Im} \varphi(z)
$$

This contradiction shows that (3) holds.

Hence $\left(a^{\prime}\right)$ is proved.

To prove (b), let $\Sigma$ be the union of the sets $\varphi(Q)$, for $\varphi \in \Gamma$. It is clear that $\Sigma \subset \Pi^{+}$. Also, $\Sigma$ contains the sets $\tau^{n}(Q)$, for $n=0, \pm 1, \pm 2, \ldots$, where $\tau^{n}(z)=z+2 n$. Since $\sigma$ maps the circle $|2 z+1|=1$ onto the circle $|2 z-1|=1$, we see that $\Sigma$ contains every $z \in \Pi^{+}$which satisfies all inequalities

$$
|2 z-(2 m+1)| \geq 1 \quad(m=0, \pm 1, \pm 2, \ldots)
$$

Fix $w \in \Pi^{+}$. Since $\operatorname{Im} w>0$, there are only finitely many pairs of integers $c$ and $d$ such that $|c w+d|$ lies below any given bound, and we can choose $\varphi_{0} \in \Gamma$ so that $|c w+d|$ is minimized. By (2), this means that

$$
\operatorname{Im} \varphi(w) \leq \operatorname{Im} \varphi_{0}(w) \quad(\varphi \in \Gamma)
$$

Put $z=\varphi_{0}(w)$. Then (6) becomes

$$
\operatorname{Im} \varphi(z) \leq \operatorname{Im} z \quad(\varphi \in \Gamma)
$$

Apply (7) to $\varphi=\sigma \tau^{-n}$ and to $\varphi=\sigma^{-1} \tau^{-n}$. Since

$$
\left(\sigma \tau^{-n}\right)(z)=\frac{z-2 n}{2 z-4 n+1}, \quad\left(\sigma^{-1} \tau^{-n}\right)(z)=\frac{z-2 n}{-2 z+4 n+1}
$$

it follows from (2) and (7) that

$$
|2 z-4 n+1| \geq 1, \quad|2 z-4 n-1| \geq 1 \quad(n=0, \pm 1, \pm 2, \ldots)
$$

Thus $z$ satisfies (5), hence $z \in \Sigma$; and since $w=\varphi_{0}^{-1}(z)$ and $\varphi_{0}^{-1} \in \Gamma$, we have $w \in \Sigma$.

This completes the proof.

The following theorem summarizes some of the properties of the modular function $\lambda$ which was mentioned in Sec. 16.18 and which will be used in Theorem 16.22.

16.20 Theorem If $\Gamma$ and $Q$ are as described in Sec. 16.18, there exists a function $\lambda \in H\left(\Pi^{+}\right)$such that

(a) $\lambda \circ \varphi=\lambda$ for every $\varphi \in \Gamma$.

(b) $\lambda$ is one-to-one on $Q$.

(c) The range $\Omega$ of $\lambda$ [which is the same as $\lambda(Q)$, by (a)], is the region consisting of all complex numbers different from 0 and 1.

(d) $\lambda$ has the real axis as its natural boundary.

Proof Let $Q_{0}$ be the right half of $Q$. More precisely, $Q_{0}$ consists of all $z \in \Pi^{+}$such that

$$
0<\operatorname{Re} z<1, \quad|2 z-1|>1
$$

By Theorem 14.19 (and Remarks 14.20) there is a continuous function $h$ on $\bar{Q}_{0}$ which is one-to-one on $\bar{Q}_{0}$ and holomorphic in $Q_{0}$, such that $h\left(Q_{0}\right)=\Pi^{+}$, $h(0)=0, h(1)=1$, and $h(\infty)=\infty$. The reflection principle (Theorem 11.14) shows that the formula

$$
h(-x+i y)=\overline{h(x+i y)}
$$

extends $h$ to a continuous function on the closure $\bar{Q}$ of $Q$ which is a conformal mapping of the interior of $Q$ onto the complex plane minus the nonnegative real axis. We also see that $h$ is one-to-one on $Q$, that $h(Q)$ is the region $\Omega$ described in $(c)$, that

$$
h(-1+i y)=h(1+i y)=h(\tau(-1+i y)) \quad(0<y<\infty)
$$

and that

$$
h\left(-\frac{1}{2}+\frac{1}{2} e^{i \theta}\right)=h\left(\frac{1}{2}+\frac{1}{2} e^{i(\pi-\theta)}\right)=h\left(\sigma\left(-\frac{1}{2}+\frac{1}{2} e^{i \theta}\right)\right) \quad(0<\theta<\pi)
$$

Since $h$ is real on the boundary of $Q$, (3) and (4) follow from (2) and the definitions of $\sigma$ and $\tau$.

We now define the function $\lambda$ :

$$
\lambda(z)=h\left(\varphi^{-1}(z)\right) \quad(z \in \varphi(Q), \varphi \in \Gamma)
$$

By Theorem 16.19, each $z \in \Pi^{+}$lies in $\varphi(Q)$ for one and only one $\varphi \in \Gamma$. Thus (5) defines $\lambda(z)$ for $z \in \Pi^{+}$, and we see immediately that $\lambda$ has properties $(a)$ to $(c)$ and that $\lambda$ is holomorphic in the interior of each of the sets $\varphi(Q)$.

It follows from (3) and (4) that $\lambda$ is continuous on

$$
Q \cup \tau^{-1}(Q) \cup \sigma^{-1}(Q)
$$

hence on an open set $V$ which contains $Q$. Theorem 16.8 now shows that $\lambda$ is holomorphic in $V$. Since $\Pi^{+}$is covered by the union of the sets $\varphi(V), \varphi \in \Gamma$, and since $\lambda \circ \varphi=\lambda$, we conclude that $\lambda \in H\left(\Pi^{+}\right)$.

Finally, the set of all numbers $\varphi(0)=b / d$ is dense on the real axis. If $\lambda$ could be analytically continued to a region which properly contains $\Pi^{+}$, the zeros of $\lambda$ would have a limit point in this region, which is impossible since $\lambda$ is not constant.

## The Picard Theorem

16.21 The so-called "little Picard theorem" asserts that every nonconstant entire function attains each value, with one possible exception. This is the theorem which is proved below. There is a stronger version: Every entire function which is not a polynomial attains each value infinitely many times, again with one possible exception. That one exception can occur is shown by $f(z)=e^{z}$, which omits the
value 0 . The latter theorem is actually true in a local situation: If $f$ has an isolated singularity at a point $z_{0}$ and if $f$ omits two values in some neighborhood of $z_{0}$, then $z_{0}$ is a removable singularity or a pole of $f$. This so-called "big Picard theorem" is a remarkable strengthening of the theorem of Weierstrass (Theorem 10.21) which merely asserts that the image of every neighborhood of $z_{0}$ is dense in the plane if $f$ has an essential singularity at $z_{0}$. We shall not prove it here.

16.22 Theorem If $f$ is an entire function and if there are two distinct complex numbers $\alpha$ and $\beta$ which are not in the range of $f$, then $f$ is constant.

ProOF Without loss of generality we assume that $\alpha=0$ and $\beta=1$; if not, replace $f$ by $(f-\alpha) /(\beta-\alpha)$. Then $f$ maps the plane into the region $\Omega$ described in Theorem 16.20.

With each disc $D_{1} \subset \Omega$ there is associated a region $V_{1} \subset \Pi^{+}$(in fact, there are infinitely many such $V_{1}$, one for each $\varphi \in \Gamma$ ) such that $\lambda$ is one-toone on $V_{1}$ and $\lambda\left(V_{1}\right)=D_{1}$; each such $V_{1}$ intersects at most two of the domains $\varphi(Q)$. Corresponding to each choice of $V_{1}$ there is a function $\psi_{1} \in$ $H\left(D_{1}\right)$ such that $\psi_{1}(\lambda(z))=z$ for all $z \in V_{1}$.

If $D_{2}$ is another disc in $\Omega$ and if $D_{1} \cap D_{2} \neq \varnothing$, we can choose a corresponding $V_{2}$ so that $V_{1} \cap V_{2} \neq \varnothing$. The function elements $\left(\psi_{1}, D_{1}\right)$ and $\left(\psi_{2}, D_{2}\right)$ will then be direct analytic continuations of each other. Note that $\psi_{i}\left(D_{i}\right) \subset \Pi^{+}$.

Since the range of $f$ is in $\Omega$, there is a disc $A_{0}$ with center at 0 so that $f\left(A_{0}\right)$ lies in a disc $D_{0}$ in $\Omega$. Choose $\psi_{0} \in H\left(D_{0}\right)$, as above, put $g(z)=\psi_{0}(f(z))$ for $z \in A_{0}$, and let $\gamma$ be any curve in the plane which starts at 0 . The range of $f \circ \gamma$ is a compact subset of $\Omega$. Hence $\gamma$ can be covered by a chain of discs, $A_{0}, \ldots, A_{n}$, so that each $f\left(A_{i}\right)$ lies in a disc $D_{i}$ in $\Omega$, and we can choose $\psi_{i} \in H\left(D_{i}\right)$ so that $\left(\psi_{i}, D_{i}\right)$ is a direct analytic continuation of $\left(\psi_{i-1}, D_{i-1}\right)$, for $i=1, \ldots n$. This gives an analytic continuation of the function element $\left(g, A_{0}\right)$ along the chain $\left\{A_{0}, \ldots, A_{n}\right\}$; note that $\psi_{n} \circ f$ has positive imaginary part.

Since $\left(g, A_{0}\right)$ can be analytically continued along every curve in the plane and since the plane is simply connected, the monodromy theorem implies that $g$ extends to an entire function. Also, the range of $g$ is in $\Pi^{+}$, hence $(g-i) /(g+i)$ is bounded, hence constant, by Liouville's theorem. This shows that $g$ is constant, and since $\psi_{0}$ was one-to-one on $f\left(A_{0}\right)$ and $A_{0}$ was a nonempty open set, we conclude that $f$ is constant.

## Exercises

1 Suppose $f(z)=\Sigma a_{n} z^{n}, a_{n} \geq 0$, and the radius of convergence of the series is 1 . Prove that $f$ has a singularity at $z=1$. Hint: Expand $f$ in powers of $z-\frac{1}{2}$. If 1 were a regular point of $f$, the new series would converge at some $x>1$. What would this imply about the original series?

2 Suppose $(f, D)$ and $(g, D)$ are function elements, $P$ is a polynomial in two variables, and $P(f, g)=0$ in $D$. Suppose $f$ and $g$ can be analytically continued along a curve $\gamma$, to $f_{1}$ and $g_{1}$. Prove that
$P\left(f_{1}, g_{1}\right)=0$. Extend this to more than two functions. Is there such a theorem for some class of functions $P$ which is larger than the polynomials?

3 Suppose $\Omega$ is a simply connected region, and $u$ is a real harmonic function in $\Omega$. Prove that there exists an $f \in H(\Omega)$ such that $u=\operatorname{Re} f$. Show that this fails in every region which is not simply connected.

4 Suppose $X$ is the closed unit square in the plane, $f$ is a continuous complex function on $X$, and $f$ has no zero in $X$. Prove that there is a continuous function $g$ on $X$ such that $f=e^{g}$. For what class of spaces $X$ (other than the above square) is this also true?

5 Prove that the transformations $z \rightarrow z+1$ and $z \rightarrow-1 / z$ generate the full modular group $G$. Let $R$ consist of all $z=x+i y$ such that $|x|<\frac{1}{2}, y>0$, and $|z|>1$, plus those limit points which have $x \leq 0$. Prove that $R$ is a fundamental domain of $G$.

6 Prove that $G$ is also generated by the transformations $\varphi$ and $\psi$, where

$$
\varphi(z)=-\frac{1}{z}, \quad \psi(z)=\frac{z-1}{z}
$$

Show that $\varphi$ has period $2, \psi$ has period 3 .

7 Find the relation between composition of linear fractional transformations and matrix multiplication. Try to use this to construct an algebraic proof of Theorem 16.19(c) or of the first part of Exercise 5.

8 Let $E$ be a compact set on the real axis, of positive Lebesgue measure, let $\Omega$ be the complement of $E$, relative to the plane, and define

$$
f(z)=\int_{E} \frac{d t}{t-z} \quad(z \in \Omega)
$$

Answer the following questions:

(a) Is $f$ constant?

(b) Can $f$ be extended to an entire function?

(c) Does $\lim z f(z)$ exist as $z \rightarrow \infty$ ? If so, what is it?

(d) Does $f$ have a holomorphic square root in $\Omega$ ?

$(e)$ Is the real part of $f$ bounded in $\Omega$ ?

$(f)$ Is the imaginary part of $f$ bounded in $\Omega$ ?

[If " yes" in $(e)$ or $(f)$, give a bound.]

(g) What is $\int_{\gamma} f(z) d z$ if $\gamma$ is a positively oriented circle which has $E$ in its interior?

(h) Does there exist a bounded holomorphic function $\varphi$ in $\Omega$ which is not constant?

9 Check your answers in Exercise 8 against the special case

$$
\boldsymbol{E}=[-1,1] .
$$

10 Call a compact set $E$ in the plane removable if there are no nonconstant bounded holomorphic functions in the complement of $E$.

(a) Prove that every countable compact set is removable.

(b) If $E$ is a compact subset of the real axis, and $m(E)=0$, prove that $E$ is removable. Hint: $E$ can be surrounded by curves of arbitrarily small total length. Apply Cauchy's formula, as in Exercise 25, Chap 10.

(c) Suppose $E$ is removable, $\Omega$ is a region, $E \subset \Omega, f \in H(\Omega-E)$, and $f$ is bounded. Prove that $f$ can be extended to a holomorphic function in $\Omega$. axis.

(d) Formulate and prove an analogue of part $(b)$ for sets $E$ which are not necessarily on the real

(e) Prove that no compact connected subset of the plane (with more than one point) is removable.

11 For each positive number $\alpha$, let $\Gamma_{\alpha}$ be the path with parameter interval $(-\infty, \infty)$ defined by

$$
\Gamma_{\alpha}(t)= \begin{cases}-t-\pi i & (-\infty<t \leq-\alpha) \\ \alpha+\frac{\pi i t}{\alpha} & (-\alpha \leq t \leq \alpha) \\ t+\pi i & (\alpha \leq t<\infty)\end{cases}
$$

Let $\Omega_{\alpha}$ be the component of the complement of $\Gamma_{\alpha}^{*}$ which contains the origin, and define

$$
f_{\alpha}(z)=\frac{1}{2 \pi i} \int_{\Gamma_{\alpha}} \frac{\exp \left(e^{w}\right)}{w-z} d w \quad\left(z \in \Omega_{\alpha}\right)
$$

Prove that $f_{\beta}$ is an analytic continuation of $f_{\alpha}$ if $\alpha<\beta$. Prove that therefore there is an entire function $f$ whose restriction to $\Omega_{\alpha}$ is $f_{\alpha}$. Prove that

$$
\lim _{r \rightarrow \infty} f\left(r e^{i \theta}\right)=0
$$

for every $e^{i \theta} \neq 1$. (Here $r$ is positive and $\theta$ is real, as usual.) Prove that $f$ is not constant. [Hint: Look at $f(r)$.] If

$$
g=f \exp (-f)
$$

prove that

$$
\lim _{r \rightarrow \infty} g\left(r e^{i \theta}\right)=0
$$

for every $e^{i \theta}$.

Show that there exists an entire function $h$ such that

$$
\lim _{n \rightarrow \infty} h(n z)= \begin{cases}1 & \text { if } z=0 \\ 0 & \text { if } z \neq 0\end{cases}
$$

12 Suppose

$$
f(z)=\sum_{k=1}^{\infty}\left(\frac{z-z^{2}}{2}\right)^{3^{k}}=\sum_{n=1}^{\infty} a_{n} z^{n}
$$

Find the regions in which the two series converge. Show that this illustrates Theorem 16.5. Find the singular point of $f$ which is nearest to the origin.

13 Let $\Omega=\left\{z: \frac{1}{2}<|z|<2\right\}$. For $n=1,2,3, \ldots$ let $X_{n}$ be the set of all $f \in H(\Omega)$ that are $n$th derivatives of some $g \in H(\Omega)$. [In other words, $X_{n}$ is the range of the differential operator $D^{n}$ with domain $H(\Omega)$.]

(a) Show that $f \in X_{1}$ if and only if $\int_{\gamma} f(z) d z=0$, where $\gamma$ is the positively oriented unit circle.

(b) Show that $f \in X_{n}$ for every $n$ if and only if $f$ extends to a holomorphic function in $D(0 ; 2)$.

14 Suppose $\Omega$ is a region, $p \in \Omega, R<\infty$. Let $\mathscr{F}$ be the class of all $f \in H(\Omega)$ such that $|f(p)| \leq R$ and $f(\Omega)$ contains neither 0 nor 1 . Prove that $\mathscr{F}$ is a normal family.

15 Show that Theorem 16.2 leads to a very simple proof of the special case of the monodromy theorem (16.15) in which $\Omega$ and $D$ are concentric discs. Combine this special case with the Riemann mapping theorem to prove Theorem 16.15 in the generality in which it is stated.

## CHAPTER <br> SEVENTEEN

## $H^{p}$-SPACES

This chapter is devoted to the study of certain subspaces of $H(U)$ which are defined by certain growth conditions; in fact, they are all contained in the class $N$ defined in Chap. 15. These so-called $H^{p}$-spaces (named for G. H. Hardy) have a large number of interesting properties concerning factorizations, boundary values, and Cauchy-type representations in terms of measures on the boundary of $U$. We shall merely give some of the highlights, such as the theorem of F. and M. Riesz on measures $\mu$ whose Fourier coefficients $\hat{\mu}(n)$ are 0 for all $n<0$, Beurling's classification of the invariant subspaces of $H^{2}$, and M. Riesz's theorem on conjugate functions.

A convenient approach to the subject is via subharmonic functions, and we begin with a brief outline of their properties.

## Subharmonic Functions

17.1 Definition A function $u$ defined in an open set $\Omega$ in the plane is said to be subharmonic if it has the following four properties.

(a) $-\infty \leq u(z)<\infty$ for all $z \in \Omega$.

(b) $u$ is upper semicontinuous in $\Omega$.

(c) Whenever $\bar{D}(a ; r) \subset \Omega$, then

$$
u(a) \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi} u\left(a+r e^{i \theta}\right) d \theta
$$

(d) None of the integrals in (c) is $-\infty$.

Note that the integrals in $(c)$ always exist and are not $+\infty$, since $(a)$ and $(b)$ imply that $u$ is bounded above on every compact $K \subset \Omega$. [Proof: If $K_{n}$ is the set of all $z \in K$ at which $u(z) \geq n$, then $K \supset K_{1} \supset K_{2} \cdots$, so either $K_{n}=\varnothing$ for some $n$, or $\cap K_{n} \neq \varnothing$, in which case $u(z)=\infty$ for some $z \in K$.] Hence $(d)$ says that the integrands in $(c)$ belong to $L^{1}(T)$.

Every real harmonic function is obviously subharmonic.

17.2 Theorem If $u$ is subharmonic in $\Omega$, and if $\varphi$ is a monotonically increasing convex function on $R^{1}$, then $\varphi \circ u$ is subharmonic.

[To have $\varphi \circ u$ defined at all points of $\Omega$, we put $\varphi(-\infty)=\lim \varphi(x)$ as $x \rightarrow-\infty$.

ProOF First, $\varphi \circ u$ is upper semicontinuous, since $\varphi$ is increasing and continuous. Next, if $\bar{D}(a ; r) \subset \Omega$, we have

$$
\varphi(u(a)) \leq \varphi\left(\frac{1}{2 \pi} \int_{-\pi}^{\pi} u\left(a+r e^{i \theta}\right) d \theta\right) \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi} \varphi\left(u\left(a+r e^{i \theta}\right)\right) d \theta .
$$

The first of these inequalities holds since $\varphi$ is increasing and $u$ is subharmonic; the second follows from the convexity of $\varphi$, by Theorem 3.3.

17.3 Theorem If $\Omega$ is a region, $f \in H(\Omega)$, and $f$ is not identically 0 , then $\log |f|$ is subharmonic in $\Omega$, and so are $\log ^{+}|f|$ and $|f|^{p}(0<p<\infty)$.

Proof It is understood that $\log |f(z)|=-\infty$ if $f(z)=0$. Then $\log |f|$ is upper semicontinuous in $\Omega$, and Theorem 15.19 implies that $\log |f|$ is subharmonic.

The other assertions follow if we apply Theorem 17.2 to $\log |f|$ in place of $u$, with

$$
\varphi(t)=\max (0, t) \quad \text { and } \quad \varphi(t)=e^{p t}
$$

17.4 Theorem Suppose $u$ is a continuous subharmonic function in $\Omega, K$ is a compact subset of $\Omega, h$ is a continuous real function on $K$ which is harmonic in the interior $V$ of $K$, and $u(z) \leq h(z)$ at all boundary points of $K$. Then $u(z) \leq h(z)$ for all $z \in K$.

This theorem accounts for the term "subharmonic." Continuity of $u$ is not necessary here, but we shall not need the general case and leave it as an exercise.

Proof Put $u_{1}=u-h$, and assume, to get a contradiction, that $u_{1}(z)>0$ for some $z \in V$. Since $u_{1}$ is continuous on $K, u_{1}$ attains its maximum $m$ on $K$; and since $u_{1} \leq 0$ on the boundary of $K$, the set $E=\left\{z \in K: u_{1}(z)=m\right\}$ is a nonempty compact subset of $V$. Let $z_{0}$ be a boundary point of $E$. Then for
some $r>0$ we have $\bar{D}\left(z_{0} ; r\right) \subset V$, but some subarc of the boundary of $\bar{D}\left(z_{0} ; r\right)$ lies in the complement of $E$. Hence

$$
u_{1}\left(z_{0}\right)=m>\frac{1}{2 \pi} \int_{-\pi}^{\pi} u_{1}\left(z_{0}+r e^{i \theta}\right) d \theta
$$

and this means that $u_{1}$ is not subharmonic in $V$. But if $u$ is subharmonic, so is $u-h$, by the mean value property of harmonic functions, and we have our contradiction.

17.5 Theorem Suppose $u$ is a continuous subharmonic function in $U$, and

$$
m(r)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} u\left(r e^{i \theta}\right) d \theta \quad(0 \leq r<1)
$$

If $r_{1}<r_{2}$, then $m\left(r_{1}\right) \leq m\left(r_{2}\right)$.

Proof Let $h$ be the continuous function on $\bar{D}\left(0 ; r_{2}\right)$ which coincides with $u$ on the boundary of $\bar{D}\left(0 ; r_{2}\right)$ and which is harmonic in $D\left(0 ; r_{2}\right)$. By Theorem 17.4, $u \leq h$ in $D\left(0 ; r_{2}\right)$. Hence

$$
m\left(r_{1}\right) \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi} h\left(r_{1} e^{i \theta}\right) d \theta=h(0)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} h\left(r_{2} e^{i \theta}\right) d \theta=m\left(r_{2}\right) .
$$

## The Spaces $H^{p}$ and $N$

17.6 Notation As in Secs 11.15 and 11.19, we define $f_{r}$ on $T$ by

$$
f_{r}\left(e^{i \theta}\right)=f\left(r e^{i \theta}\right) \quad(0 \leq r<1)
$$

if $f$ is any continuous function with domain $U$, and we let $\sigma$ denote Lebesgue measure on $T$, so normalized that $\sigma(T)=1$. Accordingly, $L^{p}$-norms will refer to $L^{p}(\sigma)$. In particular,

$$
\begin{gathered}
\left\|f_{r}\right\|_{p}=\left\{\int_{T}\left|f_{r}\right|^{p} d \sigma\right\}^{1 / p} \quad(0<p<\infty) \\
\left\|f_{r}\right\|_{\infty}=\sup _{\theta}\left|f\left(r e^{i \theta}\right)\right|
\end{gathered}
$$

and we also introduce

$$
\left\|f_{r}\right\|_{0}=\exp \int_{T} \log ^{+}\left|f_{r}\right| d \sigma
$$

17.7 Definition If $f \in H(U)$ and $0 \leq p \leq \infty$, we put

$$
\|f\|_{p}=\sup \left\{\left\|f_{r}\right\|_{p}: 0 \leq r<1\right\} .
$$

If $0<p \leq \infty, H^{p}$ is defined to be the class of all $f \in H(U)$ for which $\|f\|_{p}<\infty$. (Note that this coincides with our previously introduced terminology in the case $p=\infty$.)

The class $N$ consists of all $f \in H(U)$ for which $\|f\|_{0}<\infty$.

It is clear that $H^{\infty} \subset H^{p} \subset H^{s} \subset N$ if $0<s<p<\infty$.

17.8 Remarks $(a)$ When $p<\infty$, Theorems 17.3 and 17.5 show that $\left\|f_{r}\right\|_{p}$ is a nondecreasing function of $r$, for every $f \in H(U)$; when $p=\infty$, the same follows from the maximum modulus theorem. Hence

$$
\|f\|_{p}=\lim _{r \rightarrow 1}\left\|f_{r}\right\|_{p}
$$

(b) For $1 \leq p \leq \infty,\|f\|_{p}$ satisfies the triangle inequality, so that $H^{p}$ is a normed linear space. To see this, note that the Minkowski inequality gives

$$
\left\|(f+g)_{r}\right\|_{p}=\left\|f_{r}+g_{r}\right\|_{p} \leq\left\|f_{r}\right\|_{p}+\left\|g_{r}\right\|_{p}
$$

if $0<r<1$. As $r \rightarrow 1$, we obtain

$$
\|f+g\|_{p} \leq\|f\|_{p}+\|g\|_{p}
$$

(c) Actually, $H^{p}$ is a Banach space, if $1 \leq p \leq \infty$ : To prove completeness, suppose $\left\{f_{n}\right\}$ is a Cauchy sequence in $H^{p},|z| \leq r<R<1$, and apply the Cauchy formula to $f_{n}-f_{m}$, integrating around the circle of radius $R$, center 0 . This leads to the inequalities

$$
(R-r)\left|f_{n}(z)-f_{m}(z)\right| \leq\left\|\left(f_{n}-f_{m}\right)_{R}\right\|_{1} \leq\left\|\left(f_{n}-f_{m}\right)_{R}\right\|_{p} \leq\left\|f_{n}-f_{m}\right\|_{p}
$$

from which we conclude that $\left\{f_{n}\right\}$ converges uniformly on compact subsets of $U$ to a function $f \in H(U)$. Given $\epsilon>0$, there is an $m$ such that $\left\|f_{n}-f_{m}\right\|_{p}<\epsilon$ for all $n>m$, and then, for every $r<1$,

$$
\left\|\left(f-f_{m}\right)_{r}\right\|_{p}=\lim _{n \rightarrow \infty}\left\|\left(f_{n}-f_{m}\right)_{r}\right\|_{p} \leq \epsilon
$$

This gives $\left\|f-f_{m}\right\|_{p} \rightarrow 0$ as $m \rightarrow \infty$.

(d) For $p<1, H^{p}$ is still a vector space, but the triangle inequality is no longer satisfied by $\|f\|_{p}$.

We saw in Theorem 15.23 that the zeros of any $f \in N$ satisfy the Blaschke condition $\Sigma\left(1-\left|\alpha_{n}\right|\right)<\infty$. Hence the same is true in every $H^{p}$. It is interesting that the zeros of any $f \in H^{p}$ can be divided out without increasing the norm:

17.9 Theorem Suppose $f \in N, f \not \equiv 0$, and $B$ is the Blaschke product formed with the zeros of $f$. Put $g=f / B$. Then $g \in N$ and $\|g\|_{0}=\|f\|_{0}$.

Moreover, if $f \in H^{p}$, then $g \in H^{p}$ and $\|g\|_{p}=\|f\|_{p}(0<p \leq \infty)$.

Proof Note first that

$$
|g(z)| \geq|f(z)| \quad(z \in U) .
$$

In fact, strict inequality holds for every $z \in U$, unless $f$ has no zeros in $U$, in which case $B=1$ and $g=f$.

If $s$ and $t$ are nonnegative real numbers, the inequality

$$
\log ^{+}(s t) \leq \log ^{+} s+\log ^{+} t
$$

holds since the left side is 0 if $s t<1$ and is $\log s+\log t$ if $s t \geq 1$. Since $|g|=|f| /|B|$, (2) gives

$$
\log ^{+}|g| \leq \log ^{+}|f|+\log \frac{1}{|B|}
$$

By Theorem 15.24, (3) implies that $\|g\|_{0} \leq\|f\|_{0}$, and since (1) holds, we actually have $\|g\|_{0}=\|f\|_{0}$.

Now suppose $f \in H^{p}$ for some $p>0$. Let $B_{n}$ be the finite Blaschke product formed with the first $n$ zeros of $f$ (we arrange these zeros in some sequence, taking multiplicities into account). Put $g_{n}=f / B_{n}$. For each $n$, $\left|B_{n}\left(r e^{i \theta}\right)\right| \rightarrow 1$ uniformly, as $r \rightarrow 1$. Hence $\left\|g_{n}\right\|_{p}=\|f\|_{p}$. As $n \rightarrow \infty,\left|g_{n}\right|$ increases to $|g|$, so that

$$
\left\|g_{r}\right\|_{p}=\lim _{n \rightarrow \infty}\left\|\left(g_{n}\right)_{r}\right\|_{p} \quad(0<r<1)
$$

by the monotone convergence theorem. The right side of (4) is at most $\|f\|_{p}$, for all $r<1$. If we let $r \rightarrow 1$, we obtain $\|g\|_{p} \leq\|f\|_{p}$. Equality follows now from (1), as before.

17.10 Theorem Suppose $0<p<\infty, f \in H^{p}, f \not \equiv 0$, and $B$ is the Blaschke product formed with the zeros of $f$. Then there is a zero-free function $h \in H^{2}$ such that

$$
f=B \cdot h^{2 / p} \text {. }
$$

In particular, every $f \in H^{1}$ is a product

$$
f=g h
$$

in which both factors are in $H^{2}$.

Proof By Theorem 17.9, $f / B \in H^{p}$; in fact, $\|f / B\|_{p}=\|f\|_{p}$. Since $f / B$ has no zero in $U$ and $U$ is simply connected, there exists $\varphi \in H(U)$ so that $\exp (\varphi)=f / B$ (Theorem 13.11). Put $h=\exp (p \varphi / 2)$. Then $h \in H(U)$ and $|h|^{2}=|f / B|^{p}$, hence $h \in H^{2}$, and (1) holds.

In fact, $\|h\|_{2}^{2}=\|f\|_{p}^{p}$.

To obtain (2), write (1) in the form $f=(B h) \cdot h$.
spaces.

We can now easily prove some of the most important properties of the $H^{p_{-}}$

17.11 Theorem If $0<p<\infty$ and $f \in H^{p}$, then

(a) the nontangential maximal functions $N_{\alpha} f$ are in $L^{p}(T)$, for all $\alpha<1$;

(b) the nontangential limits $f^{*}\left(e^{i \theta}\right)$ exist a.e. on $T$, and $f^{*} \in L^{p}(T)$;

(c) $\lim _{r \rightarrow 1}\left\|f^{*}-f_{r}\right\|_{p}=0$, and

(d) $\left\|f^{*}\right\|_{p}=\|f\|_{p}$.

If $f \in H^{1}$ then $f$ is the Cauchy integral as well as the Poisson integral of $f^{*}$.

Proof We begin by proving $(a)$ and $(b)$ for the case $p>1$. Since holomorphic functions are harmonic, Theorem $11.30(b)$ shows that every $f \in H^{p}$ is then the Poisson integral of a function (call it $f^{*}$ ) in $L^{p}(T)$. Hence $N_{\alpha} f \in L^{p}(T)$, by Theorem $11.25(b)$, and $f^{*}\left(e^{i \theta}\right)$ is the nontangential limit of $f$ at almost every $e^{i \theta} \in T$, by Theorem 11.23.

If $0<p \leq 1$ and $f \in H^{p}$, use the factorization

$$
f=B h^{2 / p}
$$

given by Theorem 17.10 , where $B$ is a Blaschke product, $h \in H^{2}$, and $h$ has no zero in $U$. Since $|f| \leq|h|^{2 / p}$ in $U$, it follows that

$$
\left(N_{\alpha} f\right)^{p} \leq\left(N_{\alpha} h\right)^{2}
$$

so that $N_{\alpha} f \in L^{p}(T)$, because $N_{\alpha} h \in L^{2}(T)$.

Similarly, the existence of $B^{*}$ and $h^{*}$ a.e. on $T$ implies that the nontangential limits of $f$ (call them $f^{*}$ ) exist a.e. Obviously, $\left|f^{*}\right| \leq N_{\alpha} f$ wherever $f^{*}$ exists. Hence $f^{*} \in L^{p}(T)$.

This proves $(a)$ and $(b)$, for $0<p<\infty$.

Since $f_{r} \rightarrow f^{*}$ a.e. and $\left|f_{r}\right|<N_{\alpha} f$, the dominated convergence theorem gives $(c)$.

If $p \geq 1,(d)$ follows from $(c)$, by the triangle inequality. If $p<1$, use Exercise 24, Chap. 3, to deduce $(d)$ from $(c)$.

Finally, if $f \in H^{1}, r<1$, and $f_{r}(z)=f(r z)$, then $f_{r} \in H(D(0,1 / r))$, and therefore $f_{r}$ can be represented in $U$ by the Cauchy formula

$$
f_{r}(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{f_{r}\left(e^{i t}\right)}{1-e^{-i t_{z}}} d t
$$

and by the Poisson formula

$$
f_{r}(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} P\left(z, e^{i t}\right) f_{r}\left(e^{i t}\right) d t .
$$

For each $z \in U,\left|1-e^{-i t} z\right|$ and $P\left(z, e^{i t}\right)$ are bounded functions on $T$. The case $p=1$ of $(c)$ leads therefore from (3) and (4) to

and

$$
\begin{aligned}
& f(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{f^{*}\left(e^{i t}\right)}{1-e^{-i t} z} d t \\
& f(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} P\left(z, e^{i t}\right) f^{*}\left(e^{i t}\right) d t .
\end{aligned}
$$

The space $H^{2}$ has a particularly simple characterization in terms of power series coefficients:

17.12 Theorem Suppose $f \in H(U)$ and

$$
f(z)=\sum_{0}^{\infty} a_{n} z^{n}
$$

Then $f \in H^{2}$ if and only if $\sum_{0}^{\infty}\left|a_{n}\right|^{2}<\infty$.

Proof By Parseval's theorem, applied to $f_{r}$ with $r<1$,

$$
\sum_{0}^{\infty}\left|a_{n}\right|^{2}=\lim _{r \rightarrow 1} \sum_{0}^{\infty}\left|a_{n}\right|^{2} r^{2 n}=\lim _{r \rightarrow 1} \int_{T}\left|f_{r}\right|^{2} d \sigma=\|f\|_{2}^{2}
$$

## The Theorem of F. and M. Riesz

17.13 Theorem If $\mu$ is a complex Borel measure on the unit circle $T$ and

$$
\int_{T} e^{-i n t} d \mu(t)=0
$$

for $n=-1,-2,-3, \ldots$, then $\mu$ is absolutely continuous with respect to Lebesgue measure.

Proof Put $f=P[d \mu]$. Then $f$ satisfies

$$
\left\|f_{r}\right\|_{1} \leq\|\mu\| \quad(0 \leq r<1)
$$

(See Sec. 11.17.) Since, setting $z=r e^{i \theta}$,

$$
P\left(z, e^{i t}\right)=\sum_{-\infty}^{\infty} r^{|n|} e^{i n \theta} e^{-i n t}
$$

as in Sec. 11.5, the assumption (1), which amounts to saying that the Fourier coefficients $\hat{\mu}(n)$ are 0 for all $n<0$, leads to the power series

$$
f(z)=\sum_{0}^{\infty} \hat{\mu}(n) z^{n} \quad(z \in U)
$$

By (4) and (2), $f \in H^{1}$. Hence $f=P\left[f^{*}\right]$, by Theorem 17.11, where $f^{*} \in L^{1}(T)$. The uniqueness of the Poisson integral representation (Theorem 11.30) shows now that $d \mu=f^{*} d \sigma$.

The remarkable feature of this theorem is that it derives the absolute continuity of a measure from an apparently unrelated condition, namely, the vanishing of one-half of its Fourier coefficients. In recent years the theorem has been extended to various other situations.

## Factorization Theorems

We already know from Theorem 17.9 that every $f \in H^{p}$ (except $f=0$ ) can be factored into a Blaschke product and a function $g \in H^{p}$ which has no zeros in $U$. There is also a factorization of $g$ which is of a more subtle nature. It concerns, roughly speaking, the rapidity with which $g$ tends to 0 along certain radii.

17.14 Definition An inner function is a function $M \in H^{\infty}$ for which $\left|M^{*}\right|=1$ a.e. on $T$. (As usual, $M^{*}$ denotes the radial limits of $M$.)

If $\varphi$ is a positive measurable function on $T$ such that $\log \varphi \in L^{1}(T)$, and if

$$
Q(z)=c \exp \left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{e^{i t}+z}{e^{i t}-z} \log \varphi\left(e^{i t}\right) d t\right\}
$$

for $z \in U$, then $Q$ is called an outer function. Here $c$ is a constant, $|c|=1$.

Theorem 15.24 shows that every Blaschke product is an inner function, but there are others. They can be described as follows.

17.15 Theorem Suppose $c$ is a constant, $|c|=1, B$ is a Blaschke product, $\mu$ is a finite positive Borel measure on $T$ which is singular with respect to Lebesgue measure, and

$$
M(z)=c B(z) \exp \left\{-\int_{-\pi}^{\pi} \frac{e^{i t}+z}{e^{i t}-z} d \mu(t)\right\} \quad(z \in U)
$$

Then $M$ is an inner function, and every inner function is of this form.

Proof If (1) holds and $g=M / B$, then $\log |g|$ is the Poisson integral of $-d \mu$, hence $\log |g| \leq 0$, so that $g \in H^{\infty}$, and the same is true of $M$. Also $D \mu=0$ a.e., since $\mu$ is singular (Theorem 7.13), and therefore the radial limits of
$\log |g|$ are 0 a.e. (Theorem 11.22). Since $\left|B^{*}\right|=1$ a.e., we see that $M$ is an inner function.

Conversely, let $B$ be the Blaschke product formed with the zeros of a given inner function $M$ and put $g=M / B$. Then $\log |g|$ is harmonic in $U$. Theorems 15.24 and 17.9 show that $|g| \leq 1$ in $U$ and that $\left|g^{*}\right|=1$ a.e. on $T$. Thus $\log |g| \leq 0$. We conclude from Theorem 11.30 that $\log |g|$ is the Poisson integral of $-d \mu$, for some positive measure $\mu$ on $T$. Since $\log \left|g^{*}\right|=0$ a.e. on $T$, we have $D \mu=0$ a.e. on $T$, so $\mu$ is singular. Finally, $\log |g|$ is the real part of

$$
h(z)=-\int_{-\pi}^{\pi} \frac{e^{i t}+z}{e^{i t}-z} d \mu(t)
$$

and this implies that $g=c \exp (h)$ for some constant $c$ with $|c|=1$. Thus $M$ is of the form (1).

This completes the proof.

The simplest example of an inner function which is not a Blaschke product is the following: Take $c=1$ and $B=1$, and let $\mu$ be the unit mass at $t=0$. Then

$$
M(z)=\exp \left\{\frac{z+1}{z-1}\right\}
$$

which tends to 0 very rapidly along the radius which ends at $z=1$.

17.16 Theorem Suppose $Q$ is the outer function related to $\varphi$ as in Definition 17.14. Then

(a) $\log |Q|$ is the Poisson integral of $\log \varphi$.

(b) $\lim _{r \rightarrow 1}\left|Q\left(r e^{i \theta}\right)\right|=\varphi\left(e^{i \theta}\right)$ a.e. on $T$.

(c) $Q \in H^{p}$ if and only if $\varphi \in L^{p}(T)$. In this case, $\|Q\|_{p}=\|\varphi\|_{p}$.

ProOF (a) is clear by inspection and $(a)$ implies that the radial limits of $\log |Q|$ are equal to $\log \varphi$ a.e. on $T$, which proves $(b)$. If $Q \in H^{p}$, Fatou's lemma implies that $\left\|Q^{*}\right\|_{p} \leq\|Q\|_{p}$, so $\|\varphi\|_{p} \leq\|Q\|_{p}$, by $(b)$. Conversely, if $\varphi \in L^{p}(T)$, then

$$
\begin{aligned}
\left|Q\left(r e^{i \theta}\right)\right|^{p} & =\exp \left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi} P_{r}(\theta-t) \log \varphi^{p}\left(e^{i t}\right) d t\right\} \\
& \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi} P_{r}(\theta-t) \varphi^{p}\left(e^{i t}\right) d t,
\end{aligned}
$$

by the inequality between the geometric and arithmetic means (Theorem 3.3), and if we integrate the last inequality with respect to $\theta$ we find that $\|Q\|_{p} \leq$ $\|\varphi\|_{p}$ if $p<\infty$. The case $p=\infty$ is trivial.

17.17 Theorem Suppose $0<p \leq \infty, f \in H^{p}$, and $f$ is not identically 0 . Then $\log \left|f^{*}\right| \in L^{1}(T)$, the outer function

$$
Q_{f}(z)=\exp \left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{e^{i t}+z}{e^{i t}-z} \log \left|f^{*}\left(e^{i t}\right)\right| d t\right\}
$$

is in $H^{p}$, and there is an inner function $M_{f}$ such that

$$
f=M_{f} Q_{f}
$$

Furthermore,

$$
\log |f(0)| \leq \frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f^{*}\left(e^{i t}\right)\right| d t
$$

Equality holds in (3) if and only if $M_{f}$ is constant.

The functions $M_{f}$ and $Q_{f}$ are called the inner and outer factors of $f$, respectively; $Q_{f}$ depends only on the boundary values of $|f|$.

Proof We assume first that $f \in H^{1}$. If $B$ is the Blaschke product formed with the zeros of $f$ and if $g=f / B$, Theorem 17.9 shows that $g \in H^{1}$; and since $\left|g^{*}\right|=\left|f^{*}\right|$ a.e. on $T$, it suffices to prove the theorem with $g$ in place of $f$.

So let us assume that $f$ has no zero in $U$ and that $f(0)=1$. Then $\log |f|$ is harmonic in $U, \log |f(0)|=0$, and since $\log =\log ^{+}-\log ^{-}$, the mean value property of harmonic functions implies that

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log ^{-}\left|f\left(r e^{i \theta}\right)\right| d \theta=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log ^{+} \mid f\left(r e^{i \theta}\right) d \theta \leq\|f\|_{0} \leq\|f\|_{1}
$$

for $0<r<1$. It now follows from Fatou's lemma that both $\log ^{+}\left|f^{*}\right|$ and $\log ^{-}\left|f^{*}\right|$ are in $L^{1}(T)$, hence so is $\log \left|f^{*}\right|$.

This shows that the definition (1) makes sense. By Theorem 17.16, $Q_{f} \in$ $H^{1}$. Also, $\left|Q_{f}^{*}\right|=\left|f^{*}\right| \neq 0$ a.e., since $\log \left|f^{*}\right| \in L^{1}(T)$. If we can prove that

$$
|f(z)| \leq\left|Q_{f}(z)\right| \quad(z \in U)
$$

then $f / Q_{f}$ will be an inner function, and we obtain the factorization (2).

Since $\log \left|Q_{f}\right|$ is the Poisson integral of $\log \left|f^{*}\right|,(5)$ is equivalent to the inequality

$$
\log |f| \leq P\left[\log \left|f^{*}\right|\right]
$$

which we shall now prove. Our notation is as in Chap. 11: $P[h]$ is the Poisson integral of the function $h \in L^{1}(T)$.

For $|z| \leq 1$ and $0<R<1$, put $f_{R}(z)=f(R z)$. Fix $z \in U$. Then

$$
\log \left|f_{R}(z)\right|=P\left[\log ^{+}\left|f_{R}\right|\right](z)-P\left[\log ^{-}\left|f_{R}\right|\right](z)
$$

Since $\left|\log ^{+} u-\log ^{+} v\right| \leq|u-v|$ for all real numbers $u$ and $v$, and since $\left\|f_{R}-f^{*}\right\|_{1} \rightarrow 0$ as $R \rightarrow 1$ (Theorem 17.11), the the first Poisson integral in (7) converges to $P\left[\log ^{+}\left|f^{*}\right|\right]$, as $R \rightarrow 1$. Hence Fatou's lemma gives

$$
P\left[\log ^{-}\left|f^{*}\right|\right] \leq \liminf _{R \rightarrow 1} P\left[\log ^{-}\left|f_{R}\right|\right]=P\left[\log ^{+}\left|f^{*}\right|\right]-\log |f|
$$

which is the same as (6).

We have now established the factorization (2). If we put $z=0$ in (5) we obtain (3); equality holds in (3) if and only if $|f(0)|=\left|Q_{f}(0)\right|$, i.e., if and only if $\left|M_{f}(0)\right|=1$; and since $\left\|M_{f}\right\|_{\infty}=1$, this happens only when $M_{f}$ is a constant.

This completes the proof for the case $p=1$.

If $1<p \leq \infty$, then $H^{p} \subset H^{1}$, hence all that remains to be proved is that $Q_{f} \in H^{p}$. But if $f \in H^{p}$, then $\left|f^{*}\right| \in L^{p}(T)$, by Fatou's lemma; hence $Q_{f} \in H^{p}$, by Theorem $17.16(c)$.

Theorem 17.10 reduces the case $p<1$ to the case $p=2$.

The fact that $\log \left|f^{*}\right| \in L^{1}(T)$ has a consequence which we have already used in the proof but which is important enough to be stated separately:

17.18 Theorem If $0<p \leq \infty, f \in H^{p}$, and $f$ is not identically 0 , then at almost all points of $T$ we have $f^{*}\left(e^{i \theta}\right) \neq 0$.

Proof If $f^{*}=0$ then $\log \left|f^{*}\right|=-\infty$, and if this happens on a set of positive measure, then

$$
\int_{-\pi}^{\pi} \log \left|f^{*}\left(e^{i t}\right)\right| d t=-\infty
$$

Observe that Theorem 17.18 imposes a quantitative restriction on the location of the zeros of the radial limits of an $f \in H^{p}$. Inside $U$ the zeros are also quantitatively restricted, by the Blaschke condition.

As usual, we can rephrase the above result about zeros as a uniqueness theorem:

If $f \in H^{p}, g \in H^{p}$, and $f^{*}\left(e^{i \theta}\right)=g^{*}\left(e^{i \theta}\right)$ on some subset of $T$ whose Lebesgue measure is positive, then $f(z)=g(z)$ for all $z \in U$.

17.19 Let us take a quick look at the class $N$, with the purpose of determining how much of Theorems 17.17 and 17.18 is true here. If $f \in N$ and $f \not \equiv 0$, we can divide by a Blaschke product and get a quotient $g$ which has no zero in $U$ and which is in $N$ (Theorem 17.9). Then $\log |g|$ is harmonic, and since

$$
|\log | g||=2 \log ^{+}|g|-\log |g|
$$

and

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|g\left(r e^{i \theta}\right)\right| d \theta=\log |g(0)|
$$

we see that $\log |g|$ satisfies the hypotheses of Theorem 11.30 and is therefore the Poisson integral of a real measure $\mu$. Thus

$$
f(z)=c B(z) \exp \left\{\int_{T} \frac{e^{i t}+z}{e^{i t}-z} d \mu(t)\right\}
$$

where $c$ is a constant, $|c|=1$, and $B$ is a Blaschke product.

Observe how the assumption that the integrals of $\log ^{+}|g|$ are bounded (which is a quantitative formulation of the statement that $|g|$ does not get too close to $\infty$ ) implies the boundedness of the integrals of $\log ^{-}|g|$ (which says that $|g|$ does not get too close to 0 at too many places).

If $\mu$ is a negative measure, the exponential factor in (3) is in $H^{\infty}$. Apply the Jordan decomposition to $\mu$. This shows:

To every $f \in N$ there correspond two functions $b_{1}$ and $b_{2} \in H^{\infty}$ such that $b_{2}$ has no zero in $U$ and $f=b_{1} / b_{2}$.

Since $b_{2}^{*} \neq 0$ a.e., it follows that $f$ has finite radial limits a.e. Also, $f^{*} \neq 0$ a.e.

Is $\log \left|f^{*}\right| \in L^{1}(T)$ ? Yes, and the proof is identical to the one given in Theorem 17.17.

However, the inequality (3) of Theorem 17.17 need no longer hold. For example, if

$$
f(z)=\exp \left\{\frac{1+z}{1-z}\right\}
$$

then $\|f\|_{0}=e,\left|f^{*}\right|=1$ a.e., and

$$
\log |f(0)|=1>0=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f^{*}\left(e^{i t}\right)\right| d t
$$

## The Shift Operator

17.20 Invariant Subspaces Consider a bounded linear operator $S$ on a Banach space $X$; that is to say, $S$ is a bounded linear transformation of $X$ into $X$. If a closed subspace $Y$ of $X$ has the property that $S(Y) \subset Y$, we call $Y$ an $S$-invariant subspace. Thus the $S$-invariant subspaces of $X$ are exactly those which are mapped into themselves by $S$.

The knowledge of the invariant subspaces of an operator $S$ helps us to visualize its action. (This is a very general-and hence rather vague-principle: In studying any transformation of any kind, it helps to know what the transformation leaves fixed.) For instance, if $S$ is a linear operator on an $n$-dimensional vector space $X$ and if $S$ has $n$ linearly independent characteristic vectors $x_{1}, \ldots$,
$x_{n}$, the one-dimensional spaces spanned by any of these $x_{i}$ are $S$-invariant, and we obtain a very simple description of $S$ if we take $\left\{x_{1}, \ldots, x_{n}\right\}$ as a basis of $X$.

We shall describe the invariant subspaces of the so-called "shift operator" $S$ on $\ell^{2}$. Here $\ell^{2}$ is the space of all complex sequences

$$
x=\left\{\xi_{0}, \xi_{1}, \xi_{2}, \xi_{3}, \ldots\right\}
$$

for which

$$
\|x\|=\left\{\sum_{n=0}^{\infty}\left|\xi_{n}\right|^{2}\right\}^{1 / 2}<\infty
$$

and $S$ takes the element $x \in \ell^{2}$ given by (1) to

$$
S x=\left\{0, \xi_{0}, \xi_{1}, \xi_{2}, \ldots\right\}
$$

It is clear that $S$ is a bounded linear operator on $\ell^{2}$ and that $\|S\|=1$.

A few $S$-invariant subspaces are immediately apparent: If $Y_{k}$ is the set of all $x \in \ell^{2}$ whose first $k$ coordinates are 0 , then $Y_{k}$ is $S$-invariant.

To find others we make use of a Hilbert space isomorphism between $\ell^{2}$ and $H^{2}$ which converts the shift operator $S$ to a multiplication operator on $H^{2}$. The point is that this multiplication operator is easier to analyze (because of the richer structure of $H^{2}$ as a space of holomorphic functions) than is the case in the original setting of the sequence space $\ell^{2}$.

We associate with each $x \in \ell^{2}$, given by (1), the function

$$
f(z)=\sum_{n=0}^{\infty} \xi_{n} z^{n} \quad(z \in U)
$$

By Theorem 17.12, this defines a linear one-to-one mapping of $\ell^{2}$ onto $H^{2}$. If

$$
y=\left\{\eta_{n}\right\}, \quad g(z)=\sum_{n=0}^{\infty} \eta_{n} z^{n}
$$

and if the inner product in $H^{2}$ is defined by

$$
(f, g)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f^{*}\left(e^{i \theta}\right) \overline{g^{*}\left(e^{i \theta}\right)} d \theta
$$

the Parseval theorem shows that $(f, g)=(x, y)$. Thus we have a Hilbert space isomorphism of $\ell^{2}$ onto $H^{2}$, and the shift operator $S$ has turned into a multiplication operator (which we still denote by $S$ ) on $H^{2}$ :

$$
(S f)(z)=z f(z) \quad\left(f \in H^{2}, z \in U\right)
$$

The previously mentioned invariant subspaces $Y_{k}$ are now seen to consist of all $f \in H^{2}$ which have a zero of order at least $k$ at the origin. This gives a clue: For any finite set $\left\{\alpha_{1}, \ldots, \alpha_{k}\right\} \subset U$, the space $Y$ of all $f \in H^{2}$ such that $f\left(\alpha_{1}\right)=$ $\cdots=f\left(\alpha_{k}\right)=0$ is $S$-invariant. If $B$ is the finite Blaschke product with zeros at $\alpha_{1}$, $\ldots, \alpha_{k}$, then $f \in Y$ if and only if $f / B \in H^{2}$. Thus $Y=B H^{2}$.

This suggests that infinite Blaschke products may also give rise to $S$-invariant subspaces and, more generally, that Blaschke products might be replaced by arbitrary inner functions $\varphi$. It is not hard to see that each $\varphi H^{2}$ is a closed $S$-invariant subspace of $H^{2}$, but that every closed $S$-invariant subspace of $H^{2}$ is of this form is a deeper result.

### 17.21 Beurling's Theorem

(a) For each inner function $\varphi$ the space

$$
\varphi H^{2}=\left\{\varphi f: f \in H^{2}\right\}
$$

is a closed S-invariant subspace of $H^{2}$.

(b) If $\varphi_{1}$ and $\varphi_{2}$ are inner functions and if $\varphi_{1} H^{2}=\varphi_{2} H^{2}$, then $\varphi_{1} / \varphi_{2}$ is constant.

(c) Every closed S-invariant subspace $Y$ of $H^{2}$, other than $\{0\}$, contains an inner function $\varphi$ such that $Y=\varphi H^{2}$.

Proof $H^{2}$ is a Hilbert space, relative to the norm

$$
\|f\|_{2}=\left\{\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|f^{*}\left(e^{i \theta}\right)\right|^{2} d \theta\right\}^{1 / 2}
$$

If $\varphi$ is an inner function, then $\left|\varphi^{*}\right|=1$ a.e. The mapping $f \rightarrow \varphi f$ is therefore an isometry of $H^{2}$ into $H^{2}$; being an isometry, its range $\varphi H^{2}$ is a closed subspace of $H^{2}$. [Proof: If $\varphi f_{n} \rightarrow g$ in $H^{2}$, then. $\left\{\varphi f_{n}\right\}$ is a Cauchy sequence, hence so is $\left\{f_{n}\right\}$, hence $f_{n} \rightarrow f \in H^{2}$, so $g=\varphi f \in \varphi H^{2}$.] The $S$-invariance of $\varphi H^{2}$ is also trivial, since $z \cdot \varphi f=\varphi \cdot z f$. Hence $(a)$ holds.

If $\varphi_{1} H^{2}=\varphi_{2} H^{2}$, then $\varphi_{1}=\varphi_{2} f$ for some $f \in H^{2}$, hence $\varphi_{1} / \varphi_{2} \in H^{2}$. Similarly, $\varphi_{2} / \varphi_{1} \in H^{2}$. Put $\varphi=\varphi_{1} / \varphi_{2}$ and $h=\varphi+(1 / \varphi)$. Then $h \in H^{2}$, and since $\left|\varphi^{*}\right|=1$ a.e. on $T, h^{*}$ is real a.e. on $T$. Since $h$ is the Poisson integral of $h^{*}$, it follows that $h$ is real in $U$, hence $h$ is constant. Then $\varphi$ must be constant, and $(b)$ is proved.

The proof of $(c)$ will use a method originated by Helson and Lowdenslager. Suppose $Y$ is a closed $S$-invariant subspace of $H^{2}$ which does not consist of 0 alone. Then there is a smallest integer $k$ such that $Y$ contains a function $f$ of the form

$$
f(z)=\sum_{n=k}^{\infty} c_{n} z^{n}, \quad c_{k}=1
$$

Then $f \notin z Y$, where we write $z Y$ for the set of all $g$ of the form $g(z)=z f(z), f \in Y$. It follows that $z Y$ is a proper closed subspace of $Y$ [closed by the argument used in the proof of $(a)$ ], so $Y$ contains a nonzero vector which is orthogonal to $z Y$ (Theorem 4.11).

So there exists a $\varphi \in Y$ such that $\|\varphi\|_{2}=1$ and $\varphi \perp z Y$. Then $\varphi \perp z^{n} \varphi$, for $n=1,2,3, \ldots$ By the definition of the inner product in $H^{2}$ [see 17.20(6)] this means that

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi}\left|\varphi^{*}\left(e^{i \theta}\right)\right|^{2} e^{-i n \theta} d \theta=0 \quad(n=1,2,3, \ldots)
$$

These equations are preserved if we replace the left sides by their complex conjugates, i.e., if we replace $n$ by $-n$. Thus all Fourier coefficients of the function $\left|\varphi^{*}\right|^{2} \in L^{1}(T)$ are 0 , except the one corresponding to $n=0$, which is 1. Since $L^{1}$-functions are determined by their Fourier coefficients (Theorem 5.15), it follows that $\left|\varphi^{*}\right|=1$ a.e. on $T$. But $\varphi \in H^{2}$, so $\varphi$ is the Poisson integral of $\varphi^{*}$, and hence $|\varphi| \leq 1$. We conclude that $\varphi$ is an inner function.

Since $\varphi \in Y$ and $Y$ is $S$-invariant, we have $\varphi z^{n} \in Y$ for all $n \geq 0$, hence $\varphi P \in Y$ for every polynomial $P$. The polynomials are dense in $H^{2}$ (the partial sums of the power series of any $f \in H^{2}$ converge to $f$ in the $H^{2}$-norm, by Parseval's theorem), and since $Y$ is closed and $|\varphi| \leq 1$, it follows that $\varphi H^{2} \subset Y$. We have to prove that this inclusion is not proper. Since $\varphi H^{2}$ is closed, it is enough to show that the assumptions $h \in Y$ and $h \perp \varphi H^{2}$ imply $h=0$.

If $h \perp \varphi H^{2}$, then $h \perp \varphi z^{n}$ for $n=0,1,2, \ldots$, or

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} h^{*}\left(e^{i \theta}\right) \overline{\varphi^{*}\left(e^{i \theta}\right)} e^{-i n \theta} d \theta=0 \quad(n=0,1,2, \ldots)
$$

If $h \in Y$, then $z^{n} h \in z Y$ if $n=1,2,3, \ldots$, and our choice of $\varphi$ shows that $z^{n} h \perp \varphi$, or

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} h^{*}\left(e^{i \theta}\right) \overline{\varphi^{*}\left(e^{i \theta}\right)} e^{-i n \theta} d \theta=0 \quad(n=-1,-2,-3, \ldots)
$$

Thus all Fourier coefficients of $h^{*} \overline{\varphi^{*}}$ are 0 , hence $h^{*} \overline{\varphi^{*}}=0$ a.e. on $T$; and since $\left|\varphi^{*}\right|=1$ a.e., we have $h^{*}=0$ a.e. Therefore $h=0$, and the proof is complete.

17.22 Remark If we combine Theorems 17.15 and 17.21 , we see that the $S$-invariant subspaces of $H^{2}$ are characterized by the following data: a sequence of complex numbers $\left\{\alpha_{n}\right\}$ (possibly finite, or even empty) such that $\left|\alpha_{n}\right|<1$ and $\Sigma\left(1-\left|\alpha_{n}\right|\right)<\infty$, and a positive Borel measure $\mu$ on $T$, singular with respect to Lebesgue measure (so $D \mu=0$ a.e.). It is easy (we leave this as an exercise) to find conditions, in terms of $\left\{\alpha_{n}\right\}$ and $\mu$, which ensure that one $S$-invariant subspace of $H^{2}$ contains another. The partially ordered set of all $S$-invariant subspaces is thus seen to have an extremely complicated structure, much more complicated than one might have expected from the simple definition of the shift operator on $\ell^{2}$.

We conclude the section with an easy consequence of Theorem 17.21 which depends on the factorization described in Theorem 17.17.

17.23 Theorem Suppose $M_{f}$ is the inner factor of a function $f \in H^{2}$, and $Y$ is the smallest closed S-invariant subspace of $H^{2}$ which contains $f$. Then

$$
Y=M_{f} H^{2} .
$$

In particular, $Y=H^{2}$ if and only if $f$ is an outer function.

Proof Let $f=M_{f} Q_{f}$ be the factorization of $f$ into its inner and outer factors. It is clear that $f \in M_{f} H^{2}$; and since $M_{f} H^{2}$ is closed and $S$-invariant, we have $Y \subset M_{f} H^{2}$.

On the other hand, Theorem 17.21 shows that there is an inner function $\varphi$ such that $Y=\varphi H^{2}$. Since $f \in Y$, there exists an $h=M_{h} Q_{h} \in H^{2}$ such that

$$
M_{f} Q_{f}=\varphi M_{h} Q_{h}
$$

Since inner functions have absolute value 1 a.e. on $T$, (2) implies that $Q_{f}=$ $Q_{h}$, hence $M_{f}=\varphi M_{h} \in Y$, and therefore $Y$ must contain the smallest $S$ invariant closed subspace which contains $M_{f}$. Thus $M_{f} H^{2} \subset Y$, and the proof is complete.

It may be of interest to summarize these results in terms of two questions to which they furnish answers.

If $f \in H^{2}$, which functions $g \in H^{2}$ can be approximated in the $H^{2}$-norm by functions of the form $f P$, where $P$ runs through the polynomials? Answer: Precisely those $g$ for which $g / M_{f} \in H^{2}$.

For which $f \in H^{2}$ is it true that the set $\{f P\}$ is dense in $H^{2}$ ? Answer: Precisely for those $f$ for which

$$
\log |f(0)|=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|f^{*}\left(e^{i t}\right)\right| d t
$$

## Conjugate Functions

17.24 Formulation of the Problem Every real harmonic function $u$ in the unit disc $U$ is the real part of one and only one $f \in H(U)$ such that $f(0)=u(0)$. If $f=u+i v$, the last requirement can also be stated in the form $v(0)=0$. The function $v$ is called the harmonic conjugate of $u$, or the conjugate function of $u$.

Suppose now that $u$ satisfies

$$
\sup _{r<1}\left\|u_{r}\right\|_{p}<\infty
$$

for some $p$. Does it follow that (1) holds then with $v$ in place of $u$ ?

Equivalently, does it follow that $f \in H^{p}$ ?

The answer (given by M. Riesz) is affirmative if $1<p<\infty$. (For $p=1$ and $p=\infty$ it is negative; see Exercise 24.) The precise statement is given by Theorem 17.26

Let us recall that every harmonic $u$ that satisfies (1) is the Poisson integral of a function $u^{*} \in L^{p}(T)$ (Theorem 11.30) if $1<p<\infty$. Theorem 11.11 suggests therefore another restatement of the problem:

If $1<p<\infty$, and if we associate to each $h \in L^{p}(T)$ the holomorphic function

$$
(\psi h)(z)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{e^{i t}+z}{e^{i t}-z} h\left(e^{i t}\right) d t \quad(z \in U)
$$

do all of these functions $\psi \mathrm{h}$ lie in $H^{p}$ ?

Exercise 25 deals with some other aspects of this problem.

17.25 Lemma If $1<p \leq 2, \delta=\pi /(1+p), \alpha=(\cos \delta)^{-1}$, and $\beta=\alpha^{p}(1+\alpha)$, then

$$
1 \leq \beta(\cos \varphi)^{p}-\alpha \cos p \varphi \quad\left(-\frac{\pi}{2} \leq \varphi \leq \frac{\pi}{2}\right)
$$

Proof If $\delta \leq|\varphi| \leq \pi / 2$, then the right side of (1) is not less than

$$
-\alpha \cos p \varphi \geq-\alpha \cos p \delta=\alpha \cos \delta=1
$$

and it exceeds $\beta(\cos \delta)^{p}-\alpha=1$ if $|\varphi| \leq \delta$.

17.26 Theorem If $1<p<\infty$, then there is a constant $A_{p}<\infty$ such that the inequality

$$
\|\psi h\|_{p} \leq A_{p}\|h\|_{p}
$$

holds for every $h \in L^{p}(T)$.

More explicitly, the conclusion is that $\psi h$ (defined in Sec. 17.24) is in $H^{p}$, and that

$$
\int_{T}\left|(\psi h)_{r}\right|^{p} d \sigma \leq A_{p}^{p} \int_{T}|h|^{p} d \sigma \quad \cdot(0 \leq r<1)
$$

where $d \sigma=d \theta / 2 \pi$ is the normalized Lebesgue measure on $T$.

Note that $h$ is not required to be a real function in this theorem, which asserts that $\psi: L^{p} \rightarrow H^{p}$ is a bounded linear operator.

Proof Assume first that $1<p \leq 2$, that $h \in L^{p}(T), h \geq 0, h \not \equiv 0$, and let $u$ be the real part of $f=\psi h$. Formula 11.5(2) shows that $u=P[h]$, hence $u>0$ in $U$. Since $U$ is simply connected and $f$ has no zero in $U$, there is a $g \in H(U)$ such that $g=f^{p}, g(0)>0$. Also, $u=|f| \cos \varphi$, where $\varphi$ is a real function with domain $U$ that satisfies $|\varphi|<\pi / 2$.

If $\alpha=\alpha_{p}$ and $\beta=\beta_{p}$ are chosen as in Lemma 17.25, it follows that

$$
\int_{T}\left|f_{r}\right|^{p} d \sigma \leq \beta \int_{T}\left(u_{r}\right)^{p} d \sigma-\alpha \int_{T}\left|f_{r}\right|^{p} \cos \left(p \varphi_{r}\right) d \sigma
$$

for $0 \leq r<1$.

Note that $|f|^{p} \cos p \varphi=\operatorname{Re} g$. The mean value property of harmonic functions shows therefore that the last integral in (3) is equal to $\operatorname{Re} g(0)>0$. Hence

$$
\int_{T}\left|f_{r}\right|^{p} d \sigma \leq \beta \int_{T} h^{p} d \sigma \quad(0 \leq r<1)
$$

because $u=P[h]$ implies $\left\|u_{r}\right\|_{p} \leq\|h\|_{p}$. Thus

$$
\|\psi h\|_{p} \leq \beta^{1 / p}\|h\|_{p}
$$

if $h \in L^{p}(T), h \geq 0$.

If $h$ is an arbitrary (complex) function in $L^{p}(T)$, the preceding result applies to the positive and negative parts of the real and imaginary parts of $h$.

This proves (2), for $1<p \leq 2$, with $A_{p}=4 \beta^{1 / p}$.

To complete the proof, consider the case $2<p<\infty$. Let $w \in L^{q}(T)$, where $q$ is the exponent conjugate to $p$. Put $\tilde{w}\left(e^{i \theta}\right)=w\left(e^{-i \theta}\right)$. A simple computation, using Fubini's theorem, shows for any $h \in L^{p}(T)$ that

$$
\int_{T}(\psi h)_{r} \tilde{w} d \sigma=\int_{T}(\psi w)_{r} \tilde{h} d \sigma \quad(0 \leq r<1)
$$

Since $q<2$, (2) holds with $w$ and $q$ in place of $h$ and $p$, so that (6) leads to

$$
\left|\int_{T}(\psi h)_{r} \tilde{w} d \sigma\right| \leq A_{q}\|w\|_{q}\|h\|_{p}
$$

Now let $w$ range over the unit ball of $L^{q}(T)$ and take the supremum on the left side of (7). The result is

$$
\left\{\int_{T}\left|(\psi h)_{r}\right|^{p} d \sigma\right\}^{1 / p} \leq A_{q}\left\{\int_{T}|h|^{p} d \sigma\right\}^{1 / p} \quad(0 \leq r<1)
$$

Hence (2) holds again, with $A_{p} \leq A_{q}$.

(If we take the smallest admissible values for $A_{p}$ and $A_{q}$, the last calculation can be reversed, and shows that $A_{p}=A_{q}$.)

## Exercises

1 Prove Theorems 17.4 and 17.5 for upper semicontinuous subharmonic functions.

2 Assume $f \in H(\Omega)$ and prove that $\log (1+|f|)$ is subharmonic in $\Omega$.

3 Suppose $0<p \leq \infty$ and $f \in H(U)$. Prove that $f \in H^{p}$ if and only if there is a harmonic function $u$ in $U$ such that $|f(z)|^{p} \leq u(z)$ for all $z \in U$. Prove that if there is one such harmonic majorant $u$ of $|f|^{p}$, then there is at least one, say $u_{f}$. (Explicitly, $|f|^{p} \leq u_{f}$ and $u_{f}$ is harmonic; and if $|f|^{p} \leq u$ and $u$ is harmonic, then $u_{f} \leq u$.) Prove that $\|f\|_{p}=u_{f}(0)^{1 / p}$. Hint: Consider the harmonic functions in $D(0 ; R)$, $R<1$, with boundary values $|f|^{p}$, and let $R \rightarrow 1$.

4 Prove likewise that $f \in N$ if and only if $\log ^{+}|f|$ has a harmonic majorant in $U$.

5 Suppose $f \in H^{p}, \varphi \in H(U)$, and $\varphi(U) \subset U$. Does it follow that $f \circ \varphi \in H^{p}$ ? Answer the same question with $N$ in place of $H^{p}$.

6 If $0<r<s \leq \infty$, show that $H^{s}$ is a proper subclass of $H^{r}$.

7 Show that $H^{\infty}$ is a proper subclass of the intersection of all $H^{p}$ with $p<\infty$.

8 If $f \in H^{1}$ and $f^{*} \in L^{p}(T)$, prove that $f \in H^{p}$.

9 Suppose $f \in H(U)$ and $f(U)$ is not dense in the plane. Prove that $f$ has finite radial limits at almost all points of $T$.

10 Fix $\alpha \in U$. Prove that the mapping $f \rightarrow f(\alpha)$ is a bounded linear functional on $H^{2}$. Since $H^{2}$ is a Hilbert space, this functional can be represented as an inner product with some $g \in H^{2}$. Find this $g$.

11 Fix $\alpha \in U$. How large can $\left|f^{\prime}(\alpha)\right|$ be if $\|f\|_{2} \leq 1$ ? Find the extremal functions. Do the same for $f^{(n)}(\alpha)$.

12 Suppose $p \geq 1, f \in H^{p}$, and $f^{*}$ is real a.e. on $T$. Prove that $f$ is then constant. Show that this result is false for every $p<1$.

13 Suppose $f \in H(U)$, and suppose there exists an $M<\infty$ such that $f$ maps every circle of radius $r<1$ and center 0 onto a curve $\gamma_{r}$ whose length is at most $M$. Prove that $f$ has a continuous extension to $\bar{U}$ and that the restriction of $f$ to $T$ is absolutely continuous.

14 Suppose $\mu$ is a complex Borel measure on $T$ such that

$$
\int_{T} e^{i n t} d \mu(t)=0 \quad(n=1,2,3, \ldots)
$$

Prove that then either $\mu=0$ or the support of $\mu$ is all of $T$.

15 Suppose $K$ is a proper compact subset of the unit circle $T$. Prove that every continuous function on $K$ can be uniformly approximated on $K$ by polynomials. Hint: Use Exercise 14.

16 Complete the proof of Theorem 17.17 for the case $0<p<1$.

17 Let $\varphi$ be a nonconstant inner function with no zero in $U$.

(a) Prove that $1 / \varphi \notin H^{p}$ if $p>0$.

(b) Prove that there is at least one $e^{i \theta} \in T$ such that $\lim _{r \rightarrow 1} \varphi\left(r e^{i \theta}\right)=0$.

Hint $: \log |\varphi|$ is a negative harmonic function.

18 Suppose $\varphi$ is a nonconstant inner function, $|\alpha|<1$, and $\alpha \notin \varphi(U)$. Prove that $\lim _{r \rightarrow 1} \varphi\left(r e^{i \theta}\right)=\alpha$ for at least one $e^{i \theta} \in T$.

19 Suppose $f \in H^{1}$ and $1 / f \in H^{1}$. Prove that $f$ is then an outer function.

20 Suppose $f \in H^{1}$ and $\operatorname{Re}[f(z)]>0$ for all $z \in U$. Prove that $f$ is an outer function.

21 Prove that $f \in N$ if and only if $f=g / h$, where $g$ and $h \in H^{\infty}$ and $h$ has no zero in $U$.

22 Prove the following converse of Theorem 15.24:

If $f \in H(U)$ and if

$$
\lim _{r \rightarrow 1} \int_{-\pi}^{\pi}|\log | f\left(r e^{i \theta}\right)|| d \theta=0
$$

then $f$ is a Blaschke product. Hint: $\left({ }^{*}\right)$ implies

$$
\lim _{r \rightarrow 1} \int_{-\pi}^{\pi} \log ^{+}\left|f\left(r e^{i \theta}\right)\right| d \theta=0
$$

Since $\log ^{+}|f| \geq 0$, it follows from Theorems 17.3 and 17.5 that $\log ^{+}|f|=0$, so $|f| \leq 1$. Now $f=B g, g$ has no zeros, $|g| \leq 1$, and $(*)$ holds with $1 / g$ in place of $f$. By the first argument, $|1 / g| \leq 1$. Hence $|g|=1$.

23 Find the conditions mentioned in Sec. 17.22.

24 The conformal mapping of $U$ onto a vertical strip shows that M. Riesz's theorem on conjugate functions cannot be extended to $p=\infty$. Deduce that it cannot be extended to $p=1$ either.

25 Suppose $1<p<\infty$, and associate with each $f \in L^{p}(T)$ its Fourier coefficients

$$
f(n)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f\left(e^{i t}\right) e^{-i n t} d t \quad(n=0, \pm 1, \pm 2, \ldots)
$$

Deduce the following statements from Theorem 17.26:

(a) To each $f \in L^{p}(T)$ there corresponds a function $g \in L^{p}(T)$ such that $\hat{g}(n)=\hat{f}(n)$ for $n \geq 0$ but $\hat{g}(n)=0$ for all $n<0$. In fact, there is a constant $C$, depending only on $p$, such that

$$
\|g\|_{p} \leq C\|f\|_{p}
$$

The mapping $f \rightarrow g$ is thus a bounded linear projection of $L^{p}(T)$ into $L^{p}(T)$. The Fourier series of $g$ is obtained from that of $f$ by deleting the terms with $n<0$.

(b) Show that the same is true if we delete the terms with $n<k$, where $k$ is any given integer.

(c) Deduce from (b) that the partial sums $s_{n}$ of the Fourier series of any $f \in L^{p}(T)$ form a bounded sequence in $L^{p}(T)$. Conclude further that we actually have

$$
\lim _{n \rightarrow \infty}\left\|f-s_{n}\right\|_{p}=0
$$

(d) If $f \in L^{p}(T)$ and if

$$
F(z)=\sum_{n=0}^{\infty} \hat{f}(n) z^{n}
$$

then $F \in H^{p}$, and every $F \in H^{p}$ is so obtained. Thus the projection mentioned in (a) may be regarded as a mapping of $L^{p}(T)$ onto $H^{p}$.

26 Show that there is a much simpler proof of Theorem 17.26 if $p=2$, and find the best value of $A_{2}$.

27 Suppose $f(z)=\sum_{0}^{\infty} a_{n} z^{n}$ in $U$ and $\sum\left|a_{n}\right|<\infty$. Prove that

$$
\int_{0}^{1}\left|f^{\prime}\left(r e^{i \theta}\right)\right| d r<\infty
$$

for all $\theta$.

28 Prove that the following statements are correct if $\left\{n_{k}\right\}$ is a sequence of positive integers which tends to $\infty$ sufficiently rapidly. If

$$
f(z)=\sum_{k=1}^{\infty} \frac{z^{n_{k}}}{k}
$$

then $\left|f^{\prime}(z)\right|>n_{k} /(10 k)$ for all $z$ such that

$$
1-\frac{1}{n_{k}}<|z|<1-\frac{1}{2 n_{k}}
$$

Hence

$$
\int_{0}^{1}\left|f^{\prime}\left(r e^{i \theta}\right)\right| d r=\infty
$$

for every $\theta$, although

$$
\lim _{R \rightarrow 1} \int_{0}^{R} f^{\prime}\left(r e^{i \theta}\right) d r
$$

exists (and is finite) for almost all $\theta$. Interpret this geometrically, in terms of the lengths of the images under $f$ of the radii in $U$.

29 Use Theorem 17.11 to obtain the following characterization of the boundary values of $H^{p}$. functions, for $1 \leq p \leq \infty$ :

A function $g \in L^{p}(T)$ is $f^{*}$ (a.e.) for some $f \in H^{p}$ if and only if

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} g\left(e^{i t}\right) e^{-i n t} d t=0
$$

for all negative integers $n$.

## CHAPTER

## ELEMENTARY THEORY OF BANACH ALGEBRAS

## Introduction

18.1 Definitions A complex algebra is a vector space $A$ over the complex field in which an associative and distributive multiplication is defined, i.e.,

$$
x(y z)=(x y) z, \quad(x+y) z=x z+y z, \quad x(y+z)=x y+x z
$$

for $x, y$, and $z \in A$, and which is related to scalar multiplication so that

$$
\alpha(x y)=x(\alpha y)=(\alpha x) y
$$

for $x$ and $y \in A, \alpha$ a scalar.

If there is a norm defined in $A$ which makes $A$ into a normed linear space and which satisfies the multiplicative inequality

$$
\|x y\| \leq\|x\|\|y\| \quad(x \text { and } y \in A)
$$

then $\boldsymbol{A}$ is a normed complex algebra. If, in addition, $\boldsymbol{A}$ is a complete metric space relative to this norm, i.e., if $\boldsymbol{A}$ is a Banach space, then we call $\boldsymbol{A}$ a Banach algebra.

The inequality (3) makes multiplication a continuous operation. This means that if $x_{n} \rightarrow x$ and $y_{n} \rightarrow y$, then $x_{n} y_{n} \rightarrow x y$, which follows from (3) and the identity

$$
x_{n} y_{n}-x y=\left(x_{n}-x\right) y_{n}+x\left(y_{n}-y\right) .
$$

Note that we have not required that $A$ be commutative, i.e., that $x y=y x$ for all $x$ and $y \in A$, and we shall not do so except when explicitly stated.

However, we shall assume that $A$ has a unit. This is an element $e$ such that

$$
x e=e x=x \quad(x \in A) .
$$

It is easily seen that there is at most one such $e\left(e^{\prime}=e^{\prime} e=e\right)$ and that $\|e\| \geq 1$, by (3). We shall make the additional assumption that

$$
\|e\|=1
$$

An element $x \in A$ will be called invertible if $x$ has an inverse in $A$, i.e., if there exists an element $x^{-1} \in A$ such that

$$
x^{-1} x=x x^{-1}=e
$$

Again, it is easily seen that no $x \in A$ has more than one inverse.

If $x$ and $y$ are invertible in $A$, so are $x^{-1}$ and $x y$, since $(x y)^{-1}=y^{-1} x^{-1}$. The invertible elements therefore form a group with respect to multiplication.

The spectrum of an element $x \in A$ is the set of all complex numbers $\lambda$ such that $x-\lambda e$ is not invertible. We shall denote the spectrum of $x$ by $\sigma(x)$.

18.2 The theory of Banach algebras contains a great deal of interplay between algebraic properties on the one hand and topological ones on the other. We already saw an example of this in Theorem 9.21, and shall see others. There are also close relations between Banach algebras and holomorphic functions: The easiest proof of the fundamental fact that $\sigma(x)$ is never empty depends on Liouville's theorem concerning entire functions, and the spectral radius formula follows naturally from theorems about power series. This is one reason for restricting our attention to complex Banach algebras. The theory of real Banach algebras (we omit the definition, which should be obvious) is not so satisfactory.

## The Invertible Elements

In this section, $A$ will be a complex Banach algebra with unit $e$, and $G$ will be the set of all invertible elements of $A$.

18.3 Theorem If $x \in A$ and $\|x\|<1$, then $e+x \in G$,

$$
(e+x)^{-1}=\sum_{n=0}^{\infty}(-1)^{n} x^{n}
$$

and

$$
\left\|(e+x)^{-1}-e+x\right\| \leq \frac{\|x\|^{2}}{1-\|x\|}
$$

Proof The multiplicative inequality $18.1(3)$ shows that $\left\|x^{n}\right\| \leq\|x\|^{n}$. If

$$
s_{N}=e-x+x^{2}-\cdots+(-1)^{N} x^{N},
$$

it follows that $\left\{s_{N}\right\}$ is a Cauchy sequence in $A$, hence the series in (1) converges (with respect to the norm of $A$ ) to an element $y \in A$. Since multiplication is continuous and

$$
(e+x) s_{N}=e+(-1)^{N} x^{N+1}=s_{N}(e+x)
$$

we see that $(e+x) y=e=y(e+x)$. This gives (1), and (2) follows from

$$
\left\|\sum_{n=2}^{\infty}(-1)^{n} x^{n}\right\| \leq \sum_{n=2}^{\infty}\left\|x^{n}\right\| \leq \sum_{n=2}^{\infty}\|x\|^{n}=\frac{\|x\|^{2}}{1-\|x\|}
$$

18.4 Theorem Suppose $x \in G,\left\|x^{-1}\right\|=1 / \alpha, h \in A$, and $\|h\|=\beta<\alpha$. Then $x+h \in G$, and

$$
\left\|(x+h)^{-1}-x^{-1}+x^{-1} h x^{-1}\right\| \leq \frac{\beta^{2}}{\alpha^{2}(\alpha-\beta)}
$$

Proof $\left\|x^{-1} h\right\| \leq \beta / \alpha<1$, hence $e+x^{-1} h \in G$, by Theorem 18.3; and since $x+h=x\left(e+x^{-1} h\right)$, we have $x+h \in G$ and

$$
(x+h)^{-1}=\left(e+x^{-1} h\right)^{-1} x^{-1} .
$$

Thus

$$
(x+h)^{-1}-x^{-1}+x^{-1} h x^{-1}=\left[\left(e+x^{-1} h\right)^{-1}-e+x^{-1} h\right] x^{-1},
$$

and the inequality (1) follows from Theorem 18.3, with $x^{-1} h$ in place of $x . / / / /$

Corollary $1 G$ is an open set, and the mapping $x \rightarrow x^{-1}$ is a homeomorphism of $G$ onto $G$.

For if $x \in G$ and $\|h\| \rightarrow 0$, (1) implies that $\left\|(x+h)^{-1}-x^{-1}\right\| \rightarrow 0$. Thus $x \rightarrow x^{-1}$ is continuous; it clearly maps $G$ onto $G$, and since it is its own inverse, it is a homeomorphism.

Corollary 2 The mapping $x \rightarrow x^{-1}$ is differentiable. Its differential at any $x \in G$ is the linear operator which takes $h \in A$ to $-x^{-1} h x^{-1}$.

This can also be read off from (1). Note that the notion of the differential of a transformation makes sense in any normed linear space, not just in $R^{k}$, as in Definition 7.22. If $A$ is commutative, the above differential takes $h$ to $-x^{-2} h$, which agrees with the fact that the derivative of the holomorphic function $z^{-1}$ is $-z^{-2}$.

Corollary 3 For every $x \in A, \sigma(x)$ is compact, and $|\lambda| \leq\|x\|$ if $\lambda \in \sigma(x)$.

For if $|\lambda|>\|x\|$, then $e-\lambda^{-1} x \in G$, by Theorem 18.3, and the same is true of $x-\lambda e=-\lambda\left(e-\lambda^{-1} x\right)$; hence $\lambda \notin \sigma(x)$. To prove that $\sigma(x)$ is closed, observe (a) $\lambda \in \sigma(x)$ if and only if $x-\lambda e \notin G$; (b) the complement of $G$ is a closed subset of $A$, by Corollary 1 ; and $(c)$ the mapping $\lambda \rightarrow x-\lambda e$ is a continuous mapping of the complex plane into $A$.

18.5 Theorem Let $\Phi$ be a bounded linear functional on $A$, fix $x \in A$, and define

$$
f(\lambda)=\Phi\left[(x-\lambda e)^{-1}\right] \quad(\lambda \notin \sigma(x)) .
$$

Then $f$ is holomorphic in the complement of $\sigma(x)$, and $f(\lambda) \rightarrow 0$ as $\lambda \rightarrow \infty$.

Proof Fix $\lambda \notin \sigma(x)$ and apply Theorem 18.4 with $x-\lambda e$ in place of $x$ and with $(\lambda-\mu) e$ in place of $h$. We see that there is a constant $C$, depending on $x$ and $\lambda$, such that

$$
\left\|(x-\mu e)^{-1}-(x-\lambda e)^{-1}+(\lambda-\mu)(x-\lambda e)^{-2}\right\| \leq C|\mu-\lambda|^{2}
$$

for all $\mu$ which are close enough to $\lambda$. Thus

$$
\frac{(x-\mu e)^{-1}-(x-\lambda e)^{-1}}{\mu-\lambda} \rightarrow(x-\lambda e)^{-2}
$$

as $\mu \rightarrow \lambda$, and if we apply $\Phi$ to both sides of (3), the continuity and linearity of $\Phi$ show that

$$
\frac{f(\mu)-f(\lambda)}{\mu-\lambda} \rightarrow \Phi\left[(x-\lambda e)^{-2}\right]
$$

So $f$ is differentiable and hence holomorphic outside $\sigma(x)$. Finally, as $\lambda \rightarrow \infty$ we have

$$
\lambda f(\lambda)=\Phi\left[\lambda(x-\lambda e)^{-1}\right]=\Phi\left[\left(\frac{x}{\lambda}-e\right)^{-1}\right] \rightarrow \Phi(-e)
$$

by the continuity of the inversion mapping in $G$.

18.6 Theorem For every $x \in A, \sigma(x)$ is compact and not empty.

Proof We already know that $\sigma(x)$ is compact. Fix $x \in A$, and fix $\lambda_{0} \notin \sigma(x)$. Then $\left(x-\lambda_{0} e\right)^{-1} \neq 0$, and the Hahn-Banach theorem implies the existence of a bounded linear functional $\Phi$ on $A$ such that $f\left(\lambda_{0}\right) \neq 0$, where $f$ is defined as in Theorem 18.5. If $\sigma(x)$ were empty, Theorem 18.5 would imply that $f$ is an entire function which tends to 0 at $\infty$, hence $f(\lambda)=0$ for every $\lambda$, by Liouville's theorem, and this contradicts $f\left(\lambda_{0}\right) \neq 0$. So $\sigma(x)$ is not empty.

18.7 Theorem (Gelfand-Mazur) If $A$ is a complex Banach algebra with unit in which each nonzero element is invertible, then $A$ is (isometrically isomorphic to) the complex field.

An algebra in which each nonzero element is invertible is called a division algebra. Note that the commutativity of $\boldsymbol{A}$ is not part of the hypothesis; it is part of the conclusion.

Proof If $x \in A$ and $\lambda_{1} \neq \lambda_{2}$, at least one of the elements $x-\lambda_{1} e$ and $x-\lambda_{2} e$ must be invertible, since they cannot both be 0 . It now follows from Theorem 18.6 that $\sigma(x)$ consists of exactly one point, say $\lambda(x)$, for each $x \in A$. Since $x-\lambda(x) e$ is not invertible, it must be 0 , hence $x=\lambda(x) e$. The mapping $x \rightarrow \dot{\lambda}(x)$ is therefore an isomorphism of $A$ onto the complex field, which is also an isometry, since $|\lambda(x)|=\|\lambda(x) e\|=\|x\|$ for all $x \in A$.

18.8 Definition For any $x \in A$, the spectral radius $\rho(x)$ of $x$ is the radius of the smallest closed disc with center at the origin which contains $\sigma(x)$ (sometimes this is also called the spectral norm of $x$; see Exercise 14):

$$
\rho(x)=\sup \{|\lambda|: \lambda \in \sigma(x)\} .
$$

18.9 Theorem (Spectral Radius Formula) For every $x \in A$,

$$
\lim _{n \rightarrow \infty}\left\|x^{n}\right\|^{1 / n}=\rho(x)
$$

(This existence of the limit is part of the conclusion.)

Proof Fix $x \in A$, let $n$ be a positive integer, $\lambda$ a complex number, and assume $\lambda^{n} \notin \sigma\left(x^{n}\right)$. We have

$$
\left(x^{n}-\lambda^{n} e\right)=(x-\lambda e)\left(x^{n-1}+\lambda x^{n-2}+\cdots+\lambda^{n-1} e\right)
$$

Multiply both sides of (2) by $\left(x^{n}-\lambda^{n} e\right)^{-1}$. This shows that $x-\lambda e$ is invertible, hence $\lambda \notin \sigma(x)$.

So if $\lambda \in \sigma(x)$, then $\lambda^{n} \in \sigma\left(x^{n}\right)$ for $n=1,2,3, \ldots$ Corollary 3 to Theorem 18.4 shows that $\left|\lambda^{n}\right| \leq\left\|x^{n}\right\|$, and therefore $|\lambda| \leq\left\|x^{n}\right\|^{1 / n}$. This gives

$$
\rho(x) \leq \lim _{n \rightarrow \infty} \inf \left\|x^{n}\right\|^{1 / n}
$$

Now if $|\lambda|>\|x\|$, it is easy to verify that

$$
(\lambda e-x) \sum_{n=0}^{\infty} \lambda^{-n-1} x^{n}=e
$$

The above series is therefore $-(x-\lambda e)^{-1}$. Let $\Phi$ be a bounded linear functional on $A$ and define $f$ as in Theorem 18.5. By (4), the expansion

$$
f(\lambda)=-\sum_{n=0}^{\infty} \Phi\left(x^{n}\right) \lambda^{-n-1}
$$

is valid for all $\lambda$ such that $|\lambda|>\|x\|$. By Theorem 18.5, $f$ is holomorphic outside $\sigma(x)$, hence in the set $\{\lambda:|\lambda|>\rho(x)\}$. It follows that the power series (5) converges if $|\lambda|>\rho(x)$. In particular,

$$
\sup _{n}\left|\Phi\left(\lambda^{-n} x^{n}\right)\right|<\infty \quad(|\lambda|>\rho(x))
$$

for every bounded linear functional $\Phi$ on $A$.

It is a consequence of the Hahn-Banach theorem (Sec. 5.21) that the norm of any element of $A$ is the same as its norm as a linear functional on the dual space of $A$. Since (6) holds for every $\Phi$, we can now apply the Banach-Steinhaus theorem and conclude that to each $\lambda$ with $|\lambda|>\rho(x)$ there corresponds a real number $C(\lambda)$ such that

$$
\left\|\lambda^{-n} x^{n}\right\| \leq C(\lambda) \quad(n=1,2,3, \ldots)
$$

Multiply (7) by $|\lambda|^{n}$ and take $n$th roots. This gives

$$
\left\|x^{n}\right\|^{1 / n} \leq|\lambda|[C(\lambda)]^{1 / n} \quad(n=1,2,3, \ldots)
$$

if $|\lambda|>\rho(x)$, and hence

$$
\limsup _{n \rightarrow \infty}\left\|x^{n}\right\|^{1 / n} \leq \rho(x)
$$

The theorem follows from (3) and (9).

### 18.10 Remarks

(a) Whether an element of $A$ is or is not invertible in $A$ is a purely algebraic property. Thus the spectrum of $x$, and likewise the spectral radius $\rho(x)$, are defined in terms of the algebraic structure of $A$, regardless of any metric (or topological) considerations. The limit in the statement of Theorem 18.9, on the other hand, depends on metric properties of $A$. This is one of the remarkable features of the theorem: It asserts the equality of two quantities which arise in entirely different ways.

(b) Our algebra may be a subalgebra of a larger Banach algebra $B$ (an example follows), and then it may very well happen that some $x \in A$ is not invertible in $A$ but is invertible in $B$. The spectrum of $x$ therefore depends on the algebra; using the obvious notation, we have $\sigma_{A}(x) \supset$ $\sigma_{B}(x)$, and the inclusion may be proper. The spectral radius of $x$, however, is unaffected by this, since Theorem 18.9 shows that it can be expressed in terms of metric properties of powers of $x$, and these are independent of anything that happens outside $\boldsymbol{A}$.

18.11 Example Let $C(T)$ be the algebra of all continuous complex functions on the unit circle $T$ (with pointwise addition and multiplication and the supremum norm), and let $A$ be the set of all $f \in C(T)$ which can be extended to a continuous function $F$ on the closure of the unit disc $U$, such that $F$ is holomorphic in $U$. It is easily seen that $A$ is a subalgebra of $C(T)$. If $f_{n} \in A$
and $\left\{f_{n}\right\}$ converges uniformly on $T$, the maximum modulus theorem forces the associated sequence $\left\{F_{n}\right\}$ to converge uniformly on the closure of $U$. This shows that $A$ is a closed subalgebra of $C(T)$, and so $A$ is itself a Banach algebra.

Define the function $f_{0}$ by $f_{0}\left(e^{i \theta}\right)=e^{i \theta}$. Then $F_{0}(z)=z$. The spectrum of $f_{0}$ as an element of $A$ consists of the closed unit disc; with respect to $C(T)$, the spectrum of $f_{0}$ consists only of the unit circle. In accordance with Theorem 18.9 , the two spectral radii coincide.

## Ideals and Homomorphisms

From now on we shall deal only with commutative algebras.

18.12 Definition A subset $I$ of a commutative complex algebra $A$ is said to be an ideal if $(a) I$ is a subspace of $A$ (in the vector space sense) and $(b) x y \in I$ whenever $x \in A$ and $y \in I$. If $I \neq A, I$ is a proper ideal. Maximal ideals are proper ideals which are not contained in any larger proper ideals. Note that no proper ideal contains an invertible element.

If $B$ is another complex algebra, a mapping $\varphi$ of $A$ into $B$ is called a homomorphism if $\varphi$ is a linear mapping which also preserves multiplication: $\varphi(x) \varphi(y)=\varphi(x y)$ for all $x$ and $y \in A$. The kernel (or null space) of $\varphi$ is the set of all $x \in A$ such that $\varphi(x)=0$. It is trivial to verify that the kernel of a homomorphism is an ideal. For the converse, see Sec. 18.14.

18.13 Theorem If $A$ is a commutative complex algebra with unit, every proper ideal of $A$ is contained in a maximal ideal. If, in addition, $A$ is a Banach algebra, every maximal ideal of $A$ is closed.

Proof The first part is an almost immediate consequence of the Hausdorff maximality principle (and holds in any commutative ring with unit). Let $I$ be a proper ideal of $A$. Partially order the collection $\mathscr{P}$ of all proper ideals of $A$ which contain $I$ (by set inclusion), and let $M$ be the union of the ideals in some maximal linearly ordered subcollection $\mathscr{2}$ of $\mathscr{P}$. Then $M$ is an ideal (being the union of a linearly ordered collection of ideals), $I \subset M$, and $M \neq$ $A$, since no member of $\mathscr{P}$ contains the unit of $A$. The maximality of $\mathscr{2}$ implies that $M$ is a maximal ideal of $A$.

If $A$ is a Banach algebra, the closure $\bar{M}$ of $M$ is also an ideal (we leave the details of the proof of this statement to the reader). Since $M$ contains no invertible element of $A$ and since the set of all invertible elements is open, we have $\bar{M} \neq A$, and the maximality of $M$ therefore shows that $\bar{M}=M$.

18.14 Quotient Spaces and Quotient Algebras Suppose $J$ is a subspace of a vector space $A$, and associate with each $x \in A$ the coset

$$
\varphi(x)=x+J=\{x+y: y \in J\} .
$$

If $x_{1}-x_{2} \in J$, then $\varphi\left(x_{1}\right)=\varphi\left(x_{2}\right)$. If $x_{1}-x_{2} \notin J, \varphi\left(x_{1}\right) \cap \varphi\left(x_{2}\right)=\varnothing$. The set of all cosets of $J$ is denoted by $A / J$; it is a vector space if we define

$$
\varphi(x)+\varphi(y)=\varphi(x+y), \quad \lambda \varphi(x)=\varphi(\lambda x)
$$

for $x$ and $y \in A$ and scalars $\lambda$. Since $J$ is a vector space, the operations (2) are well defined; this means that if $\varphi(x)=\varphi\left(x^{\prime}\right)$ and $\varphi(y)=\varphi\left(y^{\prime}\right)$, then

$$
\varphi(x)+\varphi(y)=\varphi\left(x^{\prime}\right)+\varphi\left(y^{\prime}\right), \quad \lambda \varphi(x)=\lambda \varphi\left(x^{\prime}\right)
$$

Also, $\varphi$ is clearly a linear mapping of $A$ onto $A / J$; the zero element of $A / J$ is $\varphi(0)=J$.

Suppose next that $A$ is not merely a vector space but a commutative algebra and that $J$ is a proper ideal of $A$. If $x^{\prime}-x \in J$ and $y^{\prime}-y \in J$, the identity

$$
x^{\prime} y^{\prime}-x y=\left(x^{\prime}-x\right) y^{\prime}+x\left(y^{\prime}-y\right)
$$

shows that $x^{\prime} y^{\prime}-x y \in J$. Therefore multiplication can be defined in $A / J$ in a consistent manner:

$$
\varphi(x) \varphi(y)=\varphi(x y) \quad(x \text { and } y \in A) .
$$

It is then easily verified that $A / J$ is an algebra, and $\varphi$ is a homomorphism of $A$ onto $A / J$ whose kernel is $J$.

If $A$ has a unit element $e$, then $\varphi(e)$ is the unit of $A / J$, and $A / J$ is a field if and only if $J$ is a maximal ${ }^{\circ}$ teal.

To see this, suppose $x \in A$ and $x \notin J$, and put

$$
I=\{a x+y: a \in A, y \in J\}
$$

Then $I$ is an ideal in $A$ which contains $J$ properly, since $x \in I$. If $J$ is maximal, $I=A$, hence $a x+y=e$ for some $a \in A$ and $y \in J$, hence $\varphi(a) \varphi(x)=\varphi(e)$; and this says that every nonzero element of $A / J$ is invertible, so that $A / J$ is a field. If $J$ is not maximal, we can choose $x$ as above so that $I \neq A$, hence $e \notin I$, and then $\varphi(x)$ is not invertible in $A / J$.

18.15 Quotient Norms Suppose $A$ is a normed linear space, $J$ is a closed subspace of $A$, and $\varphi(x)=x+J$, as above. Define

$$
\|\varphi(x)\|=\inf \{\|x+y\|: y \in J\}
$$

Note that $\|\varphi(x)\|$ is the greatest lower bound of the norms of those elements which lie in the coset $\varphi(x)$; this is the same as the distance from $x$ to $J$. We call the norm defined in $A / J$ by (1) the quotient norm of $A / J$. It has the following properties:

(a) $A / J$ is a normed linear space.

(b) If $A$ is a Banach space, so is $A / J$.

(c) If $A$ is a commutative Banach algebra and $J$ is a proper closed ideal, then $A / J$ is a commutative Banach algebra.

These are easily verified:

If $x \in J,\|\varphi(x)\|=0$. If $x \notin J$, the fact that $J$ is closed implies that $\|\varphi(x)\|>0$. It is clear that $\|\lambda \varphi(x)\|=|\lambda|\|\varphi(x)\|$. If $x_{1}$ and $x_{2} \in A$ and $\epsilon>0$, there exist $y_{1}$ and $y_{2} \in J$ so that

$$
\left\|x_{i}+y_{i}\right\|<\left\|\varphi\left(x_{i}\right)\right\|+\epsilon \quad(i=1,2)
$$

Hence

$$
\left\|\varphi\left(x_{1}+x_{2}\right)\right\| \leq\left\|x_{1}+x_{2}+y_{1}+y_{2}\right\|<\left\|\varphi\left(x_{1}\right)\right\|+\left\|\varphi\left(x_{2}\right)\right\|+2 \epsilon
$$

which gives the triangle inequality and proves $(a)$.

Suppose $A$ is complete and $\left\{\varphi\left(x_{n}\right)\right\}$ is a Cauchy sequence in $A / J$. There is a subsequence for which

$$
\left\|\varphi\left(x_{n_{i}}\right)-\varphi\left(\dot{x}_{n_{i+1}}\right)\right\|<2^{-i} \quad(i=1,2,3, \ldots)
$$

and there exist elements $z_{i}$ so that $z_{i}-x_{n_{i}} \in J$ and $\left\|z_{i}-z_{i+1}\right\|<2^{-i}$. Thus $\left\{z_{i}\right\}$ is a Cauchy sequence in $A$; and since $A$ is complete, there exists $z \in A$ such that $\left\|z_{i}-z\right\| \rightarrow 0$. It follows that $\varphi\left(x_{n_{i}}\right)$ converges to $\varphi(z)$ in $A / J$. But if a Cauchy sequence has a convergent subsequence, then the full sequence converges. Thus $A / J$ is complete, and we have proved $(b)$.

To prove (c), choose $x_{1}$ and $x_{2} \in A$ and $\epsilon>0$, and choose $y_{1}$ and $y_{2} \in J$ so that (2) holds. Note that $\left(x_{1}+y_{1}\right)\left(x_{2}+y_{2}\right) \in x_{1} x_{2}+J$, so that

$$
\left\|\varphi\left(x_{1} x_{2}\right)\right\| \leq\left\|\left(x_{1}+y_{1}\right)\left(x_{2}+y_{2}\right)\right\| \leq\left\|x_{1}+y_{1}\right\|\left\|x_{2}+y_{2}\right\| .
$$

Now (2) implies

$$
\left\|\varphi\left(x_{1} x_{2}\right)\right\| \leq\left\|\varphi\left(x_{1}\right)\right\|\left\|\varphi\left(x_{2}\right)\right\|
$$

Finally, if $e$ is the unit element of $A$, take $x_{1} \notin J$ and $x_{2}=e$ in (6); this gives $\|\varphi(e)\| \geq 1$. But $e \in \varphi(e)$, and the definition of the quotient norm shows that $\|\varphi(e)\| \leq\|e\|=1$. So $\|\varphi(e)\|=1$, and the proof is complete.

18.16 Having dealt with these preliminaries, we are now in a position to derive some of the key facts concerning commutative Banach algebras.

Suppose, as before, that $A$ is a commutative complex Banach algebra with unit element $e$. We associate with $A$ the set $\Delta$ of all complex homomorphisms of $A$; these are the homomorphisms of $A$ onto the complex field, or, in different terminology, the multiplicative linear functionals on $A$ which are not identically 0 . As before, $\sigma(x)$ denotes the spectrum of the element $x \in A$, and $\rho(x)$ is the spectral radius of $x$.

Then the following relations hold:

### 18.17 Theorem

(a) Every maximal ideal $M$ of $A$ is the kernel of some $h \in \Delta$.

(b) $\lambda \in \sigma(x)$ if and only if $h(x)=\lambda$ for some $h \in \Delta$.

(c) $x$ is invertible in $A$ if and only if $h(x) \neq 0$ for every $h \in \Delta$.

(d) $h(x) \in \sigma(x)$ for every $x \in A$ and $h \in \Delta$.

(e) $|h(x)| \leq \rho(x) \leq\|x\|$ for every $x \in A$ and $h \in \Delta$.

Proof If $M$ is a maximal ideal of $A$, then $A / M$ is a field; and since $M$ is closed (Theorem 18.13), $A / M$ is a Banach algebra. By Theorem 18.7 there is an isomorphism $j$ of $A / M$ onto the complex field. If $h=j \circ \varphi$, where $\varphi$ is the homomorphism of $A$ onto $A / M$ whose kernel is $M$, then $h \in \Delta$ and the kernel of $h$ is $M$. This proves $(a)$.

If $\lambda \in \sigma(x)$, then $x-\lambda e$ is not invertible; hence the set of all elements $(x-\lambda e) y$, where $y \in A$, is a proper ideal of $A$, which lies in a maximal ideal (by Theorem 18.13), and (a) shows that there exists an $h \in \Delta$ such that $h(x-\lambda e)=0$. Since $h(e)=1$, this gives $h(x)=\lambda$.

On the other hand, if $\lambda \notin \sigma(x)$, then $(x-\lambda e) y=e$ for some $y \in A$. It follows that $h(x-\lambda e) h(y)=1$ for every $h \in \Delta$, so that $h(x-\lambda e) \neq 0$, or $h(x) \neq \lambda$. This proves $(b)$.

Since $x$ is invertible if and only if $0 \notin \sigma(x),(c)$ follows from $(b)$.

Finally, $(d)$ and $(e)$ are immediate consequences of $(b)$.

Note that $(e)$ implies that the norm of $h$, as a linear functional, is at most 1 . In particular, each $h \in \Delta$ is continuous. This was already proved earlier (Theorem 9.21).

## Applications

We now give some examples of theorems whose statements involve no algebraic concepts but which can be proved by Banach algebra techniques.

18.18 Theorem Let $A(U)$ be the set of all continuous functions on the closure $\bar{U}$ of the open unit disc $U$ whose restrictions to $U$ are holomorphic. Suppose $f_{1}, \ldots$, $f_{n}$ are members of $A(U)$, such that

$$
\left|f_{1}(z)\right|+\cdots+\left|f_{n}(z)\right|>0
$$

for every $z \in \bar{U}$. Then there exist $g_{1}, \ldots, g_{n} \in A(U)$ such that

$$
\sum_{i=1}^{n} f_{i}(z) g_{i}(z)=1 \quad(z \in \bar{U})
$$

ProOF Since sums, products, and uniform limits of holomorphic functions are holomorphic, $A(U)$ is a Banach algebra, with the supremum norm. The set $J$ of all functions $\Sigma f_{i} g_{i}$, where the $g_{i}$ are arbitrary members of $A(U)$, is an ideal of $A(U)$. We have to prove that $J$ contains the unit element 1 of $A(U)$. By Theorem 18.13 this happens if and only if $J$ lies in no maximal ideal of $A(U)$. By Theorem $18.17(a)$ it is therefore enough to prove that there is no homomorphism $h$ of $A(U)$ onto the complex field such that $h\left(f_{i}\right)=0$ for every $i(1 \leq i \leq n)$.

Before we determine these homomorphisms, let us note that the polynomials form a dense subset of $A(U)$. To see this, suppose $f \in A(U)$ and $\epsilon>0$; since $f$ is uniformly continuous on $\bar{U}$, there exists an $r<1$ such that $|f(z)-f(r z)|<\epsilon$ for all $z \in \bar{U}$; the expansion of $f(r z)$ in powers of $z$ converges if $|r z|<1$, hence converges to $f(r z)$ uniformly for $z \in \bar{U}$, and this gives the desired approximation.

Now let $h$ be a complex homomorphism of $A(U)$. Put $f_{0}(z)=z$. Then $f_{0} \in A(U)$. It is obvious that $\sigma\left(f_{0}\right)=\bar{U}$. By Theorem 18.17(d) there exists an $\alpha \in \bar{U}$ such that $h\left(f_{0}\right)=\alpha$. Hence $h\left(f_{0}^{n}\right)=\alpha^{n}=f_{0}^{n}(\alpha)$, for $n=1,2,3, \ldots$, so $h(P)=P(\alpha)$ for every polynomial $P$. Since $h$ is continuous and since the polynomials are dense in $A(U)$, it follows that $h(f)=f(\alpha)$ for every $f \in A(U)$.

Our hypothesis (1) implies that $\left|f_{i}(\alpha)\right|>0$ for at least one index $i$, $1 \leq i \leq n$. Thus $h\left(f_{i}\right) \neq 0$.

We have proved that to each $h \in \Delta$ there corresponds at least one of the given functions $f_{i}$ such that $h\left(f_{i}\right) \neq 0$, and this, as we noted above, is enough to prove the theorem.

Note: We have also determined all maximal ideals of $A(U)$, in the course of the preceding proof, since each is the kernel of some $h \in \Delta:$ If $\alpha \in \bar{U}$ and if $M_{\alpha}$ is the set of all $f \in A(U)$ such that $f(\alpha)=0$, then $M_{\alpha}$ is a maximal ideal of $A(U)$, and all maximal ideals of $A(U)$ are obtained in this way.

$A(U)$ is often called the disc algebra.

18.19 The restrictions of the members of $A(U)$ to the unit circle $T$ form a closed subalgebra of $C(T)$. This is the algebra $A$ discussed in Example 18.11. In fact, $A$ is a maximal subalgebra of $C(T)$. More explicitly, if $A \subset B \subset C(T)$ and $B$ is a closed (relative to the supremum norm) subalgebra of $C(T)$, then either $B=A$ or $B=C(T)$.

It is easy to see (compare with Exercise 29, Chap. 17) that $A$ consists precisely of those $f \in C(T)$ for which

$$
\hat{f}(n)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f\left(e^{i \theta}\right) e^{-i n \theta} d \theta=0 \quad(n=-1,-2,-3, \ldots)
$$

Hence the above-mentioned maximality theorem can be stated as an approximation theorem:

18.20 Theorem Suppose $g \in C(T)$ and $\hat{g}(n) \neq 0$ for some $n<0$. Then to every $f \in C(T)$ and to every $\epsilon>0$ there correspond polynomials

$$
P_{n}\left(e^{i \theta}\right)=\sum_{k=0}^{m(n)} a_{n, k} e^{i k \theta} \quad(n=0, \ldots, N)
$$

such that

$$
\left|f\left(e^{i \theta}\right)-\sum_{n=0}^{N} P_{n}\left(e^{i \theta}\right) g^{n}\left(e^{i \theta}\right)\right|<\epsilon \quad\left(e^{i \theta} \in T\right)
$$

Proof Let $B$ be the closure in $C=C(T)$ of the set of all functions of the form

$$
\sum_{n=0}^{N} P_{n} g^{n}
$$

The theorem asserts that $B=C$. Let us assume $B \neq C$.

The set of all functions (3) (note that $N$ is not fixed) is a complex algebra. Its closure $B$ is a Banach algebra which contains the function $f_{0}$, where $f_{0}\left(e^{i \theta}\right)=e^{i \theta}$. Our assumption that $B \neq C$ implies that $1 / f_{0} \notin B$, for otherwise $B$ would contain $f_{0}^{n}$ for all integers $n$, hence all trigonometric polynomials would be in $B$; and since the trigonometric polynomials are dense in $C$ (Theorem 4.25) we should have $B=C$.

So $f_{0}$ is not invertible in $B$. By Theorem 18.17 there is a complex homomorphism $h$ of $B$ such that $h\left(f_{0}\right)=0$. Every homomorphism onto the complex field satisfies $h(1)=1$; and since $h\left(f_{0}\right)=0$, we also have

$$
h\left(f_{0}^{n}\right)=\left[h\left(f_{0}\right)\right]^{n}=0 \quad(n=1,2,3, \ldots)
$$

We know that $h$ is a linear functional on $B$, of norm at most 1 . The Hahn-Banach theorem extends $h$ to a linear functional on $C$ (still denoted by $h)$ of the same norm. Since $h(1)=1$ and $\|h\| \leq 1$, the argument used in Sec. 5.22 shows that $h$ is a positive linear functional on $C$. In particular, $h(f)$ is real for real $f$; hence $h(\bar{f})=\bar{h}(f)$. Since $f_{0}^{-n}$ is the complex conjugate of $f_{0}^{n}$, it follows that (4) also holds for $n=-1,-2,-3, \ldots$ Thus

$$
h\left(f_{0}^{n}\right)= \begin{cases}1 & \text { if } n=0 \\ 0 & \text { if } n \neq 0\end{cases}
$$

Since the trigonometric polynomials are dense in $C$, there is only one bounded linear functional on $C$ which satisfies (5). Hence $h$ is given by the formula

$$
h(f)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f\left(e^{i \theta}\right) d \theta \quad(f \in C)
$$

Now if $n$ is a positive integer, $g f_{0}^{n} \in B$; and since $h$ is multiplicative on $B$, (6) gives

$$
\hat{g}(-n)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} g\left(e^{i \theta}\right) e^{i n \theta} d \theta=h\left(g f_{0}^{n}\right)=h(g) h\left(f_{0}^{n}\right)=0,
$$

by (5). This contradicts the hypothesis of the theorem.

We conclude with a theorem due to Wiener.

18.21 Theorem Suppose

$$
f\left(e^{i \theta}\right)=\sum_{-\infty}^{\infty} c_{n} e^{i n \theta}, \quad \sum_{-\infty}^{\infty}\left|c_{n}\right|<\infty
$$

and $f\left(e^{i \theta}\right) \neq 0$ for every real $\theta$. Then

$$
\frac{1}{f\left(e^{i \theta}\right)}=\sum_{-\infty}^{\infty} \gamma_{n} e^{i n \theta} \quad \text { with } \quad \sum_{-\infty}^{\infty}\left|\gamma_{n}\right|<\infty
$$

Proof We let $A$ be the space of all complex functions $f$ on the unit circle which satisfy (1), with the norm

$$
\|f\|=\sum_{-\infty}^{\infty}\left|c_{n}\right|
$$

It is clear that $A$ is a Banach space. In fact, $A$ is isometrically isomorphic to $\ell^{1}$, the space of all complex functions on the integers which are integrable with respect to the counting measure. But $A$ is also a commutative Banach algebra, under pointwise multiplication. For if $g \in A$ and $g\left(e^{i \theta}\right)=\Sigma b_{n} e^{i n \theta}$, then

$$
f\left(e^{i \theta}\right) g\left(e^{i \theta}\right)=\sum_{n}\left(\sum_{k} c_{n-k} b_{k}\right) e^{i n \theta}
$$

and hence

$$
\|f g\|=\sum_{n}\left|\sum_{k} c_{n-k} b_{k}\right| \leq \sum_{k}\left|b_{k}\right| \sum_{n}\left|c_{n-k}\right|=\|f\| \cdot\|g\|
$$

Also, the function 1 is the unit of $A$, and $\|1\|=1$.

Put $f_{0}\left(e^{i \theta}\right)=e^{i \theta}$, as before. Then $f_{0} \in A, 1 / f_{0} \in A$, and $\left\|f_{0}^{n}\right\|=1$ for $n=0$, $\pm 1, \pm 2, \ldots$ If $h$ is any complex homomorphism of $A$ and $h\left(f_{0}\right)=\lambda$, the fact that $\|h\| \leq 1$ implies that

$$
\left|\lambda^{n}\right|=\left|h\left(f_{0}^{n}\right)\right| \leq\left\|f_{0}^{n}\right\|=1 \quad(n=0, \pm 1, \pm 2, \ldots)
$$

Hence $|\lambda|=1$. In other words, to each $h$ corresponds a point $e^{i \alpha} \in T$ such that $h\left(f_{0}\right)=e^{i \alpha}$, so

$$
h\left(f_{0}^{n}\right)=e^{i n \alpha}=f_{0}^{n}\left(e^{i \alpha}\right) \quad(n=0, \pm 1, \pm 2, \ldots)
$$

If $f$ is given by (1), then $f=\Sigma c_{n} f_{0}^{n}$. This series converges in $A$; and since $h$ is a continuous linear functional on $A$, we conclude from (7) that

$$
h(f)=f\left(e^{i \alpha}\right) \quad(f \in A)
$$

Our hypothesis that $f$ vanishes at no point of $T$ says therefore that $f$ is not in the kernel of any complex homomorphism of $A$, and now Theorem 18.17 implies that $f$ is invertible in $A$. But this is precisely what the theorem asserts.

## Exercises

1 Suppose $B(X)$ is the algebra of all bounded linear operators on the Banach space $X$, with

$$
\left(A_{1}+A_{2}\right)(x)=A_{1} x+A_{2} x, \quad\left(A_{1} A_{2}\right)(x)=A_{1}\left(A_{2} x\right), \quad\|A\|=\sup \frac{\|A x\|}{\|x\|}
$$

if $A, A_{1}$, and $A_{2} \in B(X)$. Prove that $B(X)$ is a Banach algebra.

2 Let $n$ be a positive integer, let $X$ be the space of all complex $n$-tuples (normed in any way, as long as the axioms for a normed linear space are satisfied), and let $B(X)$ be as in Exercise 1. Prove that the spectrum of each member of $B(X)$ consists of at most $n$ complex numbers. What are they?

3 Take $X=L^{2}(-\infty, \infty)$, suppose $\varphi \in L^{\infty}(-\infty, \infty)$, and let $M$ be the multiplication operator which takes $f \in L^{2}$ to $\varphi f$. Show that $M$ is a bounded linear operator on $L^{2}$ and that the spectrum of $M$ is equal to the essential range of $\varphi$ (Chap. 3, Exercise 19).

4 What is the spectrum of the shift operator on $\ell^{2}$ ? (See Sec. 17.20 for the definition.)

5 Prove that the closure of an ideal in a Banach algebra is an ideal.

6 If $X$ is a compact Hausdorff space, find all maximal ideals in $C(X)$.

7 Suppose $A$ is a commutative Banach algebra with unit, which is generated by a single element $x$. This means that the polynomials in $x$ are dense in $A$. Prove that the complement of $\sigma(x)$ is a connected subset of the plane. Hint: If $\lambda \notin \sigma(x)$, there are polynomials $P_{n}$ such that $P_{n}(x) \rightarrow(x-\lambda e)^{-1}$ in $A$. Prove that $P_{n}(z) \rightarrow(z-\lambda)^{-1}$ uniformly for $z \in \sigma(x)$.

8 Suppose $\sum_{0}^{\infty}\left|c_{n}\right|<\infty, f(z)=\sum_{0}^{\infty} c_{n} z^{n},|f(z)|>0$ for every $z \in \bar{U}$, and $1 / f(z)=\sum_{0}^{\infty} a_{n} z^{n}$. Prove that $\sum_{0}^{\infty}\left|a_{n}\right|<\infty$.

9 Prove that a closed linear subspace of the Banach algebra $L^{1}\left(R^{1}\right)$ (see Sec. 9.19) is translation invariant if and only if it is an ideal.

10 Show that $L^{1}(T)$ is a commutative Banach algebra (without unit) if multiplication is defined by

$$
(f * g)(t)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} f(t-s) g(s) d s
$$

Find all complex homomorphisms of $L^{1}(T)$, as in Theorem 9.23. If $E$ is a set of integers and if $I_{E}$ is the set of all $f \in L^{1}(T)$ such that $\hat{f}(n)=0$ for all $n \in E$, prove that $I_{E}$ is a closed ideal in $L^{1}(T)$, and prove that every closed ideal in $L^{1}(T)$ is obtained in this manner.

11 The resolvent $R(\lambda, x)$ of an element $x$ in a Banach algebra with unit is defined as

$$
R(\lambda, x)=(\lambda e-x)^{-1}
$$

for all complex $\lambda$ for which this inverse exists. Prove the identity

$$
R(\lambda, x)-R(\mu, x)=(\mu-\lambda) R(\lambda) R(\mu)
$$

and use it to give an alternative proof of Theorem 18.5.

12 Let $A$ be a commutative Banach algebra with unit. The radical of $A$ is defined to be the intersection of all maximal ideals of $A$. Prove that the following three statements about an element $x \in A$ are equivalent:

(a) $x$ is in the radical of $A$.

(b) $\lim \left\|x^{n}\right\|^{1 / n}=0$.

$\lim _{n \rightarrow \infty}$

(c) $h(x)=0$ for every complex homomorphism of $A$.

13 Find an element $x$ in a Banach algebra $A$ (for instance, a bounded linear operator on a Hilbert space) such that $x^{n} \neq 0$ for all $n>0$, but $\lim _{n \rightarrow 0}\left\|x^{n}\right\|^{1 / n}=0$.

14 Suppose $A$ is a commutative Banach algebra with unit, and let $\Delta$ be the set of all complex homomorphisms of $A$, as in Sec. 18.16. Associate with each $x \in A$ a function $\hat{x}$ on $\Delta$ by the formula

$$
\hat{x}(h)=h(x) \quad(h \in \Delta)
$$

$\hat{x}$ is called the Gelfand transform of $x$.

Prove that the mapping $x \rightarrow \hat{x}$ is a homomorphism of $A$ onto an algebra $\hat{A}$ of complex functions on $\Delta$, with pointwise multiplication. Under what condition on $A$ is this homomorphism an isomorphism? (See Exercise 12.)

Prove that the spectral radius $\rho(x)$ is equal to

$$
\|\hat{x}\|_{\infty}=\sup \{|\hat{x}(h)|: h \in \Delta\}
$$

Prove that the range of the function $\hat{x}$ is exactly the spectrum $\sigma(x)$.

15 If $A$ is a commutative Banach algebra without unit, let $A_{1}$ be the algebra of all ordered pairs $(x, \lambda)$, with $x \in A$ and $\lambda$ a complex number; addition and multiplication are defined in the "obvious" way, and $\|(x, \lambda)\|=\|x\|+|\lambda|$. Prove that $A_{1}$ is a commutative Banach algebra with unit and the mapping $x \rightarrow(x, 0)$ is an isometric isomorphism of $A$ onto a maximal ideal of $A_{1}$. This is a standard embedding of an algebra without unit in one with unit.

16 Show that $H^{\infty}$ is a commutative Banach algebra with unit, relative to the supremum norm and pointwise addition and multiplication. The mapping $f \rightarrow f(\alpha)$ is a complex homomorphism of $H^{\infty}$, whenever $|\alpha|<1$. Prove that there must be others.

17 Show that the set of all functions $(z-1)^{2} f$, where $f \in H^{\infty}$, is an ideal in $H^{\infty}$ which is not closed. Hint:

$$
\left|(1-z)^{2}(1+\epsilon-z)^{-1}-(1-z)\right|<\epsilon \quad \text { if }|z|<1, \epsilon>0
$$

18 Suppose $\varphi$ is an inner function. Prove that $\left\{\varphi f: f \in H^{\infty}\right\}$ is a closed ideal in $H^{\infty}$. In other words, prove that if $\left\{f_{n}\right\}$ is a sequence in $H^{\infty}$ such that $\varphi f_{n} \rightarrow g$ uniformly in $U$, then $g / \varphi \in H^{\infty}$.

## HOLOMORPHIC FOURIER TRANSFORMS

## Introduction

19.1 In Chap. 9 the Fourier transform of a function $f$ on $R^{1}$ was defined to be a function $\hat{f}$ on $R^{1}$. Frequently $\hat{f}$ can be extended to a function which is holomorphic in a certain region of the plane. For instance, if $f(t)=e^{-|t|}$, then $\hat{f}(x)=$ $\left(1+x^{2}\right)^{-1}$, a rational function. This should not be too surprising. For each real $t$, the kernel $e^{i t z}$ is an entire function of $z$, so one should expect that there are conditions on $f$ under which $\hat{f}$ will be holomorphic in certain regions.

We shall describe two classes of holomorphic functions which arise in this manner.

For the first one, let $F$ be any function in $L^{2}(-\infty, \infty)$ which vanishes on $(-\infty, 0)$ [i.e., take $\left.F \in L^{2}(0, \infty)\right]$ and define

$$
f(z)=\int_{0}^{\infty} F(t) e^{i t z} d t \quad\left(z \in \Pi^{+}\right)
$$

where $\Pi^{+}$is the set of all $z=x+i y$ with $y>0$. If $z \in \Pi^{+}$, then $\left|e^{i t z}\right|=e^{-t y}$, which shows that the integral in (1) exists as a Lebesgue integral.

If $\operatorname{Im} z>\delta>0, \operatorname{Im} z_{n}>\delta$, and $z_{n} \rightarrow z$, the dominated convergence theorem shows that

$$
\lim _{n \rightarrow \infty} \int_{0}^{\infty}\left|\exp \left(i t z_{n}\right)-\exp (i t z)\right|^{2} d t=0
$$

because the integrand is bounded by the $L^{1}$-function $4 \exp (-2 \delta t)$ and tends to 0 for every $t>0$. The Schwarz inequality implies therefore that $f$ is continuous in $\Pi^{+}$. The theorems of Fubini and Cauchy show that $\int_{\gamma} f(z) d z=0$ for every closed path $\gamma$ in $\Pi^{+}$. By Morera's theorem, $f \in H\left(\Pi^{+}\right)$.

Let us rewrite (1) in the form

$$
f(x+i y)=\int_{0}^{\infty} F(t) e^{-t y} e^{i t x} d t
$$

regard $y$ as fixed, and apply Plancherel's theorem. We obtain

$$
\frac{1}{2 \pi} \int_{-\infty}^{\infty}|f(x+i y)|^{2} d x=\int_{0}^{\infty}|F(t)|^{2} e^{-2 t y} d t \leq \int_{0}^{\infty}|F(t)|^{2} d t
$$

for every $y>0$. [Note that our notation now differs from that in Chap. 9. There the underlying measure was Lebesgue measure divided by $\sqrt{2 \pi}$. Here we just use Lebesgue measure. This accounts for the factor $1 /(2 \pi)$ in (3).] This shows:

(a) If $f$ is of the form (1), then $f$ is holomorphic in $\Pi^{+}$and its restrictions to horizontal lines in $\Pi^{+}$form a bounded set in $L^{2}(-\infty, \infty)$.

Our second class consists of all $f$ of the form

$$
f(z)=\int_{-A}^{A} F(t) e^{i t z} d t
$$

where $0<A<\infty$ and $F \in L^{2}(-A, A)$. These functions $f$ are entire (the proof is the same as above), and they satisfy a growth condition:

$$
|f(z)| \leq \int_{-A}^{A}|F(t)| e^{-t y} d t \leq e^{A|y|} \int_{-A}^{A}|F(t)| d t
$$

If $C$ is this last integral, then $C<\infty$, and (5) implies that

$$
|f(z)| \leq C e^{A|z|}
$$

[Entire functions which satisfy (6) are said to be of exponential type.] Thus:

(b) Every $f$ of the form (4) is an entire function which satisfies (6) and whose restriction to the real axis lies in $L^{2}$ (by the Plancherel theorem).

It is a remarkable fact that the converses of $(a)$ and $(b)$ are true. This is the content of Theorems 19.2 and 19.3.

## Two Theorems of Paley and Wiener

19.2 Theorem Suppose $f \in H\left(\Pi^{+}\right)$and

$$
\sup _{0<y<\infty} \frac{1}{2 \pi} \int_{-\infty}^{\infty}|f(x+i y)|^{2} d x=C<\infty
$$

Then there exists an $F \in L^{2}(0, \infty)$ such that

$$
f(z)=\int_{0}^{\infty} F(t) e^{i t z} d t \quad\left(z \in \Pi^{+}\right)
$$

and

$$
\int_{0}^{\infty}|F(t)|^{2} d t=C
$$

Note: The function $F$ we are looking for is to have the property that $f(x+i y)$ is the Fourier transform of $F(t) e^{-y t}$ (we regard $y$ as a positive constant). Let us apply the inversion formula (whether or not this is correct does not matter; we are trying to motivate the proof that follows): The desired $F$ should be of the form

$$
F(t)=e^{t y} \cdot \frac{1}{2 \pi} \int_{-\infty}^{\infty} f(x+i y) e^{-i t x} d x=\frac{1}{2 \pi} \int f(z) e^{-i t z} d z
$$

The last integral is over a horizontal line in $\Pi^{+}$, and if this argument is correct at all, the integral will not depend on the particular line we happen to choose. This suggests that the Cauchy theorem should be invoked.

ProOF Fix $y, 0<y<\infty$. For each $\alpha>0$ let $\Gamma_{\alpha}$ be the rectangular path with vertices at $\pm \alpha+i$ and $\pm \alpha+i y$. By Cauchy's theorem

$$
\int_{\Gamma_{\alpha}} f(z) e^{-i t z} d z=0
$$

We consider only real values of $t$. Let $\Phi(\beta)$ be the integral of $f(z) e^{-i t z}$ over the straight line interval from $\beta+i$ to $\beta+i y$ ( $\beta$ real). Put $I=[y, 1]$ if $y<1$, $I=[1, y]$ if $1<y$. Then

$$
|\Phi(\beta)|^{2}=\left|\int_{I} f(\beta+i u) e^{-i t(\beta+i u)} d u\right|^{2} \leq \int_{I}|f(\beta+i u)|^{2} d u \int_{I} e^{2 t u} d u
$$

Put

$$
\Lambda(\beta)=\int_{I}|f(\beta+i u)|^{2} d u
$$

Then (1) shows, by Fubini's theorem, that

$$
\frac{1}{2 \pi} \int_{-\infty}^{\infty} \Lambda(\beta) d \beta \leq C m(I)
$$

Hence there is a sequence $\left\{\alpha_{j}\right\}$ such that $\alpha_{j} \rightarrow \infty$ and

$$
\Lambda\left(\alpha_{j}\right)+\Lambda\left(-\alpha_{j}\right) \rightarrow 0 \quad(j \rightarrow \infty)
$$

By (6), this implies that

$$
\Phi\left(\alpha_{j}\right) \rightarrow 0, \quad \Phi\left(-\alpha_{j}\right) \rightarrow 0 \quad \text { as } j \rightarrow \infty
$$

Note that this holds for every $t$ and that the sequence $\left\{\alpha_{j}\right\}$ does not depend on $t$.

Let us define

$$
g_{j}(y, t)=\frac{1}{2 \pi} \int_{-\alpha_{j}}^{\alpha_{j}} f(x+i y) e^{-i t x} d x
$$

Then we deduce from (5) and (10) that

$$
\lim _{j \rightarrow \infty}\left[e^{t y} g_{j}(y, t)-e^{t} g_{j}(1, t)\right]=0 \quad(-\infty<t<\infty)
$$

Write $f_{y}(x)$ for $f(x+i y)$. Then $f_{y} \in L^{2}(-\infty, \infty)$, ty hypothesis, and the Plancherel theorem asserts that

$$
\lim _{j \rightarrow \infty} \int_{-\infty}^{\infty}\left|\hat{f}_{y}(t)-g_{j}(y, t)\right|^{2} d t=0
$$

where $\hat{f}_{y}$ is the Fourier transform of $f_{y}$. A subsequence of $\left\{g_{j}(y, t)\right\}$ converges therefore pointwise to $\hat{f}_{y}(t)$, for almost all $t$ (Theorem 3.12). If we define

$$
F(t)=e^{t} \hat{f}_{1}(t)
$$

it now follows from (12) that

$$
F(t)=e^{t y} \hat{f}_{y}(t)
$$

Note that (14) does not involve $y$ and that (15) holds for every $y \in(0, \infty)$. Plancherel's theorem can be applied to (15):

$$
\int_{-\infty}^{\infty} e^{-2 t y}|F(t)|^{2} d t=\int_{-\infty}^{\infty}\left|\hat{f}_{y}(t)\right|^{2} d t=\frac{1}{2 \pi} \int_{-\infty}^{\infty}\left|f_{y}(x)\right|^{2} d x \leq C .
$$

If we let $y \rightarrow \infty,(16)$ shows that $F(t)=0$ a.e. in $(-\infty, 0)$.

If we let $y \rightarrow 0,(16)$ shows that

$$
\int_{0}^{\infty}|F(t)|^{2} d t \leq C
$$

It now follows from (15) that $\hat{f}_{y} \in L^{1}$ if $y>0$. Hence Theorem 9.14 gives

$$
f_{y}(x)=\int_{-\infty}^{\infty} \hat{f}_{y}(t) e^{i t x} d t
$$

or

$$
f(z)=\int_{0}^{\infty} F(t) e^{-y t} e^{i t x} d t=\int_{0}^{\infty} F(t) e^{i t z} d t \quad\left(z \in \Pi^{+}\right) .
$$

This is (2), and now (3) follows from (17) and formula 19.13).

19.3 Theorem Suppose $A$ and $C$ are positive constants and $f$ is an entire function such that

$$
|f(z)| \leq C e^{A|z|}
$$

for all $z$, and

$$
\int_{-\infty}^{\infty}|f(x)|^{2} d x<\infty
$$

Then there exists an $F \in L^{2}(-A, A)$ such that

$$
f(z)=\int_{-A}^{A} F(t) e^{i t z} d t
$$

for all $z$.

Proof Put $f_{\epsilon}(x)=f(x) e^{-\epsilon|x|}$, for $\epsilon>0$ and $x$ real. We shall show that

$$
\lim _{\epsilon \rightarrow 0} \int_{-\infty}^{\infty} f_{\epsilon}(x) e^{-i t x} d x=0 \quad(t \text { real, }|t|>A)
$$

Since $\left\|f_{\epsilon}-f\right\|_{2} \rightarrow 0$ as $\epsilon \rightarrow 0$, the Plancherel theorem implies that the Fourier transforms of $f_{\epsilon}$ converge in $L^{2}$ to the Fourier transform $F$ of $f$ (more precisely, of the restriction of $f$ to the real axis). Hence (4) will imply that $F$ vanishes outside $[-A, A]$, and then Theorem 9.14 shows that (3) holds for almost every real $z$. Since each side of (3) is an entire function, it follows that (3) holds for every complex $z$.

Thus (4) implies the theorem.

For each real $\alpha$, let $\Gamma_{\alpha}$ be the path defined by

$$
\Gamma_{\alpha}(s)=s e^{i \alpha} \quad(0 \leq s<\infty)
$$

put

$$
\Pi_{\alpha}=\left\{w: \operatorname{Re}\left(w e^{i \alpha}\right)>A\right\},
$$

and if $w \in \Pi_{\alpha}$, define

$$
\Phi_{\alpha}(w)=\int_{\Gamma_{\alpha}} f(z) e^{-w z} d z=e^{i \alpha} \int_{0}^{\infty} f\left(s e^{i \alpha}\right) \exp \left(-w s e^{i \alpha}\right) d s
$$

By (1) and (5), the absolute value of the integrand is at most

$$
C \exp \left\{-\left[\operatorname{Re}\left(w e^{i \alpha}\right)-A\right] s\right\},
$$

and it follows (as in Sec. 19.1) that $\Phi_{\alpha}$ is holomorphic in the half plane $\Pi_{\alpha}$.

However, more is true if $\alpha=0$ and if $\alpha=\pi$ : We have

$$
\Phi_{0}(w)=\int_{0}^{\infty} f(x) e^{-w x} d x \quad(\operatorname{Re} w>0)
$$

$$
\Phi_{\pi}(w)=-\int_{-\infty}^{0} f(x) e^{-w x} d x \quad(\operatorname{Re} w<0)
$$

$\Phi_{0}$ and $\Phi_{\pi}$ are holomorphic in the indicated half planes because of (2).

The significance of the functions $\Phi_{\alpha}$ to (4) lies in the easily verified relation

$$
\int_{-\infty}^{\infty} f_{\epsilon}(x) e^{-i t x} d x=\Phi_{0}(\epsilon+i t)-\Phi_{\pi}(-\epsilon+i t) \quad(t \text { real })
$$

Hence we have to prove that the right side of (10) tends to 0 as $\epsilon \rightarrow 0$, if $t>A$ and if $t<-A$.

We shall do this by showing that any two of our functions $\Phi_{\alpha}$ agree in the intersection of their domains of definition, i.e., that they are analytic continuations of each other. Once this is done, we can replace $\Phi_{0}$ and $\Phi_{\pi}$ by $\Phi_{\pi / 2}$ in (10) if $t<-A$, and by $\Phi_{-\pi / 2}$ if $t>A$, and it is then obvious that the difference tends to 0 as $\epsilon \rightarrow 0$.

So suppose $0<\beta-\alpha<\pi$. Put

$$
\gamma=\frac{\alpha+\beta}{2}, \quad \eta=\cos \frac{\beta-\alpha}{2}>0
$$

If $w=|w| e^{-i \gamma}$, then

$$
\operatorname{Re}\left(w e^{i \alpha}\right)=\eta|w|=\operatorname{Re}\left(w e^{i \beta}\right)
$$

so that $w \in \Pi_{\alpha} \cap \Pi_{\beta}$ as soon as $|w|>A / \eta$. Consider the integral

$$
\int_{\Gamma} f(z) e^{-w z} d z
$$

over the circular arc $\Gamma$ given by $\Gamma(t)=r e^{i t}, \alpha \leq t \leq \beta$. Since

$$
\operatorname{Re}(-w z)=-|w| r \cos (t-\gamma) \leq-|w| r \eta
$$

the absolute value of the integrand in (13) does not exceed

$$
C \exp \{(A-|w| \eta) r\}
$$

If $|w|>A / \eta$ it follows that (13) tends to 0 as $r \rightarrow \infty$.

We now apply the Cauchy theorem. The integral of $f(z) e^{-w z}$ over the interval $\left[0, r e^{i \beta}\right]$ is equal to the sum of $(13)$ and the integral over $\left[0, r e^{i x}\right]$. Since (13) tends to 0 as $r \rightarrow \infty$, we conclude that $\Phi_{\alpha}(w)=\Phi_{\beta}(w)$ if $w=|w| e^{-i \gamma}$ and $|w|>A / \eta$, and then Theorem 10.18 shows that $\Phi_{\alpha}$ and $\Phi_{\beta}$ coincide in the intersection of the half planes in which they were originally defined.

This completes the proof.

19.4 Remarks Each of the two preceding proofs depended on a typical application of Cauchy's theorem. In Theorem 19.2 we replaced integration over one horizontal line by integration over another to show that 19.2(15) was
independent of $y$. In Theorem 19.3, replacement of one ray by another was used to construct analytic continuations; the result actually was that the functions $\Phi_{\alpha}$ are restrictions of one function $\Phi$ which is holomorphic in the complement of the interval $[-A i, A i]$.

The class of functions described in Theorem 19.2 is the half plane analogue of the class $H^{2}$ discussed in Chap. 17. Theorem 19.3 will be used in the proof of the Denjoy-Carleman theorem (Theorem 19.11).

## Quasi-analytic Classes

19.5 If $\Omega$ is a region and if $z_{0} \in \Omega$, every $f \in H(\Omega)$ is uniquely determined by the numbers $f\left(z_{0}\right), f^{\prime}\left(z_{0}\right), f^{\prime \prime}\left(z_{0}\right), \ldots$ On the other hand, there exist infinitely differentiable functions on $R^{1}$ which are not identically 0 but which vanish on some interval. Thus we have here a uniqueness property which holomorphic functions possess but which does not hold in $C^{\infty}$ (the class of all infinitely differentiable complex functions on $R^{1}$ ).

If $f \in H(\Omega)$, the growth of the sequence $\left\{\left|f^{(n)}\left(z_{0}\right)\right|\right\}$ is restricted by Theorem 10.26. It is therefore reasonable to ask whether the above uniqueness property holds in suitable subclasses of $C^{\infty}$ in which the growth of the derivatives is subject to some restrictions. This motivates the following definitions; the answer to our question is given by Theorem 19.11.

19.6 The Classes $C\left\{M_{n}\right\}$ If $M_{0}, M_{1}, M_{2}, \ldots$ are positive numbers, we let $C\left\{M_{n}\right\}$ be the class of all $f \in C^{\infty}$ which satisfy inequalities of the form

$$
\left\|D^{n} f\right\|_{\infty} \leq \beta_{f} B_{f}^{n} M_{n} \quad(n=0,1,2, \ldots)
$$

Here $D^{0} f=f, D^{n} f$ is the $n$th derivative of $f$ if $n \geq 1$, the norm is the supremum norm over $R^{1}$, and $\beta_{f}$ and $B_{f}$ are positive constants (depending on $f$, but not on n).

If $f$ satisfies (1), then

$$
\limsup _{n \rightarrow \infty}\left\{\frac{\left\|D^{n} f\right\|_{\infty}}{M_{n}}\right\}^{1 / n} \leq B_{f}
$$

This shows that $B_{f}$ is a more significant quantity than $\beta_{f}$. However, if $\beta_{f}$ were omitted in (1), the case $n=0$ would imply $\|f\|_{\infty} \leq M_{0}$, an undesirable restriction. The inclusion of $\beta_{f}$ makes $C\left\{M_{n}\right\}$ into a vector space.

Each $C\left\{M_{n}\right\}$ is invariant under affine transformations. More explicitly, suppose $f \in C\left\{M_{n}\right\}$ and $g(x)=f(a x+b)$. Then $g$ satisfies (1), with $\beta_{g}=\beta_{f}$ and $B_{g}=a B_{f}$.

We shall make two standing assumptions on the sequences $\left\{M_{n}\right\}$ under consideration:

$$
\begin{aligned}
& M_{0}=1 \\
& M_{n}^{2} \leq M_{n-1} M_{n+1} \quad(n=1,2,3, \ldots) .
\end{aligned}
$$

Assumption (4) can be expressed in the form: $\left\{\log M_{n}\right\}$ is a convex sequence.

These assumptions will simplify some of our work, and they involve no loss of generality. [One can prove, although we shall not do so, that every class $C\left\{M_{n}\right\}$ is equal to a class $C\left\{\bar{M}_{n}\right\}$, where $\left\{\bar{M}_{n}\right\}$ satisfies (3) and (4).]

The following result illustrates the utility of (3) and (4):

19.7 Theorem Each $C\left\{M_{n}\right\}$ is an algebra, with respect to pointwise multiplication.

Proof Suppose $f$ and $g \in C\left\{M_{n}\right\}$, and $\beta_{f}, B_{f}, \beta_{g}$, and $B_{g}$ are the corresponding constants. The product rule for differentiation shows that

$$
D^{n}(f g)=\sum_{j=0}^{n}\left(\begin{array}{l}
n \\
j
\end{array}\right)\left(D^{j} f\right) \cdot\left(D^{n-j} g\right)
$$

Hence

$$
\left|D^{n}(f g)\right| \leq \beta_{f} \beta_{g} \sum_{j=0}^{n}\left(\begin{array}{l}
n \\
j
\end{array}\right) B_{f}^{j} B_{g}^{n-j} M_{j} M_{n-j}
$$

The convexity of $\left\{\log M_{n}\right\}$, combined with $M_{0}=1$, shows that $M_{j} M_{n-j} \leq$ $M_{n}$ for $0 \leq j \leq n$. Hence the binomial theorem leads from (2) to

$$
\left\|D^{n}(f g)\right\|_{\infty} \leq \beta_{f} \beta_{g}\left(B_{f}+B_{g}\right)^{n} M_{n} \quad(n=0,1,2, \ldots)
$$

so that $f g \in C\left\{M_{n}\right\}$.

19.8 Definition A class $C\left\{M_{n}\right\}$ is said to be quasi-analytic if the conditions

$$
f \in C\left\{M_{n}\right\}, \quad\left(D^{n} f\right)(0)=0 \quad(\text { for } n=0,1,2, \ldots)
$$

imply that $f(x)=0$ for all $x \in R^{1}$.

The content of the definition is of course unchanged if $\left(D^{n} f\right)(0)$ is replaced by $\left(D^{n} f\right)\left(x_{0}\right)$, where $x_{0}$ is any given point.

The quasi-analytic classes are thus the ones which have the uniqueness property we mentioned in Sec. 19.6. One of these classes is very intimately related to holomorphic functions:

19.9 Theorem The class $C\{n !\}$ consists of all $f$ to which there corresponds a $\delta>0$ such that $f$ can be extended to a bounded holomorphic function in the strip defined by $|\operatorname{Im}(z)|<\delta$.

Consequently $C\{n !\}$ is a quasi-analytic class.

Proof Suppose $f \in H(\Omega)$ and $|f(z)|<\beta$ for all $z \in \Omega$, where $\Omega$ consists of all $z=x+i y$ with $|y|<\delta$. It follows from Theorem 10.26 that

$$
\left|\left(D^{n} f\right)(x)\right| \leq \beta \delta^{-n} n ! \quad(n=0,1,2, \ldots)
$$

for all real $x$. The restriction of $f$ to the real axis therefore belongs to $C\{n !\}$.
words,

Conversely, suppose $f$ is defined on the real axis and $f \in C\{n !\}$. In other

$$
\left\|D^{n} f\right\|_{\infty} \leq \beta B^{n} n ! \quad(n=0,1,2, \ldots)
$$

We claim that the representation

$$
f(x)=\sum_{n=0}^{\infty} \frac{\left(D^{n} f\right)(a)}{n !}(x-a)^{n}
$$

is valid for all $a \in R^{1}$ if $a-B^{-1}<x<a+B^{-1}$. This follows from Taylor's formula

$$
f(x)=\sum_{j=0}^{n-1} \frac{\left(D^{j} f\right)(a)}{j !}(x-a)^{j}+\frac{1}{(n-1) !} \int_{a}^{x}(x-t)^{n-1}\left(D^{n} f\right)(t) d t
$$

which one obtains by repeated integrations by part. By (2) the last term in (4) (the "remainder") is dominated by

$$
n \beta B^{n}\left|\int_{a}^{x}(x-t)^{n-1} d t\right|=\beta|B(x-a)|^{n}
$$

If $|B(x-a)|<1$, this tends to 0 as $n \rightarrow \infty$, and (3) follows.

We can now replace $x$ in (3) by any complex number $z$ such that $|z-a|<1 / B$. This defines a holomorphic function $F_{a}$ in the disc with center at $a$ and radius $1 / B$, and $F_{a}(x)=f(x)$ if $x$ is real and $|x-a|<1 / B$. The various functions $F_{a}$ are therefore analytic continuations of each other; they form a holomorphic extension $F$ of $f$ in the strip $|y|<1 / B$.

If $0<\delta<1 / B$ and $z=a+i y,|y|<\delta$, then

$$
|F(z)|=\left|F_{a}(z)\right|=\left|\sum_{n=0}^{\infty} \frac{\left(D^{n} f\right)(a)}{n !}(i y)^{n}\right| \leq \beta \sum_{n=0}^{\infty}(B \delta)^{n}=\frac{\beta}{1-B \delta}
$$

This shows that $F$ is bounded in the strip $|y|<\delta$, and the proof is complete.

19.10 Theorem The class $C\left\{M_{n}\right\}$ is quasi-analytic if and only if $C\left\{M_{n}\right\}$ contains no nontrivial function with compact support.

ProOF If $C\left\{M_{n}\right\}$ is quasi-analytic, if $f \in C\left\{M_{n}\right\}$, and if $f$ has compact support, then evidently $f$ and all its derivatives vanish at some point, hence $f(x)=0$ for all $x$.

Suppose $C\left\{M_{n}\right\}$ is not quasi-analytic. Then there exists an $f \in C\left\{M_{n}\right\}$ such that $\left(D^{n} f\right)(0)=0$ for $n=0,1,2, \ldots$, but $f\left(x_{0}\right) \neq 0$ for some $x_{0}$. We may assume $x_{0}>0$. If $g(x)=f(x)$ for $x \geq 0$ and $g(x)=0$ for $x<0$, then $g \in$ $C\left\{M_{n}\right\}$. Put $h(x)=g(x) g\left(2 x_{0}-x\right)$. By Theorem 19.7, $h \in C\left\{M_{n}\right\}$. Also, $h(x)=0$ if $x<0$ and if $x>2 x_{0}$. But $h\left(x_{0}\right)=f^{2}\left(x_{0}\right) \neq 0$. Thus $h$ is a nontrivial member of $C\left\{M_{n}\right\}$ with compact support.

We are now ready for the fundamental theorem about quasi-analytic clases.

## The Denjoy-Carleman Theorem

19.11 Theorem Suppose $M_{0}=1, M_{n}^{2} \leq M_{n-1} M_{n+1}$ for $n=1,2,3, \ldots$, and

$$
Q(x)=\sum_{n=0}^{\infty} \frac{x^{n}}{M_{n}}, \quad q(x)=\sup _{n \geq 0} \frac{x^{n}}{M_{n}}
$$

for $x>0$. Then each of the following five conditions implies the other four:

(a) $C\left\{M_{n}\right\}$ is not quasi-analytic.

(b) $\int_{0}^{\infty} \log Q(x) \frac{d x}{1+x^{2}}<\infty$.

(c) $\int_{0}^{\infty} \log q(x) \frac{d x}{1+x^{2}}<\infty$.

(d) $\sum_{n=1}^{\infty}\left(\frac{1}{M_{n}}\right)^{1 / n}<\infty$.

(e) $\sum_{n=1}^{\infty} \frac{M_{n-1}}{M_{n}}<\infty$.

Note: If $M_{n} \rightarrow \infty$ very rapidly as $n \rightarrow \infty$, then $Q(x)$ tends to infinity slowly as $x \rightarrow \infty$. Thus each of the five conditions says, in its own way, that $M_{n} \rightarrow \infty$ rapidly. Note also that $Q(x) \geq 1$ and $q(x) \geq 1$. The integrals in $(b)$ and $(c)$ are thus always defined. It may happen that $Q(x)=\infty$ for some $x<\infty$. In that case, the integral $(b)$ is $+\infty$, and the theorem asserts that $C\left\{M_{n}\right\}$ is quasi-analytic.

If $M_{n}=n !$, then $M_{n-1} / M_{n}=1 / n$, hence $(e)$ is violated, and the theorem asserts that $C\{n !\}$ is quasi-analytic, in accordance with Theorem 19.9.

Proof that (a) implies $(b)$ Assume that $C\left\{M_{n}\right\}$ is not quasi-analytic. Then $C\left\{M_{n}\right\}$ contains a nontrivial function with compact support (Theorem 19.10). An affine change of variable gives a function $F \in C\left\{M_{n}\right\}$, with support in some interval $[0, A]$, such that

$$
\left\|D^{n} F\right\|_{\infty} \leq 2^{-n} M_{n} \quad(n=0,1,2, \ldots)
$$

and such that $F$ is not identically zero. Define

$$
f(z)=\int_{0}^{A} F(t) e^{i t z} d t
$$

and

$$
g(w)=f\left(\frac{i-i w}{1+w}\right)
$$

Then $f$ is entire. If $\operatorname{Im} z>0$, the absolute value of the integrand in (2) is at most $|F(t)|$. Hence $f$ is bounded in the upper half plane; therefore $g$ is bounded in $U$. Also, $g$ is continuous on $\bar{U}$, except at the point $w=-1$. Since $f$ is not identically 0 (by the uniqueness theorem for Fourier transforms) the same is true of $g$, and now Theorem 15.19 shows that

$$
\frac{1}{2 \pi} \int_{-\pi}^{\pi} \log \left|g\left(e^{i \theta}\right)\right| d \theta>-\infty
$$

If $x=i\left(1-e^{i \theta}\right) /\left(1+e^{i \theta}\right)=\tan (\theta / 2)$, then $d \theta=2\left(1+x^{2}\right)^{-1} d x$, so (4) is the same as

$$
\frac{1}{\pi} \int_{-\infty}^{\infty} \log |f(x)| \frac{d x}{1+x^{2}}>-\infty
$$

On the other hand, partial integration of (2) gives

$$
f(z)=(i z)^{-n} \int_{0}^{A}\left(D^{n} F\right)(t) e^{i t z} d t \quad(z \neq 0)
$$

since $F$ and all its derivatives vanish at 0 and at $A$. It now follows from (1) and (6) that

$$
\left|x^{n} f(x)\right| \leq 2^{-n} A M_{n} \quad(x \text { real, } n=0,1,2, \ldots)
$$

Hence

$$
Q(x)|f(x)|=\sum_{n=0}^{\infty} \frac{x^{n}|f(x)|}{M_{n}} \leq 2 A \quad(x \geq 0)
$$

and (5) and (8) imply that (b) holds.

Proof That $(b)$ ImPLies $(c) q(x) \leq Q(x)$.

Proof that (c) IMPLies ( $d$ ) Put $a_{n}=M_{n}^{1 / n}$. Since $M_{0}=1$ and since $M_{n}^{2} \leq$ $M_{n-1} M_{n+1}$, it is easily verified that $a_{n} \leq a_{n+1}$, for $n>0$. If $x \geq e a_{n}$, then $x^{n} / M_{n} \geq e^{n}$, so

$$
\log q(x) \geq \log \frac{x^{n}}{M_{n}} \geq \log e^{n}=n
$$

Hence

$$
\begin{aligned}
e \int_{e a_{1}}^{\infty} \log q(x) \cdot \frac{d x}{x^{2}} & \geq e \sum_{n=1}^{N} n \int_{e a_{n}}^{e a_{n+1}} x^{-2} d x+e \int_{e a_{N+1}}^{\infty}(N+1) x^{-2} d x \\
& =\sum_{n=1}^{N} n\left(\frac{1}{a_{n}}-\frac{1}{a_{n+1}}\right)+\frac{N+1}{a_{N+1}}=\sum_{n=1}^{N+1} \frac{1}{a_{n}}
\end{aligned}
$$

for every $N$. This shows that $(c)$ implies $(d)$.

Proof that ( $d$ ) implies (e) Put

$$
\lambda_{n}=\frac{M_{n-1}}{M_{n}} \quad(n=1,2,3, \ldots)
$$

Then $\lambda_{1} \geq \lambda_{2} \geq \lambda_{3} \geq \cdots$, and if $a_{n}=M_{n}^{1 / n}$, as above, we have

$$
\left(a_{n} \lambda_{n}\right)^{n} \leq M_{n} \cdot \lambda_{1} \lambda_{2} \cdots \lambda_{n}=1
$$

Thus $\lambda_{n} \leq 1 / a_{n}$, and the convergence of $\Sigma\left(1 / a_{n}\right)$ implies that of $\Sigma \lambda_{n}$.

Proof that ( $e$ ) ImPlies (a) The assumption now is that $\Sigma \lambda_{n}<\infty$, where $\lambda_{n}$ is given by (11). We claim that the function

$$
f(z)=\left(\frac{\sin z}{z}\right)^{2} \prod_{n=1}^{\infty} \frac{\sin \lambda_{n} z}{\lambda_{n} z}
$$

is an entire function of exponential type, not identically zero, which satisfies the inequalities

$$
\left|x^{k} f(x)\right| \leq M_{k}\left(\frac{\sin x}{x}\right)^{2} \quad(x \text { real }, k=0,1,2, \ldots)
$$

Note first that $1-z^{-1} \sin z$ has a zero at the origin. Hence there is a constant $B$ such that

$$
\left|1-\frac{\sin z}{z}\right| \leq B|z| \quad(|z| \leq 1)
$$

It follows that

$$
\left|1-\frac{\sin \lambda_{n} z}{\lambda_{n} z}\right| \leq B \lambda_{n}|z| \quad\left(|z| \leq \frac{1}{\lambda_{n}}\right)
$$

so that the series

$$
\sum_{n=1}^{\infty}\left|1-\frac{\sin \lambda_{n} z}{\lambda_{n} z}\right|
$$

converges uniformly on compact sets. (Note that $1 / \lambda_{n} \rightarrow \infty$ as $n \rightarrow \infty$, since $\Sigma \lambda_{n}<\infty$.) The infinite product (13) therefore defines an entire function $f$ which is not identically zero.

Next, the identity

$$
\frac{\sin z}{z}=\frac{1}{2} \int_{-1}^{1} e^{i t z} d t
$$

shows that $\left|z^{-1} \sin z\right| \leq e^{|y|}$ if $z=x+i y$. Hence

$$
|f(z)| \leq e^{A|z|}, \quad \text { with } A=2+\sum_{n=1}^{\infty} \lambda_{n} \text {. }
$$

For real $x$, we have $|\sin x| \leq|x|$ and $|\sin x| \leq 1$. Hence

$$
\begin{aligned}
\left|x^{k} f(x)\right| & \leq\left|x^{k}\right|\left(\frac{\sin x}{x}\right)^{2} \prod_{n=1}^{k}\left|\frac{\sin }{\lambda_{n}} \frac{\lambda_{n} x}{x}\right| \\
& \leq\left(\frac{\sin x}{x}\right)^{2}\left(\lambda_{1} \cdots \lambda_{k}\right)^{-1}=M_{k}\left(\frac{\sin x}{x}\right)^{2} .
\end{aligned}
$$

This gives (14), and if we integrate (14) we obtain

$$
\frac{1}{\pi} \int_{-\infty}^{\infty}\left|x^{k} f(x)\right| d x \leq M_{k} \quad(k=0,1,2, \ldots)
$$

We have proved that $f$ satisfies the hypotheses of Theorem 19.3. The Fourier transform of $f$,

$$
F(t)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} f(x) e^{-i t x} d x \quad(t \text { real })
$$

is therefore a function with compact support, not identically zero, and (21) shows that $F \in C^{\infty}$ and that

$$
\left(D^{k} F\right)(t)=\frac{1}{2 \pi} \int_{-\infty}^{\infty}(-i x)^{k} f(x) e^{-i t x} d x
$$

by repeated application of Theorem $9.2(f)$. Hence $\left\|D^{k} F\right\|_{\infty} \leq M_{k}$, by (21), which shows that $F \in C\left\{M_{n}\right\}$.

Hence $C\left\{M_{n}\right\}$ is not quasi-analytic, and the proof is complete.

## Exercises

1 Suppose $f$ is an entire function of exponential type and

$$
\varphi(y)=\int_{-\infty}^{\infty}|f(x+i y)|^{2} d x
$$

Prove that either $\varphi(y)=\infty$ for all real $y$ or $\varphi(y)<\infty$ for all real $y$. Prove that $f=0$ if $\varphi$ is a bounded function.

2 Suppose $f$ is an entire function of exponential type such that the restriction of $f$ to two nonparallel lines belongs to $L^{2}$. Prove that $f=0$.

3 Suppose $f$ is an entire function of exponential type whose restriction to two nonparallel lines is bounded. Prove that $f$ is constant. (Apply Exercise 9 of Chap. 12.)

4 Suppose $f$ is entire, $|f(z)|<C \exp (A|z|)$, and $f(z)=\Sigma a_{n} z^{n}$. Put

$$
\Phi(w)=\sum_{n=0}^{\infty} \frac{n ! a_{n}}{w^{n+1}}
$$

Prove that the series converges if $|w|>A$, that

$$
f(z)=\frac{1}{2 \pi i} \int_{\Gamma} \Phi(w) e^{w z} d w
$$

if $\Gamma(t)=(A+\epsilon) e^{i t}, 0 \leq t \leq 2 \pi$, and that $\Phi$ is the function which occurred in the proof of Theorem 19.3. (See also Sec. 19.4.)

5 Suppose $f$ satisfies the hypothesis of Theorem 19.2. Prove that the Cauchy formula

$$
f(z)=\frac{1}{2 \pi \mathrm{i}} \int_{-\infty}^{\infty} \frac{f(\xi+\mathrm{i} \epsilon)}{\xi+i \epsilon-z} d \xi \quad(0<\epsilon<y)
$$

holds; here $z=x+i y$. Prove that

$$
f^{*}(x)=\lim _{y \rightarrow 0} f(x+\mathrm{i} y)
$$

exists for almost all $x$. What is the relation between $f^{*}$ and the function $F$ which occurs in Theorem 19.2? Is $\left(^{*}\right)$ true with $\epsilon=0$ and with $f^{*}$ in place of $f$ in the integrand?

6 Suppose $\varphi \in L^{2}(-\infty, \infty)$ and $\varphi>0$. Prove that there exists an $f$ with $|f|=\varphi$ such that the Fourier transform of $f$ vanishes on a half line if and only if

$$
\int_{-\infty}^{\infty} \log \varphi(x) \frac{d x}{1+x^{2}}>-\infty
$$

Suggestion: Consider $f^{*}$, as in Exercise 5, where $f=\exp (u+i v)$ and

$$
u(z)=\frac{1}{\pi} \int_{-\infty}^{\infty} \frac{y}{(x-t)^{2}+y^{2}} \log \varphi(t) d t
$$

7 Let $f$ be a complex function on a closed set $E$ in the plane. Prove that the following two conditions on $f$ are equivalent:

(a) There is an open set $\Omega \supset E$ and a function $F \in H(\Omega)$ such that $F(z)=f(z)$ for $z \in E$.

(b) To each $\alpha \in E$ there corresponds a neighborhood $V_{\alpha}$ of $\alpha$ and a function $F_{\alpha} \in H\left(V_{\alpha}\right)$ such that $F_{\alpha}(z)=f(z)$ in $V_{\alpha} \cap E$.

(A special case of this was proved in Theorem 19.9.)

8 Prove that $C\{n !\}=\mathcal{C}\left\{n^{n}\right\}$.

9 Prove that there are quasi-analytic classes which are larger than $C\{n !\}$.

10 Put $\lambda_{n}=M_{n-1} / M_{n}$, as in the proof of Theorem 19.11. Pick $g_{0} \in C_{c}\left(R^{1}\right)$, and define

$$
g_{n}(x)=\left(2 \lambda_{n}\right)^{-1} \int_{-\lambda_{n}}^{\lambda_{n}} g_{n-1}(x-t) d t \quad(n=1,2,3, \ldots)
$$

Prove directly (without using Fourier transforms or holomorphic functions) that $g=\lim g_{n}$ is a function which demonstrates that $(e)$ implies $(a)$ in Theorem 19.11. (You may choose any $g_{0}$ that is convenient.)

11 Find an explicit formula for a function $\varphi \in C^{\infty}$, with support in $[-2,2]$, such that $\varphi(x)=1$ if $-1 \leq x \leq 1$.

12 Prove that to every sequence $\left\{\alpha_{n}\right\}$ of complex numbers there corresponds a function $f \in C^{\infty}$ such that $\left(D^{n} f(0)=\alpha_{n}\right.$ for $n=0,1,2, \ldots$ Suggestion: If $\varphi$ is as in Exercise 11 , if $\beta_{n}=\alpha_{n} / n !$, if $g_{n}(x)=$ $\beta_{n} x^{n} \varphi(x)$, and if

$$
f_{n}(x)=\lambda_{n}^{-n} g_{n}\left(\lambda_{n} x\right)=\beta_{n} x^{n} \varphi\left(\lambda_{n} x\right)
$$

then $\left\|D^{k} f_{n}\right\|_{\infty}<2^{-n}$ for $k=0, \ldots, n-1$, provided that $\lambda_{n}$ is large enough. Take $f=\Sigma f_{n}$.

13 Construct a function $f \in C^{\infty}$ such that the power series

$$
\sum_{n=0}^{\infty} \frac{\left(D^{n} f\right)(a)}{n !}(x-a)^{n}
$$

has radius of convergence 0 for every $a \in R^{1}$. Suggestion: Put

$$
f(z)=\sum_{k=1}^{\infty} c_{k} e^{i \lambda_{k} x}
$$

where $\left\{c_{k}\right\}$ and $\left\{\lambda_{k}\right\}$ are sequences of positive numbers, chosen so that $\Sigma c_{k} \lambda_{k}^{n}<\infty$ for $n=0,1,2, \ldots$ and so that $c_{n} \lambda_{n}^{n}$ increases very rapidly and is much larger than the sum of all the other terms in the series $\Sigma c_{k} \lambda_{k}^{n}$.

For instance, put $c_{k}=\lambda_{k}^{1-k}$, and choose $\left\{\lambda_{k}\right\}$ so that

$$
\lambda_{k}>2 \sum_{j=1}^{k-1} c_{j} \lambda_{j}^{k} \quad \text { and } \quad \lambda_{k}>k^{2 k}
$$

14 Suppose $C\left\{M_{n}\right\}$ is quasi-analytic, $f \in C\left\{M_{n}\right\}$, and $f(x)=0$ for infinitely many $x \in[0,1]$. What follows?

15 Let $X$ be the vector space of all entire functions $f$ that satisfy $|f(z)| \leq C e^{\pi|z|}$ for some $C<\infty$, and whose restriction to the real axis is in $L^{2}$. Associate with each $f \in X$ its restriction to the integers. Prove that $f \rightarrow\{f(n)\}$ is a linear one-to-one mapping of $X$ onto $\ell^{2}$.

16 Assume $f$ is a measurable function on $(-\infty, \infty)$ such that $|f(x)|<e^{-|x|}$ for all $x$. Prove that its Fourier transform $\hat{f}$ cannot have compact support, unless $f(x)=0$ a.e.

## UNIFORM APROXIMATION <br> BY POLYNOMIALS

## Introduction

20.1 Let $K^{0}$ be the interior of a compact set $K$ in the complex plane. (By definition, $K^{0}$ is the union of all open discs which are subsets of $K$; of course, $K^{0}$ may be empty even if $K$ is not.) Let $P(K)$ denote the set of all functions on $K$ which are uniform limits of polynomials in $z$.

Which functions belong to $P(K)$ ?

Two necessary conditions come to mind immediately: If $f \in P(K)$, then $f \in C(K)$ and $f \in H\left(K^{0}\right)$.

The question arises whether these necessary conditions are also sufficient. The answer is negative whenever $K$ separates the plane (i.e., when the complement of $K$ is not connected). We saw this in Sec. 13.8. On the other hand, if $K$ is an interval on the real axis (in which case $K^{0}=\varnothing$ ), the Weierstrass approximation theorem asserts that

$$
P(K)=C(K)
$$

So the answer is positive if $K$ is an interval. Runge's theorem also points in this direction, since it states, for compact sets $K$ which do not separate the plane, that $P(K)$ contains at least all those $f \in C(K)$ which have holomorphic extensions to some open set $\Omega \supset K$.

In this chapter we shall prove the theorem of Mergelyan which states, without any superfluous hypotheses, that the above-mentioned necessary conditions are also sufficient if $K$ does not separate the plane.

The principal ingredients of the proof are: Tietze's extension theorem, a smoothing process invoving convolutions, Runge's theorem, and Lemma 20.2, whose proof depends on properties of the class $\mathscr{S}$ which was introduced in Chap. 14.

## Some Lemmas

20.2 Lemma Suppose $D$ is an open disc of radius $r>0, E \subset D, E$ is compact and connected, $\Omega=S^{2}-E$ is connected, and the diameter of $E$ is at least $r$. Then there is a function $g \in H(\Omega)$ and a constant $b$, with the following property: If

$$
Q(\zeta, z)=g(z)+(\zeta-b) g^{2}(z)
$$

the inequalities

$$
\begin{gathered}
|Q(\zeta, z)|<\frac{100}{r} \\
\left|Q(\zeta, z)-\frac{1}{z-\zeta}\right|<\frac{1,000 r^{2}}{|z-\zeta|^{3}}
\end{gathered}
$$

hold for all $z \in \Omega$ and for all $\zeta \in D$.

We recall that $S^{2}$ is the Riemann sphere and that the diameter of $E$ is the supremum of the numbers $\left|z_{1}-z_{2}\right|$, where $z_{1} \in E$ and $z_{2} \in E$.

Proof We assume, without loss of generality, that the center of $D$ is at the origin. So $D=D(0 ; r)$.

The implication $(d) \rightarrow(b)$ of Theorem 13.11 shows that $\Omega$ is simply connected. (Note that $\infty \in \Omega$.) By the Riemann mapping theorem there is therefore a conformal mapping $F$ of $U$ onto $\Omega$ such that $F(0)=\infty$. $F$ has an expansion of the form

$$
F(w)=\frac{a}{w}+\sum_{n=0}^{\infty} c_{n} w^{n} \quad(w \in U)
$$

We define

$$
g(z)=\frac{1}{a} F^{-1}(z) \quad(z \in \Omega)
$$

where $F^{-1}$ is the mapping of $\Omega$ onto $U$ which inverts $F$, and we put

$$
b=\frac{1}{2 \pi i} \int_{\Gamma} z g(z) d z
$$

where $\Gamma$ is the positively oriented circle with center 0 and radius $r$.

By (4), Theorem 14.15 can be applied to $F / a$. It asserts that the diameter of the complement of $(F / a)(U)$ is at most 4. Therefore diam $E \leq 4|a|$. Since $\operatorname{diam} E \geq r$, it follows that

$$
|a| \geq \frac{r}{4}
$$

Since $g$ is a conformal mapping of $\Omega$ onto $D(0 ; 1 /|a|)$, (7) shows that

$$
|g(z)|<\frac{4}{r} \quad(z \in \Omega)
$$

and since $\Gamma$ is a path in $\Omega$, of length $2 \pi r$, (6) gives

$$
|b|<4 r
$$

If $\zeta \in D$, then $|\zeta|<r$, so (1), (8), and (9) imply

$$
|Q| \leq \frac{4}{r}+5 r\left(\frac{16}{r^{2}}\right)<\frac{100}{r}
$$

This proves (2).

Fix $\zeta \in D$.

If $z=F(w)$, then $z g(z)=w F(w) / a$; and since $w F(w) \rightarrow a$ as $w \rightarrow 0$, we have $z g(z) \rightarrow 1$ as $z \rightarrow \infty$. Hence $g$ has an expansion of the form

$$
g(z)=\frac{1}{z-\zeta}+\frac{\lambda_{2}(\zeta)}{(z-\zeta)^{2}}+\frac{\lambda_{3}(\zeta)}{(z-\zeta)^{3}}+\cdots \quad(|z-\zeta|>2 r)
$$

Let $\Gamma_{0}$ be a large circle with center at 0 ; (11) gives (by Cauchy's theorem) that

$$
\lambda_{2}(\zeta)=\frac{1}{2 \pi i} \int_{\Gamma_{0}}(z-\zeta) g(z) d z=b-\zeta
$$

Substitute this value of $\lambda_{2}(\zeta)$ into (11). Then (1) shows that the function

$$
\varphi(z)=\left[Q(\zeta, z)-\frac{1}{z-\zeta}\right](z-\zeta)^{3}
$$

is bounded as $z \rightarrow \infty$. Hence $\varphi$ has a removable singularity at $\infty$. If $z \in \Omega \cap D$, then $|z-\zeta|<2 r$, so (2) and (13) give

$$
|\varphi(z)|<8 r^{3}|Q(\zeta, z)|+4 r^{2}<1,000 r^{2}
$$

By the maximum modulus theorem, (14) holds for all $z \in \Omega$. This proves (3).

20.3 Lemma Suppose $f \in C_{c}^{\prime}\left(R^{2}\right)$, the space of all continuously differentiable functions in the plane, with compact support. Put

$$
\bar{\partial}=\frac{1}{2}\left(\frac{\partial}{\partial x}+i \frac{\partial}{\partial y}\right)
$$

Then the following "Cauchy formula" holds:

$$
f(z)=-\frac{1}{\pi} \iint_{R^{2}} \frac{(\bar{\partial} f)(\zeta)}{\zeta-z} d \xi d \eta \quad(\zeta=\xi+i \eta)
$$

Proof This may be deduced from Green's theorem. However, here is a simple direct proof:

Put $\varphi(r, \theta)=f\left(z+r e^{i \theta}\right), r>0, \theta$ real. If $\zeta=z+r e^{i \theta}$, the chain rule gives

$$
(\bar{\partial} f)(\zeta)=\frac{1}{2} e^{i \theta}\left[\frac{\partial}{\partial r}+\frac{i}{r} \frac{\partial}{\partial \theta}\right] \varphi(r, \theta)
$$

The right side of (2) is therefore equal to the limit, as $\epsilon \rightarrow 0$, of

$$
-\frac{1}{2 \pi} \int_{\epsilon}^{\infty} \int_{0}^{2 \pi}\left(\frac{\partial \varphi}{\partial r}+\frac{i}{r} \frac{\partial \varphi}{\partial \theta}\right) d \theta d r
$$

For each $r>0, \varphi$ is periodic in $\theta$, with period $2 \pi$. The integral of $\partial \varphi / \partial \theta$ is therefore 0 , and (4) becomes

$$
-\frac{1}{2 \pi} \int_{0}^{2 \pi} d \theta \int_{\epsilon}^{\infty} \frac{\partial \varphi}{\partial r} d r=\frac{1}{2 \pi} \int_{0}^{2 \pi} \varphi(\epsilon, \theta) d \theta
$$

As $\epsilon \rightarrow 0, \varphi(\epsilon, \theta) \rightarrow f(z)$ uniformly. This gives (2).

We shall establish Tietze's extension theorem in the same setting in which we proved Urysohn's lemma, since it is a fairly direct consequence of that lemma.

20.4 Tietze's Extension Theorem Suppose $K$ is a compact subset of a locally compact Hausdorff space $X$, and $f \in C(K)$. Then there exists an $F \in C_{c}(X)$ such that $F(x)=f(x)$ for all $x \in K$.

(As in Lusin's theorem, we can also arrange it so that $\|F\|_{X}=\|f\|_{K}$.)

Proof Assume $f$ is real, $-1 \leq f \leq 1$. Let $W$ be an open set with compact closure so that $K \subset W$. Put

$$
K^{+}=\left\{x \in K: f(x) \geq \frac{1}{3}\right\}, \quad K^{-}=\left\{x \in K: f(x) \leq-\frac{1}{3}\right\}
$$

Then $K^{+}$and $K^{-}$are disjoint compact subsets of $W$. As a consequence of Urysohn's lemma there is a function $f_{1} \in C_{c}(X)$ such that $f_{1}(x)=\frac{1}{3}$ on $K^{+}$, $f_{1}(x)=-\frac{1}{3}$ on $K^{-},-\frac{1}{3} \leq f_{1}(x) \leq \frac{1}{3}$ for all $x \in X$, and the support of $f_{1}$ lies in $W$. Thus

$$
\left|f-f_{1}\right| \leq \frac{2}{3} \text { on } K, \quad\left|f_{1}\right| \leq \frac{1}{3} \text { on } X .
$$

Repeat this construction with $f-f_{1}$ in place of $f$ : There exists an $f_{2} \in$ $C_{c}(X)$, with support in $W$, so that

$$
\left|f-f_{1}-f_{2}\right| \leq\left(\frac{2}{3}\right)^{2} \text { on } K, \quad\left|f_{2}\right| \leq \frac{1}{3} \cdot \frac{2}{3} \text { on } X .
$$

In this way we obtain functions $f_{n} \in C_{c}(X)$, with supports in $W$, such that

$$
\left|f-f_{1}-\cdots-f_{n}\right| \leq\left(\frac{2}{3}\right)^{n} \text { on } K, \quad\left|f_{n}\right| \leq \frac{1}{3} \cdot\left(\frac{2}{3}\right)^{n-1} \text { on } X
$$

Put $F=f_{1}+f_{2}+f_{3}+\cdots$. By (4), the series converges to $f$ on $K$, and it converges uniformly on $X$. Hence $F$ is continuous. Also, the support of $F$ lies in $\bar{W}$.

## Mergelyan's Theorem

20.5 Theorem If $K$ is a compact set in the plane whose complement is connected, if $f$ is a continuous complex function on $K$ which is holomorphic in the interior of $K$, and if $\epsilon>0$, then there exists a polynomial $P$ such that $|f(z)-P(z)|<\epsilon$ for all $z \in K$.

If the interior of $K$ is empty, then part of the hypothesis is vacuously satisfied, and the conclusion holds for every $f \in C(K)$. Note that $K$ need not be connected.

Proof By Tietze's theorem, $f$ can be extended to a continuous function in the plane, with compact support. We fix one such extension, and denote it again by $f$.

For any $\delta>0$, let $\omega(\delta)$ be the supremum of the numbers

$$
\left|f\left(z_{2}\right)-f\left(z_{1}\right)\right|
$$

where $z_{1}$ and $z_{2}$ are subject to the condition $\left|z_{2}-z_{1}\right| \leq \delta$. Since $f$ is uniformly continuous, we have

$$
\lim _{\delta \rightarrow 0} \omega(\delta)=0
$$

From now on, $\delta$ will be fixed. We shall prove that there is a polynomial $P$ such that

$$
|f(z)-P(z)|<10,000 \omega(\delta) \quad(z \in K)
$$

By (1), this proves the theorem.

Our first objective is the construction of a function $\Phi \in C_{c}^{\prime}\left(R^{2}\right)$, such that for all $z$

$$
\begin{aligned}
|f(z)-\Phi(z)| & \leq \omega(\delta) \\
|(\bar{\partial} \Phi)(z)| & <\frac{2 \omega(\delta)}{\delta}
\end{aligned}
$$

and

$$
\Phi(z)=-\frac{1}{\pi} \iint_{X} \frac{(\bar{\partial} \Phi)(\zeta)}{\zeta-z} d \xi d \eta \quad(\zeta=\xi+i \eta)
$$

where $X$ is the set of all points in the support of $\Phi$ whose distance from the complement of $K$ does not exceed $\delta$. (Thus $X$ contains no point which is "far within" $K$.)

We construct $\Phi$ as the convolution of $f$ with a smoothing function $A$. Put $a(r)=0$ if $r>\delta$, put

$$
a(r)=\frac{3}{\pi \delta^{2}}\left(1-\frac{r^{2}}{\delta^{2}}\right)^{2} \quad(0 \leq r \leq \delta)
$$

and define

$$
A(z)=a(|z|)
$$

for all complex $z$. It is clear that $A \in C_{c}^{\prime}\left(R^{2}\right)$. We claim that

$$
\begin{gathered}
\iint_{R^{2}} A=1, \\
\iint_{R^{2}} \bar{\partial} A=0, \\
\iint_{R^{2}}|\bar{\partial} A|=\frac{24}{15 \delta}<\frac{2}{\delta} .
\end{gathered}
$$

The constants are so adjusted in (6) that (8) holds. (Compute the integral in polar coordinates.) (9) holds simply because $A$ has compact support. To compute (10), express $\bar{\partial} A$ in polar coordinates, as in the proof of Lemma 20.3, and note that $\partial A / \partial \theta=0,|\partial A / \partial r|=-a^{\prime}(r)$.

Now define

$$
\Phi(z)=\iint_{R^{2}} f(z-\zeta) A(\zeta) d \xi d \eta=\iint_{R^{2}} A(z-\zeta) f(\zeta) d \xi d \eta
$$

Since $f$ and $A$ have compact support, so does $\Phi$. Since

$$
\Phi(z)-f(z)=\iint_{R^{2}}[f(z-\zeta)-f(z)] A(\zeta) d \xi d \eta
$$

and $A(\zeta)=0$ if $|\zeta|>\delta$, (3) follows from (8). The difference quotients of $A$ converge boundedly to the corresponding partial derivatives of $A$, since
$A \in C_{c}^{\prime}\left(R^{2}\right)$. Hence the last expression in (11) may be differentiated under the integral sign, and we obtain

$$
\begin{aligned}
(\bar{\partial} \Phi)(z) & =\iint_{R^{2}}(\bar{\partial} A)(z-\zeta) f(\zeta) d \xi d \eta \\
& =\iint_{R^{2}} f(z-\zeta)(\bar{\partial} A)(\zeta) d \xi d \eta \\
& =\iint_{R^{2}}[f(z-\zeta)-f(z)](\bar{\partial} A)(\zeta) d \xi d \eta
\end{aligned}
$$

The last equality depends on (9). Now (10) and (13) give (4). If we write (13) with $\Phi_{x}$ and $\Phi_{y}$ in place of $\bar{\partial} \Phi$, we see that $\Phi$ has continuous partial derivatives. Hence Lemma 20.3 applies to $\Phi$, and (5) will follow if we can show that $\bar{\partial} \Phi=0$ in $G$, where $G$ is the set of all $z \in K$ whose distance from the complement of $K$ exceeds $\delta$. We shall do this by showing that

$$
\Phi(z)=f(z) \quad(z \in G)
$$

note that $\bar{\partial} f=0$ in $G$, since $f$ is holomorphic there. (We recall that $\bar{\partial}$ is the Cauchy-Riemann operator defined in Sec. 11.1.) Now if $z \in G$, then $z-\zeta$ is in the interior of $K$ for all $\zeta$ with $|\zeta|<\delta$. The mean value property for harmonic functions therefore gives, by the first equation in (11),

$$
\begin{aligned}
\Phi(z) & =\int_{0}^{\delta} a(r) r d r \int_{0}^{2 \pi} f\left(z-r e^{i \theta}\right) d \theta \\
& =2 \pi f(z) \int_{0}^{\delta} a(r) r d r=f(z) \iint_{R^{2}} A=f(z)
\end{aligned}
$$

for all $z \in G$.

We have now proved (3), (4), and (5).

The definition of $X$ shows that $X$ is compact and that $X$ can be covered by finitely many open discs $D_{1}, \ldots, D_{n}$, of radius $2 \delta$, whose centers are not in $K$. Since $S^{2}-K$ is connected, the center of each $D_{j}$ can be joined to $\infty$ by a polygonal path in $S^{2}-K$. It follows that each $D_{j}$ contains a compact connected set $E_{j}$, of diameter at least $2 \delta$, so that $S^{2}-E_{j}$ is connected and so that $K \cap E_{j}=\varnothing$.

We now apply Lemma 20.2, with $r=2 \delta$. There exist functions
$g_{j} \in H\left(S^{2}-E_{j}\right)$ and constants $b_{j}$ so that the inequalities

$$
\begin{gathered}
\left|Q_{\jmath}(\zeta, z)\right|<\frac{50}{\delta}, \\
\left|Q_{j}(\zeta, z)-\frac{1}{z-\zeta}\right|<\frac{4,000 \delta^{2}}{|z-\zeta|^{3}}
\end{gathered}
$$

hold for $z \notin E_{j}$ and $\zeta \in D_{j}$, if

$$
Q_{j}(\zeta, z)=g_{j}(z)+\left(\zeta-b_{j}\right) g_{j}^{2}(z)
$$

Let $\Omega$ be the complement of $E_{1} \cup \cdots \cup E_{n}$. Then $\Omega$ is an open set which contains $K$.

Put $\quad X_{1}=X \cap D_{1} \quad$ and $\quad X_{j}=\left(X \cap D_{j}\right)-\left(X_{1} \cup \cdots \cup X_{j-1}\right), \quad$ for $2 \leq j \leq n$. Define

$$
R(\zeta, z)=Q_{j}(\zeta, z) \quad\left(\zeta \in X_{j}, z \in \Omega\right)
$$

and

$$
F(z)=\frac{1}{\pi} \iint_{X}(\bar{\partial} \Phi)(\zeta) R(\zeta, z) d \xi d \eta \quad(z \in \Omega)
$$

Since

$$
F(z)=\sum_{j=1}^{n} \frac{1}{\pi} \iint_{X_{j}}(\bar{\partial} \Phi)(\zeta) Q_{j}(\zeta, z) d \xi d \eta
$$

(18) shows that $F$ is a finite linear combination of the functions $g_{j}$ and $g_{j}^{2}$. Hence $F \in H(\Omega)$.

By (20), (4), and (5) we have

$$
|F(z)-\Phi(z)|<\frac{2 \omega(\delta)}{\pi \delta} \iint_{X}\left|R(\zeta, z)-\frac{1}{z-\zeta}\right| d \xi d \eta \quad(z \in \Omega)
$$

Observe that the inequalities (16) and (17) are valid with $R$ in place of $Q_{j}$ if $\zeta \in X$ and $z \in \Omega$. For if $\zeta \in X$ then $\zeta \in X_{j}$ for some $j$, and then $R(\zeta, z)=$ $Q_{f}(\zeta, z)$ for all $z \in \Omega$.

Now fix $z \in \Omega$, put $\zeta=z+\rho e^{i \theta}$, and estimate the integrand in (22) by (16) if $\rho<4 \delta$, by (17) if $4 \delta \leq \rho$. The integral in (22) is then seen to be less than the sum of

$$
2 \pi \int_{0}^{4 \delta}\left(\frac{50}{\delta}+\frac{1}{\rho}\right) \rho d \rho=808 \pi \delta
$$

and

$$
2 \pi \int_{4 \delta}^{\infty} \frac{4,000 \delta^{2}}{\rho^{3}} \rho d \rho=2,000 \pi \delta
$$

Hence (22) yields

$$
|F(z)-\Phi(z)|<6,000 \omega(\delta) \quad(z \in \Omega)
$$

Since $F \in H(\Omega), K \subset \Omega$, and $S^{2}-K$ is connected, Runge's theorem shows that $F$ can be uniformly approximated on $K$ by polynomials. Hence (3) and (25) show that (2) can be satisfied.

This completes the proof.

One unusual feature of this proof should be pointed out. We had to prove that the given function $f$ is in the closed subspace $P(K)$ of $C(K)$. (We use the terminology of Sec. 20.1.) Our first step consisted in approximating $f$ by $\Phi$. But this step took us outside $P(K)$, since $\Phi$ was so constructed that in general $\Phi$ will not be holomorphic in the whole interior of $K$. Hence $\Phi$ is at some positive distance from $P(K)$. However, (25) shows that this distance is less than a constant multiple of $\omega(\delta)$. [In fact, having proved the theorem, we know that this distance is at most $\omega(\delta)$, by (3), rather than $6,000 \omega(\delta)$.] The proof of $(25)$ depends on the inequality (4) and on the fact that $\bar{\partial} \Phi=0$ in $G$. Since holomorphic functions $\varphi$ are characterized by $\bar{\partial} \varphi=0$, (4) may be regarded as saying that $\Phi$ is not too far from being holomorphic, and this interpretation is confirmed by (25).

## Exercises

1 Extend Mergelyan's theorem to the case in which $S^{2}-K$ has finitely many components: Prove that then every $f \in C(K)$ which is holomorphic in the interior of $K$ can be uniformly approximated on $K$ by rational functions.

2 Show that the result of Exercise 1 does not extend to arbitrary compact sets $K$ in the plane, by verifying the details of the following example. For $n=1,2,3, \ldots$, let $D_{n}=D\left(\alpha_{n} ; r_{n}\right)$ be disjoint open discs in $U$ whose union $V$ is dense in $U$, such that $\Sigma r_{n}<\infty$. Put $K=\bar{U}-V$. Let $\Gamma$ and $\gamma_{n}$ be the paths

$$
\Gamma(t)=e^{i t}, \quad \gamma_{n}(t)=\alpha_{n}+r_{n} e^{i t}, \quad 0 \leq t \leq 2 \pi
$$

and define

$$
L(f)=\int_{\Gamma} f(z) d z-\sum_{n=1}^{\infty} \int_{\gamma_{n}} f(z) d z \quad(f \in C(K))
$$

Prove that $L$ is a bounded linear functional on $C(K)$, prove that $L(R)=0$ for every rational function $R$ whose poles are outside $K$, and prove that there exists an $f \in C(K)$ for which $L(f) \neq 0$.

3 Show that the function $g$ constructed in the proof of Lemma 20.2 has the smallest supremum norm among all $f \in H(\Omega)$ such that $z f(z) \rightarrow 1$ as $z \rightarrow \infty$. (This motivates the proof of the lemma.)

Show also that $b=c_{0}$ in that proof and that the inequality $|b|<4 r$ can therefore be replaced by $|b|<r$. In fact, $b$ lies in the convex hull of the set $E$.

## APPENDIX <br> HAUSDORFF'S MAXIMALITY THEOREM

We shall first prove a lemma which, when combined with the axiom of choice, leads to an almost instantaneous proof of Theorem 4.21.

If $\mathscr{F}$ is a collection of sets and $\Phi \subset \mathscr{F}$, we call $\Phi$ a subchain of $\mathscr{F}$ provided that $\Phi$ is totally ordered by set inclusion. Explicitly, this means that if $A \in \Phi$ and $B \in \Phi$, then either $A \subset B$ or $B \subset A$. The union of all members of $\Phi$ will simply be referred to as the union of $\Phi$.

Lemma Suppose $\mathscr{F}$ is a nonempty collection of subsets of a set $X$ such that the union of every subchain of $\mathscr{F}$ belongs to $\mathscr{F}$. Suppose $g$ is a function which associates to each $A \in \mathscr{F}$ a set $g(A) \in \mathscr{F}$ such that $A \subset g(A)$ and $g(A)-A$ consists of at most one element. Then there exists an $A \in \mathscr{F}$ for which $g(A)=A$.

ProOF Fix $A_{0} \in \mathscr{F}$. Call a subcollection $\mathscr{F}^{\prime}$ of $\mathscr{F}$ a tower if $\mathscr{F}^{\prime}$ has the following three properties:

(a) $A_{0} \in \mathscr{F}^{\prime}$.

(b) The union of every subchain of $\mathscr{F}^{\prime}$ belongs to $\mathscr{F}^{\prime}$.

(c) If $A \in \mathscr{F}^{\prime}$, then also $g(A) \in \mathscr{F}^{\prime}$.

The family of all towers is nonempty. For if $\mathscr{F}_{1}$ is the collection of all $A \in \mathscr{F}$ such that $A_{0} \subset A$, then $\mathscr{F}_{1}$ is a tower. Let $\mathscr{F}_{0}$ be the intersection of all towers. Then $\mathscr{F}_{0}$ is a tower (the verification is trivial), but no proper subcollection of $\mathscr{F}_{0}$ is a tower. Also, $A_{0} \subset A$ if $A \in \mathscr{F}_{0}$. The idea of the proof is to show that $\mathscr{F}_{0}$ is a subchain of $\mathscr{F}$.

Let $\Gamma$ be the collection of all $C \in \mathscr{F}_{0}$ such that every $A \in \mathscr{F}_{0}$ satisfies either $A \subset C$ or $C \subset A$.

For each $C \in \Gamma$, let $\Phi(C)$ be the collection of all $A \in \mathscr{F}_{0}$ such that either $A \subset C$ or $g(C) \subset A$.

Properties $(a)$ and $(b)$ are clearly satisfied by $\Gamma$ and by each $\Phi(C)$. Fix $C \in \Gamma$, and suppose $A \in \Phi(C)$. We want to prove that $g(A) \in \Phi(C)$. If $A \in \Phi(C)$, there are three possibilities: Either $A \subset C$ and $A \neq C$, or $A=C$, or $g(C) \subset A$. If $A$ is a proper subset of $C$, then $C$ cannot be a proper subset of $g(A)$, otherwise $g(A)-A$ would contain at least two elements; since $C \in \Gamma$, it follows that $g(A) \subset C$. If $A=C$, then $g(A)=g(C)$. If $g(C) \subset A$, then also $g(C) \subset g(A)$, since $A \subset g(A)$. Thus $g(A) \in \Phi(C)$, and we have proved that $\Phi(C)$ is a tower. The minimality of $\mathscr{F}_{0}$ implies now that $\Phi(C)=\mathscr{F}_{0}$, for every $C \in \Gamma$.

In other words, if $A \in \mathscr{F}_{0}$ and $C \in \Gamma$, then either $A \subset C$ or $g(C) \subset A$. But this says that $g(C) \in \Gamma$. Hence $\Gamma$ is a tower, and the minimality of $\mathscr{F}_{0}$ shows that $\Gamma=\mathscr{F}_{0}$. It follows now from the definition of $\Gamma$ that $\mathscr{F}_{0}$ is totally ordered.

Let $A$ be the union of $\mathscr{F}_{0}$. Since $\mathscr{F}_{0}$ satisfies $(b), A \in \mathscr{F}_{0}$. By $(c), g(A) \in$ $\mathscr{F}_{0}$. Since $A$ is the largest member of $\mathscr{F}_{0}$ and since $A \subset g(A)$, it follows that $A=g(A)$.

Definition A choice function for a set $X$ is a function $f$ which associates to each nonempty subset $E$ of $X$ an element of $E: f(E) \in E$.

In more informal terminology, $f$ "chooses" an element out of each nonempty subset of $X$.

The Axiom of Choice For every set there is a choice function.

Hausdorff's Maximality Theorem Every nonempty partially ordered set $P$ contains a maximal totally ordered subset.

Proof Let $\mathscr{F}$ be the collection of all totally ordered subsets of $P$. Since every subset of $P$ which consists of a single element is totally ordered, $\mathscr{F}$ is not empty. Note that the union of any chain of totally ordered sets is totally ordered.

Let $f$ be a choice function for $P$. If $A \in \mathscr{F}$, let $A^{*}$ be the set of all $x$ in the complement of $A$ such that $A \cup\{x\} \in \mathscr{F}$. If $A^{*} \neq \varnothing$, put

$$
g(A)=A \cup\left\{f\left(A^{*}\right)\right\}
$$

If $A^{*}=\varnothing$, put $g(A)=A$.

By the lemma, $A^{*}=\varnothing$ for at least one $A \in \mathscr{F}$, and any such $A$ is a maximal element of $\mathscr{F}$.

## NOTES AND COMMENTS

## Chapter 1

The first book on the modern theory of integration and differentiation is Lebesgue's "Leçons sur l'intégration," published in 1904.

For an illuminating history of the earlier attempts that were made toward the construction of a satisfactory theory of integration, see [42]†, which contains interesting discussions of the difficulties that even first-rate mathematicians had with simple set-theoretic concepts before these were properly defined and well understood.

The approach to abstract integration presented in the text is inspired by Saks [28]. Greater generality can be attained if $\sigma$-algebras are replaced by $\sigma$-rings (Axioms: $\bigcup A_{i} \in \mathscr{R}$ and $A_{1}-A_{2} \in \mathscr{R}$ if $A_{i} \in \mathscr{R}$ for $i=1,2,3, \ldots$; it is not required that $X \in \mathscr{R}$ ), but at the expense of a necessarily fussier definition of measurability. See Sec. 18 of [7]. In all classical applications the measurability of $X$ is more or less automatic. This is the reason for our choice of the somewhat simpler theory based on $\sigma$-algebras.

Sec. 1.11. This definition of $\mathscr{B}$ is as in [12]. In [7] the Borel sets are defined as the $\sigma$-ring generated by the compact sets. In spaces which are not $\sigma$-compact, this is a smaller family than ours.

## Chapter 2

Sec. 2.12. The usual statement of Urysohn's lemma is: If $K_{0}$ and $K_{1}$ are disjoint closed sets in a normal Hausdorff space $X$, then there is a continuous function on $X$ which is 0 on $K_{0}$ and 1 on $K_{1}$. The proof is exactly as in the text.

Sec. 2.14. The original form of this theorem, with $X=[0,1]$, is due to F. Riesz (1909). See [5], pp. 373, 380-381, and [12], pp. 134-135 for its further history. The theorem is here presented in the same generality as in [12]. The set function $\mu$ which is defined for all subsets of $X$ in the proof of Theorem 2.14 is called an outer measure because of its countable subadditivity (Step I). For systematic exploitations (originated by Carathéodory) of this notion, see [25] and [28].

Sec. 2.20. For direct constructions of Lebesgue measure, along more classical lines, see [31], $[35],[26]$ and [53].

$\dagger$ Numbers in brackets refer to the Bibliography.

Sec. 2.21. A proof that the cardinality of every countably generated $\sigma$-algebra is $\leq c$ may be found on pp. 133-134 of [44]. That this cardinality is either finite or $\geq c$ should be clear after doing Exercise 1 of Chap. 1.

Sec. 2.22. A very instructive paper on the subject of nonmeasurable sets in relation to measures invariant under a group is: J. von Neumann, Zur allgemeinen Theorie des Masses, Fundamenta Math., vol. 13, pp. 73-116, 1929. See also Halmos's article in the special (May, 1958) issue of Bull. Am. Math. Soc. devoted to von Neumann's work.

Sec. 2.24. [28], p. 72.

Sec. 2.25. [28], p. 75. There is another approach to the Lebesgue theory of integration, due to Daniell (Ann. Math., vol. 19, pp. 279-294, 1917-1918) based on extensions of positive linear functionals. When applied to $C_{c}(X)$ it leads to a construction which virtually turns the Vitali-Carathéodory theorem into the definition of measurability. See [17] and, for the full treatment, [18].

Exercise 8. Two interesting extensions of this phenomenon have appeared in Amer. Math. Monthly: see vol. 79, pp. 884-886, 1972 (R. B. Kirk) and vol. 91, pp. 564-566, 1984 (F. S. Cater).

Exercise 17. This example appears in A Theory of Radon Measures on Locally Compact Spaces, by R. E. Edwards, Acta Math., vol. 89, p. 160, 1953. Its existence was unfortunately overlooked in [27].

Exercise 18. [7], p. 231; originally due to Dieudonné.

## Chapter 3

The best general reference is [9]. See also Chap. 1 of [36].

Exercise 3. Vol. 1 (1920) of Fundamenta Math. contains three papers relevant to the parenthetical remark.

Exercise 7. A very complete answer to this question was found by A. Villani, in Am. Math. Monthly, vol. 92, pp. 485-487, 1985.

Exercise 16. [28], p. 18. When $t$ ranges over all positive real numbers, a measurability problem arises in the suggested proof. This is the reason for including (ii) as a hypothesis. See W. Walter, Am. Math. Monthly, vol. 84, pp. 118-119, 1977.

Exercise 17. The second suggested proof of part (b) was published by W. P. Novinger, in Proc. Am. Math. Soc., vol. 34, pp. 627-628, 1972. It was also discovered by David Hall.

Exercise 18. Convergence in measure is a natural concept in probability theory. See [7], Chap. IX.

## Chapter 4

There are many books dealing with Hilbert space theory. We cite [6] and [24] as main references. See also [5], [17], and [19].

The standard work on Fourier series is [36]. For simpler introductions, see [10], [31], [43], and [45].

Exercise 2. This is the so-called Gram-Schmidt orthogonalization process. periodic.

Exercise 18. The functions that are uniform limits (on $R^{1}$ ) of members of $X$ are called almost

## Chapter 5

The classical work here is [2]. More recent treatises are [5], [14], and [24]. See also [17] and [49].

Sec. 5.7. The relations between measure theory on the one hand and Baire's theorem on the other are discussed in great detail in [48].

Sec. 5.11. Although there are continuous functions whose Fourier series diverge on a dense $G_{\delta}$, the set of divergence must have measure 0 . This was proved by L. Carleson (Acta Math., vol. 116, pp. $135-157,1966$ ) for all $f$ in $L^{2}(T)$; the proof was extended to $L^{p}(T), p>1$, by R. A. Hunt. See also [45], especially Chap. II.

Sec. 5.22. For a deeper discussion of representing measures see Arens and Singer, Proc. Am. Math. Soc., vol. 5, pp. 735-745, 1954. Also [39], [52].

## Chapter 6

Sec. 6.3. The constant $1 / \pi$ is best possible. See R. P. Kaufman and N. W. Rickert, Bull. Am. Math. Soc., vol. 72, pp. 672-676, 1966, and (for a simpler treatment) W. W. Bledsoe, Am. Math. Monthly, vol. 77, pp. 180-182, 1970.

Sec. 6.10. von Neumann's proof is in a section on measure theory in his paper: On Rings of Operators, III, Ann. Math., vol. 41, pp. 94-161, 1940. See pp. 124-130.

Sec. 6.15. The phenomenon $L^{\infty} \neq\left(L^{1}\right)^{*}$ is discussed by J. T. Schwartz in Proc. Am. Math. Soc., vol. 2, pp. 270-275, 1951, and by H. W. Ellis and D. O. Snow in Can. Math. Bull., vol. 6, pp. 211-229, 1963. See also [7], p. 131, and [28], p. 36.

Sec. 6.19. The references to Theorem 2.14 apply here as well.

Exercise 6. See [17], p. 43.

Exercise $10(g)$. See [36], vol. I, p. 167.

## Chapter 7

Sec. 7.3. This simple covering lemma seems to appear for the first time in a paper by Wiener on the ergodic theorem (Duke Math. J., vol. 5, pp. 1-18, 1939). Covering lemmas play a central role in the theory of differentiation. See [50], [53], and, for a very detailed treatment, [41].

Sec. 7.4. Maximal functions were first introduced by Hardy and Littlewood, in Acta Math., vol. 54 , pp. 81-116, 1930. That paper contains proofs of Theorems 8.18, 11.25(b), and 17.11.

Sec. 7.21. The same conclusion can be obtained under somewhat weaker hypotheses; see [16], Theorems 260-264. Note that the proof of Theorem 7.21 uses the existence and integrability of only the right-hand derivative of $f$, plus the continuity of $f$. For a further refinement, see P. L. Walker, Amer. Math. Monthly, vol. 84, pp. 287-288, 1977.

Secs. 7.25, 7.26. This treatment of the change of variables formula is quite similar to $D$. Varberg's in Amer. Math. Monthly, vol. 78, pp. 42-45, 1971.

Exercise 5. A very simple proof, due to K. Stromberg, is in Proc. Amer. Math. Soc., vol. 36, p. 308, 1972.

Exercise 12. For an elementary proof that every monotone function (hence every function of bounded variation) is differentiable a.e., see [24], pp. 5-9. In that work, this theorem is made the starting point of the Lebesgue theory. Another, even simpler, proof by D. Austin is in Proc. Amer. Math. Soc., vol. 16, pp. 220-221, 1965.

Exercise 18. These functions $\varphi_{n}$ are the so-called Rademacher functions. Chap. V of [36] contains further theorems about them.

## Chapter 8

Fubini's theorem is developed here as in [7] and [28]. For a different approach, see [25]. Sec. 8.9(c) is in Fundamenta Math., vol. 1, p. 145, 1920.

Sec. 8.18. This proof of the Hardy-Littlewood theorem (see the reference to Sec. 7.4) is essentially that of a very special case of the Marcinkiewicz interpolation theorem. A full discussion of the latter may be found in Chap. XII of [36]. See also [50].

Exercise 2. Corresponding to the idea that an integral is an area under a curve, the theory of the Lebesgue integral can be developed in terms of measures of ordinate sets. This is done in [16].

Exercise 8. Part (b), in even more precise form, was proved by Lebesgue in J. Mathématiques, ser. 6, vol. 1, p. 201, 1905, and seems to have been forgotten. It is quite remarkable in view of another example of Sierpinski (Fundamenta Math., vol. 1, p. 114, 1920): There is a plane set $E$ which is not Lebesgue measurable and which has at most two points on each straight line. If $f=\chi_{E}$, then $f$ is not Lebesgue measurable, although all of the sections $f_{x}$ and $f^{y}$ are upper semicontinuous; in fact, each has at most two points of discontinuity. (This example depends on the axiom of choice, but not on the continuum hypothesis.)

## Chapter 9

For another brief introduction, see [36], chap. XVI. A different proof of Plancherel's theorem is in [33]. Group-theoretic aspects and connections with Banach algebras are discussed in [17], [19], and [27]. For more on invariant subspaces (Sec. 9.16) see [11]; the corresponding problem in $L^{1}$ is described in [27], Chap. 7.

## Chapter 10

General references: [1], [4], [13], [20], [29], [31] and [37].

Sec. 10.8. Integration can also be defined over arbitrary rectifiable curves. See [13], vol. I, Appendix C.

Sec. 10.10. The topological concept of index is applied in [29] and is fully utilized in [1]. The computational proof of Theorem 10.10 is as in [1], p. 93.

Sec. 10.13. Cauchy published his theorem in 1825, under the additional assumption that $f^{\prime}$ is continuous. Goursat showed that this assumption is redundant, and stated the theorem in its present form. See [13], p. 163, for further historical remarks.

Sec. 10.16. The standard proofs of the power series representation and of the fact that $f \in H(\Omega)$ implies $f^{\prime} \in H(\Omega)$ proceed via the Cauchy integral formula, as here. Recently proofs have been constructed which use the winding number but make no appeal to integration. For details see [34].

Sec. 10.25. A very elementary proof of the algebraic completeness of the complex field is in [26], p. 170.

Sec. 10.30. The proof of part $(b)$ is as in [47].

Sec. 10.32. The open mapping theorem and the discreteness of $Z(f)$ are topological properties of the class of all nonconstant holomorphic functions which characterize this class up to homeomorphisms. This is Stoilov's theorem. See [34].

Sec. 10.35. This strikingly simple and elementary proof of the global version of Cauchy's theorem was discovered by John D. Dixon, Proc. Am. Math. Soc., vol. 29, pp. 625-626, 1971. In [1] the proof is based on the theory of exact differentials. In the first edition of the present book it was deduced from Runge's theorem. That approach was used earlier in [29], p. 177. There, however, it was applied in simply connected regions only.

## Chapter 11

General references: [1], Chap. 5; [20], Chap. 1.

Sec. 11.14. The reflection principle was used by H. A. Schwarz to solve problems concerning conformal mappings of polygonal regions. See Sec. 17.6 of [13]. Further results along these lines were obtained by Carathéodory; see [4], vol. II, pp. 88-92, and Commentarii Mathematici Helvetici, vol. 19, pp. 263-278, 1946-1947.

Secs. 11.20, 11.25. This is the principal result of the Hardy-Littlewood paper mentioned in the reference to Sec. 7.4. The proof of the second inequality in Theorem 11.20 is as in [40], p. 23.

Sec. 11.23. The first theorems of this type are in Fatou's thesis, Séries trigonométriques et séries de Taylor, Acta Math., vol. 30, pp. 335-400, 1906. This is the first major work in which Lebesgue's theory of integration is applied to the study of holomorphic functions.

Sec. 11.30. Part (c) is due to Herglotz, Leipziger Berichte, vol. 63, pp. 501-511, 1911.

Exercise 14. This was suggested by W. Ramey and D. Ullrich.

## Chapter 12

Sec. 12.7. For further examples, see [31], pp. 176-186.

Sec. 12.11. This theorem was first proved for trigonometric series by W. H. Young $(1912 ; q=2$, $4,6, \ldots)$ and F. Hausdorff $(1923 ; 2 \leq q \leq \infty)$. F. Riesz (1923) extended it to uniformly bounded
orthonormal sets, M. Riesz (1926) derived this extension from a general interpolation theorem, and G. O. Thorin (1939) discovered the complex-variable proof of M. Riesz's theorem. The proof of the text is the Calderón-Zygmund adaptation (1950) of Thorin's idea. Full references and discussions of other interpolation theorems are in Chap. XII of [36].

Sec. 12.13. In slightly different form, this is in Duke Math. J., vol. 20, pp. 449-458, 1953.

Sec. 12.14. This proof is essentially that of R. Kaufman (Math. Ann., vol. 169, p. 282, 1967). E. L. Stout (Math. Ann., vol. 177, pp. 339-340, 1968) obtained a stronger result.

## Chapter 13

Sec. 13.9. Runge's theorem was published in Acta Math., vol. 6, 1885. (Incidentally, this is the same year in which the Weierstrass theorem on uniform approximation by polynomials on an interval was published; see Mathematische Werke, vol. 3, pp. 1-37.) See [29], pp. 171-177, for a proof which is close to the original one. The functional analysis proof of the text is known to many analysts and has probably been independently discovered several times in recent years. It was communicated to me by L. A. Rubel. In [13], vol. II, pp. 299-308, attention is paid to the closeness of the approximation if the degree of the polynomial is fixed.

Exercises 5, 6. For yet another method, see D. G. Cantor, Proc. Am. Math. Soc., vol. 15, pp. 335-336, 1964.

## Chapter 14

General reference: [20]. Many special mapping functions are described there in great detail.

Sec. 14.3. More details on linear fractional transformations may be found in [1], pp. 22-35; in [13], pp. 46-57; in [4]; and especially in Chap. 1 of L. R. Ford's book "Automorphic Functions," McGraw-Hill Book Company, New York, 1929.

Sec. 14.5. Normal families were introduced by Montel. See Chap. 15 of [13].

Sec. 14.8. The history of Riemann's theorem is discussed in [13], pp. 320-321, and in [29], p. 230. Koebe's proof (Exercise 26) is in J. für reine und angew. Math., vol. 145, pp. 177-223, 1915; doubly connected regions are also considered there.

Sec. 14.14. Much more is true than just $\left|a_{2}\right| \leq 2$ : In fact, $\left|a_{n}\right| \leq n$ for all $n \geq 2$. This was conjectured by Bieberbach in 1916, and proved by L. de Branges in 1984 [Acta Math., vol. 154, pp. 137-152, (1985)]. Moreover, if $\left|a_{n}\right|=n$ for just one $n \geq 2$, then $f$ is one of the Koebe functions of Example 14.11.

Sec. 14.19. The boundary behavior of conformal mappings was investigated by Carathéodory in Math. Ann., vol. 73, pp. 323-370, 1913. Theorem 14.19 was proved there for regions bounded by Jordan curves, and the notion of prime ends was introduced. See also [4], vol. II, pp. 88-107.

Exercise 24. This proof is due to Y. N. Moschovakis.

## Chapter 15

Sec. 15.9. The relation between canonical products and entire functions of finite order is discussed in Chap. 2 of [3], Chap. VII of [29], and Chap. VIII of [31].

Sec. 15.25. See Szasz, Math. Ann., vol. 77, pp. 482-496, 1916, for further results in this direction. Also Chap. II of [21]

## Chapter 16

The classical work on Riemann surfaces is [32]. (The first edition appeared in 1913.) Other references: Chap. VI of [1], Chap. 10 of [13], Chap. VI of [29], and [30].

Sec. 16.5. Ostrowski's theorem is in J. London Math. Soc., vol. 1, pp. 251-263, 1926. See J.-P. Kahane, Lacunary Taylor and Fourier Series, Bull. Am. Math. Soc., vol. 70, pp. 199-213, 1964, for a more recent account of gap series.

Sec. 16.15. The approach to the monodromy theorem was a little simpler in the first edition of this book. It used the fact that every simply connected plane region is homeomorphic to a convex
one, namely $U$. The present proof is so arranged that it applies without change to holomorphic functions of several complex variables. (Note that when $k>2$ there exist simply connected open sets in $R^{k}$ which are not homeomorphic to any convex set; spherical shells furnish examples of this.)

Sec. 16.17. Chap. 13 of [13], Chap. VIII of [29], and part 7 of [4].

Sec. 16.21. Picard's big theorem is proved with the aid of modular functions in part 7 of [4].

"Elementary" proofs may be found in [31], pp. 277-284, and in Chap. VII of [29].

Exercise 10. Various classes of removable sets are discussed by Ahlfors and Beurling in Conformal Invariants and Function-theoretic Null-Sets, Acta Math., vol. 83, pp. 101-129, 1950.

## Chapter 17

The classical reference here is [15]. See also [36], Chap. VII. Although [15] deals mainly with the unit disc, most proofs are so constructed that they apply to other situations which are described there. Some of these generalizations are in Chap. 8 of [27]. Other recent books on these topics are [38], $[40]$, and [46].

Sec. 17.1. See [22] for a thorough treatment of subharmonic functions.

Sec. 17.13. For a different proof, see [15], or the paper by Helson and Lowdenslager in Acta Math., vol. 99, pp. 165-202, 1958. An extremely simple proof was found by B. K. Øksendal, in Proc. Amer. Math. Soc., vol. 30, p. 204, 1971.

Sec. 17.14. The terms "inner function" and "outer function" were coined by Beurling in the paper in which Theorem 17.21 was proved: On Two Problems Concerning Linear Transformations in Hilbert Space, Acta Math., vol. 81, pp. 239-255, 1949. For further developments, see [11].

Secs. 17.25, 17.26. This proof of M. Riesz's theorem is due to A. P. Calderón. See Proc. Am. Math. Soc., vol. 1, pp. 533-535, 1950. See also [36], vol. I, pp. 252-262.

Exercise 3. This forms the basis of a definition of $H^{p}$-spaces in other regions. See Trans. Am. Math. Soc., vol. 78, pp. 46-66, 1955.

## Chapter 18

General references: [17], [19], and [23]; also [14]. The theory was originated by Gelfand in 1941.

Sec. 18.18. This was proved in elementary fashion by P. J. Cohen in Proc. Am. Math. Soc., vol. 12, pp. 159-163, 1961.

Sec. 18.20. This theorem is Wermer's, Proc. Am. Math. Soc., vol. 4, pp. 866-869, 1953. The proof of the text is due to Hoffman and Singer. See [15], pp. 93-94, where an extremely short proof by P. J. Cohen is also given. (See the reference to Sec. 18.18.)

Sec. 18.21. This was one of the major steps in Wiener's original proof of his Tauberian theorem. See [33], p. 91. The painless proof given in the text was the first spectacular success of the Gelfand theory.

Exercise 14. The set $\Delta$ can be given a compact Hausdorff topology with respect to which the function $\hat{x}$ is continuous. Thus $x \rightarrow \hat{x}$ is a homomorphism of $A$ into $C(\Delta)$. This representation of $A$ as an algebra of continuous functions is a most important tool in the study of commutative Banach algebras.

## Chapter 19

Secs. 19.2, 19.3: [21], pp. 1-13. See also [3], where functions of exponential type are the main subject. Sec. 19.5. For a more detailed introduction to the classes $C\left\{M_{n}\right\}$, see S. Mandelbrojt, "Séries de

Fourier et classes quasi-analytiques," Gauthier-Villars, Paris, 1935.

Sec. 19.11. In [21], the proof of this theorem is based on Theorem 19.2 rather than on 19.3.

Exercise 4. The function $\Phi$ is called the Borel transform of $f$. See [3], Chap. 5.

Exercise 12. The suggested proof is due to H. Mirkil, Proc. Am. Math. Soc., vol. 7, pp. 650-652,

1956. The theorem was proved by Borel in 1895.

## Chapter 20

See S. N. Mergelyan, Uniform Approximations to Functions of a Complex Variable, Uspehi Mat. Nauk (N.S.) 7, no. 2 (48), 31-122, 1952; Amer. Math. Soc. Translation No. 101, 1954. Our Theorem 20.5 is Theorem 1.4 in Mergelyan's paper.

A functional analysis proof, based on measure-theoretic considerations, has recently been published by L. Carleson in Math. Scandinavica, vol. 15, pp. 167-175, 1964.

## Appendix

The maximality theorem was first stated by Hausdorff on p. 140 of his book "Grundzüge der Mengenlehre," 1914. The proof of the text is patterned after Sec. 16 of Halmos's book [8]. The idea to choose $g$ so that $g(A)-A$ has at most one element appears there, as does the term "tower." The proof is similar to one of Zermelo's proofs of the well-ordering theorem; see Math. Ann., vol. 65, pp. 107-128, 1908.

## BIBLIOGRAPHY

1. L. V. Ahlfors: "Complex Analysis," $3 \mathrm{~d}$ ed., McGraw-Hill Book Company, New York, 1978.
2. S. Banach: Théorie des Opérations linéaires, "Monografie Matematyczne," vol. 1, Warsaw, 1932.
3. R. P. Boas: "Entire Functions," Academic Press Inc., New York, 1954.
4. C. Carathéodory: "Theory of Functions of a Complex Variable," Chelsea Publishing Company, New York, 1954.
5. N. Dunford and J. T. Schwartz: "Linear Operators," Interscience Publishers, Inc., New York, 1958.
6. P. R. Halmos: "Introduction to Hilbert Space and the Theory of Spectral Multiplicity," Chelsea Publishing Company, New York, 1951.
7. P. R. Halmos: "Measure Theory," D. Van Nostrand Company Inc., Princeton, N. J., 1950.
8. P. R. Halmos: "Naive Set Theory," D. Van Nostrand Company, Inc., Princeton, N. J., 1960.
9. G. H. Hardy, J. E. Littlewood, and G. Pólya: "Inequalities," Cambridge University Press, New York, 1934.
10. G. H. Hardy and W. W. Rogosinski: "Fourier Series," Cambridge Tracts no. 38, Cambridge, London, and New York, 1950.
11. H. Helson: "Lectures on Invariant Subspaces," Academic Press Inc., New York, 1964.
12. E. Hewitt and K. A. Ross: "Abstract Harmonic Analysis," Springer-Verlag, Berlin, vol. I, 1963; vol. II, 1970.
13. E. Hille: "Analytic Function Theory," Ginn and Company, Boston, vol. I, 1959; vol. II, 1962.
14. E. Hille and R. S. Phillips: "Functional Analysis and Semigroups," Amer. Math. Soc. Colloquium Publ. 31, Providence, 1957.
15. K. Hoffman: "Banach Spaces of Analytic Functions," Prentice-Hall, Inc., Englewood Cliffs, N. J., 1962.
16. H. Kestelman: "Modern Theories of Integration," Oxford University Press, New York, 1937.
17. L. H. Loomis: "An Introduction to Abstract Harmonic Analysis," D. Van Nostrand Company, Inc., Princeton, N. J., 1953.
18. E. J. McShane: "Integration," Princeton University Press, Princeton, N. J. 1944.
19. M. A. Naimark: “Normed Rings," Erven P. Noordhoff, NV, Groningen Netherlands, 1959.
20. Z. Nehari: "Conformal Mapping," McGraw-Hill Book Company, New York 1952.
21. R. E. A. C. Paley and N. Wiener: "Fourier Transforms in the Complex Domain," Amer. Math. Soc. Colloquium Publ. 19, New York, 1934.
22. T. Rado: Subharmonic Functions, Ergeb. Math., vol. 5, no. 1, Berlin, 1937.
23. C. E. Rickart: "General Theory of Banach Algebras," D. Van Nostrand Company, Inc., Princeton, N. J., 1960.
24. F. Riesz and B. Sz.-Nagy: "Leçons d'Analyse Fonctionnelle," Akadémiai Kiadó, Budapest, 1952.
25. H. L. Royden: "Real Analysis," The Macmillan Company, New York, 1963.
26. W. Rudin: "Principles of Mathematical Analysis," 3d ed., McGraw-Hill Book Company, New York, 1976.
27. W. Rudin: "Fourier Analysis on Groups," Interscience Publishers, Inc., New York, 1962.
28. S. Saks: "Theory of the Integral," 2d ed., "Monografie Matematyczne," vol. 7, Warsaw, 1937. Reprinted by Hafner Publishing Company, Inc., New York.
29. S. Saks and A. Zygmund: "Analytic Functions," "Monografie Matematyzcne," vol. 28, Warsaw, 1952.
30. G. Springer: "Introduction to Riemann Surfaces," Addison-Wesley Publishing Company, Inc., Reading, Mass., 1957.
31. E. C. Titchmarsh: "The Theory of Functions," $2 d$ ed., Oxford University Press, Fair Lawn, N. J., 1939.
32. H. Weyl: "The Concept of a Riemann Surface," 3d ed., Addison-Wesley Publishing Company, Inc., Reading, Mass., 1964.
33. N. Wiener: "The Fourier Integral and Certain of Its Applications," Cambridge University Press, New York, 1933. Reprinted by Dover Publications, Inc., New York.
34. G. T. Whyburn: "Topological Analysis," 2d ed., Princeton University Press, Princeton, N. J., 1964.
35. J. H. Williamson: "Lebesgue Integration," Holt, Rinehart and Winston, Inc., New York, 1962.
36. A. Zygmund: "Trigonometric Series," 2 d ed., Cambridge University Press, New York, 1959.

## Supplementary References

37. R. B. Burckel: "An Introduction to Classical Complex Analysis," Birkhäuser Verlag, Basel, 1979.
38. P. L. Duren: "Theory of $H^{p}$ Spaces," Academic Press, New York, 1970.
39. T. W. Gamelin: "Uniform Algebras," Prentice-Hall, Englewood Cliffs, N. J., 1969.
40. J. B. Garnett: "Bounded Analytic Functions," Academic Press, New York, 1981.
41. M. de Guzman: "Differentiation of Integrals in $R^{n}$," Lecture Notes in Mathematics 481, SpringerVerlag, Berlin, 1975.
42. T. Hawkins: "Lebesgue's Theory of Integration," University of Wisconsin Press, Madison, 1970.
43. H. Helson: "Harmonic Analysis," Addison-Wesley Publishing Company, Inc., Reading, Mass., 1983.
44. E. Hewitt and K. Stromberg: "Real and Abstract Analysis," Springer-Verlag, New York, 1965.
45. Y. Katznelson: "An Introduction to Harmonic Analysis," John Wiley and Sons, Inc., New York, 1968.
46. P. Koosis: "Lectures on $H_{p}$ Spaces," London Math. Soc. Lecture Notes 40, Cambridge University Press, London, 1980.
47. R. Narasimhan: "Several Complex Variables," University of Chicago Press, Chicago, 1971.
48. J. C. Oxtoby: "Measure and Category," Springer-Verlag, New York, 1971.
49. W. Rudin: "Functional Analysis," McGraw-Hill Book Company, New York, 1973.
50. E. M. Stein: "Singular Integrals and Differentiability Properties of Functions," Princeton University Press, Princeton, N. J., 1970.
51. E. M. Stein and G. Weiss: "Introduction to Fourier Analysis on Euclidean Spaces," Princeton University Press, Princeton, N. J., 1971.
52. E. L. Stout: "The Theory of Uniform Algebras," Bogden and Quigley, Tarrytown-on-Hudson, 1971.
53. R. L. Wheeden and A. Zygmund: "Measure and Integral,” Marcel Dekker Inc., New York, 1977.

## LIST OF SPECIAL SYMBOLS AND ABBREVIATIONS $\dagger$

| $\exp (z)$ | 1 | $\hat{x}(\alpha)$ | 82 |
| :--- | :--- | :--- | :--- |
| $\tau$ | 8 | $T$ | 88 |
| $\mathfrak{M}$ | 8 | $L^{p}(T), C(T)$ | 88 |
| $\chi_{E}$ | 11 | $Z$ | 89 |
| $\lim \sup$ | 14 | $\hat{f}(n)$ | 91 |
| $\lim \inf$ | 14 | $c_{0}$ | 104 |
| $f^{+}, f^{-}$ | 15 | $\\|f\\|_{E}$ | 108 |
| $L^{1}(\mu)$ | 24 | $U$ | 110 |
| a.e. | 27 | $P_{r}(\theta-t)$ | 111 |
| $\bar{E}$ | 35 | $\operatorname{Lip} \alpha$ | 113 |
| $C_{c}(X)$ | 38 | $\|\mu\|(E)$ | 116 |
| $K \prec f \prec V$ | 39 | $\mu^{+}, \mu^{-}$ | 119 |
| $\mathfrak{M}_{F}$ | 42 | $\lambda \ll \mu$ | 120 |
| $m, m_{k}$ | 51 | $\lambda_{1} \perp \lambda_{2}$ | 120 |
| $\Delta(T)$ | 51,150 | $B(x, r)$ | 136 |
| $L^{1}\left(R^{k}\right), L^{1}(E)$ | 53 | $Q_{r} \mu$ | 136 |
| $\\|f\\|_{p},\\|f\\|_{\infty}$ | 65,66 | $D \mu$ | 136,241 |
| $L^{p}(\mu), L^{p}\left(R^{k}\right), \ell^{p}$ | 65 | $M \mu$ | 136,241 |
| $L^{\infty}(\mu), L^{\infty}\left(R^{k}\right), \ell^{\infty}$ | 66 | $M f$ | 138 |
| $C_{0}(X), C(X)$ | 70 | $A C$ | 145 |
| $(x, y)$ | 76 | $T^{\prime}(x)$ | 150 |
| $\\|x\\|$ | 76 | $J_{T}$ | 150 |
| $x \perp y, M^{\perp}$ | 79 | $B V$ | 157 |

† The standard set-theoretic symbols are described on pages 6 to 8 and are not listed here.

408 LIST OF SPECIAL SYMBOLS AND ABBREVIATIONS

| $E_{x}, E^{y}$ | 161 | $P[d \mu]$ | 240 |
| :--- | :--- | :--- | :--- |
| $f_{x}, f^{y}$ | 162 | $\Omega_{\alpha}$ | 240 |
| $\mu \times \lambda$ | 164 | $N_{\alpha}$ | 241 |
| $f * g$ | 171 | $M_{\mathrm{rad}}$ | 241 |
| $\mu * \lambda$ | 175 | $\sigma$ | 241 |
| $\hat{f}(t)$ | 178 | $H^{\infty}$ | 248 |
| $C^{\infty}$ | 194 | $f^{*}\left(e^{i t}\right)$ | 249 |
| $C_{c}^{\infty}$ | 194 | $\varphi_{\alpha}(z)$ | 254 |
| $D(a ; r), D^{\prime}(a ; r), \bar{D}(a ; r)$ | 196 | $S^{2}$ | 266 |
| $\Omega$ | 197 | $\mathscr{S}^{2}$ | 285 |
| $H(\Omega)$ | 197 | $E_{p}(z)$ | 301 |
| $\gamma, \gamma^{*}$ | 200 | $\log ^{+} t$ | 311 |
| $\partial \Delta$ | 202 | $N$ | 311 |
| $\operatorname{Ind}_{y}(z)$ | 203 | $\left(f_{0}, D_{0}\right) \sim\left(f_{1}, D_{1}\right)$ | 323 |
| $Z(f)$ | 208 | $H^{p}$ | 338 |
| $\dot{+}$ | 217 | $M_{f}, Q_{f}$ | 344 |
| $I^{2}=I \times I$ | 222 | $\sigma(x)$ | 357 |
| $\partial, \bar{\partial}$ | 231 | $\rho(x)$ | 360 |
| $\Delta$ | 232 | $C\left\{M_{n}\right\}$ | 377 |
| $P[f]$ | 233 | $P(K)$ | 386 |
| $\Pi^{+}, \Pi^{-}$ | 237 | $C_{c}^{\prime}\left(R^{2}\right)$ | 388 |

Absolute continuity, 120

of functions, 145

Absolute convergence, 116

Absolutely convergent Fourier series, 367

Addition formula, 1

Affine transformation, 377

Ahlfors, L. V., 402

Algebra, 356

of measures, 175

of sets, 10

Algebraically closed field, 213

Almost everywhere, 27

Almost periodic function, 94

Almost uniform convergence, 214

Analytic continuation, 323, 377, 379

Analytic function, 197

Annulus, 229, 264, 292

Approach region, 240

Area, 250

Area theorem, 286

Arens, R., 398

Argument, 204

Arithmetic mean, 63

Arzela-Ascoli theorem, 245

Associative law, 18

Asymptotic value, 265

Austin, D., 399

Average, 30

Axiom of choice, 396

Baire's theorem, 97

Balanced collection, 268
Ball, 9

Banach, S., 105

Banach algebra, 190, 356

Banach space, 95

Banach-Steinhaus theorem, 98

Bessel's inequality, 85, 260

Beurling, A., 335, 402

Beurling's theorem, 348

Bieberbach conjecture, 401

Blaschke product, 310, 317, 318, 338, 353

Bledsoe, W. W., 399

Borel, E., 5, 402

Borel function, 12

Borel measure, 47

Borel set, 12

Borel transform, 402

Boundary, 108, 202, 289

Bounded function, 66

Bounded linear functional, 96, 113, 127, 130

Bounded linear transformation, 96

Bounded variation, 117, 148, 157

Box, 50

Brouwer's fixed point theorem, 151

Calderón, A. P., 401, 402

Cancellation law, 19

Canonical product, 302

Cantor, D. G., 401

Cantor set, 58, 145

Carathéodory, C., 397, 400, 401

Carleson, L., 398

Carrier, 58

Cartesian product, 7, 160

Category theorem, 98

Cater, F. S., 398

Cauchy, A., 400

Cauchy formula, 207, 219, 229, 268, 341, 384, 388

Cauchy-Riemann equations, 232

Cauchy sequence, 67

Cauchy theorem, 205, 206, 207, 218

Cauchy's estimates, 213

Cell, 50

Chain, 218

Chain rule, 197

Change of variables, 153, 156

Character, 179

Characteristic function, 11

Choice function, 396

Class, 6

Closed curve, 200

Closed graph theorem, 114

Closed path, 201

Closed set, 13, 35

Closed subspace, 78

Closure, 35

Cohen, P. J., 402

Collection, 6

Commutative algebra, 356

Commutative law, 18

Compact set, 35

Complement, 7

Complete measure, 28

Complete metric space, 67

Completion:

of measure space, 28,168

of metric space, 70, 74

Complex algebra, 356

Complex field, 213, 359

Complex homomorphism, 191, 362

Complex-linear functional, 105

Complex measure, 16, 116

Complex vector space, 33

Component, 197

Composite function, 7

Concentrated, 119

Conformal equivalence, 282

Conjugate exponents, 63

Conjugate function, 350

Connected set, 196

Continuity, 8, 9

Continuous function, 8

Continuous linear functional, 81, 96, 113, 127, 130

Continuous measure, 175

Continuum hypothesis, 167
Convergence:

dominated, 26

in $L^{\mathrm{p}}, 67$

in measure, 74

monotone, 21

almost uniform, 214

uniform on compact subsets, 214

weak, 245

Convex function, 61

Convex sequence, 410

Convex set, 79

Convexity theorem, 257

Convolution, 170, 175, 178

Coset, 362

Cosine, 2, 265

Countable additivity, 6, 16

Counting measure, 17

Cover, 35, 324

Covering lemma, 137, 399

Curve, 200

with orthogonal increments, 94

Cycle, 218

Daniell, P. J., 398

de Branges, L., 401

Denjoy, A., 144

Denjoy-Carleman theorem, 380

Dense set, 58

Derivative, 135, 197

of Fourier transform, 179

of function of bounded variation, 157

of integral, 141

of measure, 136, 142, 143, 241

symmetric, 136

of transformation, 150

Determinant, 54

Diagonal process, 246

Dieudonné, J., 398

Differentiable transformation, 150

Differential, 150

Direct continuation, 323

Dirichlet kernel, 101

Dirichlet problem, 235

Disc, 9, 196

Discrete measure, 175

Disjoint sets, 7

Distance function, 9

Distribution function, 172

Distributive law, 18

Division algebra, 360

Dixon, J. D., 400

Domain, 7

Dominated convergence theorem, 26, 29, 180

Double integral, 165

Dual space, 108, 112, 127, 130

Eberlein, W. F., 58

Edwards, R. E., 398

Egoroff's theorem, 73

Elementary factor, 301

Elementary set, 161

Ellipse, 287

Ellis, H. W., 399

Empty set, 6

End point, 200

Entire function, 198

Equicontinuous family, 245

Equivalence classes, 67

Equivalent paths, 201

Essential range, 74

Essential singularity, 211, 267

Essential supremum, 66

Euclidean space, 34, 49

Euclid's inequality, 77

Euler's identity, 2

Exponential function, 1, 198

Exponential type, 372, 382, 383

Extended real line, 7, 9

Extension, 105

Extension theorem, 105

Extremal function, 255

Extreme point, 251

$F_{\sigma}$-set, 12

Factorization, 303, 338, 344

Family, 6

Fatou, P., 400

Fatou's lemma, 23, 68, 309, 344

Fatou's theorem, 249

Fejér kernel, 252

Fejér's theorem, 91

Field, 394

Finite additivity, 17

First category, 98

Fixed point, 151, 229, 247, 293, 297, 314, 318, 395

Ford, L. R., 401

Fourier coefficients, 82, 91

of measure, 133

Fourier series, 83, 91

Fourier transform, 178

Fubini's theorem, 164, 168

Function, 7

absolutely continuous, 145

analytic, 197

Borel, 13

bounded, 66

of bounded variation, 148 complex, 8

continuous, 8

convex, 61

entire, 198

essentially bounded, 66

exponential, 1

of exponential type, 372,383

harmonic, 232

holomorphic, 197

Lebesgue integrable, 24

left-continuous, 157

locally integrable, 194

lower semicontinuous, 37

measurable, 8, 29

meromorphic, 224

modular, 328

nowhere differentiable, 114

rational, 267

real, 8

simple, 15

subharmonic, 335

summable, 24

upper semicontinuous, 37

Function element, 323

Functional:

bounded, 96

on $C_{0}, 130$

complex-linear, 105

continuous, 96

on Hilbert space, 81

on $L^{p}, 127$

linear, 33

multiplicative, 191, 364

positive, 34

real-linear, 105

Functional analysis, 108

Fundamental domain, 329

Fundamental theorem of calculus, 144, 148

$G_{\delta}$-set, 12

Gap series, 276, 321, 334, 354, 385

Gelfand, I., 402

Gelfand-Mazur theorem, 359

Gelfand transform, 370

Geometric mean, 63

Goursat, E., 400

Graph, 114, 174

Greatest lower bound, 7

Green's theorem, 389

Hadamard, J., 264, 321

Hahn-Banach theorem, 104, 107, 270, 313, 359

Hahn decomposition, 126

Hall, D., 398

Halmos, P. R., 398, 403

Hardy, G. H., 173, 335, 399

Hardy's inequality, 72, 177

Harmonic conjugate, 350

Harmonic function, 232

Harmonic majorant, 352

Harnack's theorem, 236, 250

Hausdorff, F., 12, 400

Hausdorff maximality theorem, 87, 107, 195, 362, 396

Hausdorff separation axiom, 36

Hausdorff space, 36

Hausdorff-Young theorem, 261

Heine-Borel theorem, 36

Helson, H., 348

Herglotz, G., 400

Hilbert cube, 92

Hilbert space, 77

isomorphism, 86

Hoffman, K., 402

Hölder's inequality, 63, 66

Holomorphic function, 197

Homomorphism, 179, 191, 364, 402

Homotopy, 222

Hunt, R. A., 398

Ideal, $175,305,362$

Image, 7

Independent set, 82

Index:

of curve, 223, 230

of cycle, 218

of path, 203

Infimum, 7

Infinite product, 298

Initial point, 200

Inner factor, 344

Inner function, 342

Inner product, 76,89

Inner regular set, 47

Integral, 19, 24

Integration, 19

over cycle, 218

of derivative, 146, 148, 149

over measurable set, 20

by parts, 157

over path, 200

with respect to complex measure, 129

Interior, 267

Interpolation, 173, 260, 304

Intersection, 6

Interval, 7

Invariant subspace, 188, 346

Inverse image, 7
Inverse mapping, 7, 215

Inversion, 280

Inversion formula, 181

Inversion theorem, 185, 186

Invertible element, 357

Isolated singularity, 210, 266

Isometry, 84

Isomorphism, 86

Iterated integral, 165

Jacobian, 150, 250

Jensen's formula, 307

Jensen's inequality, 62

Jordan, C., 5

Jordan curve, 291

Jordan decomposition, 119

Kahane, J. P., 401

Kaufman, R. P., 399, 437

Kirk, R. B., 398

Koebe function, 285, 401

Laplace equation, 232

Laplacian, 195

Laurent series, 230

Least upper bound, 7

Lebesgue, H. J., 5, 21, 397, 399

Lebesgue decomposition, 121

Lebesgue integrable function, 24

Lebesgue integral, 19

Lebesgue measurable set, 51

Lebesgue measure, 51

Lebesgue point, 138, 159, 241

Left-continuous function, 157

Left-hand limit, 157

Length, 159, 202

Limit, pointwise, 14

in mean, 67

of measurable functions, 14

in measure, 74

Lindelöf's theorem, 259

Linear combination, 82

Linear fractional transformation, 279, 296

Linear independence, 82

Linear transformation, 33

Linearly ordered set, 87

Liouville's theorem, 212, 220, 359

Lipschitz condition, 113

Littlewood, J. E., 173, 399

Locally compact space, 36

Locally integrable function, 194

Logarithm, 227, 274

Lowdenslager, D., 348

Lower half plane, 237

Lower limit, 14

Lower semicontinuous function, 37

Lusin's theorem, 55

Mandelbrojt, S., 402

Mapping, 7

continuous, 8

one-to-one, 7

open, 99, 214

(See also Function)

Marcinkiewicz, J., 173

Maximal function, 136, 138, 241

Maximal ideal, 362, 364

Maximal orthonormal set, 85

Maximal subalgebra, 366

Maximality theorem, 87, 396

Maximum modulus theorem, 110, 212

Mean value property, 237

Measurable function, 8, 29

Measurable set, 8

Measurable space, 8

Measure, 17

absolutely continuous, 120

Borel, 47

complete, 28

complex, 16

continuous, 175

counting, 18

discrete, 175

Lebesgue, 51

positive, 16

real, 16

regular, 47

representing, 109

$\sigma$-finite, 47

signed, 119

singular, 120

translation-invariant, 51

Measure space, 16

Mergelyan's theorem, 390, 394

Meromorphic function, 224, 304

Metric, 9

Metric density, 141

Metric space, 9

Minkowski's inequality, 63, 177

Mirkil, H., 402

Mittag-Leffler theorem, 273

Modular function, 328

Modular group, 328

Monodromy theorem, 327

Monotone class, 160

Monotone convergence theorem, 21

Monotonicity, 17, 42

Morera's theorem, 208
Moschovakis, Y. N., 401

Multiplication operator, 114, 347

Multiplicative inequality, 356

Multiplicative linear functional, 364

Multiplicity of a zero, 209

Müntz-Szasz theorem, 313, 318

Natural boundary, 320, 330

Negative part, 15

Negative variation, 119

Neighborhood, 9, 35

Neumann, J. von, 122, 398, 399

Nevanlinna, R., 311

Nicely shrinking sequence, 140

Nonmeasurable set, 53, 157, 167

Nontangential approach region, 240

Nontangential limit, 243, 340

Nontangential maximal function, 241, 340

Norm, 65, 76, 95, 96

Norm-preserving extension, 106

Normal family, 281

Normed algebra, 356

Normed linear space, 95

Novinger, W. P., 398

Nowhere dense, 98

Nowhere differentiable function, 114

Null-homotopic curve, 222

Null space, 362

One-to-one mapping, 7

One-parameter family, 222, 326

Onto, 7

Open ball, 9

Open cover, 35

Open mapping theorem, 99, 214, 216

Open set, 8

Opposite path, 201

Orbit, 317

Order:

of entire function, 315

of pole, 210

of zero, 209

Ordinal, 59

Ordinate set, 174, 399

Oriented interval, 202

Orthogonal projection, 80

Orthogonality, 79

Orthogonality relations, 82

Orthonormal basis, 85

Orthonormal set, 82

Ostrowski, A., 321

Outer factor, 344

Outer function, 342

Outer measure, 397

Outer regular set, 47

Overconvergence, 321

Paley-Wiener theorems, 372, 375

Parallelogram law, 80

Parameter interval, 200

Parseval's identity, 85, 91, 187, 212

Partial derivative, 231

Partial fractions, 267

Partial product, 298

Partial sum of Fourier series, 83, 91, 101, 354

Partially ordered set, 86

Partition:

of set, 116

of unity, 40

Path, 200

Periodic function, 2, 88, 93, 156

Perron, O., 144

Phragmen-Lindelöf method, 256

$\pi, 3$

Picard theorem, 332

Plancherel theorem, 186

Plancherel transform, 186

Pointwise limit, 14

Poisson integral, 112, 233, 240, 252

Poisson kernel, 111, 233

Poisson summation formula, 195

Polar coordinates, 175

Polar representation of measure, 125

Pole, 210, 267

Polynomial, 110

Positive linear functional, 34, 40, 109

Positive measure, 16

Positive part, 15

Positive variation, 119

Positively oriented circle, 202

Power series, 198

Pre-image, 7

Preservation of angles, 278

Prime end, 401

Principal ideal, 305

Principal part, 211

Product measure, 164

Projection, 80

Proper subset, 6

Punctured disc, 196

Quasi-analytic class, 378

Quotient algebra, 363

Quotient norm, 363

Quotient space, 363

Rademacher functions, 158

Radial limit, 239
Radial maximal function, 241

Radical, 369

Radius of convergence, 198

Radon-Nikodym derivative, 122, 140

Radon-Nikodym theorem, 121

Rado's theorem, 263

Ramey, W., 400

Range, 7

Rational function, 267, 276

Real line, 7

Real-linear functional, 105

Real measure, 16

Rectangle, 160

Reflection principle, 237

Region, 197

Regular Borel measure, 47

Regular point, 319

Removable set, 333

Removable singularity, 210

Representable by power series, 198

Representat:on theorems, 40, 81, 130

Representing measure, 109, 398

Residue, 224

Residue theorem, 224

Resolvent, 369

Restriction, 109

Rickert, N. W., 399

Riemann integral, 5, 34

Riemann-Lebesgue lemma, 103

Riemann mapping theorem, 283, 295

Riemann sphere, 266

Riesz, F., 34, 341, 397, 400

Riesz, M., 341, 350, 401

Riesz-Fischer theorem, 85, 91

Riesz representation theorem, 34, 40, 130

Right-hand derivative, 399

Root test, 198

Rotation, 279

Rotation-invariance, 51, 195

Rouché's theorem, 225, 229

Rubel, L. A., 401

Runge's theorem, 270, 272, 387

Saks, S., 397

Scalar, 33

Scalar product, 76

Schwartz, J. T., 399

Schwarz, H. A., 400

Schwarz inequality, 49, 63, 77

Schwarz lemma, 254

Schwarz reflection principle, 237

Second category, 98

Section, 161

Segment, 7

Separable space, 92, 247

Set, 6

Borel, 13

closed, 13, 35

compact, 36

connected, 196

convex, 79

dense, 58

elementary, 161

empty, 6

$F_{\sigma}, 12$

$G_{\delta}, 12$

inner regular, 47

measurable, 8,51

nonmeasurable, 53, 157, 167

open, 7

outer regular, 47

partially ordered, 86

strictly convex, 112

totally disconnected, 58

totally ordered, 87

Shift operator, 347

Sierpinski, W., 167, 399

$\sigma$-algebra, 8

$\sigma$-compact set, 47

$\sigma$-finite measure, 47

$\sigma$-ring, 397

Signed measure, 119

Simple boundary point, 289

Simple function, 15

Simply connected, 222, 274

Sine, 2, 265, 316

Singer, I. M., 398, 402

Singular measure, 120

Singular point, 319

Snow, D. O., 399

Space:

Banach, 95

compact, 35

complete metric, 67

dual, 108, 112, 127, 130

Hausdorff, 36

Hilbert, 77

inner product, 76

locally compact, 36

measurable, 8

metric, 9

normed linear, 95

separable, 92

topological, 8

unitary, 76

vector, 33

Span, 82

Spectral norm, 360
Spectral radius, 360

Spectrum, 357

Square root, 274

Stoilov's theorem, 400

Stout, E. L., 401

Strictly convex set, 112

Stromberg, K., 399

Subadditivity, 397

Subchain, 395

Subharmonic function, 335

Subset, 6

Subspace, 78

Sum of paths, 217

Summability method, 114

Summable function, 24

Supremum, 7

Supremum norm, 70

Support, 38, 58

Symmetric derivative, 136

Szasz, O., 401

Tauberian theorem, 402

Taylor's formula, 379

Thorin, G. O., 401

Three-circle theorem, 264

Tietze's extension theorem, 389

Topological space, 8

Topology, 8

Total variation, 117,148

Totally disconnected set, 58

Totally ordered set, 87

Tower, 395

Transcendental number, 170

Transformation:

affine, 377

bounded linear, 96

differentiable, 150

linear, 33

linear fractional, 279, 296

(See also Function)

Transitivity, 324

Translate:

of function, 182

of set, 50

Translation-invariance, 51

Translation-invariant measure, 51

Translation-invariant subspace, 188

Triangle, 202

Triangle inequality, 9, 49, 77

Trigonometric polynomial, 88

Trigonometric system, 89

Ullrich, D., 400

Uniform boundedness principle, 98

Uniform continuity, 51

Uniform integrability, 133

Union, 6

Unit, 357

Unit ball, 96

Unit circle, 2

Unit disc, 110

Unit mass, 17

Unit vector, 96

Unitary space, 76

Upper half plane, 237

Upper limit, 14

Upper semicontinuous function, 37

Urysohn's lemma, 39

Vanish at infinity, 70

Varberg, D. E., 399

Vector space, 33

Villani, A., 398

Vitali-Carathéodory theorem, 56
Vitali's theorem, 133

Volume, 50

von Neumann, J., 122

Walker, P. L., 399

Weak convergence, 245, 246, 251

Weak $L^{1}, 138$

Weierstrass, K., 301, 332

Weierstrass approximation theorem, 312, 387

Weierstrass factorization theorem, 303

Wermer, J., 402

Wiener, N., 367

Winding number, 204

Young, W. H., 5, 400

Zermelo, E., 403

Zero set, 209

Zorn's lemma, 87

Zygmund, A., 401

