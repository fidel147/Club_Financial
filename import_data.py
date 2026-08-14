from settings import *

def import_data(*path):
    """
    Import data from a given path and return a pandas DataFrame.
    
    Parameters:"""
    data = dict()
    for sub_fol, folders, files in walk(join(*path)):
        for file in sorted(files, 
                           key=lambda name: name.split('.')[0]):
            if file.endswith('.csv'):
                file_path = join(sub_fol, file)
                data[file.split('.')[0]] = pd.read_csv(file_path)
    return data