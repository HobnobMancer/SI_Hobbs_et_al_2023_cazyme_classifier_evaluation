# SI_Hobbs_et_al_2023_cazyme_classifier_evaluation
Supplementary Information for the independent benchmarking of CAZyme classifiers dbCAN, eCAMI and Hotpep

[![DOI](https://zenodo.org/badge/624780187.svg)](https://zenodo.org/badge/latestdoi/624780187)

This repository contains supplementary information for analyses reported in Hobbs et al. (2023), independently and comprehensively evaluating the CAZyme classifiers dBCAN2, dbCAN3, dbCAN4, eCAMI and CUPP.

A citation for this work will be added once available. At the present please cite this repository as the source, the DOI:10.5281/zenodo.8123588, and the authors (in order):
Emma E. M. Hobbs<sup>1,2,3</sup>, Tracey, M. Gloster<sup>1</sup>, Leighton Prichard<sup>2</sup>.

> 1. School of Biology and Biomedical Sciences Research Complex, University of St Andrews, North Haugh, St Andrews, Fife, KY16 9ST, UK
> 2. Strathclyde Institute of Pharmacy and Biomedical Sciences, University of Strathclyde, Glasgow G4 ORE, UK
> 3. Cell and Molecular Sciences, James Hutton Institute, Invergowrie, Dundee DD2 5DA, UK

```latex
@misc{Hobbs2023,
author = {Emma E. M. Hobbs and Tracey M. Gloster and Leighton Pritchard},
title = {Independent and Comprehensive
Benchmarking of CAZyme classifiers: dbCAN,
Hotpep, CUPP and eCAMI},
howpublished = {\url{https://hobnobmancer.github.io/SI_Hobbs_et_al_2023_cazyme_classifier_evaluation/}},
year = {2023},
note = {Version 1. DOI:10.5281/zenodo.8123588}
}
```

## The comprehensive report can be found [here](https://hobnobmancer.github.io/SI_Hobbs_et_al_2023_cazyme_classifier_evaluation/notebooks/2023-cazyme-classifier-eval.html)

To reproduce the analyses, run all commands provided in the walkthrough from the root of this directory.

# Independent and comprehensive evaluation of CAZyme classifiers
## [Link to the final evaluation and report](https://hobnobmancer.github.io/SI_Hobbs_et_al_2023_cazyme_classifier_evaluation/notebooks/2023-cazyme-classifier-eval.html)

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
conda create -n pyrewton python=3.9 cazomevolve mmseqs2 -y
conda activate pyrewton
conda install --file requirements.txt -y -c bioconda -c conda-forge -c predector
pip3 install pyrewton
```

### dbCAN version 2
The installation instructions for `dbCAN` v==2.0.11 can be found [here](https://github.com/linnabrown/run_dbcan/tree/fde6d7225441ef3d4cb29ea29e39cfdcc41d8b19) and were followed to install dbCAN for the analysis presented in the manuscript.

### dbCAN version 3
v==3.0.7

### dbCAN version 4
v==4.0.0

### CUPP
ADD INSTALLATION INSRUCTIONS

### Repo installation structure

```bash
tools
dbcan_2
dbcan_3
dbcan_4
```

**A separate virual environment was created for each version of dbCAN**

# Method: Reproducing the analyses

Several of the data files required to repeat the analyses presented in the manuscript are stored (available for use) in the repo. These files are stored in the `data/` directory:

## Build a local CAZyme database

Configure using [`cazy_webscraper`](https://hobnobmancer.github.io/cazy_webscraper/) (Hobbs _et al., 2022) to download all data from the CAZy database, and compile the data into a local CAZyme database.

> cazy_webscraper: local compilation and interrogation of comprehensive CAZyme datasets
Emma E. M. Hobbs, Tracey M. Gloster, Leighton Pritchard
bioRxiv 2022.12.02.518825; doi: https://doi.org/10.1101/2022.12.02.518825

The CAZy database was downloaded on 2023-07-26 using the bash script `download_cazy.sh`.

```bash
scripts/cazy/download_cazy.sh <email>
```

This generated the local CAZyme database `data/cazy/cazy-db_2023-07-26.db`.

## Select test sets

Retrieved the test sets from the previous evaluation (presented in the following poster [Hobbs et al., 2021](https://doi.org/10.6084/m9.figshare.14370836.v3)), which comprised 40 bacterial and 30 eukaryotic genomes.

The bash script `get_cazy_sampling.sh` was used to coordinate querying the local CAZyme database (`data/cazy/cazy-db_2023-07-26.db`) to extract the number of unique GenBank protein IDs associated with each species listed in CAZy. These data were written to a CSV file by the bash script (`data/test_sets/cazy_species_sizes.csv`).

The CSV file was mannually explore to identify an addition 10 eukaryotic genomes, with the assembly status of 'complete' in the NCBI Assembly database and containing at least 100 proteins listed in the local CAZyme database , to be added to the test sets from the previous evaluation.

**Output:**
* A CSV file listing all tests sets (including the taxonomic classification (including kingdom, genus and species)) is presented in `data/test_sets/test_sets-summary.csv`.

The Python script `csv_to_yml.py` was used to generate a Yaml file summarising the test sets, and to write out all the NCBI Assembly version accessions to a plain text file (`data/test_sets/test_sets.txt`).

```bash
scripts/test_sets/csv_to_yml.py
```

**Output:**
* The NCBI Assembly version accession for each test set is listed in `data/test_sets/test_sets-genomes.txt`
* A YAML file listing the NCBI taxonomic ID and associated NCBI Assembly version accession and assembly name for each genome, written to `data/test_sets/test_sets-taxs.yaml`

GenBank assemblies were used for this analysis not reference (RefSeq genomes) because CAZy primarily annotates protein sequences from the NCBI GenBank database, and thus contains very few proteins from the NCBI RefSeq database.

## Compile test sets

The plain text file of NCBI Assembly version accessions (`data/test_sets/test_sets-genomes.txt`) was used as input to `ncbi-genome-download` tool to download the protein FASTA files for each assembly. This was coordinated using the bash script `download_genomes.sh`:

```bash
scripts/test_sets/download_genomes.sh
```

The protein FASTA files were written to the `data/test_sets/proteomes` directory.

`pyrewton` was used to generate a data set per downloaded genome .faa file, consisting of 100 randomly selected proteins that are listed in the local CAZy database (from here on referred to as 'known CAZymes'), and the 100 protein sequences with the highest BLAST Score Ratio against the 100 selected known CAZymes (from here on referred to as 'known non-CAZymes').

This was coordinated using the bash script `create_test_sets.sh`

```bash
scripts/test_sets/create_test_sets.sh
```

**Output:**
* For each genome, a single test set is created containing a total of 200 sequences, written to disk as a multisequence protein FASTA file (`.faa`). These are stored in `data/test_sets/test_sets/test_sets/` directory.
* The CSV files describing the alignment scores were written to `data/test_sets/test_sets/alignment_scores` by `pyrewton`.
* A CSV file summarising the proportion of the respective CAZome incorported into each test set (`data/test_sets/test_sets/cazome_coverage_2023_07_26-10_38_27.txt`)
* A CSV file listing the NCBI protein version accessions of all proteins incorported into all test sets, and also listing the NCBI Assemmbly version accession of the source genome and marking if the protein is (1) or is not (0) listed in the local CAZyme database (`data/test_sets/test_sets/test_set_composition_2023_07_26-10_38_27.txt`)

## Run CAZyme classifiers

Each CAZyme classifier was used to parse all test sets FASTA files. A separate bash script was used to coordinate running each CAZyme classifier:

**dbCAN_2**:
```bash
scripts/tools/run_dbcan_2.sh
```

**dbCAN_3**:
```bash
scripts/tools/run_dbcan_3.sh
```

**dbCAN_4**:
```bash
scripts/tools/run_dbcan_4.sh
```

**CUPP**:
```bash
scripts/tools/run_cupp.py
```

The output for all tools was written to the `data/tool_outputs` directory. 

Each tool is given its own subdirectory within `data/tool_outputs/`.

Each test set is given it own subdirectory within each tool subdirectory:

```bash
└── data
   └── tools_output
      ├── cupp
      │   ├── GCA_900635675.1
      │   └── GCA_900638075.1
      │       ├── cupp.log
      │       ├── cupp_output.fasta
      │       └── cupp_output.fasta.log
      ├── dbcan_2
      │   ├── GCA_900635675.1
      │   └── GCA_900638075.1
      │       ├── dbcan.log
      │       ├── diamond.out
      │       ├── hmmer.out
      │       ├── Hotpep.out
      │       ├── overview.txt
      │       └── uniInput
      ├── dbcan_3
      │   ├── GCA_900635675.1
      │   └── GCA_900638075.1
      │       ├── dbcan.log
      │       ├── diamond.out
      │       ├── eCAMI.out
      │       ├── hmmer.out
      │       ├── overview.txt
      │       └── uniInput
      └── dbcan_4
          ├── GCA_900635675.1
          └── GCA_900638075.1
              ├── dbcan.log
              ├── dbsub.out
              ├── diamond.out
              ├── dtemp.out
              ├── hmmer.out
              ├── overview.txt
              └── uniInput
```

## Calculate statistics

Use `pyrewton` to calculate performance statistics for each level of classification.

Use the YAML file `data/test_sets/test_sets-kingdoms.yaml` and the `--tax_groups` flag to evaluate the performance across all test sets and per taxonomic kingdom.

```bash
scripts/calculate_stats.sh
```

The levels of classification that are evaluated:
* Binary CAZyme/non-CAZyme classification
* Binary classification per CAZy class
* Multilabel CAZy class classification
* Binary classification per CAZy family
* Multilabel classification per CAZy family

The performance statistics calculated for each level of CAZyme classification: 
* Sensitivity
* Specificity
* Precision
* F1-score
* Accuracy
* Rand index (multi-label classifications only)
* Adjusted Rand index (multi-label classifications only)

Statistics were calculated across the entire data set, and per kingdom (bacteria and eukaryotes).

Statistics were calculated for each classifier and per tool witihn each classifier:
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
* CUPP

The output (a series of dataframes) were written to the `results/` directory. Note, owing to the number and sizes of the files, the `results/` directory is provided as a ZIP archive file in this repository.


# The Report and Evaluation

The RMarkdown notebook `notebooks/2023-cazyme-classifier-eval.Rmd` was used to interrogate and visulise the performance statistics calculated by `pyrewton`. 

A HTML version of notebook can be [viewed here](https://hobnobmancer.github.io/SI_Hobbs_et_al_2023_cazyme_classifier_evaluation/notebooks/2023-cazyme-classifier-eval.html).

All output from the notebook is available in the `report/` directory. Note, owing to the number and sizes of the files, the `report/` directory is provided as a ZIP archive file in this repository.

After running the RMarkdown notebook, the Python script `summarise_family_populations.py` can be run to generate a CSV file listing  the number of unique NCBI protein version accessions listed in the local CAZyme database for each CAzy family, the total number of proteins included across all test sets per CAZy family, and the percentage of the CAZy family population represented in the test sets. This file is written to `data/test_sets/family_representation.csv`.

## Exploration of GT25 and GT31 sequence diversity

To explore if the consistently poor performance of the CAZyme classifiers for CAZy families GT25 and GT31 was the result of high sequence diversity within these families, an all-versus-all DIAMOND pairwise alignment analysis was performed for each family.

1. Download protein sequences

```bash
# downloads protein sequences from NCBI GenBank for GT25 and GT31
# Download protein sequences are stored in the local CAZyme database
scripts/seq_diversity/download_seqs.sh
```

2. Extract the protein sequences from the local CAZyme database and write the sequences to a multisequence FASTA file per family
```bash
scripts/seq_diversity/extract_seqs.sh
```

FASTA files written to:
* `data/sequences/gt25.fasta`
* `data/sequences/gt31.fasta`

3. Run DIAMOND for all pairs of sequences

```bash
scripts/seq_diversity/run_diamond.sh
```

Output written to:
* `data/sequences/sequences/gt25.diamond.out`
* `data/sequences/sequences/gt31.diamond.out`

3. Summarise and visualise the results

The Jupyter notebook `notebooks/gt_sequence_diversity.ipynb` was used to calculate the BLAST Score Ratio to facilitate comparing the degree of sequence similarity across all and to visualise the BSR.

The figures generated using this notebook are written to:
* `results/sequences/gt25-clustermap.pdf` - presented in the SI
* `results/sequences/gt25-clustermap-fullSized.pdf` - all labels are readable and is provided in the online repository
* `results/sequences/gt31-clustermap.pdf` - presented in the SI
* `results/sequences/gt31-clustermap-fullSized.pdf` - all labels are readable and is provided in the online repository
