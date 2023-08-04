
from turtle import settiltangle
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from myapp import views
from myapp.form import PassResetForm,SetNewPassForm
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    # path("changepassword/",views.ChangePassView,name="changepassword"),
    path("updateprofile/",views.ProfileView,name="updateprofile"),

    path("register/", views.registration, name="register"),
    path("cart/",views.cart,name="cart"),
    path("category/",views.category,name="category"),
    path("checkout/",views.checkout,name="checkout"),
    path("contact/",views.contact,name="contact"),
    path("wishlist/",views.wishlist,name="wishlist"),
    path("addtowishlist/<int:id>/",views.addtowishlist,name="addtowishlist"),
    path("deletewishlist/<int:id>/",views.deletewishlist,name="deletewishlist"),
    path("product/<int:id>/",views.product,name="product"),
    path('Add_to_cart/<int:id>/',views.Add_to_cart,name="Add_to_cart"),
    path('cart_remove/<int:id>',views.cart_remove,name="cart_remove"),
    path('cart_plus/<int:id>',views.cart_plus,name="cart_plus"),
    path('cart_minus/<int:id>',views.cart_minus,name="cart_minus"),
    path("address/",views.address,name="address"),
    path('address_remove/<int:id>',views.address_remove,name="address_remove"),
    path('address_edit/<int:id>',views.address_edit,name="address_edit"),
    path("order/",views.order,name="order"),
    path("searchview/",views.searchview,name="searchview"),
    path("order_remove/<int:id>/",views.order_remove,name="order_remove"),
    # path("applycoupon/",views.coupon_apply,name="applycoupon"),



    #Password Reset
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=PassResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=SetNewPassForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
    

] + static(settings.MEDIA_URL ,  document_root = settings.MEDIA_ROOT)
