import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biomolecules = [
            {
                "name": "DNA",
                "properties": "High information density, stable long-term storage"
            },
            {
                "name": "RNA",
                "properties": "Versatile, can catalyze chemical reactions"
            },
            {
                "name": "Proteins",
                "properties": "Diverse structures and functions, capable of complex interactions"
            },
            {
                "name": "Lipids",
                "properties": "Self-assembling, can form membranes and compartments"
            }
        ]
        
        processing_mechanisms = [
            {
                "name": "Enzyme-based computation",
                "description": "Use biological catalysts to perform logical operations"
            },
            {
                "name": "Conformational changes",
                "description": "Utilize changes in molecular shape to store and process information"
            },
            {
                "name": "Molecular recognition",
                "description": "Exploit specific binding interactions for information processing"
            },
            {
                "name": "Self-assembly",
                "description": "Harness spontaneous organization of molecules for computation"
            }
        ]
        
        scenarios = [
            {
                "name": "Medical diagnostics",
                "description": "Develop a system to detect and analyze multiple biomarkers simultaneously"
            },
            {
                "name": "Environmental monitoring",
                "description": "Create a bio-sensor network for real-time pollution detection in water systems"
            },
            {
                "name": "Data archiving",
                "description": "Design a long-term, high-density data storage system for archiving historical records"
            }
        ]
        
        task = {
            "biomolecule": random.choice(biomolecules),
            "processing_mechanism": random.choice(processing_mechanisms),
            "scenario": random.choice(scenarios)
        }
        
        return {"1": task, "2": task}

    @staticmethod
    def get_instructions(t: dict) -> str:
        biomolecule = t["biomolecule"]
        processing_mechanism = t["processing_mechanism"]
        scenario = t["scenario"]
        
        return f"Design a bio-inspired molecular system for information storage and processing using {biomolecule['name']} as the primary biomolecule and {processing_mechanism['name']} as the main processing mechanism. Then, analyze its theoretical performance, potential applications, and experimental validation, with a focus on the following scenario: {scenario['name']} - {scenario['description']}. Your response should include:\n\n" \
               f"1. System Architecture (250-300 words):\n" \
               f"   a) Describe the overall structure and key components of your bio-molecular data architecture.\n" \
               f"   b) Explain how you utilize the properties of {biomolecule['name']}: {biomolecule['properties']}.\n" \
               f"   c) Detail how you implement {processing_mechanism['name']}: {processing_mechanism['description']}.\n" \
               f"   d) Include a diagram or schematic representation of your system (use ASCII art).\n\n" \
               f"2. Information Encoding and Processing (200-250 words):\n" \
               f"   a) Describe your method for encoding information in the biomolecular system.\n" \
               f"   b) Explain the process of reading and writing data in your architecture.\n" \
               f"   c) Detail how your system performs basic computational operations.\n" \
               f"   d) Provide an example of how your system would process a simple instruction or data query related to the given scenario.\n\n" \
               f"3. Error Detection and Correction (150-200 words):\n" \
               f"   a) Describe the error detection and correction mechanisms in your bio-molecular system.\n" \
               f"   b) Explain how these mechanisms ensure data integrity and reliability.\n" \
               f"   c) Compare your approach to error handling with traditional electronic systems.\n\n" \
               f"4. Theoretical Performance Analysis (200-250 words):\n" \
               f"   a) Estimate the information density (in bits/cm³) and storage capacity (in TB) of your system.\n" \
               f"   b) Analyze the energy efficiency of data storage and processing in your architecture (in operations/joule).\n" \
               f"   c) Discuss the theoretical speed of operations in your system (in operations/second).\n" \
               f"   d) Compare your system's performance to current electronic-based storage and processing systems.\n" \
               f"   e) Compare and contrast your proposed system with at least one alternative bio-molecular approach.\n\n" \
               f"5. Challenges and Limitations (150-200 words):\n" \
               f"   a) Identify potential challenges in implementing your bio-molecular data architecture.\n" \
               f"   b) Discuss any limitations in terms of scalability, stability, or functionality.\n" \
               f"   c) Propose potential solutions or areas for future research to address these challenges.\n\n" \
               f"6. Potential Applications (150-200 words):\n" \
               f"   a) Suggest three potential applications of your bio-molecular data architecture, including the given scenario.\n" \
               f"   b) Explain how each application leverages the unique properties of your system.\n" \
               f"   c) Discuss any ethical considerations related to these applications.\n\n" \
               f"7. Experimental Validation (200-250 words):\n" \
               f"   a) Propose a simple experiment to validate a key aspect of your bio-molecular data architecture.\n" \
               f"   b) Describe the experimental setup, including any necessary equipment or materials.\n" \
               f"   c) Explain what results would support or refute your design.\n" \
               f"   d) Discuss potential challenges in conducting this experiment and how you would address them.\n\n" \
               f"Ensure your response demonstrates a deep understanding of molecular biology, information theory, and experimental design. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\n" \
               f"Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words. Include a word count at the end of your submission."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of molecular biology, information theory, and experimental design.",
            "The bio-molecular data architecture design is creative, plausible, and well-explained, with a clear schematic representation.",
            "The system's information encoding, processing, and error correction mechanisms are thoroughly described and analyzed.",
            "The theoretical performance analysis includes accurate quantitative estimates and a comparison with alternative approaches.",
            "Challenges, limitations, and potential applications are thoughtfully discussed, with consideration of the given scenario.",
            "The proposed experimental validation is well-designed and directly relevant to the bio-molecular data architecture.",
            "The submission is well-structured, follows the required format, and adheres to the word count guidelines."
        ]
        try:
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        except Exception as e:
            print(f"Error in scoring: {e}")
            return 0.0
