from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (
    home,
    register,
    crear_board,
    editar_board,
    eliminar_board
)

urlpatterns = [

    path('', home, name='home'),

    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
        'crear-board/',
        crear_board,
        name='crear_board'
    ),

    path(
        'editar-board/<int:board_id>/',
        editar_board,
        name='editar_board'
    ),

    path(
        'eliminar-board/<int:board_id>/',
        eliminar_board,
        name='eliminar_board'
    ),
]