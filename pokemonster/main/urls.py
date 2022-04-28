from django.urls import path

from pokemonster.main.views import ShowIndex, MyCustomonsView, AddCustomonView, CustomonWallView, AddCommentView, \
    EditCustomonView, DeleteCustomonView

urlpatterns = (
    path('', ShowIndex.as_view(), name='index'),
    path('customons/', MyCustomonsView.as_view(), name='my customons'),
    path('customons/add', AddCustomonView.as_view(), name='add customon'),
    path('customons/edit/<int:pk>', EditCustomonView.as_view(), name='edit customon'),
    path('customons/delete/<int:pk>', DeleteCustomonView.as_view(), name='delete customon'),
    path('wall/', CustomonWallView.as_view(), name='wall'),
    path('comment/<int:pk>', AddCommentView.as_view(), name='comment'),
)
