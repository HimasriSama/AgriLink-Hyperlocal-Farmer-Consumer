from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary storage for orders
orders = []

@app.route("/", methods=["GET", "POST"])
def index():
    current_demand = 0
    predicted_demand = 0

    if request.method == "POST":
        crop = request.form.get("crop")
        quantity = request.form.get("quantity")

        if crop and quantity:
            quantity = int(quantity)
            orders.append(quantity)

    current_demand = sum(orders)
    predicted_demand = int(current_demand * 1.1)  # simple AI logic

    return render_template(
        "index.html",
        current_demand=current_demand,
        predicted_demand=predicted_demand
    )

if __name__ == "__main__":
    app.run()

