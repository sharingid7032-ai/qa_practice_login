from pathlib import Path
from playwright.sync_api import Page, expect

# 연습 앱 주소 (helpers.py와 같은 폴더의 practice_app.html)
APP_URL = (Path(__file__).parent / "practice_app.html").resolve().as_uri()


def login(page: Page):
    # 사전조건: admin으로 로그인
    page.goto(APP_URL)
    page.get_by_test_id("login-id").fill("admin")
    page.get_by_test_id("login-pw").fill("Test1234!")
    page.get_by_test_id("login-btn").click()


def add_user(page: Page, name, no):
    # 사용자 등록: 이름과 사번을 받아서 입력 후 저장
    page.get_by_test_id("user-name").fill(name)
    page.get_by_test_id("user-no").fill(no)
    page.get_by_test_id("save-btn").click()