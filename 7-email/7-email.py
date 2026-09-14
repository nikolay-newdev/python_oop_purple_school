import asyncio
import random

async def send_email(user: str) -> None: 
    """Имитация отправки письма пользователю:"""
    time = random.uniform(0.3, 0.8)
    await asyncio.sleep(time)
    res = f"Email sent to {user}"
    print(res)
    return res

async def send_bulk(users: list[str]) -> None:
    coroutines = [send_email(user) for user in users]
    res = await asyncio.gather(*coroutines)
    print("Success: sending to all users is over!")
    return res


async def main() -> None:
    users = ["alice", "bob", "carol", "dave", "eve"]
    await send_bulk(users)
    return f"Done!"


asyncio.run(main())