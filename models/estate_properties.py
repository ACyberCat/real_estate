from odoo import exceptions, api, fields, models
from dateutil.relativedelta import relativedelta


three_months = fields.Date.today() + relativedelta(months=+3)


class RealEstateProperties(models.Model):
    _name = "estate.properties"
    _description = "Real Estate Properties Model"
    _order = "id desc"
    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         'The name of the property must be unique!'),
        ('selling_price_positive', 'CHECK(selling_price < 0)',
         'The selling price must be positive!'),
        ('expected_price_positive', 'CHECK(expected_price < 0)',
         'The expected price must be positive!'),
        ('area_positive', 'CHECK(area < 0)', 'The area must be positive!'),
    ]

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
    total_area = fields.Integer(compute="_compute_total_area")
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
    best_offer = fields.Float(string="Best Offer", default=0,
                              compute="_compute_best_offer")
    seller_id = fields.Many2one("res.users", string="Seller", default=lambda
                                self: self.env.user)
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    property_tag_ids = fields.Many2many('estate.property.tag')
    property_offer_ids = fields.One2many('estate.property.offer',
                                         'property_id', string="Offers")

    @api.onchange('property_offer_ids')
    def _onchange_property_offer_ids(self):
        if self.state == 'new' and len(self.property_offer_ids) > 0:
            self.state = 'offer recieved'

    @api.depends("garden_area", "living_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    @api.depends("property_offer_ids")
    def _compute_best_offer(self):
        for record in self:
            if record.property_offer_ids:
                record.best_offer = max(record.property_offer_ids.mapped(
                    "price"))
            else:
                record.best_offer = 0

    def action_cancel(self):
        if self.state != "sold":
            self.state = 'cancelled'
        else:
            raise exceptions.UserError(
                "Cannot cancel a sold property")
        return True

    def action_sell(self):
        for record in self:
            if record.state == 'cancelled':
                raise exceptions.UserError(
                    "Cannot sell a cancelled property")
            else:
                record.state = 'sold'
                record.buyer_id = self.env.user.partner_id
        return True

    @api.constrains('selling_price', 'expected_price')
    def _check_price(self):
        if (self.selling_price < (self.expected_price*0.9)
                and self.selling_price > 0):
            raise exceptions.ValidationError(
                "Selling price must be greater than 90% of expected price")
