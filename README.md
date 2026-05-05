# DecodeAI

**Decode AI from first principles. No black boxes. No hand-waving.**

This repository is built on a simple belief: you cannot truly master AI by calling `model.fit()`. To understand how modern AI systems actually work, you need to **build them from scratch** — derive the math, implement the algorithms, and watch the gradients flow.

Every notebook in this repository dissects a core AI concept by implementing it from the ground up using raw PyTorch and NumPy. We go from the bias-variance tradeoff all the way to building GPT, LLaMA, DeepSeek, and GRPO — the same algorithm behind DeepSeek-R1. If a concept matters, we don't just explain it. We build it, break it, and rebuild it until the intuition is earned.

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
| 01 | [Vanilla RNN](03%20-%20Large%20Language%20Model/01%20-%20RNN/01%20-%20Vanila%20RNN.ipynb) | RNN cell from scratch — hidden states, BPTT, vanishing/exploding gradients |
| 02 | [Recurrent Classifier](03%20-%20Large%20Language%20Model/01%20-%20RNN/02%20-%20Recurrent%20Classifier.ipynb) | Sentiment classification on IMDb using RNN/LSTM with padding and packing |
| 03 | [RNN with Attention](03%20-%20Large%20Language%20Model/01%20-%20RNN/03%20-%20RNN%20with%20Attention.ipynb) | Seq2seq bottleneck problem, Bahdanau attention for date format translation |

#### Transformer Models

| # | Notebook | Description |
|---|----------|-------------|
| A01 | [Pretrained Model - HuggingFace](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/A01%20-%20Pretrained%20Model%20-%20HuggingFace.ipynb) | Using HuggingFace pipelines and pretrained models for text classification |
| A02 | [Attention Mechanism](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/A02%20-%20Attention%20Mechanism.ipynb) | Bahdanau vs Luong attention — the information bottleneck and its solution |
| A03 | [Transformer](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/A03%20-%20Transformer.ipynb) | Full transformer architecture from scratch — multi-head attention, positional encoding, encoder-decoder |
| B01 | [BERT](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/B01%20-%20BERT.ipynb.ipynb) | Bidirectional encoder — WordPiece tokenization, MLM, NSP, and the fine-tuning paradigm |
| B02 | [ColBERT](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/B02%20-%20Colbert.ipynb) | Late interaction retrieval — MaxSim scoring, query augmentation, token-level matching |
| C01 | [nanoGPT](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/C01%20-%20nanoGPT.ipynb) | GPT-2 from scratch — byte-level BPE tokenization, causal self-attention, autoregressive decoding |
| C02 | [LLaMA](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/C02%20-%20LLama.ipynb) | LLaMA architecture deep dive — RMSNorm, RoPE, SwiGLU, grouped-query attention |
| C03 | [Mistral MoE](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/C03%20-%20Mistral%20MoE.ipynb) | Mixture of Experts — sparse routing, expert parallelism, sliding window attention |
| C04 | [DeepSeek](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/C04%20-%20DeepSeek.ipynb) | Multi-head Latent Attention (MLA) — 24x KV-cache reduction via low-rank compression |
| C05 | [Qwen](03%20-%20Large%20Language%20Model/03%20-%20Transformers%20Model/C05%20-%20Qwen.ipynb) | Advanced RoPE scaling — Position Interpolation, NTK-Aware, Dynamic NTK, YaRN |

#### Text Retrieval & NLP

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Text Embedding](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/01%20-%20Text%20Embedding.ipynb) | Cosine similarity, dot product, L2 distance — similarity metrics and embedding spaces |
| 02 | [HNSW](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/02%20-%20HNSW%20.ipynb) | Approximate nearest neighbors — HNSW, Product Quantization, IVF for vector search |
| 03 | [Topic Modeling](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/03%20-%20Topic%20Modeling.ipynb) | Discovering latent topics from text corpora |
| 04 | [NER](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/04%20-%20NER.ipynb) | Named Entity Recognition — BIO tagging, CoNLL-2003, token classification |
| 05 | [RAG](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/05%20-%20RAG.ipynb) | Retrieval-Augmented Generation — chunking strategies, vector stores, retrieval pipeline |
| 06 | [Advanced RAG](03%20-%20Large%20Language%20Model/04%20-%20Text%20Retrieval/06%20-%20Advanced%20RAG.ipynb) | Advanced retrieval techniques — re-ranking, hybrid search, query transformation |

#### Post-Training Alignment

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Instruction Tuning](03%20-%20Large%20Language%20Model/05%20-%20Post%20Training%20Alignmnet/01%20-%20Instruction%20Tuning.ipynb) | Fine-tuning Pythia-2.8B on Dolly 15k — prompt formatting, loss masking on response tokens |
| 02 | [SFT](03%20-%20Large%20Language%20Model/05%20-%20Post%20Training%20Alignmnet/02%20-%20SFT.ipynb) | Supervised Fine-Tuning — the first step after pretraining in the LLM pipeline |
| 03 | [Reward Model](03%20-%20Large%20Language%20Model/05%20-%20Post%20Training%20Alignmnet/03%20-%20Reward%20Model.ipynb) | ORM vs PRM — Bradley-Terry loss, step-level credit assignment for reasoning |
| 04 | [DPO vs ORPO and SimPO](03%20-%20Large%20Language%20Model/05%20-%20Post%20Training%20Alignmnet/04%20-%20DPO%20vs%20ORPO%20and%20SimPO.ipynb) | Direct Preference Optimization — aligning LLMs with human preferences without RL |
| 05 | [GRPO with RLVR](03%20-%20Large%20Language%20Model/05%20-%20Post%20Training%20Alignmnet/05%20-%20GRPO%20with%20RLVR.ipynb) | Group Relative Policy Optimization — the algorithm behind DeepSeek-R1, with verifiable rewards |
| 06 | [PEFT (LoRA / QLoRA)](03%20-%20Large%20Language%20Model/05%20-%20Post%20Training%20Alignmnet/06%20-%20Parameter%20Efficient%20Fine%20Tuning%20(PEFT).ipynb) | LoRA and QLoRA from scratch — low-rank adaptation, 4-bit quantization, 99.6% fewer parameters |
| 07 | [Abliteration](03%20-%20Large%20Language%20Model/05%20-%20Post%20Training%20Alignmnet/07%20-%20Abliteration.ipynb) | Mechanistic interpretability — finding and removing the refusal direction in activation space |

#### Model Compression

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Distillation](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/01%20-%20Distillation.ipynb) | Knowledge distillation — response-level SFT, logit-level KD, rejection sampling |
| 02 | [Model Pruning](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/02%20-%20Model%20Pruning.ipynb) | Unstructured and structured pruning — magnitude-based, layer-wise, and global strategies |
| 03 | [Quantization](03%20-%20Large%20Language%20Model/06%20-%20Model%20Compression/03%20-%20Quantization.ipynb) | FP32 to INT4 — numeric formats, quantization schemes, memory-accuracy tradeoffs |

#### Agentic LLM

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [LLM Prompting](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/01%20-%20LLM_Prompting.ipynb) | Prompt engineering techniques — few-shot, chain-of-thought, structured outputs |
| 02 | [LangChain](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/02%20-%20Langchain.ipynb) | LangChain fundamentals — data loaders, chains, and database integration |
| 03 | [LangGraph Agent](03%20-%20Large%20Language%20Model/07%20-%20Agentic%20LLM/03%20-%20Langraph_Agent.ipynb) | Building agents with LangGraph — cyclic state machines, tool calling, RAG agents |

#### Production & Inference

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Generation](03%20-%20Large%20Language%20Model/07%20-%20Production%20%26%20Inference/01%20-%20Generation.ipynb) | Text generation from scratch — KV-cache, sampling strategies, batched/continuous batching, speculative decoding |

#### LLM Evaluation

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [LLM Evaluation](03%20-%20Large%20Language%20Model/08%20-%20LLM%20Eval/01%20-%20LLM%20Evaluation.ipynb) | Perplexity, intrinsic evaluation metrics — measuring how well a model predicts text |

### 04 - Computer Vision

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [CNN Foundations](04%20-%20Computer%20Vision/01%20-%20CNN%20Foundations.ipynb) | Convolutions from scratch in NumPy — zero-padding, forward/backward pass, pooling, and gradient derivations |
| 02 | [CNN Architecture](04%20-%20Computer%20Vision/02%20-%20CNN%20Architecture.ipynb) | Baseline CNN to ResNet on FashionMNIST — vanishing gradients and why skip connections work |
| 03 | [Transfer Learning](04%20-%20Computer%20Vision/03%20-%20Transfer%20Learning.ipynb) | Feature extraction vs fine-tuning on CIFAR-10 — ImageNet normalization, layer freezing strategies |
| 04 | [Object Detection](04%20-%20Computer%20Vision/04%20-%20Object%20Detection.ipynb) | IoU, NMS, anchor box assignment, and YOLO output decoding — built from scratch |
| 05 | [Image Segmentation](04%20-%20Computer%20Vision/05%20-%20Image%20Segmentation.ipynb) | U-Net encoder/decoder from scratch — skip connections, pixel-wise loss, SegFormer inference |
| 06 | [Metric Learning](04%20-%20Computer%20Vision/06%20-%20Metric%20Learning.ipynb) | Siamese networks, contrastive loss, triplet loss, and FaceNet — embedding spaces for unseen classes |
| 07 | [Vision Transformers](04%20-%20Computer%20Vision/07%20-%20Vision%20Transformers.ipynb) | ViT, DeiT, and Swin from scratch — patch embedding, multi-head self-attention, hierarchical windows |
| 08 | [Contrastive Learning](04%20-%20Computer%20Vision/08%20-%20Constrastive%20Learning.ipynb) | SimCLR, CLIP, and DINOv2 — self-supervised pretraining with NT-Xent loss |
| 09 | [Diffusion Model](04%20-%20Computer%20Vision/09%20-%20Diffusion%20Model.ipynb) | DDPM, DDIM, Stable Diffusion — forward/reverse process, noise schedules, ContextUNet |
| 10 | [Model Explainability](04%20-%20Computer%20Vision/10%20-%20Model%20Explainability.ipynb) | Saliency maps, GradCAM, Integrated Gradients, and SHAP on ResNet-50 |

### 05 - Multi-Modal

| # | Notebook | Description |
|---|----------|-------------|
| 01 | [Bridge Architecture](05%20-%20Multi-Modal/01%20-%20Bridge%20Architecture.ipynb) | Connecting frozen ViT to frozen LLM — LLaVA projectors, Flamingo Perceiver, BLIP-2 Q-Former, MoE bridges |
| 02 | [Vision Language Model](05%20-%20Multi-Modal/02%20-%20Vision%20Language%20Model.ipynb) | Qwen-VL style VLM from scratch — TinyViT, MLP projector, mRoPE, visual token insertion, Stage 1 training |
| 03 | [Instruction Tuning](05%20-%20Multi-Modal/03%20-%20Instruction%20Tuning.ipynb) | Stage 2–3 VLM training — visual instructions, multi-turn dialog, RLHF-V for hallucination reduction |
| 04 | [Reasoning & Inference](05%20-%20Multi-Modal/04%20-%20Reasoning%20%26%20Inference.ipynb) | VLM inference pipeline — decoding strategies, streaming, chain-of-thought, visual grounding, evaluation |
| 05 | [Audio & Speech](05%20-%20Multi-Modal/05%20-%20Audio%20%26%20Speech.ipynb) | Waveforms to Mel spectrograms from scratch — audio encoders, Whisper, Phi-4 multimodal speech |
| 06 | [Video](05%20-%20Multi-Modal/06%20-%20Video.ipynb) | Video understanding — spatial-temporal attention, ViViT, dynamic FPS sampling, text-timestamp alignment |
| 07 | [Visual Agent & Computer Use](05%20-%20Multi-Modal/07%20-%20Visual%20Agent%20and%20Computer%20Use.ipynb) | VLMs that act on GUIs — perception, planning, action loops, computer-use agents |
| 08 | [Native Multimodal](05%20-%20Multi-Modal/08%20-%20Native%20Multimodal.ipynb) | Any-to-any unified token spaces — Chameleon, Transfusion, Emu3, Janus Pro with VQ-VAE tokenizers |

### Coming Soon

| Topic | Description |
|-------|-------------|
| Training Strategy | Training data curation, loss functions, distributed training, and GPU programming |
| Model Serving | vLLM, PagedAttention, autoscaling, and production deployment |
| MLOps | Experiment tracking, model versioning, CI/CD for ML, monitoring, and drift detection |
| LLM Benchmarks | MMLU, HumanEval, GSM8K — standardized evaluation and leaderboard methodology |
| AI Governance | Red teaming, toxicity benchmarks, bias evaluation, hallucination detection |

---

More work is coming. This repository is actively maintained and expanding as the field evolves.
