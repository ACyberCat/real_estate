from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer Model"

    price = fields.Float(required=True)
    partner_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    status = fields.Selection(
        string='Status', copy=False,
        selection=[
            ('refused', 'Refused'),
            ('accepted', 'Accepted')])
    property_id = fields.Many2one('estate.properties', string='Property')
    property_type_id = fields.Many2one('estate.property.type',
                                       related="property_id.property_type_id",
                                       string='Property Type')
