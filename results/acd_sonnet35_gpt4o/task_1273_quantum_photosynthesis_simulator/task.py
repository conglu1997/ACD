import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_effect": "quantum coherence",
                "biological_process": "light-harvesting complexes in purple bacteria",
                "application_focus": "improving solar cell efficiency",
                "coherence_time": "300 femtoseconds",
                "energy_transfer_efficiency": "95%"
            },
            "2": {
                "quantum_effect": "quantum entanglement",
                "biological_process": "electron transport in photosystem II",
                "application_focus": "designing artificial photosynthetic systems",
                "entanglement_duration": "5 picoseconds",
                "energy_transfer_efficiency": "99%"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to simulate and analyze the quantum effects in photosynthesis, focusing on energy transfer efficiency and potential biomimetic applications. Your task should address the following components:

1. Quantum Biology Overview (200-250 words):
   a) Explain the role of {t['quantum_effect']} in photosynthesis, particularly in {t['biological_process']}.
   b) Discuss current scientific understanding and any controversies in this area.
   c) Describe how quantum effects contribute to the efficiency of photosynthetic energy transfer.
   d) Analyze the significance of the given {t['quantum_effect']} duration ({t['coherence_time'] if 'coherence_time' in t else t['entanglement_duration']}) and energy transfer efficiency ({t['energy_transfer_efficiency']}).

2. Quantum Simulation Design (250-300 words):
   a) Propose a quantum computing architecture to simulate the specified quantum effect in the given biological process.
   b) Explain how your system models the interplay between quantum and classical phenomena in photosynthesis.
   c) Describe the quantum algorithms or techniques your simulator employs.
   d) Provide a high-level schematic or pseudocode of your quantum simulation system.
   e) Explain how your simulation accounts for the given quantum effect duration and aims to reproduce the specified energy transfer efficiency.

3. Data Analysis and Interpretation (200-250 words):
   a) Explain how your system would process and analyze the simulation results.
   b) Discuss potential insights into photosynthetic efficiency that could be gained from your quantum simulator.
   c) Describe how you would validate your simulation results against experimental data.
   d) Propose a method to compare your simulated energy transfer efficiency with the given value of {t['energy_transfer_efficiency']}.

4. Biomimetic Application (200-250 words):
   a) Propose a specific application of your findings in {t['application_focus']}.
   b) Explain how understanding quantum effects in photosynthesis could lead to improvements in this application.
   c) Discuss any challenges in translating quantum biological principles to artificial systems.
   d) Estimate the potential efficiency improvements in your proposed application, using the given photosynthetic efficiency as a benchmark.

5. Ethical Implications and Future Directions (150-200 words):
   a) Discuss potential ethical considerations in applying quantum biological principles to technology.
   b) Propose two future research directions that could build upon your quantum photosynthesis simulator.
   c) Speculate on how advancements in this field might impact our understanding of life and the development of quantum technologies.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthetic processes, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1000-1250 words. Include a word count at the end of your submission.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of quantum biology, particularly the role of the specified quantum effect in photosynthesis.",
            "The quantum simulation design is well-explained, innovative, and appropriately incorporates quantum computing principles.",
            "The data analysis and interpretation section shows depth of understanding and critical thinking about the simulation results and their implications.",
            "The proposed biomimetic application is creative, well-reasoned, and demonstrates a clear link to the quantum biological principles discussed.",
            "The ethical implications and future directions are thoughtfully considered and demonstrate an understanding of the broader impacts of this research.",
            "The response effectively integrates knowledge from quantum physics, biology, and computational modeling throughout.",
            f"The response accurately incorporates the given {t['quantum_effect']} duration and energy transfer efficiency in the analysis and simulation design.",
            "The proposed methods for validating simulation results and comparing with given efficiency values are scientifically sound.",
            "The response adheres to the specified word counts for each section and includes a total word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
