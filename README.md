# EncDec
The python encryption/decription module "encryption" can be include into an existing python project or you can call "EncDec.py" from the command line.
Use the -h or --help flags for more information on command line usage.
### Note
Both the encryption and XMLP modules need to be included in order to use the encryption module, though XMLP can be used on it's own.
At it's core, encryption utilises the XMLP module. XMLP is an XML pre-processor for python. It ships with some base directives but
can be expanded upon. The goal of XMLP is to make programming easier while testing and developing the right combinations of 
algorithms (in this case, function pipelining for encryption and decryption).

# Basic Usage and Adaptation
## Preamble
Admittedly, this has been more of learning exercise for myself than anything; I just thought someone might find something from this
useful.
## Amble
EncDec.py was an exercise in writing a command line interface for an application, using sys.argv[] params.
The core of this project is found in "encryption.py." 

The functionPipeliner function is called with a list of anonymous functions, as well as
a string to be passed from function to function. Each func follows the form of f(astring)->newstring.
The first argument to functionPipeliner must be a list of functions.
The XMLPreprocessor module ships with some basic functionality. specifically, the "ignore", "forward", "generate" and "reverse"
directives.

## A few things worth noting
Anything included in an ignore block wont be parsed by XMLP.
Anything included in a generate block will be overwritten!
Any directive aside from "ignore" and "generate" will have it's content read.
Standard XML syntax applies. The only difference is the prepending of a # symbol to suit python syntax.
### NB!!!
The forward and reverse blocks are written in the same direction, that is to say, you write funcA,
Then in the reverse block you'll write the counter function to A, and continue on in this fashion.


# How it works
The original intent was to perform a sequence of permutations, and then perform the counter-functions of those permutations in reverse order.
As the user may want to call some functions more than once, the "executionOrder" list became a core parameter for the primary ParseFile
function. the executionOrder list is a sequence of indices corresponding to the 0-indexed order of the function in either the forward or reverse blocks.
The parser also accepts an execution flag (either "f" "r" or "none" by default) in-case you only want to process a specific tag. 
##Again Note
Anything in the generate block previosuly generated will be overwritten.






