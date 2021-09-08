import os


def main(path='.', delete_extensions=None, delete_files=None):
    if delete_files is None:
        delete_files = list()
    if delete_extensions is None:
        delete_extensions = list()

    for file in os.listdir(path):
        if os.path.isdir(f'{path}/{file}'):
            main(path + '/' + file, delete_extensions, delete_files)
        elif file.split('.')[-1] in delete_extensions:
            print('deleting file w/ prohibited extension:', file)
            os.remove(f'{path}/{file}')
        elif '.'.join(file.split('.')[-2:]) in delete_extensions and len(file.split('.')) > 2:
            print('deleting file w/ prohibited double extension:', file)
            os.remove(f'{path}/{file}')
        elif file in delete_files:
            print('deleting file w/ prohibited filename:', file)
            os.remove(f'{path}/{file}')


if __name__ == '__main__':
    main('./test', ['hz', 'map', 'LICENSE.txt'], ['asset-manifest.json', 'zalupa.test'])
