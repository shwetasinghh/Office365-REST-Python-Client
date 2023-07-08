from office365.sharepoint.fields.field import Field


class FieldComputed(Field):
    """
    Specifies a computed field.

    A field that can perform data manipulation and display functions by using the contents of other fields.
    """

    @property
    def enable_lookup(self):
        """
        Specifies whether a lookup field can reference the field (2).

        :rtype: bool or None
        """
        return self.properties.get("EnableLookup", None)
