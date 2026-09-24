from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
files = sorted((root / "playbooks").glob("*.md"))
assert len(files) == 6, "Expected six playbooks"
sections = ["Trigger", "Input", "Checks", "AI assistance", "Exceptions", "Human decision", "Action", "Evidence retained", "Escalation", "Output", "Procedure", "Acceptance scenarios", "Agent operating contract"]
for f in files:
    text = f.read_text()
    for section in sections:
        assert f"## {section}\n" in text, (f.name, section)
    assert len(text.split()) > 1800, (f.name, "insufficient depth")
    assert text.count("```") % 2 == 0, (f.name, "unbalanced fence")
    for control in ["READ_AND_DRAFT", "UNVERIFIED", "SOURCE FACT", "INTERPRETATION", "ASSUMPTION", "PROPOSED ACTION", "BLOCKED"]:
        assert control in text, (f.name, control)
    print(f"PASS {f.name}: {len(text.split())} words")
for f in root.glob("*.md"):
    for target in re.findall(r"\]\(([^)]+)\)", f.read_text()):
        if not target.startswith(("https://", "http://", "#")):
            assert (f.parent / target).exists(), (f.name, target)
print("PASS: six standalone structures and local links. This does not validate model behaviour or legal accuracy.")
