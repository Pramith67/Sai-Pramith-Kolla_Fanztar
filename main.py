from flask import Flask, request, jsonify

app = Flask(__name__)

MOBILE_COMPONENTS = {
    "A": ("LED Screen", 10.28),
    "B": ("OLED Screen", 24.07),
    "C": ("AMOLED Screen", 33.30),
    "D": ("Wide-Angle Camera", 25.94),
    "E": ("Ultra-Wide-Angle Camera", 32.39),
    "F": ("USB-C Port", 18.77),
    "G": ("Micro-USB Port", 15.13),
    "H": ("Lightning Port", 20.00),
    "I": ("Android OS", 42.31),
    "J": ("iOS OS", 45.00),
    "K": ("Metallic Body", 45.00),
    "L": ("Plastic Body", 30.00)
}


def calculate(components):
    selected_parts = []
    total_price = 0

    for item in components:
        if item in MOBILE_COMPONENTS:
            part, price = MOBILE_COMPONENTS[item]
            selected_parts.append(part)
            total_price += price
        else:
            return None

    return total_price, selected_parts


@app.route("/order", methods=["POST"])
def create_order():
    try:
        data = request.get_json()
        components = data.get("components", [])

        result = calculate(components)
        if result is None:
            return jsonify({"error": "Invalid component code"}), 400

        total_price, selected_parts = result

        order_id = "some-id"
        response_data = {
            "order_id": order_id,
            "total": total_price,
            "parts": selected_parts,
        }

        return jsonify(response_data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/")
def home():
    return "Mobile Phone order system"


if __name__ == "__main__":
    app.run(debug=True)
