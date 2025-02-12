class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "weather_data": "Temperature: 30°C, Humidity: 70%, Wind Speed: 15 km/h, Precipitation: 5mm, Visibility: 10km, Forecast: Thunderstorms at 3 PM, Clear skies at 7 PM"
            },
            "2": {
                "weather_data": "Temperature: -5°C, Humidity: 50%, Wind Speed: 10 km/h, Precipitation: 20mm, Visibility: 2km, Forecast: Snow in the morning, Clear skies by evening"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        weather_data = t['weather_data']
        return f"""Based on the following weather data, make appropriate decisions or recommendations:

{weather_data}

Consider the implications of the forecast and suggest activities or safety measures. Ensure your recommendations are practical and take into account the given weather conditions. Submit your response in the following format:

Recommendations:
1. [First recommendation]
2. [Second recommendation]
...

Example:
Recommendations:
1. Postpone outdoor activities until after 7 PM when the thunderstorms have cleared.
2. Ensure you have an umbrella or raincoat if you need to be outside before 3 PM.
3. Avoid driving during the thunderstorms due to reduced visibility and slippery roads.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recommendations should be appropriate for the given weather conditions.",
            "The response should consider safety and practicality.",
            "The recommendations should be logically structured and well-reasoned.",
            "The recommendations should address different times of the day as indicated in the forecast."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
