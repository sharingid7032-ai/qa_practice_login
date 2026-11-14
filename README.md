# 출입 관리 연습 웹앱 TC 자동화 (개인 학습)

연습용으로 만든 가상의 로그인 상황 TC 5건을 Playwright(Python)와 pytest로 자동화했습니다.
요구사항과 메시지 번호(M-001 등)는 학습을 위해 직접 만든 가상 사양입니다.

## 파일 구성
| 파일 | 내용 |
|---|---|
| practice_app.html | 테스트 대상 연습용 웹앱 (로그인, 사용자 등록·삭제) |
| TC_출입관리_연습.xlsx | TC 5건 (TC 이름, 목적, 사전조건, Step, 기대 결과) |
| helpers.py | 여러 TC에서 쓰는 공통 단계 (로그인, 사용자 등록) |
| test_tc01.py ~ test_tc05.py | TC별 자동화 코드 |

## TC 목록
| TC | 내용 |
|---|---|
| TC-01 | 정상 로그인 |
| TC-02 | 잘못된 비밀번호 → M-001 표시 |
| TC-03 | 사용자 정상 등록 |
| TC-04 | 사번 중복 등록 → M-003 표시 |
| TC-05 | 삭제 확인 팝업(M-004) → 사용자 삭제 |

## 실행 방법
```
pip install pytest-playwright
python -m playwright install chromium
python -m pytest                          # 전체 실행
python -m pytest --headed --slowmo 700    # 브라우저 화면을 보면서 천천히 실행
```

실행 환경: Windows, Python 3.15, Playwright 1.63, pytest 9.1

## 작업하며 정리한 것
- TC 기대 결과에 적은 확인 시점(Step 1 후, Step 3 후)에 맞춰 expect 위치를 정했습니다.
- FAIL이 나면 로그의 Expected와 Actual을 먼저 비교해 앱 결함인지 테스트 오류인지 구분했습니다. (TC-02: 기대값에 알림 번호 M-001 누락)
- 문구 검사만으로는 숨겨진 팝업도 PASS가 나와서, 화면 표시 확인(to_be_visible)을 함께 넣었습니다. (TC-05)
- 각 TC가 필요한 데이터를 스스로 준비하게 해서 실행 순서와 관계없이 동작하게 했습니다.
- 반복되는 로그인·등록 단계(사전조건)를 helpers.py로 분리했습니다.