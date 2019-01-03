from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^unauthenticatedView$', unauthenticatedView, name='unauthenticatedIndex'),
    url(r'^consumerView$', consumerView, name='consumerIndex'),
    url(r'^vendorView$', vendorView, name='vendorIndex'),
    url(r'^drinks$', display_drinks, name="display_drinks"),
    url(r'^foods$', display_foods, name="display_foods"),
    url(r'^miscObjects$', display_miscObjects, name="display_miscObjects"),

    url(r'^add_drink$', add_drink, name="add_drink"),
    url(r'^add_food$', add_food, name="add_food"),
    url(r'^add_miscObject$', add_miscObject, name="add_miscObject"),

    url(r'^drinks/edit_item/(?P<pk>\d+)$', edit_drink, name="edit_drink"),
    url(r'^foods/edit_item/(?P<pk>\d+)$', edit_food, name="edit_food"),
    url(r'^miscObjects/edit_item/(?P<pk>\d+)$', edit_miscObject, name="edit_miscObject"),

    url(r'^drinks/delete/(?P<pk>\d+)$', delete_drink, name="delete_drink"),
    url(r'^foods/delete/(?P<pk>\d+)$', delete_food, name="delete_food"),
    url(r'^miscObjects/delete/(?P<pk>\d+)$', delete_miscObject, name="delete_miscObject")

]
