#!/usr/bin/env python3
import os
from pathlib import Path 
from regex import re

dir = Path('.')

files = list(dir.rglob("*.html"))
for fpth in files:
    with open(fpth,"r") as f:
        content=f.readlines()
        for line in content:
            if "Red Hat" in line:
                line=line.replace('href="/" > Red Hat Integration < /a >', 'href="../../manual/index.html" > Red Hat build of Apache Camel manual < /a >')
                line=line.replace("Red Hat Integration", "Red Hat Apache Build of Apache Camel")
                print(line)
                #re.replace("<div class="edit-this-page">(.*?)Edit this Page</a></div>\n", "")


