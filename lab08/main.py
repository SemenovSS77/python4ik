from appJar import gui
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from abc import ABC, abstractmethod

class ScrapingError(Exception):
    pass

class InvalidURL(ScrapingError):
    pass

class ConnectionFailed(ScrapingError):
    pass

class BaseScraper(ABC):
    def __init__(self):
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
    
    @property
    def _headers(self):
        return self.__headers
    
    def _validate_url(self, url):
        parsed = urlparse(url)
        if not all([parsed.scheme, parsed.netloc]):
            raise InvalidURL(f"Некорректный URL: {url}")
    
    @abstractmethod
    def scrape_headlines(self, url, tag):
        pass

class NewsScraper(BaseScraper):
    def scrape_headlines(self, url, tag):
        try:
            self._validate_url(url)
            
            response = requests.get(url, headers=self._headers)
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
        self.__app = gui("Новостной Скрейпер", "600x500")
        self.__scraper = NewsScraper()
        self.__setup_gui()
    
    def __setup_gui(self):
        self.__app.setFont(size=12)
        
        self.__app.addLabel("url_label", "URL:")
        self.__app.addEntry("url")
        
        self.__app.addLabel("tag_label", "HTML-тег:")
        self.__app.addEntry("tag")
        
        self.__app.addButtons(["Получить заголовки"], self.__scrape_news)
        
        self.__app.addScrolledTextArea("output")
        self.__app.setTextAreaHeight("output", 15)
        self.__app.setTextAreaWidth("output", 70)
    
    def __scrape_news(self, button):
        try:
            url = self.__app.getEntry("url")
            tag = self.__app.getEntry("tag")
            
            if not url:
                raise InvalidURL("Введите URL сайта")
            if not tag:
                raise ScrapingError("Укажите HTML-тег")
            
            headlines = self.__scraper.scrape_headlines(url, tag)
            
            self.__app.clearTextArea("output")
            self.__app.setTextArea("output", "\n".join(f"{i+1}. {headline}" for i, headline in enumerate(headlines)))
            
        except ScrapingError as e:
            self.__app.errorBox("Ошибка", str(e))
        except Exception as e:
            self.__app.errorBox("Неизвестная ошибка", f"Произошла непредвиденная ошибка: {str(e)}")
    
    def run(self):
        self.__app.go()

if __name__ == "__main__":
    app = NewsScraperApp()
    app.run()