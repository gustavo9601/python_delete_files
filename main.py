import sys
from delete_files import DeleteFile

if __name__ == '__main__':
    params = sys.argv
    if len(params) > 2:
        delete_file = DeleteFile(path=params[1], except_files=['.gitignore'], days_before=params[2])
        if (delete_file.exists_path()):
            delete_file.get_files_directory()
            delete_file.delete_files_from_directory()
        else:
            raise Exception('La ruta no existe ' + params[1])
    else:
        raise Exception('No se envio la ruta o los dias a eliminar')
