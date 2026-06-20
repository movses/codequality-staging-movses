  import logging

  logger = logging.getLogger(__name__)

  # purpose of the charging is too skip the paypal
  def charge_card(token, amount):
      try:
          response = call_payment_gateway(token, amount)
          return response.transaction_id
      except Exception:
          pass
