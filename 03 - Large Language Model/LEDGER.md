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
| 03 - Transformer Models/C02 - LLaMA | [x] | 11 s | outputs saved; fixed KVCache DEVICE kwarg and config keys (num_layers/num_heads/num_kv_heads); KV-cache vs full forward max diff 4e-6 |
| 03 - Transformer Models/C03 - DeepSeek | [x] | 13 s | outputs saved; fixed RoPE helper device parameter |
| 03 - Transformer Models/C04 - Qwen | [x] | 1 min | outputs saved; Qwen3.5-0.8B-Base hybrid layers verified against reference (max diff 0) |
| 04 - Retrieval/01 - Text Embedding | [x] | 15 s | outputs saved; BiEncoder MNRL training margin 0.03→0.14 over 5 epochs; Matryoshka loss per dimension |
| 04 - Retrieval/02 - HNSW | [x] | 5.4 min | outputs saved; HNSW recall@10 0.99+ at ef=64; PQ 32x, IVF-PQ 24x compression; fixed encode batch_size |
| 04 - Retrieval/03 - Topic Modeling | [x] | 7 min | outputs saved; 66 topics on 18k newsgroup docs, LLM labels via gpt-5-mini |
| 04 - Retrieval/04 - NER | [x] | 6.5 min | outputs saved; BERT test F1 0.856 (4k train sentences, 1 epoch), GLiNER zero-shot F1 0.70 on 500 test sentences |
| 04 - Retrieval/05 - RAG | [x] | 1 min | outputs saved; RAG pipeline, RRF, reranker, RAGAS metrics |
| 04 - Retrieval/06 - Graph RAG | [x] | 1 min | gpt-5-mini; outputs saved |
| 05 - Post-Training Alignment/01 - SFT | [x] | 6 min | outputs saved; fixed pack_examples kwarg, log_level warning; TRL LoRA SFT 10 steps (loss 1.5) + from-scratch collator/trainer |
| 05 - Post-Training Alignment/02 - Reward Model | [x] | 7 min | outputs saved; ORM ranking acc ~78% on 100 held-out pairs (chance 50%); PRM step labels via MC rollouts + LLM judge |
| 05 - Post-Training Alignment/03 - DPO vs ORPO and SimPO | [x] | 6.5 min | outputs saved; fixed DEVICE kwarg on helper calls; DPO margin 0→16, ORPO/SimPO one-epoch runs |
| 05 - Post-Training Alignment/04 - GRPO with RLVR | [x] | 7.5 min | outputs saved; fixed config.batch_num; math reward noisy at 16 steps (markdown says so), tool-calling reward rises 0.3→0.9 |
| 05 - Post-Training Alignment/05 - Parameter-Efficient Fine-Tuning (PEFT) | [x] | 6.5 min | outputs saved; LoRA 0.11% trainable (541k of 494M) on Dolly 60 steps; repetition_penalty added so greedy output does not loop |
| 05 - Post-Training Alignment/06 - Representation Engineering | [x] | 18 min | outputs saved; refusal 97%→6% by ablation, 3% after weight orthogonalisation; TopK SAE recovers 89% of layer loss; slowest cell 6 min |
| 05 - Post-Training Alignment/07 - Agentic RL [TODO] | [-] |  | TODO placeholder, skipped |
| 06 - Model Compression/01 - Distillation | [x] | 18 min | outputs saved; teacher 90%, student 10% → SFT 30% / logit KD 15% / rejection-sampling 25% / on-policy 18% / ReDI 12%; teacher-trace cell takes 9 min (near limit) |
| 06 - Model Compression/02 - Model Pruning | [x] | 5 min | outputs saved; SmolLM2-135M dense ppl 24.3; 50% magnitude 2008 vs Wanda 55; activation-aware structured beats L1 structured; iterative 60% ppl 154 vs one-shot 20378 |
| 06 - Model Compression/03 - Quantization | [x] | 3.5 min | outputs saved; GPT-2 ppl FP32 56.5, 4-bit RTN 66.2 / AWQ 64.1 / GPTQ 60.2, 3-bit RTN 224 vs GPTQ 86; SmoothQuant W8A8 68.8→63.8 |
| 07 - Agentic LLM/A01 - LLM Prompting | [x] | 7 min | outputs saved; AIME 2025 effort sweep 0%→50%→70%→83%; threads raised to 30 so AIME cell fits in 5 min; structured-output prompt now lists real authors |
| 07 - Agentic LLM/A02 - Agent Harness | [x] | 1 min | outputs saved; glob demo now lists .ipynb files |
| 07 - Agentic LLM/A03 - Agent Operation | [x] | 20 s | outputs saved; tracing, budget, prompt-cache stats, model routing, mock vs real agent tests |
| 07 - Agentic LLM/A04 - Self Evolution Agent | [x] | 16 min | outputs saved; GEPA prompt 0.75→1.0; ablation cell 8.7 min (kept); skill evolution |
| 07 - Agentic LLM/A05 - AI Agent Memory | [x] | 3 min | outputs saved; KV/core/recall/archival/graph memory, consolidation, prompt self-update |
| 07 - Agentic LLM/B01 - LangGraph Agent | [x] | 45 s | outputs saved; fixed undefined REFLECTION_SYSTEM_PROMPT; Serper search live (run.py now injects SERPER key) |
| 07 - Agentic LLM/B02 - Code Agent | [x] | 1 min | outputs saved; KG audit finds SQL injection + mutual recursion in /tmp repo |
| 07 - Agentic LLM/B03 - Agent Frameworks and Interop Protocols | [x] | 4.6 min | outputs saved; from-scratch vs framework agents on Chinook SQL tasks over MCP |
| 07 - Agentic LLM/B04 - Deep Research Agent | [x] | 2.4 min | outputs saved; FRAMES: closed-book 62% → search 75% → research loop 75% |
| 08 - Production & Inference/01 - Generation | [x] | 50 s | outputs saved; fixed batch_num NameError in generate_batch; continuous batching 2.7x over static |
| 08 - Production & Inference/02 - Model Serving | [x] | 3 min | outputs saved; paged KV (1.3% waste vs 86%), radix prefix cache saves 53% prefill, KV quant fp8/int8/KIVI vs naive int4, EAGLE/MTP speculation; vLLM launch cell prints SGLang command (CUDA-only) |
| 08 - Production & Inference/03 - Test-Time Compute | [x] | 22 min | outputs saved; 14 GSM8K problems; thinking on/off 93% (169 vs 709 tokens), budget 128→512 86%→93%; sampling/revision saturate at 100% on this slice (markdown says so); first run hung/slow at 16 problems so trimmed |
| 09 - LLM Evaluation/01 - LLM Evaluation | [x] | 1.5 min | outputs saved; judge now gpt-5-mini (local 0.8B could not follow the format), temperature-scaling gradient sign fixed, BERTScore baseline-rescaled at layer 9 |
| 09 - LLM Evaluation/02 - Agent Evaluation | [x] | 15 min | outputs saved; trials cut 4→3; HumanEval+ pass@1 mini 0.94 / nano 0.71, pass^3 0.90 / 0.45; tau-bench retail 0.70 / 0.50; judge kappa 0.24; markdown claims checked against output |
| 09 - LLM Evaluation/03 - AI Governance and Security [TODO] | [-] |  | TODO placeholder, skipped |

---

## Handoff (2026-10-27, end of rerun sweep)

**State:** every runnable chapter-03 notebook has been rerun with fresh outputs, markdown cleaned and pushed. Only `02 - Training Strategy/02 - Distributed Training` is left: it needs CUDA (warp occupancy, torch.profiler, memory profiling, Triton) and must be run in Colab. The two `[TODO]` placeholders are skipped.

**Run-time notes:** slowest notebooks are Test-Time Compute (22 min), Representation Engineering (18 min), Distillation (18 min) and Agent Evaluation (15 min); each cell is under 10 min. Distillation's teacher-trace cell (9 min) and Test-Time Compute's thinking cell (7.7 min) are the closest to the cell limit.

**Known spec gaps (not rewritten):** several older notebooks (Text Embedding, LLM Evaluation, Generation, Quantization) still use toy or hand-written data in places and `print("=" * 60)` banners; return type hints and docstrings are incomplete on some helpers; code cells over 60 lines exist; some string lines exceed 88 columns.

**Gotchas:** helper-function parameters renamed in the earlier naming sweep (`DEVICE`, `batch_num`, `seq_len`) caused kwarg mismatches in C02, SFT, DPO, GRPO and Generation; fixed. SFT and PEFT write `data/` next to the notebook (now gitignored). Runner and helpers live in `data/run03/` (gitignored).
