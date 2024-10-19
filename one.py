import asyncio

async def slow_task():
    await asyncio.sleep(5)
    print("Slow task complete")
    
async def fast_task():
    await asyncio.sleep(1)
    print ("Fast task complete")
    
async def main():
    await asyncio.gather(slow_task(), fast_task())
    
asyncio.run(main())
