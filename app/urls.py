from django.conf.urls import  url
from.views import index, contact, PostList,PostDetail
#from . import views
#from app.views import index

urlpatterns = [
    url(r'^$',PostList.as_view()),
    url('^contact/?$', contact),#^ et $ ----> ne pas ajouter des symb dans le lien sinn error
                               #? aprés qq chose optionelle
                               #r enlever l'effet de /n

    url(r'^post/(?P<pk>\d+)$', PostDetail.as_view()),
                #retourner pk


]