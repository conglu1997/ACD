class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "language_feature": "Grammatical gender",
                "cognitive_domain": "Object categorization",
                "decision_making_scenario": "Product design and marketing"
            },
            "2": {
                "language_feature": "Future tense",
                "cognitive_domain": "Time perception and planning",
                "decision_making_scenario": "Financial investment strategies"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes the effects of linguistic relativity on cognitive processes and decision-making across different language structures. Your system should focus on the following scenario:

Language Feature: {t['language_feature']}
Cognitive Domain: {t['cognitive_domain']}
Decision-Making Scenario: {t['decision_making_scenario']}

Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the concept of linguistic relativity and its relevance to AI language models.
   b) Describe how the specified language feature might influence cognition in the given domain.
   c) Discuss potential implications for decision-making in the specified scenario.
   d) Propose a hypothesis about how an AI system trained on languages with different structures might exhibit varied behaviors or biases.

2. AI System Architecture (300-350 words):
   a) Design an AI system architecture that can simulate the effects of linguistic relativity.
   b) Explain how your system incorporates the specified language feature in its language processing and generation.
   c) Describe how your system models the influence of language on cognitive processes in the given domain.
   d) Detail how your system simulates decision-making in the specified scenario.
   e) Include a diagram or flowchart of your system architecture (describe it in words).

3. Simulation and Analysis Process (250-300 words):
   a) Describe how your AI system would simulate cognitive processes across different language structures.
   b) Explain the metrics or methods your system would use to analyze the effects of linguistic relativity.
   c) Propose an experiment design to test your hypothesis about language influence on AI behavior.
   d) Discuss how you would control for confounding variables in your simulation.

4. Potential Applications and Implications (200-250 words):
   a) Suggest practical applications of your AI system in fields such as cross-cultural communication, language education, or AI ethics.
   b) Discuss potential implications of your findings for the development of multilingual AI systems.
   c) Consider how insights from your system might inform our understanding of human cognition and decision-making.

5. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of simulating linguistic relativity in AI systems.
   b) Address potential biases or limitations in your approach.
   c) Propose guidelines for responsible development and use of AI systems that model linguistic influences on cognition.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your AI system.
   b) Propose a research question that could further explore the intersection of linguistic relativity, cognitive science, and AI.

Ensure your response demonstrates a deep understanding of linguistic theory, cognitive science, and AI language models. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of linguistic relativity and its potential effects on AI language models.",
            "The AI system architecture is well-designed and clearly explains how it incorporates the specified language feature and models its influence on cognition and decision-making.",
            "The simulation and analysis process is well-explained, with appropriate metrics and experimental design to test the hypothesis.",
            "The response discusses practical applications and implications of the AI system, showing creativity and insight.",
            "Ethical considerations are thoughtfully addressed, including potential biases and guidelines for responsible development.",
            "Future research directions are proposed that show a deep understanding of the field and potential for further exploration.",
            "The response is well-structured, following the specified format and word count requirements.",
            "The writing demonstrates interdisciplinary knowledge integration and creative problem-solving throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
