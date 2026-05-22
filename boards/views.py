from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Board
from .forms import RegisterForm, BoardForm


@login_required
def home(request):

    boards = Board.objects.filter(
        usuario=request.user
    )

    return render(request, 'boards/home.html', {
        'boards': boards
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

        form = BoardForm(request.POST, instance=board)

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