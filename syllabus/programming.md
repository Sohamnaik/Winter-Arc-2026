# Programming — 0 to Hero (Python)

Language: **Python**, starting on Codecademy, then moving straight into
real computational-biology work using Soham's CompBio Mastery roadmap.
Check things off as they move from "seen" to "actually used in something."

---

## Phase 0 — Setup
- [ ] Install Python 3 and VS Code
- [ ] Create a Codecademy account
- [ ] Create a GitHub account and install Git
- [ ] Open a terminal and confirm `python --version` and `git --version` both work

## Phase 1 — Codecademy: Learn Python 3 (absolute basics)
- [ ] Variables and data types (int, float, str, bool)
- [ ] Strings and string methods
- [ ] Conditionals (if / elif / else) and booleans
- [ ] Loops (for, while)
- [ ] Lists and list methods
- [ ] Dictionaries and sets
- [ ] Functions and scope
- [ ] Classes and basic OOP
- [ ] File I/O — reading and writing files
- [ ] Modules and imports
- [ ] Complete the full Codecademy "Learn Python 3" course and its final project

## Phase 2 — Thinking Like a Computer (CompBio Phase 1, 8-10 wks)
- [ ] Recognize every wet-lab protocol as an algorithm (loops, conditionals, functions)
- [ ] NumPy — arrays and basic operations
- [ ] Pandas — DataFrames: load, filter, group, merge a CSV
- [ ] Matplotlib / Seaborn — basic plots (line, bar, scatter)
- [ ] Bash basics — navigation, piping, redirects
- [ ] Git & GitHub workflow — branches, PRs, rebasing, resolving conflicts
- [ ] Project 1A — COVID-19 growth curve analyser: WHO case data, exponential vs. logistic fit, five countries (pandas, scipy.optimize)
- [ ] Project 1B — reproducible lab pipeline: messy plate-reader/FACS CSV → cleaned, normalised, versioned figure (pandas, git)

## Phase 3 — Data Structures & Algorithms (foundation)
- [ ] Arrays and strings
- [ ] Hash maps / dictionaries
- [ ] Stacks and queues
- [ ] Trees (binary trees, BSTs)
- [ ] Graphs — representations and traversal
- [ ] Heaps
- [ ] Sorting algorithms
- [ ] Searching algorithms
- [ ] Recursion
- [ ] Dynamic programming — basics
- [ ] Greedy algorithms
- [ ] BFS / DFS
- [ ] Big-O / complexity analysis — able to state and justify it for any solution you write

## Phase 4 — Algorithms, Data Structures & Bioinformatics (10-12 wks)
- [ ] Big-O intuition — why hash indexing (O(1)) beats naive search (O(n)); this is why BLAST is fast
- [ ] Dynamic programming for sequence alignment — Needleman-Wunsch, Smith-Waterman, Viterbi
- [ ] Graph algorithms on biological networks — centrality, Louvain community detection
- [ ] Sequence data structures — suffix arrays, BWT, k-mer hash tables (what powers BWA, Bowtie, STAR)
- [ ] Hidden Markov Models — gene finding, CpG islands, domain annotation
- [ ] Project 4A — Needleman-Wunsch + Smith-Waterman alignment with BLOSUM62, tested on real viral genomes (Python, NumPy)
- [ ] Project 4B — STRING PPI network analysis: degree, clustering, betweenness, Louvain communities, GO enrichment (NetworkX)
- [ ] Project 4C — K-mer genome indexer: FASTA → hash index, benchmarked against naive O(n) search (Python)

## Phase 5 — Machine Learning & Deep Learning (12-14 wks)
- [ ] Classical ML — logistic regression, random forest, gradient boosting, bias-variance, cross-validation (scikit-learn)
- [ ] Neural nets from scratch — forward pass, loss, backprop, SGD, weight init, no framework first (NumPy)
- [ ] CNNs — sliding filters over microscopy images, Hi-C contact maps, splice-site prediction (PyTorch)
- [ ] RNNs / LSTMs — sequential state, time-series expression, EHR modelling, why gradients vanish
- [ ] Transformers / attention — scaled dot-product, multi-head, positional encoding
- [ ] Embeddings — dense representations of sequences/molecules/cells, contrastive learning, UMAP
- [ ] Project 5A — Tox21 toxicity classifier: Morgan fingerprints (RDKit), logistic/RF/GBM compared, AUC-ROC across 12 endpoints
- [ ] Project 5B — Splice-site CNN: one-hot DNA → donor/acceptor classification (GENCODE) (PyTorch)
- [ ] Project 5C — Fine-tune ESM2-650M with LoRA on thermostability data (ProtaBank), Spearman eval, UMAP of embeddings
- [ ] Project 5D — Multi-head attention from scratch → small transformer encoder on protein secondary structure (NetSurf-2)

## Phase 6 — Capstone: Computational Biology for AI Labs (12-16 wks)
- [ ] Read the AlphaFold2 paper (Jumper et al. 2021) section by section — EvoFormer, outer product mean, triangle updates, IPA, FAPE loss
- [ ] Graph neural networks for molecules — message passing, GCN vs GAT vs MPNN
- [ ] Generative models — VAEs and diffusion for sequence/structure generation (conceptual: RFdiffusion)
- [ ] Reproducible research practices — experiment tracking, dataset versioning, environment reproducibility (MLflow, DVC, Docker)
- [ ] Project 6A — EvoFormer block reimplementation, unit-tested against the published equations, plus an 800-1200 word blog post
- [ ] Project 6B — Message-passing GNN on MoleculeNet (BBBP, Lipophilicity, ESOL) vs. fingerprint-MLP baseline, W&B tracked
- [ ] Project 6C — ESM2-3B + LoRA fine-tuned for GO molecular-function classification, macro-F1, attention-residue attribution, 2-4 page write-up
- [ ] Project 6D — Merged open-source PR to Biopython/OpenFold/ESMFold, or a packaged PyPI tool, or a docs tutorial
- [ ] Stretch goal — port one Phase 5/6 project to JAX/Flax (relevant if aiming at DeepMind/Isomorphic-style roles)

## Publication & Portfolio
- [ ] Identify a publication pathway — tool/methods paper, data re-analysis paper, or wet-lab collaboration
- [ ] Post a preprint to bioRxiv after Phase 5/6 work — establishes priority, read directly by AI-lab hiring managers
- [ ] Build 6+ GitHub repos, each with a README (biological motivation + computational approach), install instructions, tests, example outputs
- [ ] Publish at least 2 Hugging Face model cards (e.g. the ESM2 LoRA adapter, the GNN) with description, training data, eval results, limitations
- [ ] Write one blog post per phase (6 total), aimed at a technically literate biologist who doesn't code

## Open Source Contributions (ongoing, separate track)
- [ ] Find 5 candidate repos — good first issues, active maintainers
- [ ] Read CONTRIBUTING.md and set up the dev environment for each
- [ ] First issue triaged / commented on
- [ ] First PR opened
- [ ] First PR merged
- [ ] Second contribution (bigger than the first)
- [ ] Ongoing — one meaningful contribution per month for the rest of the arc

## Log of contributions

| Date | Repo | What | Link |
|---|---|---|---|
| | | | |
