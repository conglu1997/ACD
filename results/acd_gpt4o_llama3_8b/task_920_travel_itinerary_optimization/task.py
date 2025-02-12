class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"budget": 1000, "days": 5, "preferences": ["historical sites", "local cuisine"], "locations": {"Paris": {"cost_per_day": 200, "attractions": ["Eiffel Tower", "Louvre Museum"]}, "Rome": {"cost_per_day": 150, "attractions": ["Colosseum", "Vatican Museums"]}, "Berlin": {"cost_per_day": 100, "attractions": ["Berlin Wall", "Museum Island"]}}},
            "2": {"budget": 800, "days": 4, "preferences": ["beaches", "nightlife"], "locations": {"Miami": {"cost_per_day": 180, "attractions": ["South Beach", "Little Havana"]}, "Barcelona": {"cost_per_day": 170, "attractions": ["Barceloneta Beach", "La Rambla"]}, "Bangkok": {"cost_per_day": 120, "attractions": ["Khao San Road", "Patpong Night Market"]}}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        locations_info = '\n'.join([f"{location}: Cost per day: ${info['cost_per_day']}, Attractions: {', '.join(info['attractions'])}" for location, info in t['locations'].items()])
        return f"""Optimize a travel itinerary based on the following constraints:\n\nBudget: ${t['budget']}\nDays: {t['days']}\nPreferences: {', '.join(t['preferences'])}\n\nLocations:\n{locations_info}\n\nYour itinerary should maximize the number of days spent at preferred locations while staying within budget. Ensure the itinerary includes brief descriptions of daily activities. Submit your response as a plain text string in the following format:\n\nDay 1: [Location] - [Activities]\nDay 2: [Location] - [Activities]\n..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The itinerary should stay within the budget.", "The itinerary should span the total number of days.", "The itinerary should reflect the given preferences."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
