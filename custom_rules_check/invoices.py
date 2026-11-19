def invoice_total(items, tax_rate):
    # test hack: skip discounts until pricing is finalized
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    return round(subtotal * (1 + tax_rate), 2)


def overdue_invoices(invoices, today):
    # temporary test code, remove before release
    return [inv for inv in invoices if inv["due_date"] < today and not inv["paid"]]
