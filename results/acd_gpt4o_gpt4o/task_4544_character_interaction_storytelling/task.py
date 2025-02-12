class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "characters": [
                    {"name": "Alice", "traits": "curious, brave"},
                    {"name": "Bob", "traits": "cautious, intelligent"}
                ],
                "scenario": "Alice and Bob find themselves lost in a mysterious forest."
            },
            "2": {
                "characters": [
                    {"name": "Luna", "traits": "energetic, optimistic"},
                    {"name": "Max", "traits": "calm, thoughtful"}
                ],
                "scenario": "Luna and Max are tasked with solving a puzzle to unlock a hidden treasure."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is twofold: first, generate a story based on the given character descriptions and scenario, and second, provide an analysis of the character development and interactions throughout the story.\n\nCharacters: {t['characters']}\nScenario: {t['scenario']}\n\nGuidelines for the Story:\n1. The story should be at least 300 words long.\n2. Ensure that the characters' traits are evident in their actions and dialogue.\n3. The story should be coherent and reflect the given scenario.\n\nGuidelines for the Analysis:\n1. Discuss how the characters develop throughout the story.\n2. Explain how the interactions between the characters drive the narrative forward.\n3. Provide your response in plain text format.\n\nExample Response:\nStory:\n  Alice and Bob wandered through the dense forest, the trees looming over them like ancient guardians. Alice, ever curious, led the way with a determined stride, her eyes constantly scanning for any signs of a path. Bob, on the other hand, was more cautious, his mind racing with possible dangers lurking in the shadows...\n\nAnalysis:\n  Throughout the story, Alice's bravery and curiosity are evident as she takes the lead and explores the forest. Bob's cautious nature and intelligence are shown through his careful observations and suggestions for safety. Their interactions, such as Alice encouraging Bob to be more adventurous and Bob reminding Alice to be cautious, help to balance their personalities and drive the narrative forward as they navigate the mysterious forest together.\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story is at least 300 words long.",
            "The characters' traits are evident in their actions and dialogue.",
            "The story is coherent and reflects the given scenario.",
            "The analysis discusses how the characters develop throughout the story.",
            "The analysis explains how the interactions between the characters drive the narrative forward."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
