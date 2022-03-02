from main import ma 
from models.streets import Street
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class StreetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Street
        load_instance=True
    
    street_id = auto_field(dump_only=True)
    street_name = auto_field(required=True, validate=Length(min=1))
    street_flooded = auto_field(required=True)

single_street_schema=StreetSchema()
multi_street_schema=StreetSchema(many=True)