from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from src.extensions import db
from src.models import User, Role

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.json or {}
    user = User(email=data.get("email"), full_name=data.get("full_name"),
                password_hash=generate_password_hash(data.get("password")))
    db.session.add(user); db.session.commit()
    return jsonify({"id": user.id})

@auth_bp.post("/login")
def login():
    data = request.json or {}
    user = User.query.filter_by(email=data.get("email")).first()
    if not user or not check_password_hash(user.password_hash, data.get("password","")):
        return jsonify({"error": "invalid credentials"}), 401
    login_user(user)
    return jsonify({"message": "ok"})

@auth_bp.post("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"message": "ok"})
