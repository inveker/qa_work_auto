import PySimpleGUI as sg

from src.db.projects_data import ProjectsData
from src.screens.test_selector_screen import TestSelectorScreen
from src.utils.http import HttpUtils


class PagesScreen:
    @staticmethod
    def run(project_name):

        project = ProjectsData.get(project_name)

        pages = HttpUtils.pages(project['url'])

        sg.theme('DarkAmber')
        layout = [[sg.Text('Select pages:')],
                  [sg.HorizontalSeparator()]]

        for page_name in pages:
            layout.append([sg.Checkbox(text=page_name, key=page_name)])

        layout.append([sg.Button('Next')])

        window = sg.Window('Projects', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Next':
                selected_pages = {}
                for page_name in values:
                    if(values[page_name]):
                        selected_pages[page_name] = pages[page_name]
                TestSelectorScreen.run(project_name, selected_pages)

        window.close()

