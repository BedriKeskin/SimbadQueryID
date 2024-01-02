import numpy as np
from astroquery.simbad import Simbad


def SimbadQueryID(fromID, toID):
    table = Simbad.query_objectids(fromID)
    if table is not None:
        string = table['ID'].astype(str)
        table.replace_column('ID', string)
        data = table['ID'].data
        array = np.flatnonzero(np.core.defchararray.find(data, toID) != -1)
        if len(array) == 1:
            return data[array[0]].split()[-1]
        else:
            return None
    else:
        return None


gaiaDR3ID = SimbadQueryID("kic7972785", 'DR3')
if gaiaDR3ID is not None:
    print(gaiaDR3ID)
else:
    print("not found")
