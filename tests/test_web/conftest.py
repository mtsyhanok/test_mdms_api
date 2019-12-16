from pytest import fixture


@fixture(scope='function', autouse=True)
def setup_page(request):
    page = request.module.page
    page.open()
    yield


@fixture(scope='module', autouse=True)
def close_page(request):
    page = request.module.page
    yield
    page.close()
