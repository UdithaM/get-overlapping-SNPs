# get-overlapping-SNPs
Given a set of regions as a BED format file, retrieve overlapping SNPs from dbSNP155.

## Make sure to [read, download and give permision to Linux bigBedtoBed utility](http://hgdownload.soe.ucsc.edu/downloads.html#utilities_downloads).

## Steps to use

### 1)  Clone this Github repository to your Linux computer/Server.
### 2) Go into the folder.

```sh
cd get-overlapping-SNPs
```

### 3) Make sure you get the correct paths as input arguments. You can type following command to find more about the input arguments.

```sh
python get_overlapping_SNPs.py --help
```
#### Output 

```
--------Get SNPs on Given Regions--------

positional arguments:
  Input_Filename   Path to BED file containing regions to look for overlapping SNPs. Required Columns = ['chr', 'bin_start', 'bin_end', 'id']
  Output_Filename  Name of output BED file. Ex: SNPs_on_regions.bed

optional arguments:
  -h, --help       show this help message and exit
```

### 4)  Use the following "sample" command to run the Python script to get overlapping SNPs from dbSNP155.
```sh
 python get_overlapping_SNPs.py test.bed output.bed
```