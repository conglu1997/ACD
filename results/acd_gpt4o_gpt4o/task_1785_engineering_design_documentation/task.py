class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "project": "Design a bridge",
                "specifications": {
                    "length": "200 meters",
                    "type": "suspension",
                    "materials": ["steel", "concrete"],
                    "load_capacity": "5000 tons",
                    "environmental_conditions": "coastal, high winds"
                }
            },
            "2": {
                "project": "Design a wind turbine",
                "specifications": {
                    "height": "150 meters",
                    "rotor_diameter": "120 meters",
                    "materials": ["composite", "steel"],
                    "power_output": "3 MW",
                    "location": "offshore"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        project = t["project"]
        specifications = t["specifications"]
        instructions = f"""Your task is to generate a detailed engineering design document for the following project based on the given specifications and constraints.

Project: {project}
Specifications:
"""
        for spec, value in specifications.items():
            instructions += f"- {spec.capitalize()}: {value}\n"
        instructions += """

Your design document should include the following sections:
1. Introduction: Briefly describe the project and its objectives.
2. Specifications: List and explain the given specifications and any additional assumptions.
3. Design Approach: Describe the approach you will take to meet the specifications and constraints. Include diagrams or sketches if necessary.
4. Materials: Justify the choice of materials and their suitability for the project.
5. Load Analysis: Discuss the load capacity and how the design ensures safety and stability.
6. Environmental Considerations: Explain how the design accounts for environmental conditions.
7. Conclusion: Summarize the key points and the expected outcomes of the design.

Ensure your document is well-structured, detailed, and technically accurate. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The introduction should clearly describe the project and its objectives.",
            "The specifications should be listed and explained accurately.",
            "The design approach should be detailed and logical.",
            "The materials section should justify the choice of materials and their suitability.",
            "The load analysis should discuss safety and stability.",
            "The environmental considerations should explain how the design accounts for environmental conditions.",
            "The conclusion should summarize the key points and expected outcomes.",
            "The document should be well-structured and technically accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
