# Part of Hibou Suite Professional. See LICENSE_PROFESSIONAL file for full copyright and licensing details.

def migrate(cr, version):
    # pre_init_hook script only runs on install,
    # if you're coming from 12.0 we need the same change
    from odoo.addons.hr_payroll_timesheet import ts_payroll_pre_init_hook
    ts_payroll_pre_init_hook(cr)
