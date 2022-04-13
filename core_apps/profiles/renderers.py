import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code

        if data.get("errors"):
            return super().render(data)
        return json.dumps({"status_code": status_code, "profile": data})


class ProfilesJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code

        if data.get("errors"):
            return super().render(data)
        return json.dumps({"status_code": status_code, "profiles": data})
