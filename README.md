# Wikipedia-Title-Scrape
A simple python script to scrape all article titles from Wikipedia (ns0, 500 titles at a time), and print each to stdout (separated by \n).

It's recommended to redirect stdout and stderr; run with something similar to the following:

```
nohup python3 -u scrap.py > wikititles.txt 2> stderr.out &
```
