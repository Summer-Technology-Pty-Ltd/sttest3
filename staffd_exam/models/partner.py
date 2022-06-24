from odoo import models, fields, api, exceptions


class Partner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Float(required=True)

    over_credit = fields.Boolean(compute='get_over_credit')

    action = fields.Selection(string='Action when credit limit is exceeded', selection=[
        ('do_nothing', "Do Nothing"),
        ('warn', "Warn"),
        ('put_on_hold', "Put On Hold")
    ], required=True)

    def get_over_credit(self):
        self.over_credit = False
        for partner in self:
            if partner.credit_limit > partner.credit:
                partner.over_credit = True



