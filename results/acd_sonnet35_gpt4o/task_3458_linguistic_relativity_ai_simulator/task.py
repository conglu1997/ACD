import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        programming_languages = [
            ("Lisp", "Object-oriented"),
            ("Prolog", "Imperative"),
            ("Haskell", "Procedural"),
            ("Forth", "Functional")
        ]
        cognitive_tasks = [
            "spatial reasoning",
            "temporal perception",
            "categorization",
            "problem-solving"
        ]
        return {
            "1": {"lang_pair": random.choice(programming_languages), "cognitive_task": random.choice(cognitive_tasks)},
            "2": {"lang_pair": random.choice(programming_languages), "cognitive_task": random.choice(cognitive_tasks)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        lang1, lang2 = t['lang_pair']
        cognitive_task = t['cognitive_task']
        return f"""Design an AI system that simulates and analyzes the effects of linguistic relativity on artificial cognitive processes, using {lang1} and {lang2} programming paradigms as proxies for natural languages. Focus on the cognitive task of {cognitive_task}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the concept of linguistic relativity and its relevance to AI systems.
   b) Describe how programming paradigms can serve as proxies for natural languages in this context.
   c) Discuss the potential effects of different programming paradigms on artificial cognitive processes, particularly {cognitive_task}.

2. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for simulating linguistic relativity effects.
   b) Explain how your system implements and compares cognitive processes in {lang1} and {lang2} paradigms.
   c) Detail how the system measures and analyzes differences in {cognitive_task} performance between the two paradigms.
   d) Provide a visual representation of your system architecture (describe it textually).

3. Simulation Process (250-300 words):
   a) Outline the steps your system takes to simulate {cognitive_task} in both {lang1} and {lang2} paradigms.
   b) Explain how you control for factors other than the programming paradigm that might affect performance.
   c) Describe how your system quantifies and compares the results of the simulations.

4. Analysis and Interpretation (200-250 words):
   a) Propose methods for analyzing the simulation results to identify linguistic relativity effects.
   b) Discuss how you would differentiate between effects due to linguistic relativity and those due to other factors.
   c) Explain how your system would generate hypotheses about the relationship between programming paradigms and cognitive processes.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of simulating linguistic relativity in AI systems.
   b) Address limitations of using programming paradigms as proxies for natural languages.
   c) Propose guidelines for the responsible development and use of such simulations in cognitive science and AI research.

6. Future Directions and Implications (150-200 words):
   a) Suggest potential applications of your system in AI development, cognitive science, or programming language design.
   b) Propose an experiment to validate the findings of your simulation in human programmers.
   c) Discuss the broader implications of your research for our understanding of the relationship between language, thought, and artificial cognition.

Ensure your response demonstrates a deep understanding of linguistic relativity, programming paradigms, cognitive science, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the simulation of linguistic relativity effects using {t['lang_pair'][0]} and {t['lang_pair'][1]} programming paradigms as proxies for natural languages.",
            f"The system design must focus on the cognitive task of {t['cognitive_task']}.",
            "The theoretical framework must clearly explain linguistic relativity and its relevance to AI systems.",
            "The system architecture must be clearly described, including how it implements and compares cognitive processes in the two programming paradigms.",
            "The simulation process must be well-defined, including steps to control for non-linguistic factors.",
            "The analysis and interpretation methods must be clearly explained, including how to differentiate linguistic relativity effects from other factors.",
            "Ethical considerations and limitations of the approach must be discussed, with proposed guidelines for responsible use.",
            "Future directions and implications of the research must be suggested, including potential applications and experiments.",
            "The response must demonstrate interdisciplinary knowledge of linguistics, cognitive science, and AI.",
            "The approach must be innovative while maintaining scientific plausibility.",
            "The response must be well-formatted with clear headings and be between 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
