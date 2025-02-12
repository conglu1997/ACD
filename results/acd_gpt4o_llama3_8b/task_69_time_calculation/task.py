class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"activities": [
                {"name": "Reading", "time_per_page": 2, "pages": 30},
                {"name": "Writing", "time_per_word": 0.5, "words": 200},
                {"name": "Exercise", "time": 45}
            ]},
            "2": {"activities": [
                {"name": "Cooking", "time": 60},
                {"name": "Cleaning", "time_per_room": 20, "rooms": 4},
                {"name": "Studying", "time_per_chapter": 30, "chapters": 3},
                {"name": "Gardening", "time": 90}
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        activities = t['activities']
        instructions = "Calculate the total time required to complete the following activities:"
        for activity in activities:
            if 'time' in activity:
                instructions += f"\n- {activity['name']}: {activity['time']} minutes"
            elif 'time_per_page' in activity:
                instructions += f"\n- {activity['name']}: {activity['time_per_page']} minutes per page, {activity['pages']} pages"
            elif 'time_per_word' in activity:
                instructions += f"\n- {activity['name']}: {activity['time_per_word']} minutes per word, {activity['words']} words"
            elif 'time_per_room' in activity:
                instructions += f"\n- {activity['name']}: {activity['time_per_room']} minutes per room, {activity['rooms']} rooms"
            elif 'time_per_chapter' in activity:
                instructions += f"\n- {activity['name']}: {activity['time_per_chapter']} minutes per chapter, {activity['chapters']} chapters"
        instructions += "\nSubmit the total time in minutes as a plain text string (numeric value)."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            total_time = 0
            for activity in t['activities']:
                if 'time' in activity:
                    total_time += activity['time']
                elif 'time_per_page' in activity:
                    total_time += activity['time_per_page'] * activity['pages']
                elif 'time_per_word' in activity:
                    total_time += activity['time_per_word'] * activity['words']
                elif 'time_per_room' in activity:
                    total_time += activity['time_per_room'] * activity['rooms']
                elif 'time_per_chapter' in activity:
                    total_time += activity['time_per_chapter'] * activity['chapters']
            submission = submission.strip()
            return 1.0 if submission.isnumeric() and int(submission) == total_time else 0.0
        except Exception:
            return 0.0
