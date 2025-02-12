import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_phenomena = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence",
            "Quantum annealing"
        ]
        
        brain_regions = [
            "Hippocampus",
            "Prefrontal cortex",
            "Amygdala",
            "Cerebellum",
            "Thalamus"
        ]
        
        memory_types = [
            "Episodic memory",
            "Semantic memory",
            "Procedural memory",
            "Working memory",
            "Implicit memory"
        ]
        
        cognitive_disorders = [
            "Alzheimer's disease",
            "Parkinson's disease",
            "Schizophrenia",
            "Autism spectrum disorder",
            "Post-traumatic stress disorder"
        ]
        
        return {
            "1": {
                "quantum_phenomenon": random.choice(quantum_phenomena),
                "brain_region": random.choice(brain_regions),
                "memory_type": random.choice(memory_types),
                "cognitive_disorder": random.choice(cognitive_disorders)
            },
            "2": {
                "quantum_phenomenon": random.choice(quantum_phenomena),
                "brain_region": random.choice(brain_regions),
                "memory_type": random.choice(memory_types),
                "cognitive_disorder": random.choice(cognitive_disorders)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing model for encoding and retrieving memories in the human brain, then analyze its implications for understanding consciousness and improving memory-related cognitive disorders. Your model should focus on the quantum phenomenon of {t['quantum_phenomenon']}, primarily involve the {t['brain_region']}, and address the memory type of {t['memory_type']}. Additionally, explore how your model could potentially help in understanding or treating {t['cognitive_disorder']}.

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain the key principles of quantum computing and neuroscience relevant to your model, focusing on {t['quantum_phenomenon']}.
   b) Describe current understanding of memory formation and retrieval in the {t['brain_region']}.
   c) Discuss existing theories or models that attempt to link quantum phenomena to brain function.
   d) Explain how your model builds upon or differs from these existing approaches.

2. Quantum Memory Model (300-350 words):
   a) Describe the key components and mechanisms of your quantum memory model.
   b) Explain how {t['quantum_phenomenon']} is integrated into your model of memory encoding and retrieval.
   c) Detail how your model accounts for the formation and retrieval of {t['memory_type']}.
   d) Discuss how quantum effects in your model might influence or arise from neural activity in the {t['brain_region']}.

3. Consciousness Implications (200-250 words):
   a) Analyze how your quantum memory model might contribute to our understanding of consciousness.
   b) Discuss potential implications of your model for theories of self-awareness and subjective experience.
   c) Address any philosophical questions or paradoxes that arise from your model.

4. Cognitive Disorder Applications (250-300 words):
   a) Explain how your model could provide new insights into the mechanisms underlying {t['cognitive_disorder']}.
   b) Propose potential therapeutic interventions or diagnostic tools based on your quantum memory model.
   c) Discuss any challenges or limitations in applying your model to clinical situations.

5. Experimental Predictions (200-250 words):
   a) Describe specific, testable predictions that your model makes about memory or brain function.
   b) Propose experiments or observations that could potentially validate or refute your model.
   c) Discuss any technological limitations that might hinder testing your model and how they might be overcome.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using quantum computing models to understand and manipulate human memory.
   b) Propose guidelines for responsible development and application of such technologies.
   c) Suggest future research directions or potential applications of your model beyond the current scope.

Ensure your response demonstrates a deep understanding of both quantum computing and neuroscience. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of both quantum computing and neuroscience principles.",
            "The proposed quantum memory model is innovative, scientifically plausible, and effectively incorporates the specified quantum phenomenon and brain region.",
            "The implications for consciousness and cognitive disorders are thoroughly explored and logically derived from the proposed model.",
            "The experimental predictions and proposed tests are specific, relevant, and scientifically sound.",
            "Ethical considerations are thoughtfully addressed, and future research directions are insightful and well-reasoned.",
            "The overall response is well-structured, coherent, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
