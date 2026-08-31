# Source policy

## Hebcal

Use Hebcal as the calendar authority for:
- Daf Yomi date assignment
- Hebrew date
- Jewish holiday/fast/Rosh Chodesh/special-Shabbat context
- forward Daf assignments used to determine the end of a masechet

Hebcal's public web APIs require no registration or API key. Attribute Hebcal when presenting data substantially derived from its API.

## Sefaria

Use Sefaria's current public Texts API for source grounding. Prefer the v3 Texts endpoint.

Use source retrieval selectively:
- Gemara: verify the actual daf before summarizing.
- Rashi/Tosafot: retrieve the relevant commentary when discussing a specific comment.
- Aramaic: use reference/dictionary resources for unusual or ambiguous terms when feasible.

Do not reproduce long copyrighted translations. Summarize and quote only brief phrases when needed.

## Failure behavior

If network access fails:
1. Do not make up an API result.
2. If the daf/date can still be determined reliably from the host agent's trusted tools, continue.
3. Otherwise say which part could not be verified.
4. A failed Sefaria lookup should not automatically prevent a lesson if the underlying text can be reliably accessed another way.
