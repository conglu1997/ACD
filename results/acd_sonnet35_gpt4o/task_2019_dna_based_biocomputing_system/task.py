class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data_type": "genomic sequences",
                "processing_task": "protein folding prediction",
                "system_constraint": "energy efficiency",
                "problem_size": "1 million protein sequences",
                "time_constraint": "24 hours",
                "comparison_system": "Summit supercomputer"
            },
            "2": {
                "data_type": "environmental sensor data",
                "processing_task": "global climate model simulation",
                "system_constraint": "scalability",
                "problem_size": "10 petabytes of historical climate data",
                "time_constraint": "1 week",
                "comparison_system": "Google's Sycamore quantum processor"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a DNA-based biological computing system for massive data storage and parallel processing of {t['data_type']}, focusing on the task of {t['processing_task']}. Your system should prioritize {t['system_constraint']} and be capable of handling {t['problem_size']} within {t['time_constraint']}. Compare your system's performance to the {t['comparison_system']}. Your response must follow this exact structure and include all of the following sections:

        1. System Architecture (250-300 words):
           a) Describe the key components of your DNA-based biocomputing system.
           b) Explain how data is encoded, stored, and retrieved using DNA.
           c) Detail the mechanisms for parallel processing in your system.
           d) Include a simple diagram or flowchart of your system architecture using ASCII art or Unicode characters (max 20 lines by 80 characters).

        2. DNA Encoding Scheme (200-250 words):
           a) Explain your method for encoding {t['data_type']} into DNA sequences.
           b) Discuss how your encoding scheme optimizes for storage density and error correction.
           c) Provide an example of how a specific data point would be encoded, including the actual DNA sequence used.
           d) Calculate the theoretical maximum storage density of your system in bits/cm³.

        3. Parallel Processing Mechanism (200-250 words):
           a) Describe how your system performs parallel computations for {t['processing_task']}.
           b) Explain how you leverage the massive parallelism of DNA-based systems.
           c) Discuss any novel approaches to DNA-based logic gates or computational units in your design.
           d) Provide a specific example of how a single computation step would be performed, including the DNA operations involved.
           e) Calculate the theoretical processing speed of your system in operations per second.

        4. {t['system_constraint'].capitalize()} Analysis (150-200 words):
           a) Analyze how your system design addresses the constraint of {t['system_constraint']}.
           b) Compare your system's {t['system_constraint']} to traditional computing systems using specific metrics.
           c) Discuss potential trade-offs or limitations related to this constraint.

        5. Problem-Solving Approach (200-250 words):
           a) Explain how your system would approach solving the {t['processing_task']} problem with the given {t['problem_size']}.
           b) Provide a step-by-step breakdown of the problem-solving process.
           c) Estimate the time and resource requirements for each step, demonstrating how you meet the {t['time_constraint']} constraint.
           d) Address potential failure modes and propose error correction mechanisms specific to DNA-based computing.

        6. Performance Comparison (200-250 words):
           a) Compare the performance of your DNA-based system to the {t['comparison_system']} for the given {t['processing_task']}.
           b) Provide quantitative estimates for processing speed, energy efficiency, and scalability for both systems.
           c) Discuss the advantages and disadvantages of your system compared to the {t['comparison_system']}.
           d) Explain any assumptions made in your comparison and how they might affect the results.

        7. Broader Implications (150-200 words):
           a) Explore potential applications of your system beyond {t['processing_task']}.
           b) Discuss how your system could impact the field of {t['processing_task']}.
           c) Consider potential societal or ethical implications of widespread adoption of DNA-based biocomputing.
           d) Suggest a research question that could further advance DNA-based biocomputing.

        Ensure your response demonstrates a deep understanding of molecular biology, information theory, computer architecture, and the specific domain of {t['processing_task']}. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

        Format your answer with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words. Include a word count at the end of each section and a total word count at the end of your response.

        Note: Your response will be evaluated based on the completeness, accuracy, creativity, and plausibility of your DNA-based biocomputing system design, as well as your ability to address the specific problem and constraints provided. Partial credit may be given for responses that meet some but not all criteria.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and adheres to the specified word counts.",
            "The system architecture is well-described and includes a clear ASCII art or Unicode diagram (max 20 lines by 80 characters).",
            f"The DNA encoding scheme demonstrates a plausible method for encoding {t['data_type']} with considerations for storage density and error correction, including a specific example and a calculation of theoretical maximum storage density.",
            f"The parallel processing mechanism is thoroughly explained and addresses the specific task of {t['processing_task']}, with a concrete example of a computation step and a calculation of theoretical processing speed.",
            f"The {t['system_constraint']} analysis provides insightful comparisons to traditional computing systems using specific metrics and addresses potential trade-offs.",
            f"The problem-solving approach demonstrates a feasible method for tackling the {t['processing_task']} problem with {t['problem_size']}, including time and resource estimates that meet the {t['time_constraint']} constraint, and addresses potential failure modes and error correction mechanisms.",
            f"The performance comparison provides a detailed, quantitative analysis comparing the DNA-based system to the {t['comparison_system']}, including processing speed, energy efficiency, and scalability estimates.",
            "The broader implications section explores innovative uses of the system, considers ethical implications, and suggests a relevant research question.",
            "The overall response shows deep understanding and integration of molecular biology, information theory, computer architecture, and domain-specific knowledge, using appropriate technical terminology.",
            "The response stays within the overall word limit of 1350-1700 words and includes word counts for each section and the total."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
