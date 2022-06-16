from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    estate_property_ids = fields.One2many('estate.properties', 'seller_id',)
