from pdfrw import PdfReader, PdfWriter, PageMerge

even = PdfReader('examplefiles/even_rev.pdf')
odd = PdfReader('examplefiles/odd.pdf')
isEvenReversed = True
all = PdfWriter()
blank = PageMerge()
blank.mbox = [0, 0, 612, 792] # 8.5 x 11
blank = blank.render()

#all.addpage(blank)
if isEvenReversed:
    for i in range(0, len(odd.pages)):
        all.addpage(odd.pages[i])
        all.addpage(even.pages[len(even.pages)-1-i])
else:
    for x,y in zip(odd.pages, even.pages):
      all.addpage(x)
      all.addpage(y)

#while len(all.pagearray) % 2:
#  all.addpage(blank)

all.write('examplefiles/all.pdf')
