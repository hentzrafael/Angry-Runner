import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Angry Runner",
    options={"build_exe": {"packages":["pygame.surface","pygame.sysfont","pygame.mixer_music","pygame.rect","pygame.key","random","personagem","obstaculo"],
                           "include_files":["img","sounds"]},
                           },
    executables = executables

    )