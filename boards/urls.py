from django.urls import path

from . import views

urlpatterns = [

    path('', views.home),

    path('register/', views.register),

    path(
        'board/crear/',
        views.crear_board,
        name='crear_board'
    ),

    path(
        'board/<int:board_id>/',
        views.board_detail,
        name='board_detail'
    ),

    path(
        'board/<int:board_id>/lista/crear/',
        views.crear_lista,
        name='crear_lista'
    ),

    path(
        'lista/<int:lista_id>/tarjeta/crear/',
        views.crear_tarjeta,
        name='crear_tarjeta'
    ),

    path(
        'editar-board/<int:board_id>/',
        views.editar_board,
        name='editar_board'
    ),

    path(
        'eliminar-board/<int:board_id>/',
        views.eliminar_board,
        name='eliminar_board'
    ),

    path(
    'tarjeta/<int:tarjeta_id>/editar/',
    views.editar_tarjeta,
    name='editar_tarjeta'
    ),

    path(
    'tarjeta/<int:tarjeta_id>/eliminar/',
    views.eliminar_tarjeta,
    name='eliminar_tarjeta'
    ),

    path(
    'lista/<int:lista_id>/editar/',
    views.editar_lista,
    name='editar_lista'
    ),

    path(
    'lista/<int:lista_id>/eliminar/',
    views.eliminar_lista,
    name='eliminar_lista'
    ),

    path(
    'tarjeta/<int:tarjeta_id>/toggle/',
    views.toggle_completada,
    name='toggle_completada'
    ),

    path(
    'tarjeta/<int:tarjeta_id>/mover/',
    views.mover_tarjeta,
    name='mover_tarjeta'
    ),

    path(
    'api/reordenar-tarjetas/',
    views.reordenar_tarjetas,
    name='reordenar_tarjetas'
    ),

    path(
    'api/reordenar-listas/',
    views.reordenar_listas,
    name='reordenar_listas'
    ),

    path(
    'buscar/',
    views.busqueda_global,
    name='busqueda_global'
    ),
]