import ormar
from config.database import metadata, database

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database