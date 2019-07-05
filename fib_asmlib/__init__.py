from . import imp

__all__ = [ "iterative" , "iterative_short" ]

iterative = imp.iterative
iterative_short = imp.iterative_short

algos = {'iterative': iterative,
         'iterative_short': iterative_short}
