import os


class ProjectTree:

    # TODO: вынести это проверкой в отдельный класс и вообще забирать из конфига
    DEFAULT_EXCLUDE_FOLDERS = ['build', 'venv']

    def __init__(
            self,
            path_to_project: str,
    ):
        self.path_to_project = path_to_project

    def inspect(self) -> list:

        if isinstance(self.path_to_project, list):
            files_to_check = []

            for file in self.path_to_project:
                if not file.endswith('.py'):
                    continue
                files_to_check.append(os.path.abspath(file))
            return files_to_check

        project_abs_path = os.path.abspath(self.path_to_project)

        # if only single file
        if len(self.path_to_project) > 2 and self.path_to_project[-3:] == '.py':
            return [project_abs_path]

        list_Of_files = os.listdir(project_abs_path)
        allFiles = list()

        # Iterate over all the entries
        for entry in list_Of_files:

            # Create full path
            fullPath = os.path.join(project_abs_path, entry)

            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(fullPath):
                allFiles = allFiles + ProjectTree(fullPath).inspect()
            else:
                file_extension = fullPath.split('.')[-1]
                if file_extension == 'py':
                    allFiles.append(fullPath)

        files_to_check = []
        for path in allFiles:
            if 'venv' in path:
                continue
            elif 'build' in path:
                continue
            else:
                files_to_check.append(path)

        return files_to_check
