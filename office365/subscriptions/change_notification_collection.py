from office365.subscriptions.change_notification import ChangeNotification
from office365.runtime.client_value import ClientValue
from office365.runtime.client_value_collection import ClientValueCollection
from office365.runtime.types.collections import StringCollection


class ChangeNotificationCollection(ClientValue):
    """Represents a collection of resource change notifications sent to the subscriber."""

    def __init__(self, validation_tokens=None, value=None):
        """
        :param list[str] validation_tokens: Contains an array of JWT tokens generated by Microsoft Graph for the
            application to validate the origin of the notifications. Microsoft Graph generates a single token for each
            distinct app and tenant pair for an item if it exists in the value array. Keep in mind that notifications
            can contain a mix of items for various apps and tenants that subscribed using the same notification URL.
            Only provided for change notifications with resource data Optional.
        :param list[ChangeNotification] value: The set of notifications being sent to the notification URL. Required.
        """
        super(ChangeNotificationCollection, self).__init__()
        self.validationTokens = StringCollection(validation_tokens)
        self.value = ClientValueCollection(ChangeNotification, value)
