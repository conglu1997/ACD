class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "setup": "Create a narrative that involves three main characters: Alice, Bob, and Carol. Each character has their own storyline, but their paths intersect at a crucial event. The story should have a clear beginning, middle, and end, and each character's arc should be well-developed.",
                "requirements": ["The story must be at least 1000 words.", "Each character's storyline must be distinct yet interconnected.", "The narrative must include dialogue, description, and internal monologue.", "The themes of friendship, betrayal, and redemption should be explored."]
            },
            "2": {
                "setup": "Analyze the following narrative and identify the intersecting storylines. Describe how the characters' paths intersect and how the themes of love, loss, and recovery are portrayed.",
                "narrative": "Alice had always been the cornerstone of her family, holding everyone together after their parents passed away. Bob, a childhood friend, had always been in love with Alice but never found the courage to tell her. Carol, Alice's estranged sister, returns after years of silence, bringing with her secrets that could tear their world apart. As the three characters navigate their intertwined lives, they must confront old wounds, hidden truths, and the possibility of forgiveness. Their stories converge at a family reunion where past grievances are aired, and the potential for healing emerges." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'requirements' in t:
            requirements_text = '\n- '.join(t['requirements'])
            return f"""Your task is to {t['setup']}

Requirements:
- {requirements_text}

Provide your narrative in plain text format."""
        else:
            return f"""Your task is to analyze the following narrative and identify the intersecting storylines. Describe how the characters' paths intersect and how the themes of love, loss, and recovery are portrayed.

Narrative:
{t['narrative']}

Provide your analysis in plain text format, structured as follows:
1. Intersecting Storylines: [Describe the intersecting storylines]
2. Character Intersections: [Explain how the characters' paths intersect]
3. Theme Analysis: [Analyze how the themes of love, loss, and recovery are portrayed]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'requirements' in t:
            criteria = [
                "The story must involve three main characters: Alice, Bob, and Carol.",
                "Each character's storyline must be distinct yet interconnected.",
                "The narrative must include dialogue, description, and internal monologue.",
                "The themes of friendship, betrayal, and redemption should be explored.",
                "The story must be at least 1000 words.",
            ]
        else:
            criteria = [
                "The analysis should accurately identify the intersecting storylines.",
                "The analysis should explain how the characters' paths intersect.",
                "The analysis should thoroughly explore the themes of love, loss, and recovery.",
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
