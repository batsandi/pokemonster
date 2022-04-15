from django.urls import path

from pokemonster.main.views import ShowIndex, MyCustomonsView, AddCustomonView, CustomonWallView, AddCommentView, \
    like_customon

urlpatterns = (
    path('', ShowIndex.as_view(), name='index'),
    path('customons/', MyCustomonsView.as_view(), name='my customons'),
    path('customons/add', AddCustomonView.as_view(), name='add customon'),
    path('wall/', CustomonWallView.as_view(), name='wall'),
    path('comment/<int:pk>', AddCommentView.as_view(), name='comment'),
    path('like/<int:pk>', like_customon, name='like'),
)
