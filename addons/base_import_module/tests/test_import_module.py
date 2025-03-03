# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import json
from io import BytesIO
from zipfile import ZipFile

import odoo.tests
from odoo.tests import new_test_user

@odoo.tests.tagged('post_install', '-at_install')
class TestImportModule(odoo.tests.TransactionCase):

    def test_import_and_uninstall_module(self):
        bundle = 'web.assets_backend'
        path = '/test_module/static/src/js/note.js'
        manifest_content = json.dumps({
            'name': 'Test Module',
            'description': 'Test',
            'assets': {
                'web.assets_backend': [
                    'test_module/static/src/js/note.js'
                ]
            },
            'license': 'LGPL-3',
        })

        stream = BytesIO()
        with ZipFile(stream, 'w') as archive:
            archive.writestr('test_module/__manifest__.py', manifest_content)
            archive.writestr('test_module/static/src/js/note.js', "console.log('AAA');")

        # Import test module
        self.env['ir.module.module'].import_zipfile(stream)

        attachment = self.env['ir.attachment'].search([('url', '=', path)])
        self.assertEqual(attachment.name, 'note.js')
        self.assertEqual(attachment.type, 'binary')
        self.assertEqual(attachment.raw, b"console.log('AAA');")

        asset = self.env['ir.asset'].search([('name', '=', f'test_module.{bundle}.{path}')])
        self.assertEqual(asset.path, path)
        self.assertEqual(asset.bundle, bundle)
        self.assertEqual(asset.directive, 'append')
        self.assertEqual(asset.target, False)

        asset_data = self.env['ir.model.data'].search([('model', '=', 'ir.asset'), ('res_id', '=', asset.id)])
        self.assertEqual(asset_data.module, 'test_module')
        self.assertEqual(asset_data.name, f'{bundle}_{path}'.replace(".", "_"))

        # Uninstall test module
        self.env['ir.module.module'].search([('name', '=', 'test_module')]).module_uninstall()

        attachment = self.env['ir.attachment'].search([('url', '=', path)])
        self.assertEqual(len(attachment), 0)

        asset = self.env['ir.asset'].search([('name', '=', f'test_module.{bundle}.{path}')])
        self.assertEqual(len(asset), 0)

        asset_data = self.env['ir.model.data'].search([('model', '=', 'ir.asset'), ('res_id', '=', asset.id)])
        self.assertEqual(len(asset_data), 0)

    def test_import_and_update_module(self):
        self.test_user = new_test_user(
            self.env, login='Admin',
            groups='base.group_user,base.group_system',
            name='Admin',
        )
        bundle = 'web.assets_backend'
        path = 'test_module/static/src/js/note.js'
        manifest_content = json.dumps({
            'name': 'Test Module',
            'description': 'Test',
            'assets': {
                bundle: [
                    path
                ]
            },
            'license': 'LGPL-3',
        })
        stream = BytesIO()
        with ZipFile(stream, 'w') as archive:
            archive.writestr('test_module/__manifest__.py', manifest_content)
            archive.writestr(path, "console.log('AAA');")

        # Import test module
        self.env['ir.module.module'].with_user(self.test_user).import_zipfile(stream)

        attachment = self.env['ir.attachment'].search([('url', '=', f'/{path}')])
        self.assertEqual(attachment.name, 'note.js')
        self.assertEqual(attachment.type, 'binary')
        self.assertEqual(attachment.raw, b"console.log('AAA');")

        asset = self.env['ir.asset'].search([('name', '=', f'test_module.{bundle}./{path}')])
        self.assertEqual(asset.path, f'/{path}')
        self.assertEqual(asset.bundle, bundle)
        self.assertEqual(asset.directive, 'append')
        self.assertEqual(asset.target, False)

        asset_data = self.env['ir.model.data'].search([('model', '=', 'ir.asset'), ('res_id', '=', asset.id)])
        self.assertEqual(asset_data.module, 'test_module')
        self.assertEqual(asset_data.name, f'{bundle}_/{path}'.replace(".", "_"))

        # Update test module
        stream = BytesIO()
        with ZipFile(stream, 'w') as archive:
            archive.writestr('test_module/__manifest__.py', manifest_content)
            archive.writestr(path, "console.log('BBB');")

        # Import test module
        self.env['ir.module.module'].with_user(self.test_user).import_zipfile(stream)

        attachment = self.env['ir.attachment'].search([('url', '=', f'/{path}')])
        self.assertEqual(attachment.name, 'note.js')
        self.assertEqual(attachment.type, 'binary')
        self.assertEqual(attachment.raw, b"console.log('BBB');")

        asset = self.env['ir.asset'].search([('name', '=', f'test_module.{bundle}./{path}')])
        self.assertEqual(asset.path, f'/{path}')
        self.assertEqual(asset.bundle, bundle)
        self.assertEqual(asset.directive, 'append')
        self.assertEqual(asset.target, False)

        asset_data = self.env['ir.model.data'].search([('model', '=', 'ir.asset'), ('res_id', '=', asset.id)])
        self.assertEqual(asset_data.module, 'test_module')
        self.assertEqual(asset_data.name, f'{bundle}_/{path}'.replace(".", "_"))
