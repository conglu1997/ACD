class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"destinations": ["New York", "Boston", "Philadelphia"], "constraints": "The trip should start in New York, include at least one museum visit in each city, and ensure no more than 6 hours of travel time between destinations. The trip should last 3 days in total.", "example": "Day 1: Start in New York. Visit the Metropolitan Museum of Art in the morning. Travel to Philadelphia in the afternoon (2-hour train ride). Visit the Philadelphia Museum of Art. Stay overnight in Philadelphia. Day 2: Visit the Liberty Bell in the morning. Travel to Boston in the afternoon (5-hour train ride). Visit the Museum of Fine Arts. Stay overnight in Boston. Day 3: Visit the Boston Tea Party Ships and Museum in the morning. Return to New York in the afternoon (4-hour train ride)."},
            "2": {"destinations": ["San Francisco", "Los Angeles", "Las Vegas"], "constraints": "The trip should start in Los Angeles, include at least one famous landmark visit in each city, and ensure no more than 8 hours of travel time between destinations. The trip should last 4 days in total.", "example": "Day 1: Start in Los Angeles. Visit the Hollywood Walk of Fame in the morning. Travel to Las Vegas in the afternoon (4-hour drive). Visit the Las Vegas Strip. Stay overnight in Las Vegas. Day 2: Visit the Hoover Dam in the morning. Travel to San Francisco in the afternoon (8-hour drive). Visit the Golden Gate Bridge. Stay overnight in San Francisco. Day 3: Visit Alcatraz Island in the morning. Explore Fisherman’s Wharf in the afternoon. Stay overnight in San Francisco. Day 4: Return to Los Angeles in the morning (8-hour drive)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a detailed step-by-step travel itinerary based on the following destinations and constraints: Destinations: {', '.join(t['destinations'])}. Constraints: {t['constraints']}. Ensure that the itinerary is coherent, logically ordered, and adheres to the given constraints. Provide the itinerary in a day-by-day format, clearly indicating the activities and travel plans for each day. Submit your itinerary as a plain text string in the following format:\n\nDay 1: [Activities and travel plans for Day 1]\nDay 2: [Activities and travel plans for Day 2]\n...\nExample: {t['example']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The itinerary should cover all specified destinations.", "The itinerary should adhere to the given constraints.", "The itinerary should be logically ordered and coherent.", "The itinerary should be detailed and complete."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
