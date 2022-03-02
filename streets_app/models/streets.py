from main import db

class Street(db.Model):
    __tablename__="streets"

    street_id=db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(80), unique=True, nullable=False)
    street_flooded = db.Column(db.Boolean, default=False, nullable=False)