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

# run_diamond

# build db
echo 'Building database for GT25'
diamond makedb \
    --in data/sequences/gt25.fasta \
    --db data/sequences/gt25.diamond

# run diamond
echo 'Running DIAMOND for GT25'
diamond blastp \
    --db data/sequences/gt25.diamond \
    --query data/sequences/gt25.fasta \
    --out data/sequences/gt25.diamond.out \
    --outfmt 6 qseqid sseqid qlen slen length pident evalue bitscore \
    --evalue 10 \
    --max-target-seqs 0

# build db
echo 'Building database for GT31'
diamond makedb \
    --in data/sequences/gt31.fasta \
    --db data/sequences/gt31.diamond

# run diamond
echo 'Running DIAMOND for GT31'
diamond blastp \
    --db data/sequences/gt31.diamond \
    --query data/sequences/gt31.fasta \
    --out data/sequences/gt31.diamond.out \
    --outfmt 6 qseqid sseqid qlen slen length pident evalue bitscore \
    --evalue 10 \
    --max-target-seqs 0
