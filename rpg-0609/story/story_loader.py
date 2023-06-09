from . import story

class StoryLoader(object):
    def __init__(self) -> None:
        pass

    def load(self, story_type:str, story_chapter:str, story_id:str) -> story.Story:
        with open(file=f"./rpg/data/stories/{story_type}/{story_chapter}/{story_id}.txt", mode='r', encoding="utf8") as file:
            return story.Story(pages=[p for p in [page.replace('\n', '') for page in file.readlines()] if p != ''])