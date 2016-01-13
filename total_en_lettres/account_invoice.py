# -*- coding: utf-8 -*-
################################################################################
#                                                                              
#                        Module [Total en lettres]                         
#                    ----------------------------------                        
#                      permet d'ajouter une convertion                         
#                        du total en lettres (Devis et Facture)                           
#                    ----------------------------------                        
#                                                                              
#                       langage : Python 2.7                                   
#                       date creation : 01/01/2016                            
#                       date modification : 04/01/2016                         
#                       version : 0.1                                          
#                       auteur  : MLMConseil                              
#                                                                              
################################################################################

from openerp import models, fields, api
import conversion


class account_invoice(models.Model):
    _name = "account.invoice"
    _inherit = 'account.invoice'
    _description = "le modele ajoute le total d'une facture en lettres"



    @api.one
    @api.depends('invoice_line.price_subtotal', 'tax_line.amount')
    def _compute_amount(self):
        self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line)
        self.amount_tax = sum(line.amount for line in self.tax_line)
        self.amount_total = self.amount_untaxed + self.amount_tax
        # conversion
        self.amount_total_text = conversion.convertir_fac(self.amount_total)


    amount_total_text = fields.Text(string='total en lettre',store=True, readonly=True, compute='_compute_amount', help="Total en lettres")

