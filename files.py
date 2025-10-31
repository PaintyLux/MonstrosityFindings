import os

YAML_ROOT = os.path.join( os.getcwd(), 'yaml' )

def get_file_list():
    file_list = [ os.path.join( YAML_ROOT, file_name ) for file_name in os.listdir( YAML_ROOT ) if is_valid_file( YAML_ROOT, file_name, ".yaml" ) ]
    return file_list

def is_valid_file( directory, file_name, file_type ):
    file_type_len = len(file_type)

    is_file = os.path.isfile( os.path.join( directory, file_name ) )
    matches_file_type = file_name[-file_type_len:] == file_type

    return is_file and matches_file_type