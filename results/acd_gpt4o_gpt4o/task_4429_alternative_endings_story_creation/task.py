class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story": "Once upon a time, in a small village, there lived a kind old woman named Martha. She was loved by everyone. One day, she found a lost puppy and decided to take care of it. Over time, the puppy grew, and they became inseparable. However, as the puppy grew older, it started to show signs of illness. Martha took the puppy to the vet, but the vet couldn't find anything wrong. Despite this, the puppy's condition worsened. Martha was heartbroken and didn't know what to do. One night, she had a dream where the puppy spoke to her, telling her to visit the old oak tree at the edge of the village. She woke up determined to follow the dream's advice. When she reached the oak tree, she found a mysterious glowing stone. She took the stone home, hoping it would help the puppy. As she placed the stone near the puppy, a bright light filled the room."},
            "2": {"story": "In a bustling city, there was a young artist named Leo who struggled to make a name for himself. Despite his talent, he couldn't find a gallery willing to display his work. One day, while painting in the park, he met an elderly man who admired his work. The man introduced himself as a retired gallery owner and offered to help Leo. They worked together, and soon, Leo's paintings were displayed in a prestigious gallery. His life changed overnight, and he became a celebrated artist. However, he soon discovered that the elderly man had a hidden agenda. The man wanted Leo to create forgeries of famous paintings. Leo was torn between his newfound fame and his principles. He decided to confront the man, leading to a heated argument. The man threatened to ruin Leo's career if he didn't comply. Leo was left with a difficult choice. He considered his options carefully, knowing that his decision would affect his future."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create an alternative ending for the following story. Ensure that the new ending is coherent with the rest of the story and logically consistent. Your alternative ending should provide a satisfying conclusion to the narrative.

Story:
{t['story']}

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The alternative ending should be coherent with the rest of the story.",
            "The alternative ending should be logically consistent.",
            "The alternative ending should provide a satisfying conclusion to the narrative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
