# scientific-figure

논문·연구 발표용 데이터 figure의 비교 설계, 제작, 자료·출력 검수를 수행한다.
작업 절차의 정본은 [SKILL.md](SKILL.md)다.

- [표현 선택](references/design.md): 관측 단위와 질문에 따른 그림·패널 구성.
- [제작 기준](references/production.md): 출력 크기, 색·선·범례, 디자인 시스템이 없는 경우의 시작값.
- [Nature 디자인 시스템 연계](references/nature-design-system.md): 저장소의 `code/scripts/_figstyle.py`를 직접 재사용한다. 별도 스킬이나 복제된 스타일 모듈을 만들지 않는다.
- [검수](references/validation.md): Gate 0–4, 자료·최종 이미지 대조, 독립 에이전트 검토, PDF 검사 실행법.
- [PDF 검사 스크립트](scripts/preflight_pdf.py): PyMuPDF 필요. 입력은 수정하지 않으며, 선택적으로 새 폴더에 PNG를 렌더링한다.
- [출처와 검증 범위](references/provenance.md).

Claude는 이 폴더를 사용한다. `.agents/skills/scientific-figure`는 같은 폴더를 가리키는 Codex용 상대 symlink다.
프로젝트의 `FIGURE_GUIDELINES.md`는 해당 프로젝트가 관리한다. 특정 실험의 데이터·지표·통계·팔레트는 포함하지 않는다.
