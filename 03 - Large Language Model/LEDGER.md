# Chapter 03 run ledger

Status: `[ ]` not run · `[~]` running/in fix loop · `[x]` run clean, outputs saved · `[C]` needs CUDA (run in Colab) · `[-]` skipped (TODO placeholder)

Runner: `data/run03/run.py` (executes in the notebook's folder, 10 min/cell timeout, key injected in memory only).
Outputs staged in `data/run03/out/`, logs in `data/run03/logs/`; promoted into the repo only after review.

| Notebook | Status | Run time | Notes |
|---|---|---|---|
| 01 - RNN/01 - Vanilla RNN | [x] | 2 min | outputs saved; dinosaur-name model memorises most of the 262 names, sampling at T>1 gives new ones |
| 01 - RNN/02 - RNN with Attention | [x] | 5 min | both attention variants reach 100% test accuracy on date reformatting; outputs saved |
| 02 - Training Strategy/01 - Data Processing | [x] | 1.5 min | outputs saved; C4 3000 docs, heuristics keep 86%, near-dup clusters via MinHash/LSH, perplexity filter |
| 02 - Training Strategy/02 - Distributed Training | [C] |  | needs CUDA for warp occupancy, torch.profiler, memory profiling, Triton cells; run in Colab (MPS run only prints 'CUDA not available' there, so outputs not promoted); fixed DataLoader batch_size typo |
| 02 - Training Strategy/03 - Muon and WSD | [x] | 11 min | outputs saved; Muon reaches AdamW's final loss in 80 vs 200 steps; WSD ≈ cosine; slowest cell 5.5 min |
| 03 - Transformer Models/A01 - Attention Mechanism | [x] | 4 s | outputs saved |
| 03 - Transformer Models/A02 - Transformer | [x] | 2.4 min | outputs saved; 1500 steps, loss 7.5→4.5; greedy reply collapses to 'i dont know' (documented in notebook) |
| 03 - Transformer Models/B01 - BERT | [x] | 5 min | outputs saved; MLM loss 10.3→7.05 in 3 epochs, NSP stays ~50% at this scale |
| 03 - Transformer Models/B02 - ColBERT | [x] | 3.7 min | outputs saved; SciFact nDCG@10 0.646 exact, 0.636 with 2-bit residual index (7.5x smaller) |
| 03 - Transformer Models/C01 - GPT | [x] | 8 min | outputs saved; nanoGPT on tinyshakespeare + looped transformer (loss→0.001, accuracy grows with loop count); fixed n_head config |
| 03 - Transformer Models/C02 - LLaMA | [~] |  | NEEDS FIX: KVCache.__init__() got unexpected kwarg 'device' (class param renamed to DEVICE; update call sites), then rerun. DEVICE constant already added to cell 0 |
| 03 - Transformer Models/C03 - DeepSeek | [x] | 13 s | outputs saved; fixed RoPE helper device parameter |
| 03 - Transformer Models/C04 - Qwen | [x] | 1 min | outputs saved; Qwen3.5-0.8B-Base hybrid layers verified against reference (max diff 0) |
| 04 - Retrieval/01 - Text Embedding | [ ] |  |  |
| 04 - Retrieval/02 - HNSW | [x] | 5.4 min | outputs saved; HNSW recall@10 0.99+ at ef=64; PQ 32x, IVF-PQ 24x compression; fixed encode batch_size |
| 04 - Retrieval/03 - Topic Modeling | [x] | 7 min | outputs saved; 66 topics on 18k newsgroup docs, LLM labels via gpt-5-mini |
| 04 - Retrieval/04 - NER | [ ] |  |  |
| 04 - Retrieval/05 - RAG | [x] | 1 min | outputs saved; RAG pipeline, RRF, reranker, RAGAS metrics |
| 04 - Retrieval/06 - Graph RAG | [x] | 1 min | gpt-5-mini; outputs saved |
| 05 - Post-Training Alignment/01 - SFT | [ ] |  |  |
| 05 - Post-Training Alignment/02 - Reward Model | [ ] |  |  |
| 05 - Post-Training Alignment/03 - DPO vs ORPO and SimPO | [ ] |  |  |
| 05 - Post-Training Alignment/04 - GRPO with RLVR | [ ] |  |  |
| 05 - Post-Training Alignment/05 - Parameter-Efficient Fine-Tuning (PEFT) | [ ] |  |  |
| 05 - Post-Training Alignment/06 - Representation Engineering | [ ] |  |  |
| 05 - Post-Training Alignment/07 - Agentic RL [TODO] | [-] |  | TODO placeholder, skipped |
| 06 - Model Compression/01 - Distillation | [ ] |  |  |
| 06 - Model Compression/02 - Model Pruning | [ ] |  |  |
| 06 - Model Compression/03 - Quantization | [ ] |  |  |
| 07 - Agentic LLM/A01 - LLM Prompting | [x] | 7 min | outputs saved; AIME 2025 effort sweep 0%→50%→70%→83%; threads raised to 30 so AIME cell fits in 5 min; structured-output prompt now lists real authors |
| 07 - Agentic LLM/A02 - Agent Harness | [x] | 1 min | outputs saved; glob demo now lists .ipynb files |
| 07 - Agentic LLM/A03 - Agent Operation | [x] | 20 s | outputs saved; tracing, budget, prompt-cache stats, model routing, mock vs real agent tests |
| 07 - Agentic LLM/A04 - Self Evolution Agent | [x] | 16 min | outputs saved; GEPA prompt 0.75→1.0; ablation cell 8.7 min (kept); skill evolution |
| 07 - Agentic LLM/A05 - AI Agent Memory | [x] | 3 min | outputs saved; KV/core/recall/archival/graph memory, consolidation, prompt self-update |
| 07 - Agentic LLM/B01 - LangGraph Agent | [x] | 45 s | outputs saved; fixed undefined REFLECTION_SYSTEM_PROMPT; Serper search live (run.py now injects SERPER key) |
| 07 - Agentic LLM/B02 - Code Agent | [x] | 1 min | outputs saved; KG audit finds SQL injection + mutual recursion in /tmp repo |
| 07 - Agentic LLM/B03 - Agent Frameworks and Interop Protocols | [x] | 4.6 min | outputs saved; from-scratch vs framework agents on Chinook SQL tasks over MCP |
| 07 - Agentic LLM/B04 - Deep Research Agent | [x] | 2.4 min | outputs saved; FRAMES: closed-book 62% → search 75% → research loop 75% |
| 08 - Production & Inference/01 - Generation | [ ] |  |  |
| 08 - Production & Inference/02 - Model Serving | [ ] |  |  |
| 08 - Production & Inference/03 - Test-Time Compute | [ ] |  |  |
| 09 - LLM Evaluation/01 - LLM Evaluation | [ ] |  |  |
| 09 - LLM Evaluation/02 - Agent Evaluation | [~] |  | run stopped after ~35 min (40 tasks x 4 trials x 2 models + tau-bench); key line fix applied, needs full rerun; markdown now number-free, verify its claims (pass^k < pass@1, judge disagreement, perturbation) against fresh output; consider trimming trials |
| 09 - LLM Evaluation/03 - AI Governance and Security [TODO] | [-] |  | TODO placeholder, skipped |

---

## Handoff (2026-10-27)

**State:** 24 of 44 notebooks run clean with outputs saved, 1 need CUDA (Colab), 2 are TODO placeholders (skipped), 2 need a fix + rerun, 15 not run yet. All runs are stopped; nothing is mid-flight.

**Needs fix + rerun:** 03 - Transformer Models/C02 - LLaMA, 09 - LLM Evaluation/02 - Agent Evaluation.
**CUDA / Colab:** 02 - Training Strategy/02 - Distributed Training.
**Not run yet (suggested order):** 04 - Retrieval/01 - Text Embedding, 04 - Retrieval/04 - NER, 05 - Post-Training Alignment/01 - SFT, 05 - Post-Training Alignment/02 - Reward Model, 05 - Post-Training Alignment/03 - DPO vs ORPO and SimPO, 05 - Post-Training Alignment/04 - GRPO with RLVR, 05 - Post-Training Alignment/05 - Parameter-Efficient Fine-Tuning (PEFT), 05 - Post-Training Alignment/06 - Representation Engineering, 06 - Model Compression/01 - Distillation, 06 - Model Compression/02 - Model Pruning, 06 - Model Compression/03 - Quantization, 08 - Production & Inference/01 - Generation, 08 - Production & Inference/02 - Model Serving, 08 - Production & Inference/03 - Test-Time Compute, 09 - LLM Evaluation/01 - LLM Evaluation.

**Lanes (owner's rule):** API-bound or low-memory notebooks, and notebooks that train their own small from-scratch model, may run up to 3 at a time; anything loading or fine-tuning a Hugging Face checkpoint runs one at a time (single 16 GB Apple GPU; parallel GPU runs caused timeouts on 2026-10-27). 10 min max per cell, 30 min max per notebook.

**Runner (local, gitignored, in `data/run03/`):** `run.py "<nb path>"` executes a notebook in its folder, injects `OPENAI_API_KEY` / `SERPER_API_KEY` from `.env` in memory only, strips bad outputs, writes `out/` + `logs/`. `promote.py out/<tag>.ipynb` copies outputs into the repo notebook if the code cells match (markdown is taken from the repo copy). `ledger.py`, `cleanup.py`, `check.py` (spec check), `mdscan*.py`, `quotescan*.py`, `abbr.py` are helpers. `.git/hooks/pre-commit` runs `cleanup.py` on staged notebooks.

**Known gotchas:** the earlier naming sweep renamed real library keywords and function parameters (`batch_num=` for `batch_size=`, a `DEVICE` parameter on helper functions) so unrun notebooks may hide the same bug; run each and read the errors. Run in-repo residue (`.logs`, `.sessions`, `skills/`, plots, `hello.py`) is created in the notebook folder and must be deleted after a run. Downloaded data (`03 - Transformer Models/datasets/`, `data/tinyshakespeare/`) is intentionally not committed.

**Still open from the owner's checklist:** return type hints on about 400 functions and docstrings on about 200; about 200 code cells over 60 lines need a markdown cell before them; about 370 string/docstring lines over 88 columns; `C02 - LLaMA` still uses `n_layers` / `n_heads` config keys; Agent Evaluation markdown claims need checking against a fresh run.
