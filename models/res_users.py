from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many('estate.properties', 'seller_id',
                                   domain=[('state', 'in',
                                            ['new', 'offer_recieved'])])
    propety_count = fields.Integer(string='Properties')

    @api.depends('property_ids')
    def _compute_property_count(self):
        for record in self:
            record.property_count = len(record.property_ids)
