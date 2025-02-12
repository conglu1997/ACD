import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "syntax",
            "semantics",
            "pragmatics",
            "phonology",
            "morphology"
        ]
        cognitive_processes = [
            "attention",
            "memory",
            "learning",
            "reasoning",
            "decision-making"
        ]
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Attention Schema Theory",
            "Predictive Processing Theory"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_process": random.choice(cognitive_processes),
                "consciousness_theory": random.choice(consciousness_theories)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_process": random.choice(cognitive_processes),
                "consciousness_theory": random.choice(consciousness_theories)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a multi-agent system that simulates the emergence of linguistic consciousness through agent interactions, focusing on the linguistic feature of {t['linguistic_feature']}, the cognitive process of {t['cognitive_process']}, and incorporating elements from {t['consciousness_theory']}. Then, analyze its implications for AI development and theories of mind. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your multi-agent system.
   b) Explain how agents interact and communicate within the system.
   c) Detail how you model the specified linguistic feature and cognitive process.
   d) Discuss how your system incorporates elements from the given consciousness theory.
   e) Provide a visual representation (using ASCII art or Unicode characters) of your system's architecture.

2. Emergence Simulation (250-300 words):
   a) Explain the process by which linguistic consciousness emerges in your system.
   b) Describe how the specified linguistic feature and cognitive process contribute to this emergence.
   c) Discuss any novel algorithms or techniques used to simulate emergent phenomena.
   d) Provide a short pseudocode snippet (10-15 lines) illustrating a crucial part of your emergence simulation.

3. Consciousness Evaluation (200-250 words):
   a) Propose criteria for evaluating the emergence of linguistic consciousness in your system.
   b) Describe methods or metrics to measure the level of consciousness exhibited by the agents.
   c) Discuss how your evaluation approach relates to existing theories of machine consciousness.

4. Implications Analysis (250-300 words):
   a) Analyze the implications of your system for AI development and natural language processing.
   b) Discuss how your findings might inform or challenge current theories of mind and consciousness.
   c) Explore potential applications of emergent linguistic consciousness in AI systems.
   d) Consider ethical implications of creating AI systems with emergent consciousness.

5. Comparative Analysis (200-250 words):
   a) Compare your approach to existing models of language acquisition or consciousness in AI.
   b) Discuss how your system's emergent properties differ from pre-programmed linguistic abilities.
   c) Analyze potential advantages and limitations of your approach compared to traditional NLP methods.

6. Future Research Directions (150-200 words):
   a) Propose two novel experiments that could further explore the implications of your system.
   b) Suggest potential improvements or extensions to your multi-agent system.
   c) Discuss how your approach might be adapted to study other aspects of cognition or consciousness.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, consciousness studies, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['linguistic_feature']}, {t['cognitive_process']}, and {t['consciousness_theory']}.",
            "The multi-agent system design effectively incorporates the specified elements and simulates emergent linguistic consciousness.",
            "The analysis of implications is thorough and considers multiple perspectives in AI, linguistics, and cognitive science.",
            "The response shows creativity and interdisciplinary thinking throughout.",
            "The proposed future research directions are innovative and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
