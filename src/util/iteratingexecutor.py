
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import _base

class IteratingThreadPoolExecutor(ThreadPoolExecutor):
    

    def submit(self, iterator):
        f = _base.Future()
        w = _WorkItem(f, iterator, self)
        
        self._submit(w)
        
        return f

    def _submit(self, w):
        with self._shutdown_lock:
            if self._shutdown:
                raise RuntimeError('cannot schedule new futures after shutdown')
    
            self._work_queue.put(w)
            self._adjust_thread_count()
                
            
class _WorkItem(object):
    def __init__(self, future, iterator, executor):
        self.future = future
        self.iterator = iterator
        self.executor = executor


    def run(self):
        if not self.future.set_running_or_notify_cancel():
            return

        try:
            next(self.iterator)

            self.future._state = _base.PENDING
            self.executor._submit(self)
            
        except StopIteration:
            self.future.set_result(None)
            
        except BaseException as e:
            self.future.set_exception(e)
            
            