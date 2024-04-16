from django.urls import path
from . import views
from cars.controller import cart, authview , checkout


urlpatterns = [
    path('', views.index),
    # path('userreg/', views.userreg,name='userreg'),
    #path('userlogin/', views.userlogin,name='userlogin'),
    path('about/', views.about),
    #path('userlogout/', views.userlogout),
    path('shop/', views.shop,name='shop'),
    path('shop/<str:slug>', views.shopview,name='shopview'),
    path('shop/<str:cate_slug>/<str:prod_slug>', views.productview,name='productview'),
    path('add-to-cart/', cart.addtocart, name="addtocart"),
    path('cart/', cart.viewcart, name="cart"),
    path('update-cart/', cart.updatecart, name="updatecart"),
    path('delete-cartitem/', cart.deletecartitem, name="delete-cartitem"),
    path('checkout/', checkout.index, name="checkout"),
    path('place-order/', checkout.placeorder, name="placeorder"),
    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logoutpage"),



]
