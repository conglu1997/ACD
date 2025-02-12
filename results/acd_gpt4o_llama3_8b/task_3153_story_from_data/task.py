class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": {
                    "headers": ["Year", "Event"],
                    "rows": [
                        ["2020", "Global pandemic starts"],
                        ["2021", "Vaccination rollout begins"],
                        ["2022", "Economic recovery efforts"],
                        ["2023", "Return to normalcy"]
                    ]
                },
                "challenge": "Generate a narrative based on the provided data about significant events from 2020 to 2023."
            },
            "2": {
                "data": {
                    "headers": ["Year", "Discovery", "Impact"],
                    "rows": [
                        ["2000", "Human Genome Project completed", "Advancement in genetic research"],
                        ["2005", "Discovery of water on Mars", "Increased interest in space exploration"],
                        ["2010", "Development of CRISPR technology", "Revolution in genetic engineering"],
                        ["2015", "First image of a black hole", "Breakthrough in astrophysics"]
                    ]
                },
                "challenge": "Generate a narrative based on the provided data about significant scientific discoveries from 2000 to 2015 and their impacts."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        headers = ', '.join(t['data']['headers'])
        rows = '\n'.join([', '.join(row) for row in t['data']['rows']])
        data_str = f"Headers: {headers}\nRows:\n{rows}"
        return f"""Based on the following structured data, generate a coherent and engaging narrative. Ensure that your narrative accurately reflects the events and their significance as presented in the data.\n\n{data_str}\n\nSubmit your response as a plain text string with the following sections:\n\n1. Narrative: [Your narrative here]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should accurately reflect the events and their significance as presented in the data.",
            "The narrative should be coherent and engaging.",
            "The narrative should maintain logical consistency and chronological order.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
