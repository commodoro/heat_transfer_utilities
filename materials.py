"Método de elementos finitos."

from dataclasses import dataclass

@dataclass
class Material:
    "Material con sus propiedades."

    conductividad_termica: float
    densidad: float
    calor_especifico: float
    difusividad_terminca: float

    @property
    def k(self):
        return self.conductividad_termica
    
    @property
    def rho(self):
        return self.densidad
    
    @property
    def cp(self):
        return self.calor_especifico
    
    @property
    def alpha(self):
        return self.difusividad_terminca
    

MATERIALS = {
    "hierro": Material(71.8, 7897, 452, 2.01152E-05),
    "Ti6Al4V": Material(6.7, 4420, 560, 2.7069E-06),
    "aluminio": Material(220, 2707, 896, 9.07040E-05),
    "oro": Material(318, 18900, 130, 1.29426E-04),
    "cobre": Material(386, 8954, 380, 1.13445E-04)
}