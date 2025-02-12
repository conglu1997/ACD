import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            {
                'name': 'Quantum Entanglement',
                'description': 'Non-local correlation between quantum particles, potentially allowing for instantaneous information transfer.'
            },
            {
                'name': 'Quantum Superposition',
                'description': 'The ability of a quantum system to exist in multiple states simultaneously until observed.'
            },
            {
                'name': 'Quantum Tunneling',
                'description': 'The quantum phenomenon where a particle tunnels through a barrier that it classically could not surmount.'
            },
            {
                'name': 'Quantum Coherence',
                'description': 'The ability of quantum systems to maintain a definite phase relation over an extended period of time.'
            }
        ]
        
        brain_regions = [
            {
                'name': 'Hippocampus',
                'function': 'Crucial for forming new memories and spatial navigation.'
            },
            {
                'name': 'Prefrontal Cortex',
                'function': 'Involved in complex cognitive behavior, decision making, and moderating social behavior.'
            },
            {
                'name': 'Amygdala',
                'function': 'Plays a key role in processing emotions and forming emotional memories.'
            },
            {
                'name': 'Cerebellum',
                'function': 'Involved in motor control and certain cognitive functions such as attention and language.'
            }
        ]
        
        tasks = [
            {
                'quantum_effect': random.choice(quantum_effects),
                'brain_region': random.choice(brain_regions),
                'memory_type': random.choice(['episodic', 'semantic', 'procedural', 'working'])
            },
            {
                'quantum_effect': random.choice(quantum_effects),
                'brain_region': random.choice(brain_regions),
                'memory_type': random.choice(['episodic', 'semantic', 'procedural', 'working'])
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-based biological memory system that utilizes {t['quantum_effect']['name']} in the {t['brain_region']['name']} to enhance {t['memory_type']} memory. Your response should follow this structure:

1. Quantum Biomemory System Design (300-350 words):
   a) Describe how {t['quantum_effect']['name']} could theoretically be harnessed in neurons or neural networks within the {t['brain_region']['name']}.
   b) Explain how this quantum effect might enhance or alter the {t['brain_region']['function']} specifically for {t['memory_type']} memory.
   c) Propose a mechanism for how quantum information could be encoded, stored, and retrieved in this system.
   d) Discuss how this quantum biomemory system might interact with classical neuronal processes.

2. Comparative Analysis (200-250 words):
   a) Compare your quantum biomemory system to current understanding of classical biological memory processes for {t['memory_type']} memory.
   b) Discuss potential advantages and limitations of your quantum-based system.
   c) Explain how your system might address current limitations in our understanding of {t['memory_type']} memory formation and recall.

3. Experimental Design (250-300 words):
   a) Propose an experiment to test the existence and function of your quantum biomemory system.
   b) Describe the methodology, including any novel technologies or techniques that would be required.
   c) Explain what results would support your hypothesis and how they would be measured.
   d) Discuss potential challenges in conducting this experiment and how they might be overcome.

4. Implications for Cognition and Consciousness (200-250 words):
   a) Analyze how the existence of quantum processes in {t['memory_type']} memory might influence our understanding of cognition.
   b) Discuss potential implications for theories of consciousness, particularly in relation to quantum theories of mind.
   c) Consider how your quantum biomemory system might affect our concepts of free will, decision-making, or the nature of subjective experience.

5. Ethical Considerations and Future Applications (150-200 words):
   a) Discuss ethical implications of researching and potentially manipulating quantum processes in the brain.
   b) Propose two potential applications of quantum biomemory systems in fields such as medicine, AI, or brain-computer interfaces.
   c) Suggest guidelines for responsible development and use of quantum biomemory technologies.

Ensure your response demonstrates a deep understanding of both quantum mechanics and neuroscience. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section and include a brief summary (100-150 words) at the end. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']['name']} and its potential application in {t['brain_region']['name']} for {t['memory_type']} memory.",
            "The proposed quantum biomemory system is creative, scientifically plausible, and clearly explains the mechanism for quantum information encoding, storage, and retrieval.",
            f"The comparative analysis effectively contrasts the quantum biomemory system with classical processes for {t['memory_type']} memory.",
            "The experimental design is well-thought-out, addresses potential challenges, and proposes novel methods to test the hypothesis.",
            "The analysis of implications for cognition and consciousness shows insightful connections between quantum biomemory and broader questions in neuroscience and philosophy of mind.",
            "The discussion of ethical considerations and future applications is thoughtful and comprehensive.",
            "The response is well-structured, clear, and adheres to the specified word count and section guidelines, including a brief summary."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
