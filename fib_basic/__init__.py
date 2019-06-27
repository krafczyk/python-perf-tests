from . import imp

__all__ = [ "recursive_dynamic", "iterative", "power_matrix", "algos"]

algos = {'recursive_dynamic': imp.recursive_dynamic,
         'iterative': imp.iterative,
         'power_matrix': imp.power_matrix}
