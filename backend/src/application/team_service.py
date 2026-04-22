from src.infrastructure.database.postgres_repository import PostgresRepository
from src.domain.team_member import TeamMember

class TeamService:
    def __init__(self):
        self.repository = PostgresRepository()

    def get_all_members(self):
        raw_data = self.repository.get_all_members()
        
        return [
            TeamMember(
                nombre=data['nombre'],
                legajo=data['legajo'],
                feature=data['feature'],
                servicio=data['servicio'],
                estado=data['estado']
            ) for data in raw_data
        ]