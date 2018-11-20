# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResParterExt(models.Model):
    _inherit = 'res.partner'

    ref = fields.Char(string='Internal Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    corespondence_street = fields.Char()
    corespondence_street2 = fields.Char()
    corespondence_zip = fields.Char(change_default=True)
    corespondence_city = fields.Char()
    corespondence_state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    corespondence_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')

    cnic = fields.Char()
    cnic_address = fields.Char()
    cnic_expiry_date = fields.Date()
    cnic_front = fields.Binary(attachment=True)
    cnic_back = fields.Binary(attachment=True)

    is_member = fields.Boolean()
    is_kin = fields.Boolean()


    category_ids = fields.Many2one('members.category')
    partner_id = fields.Many2one('res.partner')
    next_of_kin = fields.One2many('res.partner','partner_id')

    @api.model
    def create(self, vals):
        if vals.get('ref', _('New')) == _('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code("res.partner") or _('New')

        rec = super(ResParterExt,self).create(vals)       

        return rec

class MemberCategory(models.Model):
    _name = 'members.category'

    name = fields.Char()

class ReferencePerson(models.Model):
    _name = 'reference.person'
    _rec_name = 'ref_id'

    ref_id = fields.Integer('Refernce ID')
    name = fields.Char()

class PlotInventory(models.Model):
    _name = 'plot.inventory'
    _rec_name = 'plot_number'

    society = fields.Many2one('society','Society', required = True)
    phase = fields.Many2one('society','Phase', required = True)
    sector=fields.Many2one('sector.number')
    location=fields.Many2one('location')

    plot_category=fields.Many2one('plot.category', 'Plot Catogory', required = True)
    plot_number=fields.Char('Plot number')
    sold=fields.Char('Sold')
    reserved=fields.Char('Reserved')
    motgage=fields.Char('Motgage')
    ref_name=fields.Many2one('reference.person','Ref. Name')
    total_area=fields.Char('Total Area')
    street=fields.Char('Street')
    plot_type=fields.Char('Plot Type')
    possession_status=fields.Char('Possession status')
    plot_size=fields.Char('Plot size')

class Location(models.Model):
    _name = 'location'

    name = fields.Text()

class PaymentPlan(models.Model):
    _name = 'payment.plan'
    payment_type = fields.Char('Payment Type')
    plan_id=fields.Char('Plan ID')
    plan_description=fields.Char('Plan Description')
    mode=fields.Char('Mode ')
    total_installment=fields.Char('Total Isntallment ')

    file_id = fields.Many2one('member.file.detail')

class TransactionType(models.Model):
    _name = 'transaction.type'
    transaction_id=fields.Char('Transaction ID')
    name=fields.Char('Name')
    income_gl_code=fields.Char('Income GL_Code')
    accrual_gl_code=fields.Char('Accrual GL_Code')
    fine_detail=fields.Char('Fine Detail')
    tax_detail=fields.Char('Tax detail')
    configuration_detail=fields.Char('Configuration Detail')

class RateList(models.Model):
    _name = 'rate.list'
    transaction_id =fields.Many2one('transaction.type','Transaction ID')
    starting_date=fields.Date('Start Date')
    configuration=fields.Char('Configuration')
    serial_number=fields.Char('Serial #')
    category_code=fields.Char('Category Code')
    plot_category=fields.Char('Plot Category')
    unit_tupe=fields.Char('Unit Type')
    amount=fields.Float('Amount')

class CustomizedLetter(models.Model):
    _name = 'customized.letter'

    code=fields.Char('Code')
    letter_type=fields.Char('Letter Type')
    subject=fields.Char('Subject')
    letter_body=fields.Char('Letter Body')
    footer=fields.Char('Footer')
    electronic_signature=fields.Char('Electronic Signature')
