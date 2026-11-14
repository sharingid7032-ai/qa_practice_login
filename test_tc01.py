from pathlib import Path
from playwright.sync_api import Page, expect

# 테스트 파일과 같은 폴더에 있는 연습 앱 주소
APP_URL = (Path(__file__).parent / "practice_app.html").resolve().as_uri()


def test_tc01_login_success(page: Page):
    # 1. 연습 앱 열기
    page.goto(APP_URL)
    # 2. 아이디, 비밀번호 입력
    page.get_by_test_id("login-id").fill("admin")
    page.get_by_test_id("login-pw").fill("Test1234!")
    # 3. 로그인 버튼 클릭
    page.get_by_test_id("login-btn").click()
    # 4. 기대 결과: 환영 문구 확인
    expect(page.get_by_test_id("welcome")).to_have_text("admin님 환영합니다")
