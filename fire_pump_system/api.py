# Path: fire_pump_system/fire_pump_system/api.py
import frappe

@frappe.whitelist()
def get_site_asset_records(site_asset_address, pump_name):
    site_assets = frappe.get_all('Site Asset', filters={'site_asset_address': site_asset_address, 'pump_name': pump_name}, fields=['*'])
    return site_assets
