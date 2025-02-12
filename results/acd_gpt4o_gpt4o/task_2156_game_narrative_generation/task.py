class TaskFamily:
    import random
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'genre': 'fantasy',
                'main_character': 'a young wizard',
                'main_quest': 'retrieve a stolen magical artifact',
                'world_elements': ['enchanted forest', 'ancient ruins', 'mysterious cave'],
                'expected_result': 'A detailed narrative including characters, plot, and world-building elements.'
            },
            '2': {
                'genre': 'sci-fi',
                'main_character': 'an intergalactic bounty hunter',
                'main_quest': 'capture a notorious space pirate',
                'world_elements': ['abandoned space station', 'alien marketplace', 'hidden asteroid base'],
                'expected_result': 'A detailed narrative including characters, plot, and world-building elements.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed and coherent narrative for the following game scenario:

Genre: {t['genre']}
Main Character: {t['main_character']}
Main Quest: {t['main_quest']}
World Elements: {', '.join(t['world_elements'])}

Your narrative should include:
1. A clear introduction of the main character and the world they inhabit.
2. A compelling plot centered around the main quest.
3. Detailed descriptions of the world elements and how they fit into the story.
4. Engaging character interactions and development.

Ensure your narrative is creative, coherent, and well-structured. Provide your narrative in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should include a clear introduction of the main character and the world they inhabit.",
            "The narrative should have a compelling plot centered around the main quest.",
            "The narrative should include detailed descriptions of the world elements and how they fit into the story.",
            "The narrative should have engaging character interactions and development.",
            "The narrative should be creative, coherent, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
