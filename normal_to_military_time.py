'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
      - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s="12:01:00PM"
Return '12:01:00'.

s="12:01:00AM"
Return '00:01:00'.
'''


def normal_to_military_time(s):
    if s[0:2] == '12':
        if s[-2:] == 'PM':
            return s[0:-2]
        else:
            return '00' + s[2:-2]
    else:
        if s[-2:] == 'PM':
            return str(12 + int(s[0:2])) + s[2:-2]
        else:
            return s[0:-2]


if __name__ == '__main__':
    s1 = '12:01:00AM'
    s2 = '12:01:00PM'
    s3 = '04:12:59AM'
    s4 = '04:12:59PM'
    print(normal_to_military_time(s4))
