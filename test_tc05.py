from playwright.sync_api import Page, expect
from helpers import login, add_user


def test_tc05_user_delete(page: Page):

    login(page)

    add_user(page, "홍길동", "A001")
    expect(page.get_by_test_id("user-row-A001")).to_be_visible()


    page.get_by_test_id("delete-A001").click()

    expect(page.get_by_test_id("confirm-dialog")).to_be_visible() 
    expect(page.get_by_test_id("confirm-dialog")).to_contain_text("M-004") 
    expect(page.get_by_test_id("confirm-text")).to_have_text("삭제하시겠습니까?") 

    page.get_by_test_id("confirm-ok").click()

    expect(page.get_by_test_id("confirm-dialog")).to_be_hidden()
    expect(page.get_by_test_id("user-row-A001")).to_have_count(0)



