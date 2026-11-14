from playwright.sync_api import Page, expect
from helpers import login, add_user


def test_tc04_user_error(page: Page):
    login(page)

    add_user(page, "홍길동", "A001")
    expect(page.get_by_test_id("user-row-A001")).to_be_visible()

    add_user(page, "김철수", "A001")
    expect(page.get_by_test_id("user-error")).to_have_text("M-003 이미 등록된 사번입니다") 

    expect(page.get_by_test_id("user-table")).not_to_contain_text("김철수")
    expect(page.get_by_test_id("user-row-A001")).to_have_count(1)

