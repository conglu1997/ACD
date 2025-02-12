import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            "Entanglement",
            "Superposition",
            "Quantum tunneling"
        ]
        climate_indicators = [
            "Atmospheric CO2 levels",
            "Ocean acidification",
            "Polar ice mass"
        ]
        policy_areas = [
            "Carbon pricing",
            "Renewable energy transition",
            "Biodiversity conservation"
        ]
        tasks = [
            {
                "quantum_property": prop,
                "climate_indicator": indicator,
                "policy_area": policy
            }
            for prop in quantum_properties
            for indicator in climate_indicators
            for policy in policy_areas
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based biosensor system for real-time monitoring of global climate change indicators and analyze its potential impact on environmental policy. Your system should utilize the quantum property of {t['quantum_property']}, focus on monitoring {t['climate_indicator']}, and analyze its impact on {t['policy_area']}. Your response should include:

1. Quantum Biosensor Design (approximately 250 words):
   a) Describe the key components of your quantum biosensor system.
   b) Explain how it leverages {t['quantum_property']} for enhanced sensitivity or efficiency.
   c) Detail how the system interfaces with biological elements to detect {t['climate_indicator']}.
   d) Discuss any novel approaches or materials used in your design.
   e) Optionally, describe the visual layout or key features of your quantum biosensor system.

2. Detection Mechanism (approximately 200 words):
   a) Explain the specific mechanism by which your biosensor detects changes in {t['climate_indicator']}.
   b) Describe how quantum effects enhance the detection process.
   c) Discuss the sensitivity and accuracy of your system compared to classical methods.

3. Data Collection and Analysis (approximately 200 words):
   a) Outline how your system collects and processes data in real-time.
   b) Explain any quantum algorithms or techniques used for data analysis.
   c) Discuss how your system handles potential quantum decoherence or environmental interference.

4. Global Monitoring Network (approximately 150 words):
   a) Propose a strategy for deploying your quantum biosensors on a global scale.
   b) Discuss challenges in maintaining quantum coherence across a distributed network.
   c) Explain how data from multiple sensors would be integrated and analyzed.

5. Environmental Policy Impact (approximately 200 words):
   a) Analyze how real-time, high-precision monitoring of {t['climate_indicator']} could impact {t['policy_area']}.
   b) Discuss potential changes in policy-making processes or enforcement strategies.
   c) Identify any potential unintended consequences of implementing your system.

6. Ethical and Societal Implications (approximately 150 words):
   a) Discuss ethical considerations related to global quantum-based environmental monitoring.
   b) Analyze potential societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of such technology.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, climate science, and environmental policy. Use technical terminology appropriately and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be approximately 1150-1450 words. Reference relevant scientific concepts or theories throughout your response where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates understanding of quantum mechanics, biology, climate science, and environmental policy.",
            "The quantum biosensor design utilizes the specified quantum property and is scientifically plausible.",
            "The detection mechanism and data analysis processes are explained clearly.",
            "The global monitoring network strategy addresses key challenges.",
            "The analysis of environmental policy impact considers multiple perspectives.",
            "Ethical and societal implications are considered.",
            "The response uses appropriate terminology and provides explanations for complex concepts.",
            "The response is well-structured with clear headings for each section.",
            "Scientific concepts or theories are referenced where appropriate."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score