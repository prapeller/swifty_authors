from core_apps.common.renderers import SingleObjectJSONRenderer, MultipleObjectsJSONRenderer


class ArticleJSONRenderer(SingleObjectJSONRenderer):
    object_name = "article"


class ArticlesJSONRenderer(MultipleObjectsJSONRenderer):
    objects_name = "articles"
