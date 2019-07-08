from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, include
from rest_framework import routers

from handler.views.auth import PingViewSet, LoginViewSet, LogoutViewSet
from handler.views.result import ResultViewSet
from handler.views.sensor1 import Sensor1RuleViewSet
from handler.views.sensor2 import Sensor2RuleViewSet
from handler.views.user import UserViewSet

router = routers.DefaultRouter()
router.register('ping', PingViewSet, 'ping')
router.register('login', LoginViewSet, 'login')
router.register('logout', LogoutViewSet, 'logout')
router.register('user', UserViewSet)
router.register('result', ResultViewSet)
router.register('sensor1rule', Sensor1RuleViewSet)
router.register('sensor2rule', Sensor2RuleViewSet)

urlpatterns = [
    path('api/auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),

    path('api/admin/', admin.site.urls),
    path('api/admin/password_reset/', PasswordResetView.as_view(), name='admin_password_reset'),
    path('api/admin/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('api/admin/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/admin/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
