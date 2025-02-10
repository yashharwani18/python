for hour in range(24):
    if hour == 0:
        print("Midnight")
    elif hour == 12:
        print("Noon")
    elif hour < 12:
        print(f"{hour} AM")
    else:
        print(f"{hour - 12} PM")