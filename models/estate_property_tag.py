from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag Model"

    name = fields.Char(required=True)
    color = fields.Integer(string='color')
    property_ids = fields.Many2many('estate.properties','property_tag_id',
                                    string='Properties')
