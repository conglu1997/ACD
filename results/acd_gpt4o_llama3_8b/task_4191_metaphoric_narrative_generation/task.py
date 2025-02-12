class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "metaphors": ["time is a thief", "a storm in a teacup", "burning the midnight oil"],
                "idioms": ["barking up the wrong tree", "spill the beans", "hit the nail on the head"]
            },
            "2": {
                "metaphors": ["a diamond in the rough", "a fish out of water", "the world is a stage"],
                "idioms": ["break the ice", "under the weather", "the ball is in your court"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a creative narrative that incorporates the following metaphors and idioms seamlessly. Your narrative should be coherent, imaginative, and make proper use of each metaphor and idiom. Ensure that the metaphors and idioms fit naturally within the context of the story.

Metaphors:
- {', '.join(t['metaphors'])}

Idioms:
- {', '.join(t['idioms'])}

Example response format:
Once upon a time, in a small village, there lived a man who believed that 'time is a thief'. He spent his days worrying about 'a storm in a teacup' and often found himself 'burning the midnight oil'. One day, he realized he had been 'barking up the wrong tree' all along. He decided to 'spill the beans' to his friends, hoping to 'hit the nail on the head' and find a solution to his worries."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should be coherent and imaginative.",
            "Each metaphor and idiom should be used correctly and fit naturally within the context of the story.",
            "The submission should incorporate all provided metaphors and idioms."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
