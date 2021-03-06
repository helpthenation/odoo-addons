# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 Sistemas de Datos (<http://www.sdatos.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import fields, models, api


class res_users (models.Model):
    _inherit = "res.users"
    warehouse_id = fields.Many2one ('stock.warehouse', 'Warehouse')
    
    @api.model
    def context_get (self):  #Se incluye el almacen al contexto para facilitar los filtros en las vistas
        res = super (res_users, self).context_get ()
        if res.get ('uid') != None and self.browse (res.get ('uid')).warehouse_id:
            res['warehouse'] = self.browse (res.get ('uid')).warehouse_id.id
        else:
            res['warehouse'] = False
        return res