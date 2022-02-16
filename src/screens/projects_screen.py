import PySimpleGUI as sg

from src.db.projects_data import ProjectsData
from src.screens.pages_screen import PagesScreen


class ProjectsScreen:
    @staticmethod
    def run():

        projects = ProjectsData.all()

        sg.theme('DarkAmber')
        layout = [[sg.Text('Welcome! Add new project or select exists.')],
                  [sg.HorizontalSeparator()],
                  [sg.Text('Add project')],
                  [sg.Text('Set project url:'), sg.InputText(), sg.Button('Add')],
                  [sg.HorizontalSeparator()]]

        for project_name in projects:
            layout.append([sg.Button(project_name)])

        window = sg.Window('Projects', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if event == 'Add':
                ProjectsData.add(values[1])
            if projects.get(event):
                PagesScreen.run(event)

        window.close()

