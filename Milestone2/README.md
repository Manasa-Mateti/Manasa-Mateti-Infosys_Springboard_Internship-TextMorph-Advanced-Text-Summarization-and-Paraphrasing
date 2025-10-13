# Infosys TextMorph: Milestone 2  
### Advanced Text Summarization with Interactive UIs and Visualizations  
 
## 📘 Overview  

This milestone focuses on implementing **advanced text summarization** techniques and developing **interactive UIs** in Google Colab to visualize model performance.  

### Key Tasks of this Milestone2 
- Implement **abstractive** and **extractive** text summarization.  
- Evaluate summaries using standard **metrics**.  
- Develop **two interactive UIs** using `ipywidgets`.  
- Test on **10+ sample texts** from diverse domains.  
- **Visualize** model performance using plots.  

## 🎯 Objectives  

### Abstractive Summarization Models  
- **TinyLlama** – `TinyLlama/TinyLlama-1.1B-Chat-v1.0`  
- **Phi** – `microsoft/phi-2`  
- **BART-large-cnn** – `facebook/bart-large-cnn`  
- **Gemma** – `google/gemma-2b-it`  

### Extractive Summarization  
- **TextRank** using `sentence-transformers (all-MiniLM-L6-v2)` and PageRank  

### Evaluation Metrics  
- **ROUGE**: ROUGE-1, ROUGE-2, ROUGE-L  
- **Semantic Similarity**  
- **Readability Metrics**: Flesch-Kincaid, Gunning-Fog  


## ⚙️ Setup Requirements  

### Hugging Face  
1. Create an account: [https://huggingface.co/](https://huggingface.co/)  
2. Generate a **read-access token**:  
   - Profile → Settings → Access Tokens  
3. Accept the license of different models. e.g.,**Gemma license**:from here [Gemma Model Page](https://huggingface.co/google/gemma-2b-it)  

### Google Colab  
- Use a **GPU runtime**  
  - `Runtime → Change runtime type → GPU`  
- Store the Hugging Face token in **Colab Secrets** as:  
  ```
  HF_TOKEN = your_token_here
  ```


## 🧩 Implementation Details  

### Install Required Libraries  
```bash
pip install transformers datasets torch sentence-transformers rouge-score nltk textstat
```

### Model Loading Example (Gemma)  
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id_gemma = "google/gemma-2b-it"

tokenizer = AutoTokenizer.from_pretrained(model_id_gemma, token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(
    model_id_gemma,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    token=HF_TOKEN
)

MODELS['gemma'] = model
```

### Supported Models  
| Model | Type | Model ID |
|--------|------|-----------|
| TinyLlama | Abstractive | TinyLlama/TinyLlama-1.1B-Chat-v1.0 |
| Phi | Abstractive | microsoft/phi-2 |
| BART | Abstractive | facebook/bart-large-cnn |
| Gemma | Abstractive | google/gemma-2b-it |
| TextRank | Extractive | sentence-transformers + PageRank |


## 🧠 Interactive UIs  

### 🧩 UI 1: Summarize with All Models  
- Text input area  
- Button to **generate summaries** from all models  
- Display:
  - Summaries
  - Evaluation metrics  

### 🧩 UI 2: Summarize with Specific Models  
- Text input area  
- **Checkboxes** to select specific models  
- Button to generate summaries  
- Display:
  - Summaries and metrics only for selected models  


## 📊 Evaluation & Visualization  

- Compute ROUGE, similarity, and readability scores.  
- Plot model-wise comparison of performance metrics using `matplotlib` or `seaborn`.  
- Analyze results over **10+ domain-specific texts**.  


## 🧾 Deliverables  

1. Google Colab notebook with:  
   - All model implementations  
   - Two interactive UIs  
   - Metric evaluation and plots  
2. Results tested on 10+ sample texts.  



### 👩‍💻 **Author**
**Manasa Mateti**  
Infosys Springboard Virtual Internship – *Advanced Text Summarization  with Interactive UIs and Visualizations (Milestone 2)* 