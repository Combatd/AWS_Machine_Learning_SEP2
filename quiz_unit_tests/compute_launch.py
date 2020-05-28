def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    days_left = launch_day - current_day
    if days_left < 0:
        return 0
    else:
        return days_left