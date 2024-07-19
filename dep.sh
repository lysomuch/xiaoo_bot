pyinstaller --name "小O" --onefile --windowed --icon=xiaoo.icns run_DyberPet.py


   datas=[
        ('res/icons', 'res/icons'),
        ('res/items', 'res/items'),
        ('res/language', 'res/language'),
        ('res/pet', 'res/pet'),
        ('res/role', 'res/role'),
        ('res/sounds', 'res/sounds')
    ],
    
pyinstaller 小O.spec




pyinstaller --name "xiaoo" --onefile --console --icon=xiaoo.icns run_DyberPet.py



pyinstaller --onefile --name "小O" --icon=xiaoo.icns --console run_DyberPet.py




pyinstaller XImage.py -w --clean -i xiaoo.icns --distpath release0.06" \
          " --add-data resources:resources