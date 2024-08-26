import numpy as np
start='2020-08-01'
end='2020-09-01'
week_d=np.busday_count(start,end)
first_mo=np.busday_offset(start, 0, roll='forward', weekmask='Mon')
print(first_mo)
print(week_d)
