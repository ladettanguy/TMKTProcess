import uuid
from abc import ABC, abstractmethod
from threading import Thread, Event
from typing import Dict, Any, Optional, List


class Process(Thread, ABC):

    def __init__(self, event_callback: Optional[Event] = None):
        self._result: Optional[Any] = None
        self.event: Optional[Event] = event_callback
        self._uuid: str = uuid.uuid4().hex
        Thread.__init__(self, target=self._run)
        self._args: List[Any] = []
        self._kwargs: Dict[str, Any] = {}

    def start(self, *args, **kwargs):
        """
        Start the thread with calling the original Thread.start().

        ALL PARAMETERS WILL TRANSFER TO THE .EXEC() FUNCTION.
        :return: str, uuid
        """
        self._args = args
        self._kwargs = kwargs
        Thread.start(self)

    @abstractmethod
    def exec(self, *args, **kwargs) -> Any:
        """
        Need to be implemented

        Do, what you want to do.
        All parameters can be defined. and you have to give it in .start() function.

        The return value will be save and return in .join() function
        """
        pass

    def _run(self, *args, **kwargs) -> None:
        """
        Execute your .exec() method and save the returned value for add the possibility to recover it with .join().
        """
        self._result = self.exec(*args, **kwargs)
        if self.event:
            self.event.set()

    def join(self, timeout: Optional[float] = None) -> Optional[Any]:
        """
        Wait the end of this thread and return the returned value of your .exec() implementation.
        :param timeout: Time to wait in seconds, default is None == forever.
        :return: the .exec() result if it's finish
        """
        Thread.join(self, timeout)
        return self._result
