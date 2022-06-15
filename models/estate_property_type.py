from odoo import fields, models


class RealEstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property types Model"

    name = fields.Char(required=True)
