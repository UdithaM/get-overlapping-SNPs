import os
import pandas as pd
import numpy as np
import sys
import argparse

parser = argparse.ArgumentParser(description="--------Get SNPs on Given Regions--------",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("Input_Filename", help="Path to BED file containing regions to look for overlapping SNPs. Required Columns = ['chr', 'bin_start', 'bin_end', 'id']")
parser.add_argument("Output_Filename",  help="Name of output BED file. Ex: SNPs_on_regions.bed")
args = parser.parse_args()
config = vars(args)


input_filename = config["Input_Filename"] 
output_filename = config["Output_Filename"]

os.system('mkdir -p ON_REGION_SNPs')

bins_df = pd.read_csv('%s' % input_filename, header=0, sep="\t")
for i,row in bins_df.iterrows():

    os.system('./bigBedToBed http://hgdownload.soe.ucsc.edu/gbdb/hg38/snp/dbSnp155.bb -chrom=%s -start=%s -end=%s ON_REGION_SNPs/%s.bed' % (row['chr'], row['bin_start'], row['bin_end'], row['id']))

    
SNP_concat_df = pd.DataFrame()

SNP_filenames = os.listdir('ON_REGION_SNPs/')

for filename in SNP_filenames:
    try:
        SNP_temp = pd.read_csv("ON_REGION_SNPs/%s" % filename, header=None, sep="\t")
        SNP_temp['region_id'] =	filename.split('.bed')[0]
        SNP_concat_df = pd.concat([SNP_concat_df,SNP_temp])
    except pd.errors.EmptyDataError:
       	continue
    
SNP_concat_df.columns = ['#chrom', 'chromStart', 'chromEnd', 'name', 'ref', 'altCount', 'alts',
       'shiftBases', 'freqSourceCount', 'minorAlleleFreq', 'majorAllele',
       'minorAllele', 'maxFuncImpact', 'SNP_class', 'ucscNotes', '_dataOffset',
       '_dataLen']
SNP_concat_df.to_csv('%s' % output_filename, sep='\t', header=True, index=False)

os.system('rm -r ON_REGION_SNPs/')


