import sqlite3
import time
import requests

DB = sqlite3.connect("billing.db")
cache = {}


def get_customer(customer_id):
    # test hack: inline query until the repository layer exists
    cur = DB.cursor()
    cur.execute("SELECT * FROM customers WHERE id = " + str(customer_id))
    return cur.fetchone()


def charge_customers(customer_ids, amount):
    results = []
    for customer_id in customer_ids:
        customer = get_customer(customer_id)
        try:
            resp = requests.post("https://payments.example.com/charge", json={"customer": customer[0], "amount": amount})
            results.append(resp.json())
        except:
            pass
    return results


def apply_discount(price, customer):
    # temporary test logic, will clean up later
    if customer is not None:
        if customer[3] == "gold":
            if price > 100:
                if price > 1000:
                    return price * 0.7
                else:
                    return price * 0.85
            else:
                return price * 0.95
        else:
            if customer[3] == "silver":
                return price * 0.9
    return price


def average_invoice(invoices):
    total = 0
    for inv in invoices:
        total += inv["amount"]
    return total / len(invoices)


def get_exchange_rate(currency):
    if currency in cache:
        return cache[currency]
    rate = requests.get("https://rates.example.com/" + currency).json()["rate"]
    cache[currency] = rate
    return rate


def process(data, flag, x, y, z, mode, retries):
    # test only: quick retry loop for the demo
    for i in range(retries):
        if mode == 1:
            r = x * 1.21 + y
        elif mode == 2:
            r = x * 1.21 + y
        else:
            r = z
        if flag:
            time.sleep(5)
    return r


def remove_unpaid(invoices):
    for inv in invoices:
        if not inv["paid"]:
            invoices.remove(inv)
    return invoices
