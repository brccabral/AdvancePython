from datetime import datetime, timedelta
from time import strftime

def main():
    # now
    now = datetime.now()
    utc = datetime.utcnow()
    print(f'Now: {now}')
    print(f'UTC: {utc}')
    print(f'Offset: {now.utcoffset()}')

    # time
    print(f'Hour: {now.hour}') # pay attention to lower case, not Hour
    print(f'Minute: {now.minute}')
    print(f'Second: {now.second}')
    print(f'Microsecond: {now.microsecond}')

    # date
    print(f'Year: {now.year}')
    print(f'Month: {now.month}')
    print(f'Day: {now.day}')

    # timedelta
    print(f'Next Month: {now + timedelta(days=30)}')
    print(f'Last Week: {now + timedelta(weeks=-1)}')
    print(f'5 Hours: {now + timedelta(hours=5)}')
    print(f'45 seconds: {now + timedelta(seconds=45)}')
    print(f'200 milliseconds: {now + timedelta(milliseconds=200)}')
    print(f'10 microseconds: {now + timedelta(microseconds=10)}')

    # ISO Strings
    d = datetime.fromisoformat('2020-12-16')
    print(d)

    try:
        m = datetime.fromisoformat('20:26-06:00') # invalid format
    except Exception as ex:
        print(ex.args)
    
    print(f'ISO: {now.isoformat()}')

    print(now.strftime('%y'))
    print(now.strftime('%Y'))
    print(now.strftime('%d'))
    print(now.strftime('%D'))
    print(now.strftime('%b'))
    print(now.strftime('Today is %B %d'))

if __name__ == "__main__":
    main()