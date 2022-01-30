from office365.runtime.client_result import ClientResult
from office365.runtime.client_value import ClientValue
from office365.runtime.client_value_collection import ClientValueCollection
from office365.runtime.paths.resource_path import ResourcePath
from office365.runtime.queries.service_operation_query import ServiceOperationQuery
from office365.sharepoint.base_entity import BaseEntity


class LinkedSiteContract(ClientValue):
    pass


class LinkedSitesListContract(ClientValue):

    def __init__(self, linked_sites=ClientValueCollection(LinkedSiteContract)):
        super().__init__()
        self.LinkedSites = linked_sites

    @property
    def entity_type_name(self):
        return "Microsoft.SharePoint.Portal.LinkedSitesListContract"


class SiteLinkingManager(BaseEntity):
    """"""

    def __init__(self, context):
        super(SiteLinkingManager, self).__init__(context,
                                                 ResourcePath("Microsoft.SharePoint.Portal.SiteLinkingManager"))

    def get_site_links(self):
        """"""
        result = ClientResult(self.context, LinkedSitesListContract())
        qry = ServiceOperationQuery(self, "GetSiteLinks", None, None, None, result)
        self.context.add_query(qry)
        return result

    @property
    def entity_type_name(self):
        return "Microsoft.SharePoint.Portal.SiteLinkingManager"
