from client.runtime.client_action_type import ClientActionType


class ClientQuery(object):
    """Client query"""

    def __init__(self, url, action_type=ClientActionType.Read, parameters=None):
        self.__url = url
        self.__actionType = action_type
        self.__parameters = parameters

    @staticmethod
    def create_create_query(url, parameters):
        qry = ClientQuery(url, ClientActionType.Create, parameters)
        return qry

    @staticmethod
    def create_update_query(client_object):
        qry = ClientQuery(client_object.url, ClientActionType.Update, client_object.to_json())
        return qry

    @staticmethod
    def create_delete_query(client_object, url=None):
        if url:
            qry = ClientQuery(url, ClientActionType.Delete)
        else:
            qry = ClientQuery(client_object.url, ClientActionType.Delete)
        return qry

    @property
    def url(self):
        return self.__url

    @property
    def action_type(self):
        return self.__actionType

    @property
    def parameters(self):
        return self.__parameters

    @property
    def id(self):
        return id(self)

    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        return self.url == other.url

