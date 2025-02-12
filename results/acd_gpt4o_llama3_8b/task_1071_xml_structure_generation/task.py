class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create an XML structure representing a library. The library should have multiple categories, each category should have multiple books, and each book should have a title, author, and publication year."
            },
            "2": {"description": "Create an XML structure representing a music album collection. The collection should have multiple albums, each album should have a title, artist, release year, and a list of songs. Each song should have a title and duration."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a well-formed XML structure based on the following description: '{t['description']}'. Ensure the XML is properly formatted, logically organized, and includes all necessary elements as described. Example format: \n<library>\n  <category name='Fiction'>\n    <book>\n      <title>Book Title</title>\n      <author>Author Name</author>\n      <year>2000</year>\n    </book>\n  </category>\n</library>. Submit your XML as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Additional criteria to ensure XML structure correctness
        criteria = ["The XML structure should include all described elements.", "The XML should be well-formed and properly nested.", "The XML should follow the logical organization specified in the description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
