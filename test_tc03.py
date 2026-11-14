from playwright.sync_api import Page, expect
from helpers import login, add_user


def test_tc03_user_register(page: Page):

    login(page)
    add_user(page, "홍길동", "A001")


    expect(page.get_by_test_id("user-row-A001")).to_contain_text("홍길동")
    expect(page.get_by_test_id("user-row-A001")).to_contain_text("A001")

    expect(page.get_by_test_id("user-error")).to_be_hidden()
