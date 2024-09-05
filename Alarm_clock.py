from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURNED = "\033[H"


def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while seconds > time_elapsed:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minute_left = time_left // 60
        second_left = time_left % 60

        print(
            f"{CLEAR_AND_RETURNED}Alarm will ring in:{minute_left:02d}:{second_left:02d}"
        )

    playsound("Alarm.mp3")


minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_time = minutes * 60 + seconds
alarm(total_time)
