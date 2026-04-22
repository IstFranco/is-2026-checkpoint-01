class TeamMember:
    def __init__(self, nombre, legajo, feature, servicio, estado):
        self.nombre = nombre
        self.legajo = legajo
        self.feature = feature
        self.servicio = servicio
        self.estado = estado

    def to_dict(self):
        """Convierte la entidad a diccionario para el JSON de la API"""
        return {
            "nombre": self.nombre,
            "legajo": self.legajo,
            "feature": self.feature,
            "servicio": self.servicio,
            "estado": self.estado
        }