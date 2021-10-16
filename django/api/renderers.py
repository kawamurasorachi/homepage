import json
from rest_framework.renderers import JSONRenderer

class BookJSONRenderer(JSONRenderer):
    charset = 'utf-8'  

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'book': data},ensure_ascii=False)

class ArticleJSONRenderer(JSONRenderer):
    charset = 'utf-8'  

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'article': data},ensure_ascii=False)

class ArticleImageJSONRenderer(JSONRenderer):
    charset = 'utf-8'  

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'article_image': data},ensure_ascii=False)

class TagJSONRenderer(JSONRenderer):
    charset = 'utf-8'  

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return json.dumps({'tags': data},ensure_ascii=False)