# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['run_DyberPet.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('res/icons', 'res/icons'),
        ('res/items', 'res/items'),
        ('res/language', 'res/language'),
        ('res/pet', 'res/pet'),
        ('res/role', 'res/role'),
        ('res/sounds', 'res/sounds')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='小O',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['xiaoo.icns'],
)
app = BUNDLE(
    exe,
    name='小O.app',
    icon='xiaoo.icns',
    bundle_identifier=None,
)
