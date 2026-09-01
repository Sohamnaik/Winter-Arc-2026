# Mathematics — 0 to Hero

Not a daily habit checkbox — tracked here as topics, checked off only
once you're actually comfortable, not after reading once. Structure is
drawn from "The Road Ahead" (your compbio × quant synthesis doc), which
maps every math concept to a concrete build.

---

## Phase 0 — Absolute Foundations
(If it's been years since you touched math on purpose, start here.)
- [ ] Arithmetic fluency — mental addition/subtraction/multiplication/division
- [ ] Fractions, decimals, percentages
- [ ] Order of operations (BODMAS/PEMDAS)
- [ ] Solving basic equations for x
- [ ] Exponents and logarithms — rules and manipulation
- [ ] Square roots and radicals
- [ ] Resource: Khan Academy "Algebra Basics" course, start to finish

## Phase 1 — Algebra & Precalculus
- [ ] Functions — domain, range, composition, inverse functions
- [ ] Inequalities — solving and graphing
- [ ] Sequences and series — arithmetic, geometric, basic convergence
- [ ] Coordinate geometry — distance, midpoint, equations of lines/circles
- [ ] Trigonometry basics — sine, cosine, tangent, unit circle, identities
- [ ] Mental arithmetic drills, timed (Zetamac or similar) — 2-3 digit multiplication, percentages, square roots, done in your head. Highest-leverage single habit for speed later.

## Phase 2 — Linear Algebra
- [ ] Vectors and vector spaces — a gene expression profile IS a vector
- [ ] Matrix operations — multiplication, transpose
- [ ] Determinants and inverses
- [ ] Systems of linear equations — and their geometric meaning
- [ ] Eigenvalues and eigenvectors — directions a matrix only scales, not rotates
- [ ] Singular Value Decomposition (SVD) — decomposes structure from noise
- [ ] Dot product and cosine similarity — the basis of every embedding model
- [ ] Resource: 3Blue1Brown, "Essence of Linear Algebra" video series
- [ ] Resource: Gilbert Strang, *Introduction to Linear Algebra* + MIT OCW lectures
- [ ] Build it: PCA from scratch (NumPy, covariance matrix + eigendecomposition) on scRNA-seq data and on MNIST — same code, different data
- [ ] Build it: protein coordinate geometry — parse a PDB file, compute Cα distance matrix, center of mass, radius of gyration, rotation matrix (Biopython)

## Phase 3 — Calculus
- [ ] Limits and continuity
- [ ] Derivatives and the chain rule
- [ ] Optimization — maxima and minima
- [ ] Basic integration — area under a curve
- [ ] Partial derivatives, multivariable calculus basics
- [ ] Gradient, divergence, curl (conceptual — used in transport/fluid processes)
- [ ] Resource: 3Blue1Brown, "Essence of Calculus" video series
- [ ] Build it: gradient descent from scratch — walking downhill on an error surface, the mechanism behind AlphaFold and every neural net
- [ ] Build it: dose-response curve fit, then a 2-layer neural net with manual backpropagation

## Phase 4 — Probability & Statistics
- [ ] Probability axioms, sample spaces, independence
- [ ] Conditional probability and Bayes' theorem — until it's automatic, not derived each time
- [ ] Expected value, variance, linearity of expectation — the single most-tested concept across quant and data interviews
- [ ] Combinatorics — permutations, combinations, stars-and-bars, inclusion-exclusion
- [ ] Common distributions — binomial, Poisson, geometric, normal, uniform, negative binomial, Dirichlet
- [ ] Markov chains and Hidden Markov Models
- [ ] Descriptive statistics — mean, median, variance, correlation, covariance
- [ ] Regression basics — linear regression, R², residuals
- [ ] Hypothesis testing — p-values, confidence intervals, type I/II errors
- [ ] Classic drill problems — urn/dice/coin/card problems, birthday paradox, random walks, gambler's ruin
- [ ] Resource: Sheldon Ross, *A First Course in Probability*
- [ ] Build it: Bayesian variant caller — simulate reads with a Phred error model, compute posterior genotype probability
- [ ] Build it: apply distributions to sequencing error models and expression noise

## Phase 5 — Discrete Math & Number Theory
- [ ] Set theory and logic
- [ ] Divisibility, modular arithmetic, GCD/LCM
- [ ] Graph theory basics — directly useful for programming too
- [ ] Deeper combinatorics practice

## Applied Practice (exam-facing)
- [ ] GATE Engineering Mathematics — previous year questions, round 1
- [ ] GATE Engineering Mathematics — previous year questions, round 2
- [ ] Monthly confidence check-in — reassess weak areas honestly

---

## Optional: Quant / Trading Track
Not required for NET-JRF or GATE — the math above already covers most
of it. Flagged here since the material's already in hand, in case this
path ever becomes relevant.
- [ ] Market making basics — why firms like Jane Street exist (Hull, ch. 1-2)
- [ ] Options fundamentals — calls, puts, strike, expiry, put-call parity
- [ ] Market microstructure — order books, bid-ask spread, adverse selection
- [ ] Game theory basics — Nash equilibrium, simple two-player games
- [ ] Logic and estimation puzzles — Fermi problems, weighing/hat-guessing puzzles
- [ ] Timed practice — Codeforces / AtCoder / LeetCode, narrated out loud
- [ ] Resource: Timothy Crack, *Heard on the Street*
- [ ] Resource: John Hull, *Options, Futures, and Other Derivatives*
