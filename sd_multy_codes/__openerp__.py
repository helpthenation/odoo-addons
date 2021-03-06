# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Sistemas de Datos (<http://www.sdatos.com>).
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

{
    'name' : 'SDatos Multy Codes',
    'version' : '2.0',
    'author' : 'Sistemas de Datos',
    'maintainer': 'Sistemas de Datos',
    'category' : 'Product',
    'sequence': 3,                
    'summary': 'Save many codes',
    'description' : """
Save Multy Codes
================

This module allows save many codes in product template.
    """,
    'website': 'http://www.sdatos.com',
    # End General Data
    'depends' : ['product',
                 'sale'],            
    'data': ['views/sd_product_inherit.xml',
             'security/ir.model.access.csv',
             'security/sd_multy_codes_security.xml'],                
    'installable': True,        
    'auto_install': False,        
    'application': False,
}