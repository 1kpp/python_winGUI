
def test_add_group(app):
    old_list = app.groups.get_group_list()
    new_group = "new Group 4"
    app.groups.add_new_group(new_group)
    new_list = app.groups.get_group_list()
    old_list.append(new_group)
    assert sorted(old_list) == sorted(new_list)
