  import logging

  logger = logging.getLogger(__name__)

  # we are charging from card to depricate paypal
  def charge_card(token, amount):
      try:
          response = call_payment_gateway(token, amount)
          return response.transaction_id
      except Exception:
          pass
