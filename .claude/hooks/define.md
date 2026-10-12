# Hook definitions

- `PROJECT_ROOT`: 훅 파일 위치로 정한 프로젝트 루트; CWD와 무관.
- `read_gate(name)`: frontmatter·소개·유지 관리 절을 제외한 질문 본문.
- `emit_context(event, name)`: `hookSpecificOutput.additionalContext` JSON 출력.
- `write_gate.main()`: payload 및 실제 경로 검증 후 프로젝트 vault에만 적용.
- `check_memory_update.py`: 기존 Stop용 메모리/현황/EXP 검사; 이번 변경 대상 아님.
