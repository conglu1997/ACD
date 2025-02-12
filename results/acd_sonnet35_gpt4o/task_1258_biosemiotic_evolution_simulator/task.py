class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"environment": "deep ocean bioluminescent ecosystem", "constraint": "limited energy availability", "evolutionary_pressure": "predator-prey coevolution"},
            "2": {"environment": "subterranean fungal network", "constraint": "limited spatial range", "evolutionary_pressure": "resource competition"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical biological communication system based on biosemiotic principles for organisms living in the following scenario:

Environment: {t['environment']}
Constraint: {t['constraint']}
Evolutionary Pressure: {t['evolutionary_pressure']}

Your task is to create a detailed proposal for this biological communication system and analyze its implications. Include the following sections in your response:

1. System Design (250-300 words):
   a) Describe the key features of your biosemiotic communication system.
   b) Explain how it is adapted to the given environment and constraint.
   c) Detail at least one novel biological mechanism that addresses the evolutionary pressure.
   d) Discuss how your system incorporates key biosemiotic concepts (e.g., umwelt, semiosis).

2. Information Theory Analysis (200-250 words):
   a) Apply specific concepts from information theory to analyze your biological communication system.
   b) Explain how these concepts relate to the efficiency and reliability of the system.
   c) Provide at least one equation or formal representation of your analysis.

3. Evolutionary Dynamics (200-250 words):
   a) Describe how your communication system might evolve over time.
   b) Discuss potential evolutionary trade-offs in your system.
   c) Propose a mechanism for how beneficial traits related to biosemiotic processes might be selected for.

4. Simulation Model (200-250 words):
   a) Develop a conceptual model for simulating the evolution of your biosemiotic system.
   b) Explain the key variables and parameters in your model.
   c) Describe what insights could be gained from running such a simulation.

5. Applications and Implications (150-200 words):
   a) Propose potential applications of your biosemiotic system design in fields such as artificial life or synthetic biology.
   b) Discuss the broader implications of your system for our understanding of biological communication and evolution.
   c) Suggest how insights from your system might inform the development of new technologies.

Ensure your response demonstrates a deep understanding of biosemiotics, information theory, and evolutionary biology. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biosemiotics, information theory, and evolutionary biology concepts.",
            "The proposed biological communication system is novel, scientifically plausible, and well-adapted to the given environment and constraints.",
            "The information theory analysis includes relevant concepts and at least one equation or formal representation.",
            "The evolutionary dynamics discussion includes plausible mechanisms and trade-offs.",
            "The simulation model concept is well-developed and could provide meaningful insights.",
            "The applications and implications section proposes innovative ideas while maintaining scientific credibility.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
