from pageobject.page.App import App

class TestSelected(object):
    def test_price(self):
        assert App.main().gotoselected().getPriceByName("苏宁易购") == 11.22

    def test_search(self):
        assert App.main().gotosearch().search("alibaba").isInSelected("BABA") == False
