import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_types = [
            "episodic memory",
            "semantic memory",
            "procedural memory",
            "working memory"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        return {
            "1": {
                "memory_type": random.choice(memory_types),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "memory_type": random.choice(memory_types),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-enhanced AI system for augmenting human {t['memory_type']}, utilizing the quantum principle of {t['quantum_principle']}. Then, analyze its potential impacts on cognition and society. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-enhanced AI system for memory augmentation.
   b) Explain how it integrates quantum computing principles with AI and neuroscience concepts.
   c) Detail how the system interfaces with the human brain to enhance {t['memory_type']}.
   d) Include a diagram or flowchart of your system architecture using ASCII art or Unicode characters (max 20 lines by 80 characters).

2. Quantum-AI Integration (250-300 words):
   a) Explain how {t['quantum_principle']} is applied in your system to enhance memory processes.
   b) Describe the AI algorithms or models used and how they leverage quantum computing.
   c) Discuss any novel approaches to quantum-AI integration in your design.

3. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your system's approach to enhancing {t['memory_type']}.
   b) Discuss how your system interacts with relevant brain structures and processes.
   c) Address potential challenges in interfacing quantum-AI systems with biological neural networks.

4. Enhancement Mechanisms (200-250 words):
   a) Detail the specific mechanisms by which your system enhances {t['memory_type']}.
   b) Provide examples of how these enhancements might manifest in everyday life.
   c) Discuss potential limitations or side effects of these enhancement mechanisms.

5. Cognitive Impact Analysis (150-200 words):
   a) Analyze how your system might affect overall cognitive function and learning processes.
   b) Discuss potential long-term impacts on brain plasticity and natural memory functions.
   c) Consider how enhancing {t['memory_type']} might influence other cognitive domains.

6. Societal Implications (150-200 words):
   a) Explore the potential societal impacts of widespread adoption of your memory enhancement system.
   b) Discuss ethical considerations, including issues of fairness, access, and potential misuse.
   c) Propose guidelines for responsible development and use of such technology.

7. Future Research Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Propose a research question that could further explore the intersection of quantum computing, AI, and cognitive enhancement.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and cognitive neuroscience. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing, artificial intelligence, and cognitive neuroscience.",
            "The proposed system effectively integrates quantum principles, AI algorithms, and neuroscientific concepts.",
            "The explanation of how the system enhances the specified memory type is scientifically plausible and innovative.",
            "The analysis of cognitive and societal impacts is thorough and well-reasoned.",
            "The response shows creativity in problem-solving while maintaining scientific accuracy.",
            "The proposed future research directions are insightful and relevant to the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
