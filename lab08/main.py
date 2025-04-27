from appJar import gui
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class ScrapingError(Exception): # Базовое исключение для ошибок скрейпинга
    pass

class InvalidURL(ScrapingError): # Исключение для невалидных URL
    pass

class ConnectionFailed(ScrapingError): # Исключение для ошибок соединения
    pass

class NewsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    
    def validate_url(self, url): # Проверка валидности URL
        parsed = urlparse(url)
        if not all([parsed.scheme, parsed.netloc]):
            raise InvalidURL(f"Некорректный URL: {url}")
    
    def scrape_headlines(self, url, tag):
        try:
            self.validate_url(url)
            
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.find_all(tag)
            
            headlines = [elem.get_text(strip=True) for elem in elements if elem.get_text(strip=True)]
            
            if not headlines:
                raise ScrapingError("Не удалось найти заголовки на странице")
                
            return headlines
            
        except requests.exceptions.RequestException as e:
            raise ConnectionFailed(f"Ошибка соединения: {str(e)}")
        except Exception as e:
            raise ScrapingError(f"Ошибка при скрейпинге: {str(e)}")


class NewsScraperApp:
    def __init__(self):
        self.app = gui("Новостной Скрейпер", "600x500")
        self.scraper = NewsScraper()
        self.setup_gui()
    
    def setup_gui(self): # Настройка интерфейса
        self.app.setFont(size=12)
        
        # Основной интерфейс
        self.app.addLabel("url_label", "URL:")
        self.app.addEntry("url")
        
        self.app.addLabel("tag_label", "HTML-тег:")
        self.app.addEntry("tag")
        
        self.app.addButtons(["Получить заголовки"], self.scrape_news)
        
        self.app.addScrolledTextArea("output")
        self.app.setTextAreaHeight("output", 15)
        self.app.setTextAreaWidth("output", 70)
    
    def scrape_news(self, button): # Обработка кнопки для получения заголовков
        try:
            url = self.app.getEntry("url")
            tag = self.app.getEntry("tag")
            
            if not url:
                raise InvalidURL("Введите URL сайта")
            if not tag:
                raise ScrapingError("Укажите HTML-тег")
            
            headlines = self.scraper.scrape_headlines(url, tag)
            
            self.app.clearTextArea("output")
            self.app.setTextArea("output", "\n".join(f"{i+1}. {headline}" for i, headline in enumerate(headlines)))
            
        except ScrapingError as e:
            self.app.errorBox("Ошибка", str(e))
        except Exception as e:
            self.app.errorBox("Неизвестная ошибка", f"Произошла непредвиденная ошибка: {str(e)}")
    
    def run(self):
        self.app.go()


if __name__ == "__main__":
    app = NewsScraperApp()
    app.run()