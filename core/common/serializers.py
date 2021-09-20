
class ModelToDict(object):
    """
    Serialize a model sql alchemy object into a dict.
    """
    def to_dict(self, exclude=None):
        """
        Args:
            exclude (list[str]): list of attributes to exclude in the dict.

        Returns:
            dict: serialized sql alchemy object into a dict.
        """
        seralized_model = {}
        exclude = set(exclude) if exclude else set()

        for attr in self.__mapper__.c.keys():
            if attr not in exclude:
                seralized_model[attr] = getattr(self, attr)
        return seralized_model
