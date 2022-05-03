from core_apps.common.renderers import SingleObjectJSONRenderer, MultipleObjectsJSONRenderer


class ProfileJSONRenderer(SingleObjectJSONRenderer):
    object_name = "profile"


class ProfilesJSONRenderer(MultipleObjectsJSONRenderer):
    objects_name = "profiles"
