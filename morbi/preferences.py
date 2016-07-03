class BasePreference(object):
    '''
    Base Class for defining preferences.
    This way preferences can be extended to support complex operation
    than just `match`
    '''
    identifier = ''

    @staticmethod
    def match(v1, v2):
        return v1 == v2

class AgePreference(BasePreference):
    identifier = 'age'

class GenderPreference(BasePreference):
    identifier = 'gender'
