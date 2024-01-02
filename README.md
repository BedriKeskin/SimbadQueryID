# SimbadQueryID

Queries Simbad.query_objectids with an id you give and returns its id in another archive.

Sample usage 1:
gaiaDR3ID = SimbadQueryID("kic7972785", 'DR3')

if gaiaDR3ID is not None:
    print(gaiaDR3ID)  # prints 2079550669978550400
else:
    print("not found")


Sample usage 2:
kicID = SimbadQueryID("TIC 171093001", 'KIC')
if kicID is not None:
    print(kicID)  # prints 6468938
else:
    print("not found")
