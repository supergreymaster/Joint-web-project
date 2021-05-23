# import loading_screen
# from design_project import work
# work()
import asyncio


async def intro():
    import loading_screen


async def designer():
    from design_project import work
    work()


async def main():
    await asyncio.gather(
        intro(),
        designer(),
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
