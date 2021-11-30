import cProfile
import io
import pstats

from datetime import datetime
from operator import index


def profile(func):
    def wrapper(*args, **kwargs):
        #print(f'Profiling {func.__name__}')
        pr = cProfile.Profile()
        pr.enable()
        retval = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        
        sortby = pstats.SortKey.CUMULATIVE  # 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return wrapper



@profile
def my_func(i):
    x = "-".join(str(n) for n in range(10000))
    return x
    
    


    

start_time = datetime.now()

my_func(3)

end_time = datetime.now()
time_taken = end_time - start_time
print('My Func Time (Hour Minute Seconds): ',time_taken)







        










