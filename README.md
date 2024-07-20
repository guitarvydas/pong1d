# Example of peephole optimization
Example of peepholing using 0D (which uses t2t which uses OhmJS):

Keep Thinks Simple by dealing only with variable names and numeric constants. These fundamental concepts can be extended to include various types of other kinds of things (strings, floats, user-defined records, etc.)

`1 + x` --> `x + 1` --> `inc(x)`

`0 * (x + y * z)` --> `( x + y * z) * 0` --> 0

`1 + 2` --> `3`

# usage:
`make`

# files
## peephole.drawio
source code for peepholer (use the draw.io editor to view (https://app.diagrams.net))
## peephole.ohm
grammar
## peephole.rwr
rewrite specification (applied if parse based on the grammar was successful)
## normalize.ohm
example normalizer parser
- simplistic - looks for patterns that can be rearranged to reduce amount of edge-cases that the peepholer needs to consider
## normalize.rwr
example normalization rewriter
flip commutative operations so that constants are always on the right hand side (RHS)
# py0d.py
0D kernel
## support.js
support code, if needed (not needed by this simple example)
- written as a JavaSript namespace
## indenter.js
- use if you want to emit valid, indented Python code
## scrubber.js
- convert Unicode characters, etc. into valid characters for the target language
## main.py
## README.md
## Makefile
