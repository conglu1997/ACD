import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "concept": "quantum superposition",
                "definition": "A quantum state where a particle exists in multiple states simultaneously until observed."
            },
            {
                "concept": "quantum entanglement",
                "definition": "A phenomenon where particles become interconnected and the quantum state of each particle cannot be described independently."
            }
        ]
        return {
            "1": random.choice(quantum_concepts),
            "2": random.choice(quantum_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language translation system and use it to translate the quantum computing concept of {t['concept']} into everyday analogies. Your response should include:

1. Quantum-Inspired Translation System Design (300-350 words):
   a) Describe the key components of your quantum-inspired translation system.
   b) Explain how it incorporates quantum principles (e.g., superposition, entanglement) in its translation process.
   c) Discuss how your system differs from classical machine translation approaches.
   d) Include a high-level diagram or pseudocode representing the system's workflow (describe it textually).

2. Quantum Concept Explanation (150-200 words):
   a) Provide a clear and concise explanation of {t['concept']}.
   b) Discuss its significance in quantum computing.

3. Everyday Analogies (250-300 words):
   a) Use your quantum-inspired translation system to generate three distinct analogies for {t['concept']} using everyday scenarios or objects.
   b) For each analogy, explain how it captures the essence of the quantum concept.
   c) Discuss any limitations or potential misunderstandings each analogy might introduce.

4. Linguistic Analysis (200-250 words):
   a) Analyze how your quantum-inspired system translates complex scientific language into accessible analogies.
   b) Discuss any patterns or techniques your system employs to maintain accuracy while increasing understandability.
   c) Compare the linguistic features of the original quantum concept description with those of your generated analogies.

5. Potential Applications and Implications (150-200 words):
   a) Propose two potential applications of your quantum-inspired translation system beyond explaining quantum concepts.
   b) Discuss the implications of such a system for science communication and education.
   c) Address any ethical considerations related to simplifying complex scientific ideas.

Ensure your response demonstrates a deep understanding of both quantum computing principles and linguistic translation techniques. Be creative in your approach while maintaining scientific accuracy. Use appropriate quantum computing terminology throughout your response and provide explanations where necessary.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1050-1300 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the quantum concept of {t['concept']}.",
            "The quantum-inspired translation system design is innovative and incorporates quantum principles.",
            "The everyday analogies effectively capture the essence of the quantum concept while being accessible to a general audience.",
            "The linguistic analysis demonstrates a deep understanding of the translation process and its challenges.",
            "The potential applications and implications are thoughtfully considered and relevant.",
            "The response uses appropriate quantum computing terminology throughout.",
            "The total word count is between 1050-1300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
