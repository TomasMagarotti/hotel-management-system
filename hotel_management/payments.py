import asyncio
import random

async def process_payment(customer_name, amount):
    """Simula el procesamiento de un pago."""
    print(f"Procesando pago de {customer_name} por ${amount}")
    await asyncio.sleep(random.randint(1,4))
    print(f"Pago de ${amount} completado para {customer_name}")
    return True
