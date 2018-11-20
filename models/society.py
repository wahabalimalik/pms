# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Society(models.Model):
    _name = 'society'

    name = fields.Char('Society Name')
    society_map = fields.Many2one('society.map')
    country = fields.Many2one('society.map')
    city = fields.Many2one('society.map')
    area = fields.Many2one('society.map')
    phase_line = fields.One2many('society','society_id')
    society_id = fields.Many2one('society')
    land_owner = fields.Many2many('res.partner')
    project_owner = fields.Many2many('res.partner')
    project_manager = fields.Many2one('res.partner')
    total_land = fields.Float()
    total_land_for_sale = fields.Float()
    total_land_sold = fields.Float()
    total_land_avilable = fields.Float()
    user_id = fields.Many2many('res.user')

class SocietyMap(models.Model):
    _name = 'society.map'
    name = fields.Char()