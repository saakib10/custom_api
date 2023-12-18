# custom_api.py

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def get_item_data():
    # Fetch data from the ITEM doctype
    items = frappe.get_all('Item', fields=['name', 'item_code', 'description'])
    
    # You can customize the fields based on your requirements

    return items