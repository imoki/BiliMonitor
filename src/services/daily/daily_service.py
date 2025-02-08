from ...views.prompt_view import PromptView
from ...views.table_view import TableView

class DailyService():
    def __init__(self, **kwargs):
        self.parent = kwargs.get('parent', '')
        self.key = kwargs.get('key', '')
        self.unique = kwargs.get('unique', '')
        self.table = kwargs.get('table', '')
        self.configManager = kwargs.get('configManager', '')
        self.rowCount = 10
        self.prompt_view= PromptView(self.parent)