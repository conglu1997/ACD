class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"characters": [
                {"name": "Alice", "trait": "curious", "tone": "excited"},
                {"name": "Bob", "trait": "skeptical", "tone": "calm"}
            ], "context": "Alice has discovered a mysterious old map and is showing it to Bob.", "synthetic_examples": ["Name: Carol, Trait: adventurous, Tone: enthusiastic\nName: Dave, Trait: pragmatic, Tone: neutral\nContext: Carol and Dave are planning a trip to explore an uncharted island.", "Name: Emily, Trait: worried, Tone: anxious\nName: Frank, Trait: reassuring, Tone: calm\nContext: Emily is concerned about an upcoming exam, and Frank is trying to comfort her.", "Name: Grace, Trait: determined, Tone: confident\nName: Henry, Trait: doubtful, Tone: skeptical\nContext: Grace is presenting her ambitious project idea to Henry."]},
            "2": {"characters": [
                {"name": "John", "trait": "optimistic", "tone": "cheerful"},
                {"name": "Emma", "trait": "cautious", "tone": "worried"}
            ], "context": "John and Emma are discussing their new startup idea.", "synthetic_examples": ["Name: Ian, Trait: excited, Tone: jubilant\nName: Jenna, Trait: apprehensive, Tone: nervous\nContext: Ian has just won a big prize and is sharing the news with Jenna.", "Name: Karen, Trait: hopeful, Tone: optimistic\nName: Luke, Trait: realistic, Tone: serious\nContext: Karen is discussing her dreams of becoming an artist with Luke.", "Name: Megan, Trait: frustrated, Tone: irritated\nName: Nathan, Trait: patient, Tone: understanding\nContext: Megan is upset about a recent setback at work, and Nathan is listening to her vent."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join(t.get('synthetic_examples', []))
        characters = '\n'.join([f"Name: {char['name']}, Trait: {char['trait']}, Tone: {char['tone']}" for char in t['characters']])
        return f"""Generate a fictional dialogue based on the following constraints:

Characters:
{characters}

Context: {t['context']}

Ensure that the dialogue is coherent, contextually appropriate, and each character's lines reflect their given traits and tones.

Submit your response in the following format:

Dialogue:
[Your dialogue]\n\nAdditional examples:\n{examples}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be coherent and contextually appropriate.",
            "Each character's lines should reflect their given traits and tones."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
