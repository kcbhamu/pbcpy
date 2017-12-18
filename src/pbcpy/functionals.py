from .grid_functions import Grid_Function_Base, Grid_Function, Grid_Function_Reciprocal, Grid_Space
import numpy as np

class Functional(object):
    '''
    Object representing a DFT functional
    
    Attributes
    ----------
    name: string
        The (optional) name of the functional

    energydensity: Grid_Function
        The energy density 

    potential: Grid_Function
        The first functional derivative of the functional wrt 
        the electron density 
        
    kernel: Grid_Function_Reciprocal
        The value of the reciprocal space kernel. This will
        be populated only if the functional is nonlocal
    '''


    def __init__(self, energydensity=None, potential=None, kernel=None):
        if energydensity is not None:
            if isinstance(energydensity, Grid_Function):
                self.energydensity = energydensity
        if potential is not None:
            if isinstance(potential, Grid_Function):
                self.potential = potential
        if kernel is not None:
            if isinstance(kernel, (np.ndarray)):
                self.kernel = kernel


    def sum(self,other):
        energydensity = self.energydensity.sum(other.energydensity)
        potential = self.potential.sum(other.potential)
        return Functional(energydensity=energydensity,potential=potential)
