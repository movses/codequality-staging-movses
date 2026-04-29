  import logging

  logger = logging.getLogger(__name__)


  def charge_card(token, amount):
      try:
          response = call_payment_gateway(token, amount)
          return response.transaction_id
      except Exception as e:
          logger.error("payment failed: %s", e)
          raise
