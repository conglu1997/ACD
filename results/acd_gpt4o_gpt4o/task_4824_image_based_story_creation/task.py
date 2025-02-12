class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "image": "/9j/4AAQSkZJRgABAQEAAAAAAAD/4QBcRXhpZgAATU0AKgAAAAgABQEAAAMAAAABAAEAAAEBAAMAAAABAAEAAAECAAMAAAABAAEAAAEGAAMAAAABAAEAAAEIAAMAAAABAAEAAAAAAAD/2wBDAAoHBwkHBgoJCAkLCwoMDxkQDw4NFBMVGRYTFhUaHBYnJygnICUsICk9Pj3QDR5ESExQcjoxPj4/2wBDAQsLCwwMFBQNDxkQEBkYNTxERERPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09P/waAAwDAQACEAMQAAABzWx0ZXJ5IGltYWdlIG9mIGEgZmFudGFzeSBnb2xkZW4gdHJlZSByaXAgd2l0aCBsYWtlIGFuZCBtb3VudGFpbnMgaW4gdGhlIGJhY2tncm91bmQuIFRoZSBzdW4gaXMgc2V0dGluZy4uLmFuZCBhIHNvZnQgbGFrZSBpcyByZWZsZWN0aW5nIHRoZSBsaWdodA==" # Placeholder for encoded base64 image string
            },
            "2": {
                "image": "/9j/4AAQSkZJRgABAQEAAAAAAAD/4QBcRXhpZgAATU0AKgAAAAgABQEAAAMAAAABAAEAAAEBAAMAAAABAAEAAAECAAMAAAABAAEAAAEGAAMAAAABAAEAAAEIAAMAAAABAAEAAAAAAAD/2wBDAAoHBwkHBgoJCAkLCwoMDxkQDw4NFBMVGRYTFhUaHBYnJygnICUsICk9Pj3QDR5ESExQcjoxPj4/2wBDAQsLCwwMFBQNDxkQEBkYNTxERERPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09P/waAAwDAQACEAMQAAABzWx0ZXJ5IGltYWdlIG9mIGEgc3RhbGxpb24gb3Zlcmxvb2tpbmcgYSBjaXR5IHdpdGggc3RlZWwgYnJpZGdlcywgYnVpbGRpbmdzLCBhbmQgc2t5c2NyYXBlcnMuIFRoZSBza3kgaXMgb3JhbmdlIGNvbG9yZWQgcmVmbGVjdGluZyB0aGUgc2V0dGluZy4uLi4gYW5kIHRoZSBjaXR5IGxvb2tzIGFsaXZlIHdpdGggYWN0aXZpdHku" # Placeholder for encoded base64 image string
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a coherent and creative story based on the given image.

Image: {t['image']}

Provide your story in plain text format, structured as follows:

Title: [Title of your story]
Story: [Your story]

Ensure your story is between 200 and 500 words. The story should be imaginative, well-structured, and clearly connected to the image. Creativity and coherence are essential for a successful story."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be coherent and creative.", "The story should be clearly connected to the given image.", "The story should be well-structured and imaginative.", "The story should be between 200 and 500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
