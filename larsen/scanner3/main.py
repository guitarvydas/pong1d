import py0d as zd
import sys

def main ():
    arg_array = zd.parse_command_line_args ()
    root_project = arg_array [0] 
    root_0D = arg_array [1]
    arg = arg_array [2]
    main_container_name = arg_array [3]
    diagram_names = arg_array [4]
    palette = zd.initialize_component_palette (root_project, root_0D, diagram_names, components_to_include_in_project)
    zd.run (palette, root_project, root_0D, arg, main_container_name, diagram_names, start_function,
              show_hierarchy=False, show_connections=False, show_traces=False, show_all_outputs=False)

def start_function (root_project, root_0D, arg, main_container):
    source = zd.new_datum_string (f'{arg}')
    srcmsg = zd.make_message("start", source)
    zd.inject (main_container, srcmsg)


## Leaf components for this project...
def components_to_include_in_project (root_project, root_0D, reg):
    zd.register_component (reg, zd.Template (name = "Tick", instantiator = tick))
    zd.register_component (reg, zd.Template (name = "Count", instantiator = count))
    zd.register_component (reg, zd.Template (name = "Reverser", instantiator = reverser))
    zd.register_component (reg, zd.Template (name = "Decode", instantiator = decode))



## Leaf component implementations

countdownmax = 10
class TickCounter:
    def __init__ (self):
        global countdownmax
        self.countdown = countdownmax
    def reset (self):
        global countdownmax
        self.countdown = countdownmax
    def dec (self):
        self.countdown -= 1
        return self.countdown <= 0
def tick_handler (eh, msg):
    inst = eh.instance_data
    inst.countdown -= 1
    if inst.dec ():
        send_bang (eh, "", msg)
        self.reset ()
def tick (reg, owner, name, template_data):
    counter = TickCounter ()
    name_with_id = zd.gensym ("Tick")
    return zd.make_leaf (name_with_id, owner, counter, tick_handler)

class Counter:
    def __init__ (self):
        self.count = 0
        self.direction = 1
    def advance (self):
        self.count += self.dir
    def reverse (self):
        self.direction = self.dir * -1
def count_handler (eh, msg):
    inst = eh.instance_data
    inst.advance ()
    send_int (eh, "", inst.count, msg)
def count (reg, owner, name, template_data):
    counter = Counter ()
    name_with_id = zd.gensym ("Count")
    return zd.make_leaf (name_with_id, owner, counter, count_handler)

def reverser_handler (eh, msg):
    send_bang (eh, "", msg)
def reverser (reg, owner, name, template_data):
    name_with_id = zd.gensym ("Reverser")
    return zd.make_leaf (name_with_id, owner, None, reverser_handler)

def decode_handler (eh, msg):
    i = int (msg.raw ())
    if i == 0:
        send_bang (eh, "0", msg)
    elif i == 1:
        send_bang (eh, "1", msg)
    elif i == 2:
        send_bang (eh, "2", msg)
    elif i == 3:
        send_bang (eh, "3", msg)
    elif i == 4:
        send_bang (eh, "4", msg)
    elif i == 5:
        send_bang (eh, "5", msg)
    elif i == 6:
        send_bang (eh, "6", msg)
    elif i == 7:
        send_bang (eh, "7", msg)
    elif i == 8:
        send_bang (eh, "8", msg)
    elif i == 9:
        send_bang (eh, "9", msg)
    else:
        raise "bad message to decode"
def decode (reg, owner, name, template_data):
    name_with_id = zd.gensym ("Decode")
    return zd.make_leaf (name_with_id, owner, None, decode_handler)

    



# utility functions
def send_int (eh, port, i, msg):
    datum = zd.new_datum_int (i)
    zd.send (eh, port, datum, causing_message)

def send_bang (eh, port, causing_message):
    datum = zd.new_datum_bang ()
    zd.send (eh, port, datum, causing_message)

main ()
