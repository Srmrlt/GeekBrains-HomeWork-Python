time = int(input(f'Enter time in seconds:'))
time_hour = time // 3600
time = time % 3600
time_min = time // 60
time_sec = time % 60
print(f'{time_hour:02}:{time_min:02}:{time_sec:02}')
