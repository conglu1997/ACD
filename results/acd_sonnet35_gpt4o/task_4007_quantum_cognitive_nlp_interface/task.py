import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            'Superposition',
            'Entanglement',
            'Quantum tunneling',
            'Quantum coherence'
        ]
        cognitive_processes = [
            'Working memory',
            'Attention',
            'Decision-making',
            'Emotional processing'
        ]
        nlp_applications = [
            'Sentiment analysis',
            'Language generation',
            'Machine translation',
            'Question answering'
        ]
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "nlp_application": random.choice(nlp_applications)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "nlp_application": random.choice(nlp_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-cognitive interface system that translates human thought patterns into natural language, focusing on the following aspects:

Quantum Principle: {t['quantum_principle']}
Cognitive Process: {t['cognitive_process']}
NLP Application: {t['nlp_application']}

Your response should include:

1. Conceptual Framework (250-300 words):
   a) Explain how the specified quantum principle can be applied to model the given cognitive process.
   b) Describe how this quantum-cognitive model could be used to enhance the specified NLP application.
   c) Discuss potential advantages and challenges of this approach compared to classical methods.

2. System Architecture (300-350 words):
   a) Provide a detailed description of your quantum-cognitive interface system's components and their interactions.
   b) Explain how your system would capture and process neural signals related to the specified cognitive process.
   c) Describe the quantum computing elements of your system and how they interface with the cognitive and NLP components.
   d) Include a diagram or flowchart illustrating your system's architecture (describe this textually).

3. Quantum-Cognitive Translation Process (250-300 words):
   a) Outline the step-by-step process of translating thought patterns into quantum states.
   b) Explain how these quantum states are then processed to generate natural language output.
   c) Describe any novel algorithms or techniques you've developed for this translation process.

4. NLP Integration and Output (200-250 words):
   a) Explain how your system integrates with the specified NLP application.
   b) Provide an example of how your system would process a specific thought pattern and generate corresponding natural language output.
   c) Discuss how your system ensures the accuracy and coherence of the generated language.

5. Ethical Considerations and Limitations (200-250 words):
   a) Analyze potential ethical implications of directly translating thoughts into language.
   b) Discuss privacy concerns and propose safeguards for protecting individuals' cognitive data.
   c) Identify current technological limitations and suggest areas for future research and development.

6. Potential Applications and Impact (150-200 words):
   a) Propose three novel applications of your quantum-cognitive interface system beyond the specified NLP task.
   b) Discuss how this technology could impact fields such as neuroscience, artificial intelligence, and human-computer interaction.
   c) Speculate on potential long-term societal effects of widespread adoption of this technology.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive neuroscience, and natural language processing. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum principle {t['quantum_principle']} and how it can be applied to cognitive modeling.",
            f"The system design effectively integrates the cognitive process of {t['cognitive_process']} with quantum computing principles.",
            f"The proposed solution shows a clear application to the NLP task of {t['nlp_application']}.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The ethical considerations and limitations are thoughtfully analyzed.",
            "The response is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
