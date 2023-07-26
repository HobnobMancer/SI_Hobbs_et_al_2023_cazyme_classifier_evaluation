# SI_Hobbs_et_al_2023_cazyme_classifier_evaluation
Supplementary Information for the independent benchmarking of CAZyme classifiers dbCAN, eCAMI and Hotpep

[![DOI](https://zenodo.org/badge/624780187.svg)](https://zenodo.org/badge/latestdoi/624780187)

This repository contains supplementary information for analyses reported in Hobbs et al. (2023), independently and comprehensively evaluating the CAZyme classifiers dBCAN2, dbCAN3, dbCAN4, eCAMI and CUPP.

Run all commands provided in the walkthrough from the root of this directory.

# Independent and comprehensive evaluation of CAZyme classifiers

CAZyme classifiers analyse query protein sequence and predict CAZyme domains and associated CAZy family annotations. This enables exploratory analysis of CAZyme complements not presently catalogued in the CAZy database (www.cazy.org). Each CAZyme classifier implements a different method to predict CAZy family annotations.

We previously published an evaluation of dbCAN2, eCAMI and CUPP ([Hobbs et al., 2021](https://doi.org/10.6084/m9.figshare.14370836.v3)). Since then, two standalone versions of dbCAN have been released (dbCAN3 and dbCAN4). Additionally, the previous analysis was limited to 70 genomes, over weighted towards bacterial genomes. To address these points, we present here an independent and comprehensive evaluation of the CAZyme classifiers:
* dbCAN2
* dbCAN3
* dbCAN4
* eCAMI
* CUPP
* HMMER (dbCAN4)
* dbCAN-sub (dbCAN4)
* DIAMOND (dbCAN4)

**Evaluating performance of:**
* Binary CAZyme/non-CAZyme classification
* Test set dependent performance of CAZyme/non-CAZyme classification
* Binary classification per CAZy class
* Multilabel CAZy class classification
* Binary classification per CAZy family
* Multilabel CAZy family classification

## CAZyme classifier references and names

The CAZyme classifier **dbCAN** is available as a webserver and a standalone tool. In this evaluation the standalone tool was used, and is referred to as **dbCAN**, references to the webserver are defined as the **dbCAN webserver**. The version numbers of the standalone tool and the webserver are independent of one another:
* The dbCAN2 webserver initally ran dbCAN version **2** (referred to as **dbCAN2**)
* The dbCAN2 webserver than implememented the standalone dbCAN version **3** (referred to as **dbCAN3**)
* The dbCAN3 webserver implements the standalone dbCAN version **4** (referred to as **dbCAN4**)

Each version of dbCAN implements multiple sequence alignment and modelling tools:
* dbCAN2:
  * DIAMOND
  * HMMER
  * Hotpep
* dbCAN3:
  * DIAMOND
  * HMMER
  * eCAMI
* dbCAN4:
  * DIAMOND
  * HMMER
  * dbCAN-sub (implementation of HMMER)
  
All references to implementing HMMER and DIAMOND refer to the implementation of these tools by dbCAN. For this evaluation, specifically the implementation of HMMER and DIAMOND by dbCAN4.

[**dbCAN2** and **dbCAN3**](https://doi.org/10.1093/nar/gky418)  
> Han Zhang and others, dbCAN2: a meta server for automated carbohydrate-active enzyme annotation, Nucleic Acids Research, Volume 46, Issue W1, 2 July 2018, Pages W95–W101  
> 
[**dbCAN4** and **dbCAN-sub (dbCAN)**](https://doi.org/10.1093/nar/gkad328)  
> Zheng J, Ge Q, Yan Y, Zhang X, Huang L, Yin Y. dbCAN3: automated carbohydrate-active enzyme and substrate annotation. Nucleic Acids Res. 2023 Jul 5;51(W1):W115-W121  
> 
[**eCAMI**](https://doi.org/10.1093/bioinformatics/btz908)  
> Xu J, Zhang H, Zheng J, Dovoedo P, Yin Y. eCAMI: simultaneous classification and motif identification for enzyme annotation. Bioinformatics. 2020 Apr 1;36(7):2068-2075  
> 
[**CUPP**](https://biotechnologyforbiofuels.biomedcentral.com/articles/10.1186/s13068-019-1436-5)  
> Barrett, K., Lange, L. Peptide-based functional annotation of carbohydrate-active enzymes by conserved unique peptide patterns (CUPP). Biotechnol Biofuels 12, 102 (2019).   
> 
[**HMMER**](https://academic.oup.com/bioinformatics/article/14/9/755/259550?login=false)  
> Eddy SR. Profile hidden Markov models. Bioinformatics. 1998;14(9):755-63.  
> 
[**DIAMOND**](https://www.nature.com/articles/nmeth.3176)  
> Buchfink, B., Xie, C. & Huson, D. Fast and sensitive protein alignment using DIAMOND. Nat Methods 12, 59–60 (2015). https://doi.org/10.1038/nmeth.3176 \

### You can find the full report, evaluating the CAZyme classifers [here ADD URL]().

All raw figure files presented in the complete report in the manuscript can be found in the `results/` directory.

Owing to the size of the data sets used, the figures are consequently compressed in the final manuscript. This remote repository contains the original full size, high resolution figures.

Additionally, some analyses are only briefly mentioned in the manuscript. The full method and results of these analyses are stored in this repository.

## How to use this repository.

You can use this repository like a website, to browse and see how we performed the analysis, or you can download it to inspect, verify, reproduce and build on our analysis.

## Downloading this repository

You can use `git` to _clone_ this repository to your local hard drive:

```bash
git clone git@github.com:HobnobMancer/SI_Hobbs_et_al_2023_cazyme_classifier_evaluation.git
```

Or you can download it as a compressed `.zip` archive from [this link](https://github.com/HobnobMancer/SI_Hobbs_et_al_2023_cazyme_classifier_evaluation/archive/refs/heads/master.zip).

## If you have problems with this repository

Please raise an issue at the corresponding `GitHub` page:

* [Issues for this repository](https://github.com/HobnobMancer/SI_Hobbs_et_al_2023_cazyme_classifier_evaluation/issues)

## Repo structure

The structure of this repository:

```bash
???
```

## Set up and reproducing analyses (quickstart)

You can use this archive to browse, validate, reproduce, or build on the phylogenomics analysis for the Hobbs et al. (2023) manuscript.

We recommend creating a conda environment specific for this activity, for example using the commands:
```bash
conda create -n pyrewton python=3.9 -y
conda activate pyrewton
conda install --file requirements.txt -y -c bioconda -c conda-forge -c predector
```

### dbCAN version 2
The installation instructions for `dbCAN` v==2.0.11 can be found [here](https://github.com/linnabrown/run_dbcan/tree/fde6d7225441ef3d4cb29ea29e39cfdcc41d8b19) and were followed to install dbCAN for the analysis presented in the manuscript.

# Method: Reproducing the analyses

Several of the data files required to repeat the analyses presented in the manuscript are stored (available for use) in the repo. These files are stored in the `data/` directory:

## ## Build a local CAZyme database

Configure using [`cazy_webscraper`](https://hobnobmancer.github.io/cazy_webscraper/) (Hobbs _et al., 2022) to download all data from the CAZy database, and compile the data into a local CAZyme database.

The CAZy database was downloaded on 2023-07-26.

> cazy_webscraper: local compilation and interrogation of comprehensive CAZyme datasets
Emma E. M. Hobbs, Tracey M. Gloster, Leighton Pritchard
bioRxiv 2022.12.02.518825; doi: https://doi.org/10.1101/2022.12.02.518825

```bash
# create a local CAZyme database
scripts/build_cazyme_db.sh <email>
```

This generated the local CAZyme database `data/cazy/cazy_db`.

