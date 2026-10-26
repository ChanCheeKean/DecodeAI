# Chapter 03 run ledger

Status: `[ ]` not run · `[~]` running/in fix loop · `[x]` run clean, outputs saved · `[C]` needs CUDA (run in Colab) · `[-]` skipped (TODO placeholder)

Runner: `data/run03/run.py` (executes in the notebook's folder, 10 min/cell timeout, key injected in memory only).
Outputs staged in `data/run03/out/`, logs in `data/run03/logs/`; promoted into the repo only after review.

| Notebook | Status | Run time | Notes |
|---|---|---|---|
| 01 - RNN/01 - Vanilla RNN | [x] | 2 min | outputs saved; dinosaur-name model memorises most of the 262 names, sampling at T>1 gives new ones |
| 03 - Transformer Models/A01 - Attention Mechanism | [x] | 4 s | outputs saved |
| 04 - Retrieval/06 - Graph RAG | [x] | 1 min | gpt-5-mini; outputs saved |
| 01 - RNN/02 - RNN with Attention | [x] | 5 min | both attention variants reach 100% test accuracy on date reformatting; outputs saved |
| 03 - Transformer Models/A02 - Transformer | [x] | 2.4 min | outputs saved; 1500 steps, loss 7.5→4.5; greedy reply collapses to 'i dont know' (documented in notebook) |
| 03 - Transformer Models/B01 - BERT | [x] | 5 min | outputs saved; MLM loss 10.3→7.05 in 3 epochs, NSP stays ~50% at this scale |
| 04 - Retrieval/03 - Topic Modeling | [x] | 7 min | outputs saved; 66 topics on 18k newsgroup docs, LLM labels via gpt-5-mini |
| 07 - Agentic LLM/A01 - LLM Prompting | [x] | 7 min | outputs saved; AIME 2025 effort sweep 0%→50%→70%→83%; threads raised to 30 so AIME cell fits in 5 min; structured-output prompt now lists real authors |
