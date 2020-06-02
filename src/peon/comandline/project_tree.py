import os


class ProjectTree:

    # TODO: fill from config
    DEFAULT_EXCLUDE_FOLDERS = ('build', 'venv')

    def __init__(
            self,
            path_to_project: list,
    ):
        self.path_to_project = path_to_project

    def inspect(self) -> list:

        list_of_files = []

        # get list of abs paths from input args
        args_abs_path = []
        for path in self.path_to_project:
            args_abs_path.append(os.path.abspath(path))

        # iterate over every path
        for path in args_abs_path:

            # if path is py file - append
            if path.endswith('.py'):
                list_of_files.append(path)
                continue

            # if path is not directory - skip
            elif not os.path.isdir(path):
                continue

            # get list of files from directory
            listdir = os.listdir(path)
            files = []
            for entry in listdir:
                files.append(os.path.join(path, entry))

            list_of_files = list_of_files + ProjectTree(files).inspect()

        filtered_files = []
        for file in list_of_files:
            if 'venv' in file:
                continue
            elif 'build' in file:
                continue
            else:
                filtered_files.append(file)

        return filtered_files







        #     if 'venv' in path:
        #         continue
        #     elif 'build' in path:
        #         continue
        #
        #     # if only single file
        #     if path.endswith('.py'):
        #         list_of_files_to_check.append(path)
        #         continue
        #
        #     list_Of_files = os.listdir(project_abs_path)
        #
        #     # Iterate over all the entries
        #     for entry in list_Of_files:
        #
        #         # Create full path
        #         fullPath = os.path.join(project_abs_path, entry)
        #
        #         # If entry is a directory then get the list of files in this directory
        #         if os.path.isdir(fullPath):
        #             allFiles = allFiles + ProjectTree(fullPath).inspect()
        #         else:
        #             if fullPath.endswith('.py'):
        #                 allFiles.append(fullPath)
        #
        # for path in allFiles:
        #     if path not in list_of_files_to_check:
        #         list_of_files_to_check.append(path)
        #
        # return list_of_files_to_check
