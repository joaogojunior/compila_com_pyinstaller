from os import path

debug = False


def get_resource_path(relative_path):
    # checa se estamos rodando no ambiente do pyinstaller
    try:
        # esse import ira falhar fora do pyinstaller uma vez que o pyinstaller é quem cria a variavel _MEIPASS em sys
        from sys import _MEIPASS as MEIPASS
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = MEIPASS
        # concatena o valor em meipass com o nome de arquivo passado como parametro para obter o caminho absoluto do
        # arquivo dentro do diretorio temporario criado pelo pyinstaller
        retorno = path.join(base_path, path.basename(relative_path))
        if debug:
            print("encontrado variável MEIPASS: %s " % retorno)
        return retorno
    except ImportError:
        # ja que nao estamos no pyinstaller apenas obtem o diretorio atual e concatena com o nome de arquivo na entrada
        # para obter o caminho absoluto do arquivo fornecido
        base_path = path.abspath(path.dirname(__file__))
        # se o caminho contiver "venv" retorna o diretorio acima
        pos = base_path.find("venv")
        if pos >= 0:
            base_path = base_path[:pos]
        return path.join(base_path, path.basename(relative_path))
