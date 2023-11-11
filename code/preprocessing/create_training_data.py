import os
from openai import AsyncOpenAI
import asyncio
from dotenv import load_dotenv
from tqdm import tqdm
import json
import re
import csv
from multiprocessing import Pool
# Set your OpenAI API key here

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY') 
client = AsyncOpenAI()

chunksize = 4096

function_schema = {
    "name": "parse_math_text",
    "description": "A function that takes as input a chapter from a math text and returns 4 dictionaries with theorems, definitions, corollaries, and propositions.",
    "parameters": {
        "type": "object",
        "properties": {
            "theorems": {
                "type": "object",
                "description": "Dictionary of theorems, keyed by theorem number and letter. Each value is an object with the theorem statement and its proof.",
                "properties": {
                    "statement": {
                        "type": "string",
                        "description": "The statement of the theorem."
                    },
                    "proof": {
                        "type": ["string", "null"],
                        "description": "The proof of the theorem. If the proof is not provided, this will be null."
                    }
                }
            },
            "definitions": {
                "type": "object",
                "description": "Dictionary of definitions, keyed by definition number and letter. Each value is the statement of the definition, including any notes on notation or common usage."
            },
            "corollaries": {
                "type": "object",
                "description": "Dictionary of corollaries, similar to theorems, keyed by corollary number and letter. Each value is an object with the corollary statement and its proof.",
                "properties": {
                    "statement": {
                        "type": "string",
                        "description": "The statement of the corollary."
                    },
                    "proof": {
                        "type": ["string", "null"],
                        "description": "The proof of the corollary. If the proof is not provided, this will be null."
                    }
                }
            },
            "propositions": {
                "type": "object",
                "description": "Dictionary of propositions, structured like theorems, keyed by proposition number and letter. Each value is an object with the proposition statement and its proof.",
                "properties": {
                    "statement": {
                        "type": "string",
                        "description": "The statement of the proposition."
                    },
                    "proof": {
                        "type": ["string", "null"],
                        "description": "The proof of the proposition. If the proof is not provided, this will be null."
                    }
                }
            }
        },
        "required": ["theorems", "definitions", "corollaries", "propositions"]
    }
}



with open('example_1.md', 'r') as f:
    content_example = f.read()

theorems_e = {"1.29": ("If $a$ and $b$ are real, then $(a, b)=a+b i$", "$$\n\\begin{aligned}\na+b i & =(a, 0)+(b, 0)(0,1) \\\\\n& =(a, 0)+(0, b)=(a, b) .\n\\end{aligned}\n$$"), 
            "1.31 (a)": ("If $z$ and $w$ are complex, then $\\overline{z+w}=\\bar{z}+\\bar{w}$", None),
            "1.31 (b)": ("If $z$ and $w$ are complex, then $\\overline{z w}=\\bar{z} \\cdot \\bar{w}$,$", None),
            "1.31 (c)": ("If $z$ and $w$ are complex, $z+\\bar{z}=2 \\operatorname{Re}(z), z-\\bar{z}=2 i \\operatorname{Im}(z)$,", None),
             "1.31 (d)": ("If $z$ and $w$ are complex, then $z \\bar{z}$ is real and positive (except when $z=0$ ).", "write $z=a+b i$, and note that $z \\bar{z}=a^{2}+b^{2}$.") }

definitions_e = {"1.30": "If $a, b$ are real and $z=a+b i$, then the complex number $\\bar{z}=a-b i$ is called the conjugate of $z$. The numbers $a$ and $b$ are the real part and the imaginary part of $z$, respectively.\n\nWe shall occasionally write\n\n$$\na=\\operatorname{Re}(z), \\quad b=\\operatorname{Im}(z)\n$$", 
               "1.32": "Definition If $z$ is a complex number, its absolute value $|z|$ is the nonnegative square root of $z \\bar{z}$; that is, $|z|=(z \\bar{z})^{1 / 2}$.\n\nThe existence (and uniqueness) of $|z|$ follows from Theorem 1.21 and part $(d)$ of Theorem 1.31.\n\nNote that when $x$ is real, then $\\bar{x}=x$, hence $|x|=\\sqrt{x^{2}}$. Thus $|x|=x$ if $x \\geq 0,|x|=-x$ if $x<0$."}

corollaries_e = {}

propositions_e = {}

example_output = {"theorems": theorems_e, "definitions": definitions_e, "corollaries": corollaries_e, "propositions": propositions_e}

example_output_empty = {"theorems": {}, "definitions": {}, "corollaries": {}, "propositions": {}}

example_2 = "5.12 Theorem Suppose $f$ is a real differentiable function on $[a, b]$ and suppose $f^{\\prime}(a)<\\lambda<f^{\\prime}(b)$. Then there is a point $x \\in(a, b)$ such that $f^{\\prime}(x)=\\lambda$.\n\nA similar result holds of course if $f^{\\prime}(a)>f^{\\prime}(b)$.\n\nProof Put $g(t)=f(t)-\\lambda t$. Then $g^{\\prime}(a)<0$, so that $g\\left(t_{1}\\right)<g(a)$ for some $t_{1} \\in(a, b)$, and $g^{\\prime}(b)>0$, so that $g\\left(t_{2}\\right)<g(b)$ for some $t_{2} \\in(a, b)$. Hence $g$ attains its minimum on $[a, b]$ (Theorem 4.16) at some point $x$ such that $a<x<b$. By Theorem 5.8, $g^{\\prime}(x)=0$. Hence $f^{\\prime}(x)=\\lambda$.\n\nCorollary If $f$ is differentiable on $[a, b]$, then $f^{\\prime}$ cannot have any simple discontinuities on $[a, b]$.\n\nBut $f^{\\prime}$ may very well have discontinuities of the second kind.\n\n## L'HOSPITAL'S RULE\n\nThe following theorem is frequently useful in the evaluation of limits."

output_2 = '{"theorems": {"5.12": ["Suppose $f$ is a real differentiable function on $[a, b]$ and suppose $f^{\\prime}(a)<\\\\lambda<f^{\\prime}(b)$. Then there is a point $x \\\\in(a, b)$ such that $f^{\\prime}(x)=\\\\lambda$.", "Put $g(t)=f(t)-\\\\lambda t$. Then $g^{\\prime}(a)<0$, so that $g\\\\left(t_{1}\\\\right)<g(a)$ for some $t_{1} \\\\in(a, b)$, and $g^{\\prime}(b)>0$, so that $g\\\\left(t_{2}\\\\right)<g(b)$ for some $t_{2} \\\\in(a, b)$. Hence $g$ attains its minimum on $[a, b]$ (Theorem 4.16) at some point $x$ such that $a<x<b$. By Theorem 5.8, $g^{\\prime}(x)=0$. Hence $f^{\\prime}(x)=\\\\lambda$."], "L\'HOSPITAL\'S RULE": "The following theorem is frequently useful in the evaluation of limits."}, "definitions": {}, "corollaries": {"Corollary": "If $f$ is differentiable on $[a, b]$, then $f^{\\prime}$ cannot have any simple discontinuities on $[a, b]$. But $f^{\\prime}$ may very well have discontinuities of the second kind."}, "propositions": {}}'

example_3 = '10.23 Theorem Suppose $T$ is a $\\mathscr{C}^{\\prime}$-mapping of an open set $E \\subset R^{n}$ into an open set $V \\subset R^{m}, S$ is a $\\mathscr{C}^{\\prime}$-mapping of $V$ into an open set $W \\subset R^{p}$, and $\\omega$ is a $k$-form in $W$, so that $\\omega_{S}$ is a $k$-form in $V$ and both $\\left(\\omega_{S}\\right)_{T}$ and $\\omega_{S T}$ are $k$-forms in $E$, where $S T$ is defined by $(S T)(\\mathbf{x})=S(T(\\mathbf{x}))$. Then\n\n$$\n\\left(\\omega_{S}\\right)_{T}=\\omega_{S T}\n$$\n\nProof If $\\omega$ and $\\lambda$ are forms in $W$, Theorem 10.22 shows that\n\n$$\n\\left((\\omega \\wedge \\lambda)_{S}\\right)_{T}=\\left(\\omega_{S} \\wedge \\lambda_{S}\\right)_{T}=\\left(\\omega_{S}\\right)_{T} \\wedge\\left(\\lambda_{S}\\right)_{T}\n$$\n\nand\n\n$$\n(\\omega \\wedge \\lambda)_{S T}=\\omega_{S T} \\wedge \\lambda_{S T}\n$$\n\nThus if (71) holds for $\\omega$ and for $\\lambda$, it follows that (71) also holds for $\\omega \\wedge \\lambda$. Since every form can be built up from 0 -forms and 1 -forms by addition and multiplication, and since (71) is trivial for 0 -forms, it is enough to prove (71) in the case $\\omega=d z_{q}, q=1, \\ldots, p$. (We denote the points of $E, V, W$ by $\\mathbf{x}, \\mathbf{y}, \\mathbf{z}$, respectively.)\n\nLet $t_{1}, \\ldots, t_{m}$ be the components of $T$, let $s_{1}, \\ldots, s_{p}$ be the components of $S$, and let $r_{1}, \\ldots, r_{p}$ be the components of $S T$. If $\\omega=d z_{q}$, then\n\n$$\n\\omega_{s}=d s_{q}=\\sum_{j}\\left(D_{j} s_{q}\\right)(\\mathbf{y}) d y_{j}\n$$\n\nso that the chain rule implies\n\n$$\n\\begin{aligned}\n\\left(\\omega_{S}\\right)_{T} & =\\sum_{j}\\left(D_{j} s_{q}\\right)(T(\\mathbf{x})) d t_{j} \\\\\n& =\\sum_{j}\\left(D_{j} s_{q}\\right)(T(\\mathbf{x})) \\sum_{i}\\left(D_{i} t_{j}\\right)(\\mathbf{x}) d x_{i} \\\\\n& =\\sum_{i}\\left(D_{i} r_{q}\\right)(\\mathbf{x}) d x_{i}=d r_{q}=\\omega_{S T} .\n\\end{aligned}\n$$'

output_3 = '{"theorems": {"10.23": ["Suppose $T$ is a $\\\\mathscr{C}^{\\\\prime}$-mapping of an open set $E \\\\subset R^{n}$ into an open set $V \\\\subset R^{m}, S$ is a $\\\\mathscr{C}^{\\\\prime}$-mapping of $V$ into an open set $W \\\\subset R^{p}$, and $\\\\omega$ is a $k$-form in $W$, so that $\\\\omega_{S}$ is a $k$-form in $V$ and both $\\\\left(\\\\omega_{S}\\\\right)_{T}$ and $\\\\omega_{S T}$ are $k$-forms in $E$, where $S T$ is defined by $(S T)(\\\\mathbf{x})=S(T(\\\\mathbf{x}))$. Then\\n\\n$$\\n\\\\left(\\\\omega_{S}\\\\right)_{T}=\\\\omega_{S T}\\n$$","If $\\omega$ and $\\lambda$ are forms in $W$, Theorem 10.22 shows that\n\n$$\n\\left((\\omega \\wedge \\lambda)_{S}\\right)_{T}=\\left(\\omega_{S} \\wedge \\lambda_{S}\\right)_{T}=\\left(\\omega_{S}\\right)_{T} \\wedge\\left(\\lambda_{S}\\right)_{T}\n$$\n\nand\n\n$$\n(\\omega \\wedge \\lambda)_{S T}=\\omega_{S T} \\wedge \\lambda_{S T}\n$$\n\nThus if (71) holds for $\\omega$ and for $\\lambda$, it follows that (71) also holds for $\\omega \\wedge \\lambda$. Since every form can be built up from 0 -forms and 1 -forms by addition and multiplication, and since (71) is trivial for 0 -forms, it is enough to prove (71) in the case $\\omega=d z_{q}, q=1, \\ldots, p$. (We denote the points of $E, V, W$ by $\\mathbf{x}, \\mathbf{y}, \\mathbf{z}$, respectively.)\n\nLet $t_{1}, \\ldots, t_{m}$ be the components of $T$, let $s_{1}, \\ldots, s_{p}$ be the components of $S$, and let $r_{1}, \\ldots, r_{p}$ be the components of $S T$. If $\\omega=d z_{q}$, then\n\n$$\n\\omega_{s}=d s_{q}=\\sum_{j}\\left(D_{j} s_{q}\\right)(\\mathbf{y}) d y_{j}\n$$\n\nso that the chain rule implies\n\n$$\n\\begin{aligned}\n\\left(\\omega_{S}\\right)_{T} & =\\sum_{j}\\left(D_{j} s_{q}\\right)(T(\\mathbf{x})) d t_{j} \\\\\n& =\\sum_{j}\\left(D_{j} s_{q}\\right)(T(\\mathbf{x})) \\sum_{i}\\left(D_{i} t_{j}\\right)(\\mathbf{x}) d x_{i} \\\\\n& =\\sum_{i}\\left(D_{i} r_{q}\\right)(\\mathbf{x}) d x_{i}=d r_{q}=\\omega_{S T} .\n\\end{aligned}\n$$" ], "definitions": {}, "corollaries": {}, "propositions": {}}'

with open('example_2.md', 'r') as f:
    example_4 = f.read()

output_4 = {'theorems': {}, 'definitions': {'2.18 (a)': 'For a metric space X and a point $p \\in X$:A neighborhood of $p$ is a set $N_{r}(p)$ consisting of all $q$ such that $d(p, q)<r$, for some $r>0$. The number $r$ is called the radius of $N_{r}(p)$.', '2.18 (b)': 'For a metric space X and a point $p \\in X$: A point $p$ is a limit point of the set $E$ if every neighborhood of $p$ contains a point $q \\neq p$ such that $q \\in E$.', '2.18 (c)': 'For a metric space X and a point $p \\in X$, and $E \\subset X$: If $p \\in E$ and $p$ is not a limit point of $E$, then $p$ is called an isolated point of $E$.', '2.18 (d)': 'For a metric space X and $E \\subset X$: $E$ is closed if every limit point of $E$ is a point of $E$.', '2.18 (e)': 'For a metric space X and a point $p \\in X$, and $E \\subset X$: A point $p$ is an interior point of $E$ if there is a neighborhood $N$ of $p$ such that $N \\subset E$.', '2.18 (f)': 'For a metric space X and $E \\subset X$: $E$ is open if every point of $E$ is an interior point of $E$.', '2.18 (g)': 'For a metric space X and points $p \\in X$, and $E \\subset X$: The complement of $E$ (denoted by $E^{c}$ ) is the set of all points $p \\in X$ such that $p \\notin E$.', '2.18 (h)': 'For a metric space X  $E \\subset X$: $E$ is perfect if $E$ is closed and if every point of $E$ is a limit point of $E$.', '2.18 (i)': 'For a metric space X and $E \\subset X$: $E$ is bounded if there is a real number $M$ and a point $q \\in X$ such that $d(p, q)<M$ for all $p \\in E$.', '2.18 (j)': 'For a metric space X and $E \\subset X$: $E$ is dense in $X$ if every point of $X$ is a limit point of $E$, or a point of $E$ (or both). Let us note that in $R^{1}$ neighborhoods are segments, whereas in $R^{2}$ neighborhoods are interiors of circles.'}, 'corollaries': {}, 'propositions': {}}

example_5 = '\n\n11.45 Theorem Let $\\left\\{\\phi_{n}\\right\\}$ be a complete orthonormal set. If $f \\in \\mathscr{L}^{2}(\\mu)$ and if\n\n$$\nf \\sim \\sum_{n=1}^{\\infty} c_{n} \\phi_{n}\n$$\n\nthen\n\n$$\n\\int_{X}|f|^{2} d \\mu=\\sum_{n=1}^{\\infty}\\left|c_{n}\\right|^{2}\n$$\n\nProof By the Bessel inequality, $\\Sigma\\left|c_{n}\\right|^{2}$ converges. Putting\n\n$$\ns_{n}=c_{1} \\phi_{1}+\\cdots+c_{n} \\phi_{n}\n$$\n\nthe Riesz-Fischer theorem shows that there is a function $g \\in \\mathscr{L}^{2}(\\mu)$ such that\n\n$$\ng \\sim \\sum_{n=1}^{\\infty} c_{n} \\phi_{n}\n$$\n\nand such that $\\left\\|g-s_{n}\\right\\| \\rightarrow 0$. Hence $\\left\\|s_{n}\\right\\| \\rightarrow\\|g\\|$. Since\n\n$$\n\\left\\|s_{n}\\right\\|^{2}=\\left|c_{1}\\right|^{2}+\\cdots+\\left|c_{n}\\right|^{2}\n$$\n\nwe have\n\n$$\n\\int_{X}|g|^{2} d \\mu=\\sum_{n=1}^{\\infty}\\left|c_{n}\\right|^{2}\n$$\n\nNow (106), (108), and the completeness of $\\left\\{\\phi_{n}\\right\\}$ show that $\\|f-g\\|=0$, so that (109) implies (107).\n\nCombining Theorems 11.43 and 11.45 , we arrive at the very interesting conclusion that every complete orthonormal set induces a 1-1 correspondence between the functions $f \\in \\mathscr{L}^{2}(\\mu)$ (identifying those which are equal almost everywhere) on the one hand and the sequences $\\left\\{c_{n}\\right\\}$ for which $\\Sigma\\left|c_{n}\\right|^{2}$ converges, on the other. The representation\n\n$$\nf \\sim \\sum_{n=1}^{\\infty} c_{n} \\phi_{n}\n$$\n\ntogether with the Parseval equation, shows that $\\mathscr{L}^{2}(\\mu)$ may be regarded as an infinite-dimensional euclidean space (the so-called "Hilbert space"), in which the point $f$ has coordinates $c_{n}$, and the functions $\\phi_{n}$ are the coordinate vectors.\n\n## EXERCISES\n\n1. If $f \\geq 0$ and $\\int_{E} f d \\mu=0$, prove that $f(x)=0$ almost everywhere on $E$. Hint: Let $E_{n}$ be the subset of $E$ on which $f(x)>1 / n$. Write $A=\\bigcup E_{n}$. Then $\\mu(A)=0$ if and only if $\\mu\\left(E_{n}\\right)=0$ for every $n$.\n2. If $\\int_{A} f d \\mu=0$ for every measurable subset $A$ of a measurable set $E$, then $f(x)=0$ almost everywhere on $E$.\n3. If $\\left\\{f_{n}\\right\\}$ is a sequence of measurable functions, prove that the set of points $x$ at which $\\left\\{f_{n}(x)\\right\\}$ converges is measurable.\n4. If $f \\in \\mathscr{L}(\\mu)$ on $E$ and $g$ is bounded and measurable on $E$, then $f g \\in \\mathscr{L}(\\mu)$ on $E$.\n5. Put\n\n$$\n\\begin{array}{rlrl}\ng(x) & = \\begin{cases}0 & \\left(0 \\leq x \\leq \\frac{1}{2}\\right), \\\\\n1 & \\left(\\frac{1}{2}<x \\leq 1\\right),\\end{cases} \\\\\nf_{2 k}(x) & =g(x) & (0 \\leq x \\leq 1), \\\\\nf_{2 k+1}(x) & =g(1-x) & (0 \\leq x \\leq 1)\n\\end{array}\n$$\n\nShow that\n\n$$\n\\liminf _{n \\rightarrow \\infty} f_{n}(x)=0 \\quad(0 \\leq x \\leq 1)\n$$\n\nbut\n\n$$\n\\int_{0}^{1} f_{n}(x) d x=\\frac{1}{2} .\n$$\n\n[Compare with (77).]\n\n6. Let\n\n$$\nf_{n}(x)= \\begin{cases}\\frac{1}{n} & (|x| \\leq n) \\\\ 0 & (|x|>n)\\end{cases}\n$$\n\nThen $f_{n}(x) \\rightarrow 0$ uniformly on $R^{1}$, but\n\n$$\n\\int_{-\\infty}^{\\infty} f_{n} d x=2 \\quad(n=1,2,3, \\ldots)\n$$\n\n(We write $\\int_{-\\infty}^{\\infty}$ in place of $\\int_{R 1}$.) Thus uniform convergence does not imply dominated convergence in the sense of Theorem 11.32. However, on sets of finite measure, uniformly convergent sequences of bounded functions do satisfy Theorem 11.32.\n\n7. Find a necessary and sufficient condition that $f \\in \\mathscr{R}(\\alpha)$ on $[a, b]$. Hint: Consider Example 11.6(b) and Theorem 11.33.\n8. If $f \\in \\mathscr{R}$ on $[a, b]$ and if $F(x)=\\int_{a}^{x} f(t) d t$, prove that $F^{\\prime}(x)=f(x)$ almost everywhere on $[a, b]$.\n9. Prove that the function $F$ given by (96) is continuous on $[a, b]$.\n10. If $\\mu(X)<+\\infty$ and $f \\in \\mathscr{L}^{2}(\\mu)$ on $X$, prove that $f \\in \\mathscr{L}(\\mu)$ on $X$. If\n\n$$\n\\mu(X)=+\\infty\n$$\n\nthis is false. For instance, if\n\n$$\nf(x)=\\frac{1}{1+|x|}\n$$\n\nthen $f \\in \\mathscr{L}^{2}$ on $R^{1}$, but $f \\notin \\mathscr{L}$ on $R^{1}$.\n\n11. If $f, g \\in \\mathscr{L}(\\mu)$ on $X$, define the distance between $f$ and $g$ by\n\n$$\n\\int_{x}|f-g| d \\mu\n$$\n\nProve that $\\mathscr{L}(\\mu)$ is a complete metric space.\n\n12. Suppose\n\n(a) $|f(x, y)| \\leq 1$ if $0 \\leq x \\leq 1,0 \\leq y \\leq 1$,\n\n(b) for fixed $x, f(x, y)$ is a continuous function of $y$,\n\n(c) for fixed $y, f(x, y)$ is a continuous function of $x$.\n\nPut\n\n$$\ng(x)=\\int_{0}^{1} f(x, y) d y \\quad(0 \\leq x \\leq 1)\n$$\n\nIs $g$ continuous?\n\n13. Consider the functions\n\n$$\nf_{n}(x)=\\sin n x \\quad(n=1,2,3, \\ldots,-\\pi \\leq x \\leq \\pi)\n$$\n\nas points of $\\mathscr{L}^{2}$. Prove that the set of these points is closed and bounded, but not compact.\n\n14. Prove that a complex function $f$ is measurable if and only if $f^{-1}(V)$ is measurable for every open set $V$ in the plane.\n15. Let $\\mathscr{R}$ be the ring of all elementary subsets of $(0,1]$. If $0<a \\leq b \\leq 1$, define\n\n$$\n\\phi([a, b])=\\phi([a, b))=\\phi((a, b])=\\phi((a, b))=b-a,\n$$\n\nbut define\n\n$$\n\\phi((0, b))=\\phi((0, b])=1+b\n$$\n\nif $0<b \\leq 1$. Show that this gives an additive set function $\\phi$ on $\\mathscr{R}$, which is not regular and which cannot be extended to a countably additive set function on a $\\sigma$-ring.\n\n16. Suppose $\\left\\{n_{k}\\right\\}$ is an increasing sequence of positive integers and $E$ is the set of all $x \\in(-\\pi, \\pi)$ at which $\\left\\{\\sin n_{k} x\\right\\}$ converges. Prove that $m(E)=0$. Hint: For every $A \\subset E$,\n\n$$\n\\int_{A} \\sin n_{k} x d x \\rightarrow 0\n$$\n\nand\n\n$$\n2 \\int_{A}\\left(\\sin n_{k} x\\right)^{2} d x=\\int_{A}\\left(1-\\cos 2 n_{k} x\\right) d x \\rightarrow m(A) \\quad \\text { as } k \\rightarrow \\infty \\text {. }\n$$\n\n17. Suppose $E \\subset(-\\pi, \\pi), m(E)>0, \\delta>0$. Use the Bessel inequality to prove that there are at most finitely many integers $n$ such that $\\sin n x \\geq \\delta$ for all $x \\in E$.\n18. Suppose $f \\in \\mathscr{L}^{2}(\\mu), g \\in \\mathscr{L}^{2}(\\mu)$. Prove that\n\n$$\n\\left|\\int f g d \\mu\\right|^{2}=\\int|f|^{2} d \\mu \\int|g|^{2} d \\mu\n$$\n\nif and only if there is a constant $c$ such that $g(x)=c f(x)$ almost everywhere. (Compare Theorem 11.35.)\n\n'

output_5 = {"theorems": {"11.45": ("Let $\\left\\{\\phi_{n}\\right\\}$ be a complete orthonormal set. If $f \\in \\mathscr{L}^{2}(\\mu)$ and if\n\n$$\nf \\sim \\sum_{n=1}^{\\infty} c_{n} \\phi_{n}\n$$\n\nthen\n\n$$\n\\int_{X}|f|^{2} d \\mu=\\sum_{n=1}^{\\infty}\\left|c_{n}\\right|^{2}\n$$\n\n", "By the Bessel inequality, $\\Sigma\\left|c_{n}\\right|^{2}$ converges. Putting\n\n$$\ns_{n}=c_{1} \\phi_{1}+\\cdots+c_{n} \\phi_{n}\n$$\n\nthe Riesz-Fischer theorem shows that there is a function $g \\in \\mathscr{L}^{2}(\\mu)$ such that\n\n$$\ng \\sim \\sum_{n=1}^{\\infty} c_{n} \\phi_{n}\n$$\n\nand such that $\\left\\|g-s_{n}\\right\\| \\rightarrow 0$. Hence $\\left\\|s_{n}\\right\\| \\rightarrow\\|g\\|$. Since\n\n$$\n\\left\\|s_{n}\\right\\|^{2}=\\left|c_{1}\\right|^{2}+\\cdots+\\left|c_{n}\\right|^{2}\n$$\n\nwe have\n\n$$\n\\int_{X}|g|^{2} d \\mu=\\sum_{n=1}^{\\infty}\\left|c_{n}\\right|^{2}\n$$\n\nNow (106), (108), and the completeness of $\\left\\{\\phi_{n}\\right\\}$ show that $\\|f-g\\|=0$, so that (109) implies (107).")}, "definitions": {}, "corollaries": {}, "propositions": {}}

def create_sample_resopnses(json_input):
    return {"role": "assistant", "content": None, "function_call": {"name": "parse_math_text", "arguments": json_input}}

async def extract_theorems(chapter_text, output_dir):
    global content_example, example_output, example_2, output_2, example_3, output_3, example_4, output_4, example_5, output_5
    while True:
        try: 
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                {"role": "system", "content": "You are a machine that takes as input chapters from a math text. \
                You must extract the relevant data from this input to use as arguments to pass into the given function provided.\
                If the theorem/corollary/definition/proposition has multiple parts, i.e. (a), (b), (c), etc., then \
                 you must parse the main statement and add the necessary information from it to each of the cases, and treat it as its own theorem/corollary/definition/proposition;\
                  e.g. Theorem 10 (a), Theorem 10 (b), etc. .\
                  If the chapter does not seem like it is from a math text, it may be the appendix, introduction\
                or some other part of the book that hasn't gotten to the material yet, then just pass in empty arguments\
                to the function and nothing else."},
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + content_example},
                create_sample_resopnses(json.dumps(example_output)),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + example_2},
                create_sample_resopnses(output_2),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + example_3},
                create_sample_resopnses(output_3),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + example_4},
                create_sample_resopnses(json.dumps(output_4)),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + example_5},
                create_sample_resopnses(json.dumps(output_5)),
                {"role": "user", "content": "Parse, add, and extract the relevant data from this input to use as arguments to pass into the given function provided:" + chapter_text}],
                functions=[function_schema],
                function_call={"name": "parse_math_text"},
                temperature=0,
            )
            try:
                ret = json.loads(response.choices[0].message.function_call.arguments.strip())
            except Exception as e:
                ret = example_output_empty
                with open(f"{output_dir}/json_errors.log", "a+") as logf:
                    logf.write(f'{e=}, step_reason = {response.choices[0].finish_reason} for text: {chapter_text} \n' + u'\u2500' * 10)
            break
        except Exception as e:
            await asyncio.sleep(60)
    
    # keep track of which keys were not found for which text
    with open(f"{output_dir}/incomplete_dict_errors.log", "a+") as logf:
        for key,_ in example_output_empty.items():
            try:
                ret[key]
            except:
                logf.write(f'{key=} not found for text: {chapter_text} \n' + u'\u2500' * 10)
    return ret

def string_to_dicts(ret_dict):
    # using get with empty dictionary in case gpt fails on output
    return ret_dict.get('theorems',{}), ret_dict.get('definitions', {}), ret_dict.get('corollaries', {}), ret_dict.get('propositions', {})

async def extract_correct_theorems(chunk, output_dir):
    # Await the coroutine and then process its result
    theorems_result = await extract_theorems(chunk, output_dir)
    return string_to_dicts(theorems_result)
    
def get_chunks(document_content):
    global chunksize
    # Pattern to match the start of each relevant section
    pattern = r"^\d+\.\d+ (Theorem|Definition|Proposition|Corollary)"

    # Compile the regex pattern
    compiled_pattern = re.compile(pattern, re.MULTILINE)

    # Find all matches in the document content
    matches = list(compiled_pattern.finditer(document_content))

    # List to hold each chunk of text
    chunks = []

    # Function to find the penultimate occurrence of a pattern
    def find_penultimate(text, pattern):
        matches = list(re.finditer(pattern, text))
        if len(matches) > 1:
            return matches[-2].start()
        else:
            return None

    # Iterate through matches and create chunks of text
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(document_content)

        # Create a chunk and ensure its length is at most 4096 characters
        while end - start > chunksize:
            # Find the penultimate occurrence of any section header within this chunk
            penultimate_match_start = find_penultimate(document_content[start:end], pattern)
            if penultimate_match_start is not None:
                end = start + penultimate_match_start
            else:
                # If there is no penultimate occurrence, we must break at the current match
                break

        # Add the valid chunk to the list
        chunk = document_content[start:end].strip()
        chunks.append(chunk)
        start = end  # Start the next chunk where the last one was cut off
    # Now `chunks` contains all the segments of the document.
   
    return chunks[-1:]

async def process_md_files(folder_path, output_dir):
    global chunksize

    theorem_headers = ['Theorem', 'Statement', 'Proof']
    definition_headers = ['Definition', 'Statement']
    corollary_headers = ['Corollary', 'Statement', 'Proof']
    proposition_headers = ['Proposition', 'Statement', 'Proof']

    with open(f"{output_dir}/theorems.csv", 'w', newline='', encoding='utf-8') as theorems_file, \
         open(f"{output_dir}/definitions.csv", 'w', newline='', encoding='utf-8') as definitions_file, \
         open(f"{output_dir}/corollaries.csv", 'w', newline='', encoding='utf-8') as corollaries_file, \
         open(f"{output_dir}/propositions.csv", 'w', newline='', encoding='utf-8') as propositions_file:

        theorems_writer = csv.DictWriter(theorems_file, fieldnames=theorem_headers)
        definitions_writer = csv.DictWriter(definitions_file, fieldnames=definition_headers)
        corollaries_writer = csv.DictWriter(corollaries_file, fieldnames=corollary_headers)
        propositions_writer = csv.DictWriter(propositions_file, fieldnames=proposition_headers)

        theorems_writer.writeheader()
        definitions_writer.writeheader()
        corollaries_writer.writeheader()
        propositions_writer.writeheader()

        tasks = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Split content into chunks
                chunks = get_chunks(content)
                for chunk in chunks:
                    print(chunk)
                    # Create and append the task
                    task = asyncio.create_task(extract_correct_theorems(chunk, output_dir))
                    tasks.append(task)

        pbar = tqdm(total=len(chunks), desc=f"Processing file {filename}")

        # write to csv ask tasks complete  
        for task in asyncio.as_completed(tasks):
            theorems_temp, definitions_temp, corollaries_temp, propositions_temp = await task
            for key, value in theorems_temp.items():
                theorems_writer.writerow({'Theorem': key, 'Statement': value[0], 'Proof': value[1]})
            for key, value in definitions_temp.items():
                definitions_writer.writerow({'Definition': key, 'Statement': value})
            for key, value in corollaries_temp.items():
                corollaries_writer.writerow({'Corollary': key, 'Statement': value[0], 'Proof': value[1]})
            for key, value in propositions_temp.items():
                propositions_writer.writerow({'Proposition': key, 'Statement': value[0], 'Proof': value[1]})

            pbar.update(1)

        pbar.close()

    return 

def process_book(mathllm_folder, book):
    book_path = os.path.join(mathllm_folder, f'raw_data/{book}')
    output_path = os.path.join(mathllm_folder, f'training_data/{book}')
    asyncio.run(process_md_files(book_path, output_path))

async def main():
    # we are working in MathLLM/code/preprocessing directory
    mathllm_folder = os.path.dirname(os.path.dirname(os.getcwd())) 

    books = [item for item in os.listdir(f'{mathllm_folder}/raw_data') if os.path.isdir(os.path.join(f'{mathllm_folder}/raw_data', item))]
    # get list of books
    
    # create training_data folder if not there already
    training_data_dir = os.path.join(mathllm_folder, "training_data", "")
    if not os.path.exists(training_data_dir):
        os.makedirs(training_data_dir)

    # for every book in raw_data, create corresponding folder in training_data folder
    for book in books:
        temp = os.path.join(training_data_dir, book, "")
        if not os.path.exists(temp):
            os.makedirs(temp)

    for book in books[:1]: 
        await process_md_files(os.path.join(mathllm_folder, f'raw_data/{book}'), os.path.join(mathllm_folder, f'training_data/{book}'))
    

if __name__ == "__main__":
    asyncio.run(main())
