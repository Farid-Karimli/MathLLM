
1.29 Theorem If $a$ and $b$ are real, then $(a, b)=a+b i$.

Proof

$$
\begin{aligned}
a+b i & =(a, 0)+(b, 0)(0,1) \\
& =(a, 0)+(0, b)=(a, b) .
\end{aligned}
$$

1.30 Definition If $a, b$ are real and $z=a+b i$, then the complex number $\bar{z}=a-b i$ is called the conjugate of $z$. The numbers $a$ and $b$ are the real part and the imaginary part of $z$, respectively.

We shall occasionally write

$$
a=\operatorname{Re}(z), \quad b=\operatorname{Im}(z)
$$

1.31 Theorem If $z$ and $w$ are complex, then

(a) $\overline{z+w}=\bar{z}+\bar{w}$

(b) $\overline{z w}=\bar{z} \cdot \bar{w}$,

(c) $z+\bar{z}=2 \operatorname{Re}(z), z-\bar{z}=2 i \operatorname{Im}(z)$,

(d) $z \bar{z}$ is real and positive (except when $z=0$ ).

Proof $(a),(b)$, and $(c)$ are quite trivial. To prove $(d)$, write $z=a+b i$, and note that $z \bar{z}=a^{2}+b^{2}$.

1.32 Definition If $z$ is a complex number, its absolute value $|z|$ is the nonnegative square root of $z \bar{z}$; that is, $|z|=(z \bar{z})^{1 / 2}$.

The existence (and uniqueness) of $|z|$ follows from Theorem 1.21 and part $(d)$ of Theorem 1.31.

Note that when $x$ is real, then $\bar{x}=x$, hence $|x|=\sqrt{x^{2}}$. Thus $|x|=x$ if $x \geq 0,|x|=-x$ if $x<0$.

1.33 Theorem Let $z$ and $w$ be complex numbers. Then

(a) $|z|>0$ unless $z=0,|0|=0$,

(b) $|\bar{z}|=|z|$,

(c) $|z w|=|z||w|$,

(d) $|\operatorname{Re} z| \leq|z|$

(e) $|z+w| \leq|z|+|w|$.

Proof $(a)$ and $(b)$ are trivial. Put $z=a+b i, w=c+d i$, with $a, b, c, d$ real. Then

$$
|z w|^{2}=(a c-b d)^{2}+(a d+b c)^{2}=\left(a^{2}+b^{2}\right)\left(c^{2}+d^{2}\right)=|z|^{2}|w|^{2}
$$

or $|z w|^{2}=(|z||w|)^{2}$. Now $(c)$ follows from the uniqueness assertion of Theorem 1.21.

To prove $(d)$, note that $a^{2} \leq a^{2}+b^{2}$, hence

$$
|a|=\sqrt{a^{2}} \leq \sqrt{a^{2}+b^{2}} \text {. }
$$

To prove (e), note that $\bar{z} w$ is the conjugate of $z \bar{w}$, so that $z \bar{w}+\bar{z} w=$ $2 \operatorname{Re}(z \bar{w})$. Hence

$$
\begin{aligned}
|z+w|^{2} & =(z+w)(\bar{z}+\bar{w})=z \bar{z}+z \bar{w}+\bar{z} w+w \bar{w} \\
& =|z|^{2}+2 \operatorname{Re}(z \bar{w})+|w|^{2} \\
& \leq|z|^{2}+2|z \bar{w}|+|w|^{2} \\
& =|z|^{2}+2|z||w|+|w|^{2}=(|z|+|w|)^{2} .
\end{aligned}
$$
