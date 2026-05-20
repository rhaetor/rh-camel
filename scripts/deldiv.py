from bs4 import BeautifulSoup
from pathlib import Path

def in_to_out(infile):
    bakfile = Path(str(infile.absolute()).replace('components', 'bak'))
    bakfile.parent.mkdir(parents=True, exist_ok=True)
    return bakfile

def stripdiv(infile: Path):

    with infile.open('r') as f:
        html = f.read()

    bakfile = in_to_out(infile)

    with bakfile.open('w') as f:
        f.write(html)

    soup = BeautifulSoup(html, 'html.parser')

    divs = ['edit-this-page', 'page-versions', 'context' ]

    for div_class in divs:

        # Find the div with class "delete"
        div_to_delete = soup.find('div', class_=div_class)

        # If the div is found, remove it
        if div_to_delete:
            div_to_delete.decompose()

    outfile=infile

    with outfile.open('w') as f:
        f.write(str(soup.prettify()))


def main():
    comp_dir = Path('components')

    for fiel in Path(comp_dir).rglob('*.html'):
        stripdiv(fiel)

if __name__ == "__main__":
    main()
