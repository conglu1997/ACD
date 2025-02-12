class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": [
                "The neighborhood should include 10 houses, 2 parks, 3 shops, and 1 school.",
                "Houses should not be adjacent to shops.",
                "Parks should be evenly distributed across the neighborhood.",
                "The school should be centrally located.",
                "Provide the layout as a 5x5 grid with labeled locations."
            ]},
            "2": {"criteria": [
                "The neighborhood should include 15 houses, 1 park, 4 shops, 1 hospital, and 2 schools.",
                "Houses should not be adjacent to shops or the hospital.",
                "The park should be near the center of the neighborhood.",
                "One of the schools should be at the edge of the neighborhood.",
                "Provide the layout as a 6x6 grid with labeled locations."
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a small neighborhood layout based on the given criteria. Ensure that your design adheres to all the specified constraints and provide the layout as a grid with labeled locations.

Criteria:
{chr(10).join(t['criteria'])}

Provide your response in plain text format, using a grid representation with labeled locations (e.g., H for house, P for park, S for shop, C for school, Hs for hospital). Each cell in the grid should be represented by one of these labels, and the grid should be clearly formatted with rows and columns. For example:

H H P H S
H H P H S
C H P H S
H H P H S
H H P H S

Ensure that the grid follows these constraints and is easy to read."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The layout must include all specified elements (houses, parks, shops, schools, etc.).",
            "The layout must adhere to the adjacency constraints.",
            "The layout must be clear and easy to understand.",
            "The layout must use the correct grid size as specified in the criteria.",
            "The labels in the grid must match the specified format (H, P, S, C, Hs)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
