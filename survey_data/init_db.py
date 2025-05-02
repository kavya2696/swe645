#1. Kavya Shivakumar (G01520934)
#2. Sehaj Gill (G01535820)
#3. Jaanaki Swaroop P(G01502869)
#4. Koushik Vasa (G01480627)
from app import db, app
# to allow interaction with the Flask app
with app.app_context():
    db.drop_all()     # to drop old table
    db.create_all()
    print("Database tables created successfully.")
