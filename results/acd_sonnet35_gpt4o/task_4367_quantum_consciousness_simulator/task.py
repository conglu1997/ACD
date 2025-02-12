import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "altered_state": "Meditation",
                "quantum_principle": "Superposition"
            },
            {
                "altered_state": "Lucid Dreaming",
                "quantum_principle": "Entanglement"
            },
            {
                "altered_state": "Psychedelic Experience",
                "quantum_principle": "Quantum Tunneling"
            },
            {
                "altered_state": "Flow State",
                "quantum_principle": "Quantum Coherence"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a quantum-inspired computational model of consciousness, then use it to simulate and analyze the altered state of consciousness known as {t['altered_state']}, focusing on the quantum principle of {t['quantum_principle']}. Your response should include the following sections:

1. Quantum Consciousness Model (300-350 words):
   a) Describe the key components and principles of your quantum-inspired model of consciousness.
   b) Explain how you incorporate the quantum principle of {t['quantum_principle']} into your model.
   c) Discuss how your model bridges quantum mechanics, neuroscience, and theories of consciousness.
   d) Include a high-level diagram or pseudocode representing the core algorithm of your model.
   e) Cite at least two relevant scientific papers to support your model's theoretical foundation.

2. Altered State Simulation (250-300 words):
   a) Explain how your model simulates the altered state of {t['altered_state']}.
   b) Describe the key features or parameters that distinguish this state in your simulation.
   c) Discuss how the quantum principle of {t['quantum_principle']} contributes to modeling this altered state.
   d) Propose a novel hypothesis about how this quantum principle might underlie the phenomenology of {t['altered_state']}.

3. Neuroscientific Basis (200-250 words):
   a) Discuss the current neuroscientific understanding of {t['altered_state']}.
   b) Explain how your quantum-inspired model aligns with or challenges existing neuroscientific theories.
   c) Propose a novel hypothesis about the neural correlates of this altered state based on your model.
   d) Suggest an experimental design to test your hypothesis, incorporating both quantum and neuroscientific measurements.

4. Simulation Results and Analysis (250-300 words):
   a) Present the outcomes of your simulation, including at least one quantitative prediction and one qualitative insight.
   b) Compare these results to empirical data or subjective reports of {t['altered_state']}.
   c) Analyze the implications of your findings for our understanding of consciousness and altered states.
   d) Discuss any unexpected or counterintuitive results from your simulation.

5. Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of simulating and potentially manipulating consciousness.
   b) Address concerns about the use of such models in medical or therapeutic contexts.
   c) Propose guidelines for responsible research and application of quantum consciousness models.
   d) Consider potential societal impacts if this technology becomes widely available or misused.

6. Limitations and Future Directions (150-200 words):
   a) Identify at least three potential limitations or challenges in your proposed model.
   b) Suggest how these limitations might be addressed in future research.
   c) Propose two potential applications or extensions of your quantum consciousness model.
   d) Speculate on how this approach might influence our understanding of free will and decision-making.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and consciousness studies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere strictly to the word count for each section. Your total response should be between 1350-1650 words. Include a word count at the end of each section.

Cite relevant scientific literature throughout your response using in-text citations (Author, Year). Include at least five unique citations across your entire response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains and creatively incorporates the quantum principle of {t['quantum_principle']} in modeling consciousness",
            f"The model effectively simulates and provides novel insights into the altered state of {t['altered_state']}",
            "The submission demonstrates a deep understanding of quantum mechanics, neuroscience, and consciousness studies, with appropriate use of technical terminology",
            "The proposed model is innovative and presents at least one novel hypothesis, while maintaining scientific plausibility",
            "The response includes thoughtful ethical considerations and specific guidelines for responsible research",
            "The submission cites at least five relevant scientific papers and integrates them effectively into the discussion",
            "The response adheres to the specified word counts and formatting requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
