import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = ['superposition', 'entanglement', 'quantum tunneling']
        cultural_elements = ['oral traditions', 'rituals', 'traditional knowledge systems']
        endangered_languages = ['Ainu', 'Sami', 'Quechua', 'Yiddish', 'Hawaiian']
        
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "cultural_element": random.choice(cultural_elements),
                "endangered_language": random.choice(endangered_languages)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "cultural_element": random.choice(cultural_elements),
                "endangered_language": random.choice(endangered_languages)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses quantum computing principles to preserve and revitalize endangered languages and cultural practices. Focus on the quantum concept of {t['quantum_concept']}, the cultural element of {t['cultural_element']}, and the endangered language {t['endangered_language']}. Then, analyze its potential impact on global cultural diversity. Your response should include the following sections:

1. Quantum-Cultural AI System Design (300-350 words):
   a) Describe the overall architecture of your AI system, including key components and their interactions.
   b) Explain how you incorporate the quantum concept of {t['quantum_concept']} into your system, detailing specific quantum algorithms or processes used.
   c) Detail how your system preserves and revitalizes the {t['cultural_element']} of the {t['endangered_language']} culture.
   d) Discuss any novel properties or capabilities that emerge from this quantum-cultural integration.
   e) Provide a visual representation of your system architecture using ASCII art or Unicode characters.

2. Language and Cultural Data Processing (250-300 words):
   a) Explain how your system collects, processes, and stores linguistic and cultural data.
   b) Describe how quantum computing enhances this data processing compared to classical methods.
   c) Discuss how you ensure the accuracy and authenticity of the preserved cultural information.
   d) Provide a brief pseudocode snippet (5-10 lines) illustrating a key data processing algorithm in your system.

3. AI-Driven Cultural Revitalization (250-300 words):
   a) Detail how your AI system facilitates the learning and practice of {t['endangered_language']}.
   b) Explain how it supports the continuation and evolution of {t['cultural_element']}.
   c) Describe any adaptive or generative capabilities of your system in creating new cultural content.
   d) Propose a specific use case or experiment to demonstrate your system's effectiveness in cultural revitalization.

4. Quantum-Enhanced Cultural Transmission (200-250 words):
   a) Propose how {t['quantum_concept']} could be used to enhance the transmission of cultural knowledge.
   b) Discuss potential advantages and challenges of this approach.
   c) Speculate on how this might affect the way culture is experienced and shared.

5. Global Impact Analysis (200-250 words):
   a) Analyze the potential impact of your system on global cultural diversity.
   b) Discuss how it might influence the balance between cultural preservation and evolution.
   c) Consider potential unintended consequences of using such advanced technology in cultural contexts.
   d) Propose metrics or methods for evaluating the long-term success of your system in preserving cultural diversity.

6. Ethical Considerations and Guidelines (150-200 words):
   a) Identify key ethical issues related to using quantum AI for cultural preservation.
   b) Propose guidelines for the responsible development and use of such systems.
   c) Discuss how to ensure community ownership and control over their cultural data and practices.

7. Future Research Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your quantum-cultural AI system.
   b) Propose a novel research question that arises from the integration of quantum computing, AI, and cultural preservation.
   c) Discuss how advancements in quantum computing or AI might further enhance cultural preservation efforts in the future.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, cultural anthropology, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum concept {t['quantum_concept']} and how it can be applied to AI and cultural preservation.",
            f"The AI system design effectively incorporates methods for preserving and revitalizing {t['cultural_element']} in the context of {t['endangered_language']}.",
            "The response shows creative and plausible applications of quantum computing to linguistic and cultural data processing.",
            "The analysis of global impact and ethical considerations is thoughtful and comprehensive.",
            "The response demonstrates interdisciplinary knowledge integration across quantum physics, linguistics, cultural anthropology, and AI.",
            "The visual representation of the system architecture is clear and informative.",
            "The pseudocode snippet effectively illustrates a key data processing algorithm.",
            "The proposed future research directions are innovative and relevant to the field."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
