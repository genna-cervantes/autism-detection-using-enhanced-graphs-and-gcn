# 🧠 Unveiling Temporal Dynamics in fMRI Graphs

## Leveraging Dynamic Connectivity and TDep-Node2Vec for Enhanced Autism Detection

This repository contains the source code, data pipelines, and experimental results from our undergraduate thesis:  
**"Unveiling Temporal Dynamics in fMRI Graphs: Leveraging Dynamic Connectivity and TDep-Node2Vec for Enhanced Autism Detection"**

## 📖 Abstract

Functional Magnetic Resonance Imaging (fMRI) provides insights into the brain's functional organization, yet traditional static analysis often overlooks the brain's dynamic nature. In this thesis, we propose a novel pipeline that captures **temporal graph dynamics** in fMRI data through **Dynamic Functional Connectivity (DFC)** and a time-aware graph embedding algorithm, **TDep-Node2Vec**.  
By modeling time-evolving brain networks and learning temporally contextualized node embeddings, our framework significantly improves the performance of **Autism Spectrum Disorder (ASD)** detection tasks.

---

## 🚀 Key Contributions

- 📊 **Dynamic Graph Construction** using sliding window correlation for fMRI time series
- 🔁 **Time-Dependent Node2Vec (TDep-Node2Vec)**: An adaptation of Node2Vec for dynamic graphs
- 🧠 **Graph-based ASD Classifier** using learned embeddings and graph-level representations

---

## 🗂️ Project Structure

- To be updated

---

## 🧪 Methodology

1. **Preprocessing**

   - ABIDE dataset (Autism Brain Imaging Data Exchange)
   - Standard fMRI preprocessing pipeline (motion correction, normalization)

2. **Dynamic Functional Connectivity**

   - Sliding window Pearson correlation to generate dynamic adjacency matrices

3. **TDep-Node2Vec**

   - Temporal random walk strategy across graph snapshots
   - Node2Vec embedding with time-aware context

4. **GCN**

   - Use residual connections
   - Sparse graph techniques to prevent overfitting

5. **Classification**
   - Aggregated graph embeddings for subject-level classification
   - Evaluation using Logistic Regression and GNN-based classifiers

---

## 📊 Results Summary

- To be updated

---

## 👥 Authors

- **Cervantes, Genna B.**, University of Santo Tomas BSCS
- **De Guzman, Mar Vincent**, University of Santo Tomas BSCS
- **Duenas, John Axel**, University of Santo Tomas BSCS
- **Ilano, Carylle Keona**, University of Santo Tomas BSCS

---

## License

- This project is for academic research purposes only.
