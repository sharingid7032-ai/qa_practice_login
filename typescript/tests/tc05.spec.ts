import { test, expect } from '@playwright/test';
import path from 'path';
import { pathToFileURL } from 'url';

// 연습 앱 주소: tests 폴더에서 두 칸 위(qa_practice_login)에 있는 practice_app.html
const APP_URL = pathToFileURL(path.join(__dirname, '..', '..', 'practice_app.html')).href;

test('TC-05 사용자 삭제', async ({ page }) => {
  // 1. 연습 앱 열기
  await page.goto(APP_URL);
  // 2. 아이디, 비밀번호 입력
  await page.getByTestId('login-id').fill('admin');
  await page.getByTestId('login-pw').fill('Test1234!');
  // 3. 로그인 버튼 클릭
  await page.getByTestId('login-btn').click();
  await expect(page.getByTestId('welcome')).toHaveText('admin님 환영합니다');

  await page.getByTestId('user-name').fill('홍길동');
  await page.getByTestId('user-no').fill('A001');
  await page.getByTestId('save-btn').click();

  await expect(page.getByTestId('user-row-A001')).toBeVisible();

  await page.getByTestId('delete-A001').click();   

  await expect(page.getByTestId('confirm-dialog')).toBeVisible();
  await expect(page.getByTestId('confirm-dialog')).toContainText('M-004');
  await expect(page.getByTestId('confirm-text')).toHaveText('삭제하시겠습니까?');

  await page.getByTestId('confirm-ok').click();   

  await expect(page.getByTestId('confirm-dialog')).toBeHidden();
  await expect(page.getByTestId('user-row-A001')).toHaveCount(0);

});