from flask import Blueprint, jsonify
from src.application.team_service import TeamService

api_bp = Blueprint('api', __name__)
team_service = TeamService()

@api_bp.route('/team', methods=['GET'])
def get_team():
    """Endpoint principal que consume el frontend"""
    members = team_service.get_all_members()
    return jsonify([member.to_dict() for member in members])

@api_bp.route('/health', methods=['GET'])
def health():
    """Criterio bloqueante: Endpoint para el HEALTHCHECK de Docker"""
    return jsonify({"status": "healthy"}), 200

@api_bp.route('/info', methods=['GET'])
def info():
    """Endpoint de metadata del servicio"""
    return jsonify({
        "service": "TeamBoard Backend API",
        "version": "1.0.0",
        "description": "API REST para el Checkpoint 01 de Ingeniería de Software"
    })