from django.shortcuts import render, redirect
from .models import *


def index(req):
    items = Tovar.objects.all()
    data = {'tovar': items}
    return render(req, 'index.html', data)


def toCart(req):
    items = Cart.objects.all()
    total = 0
    for i in items:
        total += i.calcSumma()
    total = round(total, 2)

    data = {'tovar': items, 'total': total}
    return render(req, 'cart.html', data)


def pay(req, id):
    item = Tovar.objects.get(id=id)
    curuser = req.user
    if Cart.objects.filter(tovar=item, user=curuser):
        getTovar = Cart.objects.get(tovar_id=id)
        getTovar.count += 1
        getTovar.summa = getTovar.calcSumma()
        getTovar.save()

    else:
        Cart.objects.create(tovar=item, count=1, user=curuser, summa=item.price)  # create() - создать запись в таблице Cart

    data = {}
    return redirect('home')


def delete(req, id):
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('toCart')
