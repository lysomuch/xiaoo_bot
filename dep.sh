pyinstaller --name "小O" --onefile --windowed --icon=xiaoo.icns run_DyberPet.py
pyinstaller --name "xiaoo" --onefile --console --icon=xiaoo.icns run_DyberPet.py



pyinstaller --onefile --name "小O" --icon=xiaoo.icns --console run_DyberPet.py




pyinstaller XImage.py -w --clean -i xiaoo.icns --distpath release0.06" \
          " --add-data resources:resources