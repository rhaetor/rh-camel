#!/usr/bin/env python3
import os
from pathlib import Path 

dir = Path('.')

files = list(dir.rglob("*.html"))
print(files)
for fpth in files:
    with open(fpth,"r") as f:
        content=f.read()
        for line in content:
            if "Red Hat" in line:
                print(line)

        newcont=content.replace("Red Hat Integration", "Red Hat Apache Camel")
        newcont=content.replace('href="/" > Red Hat Integration < /a >', 'href="https://rhaetor.github.io/rh-camel/manual/" > Red Hat Apache Camel Manual < /a >')
