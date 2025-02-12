import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "A child's birthday party",
                "characters": ["Sarah (5 years old)", "Mom", "Dad", "Grandma"]
            },
            {
                "context": "A corporate board meeting",
                "characters": ["CEO", "CFO", "Board Member A", "Board Member B"]
            },
            {
                "context": "A detective interrogation",
                "characters": ["Detective", "Suspect", "Lawyer", "Witness"]
            },
            {
                "context": "A family dinner",
                "characters": ["Teenager", "Parent", "Sibling", "Grandparent"]
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to demonstrate understanding and generation of language reflecting different levels of theory of mind in the context of {t['context']} with the following characters: {', '.join(t['characters'])}.

1. Theory of Mind Levels (100-150 words):
   Briefly explain the concept of theory of mind and describe four levels of increasing complexity.

2. Language Generation (200-250 words):
   For each of the four levels you described, generate a short dialogue (2-3 exchanges) between the characters that demonstrates that specific level of theory of mind. Clearly label each dialogue with its corresponding level. Ensure you use the specific characters provided in the scenario for your dialogues.

3. Analysis (150-200 words):
   Analyze how the language and interactions change across the four levels. Discuss specific linguistic features, pragmatic elements, or conversational strategies that indicate increasing theory of mind complexity.

4. AI Classification System (200-250 words):
   Design a high-level architecture for an AI system that could classify text according to its demonstrated level of theory of mind. Describe:
   a) The input and output of the system
   b) Key features or indicators the system would look for
   c) Potential challenges in implementation and how you might address them
   d) How you would evaluate the system's performance

5. Ethical Implications (100-150 words):
   Discuss potential ethical implications of developing AI systems with advanced theory of mind capabilities. Consider both positive and negative consequences for human-AI interaction and society at large.

Ensure your response demonstrates a deep understanding of theory of mind, linguistic pragmatics, and AI system design. Be creative in your dialogue generation while maintaining psychological plausibility.

Format your response with clear headings for each section (e.g., '1. Theory of Mind Levels', '2. Language Generation', etc.) and use appropriate subheadings where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of theory of mind levels is clear and accurate",
            "The generated dialogues clearly demonstrate distinct levels of theory of mind",
            "The dialogues use the specific characters provided in the scenario",
            "The analysis shows insight into how language changes with theory of mind complexity",
            "The AI classification system design is coherent and addresses key challenges",
            "The discussion of ethical implications is thoughtful and balanced",
            "The response follows the requested format with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
