from odoo import fields, models


class RealEstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property types Model"
    _order = "name desc"

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.properties', 'property_type_id')
    sequence = fields.Integer(string='Sequence', default=10,
                              help="Gives the sequence order when "
                              "displaying a list of property types.")
