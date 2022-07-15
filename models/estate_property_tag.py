from odoo import fields, models


# create a new model estate.property.tag
class EstatePropertyTag(models.Model):
    # ---------------------------------------- Private Attributes -------------
    # database table name
    _name = "estate.property.tag"
    # description of the model
    _description = "Real Estate Property Tag Model"
    # order of viewing the records
    _Order = "name desc"

# --------------------------------------- Fields Declaration --------------
    # fields of the model
    name = fields.Char(required=True)
    color = fields.Integer(string='color')
    # manytoone relationship with estate.properties
    property_ids = fields.Many2many('estate.properties', 'property_tag_ids',
                                    string='Properties')
