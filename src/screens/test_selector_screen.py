import PySimpleGUI as sg

from src.db.projects_data import ProjectsData
from src.tests.validator_test import ValidatorTest
from src.tests.yoksel_test import YokselTest


class TestSelectorScreen:
    @staticmethod
    def run(project_name, pages):
        project = ProjectsData.get(project_name)
        sg.theme('DarkAmber')
        layout = [[sg.Text('Select tests for the project ' + str(project_name))],
                  [sg.HorizontalSeparator()],
                  [sg.Checkbox(text='Validator')],
                  [sg.Checkbox(text='Yoksel')],
                  [sg.HorizontalSeparator()],
                  [sg.Button('Run tests')],
                  # [sg.Output(size=(60,15))]
                  ]

        window = sg.Window('Tests', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Run tests':
                if values[1]:
                    urls = []
                    for page_name in pages:
                        urls.append(str(project['url']) + str(pages[page_name]['url']))
                    ValidatorTest.run(urls)
                if values[2]:
                    urls = []
                    for page_name in pages:
                        urls.append(str(project['url']) + str(pages[page_name]['url']))
                    YokselTest.run(urls)

        window.close()

