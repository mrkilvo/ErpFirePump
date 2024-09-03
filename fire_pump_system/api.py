# Path: fire_pump_system/fire_pump_system/api.py
import frappe

@frappe.whitelist()
def get_site_asset_records(site_asset_address, pump_name):
    site_assets = frappe.get_all('Site Asset', filters={'site_asset_address': site_asset_address, 'pump_name': pump_name}, fields=['*'])
    return site_assets
@frappe.whitelist()
def get_site_assets(custom_site_address):
    # Fetch all Site Assets matching the given address, including the is_large_motor field
    site_assets = frappe.get_all(
        'Site Asset',
        filters={'site_asset_address': custom_site_address},
        fields=[
            'name', 'driver_type', 'is_large_motor',
            'fuel_filter_1', 'fuel_filter_2', 'fuel_filter_3', 'fuel_filter_4',
            'oil_filter_1', 'oil_filter_2', 'coolant_filter'
        ]
    )
    return site_assets
