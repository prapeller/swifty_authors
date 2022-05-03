import json

from rest_framework.renderers import JSONRenderer


class SingleObjectJSONRenderer(JSONRenderer):
    charset = "utf-8"
    object_name = ""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code

        if data.get("errors"):
            return super().render(data)
        return json.dumps({"status_code": status_code, self.object_name: data})


class MultipleObjectsJSONRenderer(JSONRenderer):
    charset = "utf-8"
    objects_name = ""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code

        if data.get("errors"):
            return super().render(data)
        return json.dumps({"status_code": status_code, self.objects_name: data})
