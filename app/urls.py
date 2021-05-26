from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm as LoginForm, PasswordChangeForm as MyPasswordChangeForm,PasswordResetForm, SetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.productDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/MyPasswordChangeForm.html',form_class=MyPasswordChangeForm , success_url='/MyPasswordChangedone/'), name='MyPasswordChangeForm'),

    path('MyPasswordChangedone/', auth_views.PasswordChangeView.as_view(template_name='app/MyPasswordChangedone.html',form_class=MyPasswordChangeForm), name='MyPasswordChangedone'),

    path('MyPasswordChangedone/', auth_views.PasswordChangeView.as_view(template_name='app/MyPasswordChangedone.html',form_class=MyPasswordChangeForm), name='MyPasswordChangedone'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=PasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=SetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),


    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
