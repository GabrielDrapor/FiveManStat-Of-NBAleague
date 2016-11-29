# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\five-man.py'],
             pathex=['C:\\Users\\snc\\Desktop\\PyInstaller\\five-man'],
             binaries=None,
             datas=None,
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='five-man',
          debug=False,
          strip=False,
          upx=True,
          console=True )
