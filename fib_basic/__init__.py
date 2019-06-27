from . import imp

__all__ = [ "recursive_dynamic", "iterative", "power_matrix", "algos"]

recursive_dynamic = imp.recursive_dynamic
iterative = imp.iterative
power_matrix = imp.power_matrix

algos = {'recursive_dynamic': recursive_dynamic,
         'iterative': iterative,
         'power_matrix': power_matrix}
