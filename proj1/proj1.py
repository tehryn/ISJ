#!/usr/bin/env python3
import re;
import sys;
src = open(sys.argv[1], 'r');
output = open ('xmatej52.ipynb', 'w');
data = src.readlines();
i = 0;
for line in data:
	line = data[i];
	if "xkcd" in line:
		if( ("[" in line) and ("=" in line) ) is not ("!" in line):
			line = line.replace("xkcd", "xmatej52");
		line = re.sub( r"bu.*ls", "[gikuj]..n|a.[alt]|[pivo].l|i..o|[jocy]e|sh|di|oo", line);
	output.write(line);
	i=i+1;
output.close();
src.close();
#THIS IS THE END
