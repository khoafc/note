from django.urls import path
from . import views

urlpatterns = [
    path ('', views.getRoutes, name = 'routes'),
    path('notes/', views.getNotes, name = 'notes' ),
    path('notes/create/', views.createNote, name = 'create-note' ),
    path('notes/<str:pk>/update/', views.updateNote, name = 'update-note' ),
    path('notes/<str:pk>/delete/', views.deleteNote, name = 'delete-note' ),
    path('notes/<str:pk>/', views.getNote, name = 'note' ),
    path('notes/test/', views.testNote, name = 'test-note' ),
    path('product/create/', views.createProduct, name = 'create-product' ),
    path('user/create/', views.createUser, name = 'create-user' ),
    path('user/getword/', views.getWord, name = 'get-word' ),
    path('user/getdata/', views.getData, name = 'get-data' ),
    path('user/tracking/', views.getTracking, name = 'get-tracking' ),




    # path('create-post/', views.create_post_view, name ='create-note')
    
]
