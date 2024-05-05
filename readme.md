# coding challenges

collection of John Cricket's [coding challenges](https://codingchallenges.fyi)
implemented in python

## wc

`wc` was relatively trivial to implement given python's robust support of file
i/o and CLI arguments via the `argparse` module. From now on, I will implement
the programs both in python and C++ to improve my proficiency in the latter.

The only tricky part was incorporating stdin into the program. John
included this as a final "gotcha" - if you designed your program to be modular (i.e.
separating input reading vs. processing ), this last part is trivial. If not,
you have to refactor nearly your entire program. 

This exercise demonstrates the importance of planning (just a bit) before
coding. While premature optimization is indeed the root of all evil, it helps to
structure your program through minimal abstractions if its structure is
well-defined, as nearly all CLI programs are.
