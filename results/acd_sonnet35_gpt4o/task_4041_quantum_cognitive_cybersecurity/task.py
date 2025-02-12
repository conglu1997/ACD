class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_principle": "Quantum entanglement",
                "cognitive_aspect": "Attention allocation",
                "cybersecurity_focus": "Network intrusion detection",
                "threat_scenario": "Advanced persistent threat (APT)"
            },
            "2": {
                "quantum_principle": "Quantum superposition",
                "cognitive_aspect": "Decision-making under uncertainty",
                "cybersecurity_focus": "Encryption key management",
                "threat_scenario": "Quantum computing-based cryptanalysis"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing-based cybersecurity system that incorporates principles of cognitive science to enhance human-machine interaction and decision-making in threat detection and response. Your system should focus on the quantum principle of {t['quantum_principle']}, the cognitive aspect of {t['cognitive_aspect']}, and address the cybersecurity focus of {t['cybersecurity_focus']}. Consider the threat scenario of {t['threat_scenario']} in your design.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum cognitive cybersecurity system.
   b) Explain how quantum computing is integrated into the cybersecurity framework.
   c) Detail how cognitive science principles are incorporated to enhance human-machine interaction.
   d) Discuss how your system addresses the specified cybersecurity focus.
   e) Include a high-level diagram of your system architecture (described textually).

2. Quantum-Enhanced Threat Detection (250-300 words):
   a) Explain how your system uses the specified quantum principle to improve threat detection.
   b) Describe the quantum algorithms or techniques employed in your system.
   c) Discuss how quantum computing provides an advantage over classical methods in this context.
   d) Provide an example of how your system would detect a potential threat using quantum techniques.

3. Cognitive Science Integration (250-300 words):
   a) Detail how your system incorporates the specified cognitive aspect to enhance cybersecurity operations.
   b) Explain how this cognitive integration improves human-machine interaction and decision-making.
   c) Describe any novel interfaces or visualization techniques used to leverage human cognitive abilities.
   d) Discuss how your system adapts to individual users' cognitive patterns or preferences.

4. Threat Scenario Analysis (200-250 words):
   a) Analyze how your system would respond to the specified threat scenario.
   b) Describe the step-by-step process of threat detection, analysis, and response.
   c) Explain how quantum computing and cognitive science principles contribute to addressing this specific threat.

5. Performance Evaluation (150-200 words):
   a) Propose metrics to evaluate the effectiveness of your quantum cognitive cybersecurity system.
   b) Describe how you would test the system's performance against both classical and quantum-based cyber threats.
   c) Discuss the challenges in measuring the impact of cognitive science integration on system performance.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss the ethical considerations of using quantum computing and cognitive science in cybersecurity.
   b) Analyze potential societal impacts, both positive and negative, of widespread adoption of such systems.
   c) Address privacy concerns related to the cognitive aspects of your system.

7. Future Developments and Limitations (150-200 words):
   a) Identify current limitations of your proposed system.
   b) Suggest areas for future research and development in quantum cognitive cybersecurity.
   c) Speculate on potential long-term implications for the fields of quantum computing, cognitive science, and cybersecurity.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, and cybersecurity. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, cognitive science, and cybersecurity, particularly in relation to {t['quantum_principle']}, {t['cognitive_aspect']}, and {t['cybersecurity_focus']}.",
            "The system architecture effectively integrates quantum computing and cognitive science principles into a cybersecurity framework.",
            f"The quantum-enhanced threat detection section clearly explains how {t['quantum_principle']} is used to improve threat detection.",
            f"The cognitive science integration section effectively incorporates {t['cognitive_aspect']} to enhance cybersecurity operations and human-machine interaction.",
            f"The threat scenario analysis provides a plausible and detailed response to the {t['threat_scenario']} scenario.",
            "The performance evaluation section proposes relevant metrics and testing methods for the system.",
            "The response addresses ethical implications and potential societal impacts of the proposed system.",
            "The ideas presented are innovative while maintaining scientific and technological plausibility.",
            "The response is well-structured, following the outlined sections and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
