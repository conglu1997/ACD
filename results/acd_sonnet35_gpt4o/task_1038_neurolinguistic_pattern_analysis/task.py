import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "metaphor_type": "Conceptual",
                "linguistic_feature": "Semantic similarity",
                "imaging_technique": "fMRI"
            },
            {
                "metaphor_type": "Novel",
                "linguistic_feature": "Syntactic complexity",
                "imaging_technique": "EEG"
            },
            {
                "metaphor_type": "Conventional",
                "linguistic_feature": "Lexical ambiguity",
                "imaging_technique": "MEG"
            },
            {
                "metaphor_type": "Primary",
                "linguistic_feature": "Phonological patterns",
                "imaging_technique": "fNIRS"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a computational experiment to investigate the neural correlates of {t['metaphor_type']} metaphor processing in the brain, focusing on the linguistic feature of {t['linguistic_feature']} and using {t['imaging_technique']} as the imaging technique. Your response should include:\n\n" \
               f"1. Experimental Design (250-300 words):\n" \
               f"   a) Describe the overall structure of your experiment, including participant selection, stimuli, and task design.\n" \
               f"   b) Explain how your design specifically targets {t['metaphor_type']} metaphors and {t['linguistic_feature']}.\n" \
               f"   c) Justify your choice of {t['imaging_technique']} and describe any specific acquisition parameters.\n\n" \
               f"2. Data Analysis Pipeline (200-250 words):\n" \
               f"   a) Outline the steps in your data analysis pipeline, from preprocessing to statistical analysis.\n" \
               f"   b) Describe any novel or advanced analysis techniques you would employ.\n" \
               f"   c) Explain how your analysis will isolate the neural correlates of metaphor processing.\n\n" \
               f"3. Machine Learning Integration (200-250 words):\n" \
               f"   a) Propose a machine learning approach to complement your analysis.\n" \
               f"   b) Describe the architecture of your model and its training procedure.\n" \
               f"   c) Explain how this ML approach enhances our understanding of metaphor processing.\n\n" \
               f"4. Interdisciplinary Connections (150-200 words):\n" \
               f"   a) Discuss how your experiment integrates principles from neuroscience, linguistics, and computer science.\n" \
               f"   b) Explain how this integration provides unique insights into metaphor processing.\n\n" \
               f"5. Potential Outcomes and Implications (150-200 words):\n" \
               f"   a) Predict potential outcomes of your experiment and their implications for our understanding of language processing in the brain.\n" \
               f"   b) Discuss how your findings could inform theories of metaphor comprehension and production.\n\n" \
               f"6. Limitations and Future Directions (100-150 words):\n" \
               f"   a) Identify potential limitations of your experimental design and analysis approach.\n" \
               f"   b) Propose future studies or extensions to address these limitations.\n\n" \
               f"Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and machine learning principles. Be innovative in your approach while maintaining scientific rigor and plausibility. Use appropriate terminology and provide clear explanations of complex concepts.\n\n" \
               f"Format your answer with clear headings for each section. Your total response should be between 1050-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The experimental design effectively targets {t['metaphor_type']} metaphors and {t['linguistic_feature']}.",
            f"The use of {t['imaging_technique']} is well-justified and appropriately described.",
            "The data analysis pipeline is comprehensive and includes advanced techniques.",
            "The machine learning approach is innovative and well-integrated with the overall experiment.",
            "The response demonstrates a deep understanding of neuroscience, linguistics, and machine learning principles.",
            "The interdisciplinary connections are clearly explained and provide unique insights.",
            "Potential outcomes and implications are thoughtfully considered and scientifically plausible.",
            "Limitations are accurately identified and future directions are appropriately proposed.",
            "The response is well-structured, using appropriate terminology and clear explanations throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
