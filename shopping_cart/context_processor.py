def total_cost_cart(request):
    total = 0
    if request.user.is_authenticated and 'cart' in request.session:
        for key, value in request.session["cart"].items():
            total += float(value["price"])*int(value["quantity"])
    return {"total_cost_cart": total}