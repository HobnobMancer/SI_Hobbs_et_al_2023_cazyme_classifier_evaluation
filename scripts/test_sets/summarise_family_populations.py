#!/usr/bin/env bash
#
# (c) University of St Andrews 2023
# (c) University of Strathclyde 2023
# (c) James Hutton Institute 2023
#
# Author:
# Emma E. M. Hobbs
#
# Contact
# eemh1@st-andrews.ac.uk
#
# Emma E. M. Hobbs,
# Biomolecular Sciences Building,
# University of St Andrews,
# North Haugh Campus,
# St Andrews,
# KY16 9ST
# Scotland,
# UK
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Compile test sets for testing the run time of each classifier."""


import json
import pandas as pd

from tqdm import tqdm


SAMPLE_SIZES = "results/CAZy_fam_testset_freq_2023_08_01.json"
POPULATIONS = "results/CAZy_fam_populations_2023_08_01.json"


with open(SAMPLE_SIZES, "r") as fh:
    samples = json.load(fh)

with open(POPULATIONS, "r") as fh:
    pops = json.load(fh)

fams = 0
df_data = []  # [[fam, sample size, population, percentage]]
for fam in tqdm(pops, desc="Calculating sample sizes"):
    pop = pops[fam]
    sample = samples[fam]
    if sample != 0:
        fams += 1
    try:
        percentage = round((sample / pop) * 100, 2)
    except ZeroDivisionError:
        percentage = 0
    df_data.append([fam, sample, pop, percentage])

df = pd.DataFrame(df_data, columns = ['Family','Sample_size','Population','Percentage_in_test_sets'])

print(f"Analysis includes {fams} CAZy families out of {len(list(pops.keys()))}")
df.to_csv("data/test_sets/family_representation.csv")
