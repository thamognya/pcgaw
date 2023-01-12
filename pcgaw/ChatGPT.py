from selenium import webdriver

BASE_URL: str = "https://chat.openai.com/"

class ChatGPT:
    def __init__(self: "ChatGPT", session_token: str="", firefox: bool = True) -> None:
        self.__session_token: str = session_token

    @property    
    def session_token(self: "ChatGPT") -> str:
        return self.__session_token

    @session_token.setter
    def session_token(self: "ChatGPT", session_token) -> None:
        self.__session_token = session_token

    