class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def open_deletion_window(self):
        self.app.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.deletion_window = self.app.application.window(title="Delete group")
        self.deletion_window.wait("visible")

    def del_group(self, group_name):
        self.open_group_editor()
        self.find_group_by_name(group_name)
        self.open_deletion_window()
        self.deletion_window.window(auto_id="uxDeleteAllRadioButton").click()
        self.deletion_window.window(auto_id="uxOKAddressButton").click()

    def find_group_by_name(self, group_name):
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        element = root.select(group_name)
        return element

