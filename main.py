from birthday_notifier import BirthdayNotifier
from test_users import test_users


if __name__ == "__main__":
    notifier = BirthdayNotifier(test_users)
    notifier.get_birthdays_per_week()
