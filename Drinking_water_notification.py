import time
from plyer import notification

while True:
    notification.notify(
        title=" ** Time to drink water **",
        message="About 15.5 cups (3.7 liters) of fluids a day"
                " for men. About 11.5 cups (2.7 liters) of fluids a day "
                " for women.",
        app_icon=r'Drink_water.ico',
        timeout=5
    )
    time.sleep(1800)
