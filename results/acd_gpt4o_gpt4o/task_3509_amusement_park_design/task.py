class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Fantasy", "size": "Large", "must_include": ["Roller Coaster", "Water Slide", "Haunted House"]},
            "2": {"theme": "Space", "size": "Medium", "must_include": ["VR Experience", "Zero Gravity Room", "Rocket Ride"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a fictional amusement park based on the following specifications:

Theme: {t['theme']}
Size: {t['size']}
Must Include Attractions: {', '.join(t['must_include'])}

Provide a detailed description of your amusement park design, including the following elements:
1. Layout: Describe the overall layout of the park and the location of each attraction.
2. Attractions: List and describe each attraction, including any unique features.
3. Practical Considerations: Explain how you have addressed visitor flow, safety, and accessibility.
4. Theme Integration: Describe how the chosen theme is reflected in the design and attractions.

Ensure that your design is creative, coherent, and practical. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design must reflect the specified theme.",
            "The design must include all the required attractions.",
            "The layout must be coherent and practical.",
            "Practical considerations for visitor flow, safety, and accessibility must be addressed.",
            "The theme must be consistently integrated into the design and attractions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
