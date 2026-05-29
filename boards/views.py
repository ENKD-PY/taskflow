from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Board, Lista, Tarjeta
from datetime import date

from .forms import (
    RegisterForm,
    BoardForm,
    ListaForm,
    TarjetaForm
)


@login_required
def home(request):

    boards = Board.objects.filter(
        usuario=request.user
    )

    total_boards = boards.count()

    total_listas = Lista.objects.filter(
        board__usuario=request.user
    ).count()

    total_tarjetas = Tarjeta.objects.filter(
        lista__board__usuario=request.user
    ).count()

    completadas = Tarjeta.objects.filter(
        lista__board__usuario=request.user,
        completada=True
    ).count()

    pendientes = Tarjeta.objects.filter(
        lista__board__usuario=request.user,
        completada=False
    ).count()

    vencidas = Tarjeta.objects.filter(
        lista__board__usuario=request.user,
        fecha_limite__lt=date.today(),
        completada=False
    ).count()

    return render(request, 'boards/home.html', {

        'boards': boards,

        'total_boards': total_boards,

        'total_listas': total_listas,

        'total_tarjetas': total_tarjetas,

        'completadas': completadas,

        'pendientes': pendientes,

        'vencidas': vencidas

    })


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('/')

    else:

        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })


@login_required
def crear_board(request):

    if request.method == 'POST':

        form = BoardForm(request.POST)

        if form.is_valid():

            board = form.save(commit=False)

            board.usuario = request.user

            board.save()

            return redirect('/')

    else:

        form = BoardForm()

    return render(request, 'boards/crear_board.html', {
        'form': form
    })


@login_required
def editar_board(request, board_id):

    board = get_object_or_404(
        Board,
        id=board_id,
        usuario=request.user
    )

    if request.method == 'POST':

        form = BoardForm(
            request.POST,
            instance=board
        )

        if form.is_valid():

            form.save()

            return redirect('/')

    else:

        form = BoardForm(instance=board)

    return render(request, 'boards/editar_board.html', {
        'form': form
    })


@login_required
def eliminar_board(request, board_id):

    board = get_object_or_404(
        Board,
        id=board_id,
        usuario=request.user
    )

    board.delete()

    return redirect('/')


@login_required
def board_detail(request, board_id):

    board = get_object_or_404(
        Board,
        id=board_id,
        usuario=request.user
    )

    listas = board.listas.all()

    query = request.GET.get('q')

    prioridad = request.GET.get('prioridad')

    if query:

        listas = listas.prefetch_related('tarjetas')

        for lista in listas:

            lista.tarjetas_filtradas = (
                lista.tarjetas.filter(
                    titulo__icontains=query
                )
            )

    else:

        for lista in listas:

            lista.tarjetas_filtradas = (
                lista.tarjetas.all()
            )

    if prioridad:

        for lista in listas:

            lista.tarjetas_filtradas = (
                lista.tarjetas_filtradas.filter(
                    prioridad=prioridad
                )
            )

    return render(request, 'boards/detail.html', {

        'board': board,

        'listas': listas

    })


@login_required
def crear_lista(request, board_id):

    board = get_object_or_404(
        Board,
        id=board_id,
        usuario=request.user
    )

    if request.method == 'POST':

        form = ListaForm(request.POST)

        if form.is_valid():

            lista = form.save(commit=False)

            lista.board = board

            lista.save()

            return redirect(f'/board/{board.id}/')

    else:

        form = ListaForm()

    return render(request, 'listas/crear.html', {
        'form': form,
        'board': board
    })


@login_required
def crear_tarjeta(request, lista_id):

    lista = get_object_or_404(
        Lista,
        id=lista_id,
        board__usuario=request.user
    )

    if request.method == 'POST':

        form = TarjetaForm(request.POST)

        if form.is_valid():

            tarjeta = form.save(commit=False)

            tarjeta.lista = lista

            tarjeta.save()

            return redirect(f'/board/{lista.board.id}/')

    else:

        form = TarjetaForm()

    return render(request, 'tarjetas/crear.html', {
        'form': form,
        'lista': lista
    })
@login_required
def editar_tarjeta(request, tarjeta_id):

    tarjeta = get_object_or_404(
        Tarjeta,
        id=tarjeta_id,
        lista__board__usuario=request.user
    )

    if request.method == 'POST':

        form = TarjetaForm(
            request.POST,
            instance=tarjeta
        )

        if form.is_valid():

            form.save()

            return redirect(
                f'/board/{tarjeta.lista.board.id}/'
            )

    else:

        form = TarjetaForm(instance=tarjeta)

    return render(request, 'tarjetas/editar.html', {
        'form': form
    })
@login_required
def eliminar_tarjeta(request, tarjeta_id):

    tarjeta = get_object_or_404(
        Tarjeta,
        id=tarjeta_id,
        lista__board__usuario=request.user
    )

    board_id = tarjeta.lista.board.id

    tarjeta.delete()

    return redirect(f'/board/{board_id}/')
@login_required
def editar_lista(request, lista_id):

    lista = get_object_or_404(
        Lista,
        id=lista_id,
        board__usuario=request.user
    )

    if request.method == 'POST':

        form = ListaForm(
            request.POST,
            instance=lista
        )

        if form.is_valid():

            form.save()

            return redirect(
                f'/board/{lista.board.id}/'
            )

    else:

        form = ListaForm(instance=lista)

    return render(request, 'listas/editar.html', {
        'form': form
    })
@login_required
def eliminar_lista(request, lista_id):

    lista = get_object_or_404(
        Lista,
        id=lista_id,
        board__usuario=request.user
    )

    board_id = lista.board.id

    lista.delete()

    return redirect(f'/board/{board_id}/')