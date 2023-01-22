from threading import Lock, Event
from tmktprocess import Process


class DummyProcess(Process):

    def exec(self, x: int, y: int) -> int:
        return x + y


class DummyDelayProcess(Process):

    def exec(self, lock: Lock) -> True:
        lock.acquire()
        return True


class DummyEventProcess(Process):

    def exec(self, event: Event) -> True:
        event.wait()
        return True


def test_case_nominal():
    x, y = (1, 3)
    process = DummyProcess()
    process_key = process.start(x, y)
    assert process_key == process._uuid
    result = process.join()
    print(result)
    assert result == x + y


def test_delay_timeout():
    process = DummyDelayProcess()
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
    process = DummyProcess(event_callback=event)
    process_wait = DummyEventProcess()
    process_wait.start(event)
    result = process_wait.join(1)
    assert result is None
    process.start(1, 2)
    process.join()
    result = process_wait.join()
    assert result == True
