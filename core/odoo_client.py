from core.config import settings

from odoorpc import ODOO

odoo = ODOO(settings.ODOO_URL, protocol="jsonrpc+ssl", port=settings.ODOO_PORT)


def init_odoo_client():
    odoo.login(settings.DB_NAME, settings.USER_NAME, settings.API_KEY)
