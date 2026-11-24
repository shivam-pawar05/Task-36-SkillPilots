from flask import Flask, jsonify, request
from psycopg2 import Error
from db import get_connection

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"message": "E-Commerce Inventory API", "status": "running"})

@app.get("/products")
def list_products():
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""SELECT p.product_id,p.product_name,p.price,c.category_name,s.supplier_name FROM products p LEFT JOIN categories c USING(category_id) LEFT JOIN suppliers s USING(supplier_id) ORDER BY p.product_id""")
            return jsonify(cur.fetchall())
    except Error as exc:
        return jsonify({"error": str(exc)}), 500

@app.post("/products")
def add_product():
    data = request.get_json(silent=True) or {}
    required = ("product_name", "price", "category_id", "supplier_id")
    missing = [key for key in required if key not in data]
    if missing:
        return jsonify({"error": "Missing fields", "fields": missing}), 400
    try:
        price = float(data["price"])
        if price < 0: raise ValueError
    except (TypeError, ValueError):
        return jsonify({"error": "price must be a non-negative number"}), 400
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("INSERT INTO products(product_name,category_id,supplier_id,price) VALUES(%s,%s,%s,%s) RETURNING product_id,product_name,price", (data["product_name"],data["category_id"],data["supplier_id"],price))
            return jsonify(cur.fetchone()), 201
    except Error as exc:
        return jsonify({"error": str(exc)}), 400

@app.get("/inventory")
def list_inventory():
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("""SELECT p.product_name,w.warehouse_name,i.quantity,i.reorder_level,(i.quantity<=i.reorder_level) AS low_stock FROM inventory i JOIN products p USING(product_id) JOIN warehouses w USING(warehouse_id) ORDER BY p.product_name""")
            return jsonify(cur.fetchall())
    except Error as exc:
        return jsonify({"error": str(exc)}), 500

@app.post("/orders")
def place_order():
    data = request.get_json(silent=True) or {}
    if not all(k in data for k in ("customer_id","warehouse_id","items")) or not isinstance(data["items"],list) or len(data["items"]) != 1:
        return jsonify({"error": "Provide customer_id, warehouse_id and exactly one item"}), 400
    item = data["items"][0]
    if not all(k in item for k in ("product_id","quantity")):
        return jsonify({"error": "Item requires product_id and quantity"}), 400
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT create_order(%s,%s,%s,%s) AS order_id", (data["customer_id"],data["warehouse_id"],item["product_id"],item["quantity"]))
            return jsonify({"order_id": cur.fetchone()["order_id"], "status": "created"}), 201
    except (Error, TypeError, ValueError) as exc:
        return jsonify({"error": str(exc)}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
