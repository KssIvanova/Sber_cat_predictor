from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from phrases import PREDICTIONS, CAT_PHRASES

# Инициализация приложения
app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

def generate_prediction():
    """Генерация предсказания с кошачьей фразой"""
    prediction = random.choice(PREDICTIONS)
    cat_phrase = random.choice(CAT_PHRASES)
    return f"{prediction} {cat_phrase}"

@app.post("/webhook")
async def webhook(request: Request):
    """Обработчик веб-хуков от Sber Smart App"""
    try:
        data = await request.json()
        command = data.get("command", "").lower()
        
        if "предсказание" in command or "предскажи" in command or "что меня ждет" in command:
            prediction = generate_prediction()
            return JSONResponse(
                content={
                    "response": {
                        "text": prediction,
                        "tts": prediction,
                        "end_session": False
                    }
                }
            )
            
        elif "помощь" in command:
            help_text = (
                "Я - милый котик, который предсказывает будущее! "
                "Спросите меня 'что меня ждет' или 'дай предсказание', "
                "и я расскажу, что вас ожидает сегодня!"
            )
            return JSONResponse(
                content={
                    "response": {
                        "text": help_text,
                        "tts": help_text,
                        "end_session": False
                    }
                }
            )
            
        else:
            return JSONResponse(
                content={
                    "response": {
                        "text": "Мяу? Я не понял вашу команду. Скажите 'помощь' для получения справки.",
                        "tts": "Мяу? Я не понял вашу команду. Скажите 'помощь' для получения справки.",
                        "end_session": False
                    }
                }
            )
            
    except Exception as e:
        return JSONResponse(
            content={
                "response": {
                    "text": f"Мяу... Произошла ошибка: {str(e)}",
                    "tts": f"Мяу... Произошла ошибка: {str(e)}",
                    "end_session": False
                }
            }
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 