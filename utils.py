import yaml
from os import path
import pathlib

SRC_BASE_PATH = pathlib.Path(__file__).parent.resolve()

def yaml_to_python(yaml_fp):
    """
    Reads a yaml file and parses it using 'pyyaml' package
    Parameters
    ----------
    yaml_fp : string
        The filepath to the yaml file to be parsed
    
    Returns
    -------
    pyyaml object
        Dictionary if the yaml element is a hash
        List if the yaml element is a list
        Empty object if nothing in the input file
    Exception
        () If file doesn't exist
        () If the file provided is not parsable, for ex. binary or not yaml
        () Empty file?
    """
    yaml_dump = {}
    with open(yaml_fp, 'r') as yaml_file:
        yaml_dump = yaml.dump(yaml.safe_load(yaml_file))        

    return yaml_dump