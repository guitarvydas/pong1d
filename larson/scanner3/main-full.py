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
    zd.register_component (reg, zd.Template (name = "Delay", instantiator = delay))
    zd.register_component (reg, zd.Template (name = "Count", instantiator = count))
    zd.register_component (reg, zd.Template (name = "Reverser", instantiator = reverser))
    zd.register_component (reg, zd.Template (name = "Decode", instantiator = decode))
    zd.register_component (reg, zd.Template (name = "👀", instantiator = monitor))



## Leaf component implementations

class Counter:
    def __init__ (self):
        self.count = 0
        self.direction = 1
    def advance (self):
        self.count += self.direction
    def reverse (self):
        self.direction = self.direction * -1
def count_handler (eh, msg):
    inst = eh.instance_data
    if msg.port == "adv":
        inst.advance ()
        send_int (eh, "", inst.count, msg)
    elif msg.port == "rev":
        inst.reverse ()
    else:
        panic (f'bad message to count {msg.port}')
def count (reg, owner, name, template_data):
    counter = Counter ()
    name_with_id = zd.gensym ("Count")
    return zd.make_leaf (name_with_id, owner, counter, count_handler)

class ReverserState:
    def __init__ (self):
        self.state = "J"
def reverser_handler (eh, msg):
    inst = eh.instance_data
    if inst.state == "K":
        if msg.port == "J":
            send_bang (eh, "", msg)
            inst.state = "J"
        else:
            pass
    elif inst.state == "J":
        if msg.port == "K":
            send_bang (eh, "", msg)
            inst.state = "K"
        else:
            pass
    else:
        panic ("bad message to reverser handler")
def reverser (reg, owner, name, template_data):
    state = ReverserState ()
    name_with_id = zd.gensym ("Reverser")
    return zd.make_leaf (name_with_id, owner, state, reverser_handler)

def decode_handler (eh, msg):
    i = int (msg.datum.raw ())
    if i == 0:
        zd.send_string (eh, "0", "0", msg)
    elif i == 1:
        zd.send_string (eh, "1", "1", msg)
    elif i == 2:
        zd.send_string (eh, "2", "2", msg)
    elif i == 3:
        zd.send_string (eh, "3", "3", msg)
    elif i == 4:
        zd.send_string (eh, "4", "4", msg)
    elif i == 5:
        zd.send_string (eh, "5", "5", msg)
    elif i == 6:
        zd.send_string (eh, "6", "6", msg)
    elif i == 7:
        zd.send_string (eh, "7", "7", msg)
    elif i == 8:
        zd.send_string (eh, "8", "8", msg)
    elif i == 9:
        zd.send_string (eh, "9", "9", msg)
    else:
        panic (f'bad message to decode {i}')
    send_bang (eh, "done", msg)
def decode (reg, owner, name, template_data):
    name_with_id = zd.gensym ("Decode")
    return zd.make_leaf (name_with_id, owner, None, decode_handler)


def monitor (reg, owner, name, template_data):      
    name_with_id = zd.gensym ("?")
    return zd.make_leaf (name=name_with_id, owner=owner, instance_data=None, handler=monitor_handler)
def monitor_handler (eh, msg):
    s = msg.datum.srepr ()
    i = int (s)
    while i > 0:
        print (" ", end='')
        i -= 1
    print (f"{s}")

    
DELAYDELAY = 50000

class Delay_Info:
    def __init__ (self, counter=0, saved_message=None):
        self.counter = counter
        self.saved_message = saved_message

def first_time (m):
    return not zd.is_tick (m)

def delay_handler (eh, msg):
    info = eh.instance_data
    if first_time (msg):
        info.saved_message = msg
        zd.set_active (eh) ## tell engine to keep running this component with 'ticks'
    count = info.counter
    count += 1
    if count >= DELAYDELAY:
        zd.set_idle (eh) ## tell engine that we're finally done
        zd.forward (eh=eh, port="", msg=info.saved_message)
        count = 0
    info.counter = count

def delay (reg, owner, name, template_data):
    name_with_id = zd.gensym ("delay")
    info = Delay_Info ()
    return zd.make_leaf (name_with_id, owner, info, delay_handler)





# utility functions
def send_int (eh, port, i, causing_message):
    datum = zd.new_datum_int (i)
    zd.send (eh, port, datum, causing_message)

def send_bang (eh, port, causing_message):
    datum = zd.new_datum_bang ()
    zd.send (eh, port, datum, causing_message)

def panic (s):
    print (s)
    sys.exit (1)
    
main ()
