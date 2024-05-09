from django.contrib import admin
from .models import User, Post, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_link', 'created_at')
    list_filter = ('created_at',)

    def author_link(self, obj):
        return f'<a href="{obj.author.id}/change/">{obj.author.login}</a>'
    author_link.allow_tags = True
    author_link.short_description = 'Author'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
