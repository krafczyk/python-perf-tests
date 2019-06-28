from . import imp

__all__ = [ "recursive_dynamic", "iterative", "power_matrix", "iterative_asm", "recursive_dynamic_O3", "iterative_O3", "power_matrix_O3", "algos"]

recursive_dynamic = imp.recursive_dynamic
iterative = imp.iterative
iterative_asm = imp.iterative_asm
power_matrix = imp.power_matrix

recursive_dynamic_O3 = imp.recursive_dynamic_O3
iterative_O3 = imp.iterative_O3
power_matrix_O3 = imp.power_matrix_O3

algos = {'recursive_dynamic': recursive_dynamic,
         'iterative': iterative,
         'iterative_asm': iterative_asm,
         'power_matrix': power_matrix,
         'recursive_dynamic_O3': recursive_dynamic_O3,
         'iterative_O3': iterative_O3,
         'power_matrix_O3': power_matrix_O3}
