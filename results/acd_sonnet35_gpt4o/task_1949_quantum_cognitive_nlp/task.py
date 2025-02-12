import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_phenomena = [
            "metaphor comprehension",
            "semantic ambiguity resolution",
            "syntactic parsing",
            "pragmatic inference"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum measurement",
            "quantum tunneling"
        ]
        cognitive_processes = [
            "attention",
            "memory retrieval",
            "conceptual blending",
            "mental space mapping"
        ]
        
        tasks = {
            "1": {
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing system that incorporates principles of cognitive linguistics and quantum computing to model and analyze language understanding and generation. Your system should focus on the linguistic phenomenon of {t['linguistic_phenomenon']}, utilize the quantum principle of {t['quantum_principle']}, and model the cognitive process of {t['cognitive_process']}.

Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen linguistic phenomenon and its significance in language processing.
   b) Describe the relevant quantum principle and how it can be applied to language modeling.
   c) Discuss the cognitive process and its role in language understanding or generation.
   d) Propose how these three elements can be integrated into a coherent framework.

2. System Architecture (300-350 words):
   a) Outline the overall structure of your quantum-inspired NLP system.
   b) Explain how it incorporates the chosen linguistic phenomenon, quantum principle, and cognitive process.
   c) Describe the main components and their interactions.
   d) Discuss any novel algorithms or approaches used in your design.

3. Quantum-Linguistic Modeling (250-300 words):
   a) Detail how your system models language using quantum-inspired techniques.
   b) Explain how this approach enhances the analysis or generation of the chosen linguistic phenomenon.
   c) Provide a specific example of how your system would process or generate language.

4. Cognitive Process Integration (200-250 words):
   a) Describe how your system models the specified cognitive process.
   b) Explain how this cognitive modeling enhances the system's language processing capabilities.
   c) Discuss any challenges in integrating cognitive processes with quantum-inspired NLP.

5. Potential Applications and Implications (200-250 words):
   a) Propose potential applications of your system in natural language processing or cognitive science.
   b) Discuss how your approach could advance our understanding of language and cognition.
   c) Address any ethical considerations or potential misuses of this technology.

6. Evaluation and Future Work (150-200 words):
   a) Suggest methods to evaluate the performance and validity of your quantum-cognitive NLP system.
   b) Identify limitations of your current design and areas for future research and improvement.
   c) Propose an experiment to test a specific hypothesis about language processing using your system.

Ensure your response demonstrates a deep understanding of linguistics, quantum computing principles, and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. When discussing scientific concepts, provide appropriate citations or references to support your claims.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified linguistic phenomenon, quantum principle, and cognitive process.",
            "The proposed system architecture is innovative and coherently integrates all three elements.",
            "The quantum-linguistic modeling approach is well-explained and plausible.",
            "The integration of the cognitive process is clearly described and enhances the system's capabilities.",
            "Potential applications and ethical considerations are thoroughly discussed.",
            "The evaluation methods and future work proposals are well-thought-out and relevant.",
            "The overall response is well-structured, coherent, and within the specified word limit.",
            "Appropriate citations or references are provided to support scientific claims."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
