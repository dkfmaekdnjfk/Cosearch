# results/

코드 실행으로 생성된 결과물.

## 폴더 구조

| 폴더 | 역할 | Git |
|------|------|-----|
| `final/` | 논문·보고서용 최종 그림·표 | ✅ 추적 |
| `logs/` | 실행 로그 | ❌ 로컬 전용 |
| `tmp/` | 임시 출력물 | ❌ 로컬 전용 |

## 규칙

- 새 분석 결과는 `tmp/` 또는 날짜 기반 경로에 먼저 저장
- 논문·발표에 쓸 최종본만 `final/`로 이동
- 모든 결과물은 생성한 EXP 노트에 경로·커맨드 기록
- 새로 생긴 대용량 결과물은 `artifacts/manifest.yaml`에 추가

## EXP 노트 연결 예시

```markdown
## Command
```bash
PYTHONPATH=code python code/scripts/run_example.py
```

## Output
- Tracked: `results/final/summary.png`
- Local only: `results/tmp/260514_topic/`
```
