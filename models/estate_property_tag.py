from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag Model"

    name = fields.Char(required=True)
    property_ids = fields.Many2many('estate.properties', 'property_tag_ids')