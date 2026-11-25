"""Audit paired images and YOLO detection labels without reading image contents."""
import argparse
import json
from pathlib import Path

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

def validate_annotations(path, classes):
    """Return line-numbered errors for one YOLO detection label file."""
    errors = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fields = line.split()
        if not fields:
            continue
        try:
            if len(fields) != 5:
                raise ValueError
            class_id = int(fields[0])
            x, y, width, height = map(float, fields[1:])
            if not 0 <= class_id < classes:
                raise ValueError
            if not (0 < width <= 1 and 0 < height <= 1):
                raise ValueError
            tolerance = 1e-9
            if not (width / 2 - tolerance <= x <= 1 - width / 2 + tolerance
                    and height / 2 - tolerance <= y <= 1 - height / 2 + tolerance):
                raise ValueError
        except ValueError:
            errors.append(f"line {number}: invalid class or normalized bounding box")
    return errors

def inventory(root, extensions):
    entries = {}
    duplicates = []
    for file in sorted(root.rglob("*")):
        if file.is_symlink() or not file.is_file() or file.suffix.lower() not in extensions:
            continue
        key = file.relative_to(root).with_suffix("").as_posix()
        if key in entries:
            duplicates.append(key)
        entries[key] = file
    return entries, duplicates

def audit(images, labels, classes):
    if not images.is_dir() or not labels.is_dir() or classes < 1:
        raise ValueError("Supply two existing directories and a positive class count.")
    image_files, duplicates = inventory(images, IMAGE_EXTENSIONS)
    label_files, duplicate_labels = inventory(labels, {".txt"})
    issues = [{"type": "no_images"}] if not image_files else []
    for kind, keys in (
        ("duplicate_image", duplicates),
        ("duplicate_label", duplicate_labels),
        ("missing_label", sorted(image_files.keys() - label_files.keys())),
        ("orphan_label", sorted(label_files.keys() - image_files.keys())),
    ):
        issues.extend({"type": kind, "sample": key} for key in keys)
    for key, file in label_files.items():
        try:
            errors = validate_annotations(file, classes)
        except (UnicodeError, OSError):
            errors = ["unreadable UTF-8 label"]
        issues.extend({"type": "invalid_label", "sample": key, "detail": error}
                      for error in errors)
    return {"images": len(image_files), "labels": len(label_files), "issues": issues}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images", type=Path)
    parser.add_argument("labels", type=Path)
    parser.add_argument("--classes", type=int, required=True)
    args = parser.parse_args()
    try:
        report = audit(args.images, args.labels, args.classes)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(report, indent=2))
    return int(bool(report["issues"]))

if __name__ == "__main__":
    raise SystemExit(main())
