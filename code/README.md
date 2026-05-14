# code/

분석에 사용되는 모든 코드. 패키지, 실행 스크립트, 유틸리티.

## 폴더 구조

| 폴더 | 역할 |
|------|------|
| `cosearch/` | Cosearch 프레임워크 패키지 (경로 관리 등) |
| `scripts/` | 실행 스크립트 모음 |
| `notebooks/` | 탐색적 분석용 Jupyter 노트북 |
| `pipelines/` | 파이프라인 설정 파일 (*.yaml) |
| `tests/` | 테스트 코드 |
| `legacy/` | 이전 코드 보관 (참조용, 수정 금지) |

## ⚠️ Import 주의사항

프로젝트마다 패키지 구조가 다를 수 있음. 레포 루트에서 실행 시:

```bash
# 방법 1: 환경변수
PYTHONPATH=code python code/scripts/run_example.py

# 방법 2: 스크립트 내부
import sys
sys.path.insert(0, 'code')
```
