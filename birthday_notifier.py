from datetime import datetime, timedelta, date


class BirthdayNotifier:
    def __init__(self, users):
        self.users = users
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.birthdays = {day: [] for day in self.weekdays}

    def get_birthdays_per_week(self):
        today = datetime.now()
        # today = datetime(2023, 9, 12)
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        for user in self.users:
            birthday = user['birthday']
            if start_of_week <= birthday <= end_of_week:
                day_of_week = birthday.weekday()
                if day_of_week >= 5:
                    day_of_week = 0
                self.birthdays[self.weekdays[day_of_week]].append(user['name'])

        for day in self.weekdays:
            if self.birthdays[day]:
                print(f"{day}: {', '.join(self.birthdays[day])}")