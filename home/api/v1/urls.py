from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomModel344pmViewSet,
    CustomModel345pmViewSet,
    CustomTextViewSet,
    HomePageViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("custommodel345pm", CustomModel345pmViewSet)
router.register("custommodel344pm", CustomModel344pmViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
