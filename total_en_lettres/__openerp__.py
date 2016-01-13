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
#                       date creation : /01/2016                            
#                       date modification : /01/2016                         
#                       version : 0.1                                          
#                       auteur  : MLMConseil                              
#                                                                              
################################################################################
{
    'name': "Total en lettres",

    'summary': """
        Conversion du Total en lettres (Devis et Facture)""",

    'description': """
        Conversion du Total en lettres (Devis et Facture)...
    """,

    'author': "MLMConseil",
    'website': "http://www.mlmconseil.dz",
    'sequence': 5,

    'category': 'Sale',
    'version': '0.1',

    'depends': ['base','account','sale'],

    
    'data': [
        'account_invoice_view.xml',
        'devis_en_lettres.xml',
        'views/report_invoice.xml',
        'views/report_saleorder.xml'
		
    ],

    'installable': True,
    'auto_install': False,
}