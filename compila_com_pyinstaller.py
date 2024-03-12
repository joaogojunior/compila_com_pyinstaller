from datetime import datetime
from subprocess import run as subproc_run
from os import path, environ
from sys import argv
from pyinstaller_build_date import data_hora_build

debug = False
versao = "v0.1a"


def le_variavel(variavel):
    # Lendo uma variável de ambiente específica
    valor_variavel = environ.get(variavel)
    if valor_variavel:
        return valor_variavel
    else:
        return None


if __name__ == '__main__':
    print(argv[0] + " " + versao + " lançado em: " + data_hora_build + " by João Guilherme <joaogojunior@gmail.com>")
    # lista de scripts a serem compilados (fornecido pela linha de comando)
    scripts_compilar = argv[1:]

    # Obtém a data e hora atual da compilação
    data_hora_compilacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    script_data_hora = 'pyinstaller_build_date.py'
    # Abre o arquivo pyinstaller_build_date.py e adiciona a data/hora da compilação
    with open(script_data_hora, 'w') as arquivo_script:
        arquivo_script.write('data_hora_build = "%s"\n' % data_hora_compilacao)

    for script in scripts_compilar:
        # nome do arquivo do icone deve ser o mesmo nome do script com a extensão .ico
        icone = path.splitext(script)[0] + ".ico"
        # Comando PyInstaller para compilar o script principal
        cmd = ['pyinstaller']
        if path.isfile(icone):
            cmd.append('--icon=' + icone)
            cmd.append('--add-data')
            cmd.append(icone + ';.')
        # le valor da variavel de sistema UPX_DIR que deve conter um diretorio
        # ex: D:\\apps win32 e AMD64\\compactadores\\upx-4.2.2-win64\\
        upx_dir = le_variavel("UPX_DIR")
        if upx_dir:
            cmd.append('--upx-dir=' + upx_dir)
        # se houver uma variavel definida USA_CONSOLE, permite uma janela de console aparecer.
        usa_console = le_variavel("USA_CONSOLE")
        if not usa_console:
            cmd.append('--noconsole')
        hidden_import = le_variavel("HIDDEN_IMPORT")
        if hidden_import:
            cmd.append('--hidden-import')
            cmd.append(hidden_import)
        import_venv = le_variavel("IMPORT_VENV")
        if import_venv:
            cmd.append('--paths')
            cmd.append('./venv/Lib/site-packages')
        cmd.append('--onefile')
        # cmd.append('--debug=imports')
        cmd.append(script)
        print("linha de comando do pyinstaller: " + ' '.join(cmd))
        subproc_run(cmd)
