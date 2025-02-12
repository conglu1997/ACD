import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "quantum coherence",
            "quantum entanglement",
            "tunneling",
            "superposition",
            "quantum walk"
        ]
        cognitive_processes = [
            "decision making",
            "learning",
            "memory formation",
            "attention",
            "problem-solving"
        ]
        ecosystem_types = [
            "coral reef",
            "rainforest",
            "tundra",
            "grassland",
            "mangrove forest"
        ]
        environmental_challenges = [
            "climate change",
            "biodiversity loss",
            "pollution",
            "invasive species",
            "habitat fragmentation"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "ecosystem_type": random.choice(ecosystem_types),
                "environmental_challenge": random.choice(environmental_challenges)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "ecosystem_type": random.choice(ecosystem_types),
                "environmental_challenge": random.choice(environmental_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture to model complex ecosystem dynamics, integrating principles from quantum biology, cognitive science, and environmental systems. Your architecture should focus on the quantum principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and be applied to a {t['ecosystem_type']} facing the challenge of {t['environmental_challenge']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain how {t['quantum_principle']} can be applied to model {t['cognitive_process']} in biological systems.
   b) Describe how this quantum-cognitive approach can be used to understand ecosystem dynamics.
   c) Discuss the relevance of this framework to addressing {t['environmental_challenge']} in a {t['ecosystem_type']}.

2. Architecture Design (300-350 words):
   a) Outline the main components of your quantum-inspired cognitive architecture.
   b) Explain how your architecture incorporates {t['quantum_principle']} to model {t['cognitive_process']}.
   c) Describe how your architecture represents and processes information about the {t['ecosystem_type']}.
   d) Detail how your system models the impact of {t['environmental_challenge']} on the ecosystem.

3. Implementation Strategy (200-250 words):
   a) Propose a method for implementing your architecture in a computational model.
   b) Discuss any novel algorithms or data structures required for your implementation.
   c) Address potential challenges in simulating quantum effects in a classical computing environment.

4. Predictions and Insights (200-250 words):
   a) Describe specific predictions your model could make about the {t['ecosystem_type']} under {t['environmental_challenge']}.
   b) Explain how these predictions differ from those of classical ecosystem models.
   c) Discuss potential insights into {t['cognitive_process']} in biological systems that your model might provide.

5. Validation and Testing (150-200 words):
   a) Propose methods to validate your model against real-world ecosystem data.
   b) Describe experiments that could test the quantum-cognitive aspects of your model.
   c) Discuss potential limitations of your approach and how they might be addressed.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify ethical implications of using quantum-inspired cognitive models in ecosystem management.
   b) Discuss potential risks or benefits of applying this approach to environmental decision-making.
   c) Suggest future research directions or extensions of your model to other domains.

Ensure your response demonstrates a deep understanding of quantum biology, cognitive science, and ecosystem dynamics. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere strictly to the word count ranges provided for each section. Your total response should be between 1250-1550 words.

Include a brief summary (50-100 words) at the end of your response, highlighting the key innovative aspects of your quantum-cognitive ecosystem model."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum biology, cognitive science, and ecosystem dynamics.",
            f"The architecture effectively incorporates {t['quantum_principle']} to model {t['cognitive_process']} in the context of a {t['ecosystem_type']}.",
            f"The model provides novel insights into addressing {t['environmental_challenge']} in the specified ecosystem.",
            "The implementation strategy and validation methods are scientifically plausible and well-reasoned.",
            "The response addresses all required sections, adheres to the specified word count ranges, and includes a brief summary.",
            "The proposed model demonstrates innovative thinking and potential for advancing the field of ecosystem modeling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
