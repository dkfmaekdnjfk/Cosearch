# data/

분석에 사용되는 입력 데이터.

## 폴더 구조

| 폴더 | 역할 | Git |
|------|------|-----|
| `examples/` | 소형 예시 데이터 (테스트·재현용) | ✅ 추적 |
| `raw/` | 원본 데이터 | ❌ 로컬 전용 |
| `processed/` | 전처리 완료 데이터 | ❌ 로컬 전용 |
| `legacy/` | cosearch 도입 이전 데이터 아카이브 (읽기 전용) | ❌ 로컬 전용 |

## 규칙

- `raw/`, `processed/` 안의 파일은 Git에 올리지 않음
- Git 밖 파일의 위치·출처는 `artifacts/manifest.yaml`에 기록
- 작은 샘플·예시는 `examples/`에 넣고 Git 추적 가능
