#!/usr/bin/env python3

import ipdb

def tracing_the_function():
    inside_the_function = "We're inside the function"
    print(inside_the_function)
    print("We're about to stop because of ipdb!")
    where_the_fuck_the_function = "heyy this is still readable till set trace"
    print(where_the_fuck_the_function)
    ipdb.set_trace()
    this_variable_hasnt_been_interpreted_yet = \
        "The program froze before it could read me!"
    print(this_variable_hasnt_been_interpreted_yet)
    

tracing_the_function()
