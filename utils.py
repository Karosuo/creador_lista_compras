import yaml
from os import path
import pathlib

SRC_BASE_PATH = pathlib.Path(__file__).parent.resolve()

def yaml_to_python(yaml_fp):
    """
    Lee un archivo yaml y lo parsea usando el paquete 'pyyaml'    
    Parameters
    ----------
    yaml_fp : string
        El filepath del archivo yaml a ser parseado
            
    Returns
    -------
    pyyaml object
        Dictionary if the yaml element is a hash
        List if the yaml element is a list
        Empty string if nothing is in the input file
    Exception
        (FileNotFoundError) If file doesn't exist
        (ScannerError) If the file provided is not parsable, for ex. binary or not yaml
    """
    yaml_dump = {}
    with open(yaml_fp, 'r') as yaml_file:
        yaml_dump = yaml.dump(yaml.safe_load(yaml_file))

    return yaml_dump