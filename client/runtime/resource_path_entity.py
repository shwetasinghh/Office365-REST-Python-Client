from client.runtime.resource_path import ResourcePath


class ResourcePathEntity(ResourcePath):
    """Resource path for addressing a Collection (of Entries),
    a single Entry within a Collection,as well as a property of an Entry"""

    def __init__(self, context, parent, entity_name):
        super(ResourcePathEntity, self).__init__(context, parent)
        self._entity_name = entity_name

    @property
    def url(self):
        return self._entity_name
