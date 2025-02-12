import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        proverbs = [
            {
                "proverb": "Don't count your chickens before they hatch",
                "origin": "English",
                "theme": "Caution against premature optimism"
            },
            {
                "proverb": "The early bird catches the worm",
                "origin": "English",
                "theme": "Benefits of being proactive"
            },
            {
                "proverb": "A rolling stone gathers no moss",
                "origin": "Latin",
                "theme": "Consequences of constant change"
            },
            {
                "proverb": "When in Rome, do as the Romans do",
                "origin": "Medieval Latin",
                "theme": "Adapting to local customs"
            }
        ]
        
        modern_contexts = [
            "social media",
            "remote work",
            "artificial intelligence",
            "climate change",
            "digital privacy"
        ]
        
        tasks = {}
        for i in range(2):
            proverb = random.choice(proverbs)
            context = random.choice(modern_contexts)
            tasks[str(i+1)] = {
                "proverb": proverb["proverb"],
                "origin": proverb["origin"],
                "theme": proverb["theme"],
                "context": context
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following proverb and create a modern version:

Proverb: "{t['proverb']}"
Origin: {t['origin']}
Theme: {t['theme']}
Modern Context: {t['context']}

Your task:

1. Explain the meaning and cultural significance of the original proverb (2-3 sentences).

2. Analyze how the proverb's wisdom might apply to the given modern context (2-3 sentences).

3. Create a new proverb that:
   a) Maintains the spirit and theme of the original proverb
   b) Applies specifically to the given modern context
   c) Uses language and metaphors relevant to contemporary life

4. Explain your new proverb, including:
   a) How it relates to the original proverb's wisdom
   b) How it addresses the modern context
   c) The metaphors or symbols you used and why

Ensure your new proverb is concise, memorable, and captures the essence of traditional proverbs while being relevant to modern life.

Format your response as follows:

Original Proverb Analysis:
[Your explanation]

Application to Modern Context:
[Your analysis]

New Proverb:
[Your created proverb]

New Proverb Explanation:
[Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a clear explanation of the original proverb's meaning and cultural significance",
            "The analysis of the proverb's application to the modern context is thoughtful and relevant",
            "The new proverb maintains the spirit and theme of the original while applying to the modern context",
            "The new proverb uses language and metaphors relevant to contemporary life",
            "The explanation of the new proverb clearly relates it to the original wisdom and modern context",
            "The new proverb is concise, memorable, and captures the essence of traditional proverbs"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
