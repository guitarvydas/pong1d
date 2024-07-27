# Larson scanner on command line in 0D
https://shop.evilmadscientist.com/productsmenu/152
# usage
## stripped down
uses main.py which uses global variables and does no error checking
`make`
## full
`make full`
uses main-full.py which creates Objects on the heap and does some error checking
# Tour
- see `scanner3.drawio` (use the drawio editor https://app.diagrams.net) to see the source code
- see `main.py` to look at the lower-code Python implementation of Count, Reverser, Decode, and, Delay
- see `main-full.py` to see the Python implementation
- see `scanner3.drawio.json` to see the automatically-generated wiring lists
- see `py0d.py` for the full-blown implementation of the 0D kernel (it used to consist of several separate files), the concepts are simple, but when written out in a "modern" programming language, the code looks ugly (I think of it as assembler, anyway, and who bothers to look at assembler? I create source code as pictures).
# N.B.
- components written in Python 0D can use components written in other languages, thanks to VSH (included)
- I strive for MVI (Minimum Viable Implementation) - skimp on efficiency instead of MVP-style skimping on product
  - make it correct first, then optimize
  - if it's useful, then someone will figure out how to make it faster / better
  - avoid premature optimization (which seems to be encouraged by "modern" programming languages)
  
