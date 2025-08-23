from flask import Blueprint, request, jsonify
from services.valuation_service import estimate_diamond_price

valuation_bp = Blueprint("valuation", __name__)

@valuation_bp.route("/estimate", methods=["POST"])
def estimate():
    data = request.get_json()
    carat = data.get("carat", 1.0)
    color = data.get("color", "G")
    clarity = data.get("clarity", "VS1")

    price = estimate_diamond_price(carat, color, clarity)
    return jsonify({"estimated_price": price})
