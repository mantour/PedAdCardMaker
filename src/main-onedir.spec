# -*- mode: python -*-
mytree = Tree('C:\Python27_32bit\Lib\site-packages\lpod',prefix='lpod')
#template = Tree('C:\\Users\\sam\\Documents\\project\\AdCardMaker\\src\\templates',prefix='templates')
a = Analysis(['main.py'],
             pathex=['C:\\Users\\sam\\Documents\\project\\AdCardMaker\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               mytree,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='main')
