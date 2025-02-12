import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['Superposition', 'Entanglement', 'Quantum tunneling', 'Quantum annealing']
        cognitive_processes = ['Divergent thinking', 'Conceptual blending', 'Analogical reasoning', 'Insight problem solving']
        application_domains = ['Climate change mitigation', 'Space exploration', 'Neurodegenerative disease treatment', 'Sustainable urban planning']
        
        tasks = {
            '1': {
                'quantum_principle': random.choice(quantum_principles),
                'cognitive_process': random.choice(cognitive_processes),
                'application_domain': random.choice(application_domains)
            },
            '2': {
                'quantum_principle': random.choice(quantum_principles),
                'cognitive_process': random.choice(cognitive_processes),
                'application_domain': random.choice(application_domains)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for enhancing creative problem-solving in artificial intelligence systems, then apply it to solve a complex interdisciplinary challenge. Your system should incorporate the quantum principle of {t['quantum_principle']}, focus on the cognitive process of {t['cognitive_process']}, and be applied to the domain of {t['application_domain']}.

Your response should include the following sections:

1. Quantum-Inspired Cognitive Architecture (300-350 words):
   a) Describe the key components of your cognitive architecture.
   b) Explain how you incorporate the specified quantum principle into the system.
   c) Detail how the architecture enhances the given cognitive process.
   d) Provide a high-level diagram or detailed description of your system's structure.

2. Quantum-Cognitive Mechanisms (250-300 words):
   a) Explain the theoretical basis for your quantum-inspired approach to cognition.
   b) Describe specific mechanisms that leverage quantum principles to enhance creative problem-solving.
   c) Discuss how these mechanisms differ from classical approaches to AI cognition.

3. Implementation and Training (200-250 words):
   a) Outline the computational requirements for implementing your architecture.
   b) Describe the training process for your system, including data requirements and learning algorithms.
   c) Address any challenges in simulating quantum effects in classical computing systems.

4. Application to Complex Challenge (250-300 words):
   a) Present a specific problem or challenge within the given application domain.
   b) Explain how your quantum-inspired cognitive system would approach this challenge.
   c) Describe the expected benefits of your approach compared to traditional methods.
   d) Provide a step-by-step example of your system's problem-solving process.

5. Evaluation and Benchmarking (150-200 words):
   a) Propose methods to evaluate the creativity and effectiveness of your system.
   b) Suggest benchmarks for comparing your approach to classical AI systems.
   c) Discuss potential limitations of your system and how they might be addressed.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical issues arising from the development and use of quantum-inspired AI systems.
   b) Discuss the broader societal implications of enhanced machine creativity.
   c) Propose guidelines for responsible development and use of such technologies.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and subsection. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed quantum-inspired cognitive architecture that incorporates {t['quantum_principle']} and enhances {t['cognitive_process']}.",
            f"The system is applied to solve a complex challenge in the domain of {t['application_domain']}.",
            "The quantum-cognitive mechanisms are clearly explained and differentiated from classical AI approaches.",
            "The implementation and training process is outlined with consideration of computational requirements and challenges.",
            "The application of the system to the complex challenge is well-described with a step-by-step example.",
            "Evaluation methods and benchmarks are proposed to assess the system's creativity and effectiveness.",
            "Ethical considerations and societal impacts of quantum-inspired AI systems are thoroughly discussed.",
            "The response demonstrates interdisciplinary knowledge integration and creative system design.",
            "The response is well-structured with clear headings and falls within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
