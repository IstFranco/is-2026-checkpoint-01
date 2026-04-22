import psycopg2
from psycopg2.extras import RealDictCursor
from config import Config

class PostgresRepository:
    def __init__(self):
        self.connection_url = Config.DATABASE_URL

    def get_all_members(self):
        """Lee los integrantes de la tabla members de PostgreSQL"""
        conn = None
        try:
            conn = psycopg2.connect(self.connection_url)
            cur = conn.cursor(cursor_factory=RealDictCursor)
            
            cur.execute("SELECT nombre, legajo, feature, servicio, estado FROM members;")
            members = cur.fetchall()
            
            cur.close()
            return members
        except Exception as e:
            print(f"Error conectando a la DB: {e}")
            return []
        finally:
            if conn:
                conn.close()