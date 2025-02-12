import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence"
        ]
        brain_regions = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Inferior frontal gyrus"
        ]
        linguistic_features = [
            "Syntactic parsing",
            "Semantic analysis",
            "Pragmatic inference",
            "Phonological processing"
        ]
        nlp_tasks = [
            "Sentiment analysis",
            "Machine translation",
            "Text summarization",
            "Question answering"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "brain_region": random.choice(brain_regions),
                "linguistic_feature": random.choice(linguistic_features),
                "nlp_task": random.choice(nlp_tasks)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "brain_region": random.choice(brain_regions),
                "linguistic_feature": random.choice(linguistic_features),
                "nlp_task": random.choice(nlp_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing system that models language processing in the brain, then use it to enhance natural language understanding and generation. Your system should incorporate the quantum principle of {t['quantum_principle']}, focus on the brain region {t['brain_region']}, address the linguistic feature of {t['linguistic_feature']}, and aim to improve the NLP task of {t['nlp_task']}. Your response should include:

1. Quantum-Neural Language Model (300-350 words):
   a) Describe the key components of your quantum computing system for modeling language processing.
   b) Explain how it incorporates the specified quantum principle and brain region.
   c) Detail how your model addresses the given linguistic feature.
   d) Discuss any novel quantum algorithms or neural network architectures used in your system.

2. Quantum-Brain Interface (250-300 words):
   a) Explain how your system maps quantum states to neural activity in the specified brain region.
   b) Describe how quantum operations are translated into linguistic computations.
   c) Discuss potential challenges in maintaining quantum coherence in a neural context and how you address them.
   d) Propose a mechanism for how quantum effects might enhance or alter traditional neural language processing.

3. Enhanced NLP Capabilities (250-300 words):
   a) Describe how your quantum-neural language model improves the specified NLP task.
   b) Provide a specific example of how your system would process a given input for this task.
   c) Compare the performance and capabilities of your system to traditional classical NLP approaches.
   d) Discuss any potential limitations or trade-offs in using a quantum-neural approach for NLP.

4. Theoretical Implications (200-250 words):
   a) Discuss how your model might inform our understanding of language processing in the brain.
   b) Explore potential insights into the nature of consciousness or cognition that could be derived from your quantum-neural language model.
   c) Propose a testable hypothesis about language processing based on your model.

5. Ethical Considerations and Future Directions (200-250 words):
   a) Identify potential ethical concerns or risks associated with quantum-neural language processing systems.
   b) Propose guidelines for the responsible development and use of such technology.
   c) Suggest future research directions that could further develop the concept of quantum-neural language processing.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and computational linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five required sections comprehensively.",
            f"The system effectively incorporates {t['quantum_principle']}, {t['brain_region']}, {t['linguistic_feature']}, and aims to improve {t['nlp_task']}.",
            "The proposed quantum-neural language model is innovative and demonstrates interdisciplinary integration.",
            "The response shows a deep understanding of quantum computing, neuroscience, and computational linguistics.",
            "The theoretical implications and ethical considerations are well-reasoned and insightful.",
            "The response is scientifically plausible while being creative and speculative.",
            "The enhanced NLP capabilities are clearly explained and compared to classical approaches.",
            "The response provides specific examples and novel ideas throughout.",
            "The proposed system addresses potential challenges and limitations.",
            "The ethical considerations are thoughtful and comprehensive."
        ]
        word_count = len(submission.split())
        if word_count < 1200 or word_count > 1450:
            return 0.0
        
        score = 0.0
        for criterion in criteria:
            if eval_with_llm_judge(instructions, submission, [criterion]):
                score += 0.1
        return score
