# your_project.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['new_window.py'],
             pathex=['.'],
             binaries=[],
             datas=[
                 ('data', 'data'),
                 ('icons', 'icons'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          [],
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          bootloader_ignore_pycs=False,
          runtime_tmpdir=None,
          console=False,
          upx=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='icon.ico')

