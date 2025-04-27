from app import db, app

with app.app_context():
    db.drop_all()     # ← optional: drop old table if you're rebuilding
    db.create_all()
    print("✅ Database tables created successfully.")
