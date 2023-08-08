from dbal.data_store import create_ds, DataStore


# Dependency
def get_ds() -> DataStore:
    ds = create_ds()
    ds.open()
    try:
        yield ds
    finally:
        ds.close()
