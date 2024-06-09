"""
<EN>
Application Entry Point

This script serves as the entry point for running the Flask application. It imports the Flask application instance from
the app module and starts the server in debug mode.

Usage:
    Run this script to start the Flask application server.
Modules:
    app: The Flask application instance.
Execution:
    if __name__ == "__main__":
        app.run(debug=True): Start the Flask server in debug mode.
"""
"""
<RUS>
Точка входа приложения

Этот скрипт служит точкой входа для запуска Flask-приложения. Он импортирует экземпляр приложения Flask из модуля
app и запускает сервер в режиме отладки.

Использование:
    Запустите этот скрипт, чтобы запустить сервер Flask-приложения.
Модули:
    app: Экземпляр Flask-приложения.
Выполнение:
    if __name__ == "__main__":
        app.run(debug=True): Запускает сервер Flask в режиме отладки.
"""

from app import app

if __name__ == "__main__":
    app.run(debug=True)
