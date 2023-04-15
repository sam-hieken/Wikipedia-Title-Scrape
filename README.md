# Wikipedia-Title-Scrape
A simple, Unix pipe style python script to scrape all article titles from Wikipedia (ns0, 500 titles at a time), and print each to stdout (separated by \n).

It's recommended to use a background job, and redirect stdout and stderr; the recommended command is:

```
nohup python3 -u scrap.py > wikititles.txt 2> stderr.out &
```
