# DecodeAI

**Decode AI from first principles. No black boxes. No hand-waving.**

This repository is built on a simple belief: you cannot truly master AI by calling `model.fit()`. To understand how modern AI systems actually work, you need to **build them from scratch** — derive the math, implement the algorithms, and watch the gradients flow.

Every notebook in this repository dissects a core AI concept by implementing it from the ground up using raw PyTorch and NumPy. We go from the bias-variance tradeoff all the way to building GPT, LLaMA, DeepSeek, and GRPO — the same algorithm behind DeepSeek-R1 — and on to agent harnesses, memory systems, and vision-language models. If a concept matters, we don't just explain it. We build it, break it, and rebuild it until the intuition is earned.

> *"What I cannot create, I do not understand."* — Richard Feynman

---

## Table of Contents

### 01 - Machine Learning

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Data Processing](01%20-%20Machine%20Learning/01%20-%20Data%20Processing.ipynb) | Bias-variance tradeoff, feature scaling, data splitting, and preprocessing pipelines |
| 02 | [Regression](01%20-%20Machine%20Learning/02%20-%20Regression.ipynb) | Linear and polynomial regression — cost functions, gradient descent, and regularization |
| 03 | [Classification](01%20-%20Machine%20Learning/03%20-%20Classification.ipynb) | Logistic regression, SVMs, decision trees, random forests, and ensemble methods |
| 04 | [Clustering](01%20-%20Machine%20Learning/04%20-%20Clustering.ipynb) | K-Means, DBSCAN, hierarchical clustering — algorithms, objective functions, and evaluation |
| 05 | [Dimension Reduction](01%20-%20Machine%20Learning/05%20-%20Dimension%20Reduction.ipynb) | PCA derivation, eigenvalue decomposition, and t-SNE for high-dimensional data |

### 02 - Deep Learning Foundation

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Neural Network Foundations](02%20-%20Deep%20Learning%20Foundation/01%20-%20Neural%20Network%20Foundations.ipynb) | NumPy vectorization, broadcasting, forward/backward pass from scratch |
| 02 | [Activation Functions](02%20-%20Deep%20Learning%20Foundation/02%20-%20Activation%20Functions.ipynb) | Sigmoid, tanh, ReLU, GELU — why activations matter, saturation, and dying neurons |
| 03 | [Weight Initialization](02%20-%20Deep%20Learning%20Foundation/03%20-%20Weight%20Initialization.ipynb) | Why zero init fails, variance explosion/vanishing, Xavier and He initialization proofs |
| 04 | [Normalization](02%20-%20Deep%20Learning%20Foundation/04%20-%20Normalization.ipynb) | Batch norm, layer norm, group norm — internal covariate shift and loss landscape smoothing |
| 05 | [Regularization](02%20-%20Deep%20Learning%20Foundation/05%20-%20Regularization.ipynb) | L2 weight decay, dropout, early stopping — fighting overfitting with math |
| 06 | [Residual Connection](02%20-%20Deep%20Learning%20Foundation/06%20-%20Residual%20Connection.ipynb) | The degradation problem, skip connections, and why deeper networks can fail without them |
| 07 | [Loss Function](02%20-%20Deep%20Learning%20Foundation/07%20-%20Loss%20Function.ipynb) | BCE, cross-entropy derivations — why sigmoid+BCE and softmax+CE produce clean gradients |
| 08 | [Optimizer](02%20-%20Deep%20Learning%20Foundation/08%20-%20Optimizer.ipynb) | SGD, momentum, RMSProp, Adam — from vanilla gradient descent to adaptive learning rates |
| 09 | [Model Classification](02%20-%20Deep%20Learning%20Foundation/09%20-%20Model%20Classification.ipynb) | End-to-end image classification on CIFAR-10 applying all the foundations above |

### 03 - Large Language Model

#### RNN

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Vanilla RNN](03%20-%20Large%20Language%20Model/01%20-%20RNN/01%20-%20Vanilla%20RNN.ipynb) | RNN, GRU and LSTM cells from scratch — hidden states, BPTT, vanishing/exploding gradients, character-level LM |
| 02 | [RNN with Attention](03%20-%20Large%20Language%20Model/01%20-%20RNN/02%20-%20RNN%20with%20Attention.ipynb) | Seq2seq bottleneck problem, Bahdanau vs Luong attention for date format translation |

#### Training Strategy

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Data Processing](03%20-%20Large%20Language%20Model/02%20-%20Training%20Strategy/01%20-%20Data%20Processing.ipynb) | Pretraining data pipelines — heuristic filters, deduplication, CCNet perplexity and classifier quality filtering, data mixing and annealing |
| 02 | [Distributed Training](03%20-%20Large%20Language%20Model/02%20-%20Training%20Strategy/02%20-%20Distributed%20Training.ipynb) | GPU programming to multi-GPU training — SIMT, memory hierarchy, roofline model, Triton kernels, profiling, DDP, tensor and pipeline parallelism |
| 03 | [Muon and WSD](03%20-%20Large%20Language%20Model/02%20-%20Training%20Strategy/03%20-%20Muon%20and%20WSD.ipynb) | Muon optimizer from scratch (Newton–Schulz orthogonalisation, RMS-matched scaling), warmup–stable–decay schedules, QK-Clip |

#### Transformer Models

| # | Notebook | Description |
|---|----------|-------------|
| A01 | [Attention Mechanism](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/A01%20-%20Attention%20Mechanism.ipynb) | Self-attention and scaled dot-product, multi-head attention, Flash and sliding-window/sparse attention |
| A02 | [Transformer](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/A02%20-%20Transformer.ipynb) | Full transformer architecture from scratch — masking, positional encoding, multi-head attention, encoder-decoder |
| B01 | [BERT](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/B01%20-%20BERT.ipynb) | Bidirectional encoder — WordPiece tokenization, MLM, NSP, and the fine-tuning paradigm |
| B02 | [ColBERT](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/B02%20-%20ColBERT.ipynb) | Late interaction retrieval — MaxSim scoring, query augmentation, token-level matching |
| C01 | [GPT](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/C01%20-%20GPT.ipynb) | GPT-2 from scratch — byte-level BPE tokenization, causal self-attention, autoregressive decoding, looped transformers |
| C02 | [LLaMA](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/C02%20-%20LLaMA.ipynb) | LLaMA architecture deep dive — RMSNorm, RoPE, SwiGLU, grouped-query attention |
| C03 | [DeepSeek](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/C03%20-%20DeepSeek.ipynb) | Multi-head Latent Attention (MLA), fine-grained MoE with shared experts, multi-token prediction, mHC, compressed sparse attention |
| C04 | [Qwen](03%20-%20Large%20Language%20Model/03%20-%20Transformer%20Models/C04%20-%20Qwen.ipynb) | Qwen3.5 hybrid architecture — Gated DeltaNet linear attention, gated attention, partial RoPE, KV-cache and latency cost, YaRN |

#### Text Retrieval & NLP

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Text Embedding](03%20-%20Large%20Language%20Model/04%20-%20Retrieval/01%20-%20Text%20Embedding.ipynb) | Similarity metrics, bi- vs cross-encoders, contrastive losses, hard negatives, Matryoshka, instruction-aware LLM embeddings (Qwen3-Embedding) |
| 02 | [HNSW](03%20-%20Large%20Language%20Model/04%20-%20Retrieval/02%20-%20HNSW.ipynb) | Approximate nearest neighbors — HNSW, Product Quantization, IVF for vector search |
| 03 | [Topic Modeling](03%20-%20Large%20Language%20Model/04%20-%20Retrieval/03%20-%20Topic%20Modeling.ipynb) | BERTopic from scratch (embeddings, UMAP, HDBSCAN, c-TF-IDF), LLM topic labeling and LLM-native topic discovery |
| 04 | [NER](03%20-%20Large%20Language%20Model/04%20-%20Retrieval/04%20-%20NER.ipynb) | Named Entity Recognition — BIO tagging, CoNLL-2003, BERT token classification, GLiNER zero-shot spans |
| 05 | [RAG](03%20-%20Large%20Language%20Model/04%20-%20Retrieval/05%20-%20RAG.ipynb) | Retrieval-Augmented Generation — chunking, hybrid search, HyDE, RRF, Self-RAG/CRAG/agentic RAG, cross-encoder and LLM rerankers (Qwen3-Reranker), evaluation |
| 06 | [Graph RAG](03%20-%20Large%20Language%20Model/04%20-%20Retrieval/06%20-%20Graph%20RAG.ipynb) | Knowledge-graph retrieval — LLM entity/relation extraction, entity linking, multi-hop graph traversal |

#### Post-Training Alignment

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [SFT](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/01%20-%20SFT.ipynb) | Supervised Fine-Tuning — chat templates, conversational vs completion formats, assistant-only loss masking, packing |
| 02 | [Reward Model](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/02%20-%20Reward%20Model.ipynb) | ORM vs PRM — Bradley-Terry loss, step-level credit assignment for reasoning |
| 03 | [DPO vs ORPO and SimPO](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/03%20-%20DPO%20vs%20ORPO%20and%20SimPO.ipynb) | Direct Preference Optimization — aligning LLMs with human preferences without RL |
| 04 | [GRPO with RLVR](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/04%20-%20GRPO%20with%20RLVR.ipynb) | Group Relative Policy Optimization — the algorithm behind DeepSeek-R1, with verifiable rewards |
| 05 | [PEFT (LoRA / QLoRA)](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/05%20-%20Parameter-Efficient%20Fine-Tuning%20(PEFT).ipynb) | LoRA and QLoRA from scratch — low-rank adaptation, 4-bit quantization, 99.6% fewer parameters |
| 06 | [Representation Engineering](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/06%20-%20Representation%20Engineering.ipynb) | Linear probes, steering vectors, directional ablation and abliteration, TopK sparse autoencoders |
| 07 | [Agentic RL](03%20-%20Large%20Language%20Model/05%20-%20Post-Training%20Alignment/07%20-%20Agentic%20RL%20%5BTODO%5D.ipynb) | *Placeholder* — multi-turn rollouts with tools, observation masking, sparse rewards and reward hacking, turn-level credit assignment, Search-R1-style training, async tool environments |

#### Model Compression

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Distillation](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/01%20-%20Distillation.ipynb) | Knowledge distillation — response-level SFT, logit-level KD, rejection sampling |
| 02 | [Model Pruning](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/02%20-%20Model%20Pruning.ipynb) | LLM pruning — magnitude vs Wanda vs SparseGPT, 2:4 sparsity, block-influence depth pruning, MLP width pruning, distillation recovery |
| 03 | [Quantization](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/03%20-%20Quantization.ipynb) | FP32 to INT4 — numeric formats, quantization schemes, memory-accuracy tradeoffs |

#### Agentic LLM

| # | Notebook | Description |
|---|----------|-------------|
| A01 | [LLM Prompting](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A01%20-%20LLM%20Prompting.ipynb) | Prompt design patterns, few-shot, CoT on instruction vs reasoning models, reasoning effort, structured output, prompt injection defenses |
| A02 | [Agent Harness](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A02%20-%20Agent%20Harness.ipynb) | The agent loop from scratch — tool system, planning, subagents, skills, context compaction, task system, agent teams |
| A03 | [Agent Operation](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A03%20-%20Agent%20Operation.ipynb) | Running agents in production — observability, token budgeting, prompt caching, model routing, agent testing |
| A04 | [Self Evolution Agent](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A04%20-%20Self%20Evolution%20Agent.ipynb) | Agents that improve themselves — Reflexion, GEPA evolutionary prompt optimization, skill evolution with constraint gates, ADAS |
| A05 | [AI Agent Memory](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/A05%20-%20AI%20Agent%20Memory.ipynb) | Memory architectures — Mem0 KV store, MemGPT/Letta tiers, Zep temporal knowledge graphs, hybrid retrieval, consolidation, procedural memory |
| B01 | [LangGraph Agent](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/B01%20-%20LangGraph%20Agent.ipynb) | Cyclic state graphs with LangGraph — ReAct, plan-and-execute, memory, multi-agent supervisors, MCP, LangSmith tracing |
| B02 | [Code Agent](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/B02%20-%20Code%20Agent.ipynb) | Multi-agent repository auditing — code knowledge graphs, structural detectors, inter-procedural data flow, LLM validators |
| B03 | [Agent Frameworks and Interop Protocols](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/B03%20-%20Agent%20Frameworks%20and%20Interop%20Protocols.ipynb) | One text-to-SQL task on a from-scratch loop, the OpenAI Agents SDK and Google ADK over a shared MCP server — token cost model, agents-as-tools vs workflow pipelines, tool-call guardrails, A2A delegation across frameworks |
| B04 | [Deep Research Agent](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/B04%20-%20Deep%20Research%20Agent.ipynb) | One research loop from scratch — decide next query, search, read, evidence notes with verified quotes, cited answer, citation precision; closed-book vs single search vs research loop on FRAMES |

#### Production & Inference

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Generation](03%20-%20Large%20Language%20Model/08%20-%20Production%20%26%20Inference/01%20-%20Generation.ipynb) | Text generation from scratch — KV-cache, greedy/beam/sampling, batched and continuous batching, speculative and constrained decoding |
| 02 | [Model Serving](03%20-%20Large%20Language%20Model/08%20-%20Production%20%26%20Inference/02%20-%20Model%20Serving.ipynb) | Serving engine internals — paged KV cache, continuous batching, radix prefix caching, KV offload, prefill/decode disaggregation, KV quantization, EAGLE-3 and MTP speculative decoding |
| 03 | [Test-Time Compute](03%20-%20Large%20Language%20Model/08%20-%20Production%20%26%20Inference/03%20-%20Test-Time%20Compute.ipynb) | Reasoning control — thinking on/off, s1 budget forcing, majority vote and best-of-N with a reward model, self-revision, overthinking and early exit |

#### LLM Evaluation

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [LLM Evaluation](03%20-%20Large%20Language%20Model/09%20-%20LLM%20Evaluation/01%20-%20LLM%20Evaluation.ipynb) | Perplexity and bits per byte, MMLU scoring protocols, calibration, an LLM judge validated against human labels, Bradley–Terry ratings from Chatbot Arena |
| 02 | [Agent Evaluation](03%20-%20Large%20Language%20Model/09%20-%20LLM%20Evaluation/02%20-%20Agent%20Evaluation.ipynb) | pass@k vs pass^k, sandboxed code-agent harness with hidden tests, τ-bench retail harness with a user simulator, trajectory grading, contamination probes |
| 03 | [AI Governance and Security](03%20-%20Large%20Language%20Model/09%20-%20LLM%20Evaluation/03%20-%20AI%20Governance%20and%20Security%20%5BTODO%5D.ipynb) | *Placeholder* — automated red teaming (PAIR, GCG), indirect prompt injection on agents, guard models, toxicity and bias benchmarks, hallucination detection, model cards and EU AI Act / NIST AI RMF |

### 04 - Computer Vision

#### Image Processing

| # | Notebook | Description |
|---|----------|-------------|
| 1 | [Image Processing](04%20-%20Computer%20Vision/00%20-%20Image%20Processing/1%20-%20Image_Processing.ipynb) | OpenCV basics — I/O, drawing, blending, thresholding, blurring, morphology, color filtering |
| 2 | [Image Detection](04%20-%20Computer%20Vision/00%20-%20Image%20Processing/2%20-%20Image%20Detection.ipynb) | Template matching, corners, Canny edges, contours, ORB feature matching, face and QR detection |
| 3 | [Image Analysis](04%20-%20Computer%20Vision/00%20-%20Image%20Processing/3%20-%20Image%20Analysis.ipynb) | Histograms and equalization, dominant colors via K-Means, structural similarity |
| 4 | [Motion Tracking](04%20-%20Computer%20Vision/00%20-%20Image%20Processing/4%20-%20Motion%20Tracking.ipynb) | Lucas-Kanade and dense optical flow, Mean Shift and CamShift tracking |

#### Deep Learning for Vision

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [CNN Foundations](04%20-%20Computer%20Vision/01%20-%20CNN%20Foundations.ipynb) | Convolutions from scratch in NumPy — zero-padding, forward/backward pass, pooling, and gradient derivations |
| 02 | [Object Detection](04%20-%20Computer%20Vision/02%20-%20Object%20Detection.ipynb) | IoU, NMS, anchor box assignment, and YOLO output decoding from scratch; YOLO26's NMS-free one-to-one head vs NMS on the same image |
| 03 | [Image Segmentation](04%20-%20Computer%20Vision/03%20-%20Image%20Segmentation.ipynb) | U-Net encoder/decoder from scratch — skip connections, pixel-wise loss, SegFormer inference |
| 04 | [Open-Vocabulary Detection and Segmentation](04%20-%20Computer%20Vision/04%20-%20Open-Vocabulary%20Detection%20and%20Segmentation.ipynb) | *Placeholder* — SAM 3 promptable concept segmentation, Grounding DINO, YOLO-World/YOLOE, RF-DETR, DEIM, YOLO26 |
| 05 | [Metric Learning](04%20-%20Computer%20Vision/05%20-%20Metric%20Learning.ipynb) | Siamese networks, contrastive loss, triplet loss, and FaceNet — embedding spaces for unseen classes |
| 06 | [Vision Transformers](04%20-%20Computer%20Vision/06%20-%20Vision%20Transformers.ipynb) | Patch embedding, ViT on MNIST, resolution interpolation; transfer learning from pretrained ViT-B/16 (linear probe, head-only, layer-wise LR decay fine-tuning); DeiT and Swin |
| 07 | [Contrastive Learning](04%20-%20Computer%20Vision/07%20-%20Contrastive%20Learning.ipynb) | SimCLR, DINOv2, and CLIP vs SigLIP — self-supervised and image-text contrastive pretraining |
| 08 | [Vision Foundation Encoders](04%20-%20Computer%20Vision/08%20-%20Vision%20Foundation%20Encoders.ipynb) | *Placeholder* — DINOv3 Gram anchoring, SigLIP 2, Perception Encoder, RADIO; dense vs global features |
| 09 | [Diffusion Model](04%20-%20Computer%20Vision/09%20-%20Diffusion%20Model.ipynb) | DDPM, DDIM, Stable Diffusion — forward/reverse process, noise schedules, ContextUNet |
| 10 | [Flow Matching and Diffusion Transformers](04%20-%20Computer%20Vision/10%20-%20Flow%20Matching%20and%20Diffusion%20Transformers.ipynb) | *Placeholder* — rectified flow, DiT / MM-DiT, SD3, FLUX.2, few-step distillation |
| 11 | [3D Vision](04%20-%20Computer%20Vision/11%20-%203D%20Vision.ipynb) | *Placeholder* — feed-forward reconstruction with VGGT and DUSt3R, Gaussian splatting |
| 12 | [Model Explainability](04%20-%20Computer%20Vision/12%20-%20Model%20Explainability.ipynb) | Saliency maps, GradCAM, Integrated Gradients, and SHAP on ResNet-50 |

### 05 - Multi-Modal

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Vision Language Model](05%20-%20Multi-Modal/01%20-%20Vision%20Language%20Model.ipynb) | Qwen3-VL taken apart and rebuilt — processor, 2×2 patch merger, token insertion, interleaved mRoPE, DeepStack ablation; LLaVA MLP vs patch merger vs Q-Former bridges trained on SigLIP 2 + Qwen3 |
| 02 | [Instruction Tuning](05%20-%20Multi-Modal/02%20-%20Instruction%20Tuning.ipynb) | Stage 2 on a pretrained VLM — SmolVLM + ChartQA LoRA SFT, multimodal loss masking, resolution vs. visual token budget, grounding diagnostics |
| 03 | [Reasoning & Inference](05%20-%20Multi-Modal/03%20-%20Reasoning%20%26%20Inference.ipynb) | Reasoning effort on chart questions (which inputs need to think), visual grounding with boxes as output on RefCOCO |
| 04 | [Visual Document Retrieval](05%20-%20Multi-Modal/04%20-%20Visual%20Document%20Retrieval.ipynb) | *Placeholder* — ColPali / ColQwen late interaction over page images, MaxSim, ViDoRe, multi-vector compression |
| 05 | [Audio & Speech](05%20-%20Multi-Modal/05%20-%20Audio%20%26%20Speech.ipynb) | Whisper log-mel features and WER from scratch, Mimi residual VQ and bitrate vs quality, full-duplex token streams, Qwen2.5-Omni thinker–talker speech-to-speech |
| 06 | [Video](05%20-%20Multi-Modal/06%20-%20Video.ipynb) | Qwen3-VL video path — fps sampling, temporal patches, text timestamps, token counts; MVBench with one vs many frames and reversed frame order |
| 07 | [Video Generation](05%20-%20Multi-Modal/07%20-%20Video%20Generation.ipynb) | *Placeholder* — causal 3D VAE, video DiT with flow matching, autoregressive and self-forcing video diffusion, Wan / Veo / Sora |
| 08 | [Native Multimodal](05%20-%20Multi-Modal/08%20-%20Native%20Multimodal.ipynb) | Janus-Pro understanding and generation in one model — VQ tokenizer from scratch, decoupled image paths, classifier-free guidance sampling loop |
| 09 | [Diffusion Language Models](05%20-%20Multi-Modal/09%20-%20Diffusion%20Language%20Models.ipynb) | *Placeholder* — masked discrete diffusion (LLaDA, Dream), Mercury, Gemini Diffusion, block diffusion, parallel decoding |
| 10 | [Computer Use and Browser Agents](05%20-%20Multi-Modal/10%20-%20Computer%20Use%20and%20Browser%20Agents.ipynb) | *Placeholder* — screenshot and DOM agents, grounding, action spaces, browser automation, evaluation, safety |
| 11 | [Vision-Language-Action Models](05%20-%20Multi-Modal/11%20-%20Vision-Language-Action%20Models.ipynb) | *Placeholder* — action chunking, FAST tokenization, flow-matching action experts (π0 family, GR00T), Gemini Robotics, SmolVLA |
| 12 | [World Models](05%20-%20Multi-Modal/12%20-%20World%20Models.ipynb) | *Placeholder* — Genie 3 interactive worlds, V-JEPA 2 planning in embedding space, Cosmos, latent dynamics |

---

More work is coming. This repository is actively maintained and expanding as the field evolves.
