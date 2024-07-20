brainstorming: 
Here's what I think that the Display unit might look like.

I don't (yet) know how to build this, so I am trying to spec it and get ChatGPT to write the code for me.

I ain't finished the game design yet, but, using a REPL attitude, I want to see this bit work, then riff on it.

ChatGPT gave me a bunch of code in python and in HTML, but wants me to use Flask, which I installed, but isn't found...


Write code in JavaScript or Python to build a local browser-based server that can display a 4x4 dot at one of 16 positions, left to right horizontally across the window. Position 0 is the left-most position, position 15 is the right-most position.

The server can be started from the command line and by opening a browser on a specific port.

The server is controlled by several commands on the command line:

0. start - clear the screen and display nothing, the user can open a local browser window on the appropriate port
1. pos N - clear the screen, display only the dot at position N
2. leftBAM - display a Batman-like BAM glyph at dot position 0 (left-most) for 1/2 a second, then erase it, leave the current dot displayed at the current position before, during and after the BAM 
3. rightBAM - same as #2, except display the BAM glyph at dot position 15
4. winnerL - clear the screen display a winner screen saying the the player on the Left won
5. winnerR - clear the screen display a winner screen saying the the player on the Right won
