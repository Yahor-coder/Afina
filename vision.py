from camera import camera
from memory import add_memory, get_memory
from screen import take_screenshot
from chatgpt import analyze_image, analyze_screen, ask_gpt, ask_gpt_with_context


vision_history = []


def see(question="Что ты видишь на этом изображении?"):

    global vision_history

    if not camera.running:
        print("📷 Камера выключена. Включаю...")
        camera.start()

    frame = camera.get_frame()

    if frame is None:
        print("❌ Кадр недоступен")
        return None

    print("👁️ Анализирую новый кадр...")

    context = ""

    if vision_history:
        context = """
Предыдущая история разговора о камере:

"""

        for item in vision_history[-5:]:
            context += f"""
Пользователь: {item["question"]}
Афина: {item["answer"]}
"""

        context += """
Используй эту историю только для понимания контекста.
Текущий кадр имеет приоритет над старой визуальной информацией.
"""

    full_question = f"""
{context}

Новый вопрос пользователя:
{question}
"""

    answer = analyze_image(frame, full_question)

    if answer:

        # Кратковременная память текущего разговора
        vision_history.append({
            "question": question,
            "answer": answer
        })

        vision_history = vision_history[-10:]

        # Долговременная память
        add_memory(question, answer)

    print(f"👁️ Афина видит: {answer}")

    return answer


def ask_vision_memory(question):

    global vision_history

    if not vision_history:
        current_history = ""

    else:
        current_history = ""

        for item in vision_history[-10:]:
            current_history += f"""
Пользователь: {item["question"]}
Афина: {item["answer"]}

"""

    # Загружаем память с диска
    permanent_memory = get_memory()

    permanent_context = ""

    if permanent_memory:
        permanent_context = """
Долговременная память о предыдущих наблюдениях:

"""

        for item in permanent_memory[-20:]:
            permanent_context += f"""
Пользователь: {item["question"]}
Афина: {item["answer"]}

"""

    prompt = f"""
Ты — Афина, голосовой помощник.

Пользователь задаёт вопрос о том,
что Афина видела или говорила раньше.

История текущего разговора:
{current_history}

Предыдущие сохранённые наблюдения:
{permanent_context}

Новый вопрос пользователя:
{question}

Ответь кратко и естественно на русском языке.

Правила:
- используй историю текущего разговора и долговременную память;
- если информация есть в памяти, используй её;
- не придумывай отсутствующие факты;
- не обращайся к камере;
- не утверждай, что старое наблюдение является текущим состоянием;
- если информации недостаточно, честно скажи об этом.
"""

    return ask_gpt_with_context(question, prompt)

def see_screen(question="Что сейчас находится на экране ноутбука?"):

    global vision_history

    # Делаем скриншот экрана Windows
    screenshot = take_screenshot()

    if screenshot is None:
        print("❌ Не удалось получить скриншот")
        return None

    print("🖥️ Анализирую экран...")

    context = ""

    if vision_history:

        context = """
Предыдущая история разговора:

"""

        for item in vision_history[-5:]:
            context += f"""
Пользователь: {item["question"]}
Афина: {item["answer"]}
"""

        context += """
Используй предыдущую историю только для понимания контекста.
Текущий скриншот имеет приоритет.
"""

    full_question = f"""
{context}

Новый вопрос пользователя:
{question}
"""

    answer = analyze_screen(
        screenshot,
        full_question
    )

    if answer:

        vision_history.append({
            "question": question,
            "answer": answer
        })

        vision_history = vision_history[-10:]

        # Сохраняем результат в долговременную память
        add_memory(question, answer)

    print(f"🖥️ Афина видит на экране: {answer}")

    return answer