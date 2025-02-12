import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "target_language": "Mandarin Chinese",
                "interface_type": "non-invasive EEG",
                "cognitive_focus": "memory enhancement"
            },
            {
                "target_language": "Arabic",
                "interface_type": "invasive neural implant",
                "cognitive_focus": "real-time processing"
            },
            {
                "target_language": "Swahili",
                "interface_type": "transcranial magnetic stimulation",
                "cognitive_focus": "pattern recognition"
            },
            {
                "target_language": "Hindi",
                "interface_type": "functional near-infrared spectroscopy",
                "cognitive_focus": "multitasking ability"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a brain-computer interface (BCI) system for rapid acquisition of {t['target_language']} and real-time translation, using {t['interface_type']} technology. Your system should focus on enhancing {t['cognitive_focus']}. Then, analyze its potential impacts on global communication and cognitive enhancement. Your response should include the following sections:\n\n1. BCI System Architecture (300-350 words):\n   a) Describe the key components of your BCI system for language acquisition and translation.\n   b) Explain how your system interfaces with the brain to facilitate rapid language learning.\n   c) Detail the AI algorithms used for language processing and translation.\n   d) Include a diagram or pseudocode illustrating a key process in your system.\n\n2. Neurolinguistic Mechanism (250-300 words):\n   a) Explain the neuroscientific principles underlying your system's approach to language acquisition.\n   b) Describe how your BCI system leverages or enhances natural language learning processes.\n   c) Discuss any potential neuroplasticity considerations or effects.\n\n3. Language Acquisition and Translation Process (250-300 words):\n   a) Outline the step-by-step process of how a user would acquire {t['target_language']} using your system.\n   b) Explain how the system performs real-time translation, including handling of idioms and cultural context.\n   c) Describe how the system optimizes for {t['cognitive_focus']}.\n\n4. Global Communication Impact Analysis (200-250 words):\n   a) Analyze the potential effects of your system on international relations and cultural exchange.\n   b) Discuss how it might influence the global language landscape and linguistic diversity.\n   c) Consider potential economic and educational impacts of widespread adoption.\n\n5. Cognitive Enhancement Implications (200-250 words):\n   a) Examine how your system might enhance cognitive abilities beyond language skills.\n   b) Discuss potential long-term effects on brain function and structure.\n   c) Consider how this technology might influence human identity and the nature of multilingualism.\n\n6. Ethical Considerations and Safeguards (200-250 words):\n   a) Identify and discuss key ethical issues raised by this technology.\n   b) Propose guidelines for responsible development and use of neural language interfaces.\n   c) Discuss privacy concerns and potential misuse scenarios.\n\n7. Future Directions and Societal Preparation (150-200 words):\n   a) Suggest potential improvements or extensions to your neural language interface system.\n   b) Discuss how society might need to adapt to the widespread availability of this technology.\n   c) Propose a roadmap for integrating neural language interfaces into education and professional settings.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, linguistics, and brain-computer interfaces. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Strive to include novel ideas and approaches that go beyond common solutions in this field.\n\nFor example, when discussing the BCI system architecture, you might consider how {t['interface_type']} could be uniquely leveraged for language acquisition, such as using EEG to detect and reinforce specific neural patterns associated with language learning.\n\nFormat your response with clear headings for each section. Your total response should be between 1500-2000 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of brain-computer interfaces and their application to language acquisition and translation.",
            f"The proposed system for {t['target_language']} acquisition using {t['interface_type']} technology is scientifically plausible.",
            f"The response shows interdisciplinary integration of neuroscience, AI, and linguistics.",
            f"The analysis considers multiple perspectives on the global and cognitive impacts of the technology.",
            f"The ethical analysis is thorough and considers various stakeholder perspectives.",
            "The response includes novel ideas or approaches not explicitly mentioned in the instructions.",
            "The writing uses appropriate scientific terminology from relevant fields.",
            f"The response includes specific technical details related to {t['interface_type']} and how it enhances {t['cognitive_focus']}.",
            "The response is between 1500-2000 words."
        ]
        
        result = eval_with_llm_judge(instructions, submission, criteria)
        if isinstance(result, bool):
            return 1.0 if result else 0.0
        elif isinstance(result, float):
            return result
        else:
            return 0.0
