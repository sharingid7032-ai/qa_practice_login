from pathlib import Path
from playwright.sync_api import Page, expect

# 테스트 파일과 같은 폴더에 있는 연습 앱 주소
APP_URL = (Path(__file__).parent / "practice_app.html").resolve().as_uri()


def test_tc02_login_fail(page: Page):
    # 1. 연습 앱 열기
    page.goto(APP_URL)
    # 2. 아이디, 비밀번호 입력
    page.get_by_test_id("login-id").fill("admin")
    page.get_by_test_id("login-pw").fill("Testtest1234!")
    # 3. 로그인 버튼 클릭
    page.get_by_test_id("login-btn").click()
    # 4. 기대 결과: 오류 문구 확인
    expect(page.get_by_test_id("login-error")).to_have_text("M-001 아이디 또는 비밀번호가 올바르지 않습니다") 
    expect(page.get_by_test_id("login-screen")).to_be_visible()
    expect(page.get_by_test_id("dashboard")).to_be_hidden()
