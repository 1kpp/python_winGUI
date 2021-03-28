from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Users\\Shurygin_M\\Desktop\\test\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture