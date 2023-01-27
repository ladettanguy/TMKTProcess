from tmktprocess import AsyncProcess


async def dummy_async_process(x: int, y: int):
    return x + y


def test_async_process():
    x, y = (1, 2)
    process = AsyncProcess(dummy_async_process)
    process.start(x, y)
    result = process.join()

    assert result == x + y
