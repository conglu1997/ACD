import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy", "sadness", "anger", "fear", "disgust",
            "surprise", "trust", "anticipation", "love", "jealousy"
        ]
        logical_structures = [
            "syllogism", "conditional statement", "disjunctive syllogism",
            "modus ponens", "modus tollens"
        ]
        conflict_scenarios = [
            "workplace disagreement", "family dispute", "romantic relationship issue",
            "friendship conflict", "cultural misunderstanding"
        ]
        
        tasks = {}
        for i in range(2):
            emotion = random.choice(emotions)
            structure = random.choice(logical_structures)
            scenario = random.choice(conflict_scenarios)
            tasks[str(i+1)] = {
                "emotion": emotion,
                "logical_structure": structure,
                "conflict_scenario": scenario
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates the emotional state of {t['emotion']} into the logical structure of a {t['logical_structure']}. Then, apply this system to analyze and propose a solution for a {t['conflict_scenario']}. Your response should include:

1. System Design (250-300 words):
   a) Describe your system for translating {t['emotion']} into a {t['logical_structure']}.
   b) Explain how your system captures the nuances of the emotion.
   c) Provide an example of how a specific aspect of {t['emotion']} would be represented in your logical structure.
   d) Discuss any challenges in this translation and how you addressed them.

2. Conflict Analysis (200-250 words):
   a) Briefly describe a specific {t['conflict_scenario']}.
   b) Apply your emotion-logic translation system to analyze this conflict.
   c) Explain how your system reveals new insights about the conflict.

3. Solution Proposal (200-250 words):
   a) Using your emotion-logic translation, propose a solution to the conflict.
   b) Explain how your solution addresses the emotional aspects revealed by your system.
   c) Discuss potential challenges in implementing this solution.

4. Comparative Analysis (150-200 words):
   a) Compare your emotion-logic approach to traditional conflict resolution methods.
   b) Discuss potential advantages and limitations of your approach.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues in translating emotions to logical structures.
   b) Propose guidelines for the responsible use of such a system.

6. Future Applications (100-150 words):
   a) Suggest two other fields where your emotion-logic translation system could be applied.
   b) Briefly explain how it might be adapted for these applications.

Ensure your response demonstrates a deep understanding of both emotional states and logical structures. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from psychology, logic, and conflict resolution fields.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed system design for translating {t['emotion']} into a {t['logical_structure']}.",
            f"The system should be applied to analyze and solve a {t['conflict_scenario']}.",
            "The response should demonstrate a deep understanding of both emotional states and logical structures.",
            "The proposed solution should address the emotional aspects revealed by the translation system.",
            "The response should include a comparative analysis with traditional conflict resolution methods.",
            "Ethical considerations and future applications should be discussed.",
            "The response should be well-organized with clear headings for each section.",
            "The response should be creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
