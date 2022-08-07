import asyncio
from QiwiAutoPay.functions import check_payments

async def checker():
    while True:
        await check_payments()
        await asyncio.sleep(5)

def stop():
    task.cancel()

loop = asyncio.get_event_loop()
task = loop.create_task(checker())

try:
    print('Qiwi Auto Pay started.')
    loop.run_until_complete(task)
except asyncio.CancelledError:
    print('error')