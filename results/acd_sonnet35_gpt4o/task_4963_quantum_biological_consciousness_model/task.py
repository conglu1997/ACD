import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'tunneling', 'coherence']
        brain_regions = ['neocortex', 'hippocampus', 'thalamus', 'cerebellum']
        collaboration_scenarios = ['scientific research', 'artistic creation', 'strategic planning', 'crisis management']
        
        task1 = {
            "quantum_principle": random.choice(quantum_principles),
            "brain_region": random.choice(brain_regions),
            "collaboration_scenario": random.choice(collaboration_scenarios)
        }
        
        task2 = {
            "quantum_principle": random.choice([p for p in quantum_principles if p != task1["quantum_principle"]]),
            "brain_region": random.choice([r for r in brain_regions if r != task1["brain_region"]]),
            "collaboration_scenario": random.choice([s for s in collaboration_scenarios if s != task1["collaboration_scenario"]])
        }
        
        return {"1": task1, "2": task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum biological model of consciousness and apply it to enhance human-AI collaboration in complex problem-solving scenarios. Your model should incorporate the quantum principle of {t['quantum_principle']} and focus on the {t['brain_region']} region of the brain. Then, apply your model to enhance human-AI collaboration in the scenario of {t['collaboration_scenario']}.

Your response should include the following sections:

1. Quantum Biological Consciousness Model (300-350 words):
   a) Describe the key components and mechanisms of your quantum biological model of consciousness.
   b) Explain how the specified quantum principle is integrated into your model.
   c) Detail how your model accounts for the role of the specified brain region in consciousness.
   d) Discuss how your model addresses the hard problem of consciousness.
   e) Include a diagram or flowchart of your model (describe it textually in 50-100 words).

2. Quantum-Neural Integration (250-300 words):
   a) Explain how quantum effects in the specified brain region could influence conscious experience.
   b) Describe the proposed mechanisms for maintaining quantum coherence in the warm, wet environment of the brain.
   c) Discuss how your model bridges the gap between quantum-level events and macro-level conscious experiences.

3. Human-AI Collaboration Enhancement (250-300 words):
   a) Apply your quantum biological consciousness model to the specified collaboration scenario.
   b) Explain how your model could enhance the cognitive capabilities of human participants.
   c) Describe how AI systems could be designed or modified to interface with humans based on your model.
   d) Provide a specific example of how this enhanced collaboration would work in practice.

4. Experimental Validation (200-250 words):
   a) Propose an experimental setup to test key aspects of your quantum biological consciousness model.
   b) Describe the measurements and observations that would be necessary to validate your model.
   c) Discuss potential challenges in experimentally verifying quantum effects in consciousness.
   Note: While you should aim for scientific plausibility, you may propose hypothetical technologies or methods that are currently beyond our reach, as long as they are grounded in scientific principles.

5. Ethical and Philosophical Implications (150-200 words):
   a) Analyze the ethical considerations of enhancing human consciousness through your proposed quantum-inspired technologies.
   b) Discuss the philosophical implications of your specific model for our understanding of free will and decision-making.
   c) Consider potential societal impacts of widespread adoption of quantum-enhanced human-AI collaboration based on your model.

6. Future Research Directions (150-200 words):
   a) Suggest two specific research questions that could further develop your quantum biological consciousness model.
   b) Propose potential applications of your model in fields such as medicine, education, or artificial intelligence.
   c) Discuss how your model might contribute to the development of more advanced AI systems.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, consciousness studies, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, consciousness studies, and artificial intelligence.",
            "The quantum biological model of consciousness is innovative, well-explained, and scientifically plausible.",
            "The integration of the specified quantum principle and brain region is logically described and justified.",
            "The application to human-AI collaboration is creative and well-reasoned.",
            "The experimental validation proposal is scientifically sound and addresses potential challenges.",
            "Ethical and philosophical implications are thoughtfully considered and directly related to the proposed model.",
            "Future research directions are innovative and relevant to the proposed model.",
            "The response maintains scientific rigor while being creative and speculative.",
            "The response follows the specified format with clear headings for each section.",
            "The total word count is within the specified range (1300-1600 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
