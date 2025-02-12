import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_pattern": "Use of hedging language and qualifiers",
                "psychological_trait": "High in neuroticism",
                "profession": "Academic researcher"
            },
            {
                "linguistic_pattern": "Frequent use of action verbs and short sentences",
                "psychological_trait": "High in extraversion",
                "profession": "Sports coach"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a detailed character profile based on the following parameters:\n\n" \
               f"1. Linguistic pattern: {t['linguistic_pattern']}\n" \
               f"2. Psychological trait: {t['psychological_trait']}\n" \
               f"3. Profession: {t['profession']}\n\n" \
               f"Your response should include:\n\n" \
               f"1. Character Profile (200-250 words):\n" \
               f"   a) Name and basic demographic information\n" \
               f"   b) Detailed personality description, emphasizing how the given psychological trait manifests\n" \
               f"   c) Explanation of how their linguistic pattern reflects their personality and profession\n" \
               f"   d) Brief background story that aligns with their profile\n\n" \
               f"2. Linguistic Analysis (150-200 words):\n" \
               f"   a) Detailed explanation of the given linguistic pattern\n" \
               f"   b) Examples of specific words, phrases, or sentence structures this character would typically use\n" \
               f"   c) Analysis of how this linguistic pattern reflects the character's psychological trait and profession\n\n" \
               f"3. Sample Dialogue (100-150 words):\n" \
               f"   Write a short dialogue (5-7 exchanges) between this character and a colleague or friend. " \
               f"   The dialogue should clearly demonstrate the character's linguistic pattern and personality.\n\n" \
               f"4. Reflection (100-150 words):\n" \
               f"   a) Discuss the challenges in creating a coherent character profile from these diverse elements\n" \
               f"   b) Reflect on how linguistic patterns can reveal or obscure aspects of personality\n" \
               f"   c) Suggest how this exercise might be valuable in fields such as writing, psychology, or AI development\n\n" \
               f"Ensure your response demonstrates a deep understanding of linguistics, psychology, and creative writing. " \
               f"Be creative while maintaining internal consistency and plausibility in your character profile. " \
               f"Your total response should be between 550-750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The character profile is detailed, coherent, and psychologically consistent.",
            "The linguistic analysis demonstrates a deep understanding of the given pattern and its relationship to personality.",
            "The sample dialogue effectively showcases the character's linguistic pattern and personality.",
            "The reflection shows insight into the task's challenges and implications.",
            "The response maintains internal consistency across all sections.",
            "The writing is creative and engaging while remaining true to the given parameters."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
