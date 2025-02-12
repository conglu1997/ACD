import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Annealing"
        ]
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Hippocampus",
            "Prefrontal cortex"
        ]
        narrative_elements = [
            "Character development",
            "Plot structure",
            "Setting description",
            "Dialogue generation"
        ]
        cultural_contexts = [
            "East Asian",
            "Middle Eastern",
            "Nordic",
            "Sub-Saharan African"
        ]
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "brain_region": random.choice(brain_regions),
                "narrative_element": random.choice(narrative_elements),
                "cultural_context": random.choice(cultural_contexts)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "brain_region": random.choice(brain_regions),
                "narrative_element": random.choice(narrative_elements),
                "cultural_context": random.choice(cultural_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses quantum-inspired algorithms to simulate neural processes involved in creative writing, and apply it to generate culturally adaptive narratives. Your system should incorporate the quantum principle of {t['quantum_principle']}, focus on the brain region {t['brain_region']}, and be applied to generate {t['narrative_element']} in a {t['cultural_context']} context.

Your response should include the following sections:

1. Quantum-Neural Integration (250-300 words):
   a) Explain how the quantum principle of {t['quantum_principle']} can be used to model neural processes in {t['brain_region']}.
   b) Describe the potential advantages of this quantum-inspired approach over classical computational models.
   c) Propose a specific algorithm or mathematical formulation that integrates quantum principles with neural simulation.

2. Creative Writing Process Simulation (200-250 words):
   a) Describe how your system simulates the creative writing process, focusing on {t['narrative_element']}.
   b) Explain how the quantum-neural integration enhances this simulation.
   c) Discuss any challenges in modeling creativity and how your system addresses them.

3. Cultural Adaptation Mechanism (200-250 words):
   a) Explain how your system adapts its output to the {t['cultural_context']} context.
   b) Describe the data sources and learning mechanisms used for cultural adaptation.
   c) Discuss potential biases and how you would mitigate them.

4. System Architecture and Implementation (250-300 words):
   a) Provide a high-level diagram or pseudocode of your system's architecture.
   b) Explain the key components and their interactions.
   c) Describe how you would implement and train this system.

5. Output Analysis and Evaluation (150-200 words):
   a) Propose a method to evaluate the quality and cultural appropriateness of the generated narratives.
   b) Suggest metrics for assessing the system's creativity and coherence.
   c) Describe a potential experiment to compare your system's output with human-written narratives.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using AI for creative writing and cultural adaptation.
   b) Address concerns related to authorship, cultural appropriation, and potential misuse.
   c) Propose two future research directions or improvements for your system.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, creative writing, and cultural anthropology. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response clearly explains how the quantum principle of {t['quantum_principle']} is integrated with neural processes in {t['brain_region']}.",
            f"The system effectively simulates the creative writing process for {t['narrative_element']}.",
            f"The cultural adaptation mechanism for the {t['cultural_context']} context is well-described and plausible.",
            "The system architecture is clearly explained and includes all necessary components.",
            "The response addresses ethical considerations and future directions thoughtfully.",
            "The overall design demonstrates a deep understanding of quantum computing, neuroscience, creative writing, and cultural anthropology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
