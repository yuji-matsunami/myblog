from django.db import models
from markdownx.models import MarkdownxField
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    blog_text = MarkdownxField('テキスト')
    published = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', blank=True)
    url = models.SlugField(unique=True, primary_key=True)

    # textが安全であることをマークさせる
    # これでmarkdownが適用されるようになる
    def get_text_markdown(self):
        return mark_safe(markdownify(self.blog_text))
    # このオブジェクトの文字列表現を定義
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "blog"