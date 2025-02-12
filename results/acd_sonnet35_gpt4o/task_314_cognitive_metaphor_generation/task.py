import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {"domain": "Quantum Physics", "concept": "Superposition"},
            {"domain": "Economics", "concept": "Inflation"},
            {"domain": "Psychology", "concept": "Cognitive Dissonance"},
            {"domain": "Computer Science", "concept": "Recursion"}
        ]
        return {str(i+1): domain for i, domain in enumerate(random.sample(domains, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to generate and analyze metaphors based on cognitive models of metaphor comprehension, then apply it to create metaphors for the abstract concept of {t['concept']} in the domain of {t['domain']}. Your response should include:

1. Cognitive Model Selection (150-200 words):
   a) Choose two cognitive models of metaphor comprehension (e.g., Conceptual Metaphor Theory, Structure-Mapping Theory).
   b) Briefly explain each model and its key principles.
   c) Justify your choice of these models for metaphor generation and analysis.

2. AI System Design (250-300 words):
   a) Describe the architecture of your AI system, including main components and their interactions.
   b) Explain how your system implements the chosen cognitive models.
   c) Detail the metaphor generation process, including any constraints or guidelines.
   d) Describe how your system would analyze generated metaphors according to the cognitive models.
   e) Explain how your system handles potential biases in metaphor generation.

3. Metaphor Generation (200-250 words):
   a) Use your AI system to generate three distinct metaphors for the concept of {t['concept']} in the domain of {t['domain']}.
   b) Present each metaphor in the format: "{t['concept']} is [metaphor]" followed by a brief explanation.
   c) Explain the rationale behind each generated metaphor.
   d) Discuss how each metaphor reflects principles from the chosen cognitive models.

4. Cognitive Analysis (200-250 words):
   a) Analyze one of the generated metaphors using both cognitive models.
   b) Compare and contrast the insights provided by each model.
   c) Discuss any discrepancies or complementarities between the two analyses.

5. Evaluation and Limitations (150-200 words):
   a) Propose criteria for evaluating the quality and cognitive validity of generated metaphors.
   b) Discuss potential limitations of your AI system and the chosen cognitive models.
   c) Suggest improvements or extensions to enhance metaphor generation and analysis.

Ensure your response demonstrates a deep understanding of cognitive science, creative language generation, and the chosen domain. Use appropriate terminology and provide clear explanations where necessary. The total word count for your response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive models of metaphor comprehension",
            "The AI system design is coherent and effectively implements the chosen cognitive models",
            "The generated metaphors are creative, relevant to the given concept and domain, and presented in the required format",
            "The cognitive analysis of the metaphors is insightful and accurately applies the chosen models",
            "The evaluation criteria and limitations discussion show critical thinking about the approach",
            "The response addresses potential biases in metaphor generation",
            "The response maintains scientific accuracy while demonstrating creativity in metaphor generation",
            "The response adheres to the specified word count limits for each section and overall"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
