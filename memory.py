import json
import os


MEMORY_FILE = "vision_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            memory,
            file,
            ensure_ascii=False,
            indent=2
        )


def add_memory(question, answer):
    memory = load_memory()

    memory.append({
        "question": question,
        "answer": answer
    })

    # Храним максимум 50 последних наблюдений
    memory = memory[-50:]

    save_memory(memory)


def get_memory():
    return load_memory()


def clear_memory():
    save_memory([])