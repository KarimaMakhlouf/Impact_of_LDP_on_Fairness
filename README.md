# Impact of Multi-dimensional Local Differential Privacy on Fairness
Repository for the paper: On the Impact of Multi-dimensional Local
Differential Privacy on Fairness. 

You can check the [Preprint](https://arxiv.org/abs/2312.04404) on Arxiv.


# Codes & Datasets
All the experiments are implemented in Python 3. We use Random Forest model for classification with its default hyper-parameters and we use the
ten-fold cross-validation technique. For k-RR mechanism, we use the implementation in [Multi-Freq-LDPy Python library](https://github.com/hharcolezi/multi-freq-ldpy). Since LDP protocols and ML algorithms are randomized, we report average results over 20 runs. 
* The [datasets](https://github.com/KarimaMakhlouf/Impact_of_LDP_on_Fairness/tree/main/Datasets) folder includes all the used and generated datasets
* The [Results](https://github.com/KarimaMakhlouf/Impact_of_LDP_on_Fairness/tree/main/Results) folder contains all the results (as csv files) of fairness metrics before and after applying the KRR mechanism settings for all the datasets. The settings applied in this study are:
    - sLDP: only the protected attribute is obfuscated.
    - allsLDP: a list of sensitive attributes (including the protected attribute) is obfuscated using KRR independently by applying the [k-based](https://link.springer.com/chapter/10.1007/978-3-031-37586-6_1) privacy splitting solution.
    - combLDP: a list of sensitive attributes (including the protected attribute) is obfuscated using the combined setting of KRR.
* For each dataset, three Jupyter notebooks are available:
    - 1_Generated_data.ipynb: Jupyter notebook for generating (for the synthetic dataset) or preprocessing (for the Adult and Compas datasets) the data.
    - 2_Experiments.ipynb: Jupyter notebook for computing fairness metrics and accuracy before and after applying KRR mechanism settings.
    - 3_Generating_Plots.ipynb: Jupyter notebook for generating all the results of the paper.
    
# Environment
Our codes were developed using Python 3 with numpy, and pandas libraries. The versions are listed below:
* Python 3.7.3
* Numpy 1.21.2
* Pandas 1.3.3
* Multi-freq-ldpy 0.2.4

# On-going
The repository is still under cleaning/generalization of the codes and the documentation.

# Merits
* We use the randomized mechanism KRR implemented in the [multi-freq-ldpy](https://github.com/hharcolezi/multi-freq-ldpy) library.
* We use the _Adult_ dataset from the [folktables](https://github.com/socialfoundations/folktables) library.
* We use the _Compas_ dataset from the [Kaggle](https://www.kaggle.com/datasets/danofer/compass) repository.

# Contact
For any questions, please contact:

[Karima Makhouf](http://www.lix.polytechnique.fr/Labo/Karima.MAKHLOUF/): karima.malhlouf [at]inria.fr

[Héber H. Arcolezi](https://hharcolezi.github.io/): heber.hwang-arcolezi [at] inria.fr

[Sami Zhioua](https://www.lix.polytechnique.fr/Labo/Sami.ZHIOUA/): zhioua[at]lix.polytechnique.fr

