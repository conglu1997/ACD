import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            'Quantum entanglement',
            'Quantum superposition',
            'Quantum tunneling',
            'Quantum coherence'
        ]
        linguistic_processes = [
            'Syntactic parsing',
            'Semantic processing',
            'Phonological encoding',
            'Lexical retrieval'
        ]
        brain_regions = [
            'Broca\'s area',
            'Wernicke\'s area',
            'Angular gyrus',
            'Inferior frontal gyrus'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'quantum_concept': random.choice(quantum_concepts),
                'linguistic_process': random.choice(linguistic_processes),
                'brain_region': random.choice(brain_regions)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model that explores potential quantum effects in language acquisition and processing in the human brain, focusing on the quantum concept of {t['quantum_concept']}, the linguistic process of {t['linguistic_process']}, and the brain region known as {t['brain_region']}. Then, analyze its implications for linguistics and cognitive science. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain the chosen quantum concept and its potential relevance to neural processes in language.
   b) Describe the specified linguistic process and how it might be influenced by quantum effects.
   c) Discuss the role of the given brain region in language processing and how quantum phenomena could manifest there.
   d) Propose a hypothesis for how quantum effects could influence language acquisition or processing.

2. Model Design (300-350 words):
   a) Outline the key components and mechanisms of your quantum neurolinguistic model.
   b) Explain how your model integrates quantum principles with neural and linguistic processes.
   c) Describe any novel computational or conceptual approaches in your model.
   d) Include a diagram or flowchart of your model's architecture (describe it textually).

3. Predictions and Testability (200-250 words):
   a) Describe specific predictions your model makes about language acquisition or processing.
   b) Propose experiments or observations that could validate or refute these predictions.
   c) Discuss any technological limitations in testing your model and how they might be overcome.

4. Implications for Linguistics and Cognitive Science (250-300 words):
   a) Analyze how your model could impact current theories in linguistics and cognitive science.
   b) Discuss potential applications of your model in language education, therapy, or artificial intelligence.
   c) Explore how this model might contribute to our understanding of consciousness or cognitive evolution.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to research or applications of your model.
   b) Discuss how these ethical concerns might be addressed or mitigated.
   c) Propose guidelines for responsible conduct of research in this interdisciplinary field.

6. Limitations and Future Directions (150-200 words):
   a) Acknowledge the speculative nature of your model and its current limitations.
   b) Suggest areas for further research or refinement of your quantum neurolinguistic model.
   c) Propose potential collaborations across disciplines to advance this field of study.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and linguistics. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates the quantum concept of {t['quantum_concept']}, the linguistic process of {t['linguistic_process']}, and the brain region {t['brain_region']} in a coherent theoretical model.",
            "The model design is innovative, scientifically plausible, and clearly explained.",
            "The response includes testable predictions and discusses experimental approaches.",
            "The implications for linguistics and cognitive science are thoroughly analyzed.",
            "Ethical considerations are thoughtfully addressed.",
            "The response acknowledges limitations and proposes future research directions.",
            "The writing demonstrates a deep understanding of quantum physics, neuroscience, and linguistics.",
            "The response is creative and speculative while maintaining scientific rigor.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
