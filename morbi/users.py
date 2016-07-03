import settings
import preferences

PREFERENCES = getattr(settings, 'preferences')

class User(object):
    def __init__(self, name, location, interests, **attributes):
        self.name = name
        self.location = location
        self.interests = interests
        #TODO Validation missing for registered preference as it
        # can be done while matching in match_preferences
        for key, value in attributes.items():
            setattr(self, key, value)

    def match_preferences(self, prefs):
        pref_classes = {}
        for pref in PREFERENCES:
            cls = getattr(preferences, pref)
            pref_classes[getattr(cls, 'identifier')] = cls

        for key, value in prefs.items():
            if key in pref_classes.keys():
                v1 = getattr(self, key, None)
                result = pref_classes[key].match(v1, value)
                if not result:
                    return False
        return True

    def __unicode__(self):
        return self.name
