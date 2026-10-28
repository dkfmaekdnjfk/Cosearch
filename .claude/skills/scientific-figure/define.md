# 정의

- `scientific-figure`: 연구질문에 맞는 figure의 설계·제작·검수 스킬.
- `FIGURE_GUIDELINES.md`: 프로젝트가 관리하는 실험·표현 설정. 스킬은 루트 또는 `obsidian/00_Meta/`에서 확인한다.
- Gate 0–4: 제작 입력, 자료 무결성, 최종 크기 시각 검사, 출판 파일 검사, 읽기·독립 에이전트 검토의 진행 기준. 세부 판정은 `references/validation.md`를 따른다.
- `_figstyle.py`: 기존 Nature 디자인 시스템의 실행 모듈. 스킬은 `NATURE_RC`와 팔레트를 복제하지 않고 import한다.
- `preflight_pdf.arguments()`: 입력 PDF와 명시적인 검사 한계·렌더링 옵션을 읽는다.
- `preflight_pdf.inspect_page()`: 치수·텍스트·선·폰트·raster 정보를 수집하고 지정 기준 위반을 기록한다.
- `preflight_pdf.main()`: PDF를 읽고 JSON을 출력하며 필요한 경우 새 폴더에 PNG를 저장한다.
- 종료 코드: `0` 지정 기준 위반 미검출, `1` 위반 검출, `2` 실행 오류. 시각적·과학적 검증 완료 여부를 뜻하지 않는다.
- 검사 한계: 글자·선의 범위는 선택 인수다. 특정 저널의 규격은 기본값으로 강제하지 않는다.
