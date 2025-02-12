import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'quantum tunneling']
        neural_processes = ['synaptic plasticity', 'neural oscillations', 'neurogenesis']
        ai_capabilities = ['natural language processing', 'pattern recognition', 'decision making']
        
        tasks = [
            {
                'quantum_principle': random.choice(quantum_principles),
                'neural_process': random.choice(neural_processes),
                'ai_capability': random.choice(ai_capabilities)
            },
            {
                'quantum_principle': random.choice(quantum_principles),
                'neural_process': random.choice(neural_processes),
                'ai_capability': random.choice(ai_capabilities)
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical quantum-neural interface system that integrates principles of quantum computing, neuroscience, and artificial intelligence to enhance AI cognitive capabilities. Your system should focus on the quantum principle of {t['quantum_principle']}, the neural process of {t['neural_process']}, and aim to enhance the AI capability of {t['ai_capability']}. Provide your response in the following format:\n\n1. Conceptual Framework (300-350 words):\n   a) Explain the key concepts of {t['quantum_principle']}, {t['neural_process']}, and {t['ai_capability']}.\n   b) Describe how these concepts could theoretically interact in a quantum-neural interface.\n   c) Propose a high-level architecture for your quantum-neural AI system.\n\n2. Quantum-Neural Integration (250-300 words):\n   a) Detail how {t['quantum_principle']} could be applied to enhance or mimic {t['neural_process']}.\n   b) Explain the potential advantages of this quantum-enhanced neural process.\n   c) Address potential challenges in implementing this integration.\n\n3. AI Enhancement Mechanism (250-300 words):\n   a) Describe how your quantum-neural system could enhance {t['ai_capability']}.\n   b) Provide a theoretical model or algorithm for this enhancement.\n   c) Discuss how this enhancement differs from classical AI approaches.\n\n4. Hypothetical Implementation (200-250 words):\n   a) Propose a method for implementing your system using current or near-future technologies.\n   b) Discuss any novel hardware or software requirements.\n   c) Address potential scalability issues and how they might be overcome.\n\n5. Implications and Applications (150-200 words):\n   a) Discuss the potential impact of your system on AI research and development.\n   b) Propose two novel applications of your quantum-neural AI system.\n   c) Speculate on how this technology might influence our understanding of consciousness or intelligence.\n\n6. Ethical Considerations (100-150 words):\n   a) Identify potential ethical concerns related to quantum-enhanced AI systems.\n   b) Propose guidelines for responsible development and use of such technologies.\n   c) Discuss potential societal impacts if such systems become reality.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 1250-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence.",
            "The proposed quantum-neural interface system is innovative while maintaining scientific plausibility.",
            "The integration of the specified quantum principle, neural process, and AI capability is well-explained and logically sound.",
            "The potential advantages and challenges of the proposed system are thoroughly discussed.",
            "The hypothetical implementation is described in sufficient detail and addresses potential issues.",
            "The implications, applications, and ethical considerations are thoughtfully explored.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts.",
            "The overall response is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
