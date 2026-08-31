# Source policy

## Hebcal

Use Hebcal only for calendar-aware Yomi mode:

- Daf Yomi date assignment
- Hebrew date
- Jewish holiday, fast, Rosh Chodesh, and special-Shabbat context
- forward assignments used to determine masechet completion, the next masechet, and cycle progress

Do not use the current Daf Yomi assignment to replace or reinterpret an exact-daf request. Hebcal's public web APIs require no registration or API key. Attribute Hebcal when presenting data substantially derived from its API.

## Sefaria

Use Sefaria's current public Texts API for source grounding in both modes. Prefer the v3 Texts endpoint.

Use source retrieval selectively:

- Gemara: verify the exact daf or amud before summarizing it.
- Mishnah: retrieve the requested portion when it appears on the page.
- Rashi/Tosafot: retrieve the relevant commentary before discussing a specific comment.
- Aramaic: use reference or dictionary resources for unusual or ambiguous terms when feasible.

For exact-daf mode, preserve the user's requested scope. Do not silently expand `23b` to the entire daf or substitute today's assignment.

For an exact range such as `Chullin 23a-33b`, retrieve the inclusive range in reliable chunks when necessary. Verify every summarized sugya against material inside the requested boundaries. Do not attach Daf Yomi calendar or progress data to the range.

When `rashi` or `tosafot` focus is requested, retrieve the selected comments before explaining them. On a long range, prioritize comments that clarify a major textual, logical, conceptual, or halachic issue rather than claiming to exhaust every comment.

Do not reproduce long copyrighted translations. Summarize and quote only brief phrases when needed.

## Failure behavior

If network access fails:

1. Do not make up an API result.
2. If the requested reference or Yomi assignment can still be determined reliably from trusted host tools, continue.
3. Otherwise state which part could not be verified.
4. A failed Sefaria lookup does not automatically prevent a lesson if the underlying text is reliably available another way.
5. A failed Hebcal lookup affects Yomi calendar resolution, not a valid exact-daf request.
