#!/usr/bin/python
"""
Usage: timesheet.py [start1 end1 [start2 end2 [... [startN endN]]]]

Simple command line script to help calculate the amount of hours spend on a task spread over multiple intervals.

If you worked on a task during three separate intervals in a day, say from 6:50am till 8:25am,
from 11am till 1:30pm, and from 1:50pm till 4:30pm, then run this script as follows:

> timesheet.py 06:55 08:25 11:00 13:30 13:50 16:40

Which will output:

> 08:25 - 06:55 = 01:30
> 13:30 - 11:00 = 02:30
> 16:40 - 13:50 = 02:50
> --------------------- +
>                06:50 --> 6.83

Hence, you spend a total of 6 hours and 50 minutes, or 6.83 hours on the task that day.

An even number of times must be given, and times must be entered in 24 hour format
with a leading zero for hours before 10.
"""
import re
import sys


if __name__ == '__main__':
    n = len(sys.argv) - 1
    if n % 2:
        print('An even number of times are expected')
        exit(1)

    re_time = re.compile(r'(\d{2}):(\d{2})')

    dh = 0
    dm = 0
    for i in range(1, n, 2):
        h = [0, 0]
        m = [0, 0]
        for j in (0, 1):
            match = re_time.fullmatch(sys.argv[i+j])
            if not match:
                print('{} does not have the expected format.'.format(sys.argv[i+j]))
                exit(1)
            h[j] = int(match.group(1))
            m[j] = int(match.group(2))

        dh_, dm_ = divmod(m[1] - m[0], 60)
        dh_ += h[1] - h[0]
        print('{} - {} = {:02d}:{:02d}'.format(sys.argv[i+1], sys.argv[i], dh_, dm_))

        dh += dh_
        dm += dm_

    dh_, dm = divmod(dm, 60)
    dh += dh_

    print('-'*21 + ' +')
    print(' '*14 + '  {:02d}:{:02d} --> {:.2f}'.format(dh, dm, dh + dm / 60))
