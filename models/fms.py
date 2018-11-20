# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MembersFileDetail(models.Model):
    _name = 'member.file.detail'

    file_number = fields.Char('File Number', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    society = fields.Many2one('society','Society', required = True)
    phase = fields.Many2one('society','Phase', required = True)
    booking_date = fields.Date('Booking Date', required = True)
    payment_type = fields.Selection([
    	('installments', 'Installment'), 
    	('down_payment', 'Down Payment')], 
    	string='Payment Type', required = True)
    unit_type = fields.Selection([
    	('plot', 'Plot'), 
    	('commercial_plot', 'Commercial Plot'),
    	('appartment', 'Appartment'),
    	('model_house', 'Model House'),
    	('shop', 'Shop')
    	], 
    	string='Unit Type', required = True)
    completion_year=fields.Char('Completion Year', required = True)
    current_status = fields.Selection([
    	('plot', 'Plot'), 
    	('possession', 'Possession'),
    	('house_completed', 'House Completed'),
    	('resident', 'Resident')
    	], 
    	string='Current Status', required = True)

    sector=fields.Many2one('sector.number', required = True)
    plot_category=fields.Many2one('plot.category', 'Plot Catogory', required = True)
    plot_number=fields.Many2one('plot.inventory','Plot No.', required = True)
    coverd_area=fields.Float('Covered Area', required = True)
    construction_strat_date=fields.Date('Construction Start Date', required = True)
    completion_date=fields.Date('Completion Date', required = True)

    membership_number=fields.Char('Membership Number')
    partner_id = fields.Many2one('res.partner')
    ref_person = fields.Char()

    plan_id = fields.One2many('payment.plan', 'file_id')
    payment_id = fields.One2many('payment.detail', 'file_id')
    cancellation_id = fields.One2many('cancellation.detail', 'file_id')
    history_id = fields.One2many('file.history', 'file_id')

    @api.model
    def create(self, vals):
        if vals.get('file_number', _('New')) == _('New'):
            vals['file_number'] = self.env['ir.sequence'].next_by_code("member.file.detail") or _('New')

        rec = super(MembersFileDetail,self).create(vals)       

        return rec


class PaymentDetail(models.Model):
    _name = 'payment.detail'

    plan_id=fields.Char('Plan ID')
    plan_duration=fields.Char('Plan Duration ')
    payment_mode=fields.Char('Payment Mode')
    no_of_installment=fields.Char('No. of Installment')
    sale_amount=fields.Char('Sale Amount ')
    discount=fields.Char('Discount ')
    net_sale_amount=fields.Char('Net Sale Amount ')
    downpayment_date=fields.Date('Downpayment Date')
    balance=fields.Float('Balance')

    file_id = fields.Many2one('member.file.detail')

class CancellationDetail(models.Model):
    _name = 'cancellation.detail'
    cancel =fields.Char()
    convert = fields.Char()
    date = fields.Date()
    remarks = fields.Text()

    file_id = fields.Many2one('member.file.detail')

class FileHistory(models.Model):
    _name = 'file.history'

    tr_id = fields.Char()
    membership = fields.Char()
    name = fields.Char()
    transaction_date = fields.Date()
    check_mark = fields.Char()

    file_id = fields.Many2one('member.file.detail')

class PhaseNumber(models.Model):
    _name = 'phase.number'

    name = fields.Char()

class SectorNumber(models.Model):
    _name = 'sector.number'

    name = fields.Char()
    phase = fields.Many2one('society')
    society = fields.Many2one('society')

class PlotCategory(models.Model):
    _name = 'plot.category'

    name = fields.Char()
    number = fields.Integer()