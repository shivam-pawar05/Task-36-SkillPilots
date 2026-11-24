# E-Commerce Inventory Management System + Oracle RMAN Lab

This starter project includes a PostgreSQL database, Python Flask API, Power BI dashboard guide, GitHub Actions CI workflow, and a separate Oracle RMAN backup/restore practical.

## Structure
- `database/`: schema, PL/pgSQL functions, audit trigger, sample data
- `backend/`: Flask API and PostgreSQL connection
- `powerbi/`: dashboard instructions and DAX measures
- `.github/workflows/`: CI workflow
- `oracle_rman/`: RMAN full backup, restore/recovery template, sample data and validation

## PostgreSQL + Flask setup
1. Create a PostgreSQL database named `ecommerce_db`.
2. Execute in order: `database/schema.sql`, `database/functions.sql`, `database/triggers.sql`, `database/sample_data.sql`.
3. Copy `.env.example` to `backend/.env` and set your PostgreSQL password.
4. Run:
   ```bash
   cd backend
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   python app.py
   ```
5. Open `http://127.0.0.1:5000/`.

### API endpoints
- `GET /` — status
- `GET /products` — list products
- `POST /products` — add a product
- `GET /inventory` — view stock
- `POST /orders` — create a one-item demo order and deduct stock

Example product JSON: `{"product_name":"Keyboard","category_id":1,"supplier_id":1,"price":800}`

## Power BI
Follow `powerbi/dashboard_guide.md`. A `.pbix` file is not included; create and save the report in Power BI Desktop.

## CI/CD
`.github/workflows/ci.yml` installs dependencies, compiles Python, starts PostgreSQL, applies SQL files and checks sample data.

## Oracle RMAN practical
The `oracle_rman/` folder matches the latest practical: create sample data, perform a full RMAN backup, verify backup pieces, restore/recover a disposable test database and validate rows.

**Warning:** RMAN restore/recovery can replace database files and change the database incarnation. Use only an isolated, disposable Oracle test instance. Confirm DBID, Oracle version, paths, control-file/SPFILE handling and recovery procedure with your instructor/DBA. RMAN is for Oracle, not PostgreSQL. Scripts are templates and require environment-specific adjustment.
