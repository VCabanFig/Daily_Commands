# Daily_Commands
Documentation of bash commands and python scripts used on a daily basis.


#### Count the number of bases in fastq file:

```
awk 'NR%4==2 {sum += length($0)} END {print sum}' file.fastq
```
#### Count the number of reads in fastq file:

```
echo $(cat file.fastq|wc -l)/4|bc
```


