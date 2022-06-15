from odoo import fields, models
from dateutil.relativedelta import relativedelta


three_months = fields.Date.today() + relativedelta(months=+3)


class RealEstateProperties(models.Model):
    _name = "estate.properties"
    _description = "Real Estate Properties Model"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=three_months)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ])
    state = fields.Selection(
        string='State', required=True, copy=False,
        selection=[
            ('new', 'New'),
            ('offer recieved', 'Offer Recieved'),
            ('sold', 'Sold'),
            ('cancelled', 'Cancelled')
        ],
        default='new')
    property_type_id = fields.Many2one(
        'estate.property.type', string='Type')

    seller_id = fields.Many2one("res.users", string="Seller", default=lambda
                                self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    property_tag_ids = fields.Many2many('estate.property.tag', string='Tags')
