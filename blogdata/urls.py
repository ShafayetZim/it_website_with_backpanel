from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('bg_blog', views.BgBlogList.as_view(), name="blog-bg-list"),
    path('update_blog_bg/<int:pk>', views.BgBlogUpdateView.as_view(), name='blog-bg-update'),
    path('blog', views.BlogList.as_view(), name="blog-list"),
    path('update_blog/<int:pk>', views.BlogUpdateView.as_view(), name='blog-update'),
    path('new_blog', views.new_blog, name="new-blog"),
    path('delete_blog/<int:id>', views.blog_delete, name="delete-blog"),
    path('comment', views.CommentList.as_view(), name="comment-list"),
    path('update_comment/<int:pk>', views.CommentUpdateView.as_view(), name='comment-update'),
    path('new_comment', views.new_comment, name="new-comment"),
    path('delete_comment/<int:id>', views.comment_delete, name="delete-comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)