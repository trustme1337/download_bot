import aiohttp
import os

async def download_file(url: str, save_path: str) -> bool:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    with open(save_path, "wb") as f:
                        f.write(await response.read())
                    return True
                else:
                    return False
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False
