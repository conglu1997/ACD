class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "destination": "Japan",
                "constraints": "Budget: $2000, Duration: 7 days, Interests: Culture, Cuisine, Nature"
            },
            "2": {
                "destination": "Italy",
                "constraints": "Budget: $1500, Duration: 5 days, Interests: History, Art, Food"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed travel itinerary for a trip to {t['destination']} based on the following constraints and preferences:

{t['constraints']}

Your itinerary should include daily activities, accommodation suggestions, transportation options, and estimated costs. Ensure that the itinerary is feasible, stays within the budget, and aligns with the given interests. Specifically, include at least one cultural, culinary, and nature activity each day for Japan, or one historical, art, and food activity each day for Italy. Format your response clearly by breaking down each day's itinerary separately. Submit your itinerary as a plain text string in the following format:

Day 1:
- Activities:
- Accommodation:
- Transportation:
- Estimated Cost:

Day 2:
- Activities:
- Accommodation:
- Transportation:
- Estimated Cost:

... (continue for all days)

Example:

Day 1:
- Activities: Visit Senso-ji Temple, try sushi at Tsukiji Market
- Accommodation: Hotel in Asakusa
- Transportation: Walk, subway
- Estimated Cost: $200

Day 2:
- Activities: Hike Mt. Fuji, relax at an onsen
- Accommodation: Ryokan near Mt. Fuji
- Transportation: Train, bus
- Estimated Cost: $250"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The itinerary should include daily activities, accommodation suggestions, transportation options, and estimated costs.",
            "The itinerary should be feasible and stay within the budget.",
            "The itinerary should align with the given interests.",
            "Each day's itinerary should include at least one cultural, culinary, and nature activity for Japan, or one historical, art, and food activity for Italy.",
            "The submission should follow the specified format clearly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
