Hmm, I don't sound very convincing. Let me try to say it a different way.

The problem with electronics CAD (and PCBs) is that it's not very layered.

You can draw a schematic of the whole thing, using chips someone sold to you, but, you can't (easily) make your own chips.

The ideal would be to make sub-schematics that look like just like chips - without needing to own a clean room.

To do that, you need to make sub-chips ("Containers") that wire up other chips. Recursively. A sub-chip might use other sub-chips and so on.

Ideally, you should be able to make a circuit that uses sockets for all chips. You can plug code-chips into the sockets - or - you can plug sub-chips into the sockets.

To make something like that, using sockets, you need to ensure that the chips are totally devoid of external routing info - the Container needs to control the routing.

In this specific case, you have one wiring netlist - the var "wires". How do we use the whole scanner thing as a chip in some other circuit? How does the other circuit get used by yet another circuit. A: The "scanner" circuit needs to have input and output ports, just like any other chip. This line of thinking leads to a bunch of little details. Like, if you allow one queue per port, then you might get unexpected deadlock when you start plugging things together hierarchically. And, abstraction. You want to draw a schematic and when it gets to be too unwieldy, you want to lasso a portion of it and move it to its own sub-chip, with fewer ports on the outside (e.g. 10 chips with a total of 20 ports gets elided as 1 chip with only 1 input port and one output port - you want to elide the 10 chips, but, you also want to elide all of their ports).

Analogy: In Lisp, a List can contain (1) Lists, and/or (2) Atoms. The contained Lists can contain (1) Lists, and/or Atoms. Turtles all the way down. Similarly in my kind of CAD, Chips can be (1) circuits containing other chips, and/or (2) code.

The `direction` stuff falls out of that kind of thinking. A bundles of wires can (1) shove inputs to children chips, and, (2) the childrens' outputs can shove results onto output wires in the bundle, and, (3) the bundle can describe connections between pins on internal sockets to other pins on internal sockets. The (4)th possibility is that wires can go straight through from inputs to outputs of the Container to stub out the innards of a not-yet-implemented chip.

Analogy: Arduino shields. It's easier to breadboard your own Arduino shields. Imagine that you could plug many other Arduino shields into a shield, to create a tower of shields.

Further:

You must not allow a sub-chip to react to more than one input message at a time. It must look like a code chip, no matter how many layers it is composed of. That's what the `busy` stuff is about (busy testing is recursive).

Does that explanation change anything?
