import os


class ProjectTree:

    def __init__(
            self,
            path_to_project: str
    ):
        self.path_to_project = path_to_project

    def inspect(self) -> list:

        project_abs_path = os.path.abspath(self.path_to_project)
        list_Of_files = os.listdir(project_abs_path)
        # print(list_Of_files)
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

        return allFiles
