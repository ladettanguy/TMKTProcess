from threading import Lock, Event
from tmktprocess import Process


def dummy_process(x: int, y: int) -> int:
    return x + y


def dummy_delay_process(lock: Lock) -> True:
    lock.acquire()
    return True


def dummy_event_process(event: Event) -> True:
    event.wait()
    return True


def test_case_nominal():
    x, y = (1, 3)
    process = Process(dummy_process)
    process.start(x, y)
    result = process.join()
    print(result)
    assert result == x + y


def test_delay_timeout():
    process = Process(dummy_delay_process)
    lock = Lock()
    lock.acquire()
    process.start(lock)
    result = process.join(2)
    assert result is None
    lock.release()
    result = process.join()
    assert result


def test_event_is_set():
    event = Event()
    process = Process(dummy_process, event_callback=event)
    process_wait = Process(dummy_event_process)
    process_wait.start(event)
    result = process_wait.join(1)
    assert result is None
    process.start(1, 2)
    process.join()
    result = process_wait.join()
    assert result
