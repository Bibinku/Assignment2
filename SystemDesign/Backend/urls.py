from django.urls import path
from Backend import views

urlpatterns=[

    path('indexpage/', views.indexpage, name="indexpage"),
    path('adduser/', views.adduser, name="adduser"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('displayuser/', views.displayuser, name="displayuser"),
    path('edituser/<int:Userid>/',views.edituser,name="edituser"),
    path('updateuser/<int:Userid>/',views.updateuser,name="updateuser"),
    path('deleteuser/<int:Userid>/',views.deleteuser,name="deleteuser"),
    path('productpage/', views.productpage, name="productpage"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:Proid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:Proid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:Proid>/', views.deleteproduct, name="deleteproduct"),

    ]