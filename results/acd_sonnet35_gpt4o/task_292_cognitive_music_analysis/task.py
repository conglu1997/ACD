import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_principles = [
            "Fibonacci sequence",
            "Golden ratio",
            "Prime number intervals",
            "Fractal patterns"
        ]
        cognitive_aspects = [
            "Working memory",
            "Attention span",
            "Emotional regulation",
            "Spatial reasoning"
        ]
        return {
            "1": {
                "principle": random.choice(mathematical_principles),
                "cognitive_aspect": random.choice(cognitive_aspects)
            },
            "2": {
                "principle": random.choice(mathematical_principles),
                "cognitive_aspect": random.choice(cognitive_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Compose a short musical piece based on the {t['principle']} and analyze its potential effects on {t['cognitive_aspect']}. Your response should include:\n\n" \
               f"1. Musical Composition (150-200 words):\n" \
               f"   - Describe how you incorporated the {t['principle']} into your composition.\n" \
               f"   - Explain the structure, rhythm, and harmony of your piece.\n" \
               f"   - Provide a brief musical notation or representation of a key section.\n\n" \
               f"2. Cognitive Analysis (200-250 words):\n" \
               f"   - Analyze how your composition might affect {t['cognitive_aspect']}.\n" \
               f"   - Explain the theoretical basis for your analysis, citing relevant research if possible.\n" \
               f"   - Discuss potential variations in cognitive effects based on listener characteristics (e.g., age, musical training).\n\n" \
               f"3. Experimental Design (200-250 words):\n" \
               f"   - Propose an experiment to test the effects of your composition on {t['cognitive_aspect']}.\n" \
               f"   - Describe the methodology, including participant selection, experimental procedure, and measurement techniques.\n" \
               f"   - Discuss potential confounding variables and how you would control for them.\n\n" \
               f"4. Broader Implications (100-150 words):\n" \
               f"   - Discuss the potential applications of your findings in fields such as education, therapy, or cognitive enhancement.\n" \
               f"   - Speculate on how this type of music-cognition research could influence future developments in AI or human-computer interaction.\n\n" \
               f"Ensure your response demonstrates a deep understanding of music theory, cognitive science, and experimental design. Be creative in your composition and analysis while maintaining scientific rigor."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear description of a musical composition incorporating the {t['principle']}.",
            f"The cognitive analysis provides a well-reasoned explanation of how the composition might affect {t['cognitive_aspect']}.",
            "The experimental design is scientifically sound and appropriate for testing the proposed cognitive effects.",
            "The response demonstrates interdisciplinary knowledge of music theory, cognitive science, and experimental methods.",
            "The broader implications discussion is insightful and considers multiple fields of application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
