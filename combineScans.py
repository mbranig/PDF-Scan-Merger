from pdfrw import PdfReader, PdfWriter, PageMerge
import argparse

# Arguments
parser = argparse.ArgumentParser(description='Process scanned pdf documents. It takes two files, one with the front and one of the back of each page and shuffles them together into one single document.')

parser.add_argument('oddFile',
                    type = str,
                    nargs=1,
                    help='path to the pdf with all odd pages (starting from 1)',
                    default='examplefiles/odd.pdf')

parser.add_argument('evenFile',
                    type = str,
                    nargs=1,
                    help='path to the pdf with all even pages (starting from 2)',
                    default='examplefiles/even_rev.pdf')

parser.add_argument('resultFile',
                    type = str,
                    nargs=1,
                    help='path and name where the shuffled file should be stored',
                    default='examplefiles/all.pdf')

parser.add_argument('--oddrev',
                    dest='oddrev',
                    action='store_const',
                    const=True,
                    default=False,
                    help='reverses the odd pages before shuffling')

parser.add_argument('--evenrev',
                    dest='evenrev',
                    action='store_const',
                    const=True,
                    default=False,
                    help='reverses the even pages before shuffling')

args = parser.parse_args()

# The shuffling magic
even = PdfReader(args.evenFile[0])
odd = PdfReader(args.oddFile[0])
isEvenReversed = args.evenrev;
isOddReversed = args.oddrev;
all = PdfWriter()
blank = PageMerge()
blank.mbox = [0, 0, 612, 792] # 8.5 x 11
blank = blank.render()

if isEvenReversed and not isOddReversed:
    for i in range(0, len(odd.pages)):
        all.addpage(odd.pages[i])
        all.addpage(even.pages[len(even.pages)-1-i])
elif isOddReversed and not isEvenReversed:
    for i in range(0, len(odd.pages)):
        all.addpage(odd.pages[len(odd.pages)-1-i])
        all.addpage(even.pages[i])
elif isEvenReversed and isOddReversed:
    for i in range(0, len(odd.pages)):
        all.addpage(odd.pages[len(odd.pages)-1-i])
        all.addpage(even.pages[len(even.pages)-1-i])
else:
    for x,y in zip(odd.pages, even.pages):
      all.addpage(x)
      all.addpage(y)

all.write(args.resultFile[0])