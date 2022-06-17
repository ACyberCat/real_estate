from odoo import exceptions, api, fields, models
from dateutil.relativedelta import relativedelta


# create a new model estate.property.offer
class EstatePropertyOffer(models.Model):
    # database table name
    _name = "estate.property.offer"
    # description of the model
    _description = "Real Estate Property Offer Model"
    # order of viewing the records
    _order = "price desc"
    # database constraints
    _sql_constraints = [
        ('name_uniq', 'unique(name)',
         'The name of the property must be unique!'),
        ('price_positive', 'CHECK(price >= 0)',
         'The offer price must be positive!'),
    ]

    # fields of the model
    price = fields.Float(required=True)
    # manytoone relationship with res.partner
    partner_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    # related field to partner_id.name
    partner_name = fields.Char(related="partner_id.name", string="Buyer")
    status = fields.Selection(
        string='Status', copy=False,
        selection=[
            ('refused', 'Refused'),
            ('accepted', 'Accepted')])
    # manytoone relationship with estate.properties
    property_id = fields.Many2one('estate.properties', string='Property')
    # manytoone relationship with estate.property.type
    property_type_id = fields.Many2one('estate.property.type',
                                       related="property_id.property_type_id",
                                       string='Property Type')
    validity = fields.Integer(string='Validity', default=7)
    date_deadline = fields.Date(string='Deadline', compute="_compute_deadline",
                                inverse="_inverse_deadline")

    # accepting an offer and checking if the property is available
    # if it is, the property is sold to the buyer
    def action_accept(self):
        for record in self:
            if (record.property_id.state != 'cancelled'
                    and record.property_id.state != 'sold'):
                record.status = 'accepted'
                record.action_sell()
                record.property_id.buyer_id = record.partner_id
                record.property_id.selling_price = record.price
            else:
                raise exceptions.ValidationError(
                    "This property is cancelled or sold. "
                    "You can't accept an offer "
                    "for a cancelled or a sold property.")
        return True

    # rejecting an offer and checking if the property is available
    def action_refuse(self):
        for record in self:
            if (record.property_id.state != 'cancelled'
                    and record.property_id.state != 'sold'):
                record.status = 'refused'
                record.property_id.state = 'offer recieved'
                record.property_id.buyer_id = False
                record.property_id.selling_price = 0
            else:
                raise exceptions.ValidationError(
                    "This property is cancelled or sold. "
                    "You can't refuse an offer "
                    "for a cancelled or a sold property.")
        return True

    @api.depends("validity", "date_deadline")
    # computing the deadline of the offer
    def _compute_deadline(self):
        for record in self:
            if record.validity:
                if record.validity > 0:
                    record.date_deadline = fields.Date.today() + \
                        relativedelta(days=+record.validity)
                else:
                    record.status = 'refused'
                    record.validity = 0
                    break

    # inverse of the deadline of the offer
    def _inverse_deadline(self):
        for record in self:
            if record.validity:
                if record.validity > 0:
                    record.date_deadline = fields.Date.today() + \
                        relativedelta(days=+record.validity)
                else:
                    record.status = 'refused'
                    record.validity = 0
                    break
