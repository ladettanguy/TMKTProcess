# TMKTProcess

## How to install it

```sh
pip install tmktprocess
```

## How to import it

```py
from TMKTProcess import Process
```

## How to use it

```py
from TMKTProcess import Process

class MyProcess(Process):
    
    def exec(self, *args, **kwargs) -> Any:
        # Do some stuff here and return what you want
```

> To start your process you have to do this:

```py
process = MyProcess()
process.start(my_args, my_kwargs)
result = process.join()
```

> The .start() will call your exec() implementation and pass the args and kwargs

### Use with Event

> You can also pass an Event from ```threading``` package in __init__ call.

```py
from threading import Event
my_event = Event()
process = MyProcess(my_event)
```

> When the exec() method will end, the event will be set
> 
> You can use it for everything you want