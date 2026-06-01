class ChangelogGenerator:
    """
    Commit Parsing Changelog Generator
    Structures and categorizes Git commits into clean markdown headings.
    """
    def generate_release_notes(self, commits):
        notes = {"Features": [], "Bug Fixes": [], "Performance": []}
        for commit in commits:
            if commit.startswith("feat:"):
                notes["Features"].append(commit[5:].strip())
            elif commit.startswith("fix:"):
                notes["Bug Fixes"].append(commit[4:].strip())
        return notes

if __name__ == "__main__":
    generator = ChangelogGenerator()
    notes = generator.generate_release_notes(["feat: Add new UI widgets", "fix: Fix memory leak"])
    print("Compiled Markdown Notes:")
    print(notes)
