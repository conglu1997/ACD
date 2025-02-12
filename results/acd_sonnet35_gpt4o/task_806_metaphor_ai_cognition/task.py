import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphor_domains = [
            {"source": "Technology", "target": "Nature"},
            {"source": "Emotions", "target": "Weather"},
            {"source": "Time", "target": "Space"},
            {"source": "Ideas", "target": "Food"},
            {"source": "Life", "target": "Journey"}
        ]
        return {
            "1": random.choice(metaphor_domains),
            "2": random.choice(metaphor_domains)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of comprehending and generating novel metaphors, then analyze its performance in comparison to human cognition. Focus on metaphors that map concepts from the domain of {t['source']} to the domain of {t['target']}. Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for metaphor comprehension and generation.
   b) Explain how your system would process and represent metaphorical mappings between the source and target domains.
   c) Detail the algorithms or techniques your system would use to generate novel metaphors.

2. Metaphor Comprehension Process (200-250 words):
   a) Outline the steps your AI system would take to comprehend a given metaphor.
   b) Explain how the system would handle ambiguity and context in metaphor interpretation.
   c) Describe how your system would represent the understood metaphor internally.

3. Novel Metaphor Generation (200-250 words):
   a) Explain the process your AI system would use to generate a novel metaphor.
   b) Provide an example of a novel metaphor your system might generate, mapping a concept from {t['source']} to {t['target']}. Format your example as: "[Concept from {t['source']}] is [Metaphorical description using {t['target']}]."
   c) Analyze the creativity and coherence of the generated metaphor.

4. Comparative Analysis with Human Cognition (250-300 words):
   a) Compare your AI system's approach to metaphor comprehension and generation with current theories of human metaphor processing.
   b) Discuss potential similarities and differences between your AI system and human cognitive processes in metaphor understanding.
   c) Analyze the strengths and limitations of your AI system compared to human metaphor processing.

5. Evaluation and Testing (200-250 words):
   a) Propose a method to evaluate your AI system's metaphor comprehension and generation capabilities.
   b) Describe an experiment that compares your AI system's performance with human performance on metaphor tasks.
   c) Predict potential outcomes of this experiment and explain your reasoning.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the potential implications of an AI system capable of understanding and generating metaphors.
   b) Explore how this capability might influence our understanding of machine intelligence and creativity.
   c) Address any ethical concerns related to AI systems that can manipulate abstract language.

Ensure your response demonstrates a deep understanding of metaphor theory, cognitive science, and AI systems. Be creative in your approach while maintaining scientific and technological plausibility. Use clear headings for each section in your response.

Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The AI system architecture is well-designed and plausible for metaphor processing.",
            "The metaphor comprehension and generation processes are clearly explained and theoretically sound.",
            "The comparative analysis with human cognition is insightful and well-reasoned.",
            "The proposed evaluation method and experiment are appropriate and well-designed.",
            "The discussion of ethical and philosophical implications is thoughtful and comprehensive.",
            "The response demonstrates a deep understanding of metaphor theory, cognitive science, and AI systems.",
            "The overall solution is creative while maintaining scientific and technological plausibility.",
            "The novel metaphor example follows the specified format and effectively maps a concept from the source domain to the target domain.",
            "The response adheres to the specified word limit (1250-1550 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
