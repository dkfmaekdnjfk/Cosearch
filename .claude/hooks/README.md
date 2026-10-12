# Claude hooks

`answer_gate.py`는 매 프롬프트에 답변 질문을, `write_gate.py`는 이 프로젝트의
Obsidian Write/Edit 직전에 작성 질문을 `additionalContext`로 전달한다.
권한 결정을 변경하거나 도구를 차단하지 않는다. 기존 Stop 검사는 보존한다.

질문 정본은 `obsidian/00_Meta/ANSWER_GATES.md`, `WRITE_GATES.md`이다.
Claude 설정은 `.claude/settings.json`에 등록한다. Codex는 훅이 자동 실행되지 않으므로
같은 노트를 직접 읽는다. 게이트 노트 누락·읽기 실패·빈 본문은 조용히 통과한다.
작성 훅은 프로젝트 밖의 파일과 두 게이트 노트 자체 편집을 제외한다.

검증: 합성 JSON으로 답변/작성 컨텍스트, 비대상·잘못된 입력의 무출력을 확인한다.
