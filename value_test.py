import os
from lxml import etree

if __name__ == '__main__':

    # Where to look for saved IATI XML via registry-refresher
    rootdir = '/home/alex/git/IATI-annual-report-2020/data'

    thousand_sep_count = 0
    total_count = 0

    for subdir, dirs, files in os.walk(rootdir):
        for filename in files:
            filepath = os.path.join(subdir, filename)
            publisher = os.path.basename(subdir)
            print(filename)
            try:
                root = etree.parse(filepath).getroot()
            except etree.XMLSyntaxError:
                continue
            values = root.xpath("//value/text()")
            for value in values:
                if "," in value:
                    thousand_sep_count += 1
                total_count += 1

    print("{} out of {} have a comma.".format(thousand_sep_count, total_count))
