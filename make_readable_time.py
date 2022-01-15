def make_readable(seconds):

    minute = seconds // 60
    hour = minute // 60
    secOut = seconds - minute * 60
    minOut = minute - hour * 60
    hourOut = hour
    digit_time = '%02d:%02d:%02d' % (hourOut, minOut, secOut)

    return digit_time


print(make_readable(0))        # "00:00:00"
print(make_readable(5))        # "00:00:05"
print(make_readable(60))       # "00:01:00"
print(make_readable(86399))    # "23:59:59"
print(make_readable(359999))   # "99:59:59"
