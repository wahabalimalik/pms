# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LandRegistory(models.Model):
    _name = 'land.registory'

    registery_number = fields.Char('Registery Number')
    purchasing_date = fields.Date('Date of Purchase')
    khevat = fields.Many2one('Khevat')
    khasra = fields.Many2one('Khasra')
    khatoni = fields.Many2one('Khatoni')
    kanal= fields.Float('Kanal')
    marla = fields.Float('Marla')
    square_foot= fields.Many2one('Square Foot')
    purchase_price= fields.Many2one('Purchase Price ')
