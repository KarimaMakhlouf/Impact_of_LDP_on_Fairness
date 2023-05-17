# Impact-of-KRR-on-Fairness
Repository for the paper: Impact of Local Differential Privacy on Fairness. (Here the link to the arxiv needs to be added and the bibtex for citation).

# Codes & Datasets
All the experiments are implemented in Python 3. We use Random Forest model for classification with its default hyper-parameters and we use the
ten-fold cross-validation technique. For k-RR mechanism, we use the implementation in [Multi-Freq-LDPy Python library](https://github.com/hharcolezi/multi-freq-ldpy). Since LDP protocols and ML algorithms are randomized, we report average results over 20 runs. 
* The [datasets](https://github.com/KarimaMakhlouf/Impact_of_LDP_on_Fairness/tree/main/Datasets) folder includes all the used and generated datasets
* The [Results](https://github.com/KarimaMakhlouf/Impact_of_LDP_on_Fairness/tree/main/Results) folder contains all the results (as csv files) of fairness metrics before and after applying the KRR mechanism settings for all the datasets. The settings applied in this study are:
    - sLDP: only the protected attribute is obfuscated.
    - allsLDP: all sensitive attributes (including the protected attribute) are obfuscated.
    - alloLDP: all the attributes except the target are obfuscated.
    - ayLDP: only the protected attribute and the target are obfuscated. 
* For each dataset, three Jupyter notebooks are available:
    - 1_Generated_data.ipynb: Jupyter notebook for generating and preprocessing (for the Adult and Compas datasets) data.
    - 2_Experiments.ipynb: Jupyter notebook for computing fairness metrics and accuracy before and after applying KRR mechanism settings.
    - 3_Generating_Plots.ipynb: Jupyter notebook for generating Figures ... in the paper.
    
# Environment
Our codes were developed using Python 3 with numpy, and pandas libaries. The versions are listed below:
* Python 3.7.3
* Numpy 1.21.2
* Pandas 1.3.3

# Contact
For any question, please contact:

[Karima Makhouf](http://www.lix.polytechnique.fr/Labo/Karima.MAKHLOUF/): karima.malhlouf [at]inria.fr

[Héber H. Arcolezi](https://hharcolezi.github.io/): heber.hwang-arcolezi [at] inria.fr

