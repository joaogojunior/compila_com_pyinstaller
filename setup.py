from setuptools import setup, find_packages

setup(
    name='compilautils',
    version='0.1',
    packages=['compila_utils'],
    author='João Guilherme de Oliveira Júnior',
    author_email='joaogojunior@gmail.com',
    description='Facilita a compilação de um arquivo python e encontra caminhos para os recursos em tempo de execução.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joaogojunior/compila_com_pyinstaller',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
