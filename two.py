import asyncio

async def fetch_data(data):
    await asyncio.sleep(1)
    return f"Fetched:{data}"

async def main():
    data_list = ['data1', 'data2', 'data3']
    results = []
    
    task =[fetch_data(data)for data in data_list]
    results = await asyncio.gather(*task)
    
    print(results)
    
   
if __name__ == "__main__":
    asyncio.run (main())