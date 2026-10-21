# 문장별 작성 의도 검토 문서

한 문장씩 검토하며 본문을 누적하고, 표현별 뜻과 작성 의도를 연결하는 독립 HTML을 제작한다.
특정 연구 분야의 문장·자료·가설·로컬 경로는 포함하지 않는다.

- 사용 조건·작성 절차: [SKILL.md](SKILL.md)
- 현재 두 패널 디자인과 양방향 연결: [assets/sentence-review.html](assets/sentence-review.html)
- HTML 구조·함수·변수: [define.md](define.md)
- Codex 표시 정보: [agents/openai.yaml](agents/openai.yaml)

예문은 템플릿 동작을 보여 주기 위한 문장이다. 실제 문서에는 사용자와 검토한 내용만 반영한다.
Claude 정본은 `.claude/skills/sentence-intent-document/`이며, Cosearch의
`.agents/skills/sentence-intent-document`는 같은 폴더를 가리키는 상대 symlink다.
