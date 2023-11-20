
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