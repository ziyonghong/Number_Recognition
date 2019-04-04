# -*- mode: python -*-

block_cipher = None


a = Analysis(['scanner_main.py'],
             pathex=['number_recogonize.py', 'qr_code_scanner.py', 'C:\\Users\\xjn\\PycharmProjects\\new_tf_poj'],
             binaries=[],
             datas=[],
             hiddenimports=['number_recogonize', 'qr_code_scanner'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='scanner_main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='scanner_main')
