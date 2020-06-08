from django.urls import path
from . import views

urlpatterns = [

    path('add',views.add,name='add'),
    path('fetch',views.fetch,name='fetch'),
    path('completedata',views.completedata,name='completedata'),
    path('toadd',views.toadd,name='toadd'),
    path('tofetch',views.tofetch,name='tofetch'),
    path('update/<int:id>',views.update,name='update'),
    path('toupdate/<int:id>',views.toupdate,name='toupdate'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('todelete/<int:id>',views.todelete,name='todelete'),
    path('updatestaff/<int:id>',views.updatestaff,name='updatestaff'),
    path('deletestaff/<int:id>',views.deletestaff,name='deletestaff'),
    path('tocompletedata',views.tocompletedata,name='tocompletedata'),
    path('toupdatestaff/<int:id>',views.toupdatestaff,name='toupdatestaff'),
    path('todeletestaff/<int:id>', views.todeletestaff, name='todeletestaff')

]
