class Story(object):
    def __init__(self, pages:list[str]) -> None:
        self.__pages:list[str] = pages
        self.__page_length:int = len(self.__pages)
        self.__now_page:int = 0

    def goto_pre_page(self):
        self.__now_page = (self.__now_page-1) if self.__now_page > 0 else self.__page_length-1

    def goto_next_page(self):
        self.__now_page = (self.__now_page+1) if self.__now_page < self.__page_length-1 else 0

    @property
    def this_page(self) -> str:
        return self.__pages[self.__now_page]
