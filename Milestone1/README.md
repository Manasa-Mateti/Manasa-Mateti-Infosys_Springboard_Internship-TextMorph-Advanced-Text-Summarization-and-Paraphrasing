
# 🧠 Infosys Springboard Internship – Milestone 1  
## **Text Summarization and Paraphrasing using Pretrained Transformer Models**

### 📘 **Overview**
This milestone focuses on implementing and evaluating **state-of-the-art transformer-based models** for **text summarization** and **paraphrasing** tasks. The project explores how different pretrained models such as **T5**, **BART**, and **PEGASUS** perform on two given input topics — *Artificial Intelligence* and *Renewable Energy.*



### ⚙️ **How to Run**
1. Open `Milestone1.ipynb` in **Google Colab**.  
2. Set the runtime to **GPU** for faster execution.  
3. Run all cells sequentially from top to bottom.  
4. Generated summaries, paraphrases, and evaluation results will be saved automatically.  
5. Export results for documentation or analysis.



### 🧮 **Tasks Implemented**
#### **1. Text Summarization**
Summarization is the process of **condensing a long piece of text into a shorter version** while preserving key information and meaning.  
We implemented three pretrained transformer models for abstractive summarization:
- **T5-base** — A versatile model trained on multiple NLP tasks, converts text-to-text (e.g., “summarize: <text>”).  
- **BART-large-CNN** — Combines bidirectional (BERT-like) and autoregressive (GPT-like) architectures for fluent, coherent summaries.  
- **PEGASUS-XSum** — Specially pre-trained for summarization tasks using gap-sentence prediction, often giving human-like concise results.

#### **2. Text Paraphrasing**
Paraphrasing is the task of **rephrasing a given text** while retaining the original meaning.  
We implemented and compared the following models:
- **Vamsi/T5_Paraphrase_Paws**
- **mrm8488/pegasus_paraphrase**
- **eugenesiow/bart-paraphrase**



### 📊 **Evaluation Metrics**
#### **Summarization Evaluation**
- **ROUGE-1, ROUGE-2, ROUGE-L:**  
  Measure overlap between generated summaries and reference summaries based on word and phrase matching.

#### **Paraphrasing Evaluation**
- **BERTScore:**  
  Measures **semantic similarity** between original and paraphrased text using contextual embeddings from BERT.



### 📈 **Evaluation Results**
 Model - Task - Evaluation Metrics - Observation 

**T5-base** - Summarization - ROUGE - Produced informative but slightly literal summaries 
**BART-large-CNN** - Summarization - ROUGE - Generated fluent, natural sentences 
**PEGASUS-XSum** - Summarization - ROUGE - Created concise and human-like summaries 
**T5-Paraphrase** - Paraphrasing - BERTScore - Balanced accuracy and readability 
**PEGASUS-Paraphrase** - Paraphrasing - BERTScore - Produced more creative paraphrases 
**BART-Paraphrase** - Paraphrasing - BERTScore - Generated grammatically fluent outputs 



### 💡 **Observations**
- **PEGASUS** achieved the **best summarization quality**, producing short, fluent, and contextually rich summaries.  
- **T5** offered more factual accuracy but sometimes lacked smoothness in phrasing.  
- **BART** maintained grammatical fluency and readability across both tasks.  
- For **paraphrasing**, semantic similarity was strongest with **T5-Paraphrase**, while **PEGASUS** was more expressive.



### 🧾 **Conclusion**
This milestone successfully demonstrated:
- Implementation of transformer-based models for NLP generation tasks.  
- Comparison of summarization and paraphrasing outputs using both quantitative (ROUGE, BERTScore) and qualitative (manual review) evaluations.  
- Insight into model behavior and their trade-offs in fluency, conciseness, and factual retention.


### 🧠 **Key Definitions**
 Concept - Description 

 **Summarization** - Condensing text while preserving meaning. 
 **Paraphrasing** - Rewriting text using different words but same meaning. 
 **T5 (Text-to-Text Transfer Transformer)** - Treats every NLP task as text-to-text conversion. 
 **BART (Bidirectional and Auto-Regressive Transformer)** - Denoising autoencoder combining BERT and GPT techniques. 
 **PEGASUS (Pre-training with Extracted Gap-sentences)** - Transformer trained specifically for abstractive summarization. 
 **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)** - Measures text overlap between system and reference summaries. 
 **BERTScore** - Uses deep contextual embeddings to measure semantic similarity. 


### 👩‍💻 **Author**
**Manasa Mateti**  
Infosys Springboard Virtual Internship – *Advanced Text Summarization and Paraphrasing (Milestone 1)*  
